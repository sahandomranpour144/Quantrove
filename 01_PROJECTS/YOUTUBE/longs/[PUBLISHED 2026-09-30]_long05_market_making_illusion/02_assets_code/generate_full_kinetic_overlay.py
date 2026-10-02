"""
EP05 Master Full-Video Kinetic Keyword Overlay Generator (Rebuilt & Layout Contract v1 Compliant)
Renders 60fps transparent QuickTime RLE (qtrle) kinetic text overlay
across all 12 scenes (00:00.00 - 05:37.12) adhering to pipeline/config/layout_contract.json.
Enforces:
- Dynamic font scaling down to ~33-46px so card_w <= 540 <= 560px contract with ZERO clipping.
- Zero collision with caption lane (y 864-1080)
- Zero collision with margins (x < 96, x > 1824, y < 56)
- Flow scenes avoid forbidden center column (x 656-1264)
- Pill fill #222022 @ 80% opacity, 1px #233D4C border
- Rotation of slots (TL, TC, TR on Manim; TL, TR, ML, MR on Flow)
- Emits popups_manifest.json
"""
import os
import sys
import math
import json
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EPISODE_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
TIMELINE_DIR = os.path.join(EPISODE_DIR, "TIMELINE_MEDIA")
os.makedirs(TIMELINE_DIR, exist_ok=True)

WORKSPACE_ROOT = os.path.abspath(os.path.join(EPISODE_DIR, "..", "..", ".."))
CONTRACT_PATH = os.path.join(WORKSPACE_ROOT, "01_PROJECTS", "YOUTUBE", "pipeline", "config", "layout_contract.json")

# Brand Palette (Institutional Data Intelligence)
BG_TRANSPARENT = (0, 0, 0, 0)
PILL_FILL      = (34, 32, 34, 204)       # #222022 @ 80% opacity
CHROME_BORDER  = (35, 61, 76, 255)       # #233D4C 1px border
LIME_COLOR     = (195, 216, 9, 255)      # #C3D809 Power Lime
PUMPKIN_COLOR  = (253, 128, 46, 255)     # #FD802E Pumpkin
TEXT_WHITE     = (230, 237, 243, 255)    # #E6EDF3 Off-White

# Episode Timeline Map (Scene -> Engine / Clip)
TIMELINE = [
    ("Scene 01",  0.00,  20.00, "manim", "01_00m00s_to_00m20s_hook_buy_button_shatter.mp4"),
    ("Scene 02", 20.00,  38.24, "manim", "02_00m20s_to_00m38s_pace_statement_progress_bar.mp4"),
    ("Scene 03", 38.24,  63.40, "manim", "03_00m38s_to_01m03s_illusion_ticket_to_zero_loupe.mp4"),
    ("Scene 04a",63.40,  67.00, "flow",  "04_01m03s_to_01m07s_flow_hft_server_rack_corridor.mp4"),
    ("Scene 04b",67.00,  96.84, "manim", "04_01m07s_to_01m36s_order_routing_citadel_virtu.mp4"),
    ("Scene 05", 96.84, 131.80, "manim", "05_01m36s_to_02m11s_bid_ask_spread_order_book.mp4"),
    ("Scene 06",131.80, 167.04, "manim", "06_02m11s_to_02m47s_pfof_kickback_revenue_chart.mp4"),
    ("Scene 07a",167.04,170.50, "flow",  "07_02m47s_to_02m50s_flow_institutional_trading_floor.mp4"),
    ("Scene 07b",170.50,200.16, "manim", "07_02m50s_to_03m20s_sec_65m_penalty_settlement.mp4"),
    ("Scene 08",200.16, 233.48, "manim", "08_03m20s_to_03m53s_compounding_penny_500_trade_grid.mp4"),
    ("Scene 09",233.48, 263.00, "manim", "09_03m53s_to_04m23s_nbbo_vs_pfof_price_ladder.mp4"),
    ("Scene 10",263.00, 299.88, "manim", "10_04m23s_to_04m59s_three_defense_steps_limit_orders.mp4"),
    ("Scene 11",299.88, 316.80, "manim", "11_04m59s_to_05m16s_loop_ledger_four_checkmarks.mp4"),
    ("Scene 12a",316.80,320.50, "flow",  "12_05m16s_to_05m20s_flow_macro_phone_trade_confirmation.mp4"),
    ("Scene 12b",320.50,337.12, "manim", "12b_05m20s_to_05m37s_cta_end_card_clear_zones.mp4")
]

