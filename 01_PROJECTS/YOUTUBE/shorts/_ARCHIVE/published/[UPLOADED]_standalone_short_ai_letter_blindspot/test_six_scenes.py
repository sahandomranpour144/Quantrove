import os
from PIL import Image, ImageDraw, ImageFont

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_BOLD = "C:/Windows/Fonts/seguibl.ttf"
font_sub = ImageFont.truetype(FONT_BOLD, 42)

test_scenes = [
    ("preview_frame_02s_hook.jpg", "AI CAN WRITE", "test_out_02s.jpg"),
    ("preview_frame_07s_guesses.jpg", "JUST GUESS WRONG", "test_out_07s.jpg"),
    ("preview_frame_15s_tokens.jpg", "CALLED TOKENS", "test_out_15s.jpg"),
    ("preview_frame_24s_blackbox.jpg", "IT'S GUESSING", "test_out_24s.jpg"),
    ("preview_frame_31s_blindspot.jpg", "BLIND SPOT EXPLAINS", "test_out_31s.jpg"),
    ("preview_frame_36s_cta.jpg", "AI YOU USE", "test_out_36s.jpg"),
]

for in_name, text, out_name in test_scenes:
    frame = Image.open(os.path.join(CURRENT_DIR, in_name)).convert("RGBA")
    overlay = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    bbox = font_sub.getbbox(text)
    sw = bbox[2] - bbox[0]
    sh = bbox[3] - bbox[1]
    pad_x, pad_y = 24, 14
    box_x = (1080 - sw) // 2
    box_y = 1350

    # Yellow fill box with black bold text
    draw.rounded_rectangle(
        [box_x - pad_x, box_y - pad_y, box_x + sw + pad_x, box_y + sh + pad_y],
        radius=14,
        fill=(255, 238, 0, 255),
        outline=(255, 255, 255, 180),
        width=2
    )
    draw.text((box_x, box_y - bbox[1]), text, font=font_sub, fill=(0, 0, 0, 255))

    final = Image.alpha_composite(frame, overlay).convert("RGB")
    final.save(os.path.join(CURRENT_DIR, out_name), "JPEG", quality=95)
    print(f"Rendered {out_name}")
