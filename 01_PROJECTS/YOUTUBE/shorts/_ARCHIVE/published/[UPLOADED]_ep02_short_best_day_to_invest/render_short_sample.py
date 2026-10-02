import json
import math
import os
import subprocess
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

MASTER_VIDEO = "e:/AI_COMPANY/01_PROJECTS/YOUTUBE/longs/[SCHEDULED] long02_50_years_recession_data/Quantrove_EP02_50_Years_Recession_Data_MASTER/Quantrove_EP02_50_Years_Recession_Data_MASTER.mp4"
OUTPUT_DIR = "e:/AI_COMPANY/01_PROJECTS/YOUTUBE/shorts/ep02_short_best_day_to_invest"
RAW_VIDEO = os.path.join(OUTPUT_DIR, "ep02_short_best_day_to_invest_raw_9x16.mp4")
AUDIO_FILE = os.path.join(OUTPUT_DIR, "ep02_short_best_day_to_invest_audio.wav")
FINAL_OUTPUT = os.path.join(OUTPUT_DIR, "ep02_short_best_day_to_invest_FINAL.mp4")
FONT_BOLD_PATH = "e:/AI_COMPANY/01_PROJECTS/YOUTUBE/_shared_lib/fonts/Poppins-Bold.ttf"
FONT_SEMIBOLD_PATH = "e:/AI_COMPANY/01_PROJECTS/YOUTUBE/_shared_lib/fonts/Poppins-SemiBold.ttf"

FPS = 60
WIDTH = 1080
HEIGHT = 1920

# Load exact word timestamps
with open(os.path.join(OUTPUT_DIR, "exact_word_timestamps.json"), "r") as f:
    word_data = json.load(f)["words"]

# Group words into subtitle phrase chunks (2-4 words each)
def build_caption_chunks(words):
    chunks = []
    current_chunk = []
    for w in words:
        current_chunk.append(w)
        word_text = w["word"]
        if len(current_chunk) >= 4 or word_text.endswith((".", ",", "?", "!")) or (len(current_chunk) >= 3 and len(" ".join([x["word"] for x in current_chunk])) > 15):
            start_t = current_chunk[0]["start"]
            end_t = current_chunk[-1]["end"]
            chunks.append({
                "words": current_chunk,
                "start": start_t,
                "end": end_t
            })
            current_chunk = []
    if current_chunk:
        chunks.append({
            "words": current_chunk,
            "start": current_chunk[0]["start"],
            "end": current_chunk[-1]["end"]
        })
    return chunks

caption_chunks = build_caption_chunks(word_data)

# Curated Pop-Up Keywords (curated rhythmic subset, emphasis words only)
POPUP_KEYWORDS = [
    {
        "text": "50 YEARS",
        "start": 2.90,
        "end": 4.10,
        "x": 100,
        "y": 280,
        "color": (255, 184, 0),       # Amber Gold
    },
    {
        "text": "BEST DAY",
        "start": 5.00,
        "end": 6.20,
        "x": 680,
        "y": 280,
        "color": (0, 255, 163),       # Neon Emerald
    },
    {
        "text": "NEWS SCREAMING",
        "start": 8.50,
        "end": 9.90,
        "x": 100,
        "y": 280,
        "color": (255, 75, 75),       # Warning Crimson
    },
    {
        "text": "WORLD ENDING",
        "start": 10.30,
        "end": 11.60,
        "x": 600,
        "y": 280,
        "color": (255, 45, 105),      # Hot Coral Pink
    },
    {
        "text": "LOCKSTEP?",
        "start": 16.20,
        "end": 17.30,
        "x": 390,
        "y": 250,
        "color": (0, 229, 255),       # Cyber Cyan
    },
    {
        "text": "5 DECADES",
        "start": 18.50,
        "end": 19.60,
        "x": 100,
        "y": 280,
        "color": (168, 85, 247),      # Electric Purple
    },
    {
        "text": "COUNTER-INTUITIVE",
        "start": 23.00,
        "end": 24.60,
        "x": 240,
        "y": 250,
        "color": (255, 215, 0),       # Bright Gold
    },
    {
        "text": "MASSIVE RECOVERY",
        "start": 27.40,
        "end": 28.80,
        "x": 100,
        "y": 280,
        "color": (34, 197, 94),       # Vivid Green
    },
    {
        "text": "MONTHS BEFORE",
        "start": 29.00,
        "end": 30.60,
        "x": 600,
        "y": 280,
        "color": (0, 240, 255),       # Ice Blue
    }
]

