"""
EP03 Master Full-Video Kinetic Keyword Overlay Generator
Renders 60fps transparent kinetic text overlay across all 7 scenes (00:00 - 05:18.60)
with elastic spring-pop punch-in animation, glowing typography, and margin-safe positioning.
"""
import os, sys, math, json, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA"))

def get_font(size):
    font_paths = [
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/impact.ttf",
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
    """Elastic overshoot easing: starts fast, overshoots, settles."""
    t = max(0.0, min(1.0, t))
    t -= 1.0
    return t * t * ((s + 1.0) * t + s) + 1.0

def ease_out_quad(t):
    t = max(0.0, min(1.0, t))
    return t * (2 - t)

# Palettes
CYAN  = (0, 240, 255)
GOLD  = (255, 184, 0)
RED   = (255, 75, 75)
GREEN = (16, 185, 129)
WHITE = (255, 255, 255)

# Full-Video Curated Keyword List (All 7 Scenes)
ALL_KEYWORDS = [
    # --- SCENE 1: THE HOOK (00:00.00 - 00:42.04) ---
    {"text": "SYSTEM",               "start": 0.96,  "end": 1.70,  "pos": (460, 420),  "color": CYAN,  "style": "glow"},
    {"text": "INTERACT",             "start": 1.82,  "end": 2.55,  "pos": (1440, 520), "color": WHITE, "style": "clean"},
    {"text": "HUMAN BEING",          "start": 5.80,  "end": 6.70,  "pos": (960, 300),  "color": GOLD,  "style": "glow"},
    {"text": "NEVER BUILT",          "start": 8.80,  "end": 9.70,  "pos": (460, 640),  "color": RED,   "style": "glow"},
    {"text": "KEEP YOU WATCHING",     "start": 14.30, "end": 15.70, "pos": (1420, 440), "color": CYAN,  "style": "glow"},
    {"text": "FRIGHTENINGLY GOOD",   "start": 16.70, "end": 17.90, "pos": (520, 360),  "color": GOLD,  "style": "glow"},
    {"text": "ALWAYS WRONG",         "start": 23.00, "end": 24.30, "pos": (1580, 240), "color": RED,   "style": "glow"},
    {"text": "OPTIMIZING",           "start": 27.60, "end": 28.80, "pos": (320, 860),  "color": CYAN,  "style": "glow"},
    {"text": "WILDLY DIFFERENT",     "start": 32.40, "end": 33.90, "pos": (1600, 860), "color": GOLD,  "style": "glow"},
    {"text": "REAL MECHANISM",       "start": 36.40, "end": 37.60, "pos": (480, 480),  "color": CYAN,  "style": "glow"},
    {"text": "EVERY PLATFORM",       "start": 39.70, "end": 41.20, "pos": (1400, 560), "color": WHITE, "style": "glow"},

    # --- SCENE 2: THE MYTH (00:42.04 - 01:22.32) ---
    {"text": "MOST PEOPLE",          "start": 42.50, "end": 43.60, "pos": (1620, 240), "color": WHITE, "style": "glow"},
    {"text": "POPULAR",              "start": 49.30, "end": 50.20, "pos": (280, 840),  "color": GOLD,  "style": "glow"},
    {"text": "TRENDING",             "start": 50.70, "end": 51.50, "pos": (1640, 840), "color": CYAN,  "style": "glow"},
    {"text": "ACTUALLY HAPPENING",    "start": 56.10, "end": 57.30, "pos": (960, 200),  "color": RED,   "style": "glow"},
    {"text": "SAME MOMENT",          "start": 60.30, "end": 61.30, "pos": (420, 400),  "color": WHITE, "style": "clean"},
    {"text": "DO NOT",               "start": 63.90, "end": 64.70, "pos": (1480, 420), "color": RED,   "style": "glow"},
    {"text": "TWO PEOPLE",           "start": 65.10, "end": 66.00, "pos": (460, 680),  "color": CYAN,  "style": "glow"},
    {"text": "DIFFERENT FEEDS",       "start": 70.20, "end": 71.50, "pos": (1460, 660), "color": GOLD,  "style": "glow"},
    {"text": "DIFFERENT SIGNALS",     "start": 72.70, "end": 73.90, "pos": (480, 320),  "color": WHITE, "style": "glow"},
    {"text": "PREDICTION SYSTEM",     "start": 77.50, "end": 78.90, "pos": (960, 260),  "color": CYAN,  "style": "glow"},
    {"text": "YOU SPECIFICALLY",      "start": 81.00, "end": 82.20, "pos": (1440, 520), "color": GOLD,  "style": "glow"},

    # --- SCENE 3: TWO-STAGE NEURAL ARCHITECTURE (01:22.32 - 02:02.72) ---
    {"text": "RESEARCH",             "start": 83.60,  "end": 84.60,  "pos": (260, 220),  "color": CYAN,  "style": "glow"},
    {"text": "TWO-STAGE",            "start": 88.00,  "end": 89.40,  "pos": (1660, 220), "color": GOLD,  "style": "glow"},
    {"text": "CANDIDATE GENERATION",  "start": 91.60,  "end": 93.00,  "pos": (960, 160),  "color": GOLD,  "style": "glow"},
    {"text": "MILLIONS",             "start": 94.50,  "end": 95.40,  "pos": (440, 520),  "color": RED,   "style": "glow"},
    {"text": "FEW HUNDRED",          "start": 99.60,  "end": 100.70, "pos": (1480, 540), "color": CYAN,  "style": "glow"},
    {"text": "WATCH HISTORY",        "start": 101.30, "end": 102.40, "pos": (480, 720),  "color": WHITE, "style": "clean"},
    {"text": "RANKING",              "start": 108.50, "end": 109.30, "pos": (1640, 220), "color": CYAN,  "style": "glow"},
    {"text": "SCORES EVERY ONE",     "start": 112.50, "end": 114.00, "pos": (260, 860),  "color": GOLD,  "style": "glow"},
    {"text": "OBJECTIVELY",          "start": 116.60, "end": 117.60, "pos": (1640, 860), "color": RED,   "style": "glow"},
    {"text": "KEEP YOU WATCHING",     "start": 119.80, "end": 121.40, "pos": (960, 880),  "color": CYAN,  "style": "glow"},

    # --- SCENE 4: WATCH TIME REVOLUTION (02:02.72 - 02:47.76) ---
    {"text": "NOBODY KNOWS",         "start": 124.80, "end": 126.00, "pos": (480, 360),  "color": WHITE, "style": "glow"},
    {"text": "MAXIMIZE CLICKS",      "start": 131.20, "end": 132.70, "pos": (1440, 420), "color": RED,   "style": "glow"},
    {"text": "MISLEADING",           "start": 137.90, "end": 139.10, "pos": (460, 660),  "color": RED,   "style": "glow"},
    {"text": "CLICKED MORE",         "start": 140.70, "end": 141.80, "pos": (1460, 640), "color": GOLD,  "style": "glow"},
    {"text": "CHANGED THE TARGET",   "start": 146.90, "end": 148.50, "pos": (960, 260),  "color": CYAN,  "style": "glow"},
    {"text": "WATCH TIME",           "start": 149.50, "end": 151.20, "pos": (1580, 240), "color": GOLD,  "style": "glow"},
    {"text": "KEEP WATCHING",        "start": 159.00, "end": 160.40, "pos": (280, 840),  "color": CYAN,  "style": "glow"},
    {"text": "SINGLE CHANGE",        "start": 161.40, "end": 162.60, "pos": (1640, 840), "color": GOLD,  "style": "glow"},
    {"text": "YOUR FEED TODAY",      "start": 165.50, "end": 166.80, "pos": (960, 900),  "color": WHITE, "style": "glow"},

    # --- SCENE 5: PERSONALIZATION PARADOX (02:47.76 - 03:32.24) ---
    {"text": "EXACT SAME",           "start": 169.60, "end": 170.80, "pos": (1640, 220), "color": WHITE, "style": "glow"},
    {"text": "DIFFERENTLY",          "start": 172.30, "end": 173.30, "pos": (260, 860),  "color": GOLD,  "style": "glow"},
    {"text": "PREDICTION TARGET",    "start": 178.10, "end": 179.30, "pos": (1640, 860), "color": CYAN,  "style": "glow"},
    {"text": "DOCUMENTARIES",        "start": 183.70, "end": 184.80, "pos": (440, 240),  "color": GREEN, "style": "glow"},
    {"text": "WATCH IT FULLY",       "start": 186.40, "end": 187.50, "pos": (440, 840),  "color": GREEN, "style": "glow"},
    {"text": "IDENTICAL VIDEO",      "start": 188.50, "end": 189.60, "pos": (1480, 240), "color": WHITE, "style": "clean"},
    {"text": "SHORT CLIPS",          "start": 191.20, "end": 192.00, "pos": (1480, 680), "color": RED,   "style": "glow"},
    {"text": "DROP OFF",             "start": 193.40, "end": 194.30, "pos": (1480, 840), "color": RED,   "style": "glow"},
    {"text": "TWO CREATORS",         "start": 198.90, "end": 200.00, "pos": (960, 180),  "color": GOLD,  "style": "glow"},
    {"text": "IDENTICAL CONTENT",    "start": 200.70, "end": 202.20, "pos": (960, 880),  "color": WHITE, "style": "glow"},
    {"text": "SPECIFIC OUTCOME",     "start": 209.20, "end": 210.40, "pos": (960, 220),  "color": CYAN,  "style": "glow"},

    # --- SCENE 6: THE RABBIT HOLE EFFECT (03:32.24 - 04:20.40) ---
    {"text": "SCRUTINY",             "start": 215.70, "end": 216.50, "pos": (480, 360),  "color": WHITE, "style": "glow"},
    {"text": "NARROW",               "start": 223.20, "end": 224.20, "pos": (1440, 440), "color": RED,   "style": "glow"},
    {"text": "EXTREME",              "start": 227.60, "end": 228.50, "pos": (460, 680),  "color": RED,   "style": "glow"},
    {"text": "NOT A SECRET",         "start": 233.60, "end": 234.60, "pos": (1620, 240), "color": GOLD,  "style": "glow"},
    {"text": "ACTIVELY RESHAPE",     "start": 247.90, "end": 249.40, "pos": (280, 840),  "color": RED,   "style": "glow"},
    {"text": "NOT PARANOIA",         "start": 251.80, "end": 253.00, "pos": (480, 380),  "color": WHITE, "style": "clean"},
    {"text": "DELIBERATELY",         "start": 257.30, "end": 258.20, "pos": (1420, 520), "color": CYAN,  "style": "glow"},

    # --- SCENE 7: CONCLUSION & 3 RULES (04:20.40 - 05:18.60) ---
    {"text": "ACTUALLY CHANGE",      "start": 263.10, "end": 264.70, "pos": (1600, 220), "color": CYAN,  "style": "glow"},
    {"text": "INDIVIDUAL PREDICTION","start": 269.80, "end": 271.50, "pos": (1600, 840), "color": GOLD,  "style": "glow"},
    {"text": "ATTENTION",            "start": 276.60, "end": 277.50, "pos": (280, 840),  "color": CYAN,  "style": "glow"},
    {"text": "NOT ACCURACY",         "start": 277.60, "end": 279.10, "pos": (1640, 840), "color": RED,   "style": "glow"},
    {"text": "DIFFERENT SIGNALS",     "start": 293.80, "end": 295.00, "pos": (460, 420),  "color": CYAN,  "style": "glow"},
    {"text": "GENUINELY DIFFERENT",  "start": 295.90, "end": 297.30, "pos": (1460, 500), "color": GOLD,  "style": "glow"},
    {"text": "MARKETS CRASH",        "start": 300.40, "end": 301.50, "pos": (440, 680),  "color": RED,   "style": "glow"},
    {"text": "RECESSIONS",           "start": 302.10, "end": 303.00, "pos": (1440, 660), "color": RED,   "style": "glow"},
    {"text": "NEXT BREAKDOWN",       "start": 307.90, "end": 309.00, "pos": (960, 320),  "color": CYAN,  "style": "glow"},
    {"text": "QUANTROVE",            "start": 315.60, "end": 316.80, "pos": (960, 540),  "color": GOLD,  "style": "glow"},
]

def render_keyword_card(text, color, style, font_size=58):
    """Pre-render a high-DPI text card with glowing shadow and sleek typography."""
    font = get_font(font_size)
    
    dummy_img = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
    dummy_draw = ImageDraw.Draw(dummy_img)
    bbox = dummy_draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    pad = 60
    cw = tw + pad * 2
    ch = th + pad * 2
    
    card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    tx = pad - bbox[0]
    ty = pad - bbox[1]
    
    # 1. Soft deep drop shadow for legibility against any background
    shadow_card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_card)
    for off in range(2, 6):
        s_draw.text((tx + off, ty + off), text, font=font, fill=(0, 0, 0, 190))
    shadow_card = shadow_card.filter(ImageFilter.GaussianBlur(radius=8))
    
    # 2. Subtle colored ambient halo if style == "glow"
    if style == "glow":
        glow_card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_card)
        g_color = (color[0], color[1], color[2], 140)
        g_draw.text((tx, ty), text, font=font, fill=g_color)
        glow_card = glow_card.filter(ImageFilter.GaussianBlur(radius=14))
        card = Image.alpha_composite(card, glow_card)
        
    card = Image.alpha_composite(card, shadow_card)
    
    # 3. Crisp sharp main text on top
    text_layer = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(text_layer)
    t_draw.text((tx, ty), text, font=font, fill=(color[0], color[1], color[2], 255))
    
    card = Image.alpha_composite(card, text_layer)
    return card, (cw // 2, ch // 2)

def generate_full_overlay(out_overlay_path, fps=60, total_duration=318.60):
    """Generate 60fps transparent alpha video across the entire video."""
    print(f"\n========================================================")
    print(f"Generating full 60fps kinetic overlay (318.60s, {len(ALL_KEYWORDS)} curated keywords)...")
    print(f"========================================================")
    
    cards = {}
    for kw in ALL_KEYWORDS:
        card, center = render_keyword_card(kw["text"], kw["color"], kw["style"])
        cards[kw["text"]] = (card, center)
        
    total_frames = int(math.ceil(total_duration * fps))
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-pix_fmt", "rgba",
        "-s", "1920x1080",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "qtrle",
        out_overlay_path
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    
    pop_duration = 0.22   # 220ms elastic spring pop-in
    fade_duration = 0.12  # 120ms fade-out
    empty_frame = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    
    for f in range(total_frames):
        t = f / fps
        active_kws = [kw for kw in ALL_KEYWORDS if kw["start"] <= t <= kw["end"]]
        
        if not active_kws:
            proc.stdin.write(empty_frame.tobytes())
            continue
            
        frame = empty_frame.copy()
        
        for kw in active_kws:
            card, (cx, cy) = cards[kw["text"]]
            elapsed = t - kw["start"]
            remaining = kw["end"] - t
            
            if elapsed < pop_duration:
                progress = elapsed / pop_duration
                scale = 0.35 + 0.65 * ease_out_back(progress, s=2.2)
                alpha = min(1.0, elapsed / 0.08)
            elif remaining < fade_duration:
                progress = remaining / fade_duration
                scale = 1.0 + 0.08 * (1.0 - progress)
                alpha = ease_out_quad(progress)
            else:
                hold_progress = (elapsed - pop_duration) / max(0.01, (kw["end"] - kw["start"] - pop_duration - fade_duration))
                scale = 1.0 + 0.04 * hold_progress
                alpha = 1.0
                
            scale = max(0.01, scale)
            target_w = int(card.width * scale)
            target_h = int(card.height * scale)
            
            scaled_card = card.resize((target_w, target_h), Image.Resampling.BILINEAR)
            
            if alpha < 0.99:
                r, g, b, a = scaled_card.split()
                a = a.point(lambda p: int(p * alpha))
                scaled_card = Image.merge("RGBA", (r, g, b, a))
                
            px, py = kw["pos"]
            x = px - target_w // 2
            y = py - target_h // 2
            
            frame.alpha_composite(scaled_card, (x, y))
            
        proc.stdin.write(frame.tobytes())
        
        if f % 1200 == 0:
            print(f"  Rendered {f}/{total_frames} frames ({f/total_frames*100:.1f}%)...")
            
    proc.stdin.close()
    proc.wait()
    print("\n✓ Full 5:19 master kinetic overlay rendered successfully!")

if __name__ == "__main__":
    overlay_out = os.path.join(TIMELINE_DIR, "00_OVERLAY_00m00s_to_05m19s_kinetic_word_pops_60fps.mov")
    generate_full_overlay(overlay_out)
