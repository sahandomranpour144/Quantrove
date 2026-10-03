"""
Reusable long-form kinetic keyword overlay (CapCut Track V2).
Adapted from EP05 generate_full_kinetic_overlay.py (card look, easing, slots, qtrle RGBA).

Inputs : script .md (per-scene `KEYWORDS:` line), words.json (faster-whisper all_words), master timeline .json
Output : 1920x1080 60 fps QuickTime RLE (argb, alpha) MOV, full timeline length; manifest JSON; optional 2x2 preview PNG

Usage:
  python kinetic_overlay.py --script EP07_SCRIPT_AND_SHOTLIST.md --words EP07_words.json \
      --timeline EP07_MASTER_TIMELINE.json --out 00_OVERLAY_EP07_kinetic_word_pops_60fps.mov \
      [--manifest m.json] [--preview p.png] [--plan-only]

Timing: each keyword pops at the start of its spoken words (phrase match inside the scene's time range);
if not spoken verbatim, at the first spoken keyword token (prefix match); else spread evenly over the scene.
Nothing is placed inside the final END_CLEAR_S seconds (end-screen).
"""
import argparse
import json
import math
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[3]  # workspace root
CONTRACT = json.loads((Path(__file__).parent / "config" / "layout_contract.json").read_text(encoding="utf-8"))["long_form"]
W, H, FPS = 1920, 1080, 60
END_CLEAR_S = 20.0
HOLD_S, MIN_HOLD_S, GAP_S, LEAD_S = 2.4, 1.0, 0.05, 0.08
POP_S, FADE_S = 0.22, 0.14
FONT_MAX, FONT_FLOOR = CONTRACT["popup_box"]["font_size_max"], 34
CARD_MAX_W = CONTRACT["popup_box"]["max_width"] - 20  # 540: margin under the 560 contract
PAD_X, PAD_Y = 28, 16

PILL_FILL = (34, 32, 34, 204)    # #222022 @ 80%
BORDER = (35, 61, 76, 255)       # #233D4C 1px
LIME = (195, 216, 9, 255)        # #C3D809
PUMPKIN = (253, 128, 46, 255)    # #FD802E
WHITE = (230, 237, 243, 255)     # #E6EDF3
HEX = {LIME: "#C3D809", PUMPKIN: "#FD802E", WHITE: "#E6EDF3"}

RISK = ["BROKE", "FAILED", "SLOWER", "LESS ", "COST", "CHARGED", "NOT ", "NOBODY", "FADE", "SQUEEZED", "BOTTLENECK",
        "IDLE", "HOMEMAKER", "SAME DISTANCE", "SIMILARITY = 0", "TWO MEANINGS", "≠", "BAD MEMORY", "4×", "STILL STEP",
        "LEARNED FROM US", "MORE RULES", "WHAT ELSE", "DELETE THE CHAIN", "MIRROR"]
STOP = {"the", "a", "an", "of", "is", "it", "to", "in", "on", "and", "or", "for", "by", "as", "at", "with", "what",
        "not", "no", "one", "all", "every", "same", "more", "than", "was", "did", "they", "its", "be"}
