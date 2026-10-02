import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1080
HEIGHT = 1920

# Brand colors
BG = (32, 35, 34, 255)            # Raisin Black #202322
CHROME = (35, 61, 76, 255)        # Charcoal Slate #233D4C
LIME = (195, 216, 9, 255)         # Power Lime #C3D809
PUMPKIN = (253, 128, 46, 255)     # Pumpkin #FD802E
TEXT = (230, 237, 243, 255)       # Off-White #E6EDF3
MUTED = (139, 154, 152, 255)

FONT_PATH = "assets/fonts/Nohemi-Bold.ttf"
FONT_MED_PATH = "assets/fonts/Nohemi-Medium.ttf"

def draw_grid(draw):
    for x in range(0, WIDTH, 60):
        draw.line([(x, 0), (x, HEIGHT)], fill=(35, 61, 76, 70), width=1)
    for y in range(0, HEIGHT, 60):
        draw.line([(0, y), (WIDTH, y)], fill=(35, 61, 76, 70), width=1)

def add_glow_rect(img, box, color, blur_radius=25, stroke_width=4):
    glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.rounded_rectangle(box, radius=16, outline=color, width=stroke_width)
    glow = glow.filter(ImageFilter.GaussianBlur(blur_radius))
    img.alpha_composite(glow)
    # Crisp outline
    cdraw = ImageDraw.Draw(img)
    cdraw.rounded_rectangle(box, radius=16, outline=color, width=stroke_width)

