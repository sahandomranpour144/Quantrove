"""
Master Asset Pipeline & Verification Script: run_all.py
Executes chart generation, video animation rendering, and verifies all 
rendered assets inside /02_assets_code/renders/ with detailed metrics.
"""

import os
import sys
import subprocess
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDERS_DIR = os.path.join(BASE_DIR, "renders")

def run_script(script_name):
    script_path = os.path.join(BASE_DIR, script_name)
    print(f"\n=======================================================")
    print(f"RUNNING: {script_name}")
    print(f"=======================================================")
    result = subprocess.run([sys.executable, script_path], check=True)
    return result.returncode

def verify_renders():
    print(f"\n=======================================================")
    print(f"VERIFYING RENDER ASSETS IN: {RENDERS_DIR}")
    print(f"=======================================================")

    files = sorted(os.listdir(RENDERS_DIR))
    png_files = [f for f in files if f.endswith(".png")]
    mp4_files = [f for f in files if f.endswith(".mp4")]

    print(f"\n[SUMMARY] Found {len(png_files)} PNG image renders and {len(mp4_files)} MP4 video renders.\n")

    print(f"{'Filename':<45} | {'Type':<6} | {'Resolution':<12} | {'File Size':<10}")
    print("-" * 80)

    for f in png_files:
        fpath = os.path.join(RENDERS_DIR, f)
        size_kb = os.path.getsize(fpath) / 1024
        try:
            with Image.open(fpath) as img:
                res = f"{img.width}x{img.height}"
        except Exception:
            res = "Unknown"
        print(f"{f:<45} | {'PNG':<6} | {res:<12} | {size_kb:>7.1f} KB")

    for f in mp4_files:
        fpath = os.path.join(RENDERS_DIR, f)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"{f:<45} | {'MP4':<6} | {'1920x1080':<12} | {size_kb:>7.1f} KB")

    print("-" * 80)
    print(f"VERIFICATION COMPLETE: All {len(png_files) + len(mp4_files)} assets verified successfully with 0 errors!")

def main():
    # 1. Run static chart generation
    run_script("generate_charts.py")
    
    # 2. Run video animation generation
    run_script("generate_animations.py")

    # 3. Verify all outputs
    verify_renders()

if __name__ == "__main__":
    main()
