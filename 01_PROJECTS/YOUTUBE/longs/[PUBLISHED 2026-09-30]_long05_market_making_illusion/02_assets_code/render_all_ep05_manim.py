"""
EP05 Manim Master Batch Render & Exact Duration Verification Runner
Renders all 12 scenes at 1080p 60fps using manim_wrapper.py.
Copies renders directly to TIMELINE_MEDIA with exact chronological names.
Enforces zero tolerance: ffprobe duration MUST match TIMELINE_MANIFEST.md within +-0.05s.
Extracts start/mid/end screenshots for every rebuilt scene.
"""
import sys
import os
import shutil
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EPISODE_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
TIMELINE_DIR = os.path.join(EPISODE_DIR, "TIMELINE_MEDIA")
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
SCREENSHOTS_DIR = os.path.join(EPISODE_DIR, "screenshots")

os.makedirs(RENDERS_DIR, exist_ok=True)
os.makedirs(TIMELINE_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

WRAPPER_PATH = os.path.join(BASE_DIR, "manim_wrapper.py")

SCENES = [
    ("scene01_hook.py",              "Scene01Hook",              "01_00m00s_to_00m20s_hook_buy_button_shatter.mp4",             20.00),
    ("scene02_pace_statement.py",   "Scene02PaceStatement",    "02_00m20s_to_00m38s_pace_statement_progress_bar.mp4",          18.24),
    ("scene03_illusion_of_zero.py",  "Scene03IllusionOfZero",    "03_00m38s_to_01m03s_illusion_ticket_to_zero_loupe.mp4",        25.16),
    ("scene04_who_fills_orders.py",  "Scene04WhoFillsOrders",    "04b_01m07s_to_01m36s_order_routing_citadel_virtu.mp4",         29.84),
    ("scene05_bid_ask_mechanism.py", "Scene05BidAskMechanism",   "05_01m36s_to_02m11s_bid_ask_spread_order_book.mp4",           34.96),
    ("scene06_pfof_kickback.py",     "Scene06PfofKickback",      "06_02m11s_to_02m47s_pfof_kickback_revenue_chart.mp4",          35.24),
    ("scene07_sec_65m_penalty.py",   "Scene07Sec65mPenalty",    "07b_02m50s_to_03m20s_sec_65m_penalty_settlement.mp4",          29.66),
    ("scene08_real_cost_to_you.py",  "Scene08RealCostToYou",     "08_03m20s_to_03m53s_compounding_penny_500_trade_grid.mp4",    33.32),
    ("scene09_nbbo_benchmark.py",    "Scene09NbboBenchmark",     "09_03m53s_to_04m23s_nbbo_vs_pfof_price_ladder.mp4",           29.52),
    ("scene10_defense_steps.py",     "Scene10DefenseSteps",      "10_04m23s_to_04m59s_three_defense_steps_limit_orders.mp4",     36.88),
    ("scene11_close_loops_recap.py", "Scene11CloseLoopsRecap",   "11_04m59s_to_05m16s_loop_ledger_four_checkmarks.mp4",         16.92),
    ("scene12_cta_outro.py",         "Scene12CtaOutro",          "12b_05m20s_to_05m37s_cta_end_card_clear_zones.mp4",            16.62),
]

def ffprobe_duration(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) < 1000:
        return None
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True
        )
        return float(res.stdout.strip())
    except Exception:
        return None

def extract_scene_screenshots(video_path, scene_name, duration):
    t_start = 0.5
    t_mid = duration / 2.0
    t_end = max(0.5, duration - 0.5)

    shots = [
        (t_start, f"{scene_name}_start_{t_start:.1f}s.png"),
        (t_mid,   f"{scene_name}_mid_{t_mid:.1f}s.png"),
        (t_end,   f"{scene_name}_end_{t_end:.1f}s.png")
    ]
    for t, out_name in shots:
        out_path = os.path.join(SCREENSHOTS_DIR, out_name)
        cmd = [
            "ffmpeg", "-y",
            "-ss", str(t),
            "-i", video_path,
            "-vframes", "1",
            out_path
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

def render_and_verify(selected_scenes=None):
    results = []
    print("=" * 75)
    print("🎬 REBUILDING EP05 MANIM SCENES (1080p60, Exact Duration Anchored)")
    print("=" * 75)

    media_dir = os.path.join(BASE_DIR, "media")

    for i, (script, cls, timeline_name, target_dur) in enumerate(SCENES, 1):
        if selected_scenes and cls not in selected_scenes and str(i) not in selected_scenes:
            continue

        timeline_target = os.path.join(TIMELINE_DIR, timeline_name)
        out_name = f"{cls}.mp4"
        out_path = os.path.join(RENDERS_DIR, out_name)

        print(f"\n[{i}/{len(SCENES)}] Rendering {cls} (Target: {target_dur:.2f}s)...")
        script_path = os.path.join(BASE_DIR, script)

        cmd = [
            sys.executable, WRAPPER_PATH, "-qh", "--fps", "60",
            "--media_dir", media_dir,
            "-o", out_name,
            script_path, cls
        ]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.returncode != 0:
            print(f"❌ Error rendering {cls} (Exit code: {result.returncode})")
            print("\n".join(result.stdout.splitlines()[-15:]))
            sys.exit(result.returncode)

        # Locate output video in media_dir
        src_video = None
        for root, dirs, files in os.walk(os.path.join(media_dir, "videos")):
            if out_name in files:
                src_video = os.path.join(root, out_name)
                break

        if not src_video or not os.path.exists(src_video):
            print(f"❌ Rendered file {out_name} not found in {media_dir}!")
            sys.exit(1)

        shutil.copy2(src_video, out_path)
        shutil.copy2(src_video, timeline_target)

        actual_dur = ffprobe_duration(timeline_target)
        delta = actual_dur - target_dur
        status = "PASS" if abs(delta) < 0.05 else "FAIL"

        print(f"  Target: {target_dur:.2f}s | ffprobe: {actual_dur:.2f}s | Delta: {delta:+.2f}s -> {status}")
        if status != "PASS":
            print(f"❌ DURATION MISMATCH FAILURE: {cls} produced {actual_dur:.2f}s (wanted {target_dur:.2f}s)")
            sys.exit(1)

        # Extract screenshots
        extract_scene_screenshots(timeline_target, cls, actual_dur)
        results.append((cls, timeline_name, target_dur, actual_dur, delta, status))

    print("\n" + "=" * 75)
    print("VERIFICATION SUMMARY TABLE")
    print("=" * 75)
    print(f"{'Scene Class':25} | {'Assigned':8} | {'Actual':8} | {'Delta':7} | {'Status'}")
    print("-" * 75)
    for cls, t_name, td, ad, delta, st in results:
        print(f"{cls:25} | {td:6.2f}s | {ad:6.2f}s | {delta:+6.2f}s | {st}")
    print("=" * 75)

if __name__ == "__main__":
    sel = sys.argv[1:] if len(sys.argv) > 1 else None
    render_and_verify(sel)
