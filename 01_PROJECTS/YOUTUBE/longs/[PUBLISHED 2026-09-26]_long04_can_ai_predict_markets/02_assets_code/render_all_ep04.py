"""EP04 Manim render driver.

Renders all five director-approved chart animations at 1080p60 and installs
them into TIMELINE_MEDIA/ with the exact final filenames referenced by
01_scripts/VISUAL_SHOT_LIST.md and 01_scripts/CAPCUT_FINAL_ASSEMBLY_GUIDE.md.

Why the scratch dir: manim's scene-name parser treats the episode folder's
'[IN_PROGRESS 2026-09-23]' brackets as regex character classes and crashes
('bad character range'). We copy the scene files to a bracket-free scratch
dir, render there, then move the finished MP4s into TIMELINE_MEDIA/.

Usage:  py -3.12 02_assets_code/render_all_ep04.py
"""
import subprocess
import shutil
import sys
from pathlib import Path

EP = Path(__file__).resolve().parent.parent
ASSETS = EP / "02_assets_code"
TIMELINE = EP / "TIMELINE_MEDIA"
SCRATCH = EP.parent.parent / "_render_scratch_ep04"

# (source file, scene class, timeline filename, target duration seconds)
JOBS = [
    ("Scene_02_Bell_Curve_5075.py", "BellCurve5075Scene", "02_01m26s_to_01m50s_Scene_02_BellCurve5075_manim.mp4", 24.0),
    ("Scene_02_Reflexivity.py", "ReflexivityScene", "02_02m00s_to_02m29s_Scene_02_Reflexivity_manim.mp4", 29.0),
    ("Scene_03_Alpha_Decay.py", "AlphaDecayScene", "03_02m29s_to_03m00s_Scene_03_AlphaDecay_manim.mp4", 31.0),
    ("Scene_04_Overfitting_Trap.py", "OverfittingTrapPart1", "04_03m21s_to_03m50s_Scene_04_OverfittingTrapPart1_manim.mp4", 29.0),
    ("Scene_04_Overfitting_Trap.py", "OverfittingTrapPart2", "04_04m00s_to_04m33s_Scene_04_OverfittingTrapPart2_manim.mp4", 33.0),
]
TOLERANCE = 0.35  # seconds

BED_SRC = EP.parent.parent / "_shared_lib" / "audio_sfx" / "bg_music.wav"
if not BED_SRC.exists():
    BED_SRC = Path(r"E:\AI_With_Hermes(Backup)\01_PROJECTS\YOUTUBE\_shared_lib\audio_sfx\bg_music.wav")
VO_MASTER = TIMELINE / "00_AUDIO_00m00s_to_07m05s_full_voiceover_ep04_master.wav"
BED_OUT = TIMELINE / "00_AUDIO_00m00s_to_07m05s_ambient_bed.wav"


def build_ambient_bed() -> None:
    """Loop the 60s cyber bed to the exact master-VO length with a tail fade."""
    dur = ffprobe_duration(VO_MASTER)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-stream_loop", "7", "-i", str(BED_SRC),
         "-t", f"{dur:.2f}", "-af", f"afade=t=out:st={dur - 3.2:.2f}:d=3.2",
         "-c:a", "pcm_s16le", str(BED_OUT)],
        check=True)
    print(f"[OK] {BED_OUT.name}: {ffprobe_duration(BED_OUT):.2f}s (matched to VO master)", flush=True)


def ffprobe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def _rmtree_tolerant(path: Path) -> None:
    """Delete tree, ignoring locks (e.g. a terminal cd'd into it). Any leftovers
    are cleared next run; renders still go to a fresh subfolder each time."""
    def onexc(func, p, exc):
        print(f"[warn] could not delete {p} ({exc}); continuing", flush=True)
    shutil.rmtree(path, ignore_errors=False, onexc=onexc)


def main() -> int:
    # Fresh scratch dir with the scene sources
    if SCRATCH.exists():
        _rmtree_tolerant(SCRATCH)
    SCRATCH.mkdir(parents=True)
    for src in {j[0] for j in JOBS}:
        shutil.copy2(ASSETS / src, SCRATCH / src)

    failures = []
    for src, scene, final_name, target in JOBS:
        print(f"[render] {scene} -> {final_name} (target {target}s)", flush=True)
        proc = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--disable_caching", src, scene],
            cwd=SCRATCH, capture_output=True, text=True)
        if proc.returncode != 0:
            print(f"[FAIL render] {scene}\n{proc.stdout[-2000:]}\n{proc.stderr[-2000:]}", flush=True)
            failures.append(scene)
            continue
        produced = next((SCRATCH / "media" / "videos").rglob(f"{scene}.mp4"))
        dest = TIMELINE / final_name
        if dest.exists():
            dest.unlink()
        shutil.move(str(produced), dest)
        dur = ffprobe_duration(dest)
        ok = abs(dur - target) <= TOLERANCE
        size_mb = dest.stat().st_size / 1e6
        print(f"[{'OK' if ok else 'DURATION-MISMATCH'}] {final_name}: {dur:.2f}s (target {target}s), {size_mb:.1f} MB", flush=True)
        if not ok:
            failures.append(final_name)

    print("\n=== RENDER SUMMARY ===")
    print(f"installed={len(JOBS) - len(failures)}/{len(JOBS)} failures={failures or 'none'}")
    if not failures:
        build_ambient_bed()
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
