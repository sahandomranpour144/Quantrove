"""Visual-density + runtime check for a long-form script (EPxx_SCRIPT_AND_SHOTLIST.md).

Reads [NARRATION] "..." lines, splits beats on '‖', estimates timing at a given WPM,
flags beats > MAX_BEAT_S, and writes VO_SCRIPT_CLEAN.txt (beat marks removed) next to the script.
Usage: python ep_beatcheck.py <script.md> [wpm=159]
"""
import re, sys
from pathlib import Path

MAX_BEAT_S = 6.0      # visual-density.md: new shot every <= 6 s
END_SCREEN_S = 20.0

def check(path, wpm=159.0):
    text = Path(path).read_text(encoding="utf-8")
    scenes = re.findall(r'\*\*Scene (\d+)[^\n]*\n(?:.*\n)*?\[NARRATION\] "(.*)"', text)
    total_words, beats, long_beats, vo = 0, 0, [], []
    for num, narr in scenes:
        segs = [s.strip() for s in narr.split("‖") if s.strip()]
        vo.append(" ".join(segs))
        for s in segs:
            w = len(s.split())
            total_words += w
            beats += 1
            if w / wpm * 60 > MAX_BEAT_S:
                long_beats.append((int(num), round(w / wpm * 60, 1), s[:50]))
    narr_s = total_words / wpm * 60
    Path(path).with_name("VO_SCRIPT_CLEAN.txt").write_text("\n\n".join(vo) + "\n", encoding="utf-8")
    return {"scenes": len(scenes), "words": total_words, "beats": beats,
            "median_beat_s": round(narr_s / max(beats, 1), 2),
            "runtime": f"{int((narr_s + END_SCREEN_S) // 60)}:{int((narr_s + END_SCREEN_S) % 60):02d}",
            "long_beats": long_beats}

def sync(path):
    """Renumber '**Scene N —' sequentially and rebuild the §3 shot-list table from §4."""
    s = Path(path).read_text(encoding="utf-8")
    n = [0]
    def nx(_):
        n[0] += 1
        return f"**Scene {n[0]} —"
    s = re.sub(r"\*\*Scene \d+ —", nx, s)
    rows, chap = ["| Scene | Engine | Asset ID | Chapter |", "|---|---|---|---|"], ""
    for line in s[s.index("## 4. Script"):s.index("## 5. ")].splitlines():
        if line.startswith("### "):
            chap = line[4:].split(" — ")[-1].title()
        m = re.match(r"\*\*Scene (\d+) — (\S+) \((\w+)", line)
        if m:
            rows.append(f"| {m[1]} | {m[2]} | {m[3]} | {chap} |")
    a, b = s.index("## 3. Shot list"), s.index("## 4. Script")
    s = s[:a] + "## 3. Shot list (auto-built from §4 by ep_beatcheck.py --sync)\n" + "\n".join(rows) + "\n\n" + s[b:]
    Path(path).write_text(s, encoding="utf-8")

if __name__ == "__main__":
    if "--sync" in sys.argv:
        sys.argv.remove("--sync")
        sync(sys.argv[1])
    # self-check
    import tempfile, os
    sample = '**Scene 1 — Manim (X)**\n[VISUAL] v\n[NARRATION] "one two three ‖ four five"\n'
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "s.md"); Path(p).write_text(sample, encoding="utf-8")
        r = check(p, wpm=60)
        assert r["words"] == 5 and r["beats"] == 2 and not r["long_beats"], r
        assert Path(d, "VO_SCRIPT_CLEAN.txt").read_text(encoding="utf-8").strip() == "one two three four five"
    if len(sys.argv) > 1:
        r = check(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 159.0)
        lb = r.pop("long_beats")
        print(r)
        for b in lb: print("LONG BEAT", b)
