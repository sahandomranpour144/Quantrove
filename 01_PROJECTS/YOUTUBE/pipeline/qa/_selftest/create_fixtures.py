#!/usr/bin/env python3
"""
Generate synthetic fixtures for Quantrove Shorts QA self-test.
Creates:
  1. pipeline/qa/_selftest/good/ (Passes all automated rules)
  2. pipeline/qa/_selftest/bad/ (Fails R2, R6, R9)
"""

import os
import sys
import json
import subprocess

SELFTEST_DIR = os.path.dirname(os.path.abspath(__file__))
PIPELINE_DIR = os.path.dirname(os.path.dirname(SELFTEST_DIR))
TEXT_LAYER_DIR = os.path.join(PIPELINE_DIR, "text_layer")
sys.path.insert(0, TEXT_LAYER_DIR)
from generate_text_events import generate_text_events

GOOD_DIR = os.path.join(SELFTEST_DIR, "good")
BAD_DIR = os.path.join(SELFTEST_DIR, "bad")

os.makedirs(GOOD_DIR, exist_ok=True)
os.makedirs(BAD_DIR, exist_ok=True)

STYLE_PATH = os.path.join(PIPELINE_DIR, "config", "shorts_style.json")
with open(STYLE_PATH, "r", encoding="utf-8") as sf:
    STYLE_CONFIG = json.load(sf)

def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running cmd: {cmd}\n{res.stderr}", file=sys.stderr)
    return res

def build_good_fixtures():
    print("[+] Building GOOD fixtures...")
    # 1. 35-second moving video (testsrc changes every frame, zero freezes)
    vid_path = os.path.join(GOOD_DIR, "video.mp4")
    run_cmd(f'ffmpeg -y -f lavfi -i testsrc=size=1080x1920:rate=30:duration=35 -pix_fmt yuv420p -c:v libx264 "{vid_path}"')

    # 2. Calibrated audio stems (-14.0 LUFS voice, -32.0 LUFS music -> delta 18 dB)
    voice_path = os.path.join(GOOD_DIR, "voice.wav")
    music_path = os.path.join(GOOD_DIR, "music.wav")
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=440:duration=35" -af "volume=7.8dB" "{voice_path}"')
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=35" -af "volume=-10dB" "{music_path}"')

    # Mux calibrated audio into video.mp4 so mix measurement passes in --mix-only mode
    run_cmd(f'ffmpeg -y -i "{vid_path}" -i "{voice_path}" -c:v copy -c:a aac -b:a 192k "{vid_path}.tmp.mp4"')
    if os.path.exists(f"{vid_path}.tmp.mp4"):
        os.replace(f"{vid_path}.tmp.mp4", vid_path)

    # 3. Words: 84 words across 33.6s -> ~150 WPM
    word_texts = [
        "How", "algorithms", "control", "global",
        "liquidity", "without", "retail", "noticing.",
        "Most", "traders", "believe", "patterns",
        "predict", "future", "market", "breakouts.",
        "They", "draw", "trendlines", "on",
        "lagging", "indicators", "hoping", "for",
        "reversals.", "Institutions", "hunt", "those",
        "exact", "stop", "losses", "daily.",
        "The", "math", "proves", "order",
        "flow", "drives", "twenty", "billion",
        "dollars", "in", "forced", "liquidations.",
        "When", "volatility", "spikes", "automated",
        "systems", "drain", "depth", "from",
        "order", "books", "in", "milliseconds.",
        "Retail", "absorbs", "the", "toxic",
        "flow", "while", "market", "makers",
        "hedge", "delta", "neutral", "positions.",
        "Here", "is", "the", "undeniable",
        "algorithmic", "reality:", "liquidity", "pools",
        "always", "dictate", "asset", "price",
        "direction", "regardless", "of", "sentiment.",
        "Trust", "pure", "math", "only."
    ] # 84 words

    words = []
    step = (34.2 - 0.2) / len(word_texts)
    for i, wt in enumerate(word_texts):
        w_start = round(0.2 + i * step, 3)
        w_end = round(w_start + step * 0.85, 3)
        words.append({"word": wt, "start": w_start, "end": w_end})

    words_data = {"all_words": words, "total_words": len(words)}
    with open(os.path.join(GOOD_DIR, "words.json"), "w", encoding="utf-8") as f:
        json.dump(words_data, f, indent=2)

    # 4. Shotlist
    shotlist = {
        "type": "native",
        "scenes": [
            {"id": 1, "beat": "IDEA", "start_s": 0.0, "end_s": 8.5, "motion_tag": "manim_draw", "type": "native"},
            {"id": 2, "beat": "SIMPLE_WRONG", "start_s": 8.5, "end_s": 17.0, "motion_tag": "camera_push", "camera_push_scale": 1.06, "motion_purpose": "Zoom on false breakout", "type": "native"},
            {"id": 3, "beat": "COMPLEX_WRONG", "start_s": 17.0, "end_s": 26.0, "motion_tag": "manim_transform", "type": "native"},
            {"id": 4, "beat": "INSIGHT", "start_s": 26.0, "end_s": 35.0, "motion_tag": "manim_draw", "badge": "THE REAL PATTERN", "type": "native"}
        ]
    }
    with open(os.path.join(GOOD_DIR, "shotlist.json"), "w", encoding="utf-8") as f:
        json.dump(shotlist, f, indent=2)

    # 5. Generate text events using generate_text_events
    text_events = generate_text_events(words_data, STYLE_CONFIG, shotlist)
    if text_events:
        text_events[0]["start"] = 0.05
    with open(os.path.join(GOOD_DIR, "text_events.json"), "w", encoding="utf-8") as f:
        json.dump(text_events, f, indent=2)

    print("  [OK] Good fixtures created successfully.")