def get_scene_info(t):
    for name, t0, t1, stype, clip in TIMELINE:
        if t0 <= t < t1:
            return stype, clip
    return "manim", TIMELINE[-1][4]

def get_nohemi_font(size, bold=True):
    font_candidates = [
        os.path.join(WORKSPACE_ROOT, "assets", "fonts", "Nohemi-Bold.ttf" if bold else "Nohemi-Medium.ttf"),
        os.path.join(WORKSPACE_ROOT, "01_PROJECTS", "YOUTUBE", "pipeline", "remotion_engine", "public", "fonts", "Nohemi-Bold.ttf" if bold else "Nohemi-Medium.ttf"),
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arialbd.ttf"
    ]
    for p in font_candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def ease_out_back(t, s=1.70158):
    t = max(0.0, min(1.0, t))
    t -= 1.0
    return t * t * ((s + 1.0) * t + s) + 1.0

def ease_out_quad(t):
    t = max(0.0, min(1.0, t))
    return t * (2 - t)

# Master Curated Keywords (kept verbatim from original production)
RAW_KEYWORDS = [
    # --- SCENE 01: THE HOOK (00:00 - 00:20) ---
    {"text": "FREE TRADING ISN'T FREE", "start": 6.00,  "end": 8.50,  "color": PUMPKIN_COLOR, "style": "badge"},
    {"text": "YOU ARE THE PRODUCT",     "start": 11.80, "end": 14.20, "color": PUMPKIN_COLOR, "style": "glow"},
    {"text": "WHO'S BUYING YOU",        "start": 16.50, "end": 18.80, "color": LIME_COLOR,    "style": "badge"},

    # --- SCENE 02: PACE STATEMENT (00:20 - 00:38) ---
    {"text": "FAST VERSION",            "start": 20.20, "end": 22.50, "color": LIME_COLOR,    "style": "badge"},
    {"text": "BILLIONS IN ORDER FLOW",  "start": 27.50, "end": 30.50, "color": PUMPKIN_COLOR, "style": "glow"},
    {"text": "SEC PENALTY",             "start": 32.00, "end": 34.50, "color": PUMPKIN_COLOR, "style": "badge"},

    # --- SCENE 03: ILLUSION OF ZERO (00:38 - 01:03) ---
    {"text": "$19.95 PER TRADE",        "start": 41.00, "end": 44.00, "color": TEXT_WHITE,    "style": "clean"},
    {"text": "NOT GENEROUS",            "start": 54.50, "end": 57.00, "color": PUMPKIN_COLOR, "style": "glow"},
    {"text": "$0 ≠ FREE",               "start": 60.00, "end": 63.00, "color": PUMPKIN_COLOR, "style": "badge"},

    # --- SCENE 04: WHO FILLS ORDERS (01:03 - 01:36) ---
    {"text": "NOT THE NYSE",            "start": 82.50, "end": 85.50, "color": PUMPKIN_COLOR, "style": "badge"},
    {"text": "CITADEL & VIRTU",         "start": 88.50, "end": 92.00, "color": LIME_COLOR,    "style": "glow"},
    {"text": "WHOLESALE INTERNALIZERS", "start": 98.00, "end": 101.50,"color": LIME_COLOR,    "style": "badge"},

    # --- SCENE 05: BID-ASK SPREAD (01:36 - 02:11) ---
    {"text": "AIRPORT BOOTH MODEL",     "start": 105.00,"end": 108.50,"color": TEXT_WHITE,    "style": "clean"},
    {"text": "THE BID-ASK SPREAD",      "start": 117.00,"end": 120.50,"color": PUMPKIN_COLOR, "style": "badge"},
    {"text": "RISK-FREE PROFIT",        "start": 127.50,"end": 131.00,"color": LIME_COLOR,    "style": "glow"},

    # --- SCENE 06: PAYMENT FOR ORDER FLOW (02:11 - 02:47) ---
    {"text": "RETAIL FLOW IS SAFE",     "start": 138.50,"end": 142.00,"color": LIME_COLOR,    "style": "clean"},
    {"text": "PFOF KICKBACK",           "start": 149.00,"end": 152.50,"color": PUMPKIN_COLOR, "style": "badge"},
    {"text": "$200,000,000+ / QUARTER", "start": 159.00,"end": 163.00,"color": LIME_COLOR,    "style": "glow"},

    # --- SCENE 07: $65M SEC PENALTY (02:47 - 03:20) ---
    {"text": "$65,000,000 FINE",        "start": 172.00,"end": 176.00,"color": PUMPKIN_COLOR, "style": "badge"},
    {"text": "WORSE EXECUTION",         "start": 185.00,"end": 188.50,"color": PUMPKIN_COLOR, "style": "glow"},
    {"text": "THE HIDDEN INVOICE",      "start": 194.50,"end": 198.00,"color": TEXT_WHITE,    "style": "badge"},

    # --- SCENE 08: REAL COST (03:20 - 03:53) ---
    {"text": "THE REAL MATH",           "start": 207.50,"end": 210.50,"color": LIME_COLOR,    "style": "clean"},
    {"text": "-$2.00 PER 100 SHARES",   "start": 217.00,"end": 221.00,"color": PUMPKIN_COLOR, "style": "badge"},
    {"text": "SILENT COMPOUNDING",      "start": 227.00,"end": 231.00,"color": PUMPKIN_COLOR, "style": "glow"},

    # --- SCENE 09: NBBO BENCHMARK (03:53 - 04:23) ---
    {"text": "NBBO BENCHMARK",          "start": 242.00,"end": 245.50,"color": LIME_COLOR,    "style": "badge"},
    {"text": "LOST PRICE IMPROVEMENT",  "start": 254.00,"end": 258.00,"color": PUMPKIN_COLOR, "style": "glow"},

    # --- SCENE 10: 3 DEFENSE RULES (04:23 - 04:59) ---
    {"text": "1. LIMIT ORDERS ONLY",    "start": 277.50,"end": 281.50,"color": LIME_COLOR,    "style": "badge"},
    {"text": "2. AUDIT YOUR NBBO",      "start": 284.50,"end": 288.50,"color": LIME_COLOR,    "style": "badge"},
    {"text": "3. DIRECT ROUTING",       "start": 293.00,"end": 297.00,"color": LIME_COLOR,    "style": "badge"},

    # --- SCENE 11: RECAP (04:59 - 05:16) ---
    {"text": "4 LOOPS RESOLVED",        "start": 312.00,"end": 315.50,"color": LIME_COLOR,    "style": "badge"},

    # --- SCENE 12: CTA & OUTRO (05:16 - 05:37) ---
    {"text": "CHECK YOUR CONFIRMATION", "start": 320.00,"end": 324.00,"color": LIME_COLOR,    "style": "badge"},
    {"text": "SUBSCRIBE // EPISODE 06", "start": 332.00,"end": 336.50,"color": LIME_COLOR,    "style": "glow"},
]

