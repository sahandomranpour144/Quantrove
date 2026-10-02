import os
import sys
import json
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.join(CURRENT_DIR, "TIMELINE_MEDIA")

RAW_VIDEO = os.path.join(CURRENT_DIR, "standalone_short_ai_letter_blindspot_raw_9x16.mp4")
AUDIO_FILE = os.path.join(CURRENT_DIR, "standalone_short_ai_letter_blindspot_audio.wav")
SRT_FILE = os.path.join(CURRENT_DIR, "ai_letter_blindspot_captions.srt")
FINAL_OUTPUT = os.path.join(CURRENT_DIR, "standalone_short_ai_letter_blindspot_FINAL.mp4")
OVERLAY_MOV = os.path.join(TIMELINE_DIR, "00_00m00s_to_00m43s_OVERLAY_kinetic_word_pops_60fps.mov")

FONT_BOLD = "C:/Windows/Fonts/seguibl.ttf"
if not os.path.exists(FONT_BOLD):
    FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"

FPS = 60
WIDTH = 1080
HEIGHT = 1920

# Load fonts
font_sub = ImageFont.truetype(FONT_BOLD, 42)
font_kw = ImageFont.truetype(FONT_BOLD, 34)

# Brand colors
CYAN = (0, 240, 255)
MINT = (0, 255, 163)
GOLD = (255, 215, 0)
CRIMSON = (255, 51, 102)
WHITE = (255, 255, 255)
YELLOW_BOX = (255, 238, 0) # #FFEE00 solid yellow
BLACK = (0, 0, 0)

POPUP_KEYWORDS = [
    {"text": "WRITES A NOVEL", "start": 0.50, "end": 4.50, "color": CYAN},
    {"text": "STRAWBERRY TEST", "start": 5.00, "end": 8.50, "color": CRIMSON},
    {"text": "CAN'T SEE LETTERS", "start": 9.50, "end": 11.80, "color": GOLD},
    {"text": "TOKEN CHUNKS", "start": 15.00, "end": 18.00, "color": MINT},
    {"text": "[ 496 ] + [ 675 ]", "start": 18.50, "end": 22.00, "color": CYAN},
    {"text": "GUESSING, NOT COUNTING", "start": 25.00, "end": 29.00, "color": CRIMSON},
    {"text": "THE TOKEN BLIND SPOT", "start": 34.50, "end": 38.50, "color": GOLD},
    {"text": "SUBSCRIBE @QUANTROVE", "start": 39.50, "end": 43.00, "color": MINT},
]