NUMW = {w: str(i) for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve".split())}

NOHEMI = str(ROOT / "assets" / "fonts" / "Nohemi-Bold.ttf")
FALLBACK = "C:/Windows/Fonts/segoeuib.ttf"


def norm(s):
    s = re.sub(r"[^0-9a-z]", "", s.lower().replace("’", "'").replace("'", ""))
    return NUMW.get(s, s)


# ---------------------------------------------------------------- inputs
def parse_keywords(script_text):
    out, cur = {}, None
    for line in script_text.splitlines():
        m = re.match(r"\*\*Scene (\d+) —", line)
        if m:
            cur = int(m.group(1))
        elif line.startswith("KEYWORDS:") and cur is not None:
            body = line[len("KEYWORDS:"):].strip()
            out[cur] = [] if body.lower().startswith("none") else [k.strip() for k in body.split(" | ") if k.strip()]
    return out


def find_anchor(kw, words, after, override=None):
    """words: [(norm, start)] for one scene. Returns (time, method)."""
    stream, starts, ends = "", {}, {}
    for i, (n, _) in enumerate(words):
        starts[len(stream)] = i
        stream += n
        ends[len(stream)] = i

    def hits(target):  # boundary-aligned matches in the joined stream (handles whisper "50 ,257")
        out, pos = [], stream.find(target) if target else -1
        while pos != -1:
            if pos in starts and pos + len(target) in ends:
                out.append(words[starts[pos]][1])
            pos = stream.find(target, pos + 1)
        return out

    def pick(ts):
        later = [t for t in ts if t >= after]
        return (later or ts)[0]

    if override:
        ts = [s for n, s in words if n.startswith(norm(override))]
        if ts:
            return pick(ts), f"anchor:{override}"
    toks = [t for t in (norm(x) for x in re.split(r"[\s\-–—/·]+", kw)) if t]
    ts = hits("".join(toks))
    if ts:
        return pick(ts), "phrase"
    content = sorted([t for t in toks if t not in STOP] or toks, key=len, reverse=True)  # most specific first
    for t in content:
        ts = hits(t) or ([] if len(t) < 4 or t.isdigit() else [s for n, s in words if n.startswith(t[:5])])
        if ts:
            return pick(ts), f"token:{t}"
    return None, "none"


def plan(script, words_json, timeline, anchors=None):
    kws = parse_keywords(Path(script).read_text(encoding="utf-8"))
    words = json.loads(Path(words_json).read_text(encoding="utf-8"))["all_words"]
    tl = json.loads(Path(timeline).read_text(encoding="utf-8"))
    total = tl["total_duration_s"]
    end_clear = total - END_CLEAR_S
    pops, log = [], []
    for sc in tl["scenes"]:
        klist = kws.get(sc["scene"], [])
        sw = [(norm(w["word"]), w["start"]) for w in words if sc["start"] <= w["start"] < sc["end"]]
        sw = [x for x in sw if x[0]]
        after = sc["start"]
        for i, kw in enumerate(klist):
            t, how = find_anchor(kw, sw, after, (anchors or {}).get(kw))
            if t is None:
                t, how = sc["start"] + (i + 0.5) / len(klist) * (sc["end"] - sc["start"]), "fallback:even"
            after = t
            pops.append({"text": kw, "anchor": round(t, 3), "scene": sc["scene"], "engine": sc["engine"], "method": how})
    pops.sort(key=lambda p: p["anchor"])
    # timing: lead-in, min spacing, hold, end-screen clearance
    prev_start = -9.0
    for p in pops:
        p["start"] = max(p["anchor"] - LEAD_S, prev_start + MIN_HOLD_S + GAP_S)
        prev_start = p["start"]
    for i, p in enumerate(pops):
        nxt = pops[i + 1]["start"] - GAP_S if i + 1 < len(pops) else 1e9
        p["end"] = min(p["start"] + HOLD_S, nxt, end_clear - GAP_S)
    kept = [p for p in pops if p["end"] - p["start"] >= MIN_HOLD_S * 0.9]
    for p in pops:
        if p not in kept:
            log.append(f"DROPPED {p['text']!r} (no room before end-screen {end_clear:.2f}s)")
    # color, style, slot (LRU, never the same slot twice in a row)
    last_used, prev = {}, None
    for i, p in enumerate(kept):
        up = p["text"].upper() + " "
        p["color"] = PUMPKIN if any(r in up for r in RISK) else (WHITE if re.search(r"\d", up) else LIME)
        p["style"] = "glow" if i % 2 == 0 else "badge"
        cands = ["TL", "TR", "ML", "MR"] if p["engine"].lower() == "flow" else ["TL", "TC", "TR"]
        slot = min([c for c in cands if c != prev], key=lambda c: last_used.get(c, -1))
        last_used[slot], prev = i, slot
        p["slot"] = slot
    return kept, total, log


# ---------------------------------------------------------------- cards
_cmap = None


def has_glyph(ch):
    global _cmap
    if _cmap is None:
        try:
            from fontTools.ttLib import TTFont
            _cmap = set(TTFont(NOHEMI).getBestCmap().keys())
        except Exception:
            _cmap = set(range(32, 127))
    return ord(ch) in _cmap


def runs(text):
    out = []
    for ch in text:
        f = NOHEMI if (has_glyph(ch) or ch == " ") else FALLBACK
        if out and out[-1][1] == f:
            out[-1][0] += ch
        else:
            out.append([ch, f])
    return out


def measure(text, size):
    x, top, bot, parts = 0.0, 0, 0, []
    for s, f in runs(text):
        font = ImageFont.truetype(f, size)
        b = font.getbbox(s, anchor="ls")
        top, bot = min(top, b[1]), max(bot, b[3])
        parts.append((s, font, x))
        x += font.getlength(s)
    return x, top, bot, parts


def render_card(text, color, style):
    """Single line 72->56 px; else two balanced lines (largest size fitting 560x110 contract); else shrink 1 line."""
    MAXH = CONTRACT["popup_box"]["max_height"]
    lines, size, pad_y = [text], FONT_MAX, PAD_Y
    for sz in range(FONT_MAX, CONTRACT["popup_box"]["font_size_min"] - 1, -1):
        if measure(text, sz)[0] + 2 * PAD_X <= CARD_MAX_W:
            size = sz
            break
    else:
        toks = text.split(" ")
        splits = [(" ".join(toks[:i]), " ".join(toks[i:])) for i in range(1, len(toks))]
        done = False
        for sz in range(CONTRACT["popup_box"]["font_size_min"], 29, -1):
            lh = int(sz * 1.08)
            for l1, l2 in sorted(splits, key=lambda p: abs(len(p[0]) - len(p[1]))):
                if max(measure(l1, sz)[0], measure(l2, sz)[0]) + 2 * PAD_X <= CARD_MAX_W and int(0.92 * sz) + lh + 2 * 12 <= MAXH:
                    lines, size, pad_y, done = [l1, l2], sz, 12, True
                    break
            if done:
                break
        if not done:
            size = FONT_MAX
            while measure(text, size)[0] + 2 * PAD_X > CARD_MAX_W and size > FONT_FLOOR:
                size -= 1
    ms = [measure(l, size) for l in lines]
    lh = int(size * 1.08)
    tw = max(m[0] for m in ms)
    top, bot = min(m[1] for m in ms), max(m[2] for m in ms)
    cw = int(math.ceil(tw + 2 * PAD_X))
    ch = int(bot - top + 2 * pad_y + (len(lines) - 1) * lh)
    card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, cw - 1, ch - 1], radius=14, fill=PILL_FILL, outline=BORDER, width=1)
    for li, (lw, _, _, parts) in enumerate(ms):
        ox = (tw - lw) / 2
        for s, font, x in parts:
            d.text((PAD_X + ox + x, pad_y - top + li * lh), s, fill=color, font=font, anchor="ls")
    if style == "glow":
        g = Image.new("RGBA", (cw + 24, ch + 24), (0, 0, 0, 0))
        ImageDraw.Draw(g).rounded_rectangle([12, 12, cw + 12, ch + 12], radius=16, fill=color[:3] + (50,))
        g = g.filter(ImageFilter.GaussianBlur(8))
        g.alpha_composite(card, (12, 12))
        card = g
    return card, (cw, ch), size


