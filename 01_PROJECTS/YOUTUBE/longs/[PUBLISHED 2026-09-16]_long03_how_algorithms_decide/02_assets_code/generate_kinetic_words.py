"""
EP03 Full-Video Scattered Kinetic Word Emphasis Generator
Generates ASS subtitle tracks with yellow-highlight/black-text treatment
scattered dynamically across the 1920x1080 canvas for ALL 7 scenes.

Usage:
  python generate_kinetic_words.py              # Full pipeline: generates ASS + Scene 1 sample
  python generate_kinetic_words.py --ass-only   # Only generate the ASS file (no render)
"""
import os, sys, json, subprocess, random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA"))

# ============================================================================
# SCENE TIMECODE WINDOWS (from README_TIMELINE_MANIFEST.md)
# ============================================================================
SCENE_WINDOWS = {
    1: (0.00,   42.04),
    2: (42.04,  82.32),
    3: (82.32,  122.72),
    4: (122.72, 167.76),
    5: (167.76, 212.24),
    6: (212.24, 260.40),
    7: (260.40, 318.60),
}

# Manim clip windows within each scene (keep words to margins during these)
MANIM_WINDOWS = [
    (18.00,  36.00),   # Scene 1: ScaleOfUploads
    (42.04,  56.74),   # Scene 2: TwoTowerVectorSpace
    (82.32,  94.02),   # Scene 3: ThreeStageFunnel
    (107.48, 122.72),  # Scene 3: NeuralScoringMatrix
    (148.72, 167.76),  # Scene 4: VariableRewardCurve
    (167.76, 179.16),  # Scene 5: TransformerAttention
    (187.98, 212.24),  # Scene 5: DivergentMetrics
    (230.64, 246.44),  # Scene 6: EchoChamberDiversity
    (260.40, 285.94),  # Scene 7: AlgorithmSummaryRules
]

def is_during_manim(t):
    """Check if timestamp t falls during a Manim clip."""
    for start, end in MANIM_WINDOWS:
        if start <= t <= end:
            return True
    return False

# ============================================================================
# POSITION GENERATION
# ============================================================================
# Full-frame scattered positions (for Flow/Image clips)
FULL_POSITIONS = [
    (440, 280), (1480, 360), (380, 560), (1540, 620), (960, 220),
    (420, 780), (1460, 280), (400, 420), (1500, 760), (480, 320),
    (1420, 480), (960, 820), (420, 260), (1520, 380), (360, 640),
    (1480, 680), (960, 280), (420, 460), (1500, 460), (960, 840),
    (300, 360), (1600, 440), (500, 700), (1400, 700), (750, 200),
    (1200, 200), (300, 800), (1620, 800), (700, 500), (1300, 500),
    (440, 160), (1480, 160), (380, 880), (1540, 880), (960, 400),
]

# Margin-safe positions (for Manim clips — avoid center content)
MANIM_SAFE_POSITIONS = [
    (280, 240), (1640, 240), (280, 840), (1640, 840),
    (280, 300), (1640, 300), (280, 820), (1640, 820),
    (960, 160), (960, 920), (200, 540), (1720, 540),
    (280, 180), (1640, 180), (280, 900), (1640, 900),
    (380, 160), (1540, 160), (380, 920), (1540, 920),
]

def get_position(t, idx):
    """Get a scattered position, using margin-safe positions during Manim clips."""
    if is_during_manim(t):
        return MANIM_SAFE_POSITIONS[idx % len(MANIM_SAFE_POSITIONS)]
    return FULL_POSITIONS[idx % len(FULL_POSITIONS)]


# ============================================================================
# CURATED EMPHASIS WORDS (per scene)
# Word timings will be filled from all_words.json or hardcoded from Scene 1
# ============================================================================

