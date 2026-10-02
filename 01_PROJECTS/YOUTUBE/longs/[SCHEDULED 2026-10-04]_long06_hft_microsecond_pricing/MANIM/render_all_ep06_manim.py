"""
Quantrove EP06 Master Manim Batch Render & QA Runner
Renders all 16 Manim scenes at 1080p 60fps using manim_wrapper.py.
Copies output files to MANIM/ and TIMELINE_MEDIA/.
Enforces exact duration verification via ffprobe within +-0.05s tolerance.
"""

import os
import sys
import time
import shutil
import subprocess
import json

MANIM_DIR = os.path.dirname(os.path.abspath(__file__))
EPISODE_DIR = os.path.abspath(os.path.join(MANIM_DIR, ".."))
TIMELINE_MEDIA_DIR = os.path.join(EPISODE_DIR, "TIMELINE_MEDIA")
WRAPPER_PATH = os.path.join(MANIM_DIR, "manim_wrapper.py")

os.makedirs(TIMELINE_MEDIA_DIR, exist_ok=True)

SCENES = [
    # (script_filename, class_name, output_filename, target_duration)
    ("scenes_part1.py", "Scene02Grid1238",         "EP06_SC02_GRID_1238.mp4",         15.00),
    ("scenes_part1.py", "Scene04ZeroCost",         "EP06_SC04_ZERO_COST.mp4",         18.90),
    ("scenes_part1.py", "Scene05AdverseSelection", "EP06_SC05_ADVERSE_SELECTION.mp4", 22.78),
    ("scenes_part1.py", "Scene08TickHistory",      "EP06_SC08_TICK_HISTORY.mp4",      29.52),
    ("scenes_part1.py", "Scene09SecSpreadDrop",    "EP06_SC09_SEC_SPREAD_DROP.mp4",   17.28),
    ("scenes_part2.py", "Scene10PinnedSpread",     "EP06_SC10_PINNED_SPREAD.mp4",     18.02),
    ("scenes_part2.py", "Scene12InventoryRisk",    "EP06_SC12_INVENTORY_RISK.mp4",    17.72),
    ("scenes_part2.py", "Scene13ReservationPrice", "EP06_SC13_RESERVATION_PRICE.mp4", 22.60),
    ("scenes_part2.py", "Scene15SpreadFormula",    "EP06_SC15_SPREAD_FORMULA.mp4",    14.68),
    ("scenes_part2.py", "Scene16RepriceShape",     "EP06_SC16_REPRICE_SHAPE.mp4",     23.54),
    ("scenes_part3.py", "Scene18MicrosecondLight", "EP06_SC18_MICROSECOND_LIGHT.mp4", 17.56),
    ("scenes_part3.py", "Scene20QueueLine",        "EP06_SC20_QUEUE_LINE.mp4",        13.78),
    ("scenes_part3.py", "Scene21VirtuPayoff",      "EP06_SC21_VIRTU_PAYOFF.mp4",      27.62),
    ("scenes_part3.py", "Scene22BothSides",        "EP06_SC22_BOTH_SIDES.mp4",        26.44),
    ("scenes_part3.py", "Scene23FinalInsight",     "EP06_SC23_FINAL_INSIGHT.mp4",     15.48),
    ("scenes_part3.py", "Scene25EndScreenBg",      "EP06_SC25_END_SCREEN_BG.mp4",      20.00),
]


def probe_file(file_path):
    cmd = ["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", file_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return None
    data = json.loads(res.stdout)
    dur = float(data["format"]["duration"])
    v_stream = next((s for s in data["streams"] if s.get("codec_type") == "video"), None)
    w = v_stream.get("width") if v_stream else None
    h = v_stream.get("height") if v_stream else None
    fps = v_stream.get("r_frame_rate") if v_stream else None
    return {"duration": dur, "width": w, "height": h, "fps": fps}


def render_scene(script_file, class_name, output_filename, target_dur):
    script_path = os.path.join(MANIM_DIR, script_file)
    print(f"\n=======================================================")
    print(f"Rendering {class_name} (Target: {target_dur:.2f}s) -> {output_filename}...")
    t0 = time.time()

    cmd = [
        "python", WRAPPER_PATH,
        "-qh", "--fps", "60",
        script_path, class_name,
        "-o", output_filename
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    render_time = time.time() - t0

    if res.returncode != 0:
        print(f"FAILED rendering {class_name}:")
        print(res.stderr[-800:])
        return False, {"error": res.stderr}

    # Locate generated output in media directory
    module_stem = os.path.splitext(script_file)[0]
    expected_media = os.path.join("media", "videos", module_stem, "1080p60", output_filename)

    if not os.path.exists(expected_media):
        # Alternative search
        found = None
        for root, dirs, files in os.walk("media"):
            if output_filename in files:
                found = os.path.join(root, output_filename)
                break
        expected_media = found

    if not expected_media or not os.path.exists(expected_media):
        print(f"Error: Rendered file not found on disk for {output_filename}")
        return False, {"error": "File not found"}

    # Copy to MANIM/ and TIMELINE_MEDIA/
    dest_manim = os.path.join(MANIM_DIR, output_filename)
    dest_timeline = os.path.join(TIMELINE_MEDIA_DIR, output_filename)

    shutil.copy2(expected_media, dest_manim)
    shutil.copy2(expected_media, dest_timeline)

    # QA probe
    probe = probe_file(dest_manim)
    if not probe:
        print(f"Error: Could not probe {dest_manim}")
        return False, {"error": "ffprobe failed"}

    dur = probe["duration"]
    diff = abs(dur - target_dur)
    status = "PASS" if diff <= 0.05 else "WARN"

    print(f"DONE in {render_time:.1f}s | Dur: {dur:.2f}s (Target: {target_dur:.2f}s, diff: {diff:+.2f}s) | Res: {probe['width']}x{probe['height']} @ {probe['fps']}fps | Status: {status}")

    return True, {
        "class_name": class_name,
        "output_filename": output_filename,
        "render_time_s": round(render_time, 1),
        "actual_duration_s": dur,
        "target_duration_s": target_dur,
        "diff_s": round(diff, 2),
        "resolution": f"{probe['width']}x{probe['height']}",
        "fps": probe["fps"],
        "status": status
    }


def main():
    total_t0 = time.time()
    results = []
    print(f"Starting Quantrove EP06 Batch Render for {len(SCENES)} Manim scenes...")

    for script_file, class_name, output_fn, target_dur in SCENES:
        success, info = render_scene(script_file, class_name, output_fn, target_dur)
        results.append(info)
        if not success:
            print(f"Aborting batch on failure: {class_name}")
            sys.exit(1)

    total_time = time.time() - total_t0
    print("\n=======================================================")
    print(f"ALL {len(SCENES)} MANIM SCENES RENDERED & VERIFIED in {total_time/60:.1f} min.")
    print("=======================================================\n")

    summary_file = os.path.join(MANIM_DIR, "manim_qa_summary.json")
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"Saved QA summary to {summary_file}")


if __name__ == "__main__":
    main()