def place(slot, cw, ch):
    band_y = (CONTRACT["manim_popup_band"]["ymin"] + CONTRACT["manim_popup_band"]["ymax"]) // 2  # 116
    xl, xr = CONTRACT["manim_stage"]["xmin"], CONTRACT["manim_stage"]["xmax"]
    cx = {"TL": xl + cw // 2, "TC": W // 2, "TR": xr - cw // 2, "ML": xl + cw // 2, "MR": xr - cw // 2}[slot]
    cy = 540 if slot in ("ML", "MR") else band_y
    return cx, cy, [cx - cw // 2, cy - ch // 2, cx - cw // 2 + cw, cy - ch // 2 + ch]


def ease_out_back(t, s=1.70158):
    t = max(0.0, min(1.0, t)) - 1.0
    return t * t * ((s + 1.0) * t + s) + 1.0


def frame_at(t, pops, cards, base=None):
    frame = base.copy() if base is not None else Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for p in pops:
        if not (p["start"] <= t <= p["end"]):
            continue
        card = cards[id(p)]
        el, rem = t - p["start"], p["end"] - t
        if el < POP_S:
            scale, alpha = 0.40 + 0.60 * ease_out_back(el / POP_S), min(1.0, el / 0.08)
        elif rem < FADE_S:
            q = rem / FADE_S
            scale, alpha = 1.0 + 0.05 * (1.0 - q), q * (2 - q)
        else:
            scale, alpha = 1.0, 1.0
        tw, th = max(1, int(card.width * scale)), max(1, int(card.height * scale))
        c = card.resize((tw, th), Image.Resampling.BILINEAR) if (tw, th) != card.size else card
        if alpha < 0.99:
            r, g, b, a = c.split()
            c = Image.merge("RGBA", (r, g, b, a.point(lambda v: int(v * alpha))))
        cx, cy = p["pos"]
        frame.alpha_composite(c, (cx - tw // 2, cy - th // 2))
    return frame


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--words", required=True)
    ap.add_argument("--timeline", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--manifest")
    ap.add_argument("--preview")
    ap.add_argument("--anchors", help='JSON {"KEYWORD": "spoken word"} for keywords not spoken verbatim')
    ap.add_argument("--plan-only", action="store_true")
    a = ap.parse_args()

    anchors = json.loads(Path(a.anchors).read_text(encoding="utf-8")) if a.anchors else None
    pops, total, log = plan(a.script, a.words, a.timeline, anchors)
    cards = {}
    for p in pops:
        card, (cw, ch), size = render_card(p["text"], p["color"], p["style"])
        cx, cy, bbox = place(p["slot"], cw, ch)
        cards[id(p)], p["pos"], p["bbox"], p["font_px"] = card, (cx, cy), bbox, size
        if size < CONTRACT["popup_box"]["font_size_min"]:
            log.append(f"FONT {size}px < contract min {p['text']!r} (2-line wrap to fit 560x110)")
        if ch > CONTRACT["popup_box"]["max_height"]:
            log.append(f"HEIGHT {ch}px > 110 for {p['text']!r}")
    for p in pops:
        log.append(f"{p['start']:8.2f}-{p['end']:7.2f}  sc{p['scene']:02d} {p['slot']}  {p['method']:<18} {p['text']}")

    manifest = Path(a.manifest or Path(a.out).with_suffix(".manifest.json"))
    manifest.write_text(json.dumps([{"word": p["text"], "start": round(p["start"], 3), "end": round(p["end"], 3),
                                     "anchor": p["anchor"], "method": p["method"], "scene": p["scene"],
                                     "slot": p["slot"], "bbox": p["bbox"], "font_px": p["font_px"],
                                     "color": HEX[p["color"]], "scene_type": p["engine"]} for p in pops], indent=1),
                        encoding="utf-8")
    print("\n".join(log))
    print(f"{len(pops)} pops · total {total}s · manifest {manifest}")

    if a.preview:
        picks = [pops[int(i * (len(pops) - 1) / 3)] for i in range(4)]
        bg = Image.new("RGBA", (W, H), (0x20, 0x23, 0x22, 255))
        tiles = [frame_at(p["start"] + 0.6, pops, cards, bg).convert("RGB").resize((960, 540)) for p in picks]
        sheet = Image.new("RGB", (1920, 1080))
        for i, t in enumerate(tiles):
            sheet.paste(t, ((i % 2) * 960, (i // 2) * 540))
        sheet.save(a.preview)
        print(f"preview {a.preview} at t = {[round(p['start'] + 0.6, 2) for p in picks]}")
    if a.plan_only:
        return

    n = round(total * FPS)
    proc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-c:v", "qtrle", "-pix_fmt", "argb", a.out], stdin=subprocess.PIPE)
    empty = bytes(W * H * 4)
    for f in range(n):
        t = f / FPS
        active = any(p["start"] <= t <= p["end"] for p in pops)
        proc.stdin.write(frame_at(t, pops, cards).tobytes() if active else empty)
    proc.stdin.close()
    proc.wait()
    print(f"wrote {a.out} ({n} frames)")


if __name__ == "__main__":
    # self-check: phrase match across whisper-split numbers, token fallback, number words
    _w = [(norm(x), i) for i, x in enumerate(["They", "used", "50", ",257", "slots,", "six", "rules", "king"])]
    assert find_anchor("50,257 SLOTS", _w, 0) == (2, "phrase")
    assert find_anchor("6 RULES", _w, 0) == (5, "phrase")
    assert find_anchor("KING − MAN + WOMAN ≈ QUEEN", _w, 0) == (7, "token:king")
    assert find_anchor("50,257 TOKENS", _w, 0) == (2, "token:50257")
    assert find_anchor("THE T IN GPT", _w, 0) == (None, "none")
    assert find_anchor("2× COST", _w, 0, "six") == (5, "anchor:six")
    main()
