import os
import shutil

src_root = r"01_PROJECTS/YOUTUBE/longs/[IN_PROGRESS 2026-09-23]_long05_market_making_illusion"
dst_root = r"01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion"

os.makedirs(os.path.join(dst_root, "TIMELINE_MEDIA"), exist_ok=True)
os.makedirs(os.path.join(dst_root, "01_scripts"), exist_ok=True)
os.makedirs(os.path.join(dst_root, "02_assets_code"), exist_ok=True)
os.makedirs(os.path.join(dst_root, "03_metadata"), exist_ok=True)

files_to_copy = [
    ("TIMELINE_MEDIA/00_00m00s_to_05m37s_ep05_master_voiceover.wav", "TIMELINE_MEDIA/00_00m00s_to_05m37s_ep05_master_voiceover.wav"),
    ("TIMELINE_MEDIA/00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov", "TIMELINE_MEDIA/00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov"),
    ("TIMELINE_MEDIA/99_00m00s_to_05m37s_thumbnail_ep05_market_making.png", "TIMELINE_MEDIA/99_00m00s_to_05m37s_thumbnail_ep05_market_making.png"),
    ("01_scripts/TIMELINE_MANIFEST.md", "01_scripts/TIMELINE_MANIFEST.md"),
    ("01_scripts/VISUAL_SHOT_LIST.md", "01_scripts/VISUAL_SHOT_LIST.md"),
    ("01_scripts/EP05_SCRIPT.md", "01_scripts/EP05_SCRIPT.md"),
    ("02_assets_code/ep05_exact_word_timestamps.json", "02_assets_code/ep05_exact_word_timestamps.json"),
    ("popups_manifest.json", "popups_manifest.json"),
]

copied = []
for rel_src, rel_dst in files_to_copy:
    s = os.path.join(src_root, rel_src)
    d = os.path.join(dst_root, rel_dst)
    if os.path.exists(s):
        shutil.copy2(s, d)
        copied.append(f"Copied {rel_src} -> {rel_dst} ({os.path.getsize(d):,} bytes)")
    else:
        copied.append(f"MISSING: {rel_src}")

with open("logs/rebuild_setup_log.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(copied))

print(f"Rebuild workspace initialized at {dst_root} with {len(copied)} files copied.")