def build_bad_fixtures():
    print("[+] Building BAD fixtures (failing R2, R6, R9)...")
    # 1. 35-second video with a 5s static clip spliced between moving segments -> FAILS R2
    vid_path = os.path.join(BAD_DIR, "video.mp4")
    concat_cmd = (
        'ffmpeg -y '
        '-f lavfi -i testsrc=size=1080x1920:rate=30:duration=10 '
        '-f lavfi -i color=c=black:size=1080x1920:rate=30:duration=5 '
        '-f lavfi -i testsrc=size=1080x1920:rate=30:duration=20 '
        '-filter_complex "[0:v][1:v][2:v]concat=n=3:v=1:a=0[outv]" '
        f'-map "[outv]" -pix_fmt yuv420p -c:v libx264 "{vid_path}"'
    )
    run_cmd(concat_cmd)

    # 2. Audio stems (calibrated so R3 passes)
    voice_path = os.path.join(BAD_DIR, "voice.wav")
    music_path = os.path.join(BAD_DIR, "music.wav")
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=440:duration=35" -af "volume=7.8dB" "{voice_path}"')
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=35" -af "volume=-10dB" "{music_path}"')

    # 3. Words: 75 words at ~150 WPM, but ends at 30.0s -> 5.0s tail on 35s video (FAILS R9)
    # Starts at 0.2s (R1 passes)
    words = []
    base_words = ["Market", "structure", "reveals", "institutional", "intent", "behind", "every", "volatility", "spike"] * 8
    base_words = base_words[:74] + ["subscribe"] # 75 words
    step = (30.0 - 0.2) / len(base_words)
    for i, wt in enumerate(base_words):
        w_start = round(0.2 + i * step, 3)
        w_end = round(w_start + step * 0.85, 3)
        words.append({"word": wt, "start": w_start, "end": w_end})

    with open(os.path.join(BAD_DIR, "words.json"), "w", encoding="utf-8") as f:
        json.dump({"all_words": words, "total_words": len(words)}, f, indent=2)

    # 4. Text events -> FAILS R6 (6 words > 4 max) AND FAILS R9 (contains forbidden word "subscribe")
    text_events = [
        {
            "start": 0.05,
            "end": 2.5,
            # VIOLATION OF R6: 6 words (max is 4)
            "words": [
                {"word": "This", "start": 0.1, "end": 0.4},
                {"word": "is", "start": 0.5, "end": 0.8},
                {"word": "way", "start": 0.9, "end": 1.2},
                {"word": "too", "start": 1.3, "end": 1.6},
                {"word": "many", "start": 1.7, "end": 2.0},
                {"word": "words", "start": 2.1, "end": 2.4}
            ],
            "type": "chunk",
            "y_pct": 68.0,
            "emphasis_word": None
        },
        {
            "start": 2.5,
            "end": 4.5,
            # VIOLATION OF R9: forbidden word "subscribe"
            "words": [
                {"word": "subscribe", "start": 2.6, "end": 3.2},
                {"word": "for", "start": 3.3, "end": 3.6},
                {"word": "more", "start": 3.7, "end": 4.0}
            ],
            "type": "chunk",
            "y_pct": 68.0,
            "emphasis_word": None
        }
    ]
    with open(os.path.join(BAD_DIR, "text_events.json"), "w", encoding="utf-8") as f:
        json.dump(text_events, f, indent=2)

    # 5. Shotlist: 4 scenes, but Scene 2 (10-15s) has NO hold_tag -> FAILS R2 (5s freeze without HOLD tag)
    # Also has an outro card -> FAILS R9
    shotlist = {
        "type": "native",
        "scenes": [
            {"id": 1, "beat": "IDEA", "start_s": 0.0, "end_s": 10.0, "motion_tag": "manim_draw", "type": "native"},
            {"id": 2, "beat": "SIMPLE_WRONG", "start_s": 10.0, "end_s": 15.0, "motion_tag": "manim_transform", "type": "native"}, # Frozen for 5s with NO hold_tag!
            {"id": 3, "beat": "COMPLEX_WRONG", "start_s": 15.0, "end_s": 26.0, "motion_tag": "manim_draw", "type": "native"},
            {"id": 4, "beat": "INSIGHT", "start_s": 26.0, "end_s": 32.0, "motion_tag": "manim_draw", "type": "native"},
            {"id": 5, "beat": "OUTRO", "start_s": 32.0, "end_s": 35.0, "motion_tag": "manim_draw", "type": "outro"} # Outro scene!
        ]
    }
    with open(os.path.join(BAD_DIR, "shotlist.json"), "w", encoding="utf-8") as f:
        json.dump(shotlist, f, indent=2)

    print("  [OK] Bad fixtures created successfully.")

