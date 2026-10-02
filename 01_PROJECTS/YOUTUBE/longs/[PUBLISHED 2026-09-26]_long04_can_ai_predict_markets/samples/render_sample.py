import subprocess, shutil, os, sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRATCH = Path(r"E:\AI_COMPANY\01_PROJECTS\YOUTUBE\_render_scratch_ep04")
SCRATCH.mkdir(parents=True, exist_ok=True)

src_py = BASE_DIR / "sample_medallion_compounding.py"
dst_py = SCRATCH / "sample_medallion_compounding.py"
shutil.copy2(src_py, dst_py)

out_mp4 = BASE_DIR / "sample_medallion_compounding.mp4"

print("Rendering MedallionCompoundingSample via bracket-free scratch dir...")
cmd = [
    sys.executable, "-m", "manim",
    "-qh", "--fps", "60",
    str(dst_py),
    "MedallionCompoundingSample",
    "-o", "sample_medallion_compounding.mp4",
    "--media_dir", str(SCRATCH / "media")
]

res = subprocess.run(cmd, cwd=str(SCRATCH))
if res.returncode != 0:
    print(f"Render failed with code {res.returncode}")
    sys.exit(res.returncode)

rendered = SCRATCH / "media" / "videos" / "sample_medallion_compounding" / "1080p60" / "sample_medallion_compounding.mp4"
if rendered.exists():
    shutil.copy2(rendered, out_mp4)
    print(f"\n[SUCCESS] Sample rendered and copied to: {out_mp4}")
    
    # Extract preview frames
    frames_dir = BASE_DIR / "preview_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    for sec in [1.5, 3.5, 6.0, 8.5, 9.8]:
        f_out = frames_dir / f"frame_{sec:.1f}s.png"
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(sec), "-i", str(out_mp4),
            "-vframes", "1", "-q:v", "2", str(f_out)
        ], capture_output=True)
    print(f"Extracted preview frames in: {frames_dir}")
else:
    print(f"Could not find rendered video at {rendered}")