def parse_srt(srt_path):
    """Parses SRT file into a list of subtitle chunks."""
    chunks = []
    with open(srt_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        if line.isdigit():
            # Caption index
            i += 1
            if i >= len(lines):
                break
            time_line = lines[i]
            if "-->" in time_line:
                parts = time_line.split("-->")
                start_parts = parts[0].strip().replace(",", ".").split(":")
                end_parts = parts[1].strip().replace(",", ".").split(":")

                start_s = float(start_parts[0]) * 3600 + float(start_parts[1]) * 60 + float(start_parts[2])
                end_s = float(end_parts[0]) * 3600 + float(end_parts[1]) * 60 + float(end_parts[2])

                i += 1
                text_lines = []
                while i < len(lines) and lines[i]:
                    text_lines.append(lines[i])
                    i += 1
                text = " ".join(text_lines).upper()
                chunks.append({
                    "start": start_s,
                    "end": end_s,
                    "text": text
                })
        i += 1
    return chunks

def ease_out_back(p):
    """Elastic spring-pop easing function."""
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * math.pow(p - 1, 3) + c1 * math.pow(p - 1, 2)

def render_overlay_elements(overlay_draw, t, caption_chunks):
    """Renders subtitle box and kinetic popups onto an RGBA ImageDraw context."""
    # 1. POP-UP KEYWORDS (Upper-third: Y=200)
    return_card = None
    for kw in POPUP_KEYWORDS:
        if kw["start"] <= t <= kw["end"]:
            rel_t = t - kw["start"]
            k_dur = kw["end"] - kw["start"]

            # Entry spring pop
            if rel_t < 0.12:
                p = rel_t / 0.12
                scale = max(0.85, min(1.10, ease_out_back(p)))
                alpha = int(255 * p)
            elif rel_t > k_dur - 0.10:
                p = (k_dur - rel_t) / 0.10
                scale = 1.0
                alpha = int(255 * max(0.0, p))
            else:
                scale = 1.0
                alpha = 255

            kw_text = kw["text"]
            col = kw["color"]
            kw_bbox = font_kw.getbbox(kw_text)
            kw_w = kw_bbox[2] - kw_bbox[0]
            kw_h = kw_bbox[3] - kw_bbox[1]
            pad_x, pad_y = 24, 12

            # Center at X=540, Y=200
            cw = kw_w + pad_x * 2
            ch = kw_h + pad_y * 2

            card_img = Image.new("RGBA", (cw + 20, ch + 20), (0, 0, 0, 0))
            card_draw = ImageDraw.Draw(card_img)

            # Glass card with border
            card_draw.rounded_rectangle(
                [10, 10, 10 + cw, 10 + ch],
                radius=16,
                fill=(10, 18, 32, int(230 * (alpha / 255))),
                outline=(col[0], col[1], col[2], int(220 * (alpha / 255))),
                width=2
            )
            card_draw.text((10 + pad_x, 10 + pad_y - kw_bbox[1]), kw_text, font=font_kw, fill=(col[0], col[1], col[2], alpha))

            if abs(scale - 1.0) > 0.01:
                nw = max(1, int(card_img.width * scale))
                nh = max(1, int(card_img.height * scale))
                card_img = card_img.resize((nw, nh), Image.Resampling.BILINEAR)
                pos_x = int(540 - card_img.width / 2)
                pos_y = int(200 - card_img.height / 2)
            else:
                pos_x = int(540 - card_img.width / 2)
                pos_y = int(200 - card_img.height / 2)

            # Composite onto overlay
            return_card = (card_img, (pos_x, pos_y))
            break

    # 2. KINETIC SUBTITLE BOX (Lower-third: Y=1350)
    sub_box = None
    for chunk in caption_chunks:
        if chunk["start"] <= t <= chunk["end"] + 0.05:
            rel_t = t - chunk["start"]
            c_dur = chunk["end"] - chunk["start"]

            # Fast bounce-pop on block entry (0.08s)
            if rel_t < 0.08:
                p = rel_t / 0.08
                scale = max(0.88, min(1.10, ease_out_back(p)))
                alpha = int(255 * p)
            elif rel_t > c_dur:
                p = (c_dur + 0.05 - rel_t) / 0.05
                scale = 1.0
                alpha = int(255 * max(0.0, p))
            else:
                scale = 1.0
                alpha = 255

            sub_text = chunk["text"]
            bbox = font_sub.getbbox(sub_text)
            sw = bbox[2] - bbox[0]
            sh = bbox[3] - bbox[1]
            pad_x, pad_y = 24, 14

            bw = sw + pad_x * 2
            bh = sh + pad_y * 2

            sub_img = Image.new("RGBA", (bw + 20, bh + 20), (0, 0, 0, 0))
            sub_draw = ImageDraw.Draw(sub_img)

            # Solid #FFEE00 yellow fill box
            sub_draw.rounded_rectangle(
                [10, 10, 10 + bw, 10 + bh],
                radius=14,
                fill=(YELLOW_BOX[0], YELLOW_BOX[1], YELLOW_BOX[2], alpha),
                outline=(255, 255, 255, int(180 * (alpha / 255))),
                width=2
            )
            # Black bold text
            sub_draw.text((10 + pad_x, 10 + pad_y - bbox[1]), sub_text, font=font_sub, fill=(BLACK[0], BLACK[1], BLACK[2], alpha))

            if abs(scale - 1.0) > 0.01:
                nw = max(1, int(sub_img.width * scale))
                nh = max(1, int(sub_img.height * scale))
                sub_img = sub_img.resize((nw, nh), Image.Resampling.BILINEAR)
                pos_x = int(540 - sub_img.width / 2)
                pos_y = int(1350 - sub_img.height / 2)
            else:
                pos_x = int(540 - sub_img.width / 2)
                pos_y = int(1350 - sub_img.height / 2)

            sub_box = (sub_img, (pos_x, pos_y))
            break

    return (return_card, sub_box)

def render_final_video():
    print("==================================================")
    print("🎬 RENDERING FINAL SHORT WITH BURNED-IN CAPTIONS")
    print(f"Target: {FINAL_OUTPUT}")
    print("==================================================")

    caption_chunks = parse_srt(SRT_FILE)
    print(f"Loaded {len(caption_chunks)} caption blocks from SRT.")

    # Probe duration
    probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", RAW_VIDEO]
    probe_out = subprocess.check_output(probe_cmd).decode("utf-8")
    total_dur = float(json.loads(probe_out)["format"]["duration"])
    total_frames = int(total_dur * FPS)
    print(f"Total Duration: {total_dur:.3f}s ({total_frames} frames @ {FPS} fps)")

    # 1. Setup raw video decode pipe
    decode_cmd = [
        "ffmpeg", "-i", RAW_VIDEO,
        "-f", "image2pipe", "-pix_fmt", "rgb24", "-vcodec", "rawvideo", "-"
    ]
    decode_proc = subprocess.Popen(decode_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    # 2. Setup video encode pipe for FINAL MP4
    encode_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS),
        "-i", "-",
        "-i", AUDIO_FILE,
        "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        FINAL_OUTPUT
    ]
    encode_proc = subprocess.Popen(encode_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    frame_bytes_len = WIDTH * HEIGHT * 3
    print("Rendering composite frames...")

    for frame_idx in range(total_frames):
        raw_frame = decode_proc.stdout.read(frame_bytes_len)
        if len(raw_frame) < frame_bytes_len:
            break

        t = frame_idx / FPS
        base_img = Image.frombytes("RGB", (WIDTH, HEIGHT), raw_frame)

        # Overlay drawing
        overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        kw_card, sub_box = render_overlay_elements(None, t, caption_chunks)

        if kw_card:
            card_img, pos = kw_card
            overlay.alpha_composite(card_img, pos)

        if sub_box:
            sub_img, pos = sub_box
            overlay.alpha_composite(sub_img, pos)

        final_img = Image.alpha_composite(base_img.convert("RGBA"), overlay).convert("RGB")
        encode_proc.stdin.write(final_img.tobytes())

        if (frame_idx + 1) % 300 == 0 or frame_idx == total_frames - 1:
            print(f"  Frame {frame_idx + 1}/{total_frames} ({100 * (frame_idx + 1) / total_frames:.1f}%)")

    decode_proc.stdout.close()
    encode_proc.stdin.close()
    decode_proc.wait()
    encode_proc.wait()

    print(f"✅ FINAL Short rendered successfully: {FINAL_OUTPUT}")
    print(f"📏 Size: {os.path.getsize(FINAL_OUTPUT) / (1024*1024):.2f} MB")

def render_capcut_overlay():
    print("\n==================================================")
    print("🎬 RENDERING TRANSPARENT MOV OVERLAY FOR CAPCUT")
    print(f"Target: {OVERLAY_MOV}")
    print("==================================================")

    caption_chunks = parse_srt(SRT_FILE)

    probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", RAW_VIDEO]
    probe_out = subprocess.check_output(probe_cmd).decode("utf-8")
    total_dur = float(json.loads(probe_out)["format"]["duration"])
    total_frames = int(total_dur * FPS)

    # Setup ProRes 4444 encode pipe
    encode_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS),
        "-i", "-",
        "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le",
        "-t", f"{total_dur:.3f}",
        OVERLAY_MOV
    ]
    encode_proc = subprocess.Popen(encode_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    for frame_idx in range(total_frames):
        t = frame_idx / FPS
        overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        kw_card, sub_box = render_overlay_elements(None, t, caption_chunks)

        if kw_card:
            card_img, pos = kw_card
            overlay.alpha_composite(card_img, pos)

        if sub_box:
            sub_img, pos = sub_box
            overlay.alpha_composite(sub_img, pos)

        encode_proc.stdin.write(overlay.tobytes())

        if (frame_idx + 1) % 450 == 0 or frame_idx == total_frames - 1:
            print(f"  Overlay Frame {frame_idx + 1}/{total_frames} ({100 * (frame_idx + 1) / total_frames:.1f}%)")

    encode_proc.stdin.close()
    encode_proc.wait()

    print(f"✅ Transparent MOV Overlay rendered: {OVERLAY_MOV}")
    print(f"📏 Size: {os.path.getsize(OVERLAY_MOV) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    render_final_video()
    render_capcut_overlay()