# Scene 1 words — already timed from faster-whisper (scene01_words.json)
SCENE1_WORDS = [
    # Sentence 1: "There is a system you interact with more times per day than you talk to any single human being in your life."
    {"text": "SYSTEM",         "start": 0.96, "end": 1.40},
    {"text": "YOU",            "start": 1.40, "end": 1.82},
    {"text": "INTERACT",       "start": 1.82, "end": 2.45},
    {"text": "MORE",           "start": 2.66, "end": 3.10},
    {"text": "THAN",           "start": 4.14, "end": 4.60},
    {"text": "TALK TO",        "start": 4.66, "end": 5.20},
    {"text": "HUMAN",          "start": 5.96, "end": 6.45},
    {"text": "IN YOUR",        "start": 6.80, "end": 7.36},
    {"text": "LIFE",           "start": 7.36, "end": 7.90},
    # Sentence 2: "It was never built to inform you."
    {"text": "NEVER",          "start": 8.82, "end": 9.20},
    {"text": "BUILT",          "start": 9.20, "end": 9.65},
    {"text": "INFORM YOU",     "start": 9.80, "end": 10.56},
    # Sentence 3: "It was built to do exactly one thing: keep you watching."
    {"text": "BUILT TO",       "start": 11.40, "end": 12.00},
    {"text": "EXACTLY",        "start": 12.14, "end": 12.60},
    {"text": "ONE THING",      "start": 12.60, "end": 13.50},
    {"text": "KEEP YOU",       "start": 14.48, "end": 14.98},
    {"text": "WATCHING",       "start": 14.98, "end": 15.60},
    # Sentence 4: "And it is frighteningly good at its job."
    {"text": "FRIGHTENINGLY",  "start": 16.80, "end": 17.54},
    {"text": "GOOD",           "start": 17.54, "end": 18.00},
    {"text": "ITS JOB",        "start": 18.14, "end": 18.70},
    # Sentence 5: "Most people think they know how it works."
    {"text": "PEOPLE",         "start": 20.20, "end": 20.60},
    {"text": "THINK",          "start": 20.60, "end": 21.00},
    {"text": "HOW IT WORKS",   "start": 21.40, "end": 22.10},
    # Sentence 6: "They are almost always wrong."
    {"text": "ALMOST",         "start": 23.06, "end": 23.40},
    {"text": "ALWAYS",         "start": 23.40, "end": 23.96},
    {"text": "WRONG",          "start": 23.96, "end": 24.50},
    # Sentence 7: "So what is the algorithm actually optimizing for?"
    {"text": "ALGORITHM",      "start": 26.56, "end": 27.10},
    {"text": "ACTUALLY",       "start": 27.10, "end": 27.80},
    {"text": "OPTIMIZING",     "start": 27.80, "end": 28.50},
    # Sentence 8: "Why do two nearly identical videos get wildly different results?"
    {"text": "TWO",            "start": 30.06, "end": 30.40},
    {"text": "IDENTICAL",      "start": 30.78, "end": 31.50},
    {"text": "WILDLY",         "start": 32.44, "end": 32.94},
    {"text": "DIFFERENT",      "start": 32.94, "end": 33.50},
    {"text": "RESULTS",        "start": 33.50, "end": 34.10},
    # Sentence 9: "And once you understand the real mechanism..."
    {"text": "UNDERSTAND",     "start": 35.68, "end": 36.24},
    {"text": "REAL MECHANISM", "start": 36.48, "end": 37.35},
    {"text": "CHANGE",         "start": 38.42, "end": 38.80},
    {"text": "THE WAY",        "start": 38.80, "end": 39.20},
    {"text": "EVERY PLATFORM", "start": 39.76, "end": 40.98},
    {"text": "YOU ARE ON",     "start": 40.98, "end": 41.70},
]

# Scenes 2-7: curated emphasis words with approximate timings
# Timings are relative to the SCENE START, will be converted to absolute
# These will be refined when all_words.json is available

SCENE2_WORDS_REL = [
    # "Ask most people how recommendations work, and you will hear some version of the same answer:"
    {"text": "PEOPLE",           "rel": 1.20},
    {"text": "RECOMMENDATIONS",  "rel": 2.80},
    {"text": "SAME ANSWER",      "rel": 5.20},
    # "it shows you what is popular. What is trending."
    {"text": "POPULAR",          "rel": 7.00},
    {"text": "TRENDING",         "rel": 8.20},
    # "That is not what is actually happening."
    {"text": "NOT",              "rel": 10.40},
    {"text": "ACTUALLY",         "rel": 11.20},
    # "everyone logged in at the same moment would see the same recommended videos."
    {"text": "SAME MOMENT",      "rel": 14.80},
    {"text": "RECOMMENDED",      "rel": 16.40},
    # "They do not."
    {"text": "DO NOT",           "rel": 18.60},
    # "Two people can open the same platform, at the same second, and see almost completely different feeds"
    {"text": "TWO PEOPLE",       "rel": 19.80},
    {"text": "SAME PLATFORM",    "rel": 21.40},
    {"text": "DIFFERENT FEEDS",  "rel": 24.00},
    # "built from completely different signals."
    {"text": "DIFFERENT SIGNALS","rel": 26.20},
    # "This is not a popularity contest. It is a prediction system, built individually, for you specifically."
    {"text": "NOT",              "rel": 28.40},
    {"text": "POPULARITY",       "rel": 29.20},
    {"text": "PREDICTION",       "rel": 31.00},
    {"text": "INDIVIDUALLY",     "rel": 33.40},
    {"text": "YOU SPECIFICALLY",  "rel": 35.60},
]

