"""
EP04 Master Full-Video Kinetic Keyword Overlay Generator v2
Renders 60fps transparent kinetic text overlay across all 6 scenes (00:00 - 07:05.48)
with elastic spring-pop punch-in animation, glowing typography, and margin-safe positioning.
Output: TIMELINE_MEDIA/00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps_v2.mov
"""

import os
import sys
import math
import json
import subprocess
import time
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EP_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
TIMELINE_DIR = os.path.join(EP_DIR, "TIMELINE_MEDIA")
TIMING_FILE = os.path.join(TIMELINE_DIR, "00_TIMING_all_words_v3_patched_transcription.json")

# Load timing
with open(TIMING_FILE, "r", encoding="utf-8") as f:
    ALL_WORDS = json.load(f)["all_words"]

def find_word(word_text, min_time):
    clean_target = word_text.lower().strip(".,?!:;\"")
    for i, w in enumerate(ALL_WORDS):
        if w["start"] >= min_time - 0.25:
            w_clean = w["word"].lower().strip(".,?!:;\"")
            if w_clean == clean_target:
                return w["start"], i
    raise ValueError(f"Could not find word '{word_text}' after {min_time}s")

# Positioning anchors (all well above bottom 12% cutoff at Y >= 950)
P_TOP_L  = (480, 260)
P_TOP_R  = (1440, 260)
P_TOP_C  = (960, 240)
P_MID_L  = (460, 480)
P_MID_R  = (1460, 480)
P_LOW_L  = (480, 740)
P_LOW_R  = (1440, 740)
P_LOW_C  = (960, 740)

# Colors
TEXT   = (230, 237, 243) # #E6EDF3 (Clean text)
ACCENT = (195, 216,   9) # #C3D809 (Accent lime)
RISK   = (253, 128,  46) # #FD802E (Risk / warning orange)
CYAN   = (  0, 240, 255) # #00F0FF (Neon Cyan)
GOLD   = (255, 215,   0) # #FFD700 (Gold)
WHITE  = (255, 255, 255)

