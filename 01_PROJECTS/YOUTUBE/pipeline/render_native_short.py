#!/usr/bin/env python3
"""
Renders a native Short Manim scene and copies the final video to video.mp4.
"""
import os
import sys
import shutil
import subprocess

def render_short(short_folder, scene_name, quality="l"):
    short_dir = os.path.join(r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\shorts", short_folder)
    script_path = os.path.join(short_dir, "render_scene.py")
    media_dir = os.path.join(short_dir, "media")

    cmd = [
        sys.executable, "-m", "manim",
        f"-q{quality}",
        "--media_dir", media_dir,
        script_path,
        scene_name
    ]
    print(f"▶ Rendering {scene_name} from {script_path}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("❌ Render failed:")
        print(res.stderr[-1000:])
        return False

    # Find the final rendered file
    final_video = None
    for root, dirs, files in os.walk(media_dir):
        if "partial_movie_files" in root:
            continue
        for f in files:
            if f.endswith(".mp4") and scene_name in f:
                final_video = os.path.join(root, f)
                break

    if not final_video:
        print("❌ Could not locate final rendered mp4.")
        return False

    target_video = os.path.join(short_dir, "video.mp4")
    shutil.copyfile(final_video, target_video)
    print(f"✅ Rendered and copied to: {target_video} ({os.path.getsize(target_video)/1024/1024:.2f} MB)")
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True)
    parser.add_argument("--scene", required=True)
    parser.add_argument("--quality", default="l")
    args = parser.parse_args()
    success = render_short(args.folder, args.scene, args.quality)
    sys.exit(0 if success else 1)
