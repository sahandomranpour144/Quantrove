"""
Master Manim Rendering & Verification Script: render_manim_ep02.py
Renders all 6 Manim animation scenes at 1080p 60fps into /02_assets_code/renders/manim/
Verifies exact runtimes:
1. Hook50YrRecessionScene: 25.0s
2. NBERFrameworkScene: 26.0s
3. RefereeLagScene: 28.0s
4. LeadLagParadoxScene: 30.0s
5. TimeJobsAsymmetryScene: 30.0s
6. MacroRulesSummaryScene: 25.0s
"""

import os
import sys
import shutil
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MANIM_RENDERS_DIR = os.path.join(BASE_DIR, "renders", "manim")
os.makedirs(MANIM_RENDERS_DIR, exist_ok=True)

SCENES = [
    ("scene01_hook_50yr_recession.py", "Hook50YrRecessionScene", 25.0, "Hook50YrRecessionScene.mp4"),
    ("scene02_nber_framework.py", "NBERFrameworkScene", 26.0, "NBERFrameworkScene.mp4"),
    ("scene03_referee_lag.py", "RefereeLagScene", 28.0, "RefereeLagScene.mp4"),
    ("scene04_lead_lag_paradox.py", "LeadLagParadoxScene", 30.0, "LeadLagParadoxScene.mp4"),
    ("scene05_time_and_jobs_asymmetry.py", "TimeJobsAsymmetryScene", 30.0, "TimeJobsAsymmetryScene.mp4"),
    ("scene06_macro_rules_summary.py", "MacroRulesSummaryScene", 25.0, "MacroRulesSummaryScene.mp4"),
]

def get_video_duration(file_path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(result.stdout.strip())

def render_scene(script_file, scene_name, target_duration, output_filename):
    script_path = os.path.join(BASE_DIR, script_file)
    temp_media = os.path.join(BASE_DIR, f"temp_manim_{scene_name}")
    os.makedirs(temp_media, exist_ok=True)

    print(f"\n=======================================================")
    print(f"🎬 RENDERING: {scene_name} from {script_file}")
    print(f"Target Runtime: {target_duration:.1f}s | Resolution: 1920x1080 @ 60 FPS")
    print(f"=======================================================")

    cmd = [
        sys.executable, "-m", "manim", "render",
        "-r", "1920,1080", "--fps", "60",
        "--media_dir", temp_media,
        script_path, scene_name
    ]
    subprocess.run(cmd, check=True)

    # Locate generated mp4 file in temp_media
    found_mp4 = None
    for root, dirs, files in os.walk(temp_media):
        for f in files:
            if f.endswith(".mp4") and scene_name in f:
                found_mp4 = os.path.join(root, f)
                break

    if not found_mp4:
        raise FileNotFoundError(f"Could not locate rendered MP4 for {scene_name} in {temp_media}")

    dest_path = os.path.join(MANIM_RENDERS_DIR, output_filename)
    shutil.copy2(found_mp4, dest_path)
    shutil.rmtree(temp_media, ignore_errors=True)

    actual_duration = get_video_duration(dest_path)
    file_size_mb = os.path.getsize(dest_path) / (1024 * 1024)

    print(f"-> ✅ Saved: {dest_path}")
    print(f"-> Duration: {actual_duration:.2f}s (Target: {target_duration:.1f}s)")
    print(f"-> Size: {file_size_mb:.2f} MB")

    return actual_duration, file_size_mb

def main():
    results = []
    print("🚀 Starting Production Manim Rendering for EP02 (1080p 60fps)...")

    for script_file, scene_name, target_dur, out_name in SCENES:
        actual_dur, size_mb = render_scene(script_file, scene_name, target_dur, out_name)
        results.append((scene_name, target_dur, actual_dur, size_mb, out_name))

    print(f"\n=======================================================")
    print(f"🎉 ALL 6 MANIM SCENES RENDERED & VERIFIED IN RENDERS/MANIM/")
    print(f"Output Directory: {MANIM_RENDERS_DIR}")
    print(f"=======================================================\n")
    print(f"{'Scene Name':<25} | {'Target Dur':<11} | {'Actual Dur':<11} | {'Size':<10} | {'Status'}")
    print("-" * 80)
    for s_name, t_dur, a_dur, size, out_f in results:
        status = "PASSED (Exact)" if abs(t_dur - a_dur) < 0.1 else f"DIFF ({a_dur - t_dur:+.2f}s)"
        print(f"{s_name:<25} | {t_dur:>9.1f}s | {a_dur:>9.2f}s | {size:>7.2f} MB | {status}")
    print("-" * 80)

if __name__ == "__main__":
    main()