SCENE3_WORDS_REL = [
    # "Publicly documented research from the engineers who build these systems describes a two-stage architecture"
    {"text": "RESEARCH",         "rel": 1.80},
    {"text": "ENGINEERS",        "rel": 3.20},
    {"text": "TWO-STAGE",        "rel": 6.80},
    # "Stage one: candidate generation."
    {"text": "STAGE ONE",        "rel": 9.20},
    {"text": "CANDIDATE",        "rel": 10.40},
    {"text": "GENERATION",       "rel": 11.20},
    # "millions of available videos, a first system narrows the field down to a few hundred"
    {"text": "MILLIONS",         "rel": 13.60},
    {"text": "NARROWS",          "rel": 16.40},
    {"text": "FEW HUNDRED",      "rel": 18.00},
    # "using your watch history, your session context"
    {"text": "WATCH HISTORY",    "rel": 20.40},
    {"text": "SESSION",          "rel": 22.00},
    # "Stage two: ranking."
    {"text": "STAGE TWO",        "rel": 25.60},
    {"text": "RANKING",          "rel": 26.80},
    # "scores every single one -- not by how good the video objectively is"
    {"text": "SCORES",           "rel": 28.80},
    {"text": "EVERY SINGLE",     "rel": 29.80},
    {"text": "OBJECTIVELY",      "rel": 32.60},
    # "but by how likely it is to keep you, specifically, watching."
    {"text": "KEEP YOU",         "rel": 34.80},
    {"text": "SPECIFICALLY",     "rel": 36.00},
    {"text": "WATCHING",         "rel": 37.40},
]

SCENE4_WORDS_REL = [
    # "Here is the detail almost nobody outside the industry knows"
    {"text": "DETAIL",           "rel": 1.80},
    {"text": "NOBODY",           "rel": 3.20},
    {"text": "INDUSTRY",         "rel": 5.00},
    # "recommendation systems were built to maximize clicks"
    {"text": "MAXIMIZE",         "rel": 8.00},
    {"text": "CLICKS",           "rel": 9.20},
    # "creators learned that outrageous, misleading thumbnails and titles got clicked more"
    {"text": "OUTRAGEOUS",       "rel": 12.40},
    {"text": "MISLEADING",       "rel": 13.60},
    {"text": "CLICKED MORE",     "rel": 16.00},
    # "So platforms changed the target. Not clicks -- watch time."
    {"text": "CHANGED",          "rel": 19.20},
    {"text": "TARGET",           "rel": 20.00},
    {"text": "NOT CLICKS",       "rel": 21.40},
    {"text": "WATCH TIME",       "rel": 22.60},
    # "The system stopped asking what will get clicked"
    {"text": "STOPPED",          "rel": 24.80},
    {"text": "ASKING",           "rel": 25.80},
    # "and started asking what will this specific person actually keep watching"
    {"text": "SPECIFIC PERSON",  "rel": 29.00},
    {"text": "KEEP WATCHING",    "rel": 31.40},
    # "That single change is the most important thing to understand"
    {"text": "SINGLE CHANGE",    "rel": 34.00},
    {"text": "MOST IMPORTANT",   "rel": 36.00},
    {"text": "YOUR FEED",        "rel": 40.40},
    {"text": "TODAY",            "rel": 41.60},
]