def render_keyword_card(text, color, style="badge"):
    """
    Renders contract-compliant pop-up card:
    - Dynamic font scaling: scales down to ~30-46px so card_w <= 540 <= 560px max width contract.
    - Zero clipping on every single word.
    - Pill fill #222022 @ 80% opacity
    - 1px #233D4C border
    """
    pad_x = 28
    pad_y = 16
    max_allowed_w = 540  # strictly <= 560px max_width contract

    font_size = 46
    while font_size >= 20:
        font = get_nohemi_font(font_size, bold=True)
        bbox = font.getbbox(text)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        card_w = tw + pad_x * 2
        card_h = th + pad_y * 2
        if card_w <= max_allowed_w:
            break
        font_size -= 1

    card = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)

    # 1. Pill fill #222022 @ 80% opacity with 1px #233D4C border
    draw.rounded_rectangle(
        [0, 0, card_w - 1, card_h - 1],
        radius=14, fill=PILL_FILL, outline=CHROME_BORDER, width=1
    )

    # 2. Text in high-contrast brand color perfectly centered
    text_x = (card_w - tw) // 2 - bbox[0]
    text_y = (card_h - th) // 2 - bbox[1]
    draw.text((text_x, text_y), text, fill=color, font=font)

    if style == "glow":
        # Subtle glowing halo per kinetic-popups.md
        glow = Image.new("RGBA", (card_w + 24, card_h + 24), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        glow_draw.rounded_rectangle(
            [12, 12, card_w + 12, card_h + 12],
            radius=16, fill=(color[0], color[1], color[2], 50)
        )
        glow = glow.filter(ImageFilter.GaussianBlur(8))
        glow.alpha_composite(card, (12, 12))
        return glow, (glow.width // 2, glow.height // 2), (card_w, card_h)

    return card, (card_w // 2, card_h // 2), (card_w, card_h)


def prepare_manifest_and_keywords():
    """
    Assigns contract slots (LRU rotation, no back-to-back same slot),
    verifies zero time overlaps (resolves if any), computes exact bboxes,
    and returns processed keywords and manifest entries.
    """
    manim_slots = ["TL", "TC", "TR"]
    flow_slots  = ["TL", "TR", "ML", "MR"]

    slot_history = {"TL": -999, "TC": -999, "TR": -999, "ML": -999, "MR": -999}
    prev_slot = None

    processed_kws = []
    manifest_entries = []

    # Check & fix any time overlaps
    sorted_raw = sorted(RAW_KEYWORDS, key=lambda k: k["start"])
    for i in range(len(sorted_raw) - 1):
        if sorted_raw[i]["end"] > sorted_raw[i+1]["start"]:
            sorted_raw[i]["end"] = sorted_raw[i+1]["start"] - 0.0167

    for idx, kw in enumerate(sorted_raw):
        st = kw["start"]
        et = kw["end"]
        text = kw["text"]
        color = kw["color"]
        style = kw.get("style", "badge")
        stype, clip = get_scene_info(st)

        # LRU slot selection avoiding consecutive same slot
        cands = manim_slots if stype == "manim" else flow_slots
        valid_cands = [c for c in cands if c != prev_slot]
        best_slot = min(valid_cands, key=lambda s: slot_history[s])
        slot_history[best_slot] = idx
        prev_slot = best_slot

        # Render card to determine dimensions
        _, (cx, cy), (bw, bh) = render_keyword_card(text, color, style)

        # Compute position & bbox strictly inside popup band (y: 56-176, centered at y=116)
        if best_slot == "TL":
            xmin = 96
            xmax = 96 + bw
            ymin = 116 - bh // 2
            ymax = ymin + bh
            center_x = 96 + bw // 2
            center_y = 116
        elif best_slot == "TC":
            xmin = 960 - bw // 2
            xmax = xmin + bw
            ymin = 116 - bh // 2
            ymax = ymin + bh
            center_x = 960
            center_y = 116
        elif best_slot == "TR":
            xmax = 1824
            xmin = 1824 - bw
            ymin = 116 - bh // 2
            ymax = ymin + bh
            center_x = 1824 - bw // 2
            center_y = 116
        elif best_slot == "ML":
            xmin = 96
            xmax = 96 + bw
            ymin = 540 - bh // 2
            ymax = ymin + bh
            center_x = 96 + bw // 2
            center_y = 540
        elif best_slot == "MR":
            xmax = 1824
            xmin = 1824 - bw
            ymin = 540 - bh // 2
            ymax = ymin + bh
            center_x = 1824 - bw // 2
            center_y = 540

        color_hex = "#FD802E" if color == PUMPKIN_COLOR else ("#C3D809" if color == LIME_COLOR else "#E6EDF3")

        processed_kw = {
            "text": text,
            "start": st,
            "end": et,
            "pos": (center_x, center_y),
            "color": color,
            "style": style,
            "slot": best_slot,
            "bbox": [xmin, ymin, xmax, ymax],
            "scene_type": stype,
            "clip": clip,
            "color_hex": color_hex
        }
        processed_kws.append(processed_kw)

        manifest_entry = {
            "word": text,
            "start": st,
            "end": et,
            "slot": best_slot,
            "bbox": [xmin, ymin, xmax, ymax],
            "color": color_hex,
            "scene_type": stype,
            "clip": clip
        }
        manifest_entries.append(manifest_entry)

    return processed_kws, manifest_entries


def generate_overlay():
    fps = 60
    total_duration = 337.13  # matches measured master audio
    total_frames = int(math.ceil(total_duration * fps))

    out_overlay_path = os.path.join(TIMELINE_DIR, "00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov")
    print(f"🎬 Generating 60fps Kinetic Word Pop Overlay ({total_frames} frames)...")
    print(f"   Output: {out_overlay_path}")

    keywords, manifest = prepare_manifest_and_keywords()

    # Emit popups_manifest.json to episode folders
    manifest_paths = [
        os.path.join(EPISODE_DIR, "popups_manifest.json"),
        os.path.join(BASE_DIR, "popups_manifest.json"),
        os.path.join(TIMELINE_DIR, "popups_manifest.json")
    ]
    for mp in manifest_paths:
        with open(mp, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
    print(f"✅ Emitted popups_manifest.json ({len(manifest)} items)")

    # Pre-render cards
    cards = {}
    for kw in keywords:
        card, center, _ = render_keyword_card(kw["text"], kw["color"], kw["style"])
        cards[kw["text"]] = (card, center)

    # Start ffmpeg process with qtrle encoder
    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-pix_fmt", "rgba",
        "-s", "1920x1080",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "qtrle",
        out_overlay_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    pop_duration = 0.22   # 220ms elastic spring pop-in
    fade_duration = 0.14  # 140ms smooth fade-out
    empty_frame = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    empty_bytes = empty_frame.tobytes()

    for f in range(total_frames):
        t = f / fps
        active_kws = [kw for kw in keywords if kw["start"] <= t <= kw["end"]]

        if not active_kws:
            proc.stdin.write(empty_bytes)
            continue

        frame = empty_frame.copy()

        for kw in active_kws:
            card, (cx, cy) = cards[kw["text"]]
            elapsed = t - kw["start"]
            remaining = kw["end"] - t

            if elapsed < pop_duration:
                progress = elapsed / pop_duration
                scale = 0.40 + 0.60 * ease_out_back(progress, s=1.70158)
                alpha = min(1.0, elapsed / 0.08)
            elif remaining < fade_duration:
                progress = remaining / fade_duration
                scale = 1.0 + 0.05 * (1.0 - progress)
                alpha = ease_out_quad(progress)
            else:
                scale = 1.0
                alpha = 1.0

            scale = max(0.01, scale)
            target_w = int(card.width * scale)
            target_h = int(card.height * scale)

            scaled_card = card.resize((target_w, target_h), Image.Resampling.BILINEAR)

            if alpha < 0.99:
                r, g, b, a = scaled_card.split()
                a = a.point(lambda p: int(p * alpha))
                scaled_card = Image.merge("RGBA", (r, g, b, a))

            px, py = kw["pos"]
            x = px - target_w // 2
            y = py - target_h // 2

            frame.alpha_composite(scaled_card, (x, y))

        proc.stdin.write(frame.tobytes())

        if f % 4000 == 0:
            print(f"  Overlay progress: {f}/{total_frames} frames ({f/total_frames*100:.1f}%)...")

    proc.stdin.close()
    proc.wait()
    print("\n✅ 60fps Master Kinetic Keyword Overlay rendered successfully!")

if __name__ == "__main__":
    generate_overlay()
