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

def ease_in_quad(t):
    t = max(0.0, min(1.0, t))
    return t * t

# Define curated punchy keywords for Scene 1 with exact whisper timestamps
SCENE1_KEYWORDS = [
    # 00:00 - 00:10: Infinite Feed Vortex
    {"text": "SYSTEM",          "start": 0.96,  "end": 1.70, "pos": (460, 420),  "color": (0, 240, 255), "style": "glow"},
    {"text": "INTERACT",        "start": 1.82,  "end": 2.55, "pos": (1440, 520), "color": (255, 255, 255), "style": "clean"},
    {"text": "HUMAN BEING",     "start": 5.80,  "end": 6.70, "pos": (960, 300),  "color": (255, 184, 0), "style": "glow"},
    
    # 00:10 - 00:18: Billions Scrolling Darkness
    {"text": "NEVER BUILT",     "start": 8.80,  "end": 9.70, "pos": (460, 640),  "color": (255, 75, 75), "style": "glow"},
    {"text": "KEEP YOU WATCHING","start": 14.30, "end": 15.70, "pos": (1420, 440), "color": (0, 240, 255), "style": "glow"},
    {"text": "FRIGHTENINGLY GOOD","start": 16.70,"end": 17.90, "pos": (520, 360),  "color": (255, 184, 0), "style": "glow"},
    
    # 00:18 - 00:36: Manim ScaleOfUploads (keep to clean margins)
    {"text": "ALWAYS WRONG",    "start": 23.00, "end": 24.30, "pos": (1580, 240), "color": (255, 75, 75), "style": "glow"},
    {"text": "OPTIMIZING",      "start": 27.60, "end": 28.80, "pos": (320, 860),  "color": (0, 240, 255), "style": "glow"},
    {"text": "WILDLY DIFFERENT","start": 32.40, "end": 33.90, "pos": (1600, 860), "color": (255, 184, 0), "style": "glow"},
    
    # 00:36 - 00:42: Glass Touchpoint
    {"text": "REAL MECHANISM",  "start": 36.40, "end": 37.60, "pos": (480, 480),  "color": (0, 240, 255), "style": "glow"},
    {"text": "EVERY PLATFORM",  "start": 39.70, "end": 41.20, "pos": (1400, 560), "color": (255, 255, 255), "style": "glow"},
]

def render_keyword_card(text, color, style, font_size=58):
    """Pre-render a high-DPI text card with glowing shadow and sleek typography."""
    font = get_font(font_size)
    
    # Measure text
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
        s_draw.text((tx + off, ty + off), text, font=font, fill=(0, 0, 0, 180))
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

def generate_scene01_overlay_video(out_overlay_path, fps=60, total_duration=42.04):
    """Generate 60fps transparent alpha video with spring-pop animations."""
    print(f"Generating 60fps kinetic overlay for Scene 1 ({total_duration}s)...")
    
    # Pre-render cards
    cards = {}
    for kw in SCENE1_KEYWORDS:
        card, center = render_keyword_card(kw["text"], kw["color"], kw["style"])
        cards[kw["text"]] = (card, center)
        
    total_frames = int(math.ceil(total_duration * fps))
    
    # Setup ffmpeg process to encode ProRes 4444 with alpha or raw video
    # We will output a quick MOV with png/qtrle or pipe raw frames
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
    
    pop_duration = 0.22   # 220ms elastic pop-in
    fade_duration = 0.12  # 120ms fade-out
    
    empty_frame = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    
    for f in range(total_frames):
        t = f / fps
        
        # Check active keywords at time t
        active_kws = [kw for kw in SCENE1_KEYWORDS if kw["start"] <= t <= kw["end"]]
        
        if not active_kws:
            proc.stdin.write(empty_frame.tobytes())
            continue
            
        frame = empty_frame.copy()
        
        for kw in active_kws:
            card, (cx, cy) = cards[kw["text"]]
            elapsed = t - kw["start"]
            remaining = kw["end"] - t
            
            # Animation curves
            if elapsed < pop_duration:
                # Elastic spring pop: scale from 0.35 to 1.15 to 1.0
                progress = elapsed / pop_duration
                scale = 0.35 + 0.65 * ease_out_back(progress, s=2.2)
                alpha = min(1.0, elapsed / 0.08)
            elif remaining < fade_duration:
                # Smooth fade out with subtle expansion
                progress = remaining / fade_duration
                scale = 1.0 + 0.08 * (1.0 - progress)
                alpha = ease_out_quad(progress)
            else:
                # Hold state with subtle cinematic micro-zoom
                hold_progress = (elapsed - pop_duration) / max(0.01, (kw["end"] - kw["start"] - pop_duration - fade_duration))
                scale = 1.0 + 0.04 * hold_progress
                alpha = 1.0
                
            scale = max(0.01, scale)
            target_w = int(card.width * scale)
            target_h = int(card.height * scale)
            
            # Resize card
            scaled_card = card.resize((target_w, target_h), Image.Resampling.BILINEAR)
            
            # Apply alpha if needed
            if alpha < 0.99:
                r, g, b, a = scaled_card.split()
                a = a.point(lambda p: int(p * alpha))
                scaled_card = Image.merge("RGBA", (r, g, b, a))
                
            # Position centered at kw["pos"]
            px, py = kw["pos"]
            x = px - target_w // 2
            y = py - target_h // 2
            
            # Composite onto frame
            frame.alpha_composite(scaled_card, (x, y))
            
        proc.stdin.write(frame.tobytes())
        
        if f % 300 == 0:
            print(f"  Rendered {f}/{total_frames} frames ({f/total_frames*100:.1f}%)...")
            
    proc.stdin.close()
    proc.wait()
    print("✓ Overlay render complete!")

if __name__ == "__main__":
    overlay_path = os.path.join(BASE_DIR, "scene01_kinetic_overlay.mov")
    generate_scene01_overlay_video(overlay_path)