SCENE5_WORDS_REL = [
    # "Pattern number one: the exact same video can perform completely differently"
    {"text": "PATTERN ONE",      "rel": 1.80},
    {"text": "EXACT SAME",       "rel": 4.00},
    {"text": "COMPLETELY",       "rel": 6.20},
    {"text": "DIFFERENTLY",      "rel": 7.20},
    # "not because the video changed, but because the prediction target did"
    {"text": "VIDEO CHANGED",    "rel": 9.40},
    {"text": "PREDICTION",       "rel": 11.60},
    {"text": "TARGET",           "rel": 12.60},
    # "Show a video to someone whose history is full of long-form documentaries"
    {"text": "HISTORY",          "rel": 15.80},
    {"text": "LONG-FORM",        "rel": 17.40},
    {"text": "WATCH IT FULLY",   "rel": 19.80},
    # "Show the identical video to someone who only watches short clips"
    {"text": "IDENTICAL",        "rel": 22.40},
    {"text": "SHORT CLIPS",      "rel": 25.00},
    {"text": "DROP OFF",         "rel": 27.40},
    {"text": "SECONDS",          "rel": 28.60},
    # "This is why two creators can post nearly identical content and get wildly different results."
    {"text": "TWO CREATORS",     "rel": 31.40},
    {"text": "IDENTICAL CONTENT","rel": 33.60},
    {"text": "WILDLY DIFFERENT",  "rel": 35.80},
    # "It is predicting a specific outcome for a specific person."
    {"text": "PREDICTING",       "rel": 38.40},
    {"text": "SPECIFIC OUTCOME", "rel": 39.80},
    {"text": "SPECIFIC PERSON",  "rel": 41.40},
]

SCENE6_WORDS_REL = [
    # "Pattern number two is the one that has drawn the most public scrutiny"
    {"text": "PATTERN TWO",      "rel": 1.60},
    {"text": "PUBLIC SCRUTINY",  "rel": 4.80},
    # "when a system is purely optimized for keeping you watching"
    {"text": "PURELY",           "rel": 7.20},
    {"text": "OPTIMIZED",        "rel": 8.40},
    {"text": "KEEPING YOU",      "rel": 9.80},
    # "it can quietly narrow what you see"
    {"text": "QUIETLY",          "rel": 12.40},
    {"text": "NARROW",           "rel": 13.20},
    # "nudging toward more intense, more extreme"
    {"text": "INTENSE",          "rel": 15.00},
    {"text": "EXTREME",          "rel": 16.20},
    {"text": "EMOTIONALLY",      "rel": 17.60},
    # "This is not a secret."
    {"text": "NOT A SECRET",     "rel": 20.40},
    # "Platforms have publicly acknowledged the effect and made real changes to reduce it"
    {"text": "ACKNOWLEDGED",     "rel": 23.00},
    {"text": "REAL CHANGES",     "rel": 25.40},
    # "a system optimized purely for engagement, left unchecked"
    {"text": "ENGAGEMENT",       "rel": 28.60},
    {"text": "UNCHECKED",        "rel": 30.20},
    # "does not just reflect what you are interested in. It can actively reshape it."
    {"text": "REFLECT",          "rel": 32.40},
    {"text": "RESHAPE",          "rel": 34.80},
    # "It is about knowing what the system is actually doing"
    {"text": "KNOWING",          "rel": 38.40},
    {"text": "SYSTEM",           "rel": 39.60},
    # "so you can use it deliberately, instead of being used by it."
    {"text": "DELIBERATELY",     "rel": 41.80},
    {"text": "USED BY IT",       "rel": 44.00},
]

SCENE7_WORDS_REL = [
    # "So what does understanding the algorithm actually change?"
    {"text": "UNDERSTANDING",    "rel": 1.60},
    {"text": "ACTUALLY CHANGE",  "rel": 3.80},
    # "First: it was never a popularity contest."
    {"text": "NEVER",            "rel": 6.80},
    {"text": "POPULARITY",       "rel": 8.00},
    {"text": "INDIVIDUAL",       "rel": 10.20},
    {"text": "PREDICTION",       "rel": 11.40},
    {"text": "YOUR BEHAVIOR",    "rel": 13.00},
    # "Second: it optimizes for attention, not accuracy or importance"
    {"text": "ATTENTION",        "rel": 16.00},
    {"text": "NOT ACCURACY",     "rel": 17.60},
    {"text": "IMPORTANCE",       "rel": 19.00},
    {"text": "VERY DIFFERENT",   "rel": 20.80},
    # "And third: the moment you understand what it is actually predicting"
    {"text": "THE MOMENT",       "rel": 24.00},
    {"text": "UNDERSTAND",       "rel": 25.40},
    {"text": "PREDICTING",       "rel": 27.40},
    # "you can deliberately feed it different signals"
    {"text": "DELIBERATELY",     "rel": 29.40},
    {"text": "DIFFERENT SIGNALS","rel": 31.00},
    {"text": "DIFFERENT FEED",   "rel": 33.20},
    # "We have now covered how markets crash, how recessions really move"
    {"text": "MARKETS CRASH",    "rel": 37.20},
    {"text": "RECESSIONS",       "rel": 39.00},
    {"text": "ALGORITHM DECIDES","rel": 42.00},
    # "subscribe to Quantrove"
    {"text": "SUBSCRIBE",        "rel": 49.60},
    {"text": "QUANTROVE",        "rel": 50.80},
    {"text": "JUST GETTING STARTED", "rel": 52.40},
]

