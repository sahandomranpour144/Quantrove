#!/usr/bin/env python3
"""
Render 60fps Transparent Alpha Kinetic Pop-Up Overlays for EP04 Patch Segments
Reuses the exact styling, font, easing (ease_out_back), halos, and alpha export settings
from generate_full_kinetic_overlay_ep04.py.
Outputs:
  EP04_PATCH/overlay_segment_1_intro_60fps.mov
  EP04_PATCH/overlay_segment_2_mercer_60fps.mov
  EP04_PATCH/overlay_segment_3_noise_60fps.mov
  EP04_PATCH/overlay_segment_4_cta_60fps.mov
"""

import os
import sys
import math
import json
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

PATCH_DIR = os.path.dirname(os.path.abspath(__file__))

WIDTH, HEIGHT = 1920, 1080
FPS = 60

CYAN  = (0, 240, 255)
GOLD  = (255, 184, 0)
MINT  = (0, 255, 163)
RED   = (255, 75, 75)
WHITE = (255, 255, 255)

def get_font(size):
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibrib.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def ease_out_back(t, s=1.70158):
    t = max(0.0, min(1.0, t))
    t -= 1.0
    return t * t * ((s + 1.0) * t + s) + 1.0

def ease_out_quad(t):
    t = max(0.0, min(1.0, t))
    return t * (2 - t)

# Keyword configurations anchored to each segment's narration
PATCH_OVERLAYS = [
    {
        "output": "overlay_segment_1_intro_60fps.mov",
        "duration": 34.850,
        "keywords": [
            {"text": "CAN AI PREDICT?", "start": 0.50, "end": 2.80, "pos": (960, 280), "color": CYAN, "style": "glow"},
            {"text": "MOSTLY NO", "start": 4.80, "end": 7.20, "pos": (440, 780), "color": RED, "style": "glow"},
            {"text": "WORTH GOING SLOWLY", "start": 9.50, "end": 12.00, "pos": (1480, 780), "color": WHITE, "style": "clean"},
            {"text": "1988", "start": 14.50, "end": 16.50, "pos": (440, 320), "color": CYAN, "style": "glow"},
            {"text": "JIM SIMONS", "start": 17.50, "end": 20.00, "pos": (1480, 320), "color": GOLD, "style": "glow"},
            {"text": "+66% A YEAR", "start": 23.50, "end": 26.50, "pos": (960, 820), "color": GOLD, "style": "glow"},
            {"text": "AVOIDED WALL STREET", "start": 30.00, "end": 33.50, "pos": (960, 260), "color": RED, "style": "glow"}
        ]
    },
    {
        "output": "overlay_segment_2_mercer_60fps.mov",
        "duration": 9.833,
        "keywords": [
            {"text": "ROBERT MERCER", "start": 1.20, "end": 3.80, "pos": (480, 340), "color": CYAN, "style": "glow"},
            {"text": "50.75% OF THE TIME", "start": 5.50, "end": 8.80, "pos": (1440, 340), "color": GOLD, "style": "glow"}
        ]
    },
    {
        "output": "overlay_segment_3_noise_60fps.mov",
        "duration": 3.949,
        "keywords": [
            {"text": "PURE NOISE", "start": 1.50, "end": 3.50, "pos": (960, 480), "color": RED, "style": "glow"}
        ]
    },
    {
        "output": "overlay_segment_4_cta_60fps.mov",
        "duration": 19.985,
        "keywords": [
            {"text": "AI & MARKETS", "start": 1.80, "end": 4.50, "pos": (460, 320), "color": CYAN, "style": "glow"},
            {"text": "RECOMMENDATION ALGORITHM", "start": 6.50, "end": 10.50, "pos": (1460, 320), "color": GOLD, "style": "glow"},
            {"text": "REAL DATA & MATHEMATICS", "start": 13.00, "end": 16.50, "pos": (960, 780), "color": MINT, "style": "glow"},
            {"text": "QUANTROVE", "start": 17.50, "end": 19.50, "pos": (960, 360), "color": GOLD, "style": "glow"}
        ]
    }
]