# Load fonts
font_caption = ImageFont.truetype(FONT_BOLD_PATH, 44)
font_keyword = ImageFont.truetype(FONT_BOLD_PATH, 38)
font_cta = ImageFont.truetype(FONT_SEMIBOLD_PATH, 30)

def render_overlay_frame(t, total_dur):
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. RENDER POP-UP KEYWORD LAYER
    for kw in POPUP_KEYWORDS:
        if kw["start"] <= t <= kw["end"]:
            rel_t = t - kw["start"]
            k_dur = kw["end"] - kw["start"]

            # Animation: Scale pop (0.0s -> 0.15s: pop 0.85 -> 1.08 -> 1.00)
            if rel_t < 0.15:
                p = rel_t / 0.15
                scale = 0.85 + 0.23 * math.sin(p * math.pi * 0.5)
                alpha = int(255 * p)
            elif rel_t > k_dur - 0.12:
                p = (k_dur - rel_t) / 0.12
                scale = 1.0
                alpha = int(255 * max(0.0, p))
            else:
                scale = 1.0
                alpha = 255

            kw_text = kw["text"]
            bbox = font_keyword.getbbox(kw_text)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            pad_x = 26
            pad_y = 14
            card_w = tw + pad_x * 2 + 20
            card_h = th + pad_y * 2

            kw_img = Image.new("RGBA", (card_w + 30, card_h + 30), (0, 0, 0, 0))
            kw_draw = ImageDraw.Draw(kw_img)

            glow_box = [15, 15, 15 + card_w, 15 + card_h]
            kw_color = kw["color"]
            
            # Dark glass pill with colored outline
            kw_draw.rounded_rectangle(glow_box, radius=18, fill=(10, 15, 28, int(230 * (alpha / 255))), outline=(kw_color[0], kw_color[1], kw_color[2], int(200 * (alpha / 255))), width=2)
            
            # Left accent dot
            dot_y = 15 + (card_h - 12) // 2
            kw_draw.ellipse([26, dot_y, 38, dot_y + 12], fill=(kw_color[0], kw_color[1], kw_color[2], alpha))

            # Text
            text_x = 48
            text_y = 15 + pad_y - bbox[1]
            kw_draw.text((text_x, text_y), kw_text, font=font_keyword, fill=(kw_color[0], kw_color[1], kw_color[2], alpha))

            # Apply scale transform
            if abs(scale - 1.0) > 0.01:
                new_w = max(1, int(kw_img.width * scale))
                new_h = max(1, int(kw_img.height * scale))
                kw_img = kw_img.resize((new_w, new_h), Image.Resampling.BILINEAR)
                pos_x = int(kw["x"] - (new_w - kw_img.width) / 2)
                pos_y = int(kw["y"] - (new_h - kw_img.height) / 2)
            else:
                pos_x = kw["x"]
                pos_y = kw["y"]

            img.alpha_composite(kw_img, (pos_x, pos_y))
            break # Strictly one keyword at once

    # 2. RENDER BOTTOM CAPTIONS LAYER
    active_chunk = None
    for chunk in caption_chunks:
        if chunk["start"] - 0.05 <= t <= chunk["end"] + 0.15:
            active_chunk = chunk
            break

    if active_chunk:
        words = active_chunk["words"]
        word_renders = []
        total_text_w = 0
        space_w = font_caption.getbbox(" ")[2] - font_caption.getbbox(" ")[0]

        for w in words:
            w_text = w["word"].upper()
            w_bbox = font_caption.getbbox(w_text)
            w_w = w_bbox[2] - w_bbox[0]
            w_h = w_bbox[3] - w_bbox[1]
            is_active = (w["start"] <= t <= w["end"] + 0.08)
            word_renders.append({
                "text": w_text,
                "w": w_w,
                "h": w_h,
                "is_active": is_active,
                "bbox": w_bbox
            })
            total_text_w += w_w

        total_text_w += space_w * (len(words) - 1)

        cap_pad_x = 34
        cap_pad_y = 18
        box_w = total_text_w + cap_pad_x * 2
        box_h = 44 + cap_pad_y * 2
        box_x = (WIDTH - box_w) // 2
        box_y = 1350

        # High contrast background
        draw.rounded_rectangle(
            [box_x, box_y, box_x + box_w, box_y + box_h],
            radius=20,
            fill=(8, 12, 22, 225),
            outline=(255, 255, 255, 40),
            width=2
        )

        cur_x = box_x + cap_pad_x
        base_y = box_y + cap_pad_y

        for wr in word_renders:
            text_y = base_y - wr["bbox"][1] + 4
            if wr["is_active"]:
                # Radiant golden yellow highlight
                draw.text((cur_x + 1, text_y + 1), wr["text"], font=font_caption, fill=(0, 0, 0, 180))
                draw.text((cur_x, text_y), wr["text"], font=font_caption, fill=(255, 222, 0, 255))
            else:
                # Clean white
                draw.text((cur_x + 1, text_y + 1), wr["text"], font=font_caption, fill=(0, 0, 0, 140))
                draw.text((cur_x, text_y), wr["text"], font=font_caption, fill=(245, 245, 245, 255))
            
            cur_x += wr["w"] + space_w

    # 3. END-SCREEN CTA BADGE (Final 2.5 seconds)
    if t >= total_dur - 2.5:
        cta_p = min(1.0, (t - (total_dur - 2.5)) / 0.35)
        cta_alpha = int(255 * cta_p)
        cta_w = 700
        cta_h = 70
        cta_x = (WIDTH - cta_w) // 2
        cta_y = 1530

        draw.rounded_rectangle(
            [cta_x, cta_y, cta_x + cta_w, cta_y + cta_h],
            radius=20,
            fill=(15, 23, 42, int(235 * cta_p)),
            outline=(255, 184, 0, int(210 * cta_p)),
            width=2
        )
        cta_text = "Full 50-Year Breakdown Linked Below 🔗"
        cbbox = font_cta.getbbox(cta_text)
        ctw = cbbox[2] - cbbox[0]
        ctx = (WIDTH - ctw) // 2
        cty = cta_y + (cta_h - (cbbox[3] - cbbox[1])) // 2 - cbbox[1]
        draw.text((ctx, cty), cta_text, font=font_cta, fill=(255, 255, 255, cta_alpha))

    return img