def convert_relative_to_absolute(words_rel, scene_num):
    """Convert relative-to-scene timings to absolute timings."""
    scene_start = SCENE_WINDOWS[scene_num][0]
    result = []
    for w in words_rel:
        abs_start = scene_start + w["rel"]
        duration = min(len(w["text"]) * 0.06 + 0.2, 0.8)  # Duration proportional to word length
        result.append({
            "text": w["text"],
            "start": round(abs_start, 2),
            "end": round(abs_start + duration, 2),
        })
    return result

def refine_with_whisper_data(words, all_words_data):
    """
    Try to match curated emphasis words with actual whisper word-level timestamps.
    This refines the approximate timings with real speech alignment.
    """
    if not all_words_data:
        return words

    whisper_words = all_words_data.get("all_words", [])
    refined = []

    for w in words:
        target_start = w["start"]
        target_text_lower = w["text"].lower().split()[0]  # Match first word

        # Search whisper data near the expected timestamp (+/- 3s window)
        best_match = None
        best_dist = 999

        for ww in whisper_words:
            if abs(ww["start"] - target_start) < 3.0:
                if ww["word"].lower().startswith(target_text_lower[:4]):
                    dist = abs(ww["start"] - target_start)
                    if dist < best_dist:
                        best_dist = dist
                        best_match = ww

        if best_match and best_dist < 2.0:
            # Use whisper timing with the curated text
            if " " in w["text"]:
                # Multi-word: extend end to cover additional words
                duration = w["end"] - w["start"]
                refined.append({
                    "text": w["text"],
                    "start": round(best_match["start"], 2),
                    "end": round(best_match["start"] + duration, 2),
                })
            else:
                refined.append({
                    "text": w["text"],
                    "start": round(best_match["start"], 2),
                    "end": round(best_match["end"], 2),
                })
        else:
            # Keep approximate timing
            refined.append(w)

    return refined


# ============================================================================
# ASS GENERATION
# ============================================================================

def to_ass_time(sec):
    """Formats float seconds into ASS timestamp string: H:MM:SS.cs"""
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def build_full_ass(ass_path, all_words_data=None):
    """Generate the full-video ASS subtitle file covering all 7 scenes."""

    # Build all word lists
    all_emphasis_words = []

    # Scene 1: already has absolute timings
    all_emphasis_words.extend(SCENE1_WORDS)

    # Scenes 2-7: convert relative to absolute
    for scene_num, words_rel in [
        (2, SCENE2_WORDS_REL), (3, SCENE3_WORDS_REL), (4, SCENE4_WORDS_REL),
        (5, SCENE5_WORDS_REL), (6, SCENE6_WORDS_REL), (7, SCENE7_WORDS_REL),
    ]:
        abs_words = convert_relative_to_absolute(words_rel, scene_num)
        # Refine with whisper data if available
        if all_words_data:
            abs_words = refine_with_whisper_data(abs_words, all_words_data)
        all_emphasis_words.extend(abs_words)

    # Sort by start time
    all_emphasis_words.sort(key=lambda w: w["start"])

    # Assign scattered positions
    events = []
    for idx, item in enumerate(all_emphasis_words):
        x, y = get_position(item["start"], idx)
        s_time = to_ass_time(item["start"])
        e_time = to_ass_time(item["end"])
        # Animation: smooth fade in (60ms) and out (80ms), scale pop from 110% to 100% in 90ms
        anim_tag = r"{\pos(" + f"{x},{y}" + r")\fad(60,80)\fscx110\fscy110\t(0,90,\fscx100\fscy100)}"
        events.append(f"Dialogue: 0,{s_time},{e_time},KineticPill,,0,0,0,,{anim_tag}{item['text']}")

    events_str = "\n".join(events)

    ass_content = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: KineticPill,Arial,50,&H00000000,&H00000000,&H0000E5FF,&H0000E5FF,1,0,0,0,100,100,2,0,3,14,0,5,20,20,20,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
{events_str}
"""
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
    print(f"Generated full kinetic words ASS at: {ass_path}")
    print(f"  Total events: {len(all_emphasis_words)} across 7 scenes")
    return all_emphasis_words


def build_scene01_ass(ass_path):
    """Generate Scene 1-only ASS for sample review."""
    events = []
    for idx, item in enumerate(SCENE1_WORDS):
        x, y = get_position(item["start"], idx)
        s_time = to_ass_time(item["start"])
        e_time = to_ass_time(item["end"])
        anim_tag = r"{\pos(" + f"{x},{y}" + r")\fad(60,80)\fscx110\fscy110\t(0,90,\fscx100\fscy100)}"
        events.append(f"Dialogue: 0,{s_time},{e_time},KineticPill,,0,0,0,,{anim_tag}{item['text']}")

    events_str = "\n".join(events)

    ass_content = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: KineticPill,Arial,50,&H00000000,&H00000000,&H0000E5FF,&H0000E5FF,1,0,0,0,100,100,2,0,3,14,0,5,20,20,20,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
{events_str}
"""
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
    print(f"Generated Scene 1 kinetic words ASS at: {ass_path} ({len(SCENE1_WORDS)} events)")


