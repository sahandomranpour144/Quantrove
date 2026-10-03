"""Conform Sahand's Flow clips to the episode timeline.
Usage: python flow_ingest.py <episode folder> <EPxx>
Reads FLOW/<CLIP_ID>*.mp4, trims to the exact timeline frame count (never stretched; a short clip
holds its last frame), upscales to 1920x1080 @ 60 fps, applies a subtle brand-canvas grade, and writes
TIMELINE_MEDIA/EPxx_SCnn_<CLIP_ID>.mp4.
"""
import glob, json, os, subprocess, sys

GRADE = "eq=saturation=0.82:contrast=1.05:brightness=-0.025,colorbalance=bs=0.03:bm=0.02"  # cool, toward #202322/#233D4C

ep_dir, ep = sys.argv[1], sys.argv[2]
tl = json.load(open(os.path.join(ep_dir, "ASSEMBLY", f"{ep}_MASTER_TIMELINE.json"), encoding="utf-8"))
for sc in (s for s in tl["scenes"] if s["engine"] == "Flow"):
    src = glob.glob(os.path.join(glob.escape(ep_dir), "FLOW", glob.escape(sc["asset"]) + "*.mp4"))
    if not src:
        print("MISSING", sc["asset"]); continue
    frames = round(sc["end"] * 60) - round(sc["start"] * 60)
    out = os.path.join(ep_dir, "TIMELINE_MEDIA", f"{ep}_SC{sc['scene']:02d}_{sc['asset']}.mp4")
    vf = (f"scale=1920:1080:flags=lanczos,fps=60,{GRADE},"
          f"tpad=stop_mode=clone:stop_duration=2,trim=end_frame={frames},setpts=PTS-STARTPTS")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src[0], "-an", "-vf", vf, "-c:v", "libx264",
                    "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", out], check=True)
    got = int(subprocess.check_output(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                                       "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", out], text=True))
    print(f"{os.path.basename(out)}: {got}/{frames} frames {'OK' if abs(got - frames) <= 1 else 'MISMATCH'}")