CURATION = [
    # --- SCENE 1: HOOK & SIMONS PARADOX (0:00 - 1:06.70) ---
    # S01 (0.0-3.4s)
    ("can",          0.0,   "CAN AI PREDICT?",           CYAN,   "glow",  P_TOP_C),
    # S02 (4.0-6.0s)
    ("clicked",      3.8,   "CLICKED TO FIND OUT",       TEXT,   "clean", P_TOP_L),
    # S03 (6.6-12.3s)
    ("mostly",       6.5,   "MOSTLY NO",                 RISK,   "glow",  P_TOP_R),
    ("think",        9.5,   "NOT WHAT YOU THINK",        TEXT,   "clean", P_LOW_C),
    # S05 (14.2-15.6s)
    ("slowly",      13.5,   "WORTH GOING SLOWLY",        ACCENT, "glow",  P_LOW_L),
    # S06 (16.4-26.7s, 10.3s)
    ("1988",        16.0,   "1988",                      CYAN,   "glow",  P_TOP_L),
    ("simons",      18.5,   "JIM SIMONS",                GOLD,   "glow",  P_TOP_R),
    ("medallion",   20.2,   "MEDALLION FUND",            CYAN,   "glow",  P_TOP_C),
    ("66",          23.5,   "+66% A YEAR",               ACCENT, "glow",  P_LOW_R),
    # S07 (27.3-34.5s, 7.1s)
    ("physicists",  27.0,   "PHYSICISTS & MATH",         CYAN,   "glow",  P_TOP_L),
    ("avoided",     31.5,   "AVOIDED TRADERS",           RISK,   "glow",  P_TOP_R),
    # S08 (35.3-48.4s, 13.1s)
    ("wall",        35.0,   "WALL STREET",               TEXT,   "clean", P_MID_L),
    ("billions",    38.0,   "SPEND BILLIONS",            GOLD,   "glow",  P_MID_R),
    ("supercomputers", 41.0,"SUPERCOMPUTERS",            CYAN,   "glow",  P_LOW_L),
    ("fail",        44.5,   "FAIL TO BEAT INDEX",        RISK,   "glow",  P_LOW_R),
    # S09 (49.3-59.6s, 10.3s)
    ("cracked",     49.0,   "CRACKED THE MARKET",        ACCENT, "glow",  P_TOP_L),
    ("barely",      53.0,   "BARELY 51% EDGE",           ACCENT, "glow",  P_TOP_R),
    ("fail",        57.0,   "FAIL EVERY DAY",            RISK,   "glow",  P_LOW_C),
    # S10 (60.1-66.7s, 6.6s)
    ("real",        60.0,   "REAL MATHEMATICS",          CYAN,   "glow",  P_TOP_L),
    ("cannot",      63.0,   "CANNOT PREDICT",            RISK,   "glow",  P_TOP_R),

    # --- SCENE 2: 50.75% EDGE & REFLEXIVITY (1:06.70 - 2:29.46) ---
    # S11 (67.3-71.0s)
    ("great",       67.0,   "GREAT ILLUSION",            TEXT,   "clean", P_TOP_C),
    # S12 (71.5-77.1s)
    ("assume",      71.0,   "PEOPLE ASSUME",             TEXT,   "clean", P_MID_L),
    ("90",          74.0,   "NOT 90% ACCURACY",          RISK,   "glow",  P_TOP_R),
    # S13 (77.8-87.4s)
    ("mercer",      80.0,   "ROBERT MERCER",             CYAN,   "glow",  P_MID_L),
    ("50",          84.0,   "50.75% OF THE TIME",        ACCENT, "glow",  P_LOW_R),
    # S14 (88.3-98.1s)
    ("law",         88.5,   "LAW OF LARGE NUMBERS",      CYAN,   "glow",  P_TOP_C),
    ("millions",    92.0,   "MILLIONS OF TRADES",        ACCENT, "glow",  P_MID_L),
    ("billions",    96.0,   "BILLIONS IN PROFIT",        GOLD,   "glow",  P_LOW_R),
    # S15 (98.7-106.9s)
    ("generative", 100.0,   "GENERATIVE AI",             CYAN,   "glow",  P_TOP_L),
    ("decades",    103.5,   "DECADES OF DATA",           TEXT,   "clean", P_TOP_R),
    # S16 (107.6-115.0s)
    ("markets",    107.5,   "UNIQUE PROPERTY",           TEXT,   "clean", P_MID_R),
    ("react",      112.5,   "REACT TO PREDICTION",       RISK,   "glow",  P_TOP_C),
    # S17-S18 (115.5-125.7s)
    ("image",      115.5,   "IMAGE RECOGNITION",         CYAN,   "glow",  P_TOP_L),
    ("cat",        120.0,   "IDENTIFY AN OBJECT",        TEXT,   "clean", P_TOP_R),
    ("change",     122.0,   "CAT NEVER CHANGES",         CYAN,   "glow",  P_MID_R),
    # S19 (126.1-131.8s)
    ("zero",       127.5,   "ZERO-SUM GAME",             RISK,   "glow",  P_TOP_C),
    ("algorithmic",130.0,   "ALGORITHMIC PLAYERS",       CYAN,   "glow",  P_MID_L),
    # S20 (132.3-142.9s)
    ("profitable", 134.0,   "PROFITABLE PATTERN",        ACCENT, "glow",  P_TOP_L),
    ("deploy",     137.5,   "DEPLOY CAPITAL",            TEXT,   "clean", P_LOW_L),
    ("buying",     140.0,   "BUYING PRESSURE",           GOLD,   "glow",  P_LOW_R),
    # S21-S22 (143.5-149.5s)
    ("erases",     143.5,   "ERASES THE PATTERN",        RISK,   "glow",  P_TOP_C),
    ("self",       148.0,   "IT SELF-DESTRUCTS",         RISK,   "glow",  P_TOP_R),

    # --- SCENE 3: ALPHA DECAY (2:29.46 - 3:21.55) ---
    # S23 (149.6-155.5s)
    ("quantitative", 150.0, "QUANTITATIVE FINANCE",      CYAN,   "glow",  P_TOP_C),
    ("alpha",      154.0,   "ALPHA DECAY",               RISK,   "glow",  P_TOP_L),
    # S24-S25 (156.1-165.5s)
    ("gravity",    157.0,   "PHYSICAL GRAVITY",          TEXT,   "clean", P_MID_R),
    ("finance",    161.5,   "IN FINANCE",                TEXT,   "clean", P_MID_L),
    ("expiring",   163.5,   "EXPIRING PATENT",           GOLD,   "glow",  P_TOP_C),
    # S26 (166.0-176.2s)
    ("trading",    167.0,   "TRADING ANOMALY",           CYAN,   "glow",  P_TOP_L),
    ("competing",  169.5,   "COMPETING FUNDS",           TEXT,   "clean", P_MID_L),
    ("high",       171.0,   "HIGH-FREQUENCY ALGOS",      CYAN,   "glow",  P_TOP_R),
    ("volume",     174.5,   "VOLUME SPIKES",             ACCENT, "glow",  P_LOW_R),
    # S27 (176.7-189.3s)
    ("automated",  177.0,   "AUTOMATED SYSTEMS",         TEXT,   "clean", P_MID_L),
    ("crowd",      181.0,   "CROWD THE TRADE",           RISK,   "glow",  P_TOP_L),
    ("compress",   184.0,   "COMPRESS SPREADS",          RISK,   "glow",  P_TOP_R),
    ("equilibrium",188.0,   "EQUILIBRIUM",               TEXT,   "clean", P_TOP_C),
    # S28 (189.8-197.3s)
    ("brilliant",  191.5,   "BRILLIANT IN BACKTEST",     ACCENT, "glow",  P_LOW_L),
    ("four",       195.0,   "DEAD IN 4 MONTHS",          RISK,   "glow",  P_LOW_R),
    # S29 (197.8-201.4s)
    ("agapted",    199.5,   "MARKET ADAPTED",            CYAN,   "glow",  P_TOP_C),

    # --- SCENE 4: OVERFITTING TRAP (3:21.55 - 4:33.60) ---
    # S30 (201.8-212.1s)
    ("fatal",      202.0,   "FATAL FLAW",                RISK,   "glow",  P_TOP_L),
    ("machine",    204.0,   "MACHINE LEARNING",          CYAN,   "glow",  P_TOP_R),
    ("retail",     208.0,   "RETAIL TRADERS",            TEXT,   "clean", P_MID_L),
    ("overfitting",210.5,   "OVERFITTING TRAP",          RISK,   "glow",  P_TOP_C),
    # S31 (212.9-217.9s)
    ("low",        214.5,   "LOW SIGNAL-TO-NOISE",       TEXT,   "clean", P_TOP_L),
    # S32 (218.5-228.9s)
    ("tuesday",    218.5,   "TUESDAY PRICE MOVE",        TEXT,   "clean", P_MID_L),
    ("rebalancing",221.5,   "INSTITUTIONAL FLOWS",       CYAN,   "glow",  P_TOP_R),
    ("rumors",     226.0,   "GEOPOLITICAL RUMORS",       TEXT,   "clean", P_LOW_L),
    # S33 (229.6-233.1s)
    ("pure",       231.5,   "PURE NOISE",                RISK,   "glow",  P_TOP_C),
    # S34 (234.3-239.5s)
    ("deep",       234.5,   "DEEP NEURAL NETWORKS",      CYAN,   "glow",  P_TOP_L),
    ("billions",   237.5,   "BILLIONS OF PARAMETERS",    GOLD,   "glow",  P_TOP_R),
    # S35 (240.2-248.8s)
    ("30",         241.0,   "30 YEARS OF DATA",          RISK,   "glow",  P_LOW_L),
    ("mathematics",245.0,   "MATHEMATICS GUARANTEES",    CYAN,   "glow",  P_LOW_R),
    ("correlations",247.5,  "FALSE CORRELATIONS",        RISK,   "glow",  P_TOP_C),
    # S36 (249.2-257.8s)
    ("temperature",251.0,   "CHICAGO TEMPERATURE",       TEXT,   "clean", P_TOP_L),
    ("semiconductor",254.5, "SEMICONDUCTOR RALLY",       GOLD,   "glow",  P_TOP_R),
    # S37 (258.3-268.5s)
    ("straight",   260.0,   "STRAIGHT LINE BACKTEST",    ACCENT, "glow",  P_TOP_C),
    ("real",       265.0,   "REAL CAPITAL",              TEXT,   "clean", P_MID_L),
    # S38 (268.8-273.1s)
    ("evaporates", 271.0,   "EVAPORATES IMMEDIATELY",    RISK,   "glow",  P_TOP_C),

    # --- SCENE 5: 4 REAL ENGINES (4:33.60 - 6:07.53) ---
    # S39-S41 (273.8-287.9s)
    ("wall",       275.0,   "WALL STREET AI",            CYAN,   "glow",  P_TOP_L),
    ("not",        278.0,   "NOT AT ALL",                TEXT,   "clean", P_TOP_R),
    ("fortunes",   280.5,   "SPEND FORTUNES",            GOLD,   "glow",  P_TOP_C),
    ("naive",      283.0,   "NAIVE QUESTION",            RISK,   "glow",  P_MID_L),
    ("tesla",      285.0,   "TESLA AT NOON?",            TEXT,   "clean", P_TOP_R),
    # S42 (288.7-292.8s)
    ("four",       290.0,   "4 REAL ENGINES",            CYAN,   "glow",  P_TOP_C),
    # S43-S45: Engine 1 (293.3-310.7s)
    ("first",      293.0,   "ENGINE 1: RISK MODELING",   CYAN,   "glow",  P_TOP_L),
    ("direction",  296.5,   "NOT PREDICTING DIRECTION",  TEXT,   "clean", P_MID_L),
    ("simulates",  298.0,   "SIMULATES CRASHES",         CYAN,   "glow",  P_TOP_R),
    ("catastrophic",300.5,  "CATASTROPHIC SCENARIOS",    RISK,   "glow",  P_TOP_C),
    ("liquidity",  303.5,   "LIQUIDITY FREEZES",         RISK,   "glow",  P_LOW_L),
    ("interest",   304.5,   "INTEREST RATE SHOCKS",      RISK,   "glow",  P_LOW_R),
    ("ruin",       309.5,   "PROBABILITY OF RUIN",       RISK,   "glow",  P_TOP_C),
    # S46-S48: Engine 2 (311.4-332.1s)
    ("second",     311.0,   "ENGINE 2: EXECUTION",       ACCENT, "glow",  P_TOP_L),
    ("five",       316.0,   "$5 BILLION ORDER",          GOLD,   "glow",  P_TOP_R),
    ("crash",      319.5,   "CRASH THE PRICE",           RISK,   "glow",  P_TOP_C),
    ("reinforcement",322.0, "REINFORCEMENT LEARNING",    CYAN,   "glow",  P_MID_L),
    ("microslices",325.5,   "THOUSANDS OF SLICES",       TEXT,   "clean", P_TOP_R),
    ("dark",       328.5,   "DARK POOLS",                TEXT,   "clean", P_MID_L),
    # S49: Engine 3 (332.7-345.8s)
    ("third",      332.5,   "ENGINE 3: FRAUD DETECTION", RISK,   "glow",  P_TOP_L),
    ("hundreds",   336.5,   "100,000 PER SECOND",        GOLD,   "glow",  P_TOP_R),
    ("spoofing",   340.5,   "SPOOFING & WASH TRADES",    RISK,   "glow",  P_TOP_C),
    ("regulators", 344.0,   "BEFORE REGULATORS",         TEXT,   "clean", P_LOW_R),
    # S50-S54: Engine 4 & Optimization (346.4-367.0s)
    ("fourth",     346.5,   "ENGINE 4: REBALANCING",     ACCENT, "glow",  P_TOP_L),
    ("500",        350.0,   "500 ASSETS",                TEXT,   "clean", P_TOP_R),
    ("covariance", 354.0,   "COVARIANCE MATRIX",         CYAN,   "glow",  P_TOP_C),
    ("volatility", 357.5,   "MINIMIZE VOLATILITY",       ACCENT, "glow",  P_LOW_R),
    ("predicting", 362.0,   "NOT PREDICTING FUTURE",     RISK,   "glow",  P_TOP_R),
    ("optimization",364.5,  "OPTIMIZATION PROBLEMS",     CYAN,   "glow",  P_TOP_C),

    # --- SCENE 6: VERDICT & OUTRO (6:07.53 - 7:05.47) ---
    # S55 (367.7-375.6s)
    ("modern",     369.5,   "AI & FINANCE",              CYAN,   "glow",  P_TOP_L),
    ("fundamental",374.0,   "FUNDAMENTAL RULE",          GOLD,   "glow",  P_TOP_R),
    # S56-S57 (376.3-385.7s)
    ("puzzle",     377.5,   "NOT A PUZZLE",              RISK,   "glow",  P_TOP_C),
    ("reflexive",  382.5,   "REFLEXIVE ECOSYSTEM",       CYAN,   "glow",  P_TOP_L),
    # S58 (386.2-391.2s)
    ("survive",    387.0,   "SURVIVE LONG-TERM",         ACCENT, "glow",  P_TOP_C),
    ("magic",      389.5,   "NO MAGIC ALGORITHM",        RISK,   "glow",  P_MID_L),
    # S59 (391.8-404.1s)
    ("structural", 392.5,   "STRUCTURAL SPEED",          CYAN,   "glow",  P_TOP_L),
    ("statistical",396.8,   "STATISTICAL EDGES",         ACCENT, "glow",  P_LOW_L),
    ("millions",   399.5,   "MILLIONS OF TRADES",        ACCENT, "glow",  P_LOW_R),
    ("jim",        401.0,   "JIM SIMONS: 40 YEARS",      GOLD,   "glow",  P_TOP_C),
    # S60 (405.0-424.5s)
    ("changed",    405.0,   "PERSPECTIVE CHANGED",       TEXT,   "clean", P_MID_L),
    ("watch",      408.0,   "WATCH THIS NEXT",           ACCENT, "glow",  P_MID_R),
    ("algorithm",  411.0,   "YOUTUBE ALGORITHM",         GOLD,   "glow",  P_TOP_R),
    ("system",     414.0,   "THE SYSTEM AT WORK",        TEXT,   "clean", P_TOP_C),
    ("mathematics",420.0,   "REAL MATHEMATICS",          CYAN,   "glow",  P_LOW_L),
    ("quantrove",  423.5,   "QUANTROVE",                 GOLD,   "glow",  P_TOP_C)
]

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

