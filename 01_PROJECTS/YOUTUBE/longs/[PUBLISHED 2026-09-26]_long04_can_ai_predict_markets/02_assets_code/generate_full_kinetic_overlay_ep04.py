"""
EP04 Master Full-Video Kinetic Keyword Overlay Generator
Renders 60fps transparent kinetic text overlay across all 6 scenes (00:00 - 07:05.47)
with elastic spring-pop punch-in animation, glowing typography, and margin-safe positioning.
Output: TIMELINE_MEDIA/00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps.mov
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

# Palettes (Quantrove Dark Luxury Standard)
CYAN  = (0, 240, 255)
GOLD  = (255, 184, 0)
MINT  = (0, 255, 163)
RED   = (255, 75, 75)
WHITE = (255, 255, 255)

ALL_KEYWORDS = [
    # --- SCENE 1: THE SIMONS PARADOX & THE HOOK (0:00 - 1:06.81) ---
    {"text": "1988",                         "start": 0.50,   "end": 1.70,   "pos": (440, 300),  "color": CYAN,  "style": "glow"},
    {"text": "JIM SIMONS",                   "start": 5.10,   "end": 6.40,   "pos": (1480, 260), "color": GOLD,  "style": "glow"},
    {"text": "MATHEMATICALLY IMPOSSIBLE",     "start": 8.50,   "end": 10.50,  "pos": (960, 220),  "color": RED,   "style": "glow"},
    {"text": "30 YEARS",                     "start": 12.00,  "end": 13.50,  "pos": (420, 820),  "color": WHITE, "style": "clean"},
    {"text": "+66% A YEAR",                  "start": 16.50,  "end": 18.50,  "pos": (1500, 820), "color": GOLD,  "style": "glow"},
    {"text": "$1,000 -> $42,000,000",        "start": 20.00,  "end": 22.80,  "pos": (960, 840),  "color": GOLD,  "style": "glow"},
    {"text": "ONE STRICT RULE",              "start": 25.00,  "end": 26.80,  "pos": (440, 320),  "color": RED,   "style": "glow"},
    {"text": "BANNED FINANCE DEGREES",       "start": 27.50,  "end": 30.50,  "pos": (1460, 340), "color": RED,   "style": "glow"},
    {"text": "PHYSICISTS & MATHEMATICIANS",   "start": 32.50,  "end": 35.50,  "pos": (960, 220),  "color": CYAN,  "style": "glow"},
    {"text": "SPEND BILLIONS",               "start": 38.50,  "end": 40.00,  "pos": (420, 780),  "color": WHITE, "style": "clean"},
    {"text": "NEURAL NETWORKS",              "start": 40.20,  "end": 42.00,  "pos": (1480, 780), "color": CYAN,  "style": "glow"},
    {"text": "FAIL TO BEAT",                 "start": 45.00,  "end": 47.00,  "pos": (960, 860),  "color": RED,   "style": "glow"},
    {"text": "51% COIN FLIP",                "start": 52.50,  "end": 54.80,  "pos": (440, 280),  "color": GOLD,  "style": "glow"},
    {"text": "FAIL EVERY DAY",               "start": 56.50,  "end": 58.50,  "pos": (1480, 280), "color": RED,   "style": "glow"},
    {"text": "REAL MATHEMATICS",             "start": 61.00,  "end": 62.80,  "pos": (440, 820),  "color": CYAN,  "style": "glow"},
    {"text": "CANNOT PREDICT",               "start": 63.20,  "end": 65.00,  "pos": (1480, 820), "color": RED,   "style": "glow"},

    # --- SCENE 2: THE 50.75% EDGE & REFLEXIVITY (1:06.81 - 2:29.46) ---
    {"text": "GREAT ILLUSION",               "start": 68.20,  "end": 70.00,  "pos": (460, 260),  "color": WHITE, "style": "glow"},
    {"text": "NOT 90% ACCURACY",             "start": 76.50,  "end": 78.80,  "pos": (1480, 260), "color": RED,   "style": "glow"},
    {"text": "STATISTICAL EDGE",             "start": 81.20,  "end": 82.80,  "pos": (440, 840),  "color": CYAN,  "style": "glow"},
    {"text": "MICROSCOPIC: 50.75%",          "start": 84.00,  "end": 86.80,  "pos": (1460, 840), "color": GOLD,  "style": "glow"},
    {"text": "LAW OF LARGE NUMBERS",         "start": 90.00,  "end": 92.20,  "pos": (960, 220),  "color": CYAN,  "style": "glow"},
    {"text": "MILLIONS OF TRADES",           "start": 92.80,  "end": 94.80,  "pos": (440, 360),  "color": GOLD,  "style": "glow"},
    {"text": "BILLIONS IN PROFIT",           "start": 97.50,  "end": 99.50,  "pos": (1480, 360), "color": MINT,  "style": "glow"},
    {"text": "GENERATIVE AI",                "start": 102.20, "end": 104.00, "pos": (440, 820),  "color": CYAN,  "style": "glow"},
    {"text": "DECADES OF DATA",              "start": 104.80, "end": 106.80, "pos": (1480, 820), "color": WHITE, "style": "clean"},
    {"text": "REACT TO BEING PREDICTED",     "start": 113.20, "end": 116.00, "pos": (960, 220),  "color": RED,   "style": "glow"},
    {"text": "IMAGE RECOGNITION",            "start": 117.80, "end": 119.80, "pos": (440, 280),  "color": WHITE, "style": "clean"},
    {"text": "CAT NEVER CHANGES",            "start": 121.50, "end": 124.00, "pos": (1480, 280), "color": CYAN,  "style": "glow"},
    {"text": "ZERO-SUM GAME",                "start": 128.00, "end": 130.00, "pos": (960, 840),  "color": RED,   "style": "glow"},
    {"text": "BUYING PRESSURE",              "start": 140.00, "end": 142.00, "pos": (440, 820),  "color": GOLD,  "style": "glow"},
    {"text": "ERASES THE PATTERN",           "start": 144.20, "end": 146.50, "pos": (1480, 820), "color": RED,   "style": "glow"},
    {"text": "SELF-DESTRUCTS",               "start": 148.00, "end": 150.20, "pos": (960, 220),  "color": RED,   "style": "glow"},

    # --- SCENE 3: ALPHA DECAY (2:29.46 - 3:21.55) ---
    {"text": "ALPHA DECAY",                  "start": 154.50, "end": 156.80, "pos": (440, 240),  "color": CYAN,  "style": "glow"},
    {"text": "EXPIRING PATENT",              "start": 164.20, "end": 166.50, "pos": (1480, 240), "color": GOLD,  "style": "glow"},
    {"text": "TRADING ANOMALY",              "start": 167.50, "end": 169.50, "pos": (420, 840),  "color": WHITE, "style": "clean"},
    {"text": "VOLUME SPIKES",                "start": 175.20, "end": 177.20, "pos": (1480, 840), "color": CYAN,  "style": "glow"},
    {"text": "CROWD THE TRADE",              "start": 182.00, "end": 184.00, "pos": (440, 280),  "color": RED,   "style": "glow"},
    {"text": "COMPRESS SPREADS",             "start": 185.00, "end": 187.00, "pos": (1480, 280), "color": RED,   "style": "glow"},
    {"text": "EQUILIBRIUM",                  "start": 188.20, "end": 190.50, "pos": (960, 840),  "color": WHITE, "style": "glow"},
    {"text": "BRILLIANT IN BACKTEST",        "start": 192.20, "end": 194.50, "pos": (440, 780),  "color": GOLD,  "style": "glow"},
    {"text": "DEAD IN 4 MONTHS",             "start": 195.50, "end": 197.80, "pos": (1480, 780), "color": RED,   "style": "glow"},
    {"text": "MARKET ADAPTED",               "start": 201.50, "end": 204.00, "pos": (960, 220),  "color": CYAN,  "style": "glow"},

    # --- SCENE 4: THE OVERFITTING TRAP (3:21.55 - 4:33.60) ---
    {"text": "FATAL FLAW",                   "start": 205.00, "end": 206.80, "pos": (440, 240),  "color": RED,   "style": "glow"},
    {"text": "THE OVERFITTING TRAP",         "start": 210.50, "end": 213.00, "pos": (1460, 240), "color": RED,   "style": "glow"},
    {"text": "LOW SIGNAL-TO-NOISE",          "start": 215.80, "end": 218.00, "pos": (440, 840),  "color": WHITE, "style": "clean"},
    {"text": "95% PURE NOISE",               "start": 231.50, "end": 234.00, "pos": (1480, 840), "color": RED,   "style": "glow"},
    {"text": "BILLIONS OF PARAMETERS",       "start": 237.80, "end": 240.20, "pos": (960, 220),  "color": CYAN,  "style": "glow"},
    {"text": "30 YEARS OF NOISE",            "start": 241.50, "end": 243.80, "pos": (440, 320),  "color": WHITE, "style": "clean"},
    {"text": "PHANTOM CORRELATIONS",         "start": 248.00, "end": 250.50, "pos": (1480, 320), "color": GOLD,  "style": "glow"},
    {"text": "STRAIGHT LINE BACKTEST",       "start": 260.00, "end": 262.50, "pos": (440, 820),  "color": GOLD,  "style": "glow"},
    {"text": "REAL CAPITAL",                 "start": 265.50, "end": 267.50, "pos": (1480, 820), "color": WHITE, "style": "clean"},
    {"text": "EVAPORATES IMMEDIATELY",       "start": 271.20, "end": 273.80, "pos": (960, 840),  "color": RED,   "style": "glow"},

    # --- SCENE 5: THE 4 REAL ENGINES (4:33.60 - 6:07.53) ---
    {"text": "SPEND FORTUNES",               "start": 280.20, "end": 282.20, "pos": (440, 240),  "color": GOLD,  "style": "glow"},
    {"text": "NAIVE QUESTION",               "start": 283.50, "end": 285.50, "pos": (1480, 240), "color": RED,   "style": "glow"},
    {"text": "4 REAL ENGINES",               "start": 290.50, "end": 293.00, "pos": (960, 220),  "color": CYAN,  "style": "glow"},
    {"text": "ENGINE 1: RISK MODELING",       "start": 294.50, "end": 297.20, "pos": (440, 320),  "color": CYAN,  "style": "glow"},
    {"text": "CATASTROPHIC SCENARIOS",       "start": 300.50, "end": 303.00, "pos": (1480, 320), "color": RED,   "style": "glow"},
    {"text": "PROBABILITY OF RUIN",          "start": 311.50, "end": 314.00, "pos": (960, 840),  "color": RED,   "style": "glow"},
    {"text": "ENGINE 2: EXECUTION",          "start": 314.50, "end": 317.00, "pos": (440, 260),  "color": MINT,  "style": "glow"},
    {"text": "$5 BILLION ORDER",             "start": 317.50, "end": 320.00, "pos": (1480, 260), "color": GOLD,  "style": "glow"},
    {"text": "REINFORCEMENT LEARNING",       "start": 323.50, "end": 326.00, "pos": (440, 820),  "color": CYAN,  "style": "glow"},
    {"text": "DARK POOLS",                   "start": 328.50, "end": 330.50, "pos": (1480, 820), "color": WHITE, "style": "clean"},
    {"text": "ENGINE 3: FRAUD DETECTION",    "start": 333.50, "end": 336.50, "pos": (440, 280),  "color": RED,   "style": "glow"},
    {"text": "DETECT SPOOFING",              "start": 341.50, "end": 343.80, "pos": (1480, 280), "color": RED,   "style": "glow"},
    {"text": "ENGINE 4: REBALANCING",        "start": 348.00, "end": 351.00, "pos": (440, 820),  "color": MINT,  "style": "glow"},
    {"text": "COVARIANCE MATRIX",            "start": 354.00, "end": 356.20, "pos": (1480, 820), "color": CYAN,  "style": "glow"},
    {"text": "MAXIMIZE SHARPE RATIO",        "start": 356.50, "end": 359.00, "pos": (960, 840),  "color": GOLD,  "style": "glow"},
    {"text": "OPTIMIZATION PROBLEMS",        "start": 364.20, "end": 366.50, "pos": (440, 240),  "color": CYAN,  "style": "glow"},
    {"text": "NOT CRYSTAL BALLS",            "start": 366.80, "end": 369.20, "pos": (1480, 240), "color": RED,   "style": "glow"},

    # --- SCENE 6: THE VERDICT & OUTRO (6:07.53 - 7:05.47) ---
    {"text": "FUNDAMENTAL RULE",             "start": 374.20, "end": 376.50, "pos": (960, 220),  "color": GOLD,  "style": "glow"},
    {"text": "NOT A PUZZLE",                 "start": 377.20, "end": 379.20, "pos": (440, 320),  "color": RED,   "style": "glow"},
    {"text": "COMPETING INTELLIGENCES",      "start": 384.00, "end": 386.50, "pos": (1480, 320), "color": CYAN,  "style": "glow"},
    {"text": "STRUCTURAL SPEED",             "start": 392.20, "end": 394.20, "pos": (440, 820),  "color": CYAN,  "style": "glow"},
    {"text": "DISCIPLINED RISK",             "start": 394.50, "end": 396.50, "pos": (1480, 820), "color": MINT,  "style": "glow"},
    {"text": "COMPOUNDED EDGES",             "start": 399.00, "end": 401.50, "pos": (960, 840),  "color": GOLD,  "style": "glow"},
    {"text": "RECOMMENDATION ALGORITHM",     "start": 409.20, "end": 412.00, "pos": (960, 240),  "color": CYAN,  "style": "glow"},
    {"text": "QUANTROVE",                    "start": 423.50, "end": 425.40, "pos": (960, 540),  "color": GOLD,  "style": "glow"},
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

def generate_full_overlay(out_overlay_path, fps=60, total_duration=425.47):
    """Generate 60fps transparent alpha video across the entire EP04 video."""
    print(f"\n========================================================")
    print(f"Generating full 60fps kinetic overlay (EP04: {total_duration}s, {len(ALL_KEYWORDS)} curated keywords)...")
    print(f"Destination: {out_overlay_path}")
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
    empty_bytes = empty_frame.tobytes()
    
    for f in range(total_frames):
        t = f / fps
        active_kws = [kw for kw in ALL_KEYWORDS if kw["start"] <= t <= kw["end"]]
        
        if not active_kws:
            proc.stdin.write(empty_bytes)
            if f % 1200 == 0:
                print(f"  Rendered {f}/{total_frames} frames ({f/total_frames*100:.1f}%)...")
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
    print("\n✓ Full 7:05 master kinetic overlay rendered successfully!")

if __name__ == "__main__":
    overlay_out = os.path.join(TIMELINE_DIR, "00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps.mov")
    generate_full_overlay(overlay_out)
