import os
import sys
import json
import math
from PIL import Image, ImageDraw, ImageFont

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_BOLD = "C:/Windows/Fonts/seguibl.ttf"

font_sub = ImageFont.truetype(FONT_BOLD, 44)
font_kw = ImageFont.truetype(FONT_BOLD, 34)

# Test rendering a sample frame with kinetic subtitle and pop-up keyword
frame = Image.open(os.path.join(CURRENT_DIR, "preview_frame_07s_guesses.jpg")).convert("RGBA")
overlay = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# 1. Pop-up keyword badge (Upper area: Y=220)
kw_text = "STRAWBERRY TEST"
kw_col = (255, 51, 102) # Crimson
kw_bbox = font_kw.getbbox(kw_text)
kw_w = kw_bbox[2] - kw_bbox[0]
kw_h = kw_bbox[3] - kw_bbox[1]
kw_pad_x, kw_pad_y = 24, 12
kw_x = (1080 - kw_w) // 2
kw_y = 200

# Capsule background with glowing border
draw.rounded_rectangle(
    [kw_x - kw_pad_x, kw_y - kw_pad_y, kw_x + kw_w + kw_pad_x, kw_y + kw_h + kw_pad_y],
    radius=16,
    fill=(10, 18, 32, 230),
    outline=kw_col,
    width=2
)
draw.text((kw_x, kw_y - kw_bbox[1]), kw_text, font=font_kw, fill=kw_col)

# 2. Kinetic subtitle yellow box (Lower-third: Y=1300)
sub_text = "HOW MANY R'S"
bbox = font_sub.getbbox(sub_text)
sw = bbox[2] - bbox[0]
sh = bbox[3] - bbox[1]
pad_x, pad_y = 24, 14
box_x = (1080 - sw) // 2
box_y = 1300

# Yellow fill box with black bold text
draw.rounded_rectangle(
    [box_x - pad_x, box_y - pad_y, box_x + sw + pad_x, box_y + sh + pad_y],
    radius=14,
    fill=(255, 238, 0, 255), # #FFEE00
    outline=(255, 255, 255, 180),
    width=2
)
draw.text((box_x, box_y - bbox[1]), sub_text, font=font_sub, fill=(0, 0, 0, 255))

final_sample = Image.alpha_composite(frame, overlay).convert("RGB")
out_sample = os.path.join(CURRENT_DIR, "test_kinetic_composite.jpg")
final_sample.save(out_sample, "JPEG", quality=95)
print(f"Saved test composite to: {out_sample}")