def main():
    print(f"Opening source video: {RAW_VIDEO}")
    # Get total frames and duration from ffprobe
    probe_cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=nb_frames,duration", "-of", "json", RAW_VIDEO
    ]
    probe_out = subprocess.check_output(probe_cmd).decode("utf-8")
    probe_data = json.loads(probe_out)["streams"][0]
    total_frames = int(probe_data.get("nb_frames", 1934))
    total_dur = float(probe_data.get("duration", 32.233))
    print(f"Total Frames: {total_frames}, Total Duration: {total_dur:.2f}s @ {FPS} fps")

    # Start ffmpeg decoder process for raw RGB24 frames
    decode_cmd = [
        "ffmpeg", "-y", "-i", RAW_VIDEO,
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"
    ]
    decode_proc = subprocess.Popen(decode_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    # Start ffmpeg encoder process
    encode_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS),
        "-i", "-",
        "-i", AUDIO_FILE,
        "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        FINAL_OUTPUT
    ]
    encode_proc = subprocess.Popen(encode_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    frame_bytes_len = WIDTH * HEIGHT * 3
    print("Rendering video with composite captions + pop-up keywords...")

    frame_idx = 0
    while True:
        raw_bytes = decode_proc.stdout.read(frame_bytes_len)
        if not raw_bytes or len(raw_bytes) < frame_bytes_len:
            break

        t = frame_idx / FPS
        # Convert raw frame to PIL Image
        base_frame = Image.frombytes("RGB", (WIDTH, HEIGHT), raw_bytes)
        
        # Render overlay
        overlay = render_overlay_frame(t, total_dur)
        
        # Alpha composite
        base_rgba = base_frame.convert("RGBA")
        composite_rgba = Image.alpha_composite(base_rgba, overlay)
        composite_rgb = composite_rgba.convert("RGB")

        encode_proc.stdin.write(composite_rgb.tobytes())
        frame_idx += 1

        if frame_idx % 120 == 0 or frame_idx == total_frames:
            sys.stdout.write(f"\rRendered {frame_idx}/{total_frames} frames ({(frame_idx/total_frames)*100:.1f}%) [t={t:.2f}s]")
            sys.stdout.flush()

    print("\nFinalizing video stream...")
    decode_proc.stdout.close()
    decode_proc.wait()
    encode_proc.stdin.close()
    encode_proc.wait()

    print(f"SUCCESS: Final Short rendered to:\n{FINAL_OUTPUT}")

if __name__ == "__main__":
    main()