def generate_image_1(out_path):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    # Top header badge
    add_glow_rect(img, [100, 180, 980, 280], LIME, blur_radius=20, stroke_width=3)
    idraw = ImageDraw.Draw(img)
    font_h1 = ImageFont.truetype(FONT_PATH, 38)
    idraw.text((WIDTH//2, 230), "STATIONARY OBJECT DETECTION", font=font_h1, fill=LIME, anchor="mm")

    # Center bounding box for Cat
    box_cat = [180, 480, 900, 1280]
    add_glow_rect(img, box_cat, LIME, blur_radius=35, stroke_width=4)

    # Corner reticles (Targeting brackets)
    c_len = 50
    for corner in [(180, 480), (900, 480), (180, 1280), (900, 1280)]:
        cx, cy = corner
        sx = 1 if cx == 180 else -1
        sy = 1 if cy == 480 else -1
        idraw.line([(cx, cy), (cx + sx * c_len, cy)], fill=LIME, width=8)
        idraw.line([(cx, cy), (cx, cy + sy * c_len)], fill=LIME, width=8)

    # Geometric Cat Silhouette inside the box
    cat_points = [
        (380, 1100), (360, 900), (320, 750), (280, 680), (340, 620), (390, 700),
        (540, 700), (690, 700), (740, 620), (800, 680), (760, 750), (720, 900),
        (700, 1100), (540, 1150)
    ]
    # Draw glowing outline for cat
    glow_cat = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow_cat)
    gdraw.polygon(cat_points, outline=LIME, fill=(195, 216, 9, 30))
    glow_cat = glow_cat.filter(ImageFilter.GaussianBlur(18))
    img.alpha_composite(glow_cat)

    idraw = ImageDraw.Draw(img)
    idraw.polygon(cat_points, outline=LIME, fill=(195, 216, 9, 45))

    # Cat eyes (Glowing Lime)
    idraw.ellipse([440, 760, 480, 800], fill=LIME)
    idraw.ellipse([600, 760, 640, 800], fill=LIME)

    # Scan lines
    for y in range(500, 1260, 35):
        idraw.line([(190, y), (890, y)], fill=(195, 216, 9, 50), width=1)

    # Telemetry data overlay
    font_med = ImageFont.truetype(FONT_MED_PATH, 28)
    font_bold = ImageFont.truetype(FONT_PATH, 32)
    idraw.text((220, 520), "TARGET: FELIS CATUS", font=font_bold, fill=TEXT)
    idraw.text((220, 565), "CONFIDENCE: 99.84% [OPTIMAL]", font=font_med, fill=LIME)

    # Bottom status card
    add_glow_rect(img, [120, 1380, 960, 1680], (35, 61, 76, 255), blur_radius=15, stroke_width=2)
    idraw = ImageDraw.Draw(img)
    idraw.text((WIDTH//2, 1440), "PHYSICAL RULES NEVER MUTATE", font=font_bold, fill=TEXT, anchor="mm")
    idraw.text((WIDTH//2, 1510), "The cat does not change shape", font=font_med, fill=MUTED, anchor="mm")
    idraw.text((WIDTH//2, 1560), "because the AI got good at recognizing it.", font=font_med, fill=LIME, anchor="mm")
    idraw.text((WIDTH//2, 1630), "RESULT: STATIONARY ACCURACY = 99.8%", font=font_bold, fill=LIME, anchor="mm")

    img.convert("RGB").save(out_path, quality=95)
    print("Generated Image 1:", out_path)

def generate_image_2(out_path):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    # Header
    add_glow_rect(img, [100, 160, 980, 260], PUMPKIN, blur_radius=20, stroke_width=3)
    idraw = ImageDraw.Draw(img)
    font_h1 = ImageFont.truetype(FONT_PATH, 36)
    idraw.text((WIDTH//2, 210), "CAPITAL RUSHING IN (THE SIGNAL)", font=font_h1, fill=PUMPKIN, anchor="mm")

    # Order book depth bars (Heatmap)
    font_med = ImageFont.truetype(FONT_MED_PATH, 26)
    font_bold = ImageFont.truetype(FONT_PATH, 30)

    # Top selling pressure (Pumpkin)
    idraw.text((120, 320), "INSTITUTIONAL BUY VOLUME SWARM", font=font_bold, fill=LIME)
    np.random.seed(101)
    for i in range(8):
        y = 380 + i * 55
        w = int(250 + np.random.rand() * 550)
        # Glowing bar
        add_glow_rect(img, [120, y, 120 + w, y + 42], LIME, blur_radius=15, stroke_width=2)
        idraw = ImageDraw.Draw(img)
        idraw.rectangle([120, y, 120 + w, y + 42], fill=(195, 216, 9, 80))
        idraw.text((140, y + 21), f"ALGO CLUSTER #{i+1} : +${np.random.randint(15, 85)}M", font=font_med, fill=TEXT, anchor="lm")

    # Mid divider: The flash breakout
    add_glow_rect(img, [100, 880, 980, 1080], PUMPKIN, blur_radius=28, stroke_width=4)
    idraw = ImageDraw.Draw(img)
    idraw.text((WIDTH//2, 940), "BUYING PRESSURE INSTANTLY", font=font_bold, fill=PUMPKIN, anchor="mm")
    idraw.text((WIDTH//2, 1010), "DRIVES THE PRICE UP TODAY", font=font_h1, fill=TEXT, anchor="mm")

    # Bottom chart: dodge trajectory
    chart_box = [120, 1160, 960, 1680]
    add_glow_rect(img, chart_box, CHROME, blur_radius=15, stroke_width=2)
    idraw = ImageDraw.Draw(img)

    # Drawing neon price curve
    pts = []
    for x in range(150, 930, 15):
        norm_x = (x - 150) / 780.0
        y = 1500 - int(math.sin(norm_x * 4.0) * 160 + norm_x * 120)
        pts.append((x, y))

    # Glow line
    glow_line = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow_line)
    gdraw.line(pts, fill=PUMPKIN, width=12)
    glow_line = glow_line.filter(ImageFilter.GaussianBlur(20))
    img.alpha_composite(glow_line)

    idraw = ImageDraw.Draw(img)
    idraw.line(pts, fill=PUMPKIN, width=4)

    # Arrow pointing up
    idraw.line([(750, 1380), (880, 1250)], fill=LIME, width=6)
    idraw.polygon([(880, 1250), (840, 1265), (865, 1290)], fill=LIME)
    idraw.text((620, 1260), "CAPITAL DISCOVERY", font=font_bold, fill=LIME)

    img.convert("RGB").save(out_path, quality=95)
    print("Generated Image 2:", out_path)

def generate_image_3(out_path):
    img = Image.new("RGBA", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    draw_grid(draw)

    # Big Glowing Warning Stamp
    add_glow_rect(img, [100, 320, 980, 720], PUMPKIN, blur_radius=40, stroke_width=5)
    idraw = ImageDraw.Draw(img)

    font_huge = ImageFont.truetype(FONT_PATH, 52)
    font_bold = ImageFont.truetype(FONT_PATH, 34)
    font_med = ImageFont.truetype(FONT_MED_PATH, 28)

    idraw.text((WIDTH//2, 420), "PREDICTION ERASES", font=font_huge, fill=PUMPKIN, anchor="mm")
    idraw.text((WIDTH//2, 510), "THE PATTERN", font=font_huge, fill=TEXT, anchor="mm")

    add_glow_rect(img, [160, 580, 920, 670], PUMPKIN, blur_radius=15, stroke_width=2)
    idraw = ImageDraw.Draw(img)
    idraw.rectangle([160, 580, 920, 670], fill=(253, 128, 46, 50))
    idraw.text((WIDTH//2, 625), "SIGNAL SELF-DESTRUCTION : 100%", font=font_bold, fill=PUMPKIN, anchor="mm")

    # Center comparison metrics
    add_glow_rect(img, [120, 800, 960, 1400], CHROME, blur_radius=20, stroke_width=2)
    idraw = ImageDraw.Draw(img)

    idraw.text((160, 860), "ALPHA AT DISCOVERY: +12.0%", font=font_bold, fill=LIME)
    idraw.text((160, 920), "COMPETING BOTS FLOODING: 1,420+", font=font_med, fill=MUTED)

    # Flatline graphic
    flat_y = 1040
    idraw.line([(160, flat_y), (920, flat_y)], fill=PUMPKIN, width=6)
    # Glowing flatline
    glow_flat = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow_flat)
    gdraw.line([(160, flat_y), (920, flat_y)], fill=PUMPKIN, width=16)
    glow_flat = glow_flat.filter(ImageFilter.GaussianBlur(15))
    img.alpha_composite(glow_flat)

    idraw = ImageDraw.Draw(img)
    idraw.text((WIDTH//2, 1100), "EQUILIBRIUM REACHED (EDGE = 0.0%)", font=font_bold, fill=PUMPKIN, anchor="mm")
    idraw.text((WIDTH//2, 1160), "The edge self-destructs the moment it's found", font=font_med, fill=TEXT, anchor="mm")

    # Bottom takeaway
    add_glow_rect(img, [120, 1500, 960, 1720], LIME, blur_radius=25, stroke_width=3)
    idraw = ImageDraw.Draw(img)
    idraw.text((WIDTH//2, 1570), "MARKETS ARE REFLEXIVE", font=font_huge, fill=LIME, anchor="mm")
    idraw.text((WIDTH//2, 1650), "QUANTROVE DATA INTELLIGENCE", font=font_med, fill=TEXT, anchor="mm")

    img.convert("RGB").save(out_path, quality=95)
    print("Generated Image 3:", out_path)

if __name__ == "__main__":
    out_dir = "01_PROJECTS/YOUTUBE/shorts/[IN_PROGRESS 2026-09-23]_ep04_short_cat_vs_market_reflexivity/TIMELINE_MEDIA"
    generate_image_1(os.path.join(out_dir, "02_00m00s_to_00m04s_image_01_computer_vision_cat_glow.png"))
    generate_image_2(os.path.join(out_dir, "02_00m14s_to_00m18s_image_02_algorithmic_buying_pressure_glow.png"))
    generate_image_3(os.path.join(out_dir, "02_00m26s_to_00m30s_image_03_signal_erased_self_destruct_glow.png"))
