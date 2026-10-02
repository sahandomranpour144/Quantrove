import os
import subprocess

overlay_path = r"01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion/TIMELINE_MEDIA/00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov"
out_dir = r"01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion/screenshots"
os.makedirs(out_dir, exist_ok=True)

snapshots = [
    (7.0, "popup_01_free_trading_isnt_free_07s.png"),
    (21.0, "popup_02_fast_version_21s.png"),
    (99.5, "popup_03_wholesale_internalizers_100s.png"),
    (150.5, "popup_04_pfof_kickback_151s.png"),
    (279.0, "popup_05_limit_orders_only_279s.png"),
    (322.0, "popup_06_check_your_confirmation_322s.png"),
]

for t, filename in snapshots:
    out_path = os.path.join(out_dir, filename)
    # Composite over #202322 background using ffmpeg filter
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(t),
        "-i", overlay_path,
        "-filter_complex", "color=c=#202322:s=1920x1080:d=1[bg];[bg][0:v]overlay=0:0[out]",
        "-map", "[out]",
        "-vframes", "1",
        out_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Extracted {filename} at {t}s (size: {os.path.getsize(out_path):,} bytes)")

print("All 6 pop-up verification screenshots extracted successfully!")
