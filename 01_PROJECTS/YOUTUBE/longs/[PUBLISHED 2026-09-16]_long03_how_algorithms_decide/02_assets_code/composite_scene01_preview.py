import os, sys, subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA"))

c1 = os.path.join(TIMELINE_DIR, "01_00m00s_to_00m10s_Scene_01_flow_infinite_feed_vortex.mp4")
c2 = os.path.join(TIMELINE_DIR, "01_00m10s_to_00m18s_Scene_01_flow_billions_scrolling_darkness.mp4")
c3 = os.path.join(TIMELINE_DIR, "01_00m18s_to_00m36s_Scene_01_ScaleOfUploads_manim.mp4")
c4 = os.path.join(TIMELINE_DIR, "01_00m36s_to_00m42s_Scene_01_flow_glass_touchpoint.mp4")
audio = os.path.join(TIMELINE_DIR, "01_AUDIO_00m00s_to_00m42s_Scene_01_hook_voiceover.mp3")
overlay = os.path.join(BASE_DIR, "scene01_kinetic_overlay.mov")
out_sample = os.path.join(TIMELINE_DIR, "Scene_01_kinetic_word_sample.mp4")

filter_script = (
    "[0:v]trim=0:10.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v0];"
    "[1:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v1];"
    "[2:v]trim=0:18.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v2];"
    "[3:v]trim=0:6.040,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v3];"
    "[v0][v1][v2][v3]concat=n=4:v=1:a=0[vbase];"
    "[4:v]scale=1920:1080,fps=60[vover];"
    "[vbase][vover]overlay=0:0:format=auto[vfinal]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", c1,
    "-i", c2,
    "-i", c3,
    "-i", c4,
    "-i", overlay,
    "-i", audio,
    "-filter_complex", filter_script,
    "-map", "[vfinal]",
    "-map", "5:a",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    "-t", "42.040",
    out_sample
]

print("Rendering final Scene 1 composite with kinetic pop overlay...")
res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("FFmpeg error:", res.stderr[-2000:])
    sys.exit(1)

print("✓ Finished composite render:", out_sample)