def render_keyword_card(text, color, style, font_size=58):
    font = get_font(font_size)
    dummy_img = Image.new("RGBA", (10, 10), (0, 0, 0, 0))
    dummy_draw = ImageDraw.Draw(dummy_img)
    bbox = dummy_draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]

    pad = 50
    cw = tw + pad * 2
    ch = th + pad * 2

    card = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    tx = pad - bbox[0]
    ty = pad - bbox[1]

    # 1. Soft deep drop shadow for legibility
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

def build_keywords():
    raw_pops = []
    for anchor, min_t, text, color, style, pos in CURATION:
        st, idx = find_word(anchor, min_t)
        raw_pops.append({
            "text": text,
            "anchor": anchor,
            "anchor_idx": idx,
            "start": st,
            "color": color,
            "style": style,
            "pos": pos
        })

    raw_pops.sort(key=lambda x: x["start"])

    # Ensure no overlaps and readable durations (1.6s - 2.0s)
    for i in range(len(raw_pops)):
        st = raw_pops[i]["start"]
        if i + 1 < len(raw_pops):
            nxt_st = raw_pops[i+1]["start"]
            max_dur = nxt_st - st - 0.08
            dur = min(2.0, max(1.2, max_dur))
            raw_pops[i]["end"] = st + dur
        else:
            raw_pops[i]["end"] = st + 1.8

    return raw_pops