def render_overlay(config):
    out_path = os.path.join(PATCH_DIR, config["output"])
    duration = config["duration"]
    keywords = config["keywords"]
    total_frames = int(duration * FPS)

    print(f"\n[+] Rendering Overlay: {config['output']} ({total_frames} frames @ {FPS}fps, dur: {duration:.3f}s)...")

    # ffmpeg pipe targeting prores_ks with yuva420p alpha channel
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-f", "rawvideo",
        "-pix_fmt", "rgba",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-r", str(FPS),
        "-i", "-",
        "-c:v", "prores_ks",
        "-profile:v", "4",
        "-pix_fmt", "yuva420p",
        out_path
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    font_cache = {}

    for frame_idx in range(total_frames):
        t = frame_idx / float(FPS)
        frame_img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))

        for kw in keywords:
            t_start = kw["start"]
            t_end = kw["end"]
            if t_start <= t <= t_end:
                age = t - t_start
                rem = t_end - t

                # Scale easing (pop in)
                if age < 0.25:
                    scale = ease_out_back(age / 0.25)
                else:
                    scale = 1.0

                # Fade in / out alpha
                if age < 0.15:
                    alpha = ease_out_quad(age / 0.15)
                elif rem < 0.25:
                    alpha = ease_out_quad(rem / 0.25)
                else:
                    alpha = 1.0

                target_font_size = 54
                scaled_font_size = max(10, int(target_font_size * scale))

                if scaled_font_size not in font_cache:
                    font_cache[scaled_font_size] = get_font(scaled_font_size)
                font = font_cache[scaled_font_size]

                text = kw["text"]
                color = kw["color"]
                style = kw.get("style", "glow")
                cx, cy = kw["pos"]

                # Measure bounding box
                bbox = font.getbbox(text)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]

                # Draw glowing background card
                pad_x, pad_y = int(24 * scale), int(12 * scale)
                box_w = tw + pad_x * 2
                box_h = th + pad_y * 2
                x0 = int(cx - box_w / 2)
                y0 = int(cy - box_h / 2)
                x1 = x0 + box_w
                y1 = y0 + box_h

                draw = ImageDraw.Draw(frame_img)
                bg_alpha = int(180 * alpha)
                border_alpha = int(220 * alpha)

                # Card background
                draw.rounded_rectangle(
                    [x0, y0, x1, y1], radius=int(8 * scale),
                    fill=(11, 15, 25, bg_alpha),
                    outline=(*color, border_alpha),
                    width=max(1, int(2 * scale))
                )

                # Text position
                tx = cx - tw / 2
                ty = cy - th / 2 - bbox[1]
                text_alpha = int(255 * alpha)

                # Glow layer if enabled
                if style == "glow" and alpha > 0.3:
                    glow_img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
                    glow_draw = ImageDraw.Draw(glow_img)
                    glow_draw.text((tx, ty), text, font=font, fill=(*color, int(120 * alpha)))
                    glow_blur = glow_img.filter(ImageFilter.GaussianBlur(radius=int(6 * scale)))
                    frame_img.alpha_composite(glow_blur)

                draw.text((tx, ty), text, font=font, fill=(*color, text_alpha))

        proc.stdin.write(frame_img.tobytes())

    proc.stdin.close()
    proc.wait()

    if proc.returncode == 0:
        # Check output with ffprobe
        probe = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=pix_fmt,r_frame_rate,duration", "-of", "csv=p=0", out_path],
            capture_output=True, text=True
        )
        print(f"  [OK] Rendered {config['output']}: {probe.stdout.strip()}")
    else:
        print(f"  [ERROR] Failed to render {config['output']}", file=sys.stderr)

def main():
    for cfg in PATCH_OVERLAYS:
        render_overlay(cfg)
    print("\n[+] All 4 kinetic overlay patch files generated successfully!")

if __name__ == "__main__":
    main()
