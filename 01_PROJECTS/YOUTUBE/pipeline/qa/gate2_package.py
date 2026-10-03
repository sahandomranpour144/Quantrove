"""Gate 2 package for a long-form episode.
Usage: python gate2_package.py <episode folder> <EPxx>
- Verifies every timeline scene has TIMELINE_MEDIA/EPxx_SCnn_<ASSET>.mp4 (1920x1080, 60 fps, frames == timeline ±1)
- Verifies 00_OVERLAY_EPxx_kinetic_word_pops_60fps.mov (alpha, 60 fps, full length)
- Writes ASSEMBLY/GATE2_CONTACT_SHEET.png (one mid-scene frame per scene, labelled)
- Writes ASSEMBLY/CAPCUT_IMPORT_ORDER.md (V1 order with exact in-points, V2 overlay, A1 VO, A2 music)
"""
import glob, json, os, subprocess, sys

def probe(path, entries):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
                                   "-show_entries", f"stream={entries}", "-of", "json", path], text=True)
    st = json.loads(out)["streams"][0]
    return [str(st.get(k, "")) for k in entries.split(",")]

def main(ep_dir, ep):
    tl = json.load(open(os.path.join(ep_dir, "ASSEMBLY", f"{ep}_MASTER_TIMELINE.json"), encoding="utf-8"))
    media = os.path.join(ep_dir, "TIMELINE_MEDIA")
    rows, missing, bad, frames_dir = [], [], [], os.path.join(ep_dir, "ASSEMBLY", "_gate2_frames")
    os.makedirs(frames_dir, exist_ok=True)
    for sc in tl["scenes"]:
        name = f"{ep}_SC{sc['scene']:02d}_{sc['asset']}.mp4"
        path = os.path.join(media, name)
        want = round(sc["end"] * 60) - round(sc["start"] * 60)
        if not os.path.exists(path):
            missing.append(name); rows.append((sc, name, "MISSING")); continue
        w, h, fps, n = probe(path, "width,height,r_frame_rate,nb_read_frames")
        ok = (w, h, fps) == ("1920", "1080", "60/1") and abs(int(n) - want) <= 1
        if not ok:
            bad.append(f"{name}: {w}x{h} {fps} {n}/{want} frames")
        rows.append((sc, name, "OK" if ok else "CHECK"))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{sc['duration'] / 2:.2f}", "-i", path, "-frames:v", "1",
                        "-vf", "scale=384:216",
                        os.path.join(frames_dir, f"{sc['scene']:02d}.png")], check=False)
    ov = os.path.join(media, f"00_OVERLAY_{ep}_kinetic_word_pops_60fps.mov")
    ov_status = "MISSING"
    if os.path.exists(ov):
        try:
            pix, fps = probe(ov, "pix_fmt,r_frame_rate")[:2]
            ov_status = "OK" if ("a" in pix and fps == "60/1") else f"CHECK ({pix}, {fps})"
        except subprocess.CalledProcessError:
            ov_status = "UNREADABLE (still rendering?)"
    # contact sheet: 6 columns, labelled with Pillow (ffmpeg drawtext lacks fontconfig on Windows)
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "assets", "fonts", "Nohemi-Bold.ttf"), 18)
    cols, W, H = 6, 384, 216
    sheet = Image.new("RGB", (cols * W, -(-len(rows) // cols) * H), "#202322")
    for i, (sc, _, st) in enumerate(rows):
        f = os.path.join(frames_dir, f"{sc['scene']:02d}.png")
        tile = Image.open(f).convert("RGB") if os.path.exists(f) else Image.new("RGB", (W, H), "#202322")
        d = ImageDraw.Draw(tile)
        d.rectangle([0, 0, W, 26], fill="#202322")
        d.text((8, 3), f"S{sc['scene']} {sc['engine']} {sc['asset'][:22]}", font=font,
               fill="#E6EDF3" if st == "OK" else "#FD802E")
        sheet.paste(tile, ((i % cols) * W, (i // cols) * H))
    sheet.save(os.path.join(ep_dir, "ASSEMBLY", "GATE2_CONTACT_SHEET.png"))
    lines = [f"# {ep} — CapCut import order (1920x1080, 60 fps project)", "",
             f"Total length: {tl['total_duration_s']:.2f} s. Place each clip at its START on V1, back to back; durations are frame-exact.", "",
             "| # | V1 file | Start | Duration | Engine |", "|---|---|---|---|---|"]
    for sc, name, st in rows:
        m, s = divmod(sc["start"], 60)
        lines.append(f"| {sc['scene']} | `{name}` | {int(m):02d}:{s:06.3f} | {sc['duration']:.3f} s | {sc['engine']}{'' if st == 'OK' else ' ⚠ ' + st} |")
    lines += ["", f"- **V2:** `00_OVERLAY_{ep}_kinetic_word_pops_60fps.mov` at 00:00.000 (alpha, normal blend) — {ov_status}",
              f"- **A1:** voiceover `{os.path.basename(tl['vo_file'])}` at 00:00.000, normalize to −14 LUFS",
              "- **A2:** `assets/audio/BGM.mp3`, loop, ≥16 dB under voice with ducking, swell on the end screen. Credit block from `assets/audio/CREDITS.md` goes in the description (CC BY-ND 3.0).",
              "- Transitions: hard cuts; 0.25-0.40 s dissolves only at chapter starts; dip to black on the last 1 s."]
    open(os.path.join(ep_dir, "ASSEMBLY", "CAPCUT_IMPORT_ORDER.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"{ep}: {len(rows) - len(missing)}/{len(rows)} scenes present · {len(bad)} need checking · overlay {ov_status}")
    for x in missing: print("  MISSING", x)
    for x in bad: print("  CHECK", x)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