def generate_overlay(out_path, fps=60, total_duration=425.483333):
    keywords = build_keywords()
    total_frames = int(math.ceil(total_duration * fps))

    print(f"Pre-rendering {len(keywords)} keyword cards...")
    cards = {}
    for kw in keywords:
        if kw["text"] not in cards:
            cards[kw["text"]] = render_keyword_card(kw["text"], kw["color"], kw["style"])

    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-f", "rawvideo",
        "-pix_fmt", "rgba",
        "-s", "1920x1080",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "qtrle",
        out_path
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    pop_duration = 0.22   # 220ms elastic spring pop-in
    fade_duration = 0.12  # 120ms fade-out
    empty_frame = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0))
    empty_bytes = empty_frame.tobytes()

    t0 = time.time()
    for f in range(total_frames):
        t = f / float(fps)
        active = [kw for kw in keywords if kw["start"] <= t <= kw["end"]]

        if not active:
            proc.stdin.write(empty_bytes)
            if f % 1800 == 0 and f > 0:
                elapsed = time.time() - t0
                fps_rate = f / elapsed if elapsed > 0 else 0
                pct = (f / total_frames) * 100
                print(f"  Frame {f}/{total_frames} ({pct:.1f}%) @ {fps_rate:.1f} fps")
            continue

        frame = empty_frame.copy()
        for kw in active:
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
                scale = 1.0
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
            frame.paste(scaled_card, (x, y))

        proc.stdin.write(frame.tobytes())

        if f % 1800 == 0 and f > 0:
            elapsed = time.time() - t0
            fps_rate = f / elapsed if elapsed > 0 else 0
            pct = (f / total_frames) * 100
            print(f"  Frame {f}/{total_frames} ({pct:.1f}%) @ {fps_rate:.1f} fps")

    proc.stdin.close()
    proc.wait()
    total_time = time.time() - t0
    print(f"\n✓ Render finished: {total_frames} frames in {total_time:.1f}s ({total_frames/total_time:.1f} fps)")

if __name__ == "__main__":
    out_mov = os.path.join(TIMELINE_DIR, "00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps_v2.mov")
    generate_overlay(out_mov)