BAD2_DIR = os.path.join(SELFTEST_DIR, "bad2")
os.makedirs(BAD2_DIR, exist_ok=True)

def build_bad2_fixtures():
    print("[+] Building BAD2 fixtures (failing R1, R3, R4, R5/R6, R7, R8)...")
    # 1. 22-second moving video -> FAILS R7 (22s < 30s min length), PASSES R2 (moving, no freeze)
    vid_path = os.path.join(BAD2_DIR, "video.mp4")
    run_cmd(f'ffmpeg -y -f lavfi -i testsrc=size=1080x1920:rate=30:duration=22 -pix_fmt yuv420p -c:v libx264 "{vid_path}"')

    # 2. Audio stems -> FAILS R3 (voice=-28 LUFS is far below -14±1.5 LUFS)
    voice_path = os.path.join(BAD2_DIR, "voice.wav")
    music_path = os.path.join(BAD2_DIR, "music.wav")
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=440:duration=22" -af "volume=-6dB" "{voice_path}"')
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=22" -af "volume=-10dB" "{music_path}"')

    # 3. Words -> FAILS R1 (first word starts at 2.5s >= 0.5s) AND FAILS R4 (28 words in 19s -> ~88 WPM < 135 WPM)
    # Ends at 21.5s on 22s video (tail = 0.5s <= 1.0s -> R9 passes)
    words = []
    base_words = [
        "In", "this", "slow", "paced", "presentation",
        "we", "analyze", "why", "markets", "move",
        "without", "speed", "or", "urgency", "today.",
        "Notice", "how", "every", "single", "spoken",
        "word", "is", "delayed", "far", "beyond",
        "any", "acceptable", "threshold."
    ] # 28 words
    t = 2.5 # First word at 2.5s -> FAILS R1!
    step = (21.5 - 2.5) / len(base_words)
    for i, wt in enumerate(base_words):
        w_start = round(t + i * step, 3)
        w_end = round(w_start + step * 0.8, 3)
        words.append({"word": wt, "start": w_start, "end": w_end})

    with open(os.path.join(BAD2_DIR, "words.json"), "w", encoding="utf-8") as f:
        json.dump({"all_words": words, "total_words": len(words)}, f, indent=2)

    # 4. Text events -> FAILS R1 (starts at 2.0s > 0.1s) AND FAILS R5/R6 (disallowed color, overlap, outside safe zone)
    text_events = [
        {
            "start": 2.0, # Starts at 2.0s -> FAILS R1!
            "end": 4.5,
            "words": words[0:3],
            "type": "chunk",
            "y_pct": 88.0, # FAILS R5/R6: 88% is outside safe zone (max 80%)!
            "color": "#FF0055", # FAILS R5/R6: disallowed color!
            "emphasis_word": None
        },
        {
            "start": 4.0, # FAILS R5/R6: overlaps with event 0 (which ends at 4.5s)!
            "end": 6.5,
            "words": words[3:6],
            "type": "chunk",
            "y_pct": 68.0,
            "emphasis_word": None
        },
        {
            "start": 6.5,
            "end": 21.5,
            "words": words[6:10],
            "type": "chunk",
            "y_pct": 68.0,
            "emphasis_word": None
        }
    ]
    with open(os.path.join(BAD2_DIR, "text_events.json"), "w", encoding="utf-8") as f:
        json.dump(text_events, f, indent=2)

    # 5. Shotlist -> FAILS R7 (beats out of order, length 22s < 30s) AND FAILS R8 (invalid motion tag, camera_push scale 1.25 without purpose)
    # No outro card -> R9 passes
    shotlist = {
        "type": "native",
        "scenes": [
            {
                "id": 1,
                "beat": "COMPLEX_WRONG", # Out of order! (Expected IDEA first)
                "start_s": 0.0,
                "end_s": 7.0,
                "motion_tag": "invalid_spin_zoom", # FAILS R8: invalid motion tag!
                "type": "native"
            },
            {
                "id": 2,
                "beat": "IDEA",
                "start_s": 7.0,
                "end_s": 14.0,
                "motion_tag": "camera_push",
                "camera_push_scale": 1.25, # FAILS R8: 1.25 > 1.08 max!
                "motion_purpose": "", # FAILS R8: missing purpose!
                "type": "native"
            },
            {
                "id": 3,
                "beat": "INSIGHT",
                "start_s": 14.0,
                "end_s": 22.0,
                "motion_tag": "manim_draw",
                "type": "native"
            }
        ]
    }
    with open(os.path.join(BAD2_DIR, "shotlist.json"), "w", encoding="utf-8") as f:
        json.dump(shotlist, f, indent=2)

    print("  [OK] Bad2 fixtures created successfully.")

if __name__ == "__main__":
    build_good_fixtures()
    build_bad_fixtures()
    build_bad2_fixtures()