def render_scene01_sample(ass_path, out_video_path):
    """Render Scene 1 sample with kinetic word overlay."""
    print("Assembling Scene 1 video base clips...")
    # Asset paths
    c1 = os.path.join(TIMELINE_DIR, "01_00m00s_to_00m10s_Scene_01_flow_infinite_feed_vortex.mp4")
    c2 = os.path.join(TIMELINE_DIR, "01_00m10s_to_00m18s_Scene_01_flow_billions_scrolling_darkness.mp4")
    c3 = os.path.join(TIMELINE_DIR, "01_00m18s_to_00m36s_Scene_01_ScaleOfUploads_manim.mp4")
    c4 = os.path.join(TIMELINE_DIR, "01_00m36s_to_00m42s_Scene_01_flow_glass_touchpoint.mp4")
    audio = os.path.join(TIMELINE_DIR, "01_AUDIO_00m00s_to_00m42s_Scene_01_hook_voiceover.mp3")

    # Verify input existence
    for p in [c1, c2, c3, c4, audio]:
        if not os.path.exists(p):
            raise FileNotFoundError(f"Missing required asset: {p}")

    # Path with escaped backslashes / colons for FFmpeg ass filter
    escaped_ass = ass_path.replace("\\", "/").replace(":", "\\:")

    filter_script = (
        "[0:v]trim=0:10.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v0];"
        "[1:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v1];"
        "[2:v]trim=0:18.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v2];"
        "[3:v]trim=0:6.040,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=60[v3];"
        f"[v0][v1][v2][v3]concat=n=4:v=1:a=0,ass='{escaped_ass}'[vfinal]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", c1,
        "-i", c2,
        "-i", c3,
        "-i", c4,
        "-i", audio,
        "-filter_complex", filter_script,
        "-map", "[vfinal]",
        "-map", "4:a",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-t", "42.040",
        out_video_path
    ]

    print("Running FFmpeg render...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg error:\n", res.stderr[-2000:])
        sys.exit(1)

    print(f"✓ Successfully rendered Scene 1 sample to:\n  {out_video_path}")


if __name__ == "__main__":
    ass_only = "--ass-only" in sys.argv

    # Load whisper data if available
    all_words_path = os.path.join(BASE_DIR, "all_words.json")
    all_words_data = None
    if os.path.exists(all_words_path):
        with open(all_words_path, "r", encoding="utf-8") as f:
            all_words_data = json.load(f)
        print(f"Loaded {all_words_data['total_words']} words from all_words.json")

    # Generate full ASS
    full_ass = os.path.join(BASE_DIR, "ep03_kinetic_words_full.ass")
    build_full_ass(full_ass, all_words_data)

    # Generate Scene 1 ASS for sample
    scene1_ass = os.path.join(BASE_DIR, "scene01_kinetic_words.ass")
    build_scene01_ass(scene1_ass)

    if not ass_only:
        # Render Scene 1 sample
        out_sample = os.path.join(TIMELINE_DIR, "Scene_01_kinetic_word_sample.mp4")
        render_scene01_sample(scene1_ass, out_sample)
