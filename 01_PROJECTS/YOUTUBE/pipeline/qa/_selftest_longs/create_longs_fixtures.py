#!/usr/bin/env python3
"""
Generate synthetic fixtures for Quantrove Long-Form QA self-test.
Creates:
  1. pipeline/qa/_selftest_longs/good/ (Passes all rules)
  2. pipeline/qa/_selftest_longs/bad/ (Fails L2, L3, L5, L7, and visual 5s freeze)
  3. pipeline/qa/_selftest_longs/bad2/ (Fails L4, L3, audio, text, end-screen)
"""

import os
import sys
import json
import subprocess

SELFTEST_DIR = os.path.dirname(os.path.abspath(__file__))
GOOD_DIR = os.path.join(SELFTEST_DIR, "good")
BAD_DIR = os.path.join(SELFTEST_DIR, "bad")
BAD2_DIR = os.path.join(SELFTEST_DIR, "bad2")

os.makedirs(GOOD_DIR, exist_ok=True)
os.makedirs(BAD_DIR, exist_ok=True)
os.makedirs(BAD2_DIR, exist_ok=True)

def run_cmd(cmd):
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running cmd: {cmd}\n{res.stderr}", file=sys.stderr)
    return res

def build_good_fixtures():
    print("[+] Building GOOD long-form fixtures (120s runtime)...")
    vid_path = os.path.join(GOOD_DIR, "video.mp4")
    run_cmd(f'ffmpeg -y -f lavfi -i testsrc=size=1920x1080:rate=30:duration=120 -pix_fmt yuv420p -c:v libx264 "{vid_path}"')

    voice_path = os.path.join(GOOD_DIR, "voice.wav")
    music_path = os.path.join(GOOD_DIR, "music.wav")
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=440:duration=120" -af "volume=7.8dB" "{voice_path}"')
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=120" -af "volume=-10dB" "{music_path}"')

    # Mux audio into video.mp4
    run_cmd(f'ffmpeg -y -i "{vid_path}" -i "{voice_path}" -c:v copy -c:a aac -b:a 192k "{vid_path}.tmp.mp4"')
    if os.path.exists(f"{vid_path}.tmp.mp4"):
        os.replace(f"{vid_path}.tmp.mp4", vid_path)

    # Words: Title keywords in first 5s ("algorithmic", "order", "flow")
    # Pace statement in 5-20s ("In the next 2 minutes, I will show you exactly how liquidity works.")
    # Total words: 310 across 119s -> ~156 WPM
    words = []
    opening = [
        ("How", 0.5, 0.9),
        ("algorithmic", 1.0, 1.8),
        ("order", 1.9, 2.3),
        ("flow", 2.4, 2.9),
        ("operates.", 3.0, 3.8),
        ("In", 6.0, 6.3),
        ("the", 6.4, 6.6),
        ("next", 6.7, 7.0),
        ("2", 7.1, 7.4),
        ("minutes,", 7.5, 8.0),
        ("I", 8.1, 8.3),
        ("will", 8.4, 8.7),
        ("show", 8.8, 9.1),
        ("you", 9.2, 9.4),
        ("exactly", 9.5, 10.0),
        ("how", 10.1, 10.4),
        ("liquidity", 10.5, 11.2),
        ("works.", 11.3, 11.9)
    ]
    for w, s, e in opening:
        words.append({"word": w, "start": s, "end": e})

    body_vocab = ["market", "makers", "exploit", "retail", "liquidity", "pools", "using", "automated", "latency", "arbitrage"]
    t = 13.0
    step = (119.0 - 13.0) / 290
    for i in range(290):
        w_word = body_vocab[i % len(body_vocab)]
        w_start = round(t + i * step, 3)
        w_end = round(w_start + step * 0.85, 3)
        words.append({"word": w_word, "start": w_start, "end": w_end})

    with open(os.path.join(GOOD_DIR, "words.json"), "w", encoding="utf-8") as f:
        json.dump({"all_words": words, "total_words": len(words)}, f, indent=2)

    script_content = """---
title: "Algorithmic Order Flow Liquidity Proof"
promise_sentence: "Show how market makers exploit order book physics."
thumbnail_concept: "Gold liquidation wick piercing obsidian order book"
pace_mode: "focused"
est_runtime_min: 2.0
chapters:
  - id: 1
    title: "The Order Book Illusion"
  - id: 2
    title: "Microstructure Cascades"
  - id: 3
    title: "Delta Neutral Harvest"
  - id: 4
    title: "The Inversion Proof"
cta_line: "If you want to master how algorithmic order flow exploits this exact pattern, watch our breakdown on institutional liquidity right here."
---

# Episode Script
In the next 2 minutes, I will show you exactly how liquidity works.
"""
    with open(os.path.join(GOOD_DIR, "script.md"), "w", encoding="utf-8") as f:
        f.write(script_content)

    # Loop Ledger (4 loops, first payoff at 50s <=90s, primary paid at 105s [87.5%], all paid <=120s)
    loops = [
        {
            "id": 1,
            "question": "How do market makers guarantee profitability during liquidity vacuums?",
            "planted_at_s": 5.0,
            "paid_at_s": 105.0,
            "payoff_type": "primary_insight"
        },
        {
            "id": 2,
            "question": "Why does standard deviation understate extreme tail risk?",
            "planted_at_s": 8.0,
            "paid_at_s": 50.0,
            "payoff_type": "empirical_proof"
        },
        {
            "id": 3,
            "question": "What happens when limit order queues are deliberately stuffed?",
            "planted_at_s": 40.0,
            "paid_at_s": 85.0,
            "payoff_type": "mechanism_reveal"
        },
        {
            "id": 4,
            "question": "How can quantitative traders detect the institutional footprint?",
            "planted_at_s": 70.0,
            "paid_at_s": 112.0,
            "payoff_type": "strategic_resolution"
        }
    ]
    with open(os.path.join(GOOD_DIR, "loop_ledger.json"), "w", encoding="utf-8") as f:
        json.dump(loops, f, indent=2)

    # Shotlist: CTA between 80-98s (starts T-40s >= T-45s, ends T-22s <= T-20s, dur 18s <= 25s)
    # End-screen safe: 100-120s has end_screen_safe: true and on_screen_text: null
    shotlist = {
        "scenes": [
            {"id": 1, "chapter": 0, "scene_name": "Cold Open Hook", "start_s": 0.0, "end_s": 15.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "The Liquidity Lie", "word_count": 3}},
            {"id": 2, "chapter": 0, "scene_name": "Pace Statement", "start_s": 15.0, "end_s": 30.0, "motion_tag": "camera_push", "camera_push_scale": 1.05, "motion_purpose": "Zoom diagram", "pattern_interrupt": False, "end_screen_safe": False, "on_screen_text": {"text": "2 Minutes to Reality", "word_count": 4}},
            {"id": 3, "chapter": 1, "scene_name": "Chapter 1 Breakdown", "start_s": 30.0, "end_s": 55.0, "motion_tag": "manim_transform", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Standard Deviation Fails", "word_count": 3}},
            {"id": 4, "chapter": 2, "scene_name": "Chapter 2 Cascades", "start_s": 55.0, "end_s": 75.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Order Flow Cascades", "word_count": 3}},
            {"id": 5, "chapter": 3, "scene_name": "Disciplined Spoken CTA", "start_s": 80.0, "end_s": 98.0, "motion_tag": "manim_transform", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Watch Institutional Liquidity Next", "word_count": 4}},
            {"id": 6, "chapter": 4, "scene_name": "Primary Payoff", "start_s": 98.0, "end_s": 100.0, "motion_tag": "manim_draw", "pattern_interrupt": False, "end_screen_safe": False, "on_screen_text": None},
            {"id": 7, "chapter": 4, "scene_name": "End Screen YouTube Card Zone", "start_s": 100.0, "end_s": 120.0, "motion_tag": "manim_draw", "pattern_interrupt": False, "end_screen_safe": True, "on_screen_text": None}
        ]
    }
    with open(os.path.join(GOOD_DIR, "shotlist.json"), "w", encoding="utf-8") as f:
        json.dump(shotlist, f, indent=2)

    print("  [OK] Good long-form fixtures ready.")

def build_bad_fixtures():
    print("[+] Building BAD long-form fixtures (failing L2, L3, L5, L7, and 5s freeze)...")
    vid_path = os.path.join(BAD_DIR, "video.mp4")
    concat_cmd = (
        'ffmpeg -y '
        '-f lavfi -i testsrc=size=1920x1080:rate=30:duration=30 '
        '-f lavfi -i color=c=black:size=1920x1080:rate=30:duration=5 '
        '-f lavfi -i testsrc=size=1920x1080:rate=30:duration=85 '
        '-filter_complex "[0:v][1:v][2:v]concat=n=3:v=1:a=0[outv]" '
        f'-map "[outv]" -pix_fmt yuv420p -c:v libx264 "{vid_path}"'
    )
    run_cmd(concat_cmd)

    voice_path = os.path.join(BAD_DIR, "voice.wav")
    music_path = os.path.join(BAD_DIR, "music.wav")
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=440:duration=120" -af "volume=7.8dB" "{voice_path}"')
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=120" -af "volume=-10dB" "{music_path}"')

    run_cmd(f'ffmpeg -y -i "{vid_path}" -i "{voice_path}" -c:v copy -c:a aac -b:a 192k "{vid_path}.tmp.mp4"')
    if os.path.exists(f"{vid_path}.tmp.mp4"):
        os.replace(f"{vid_path}.tmp.mp4", vid_path)

    # Words: No title keywords in first 5s -> FAILS L2
    words = [
        {"word": "Welcome", "start": 0.5, "end": 1.0},
        {"word": "everyone", "start": 1.1, "end": 1.8},
        {"word": "today", "start": 1.9, "end": 2.3},
        {"word": "we", "start": 2.4, "end": 2.6},
        {"word": "discuss", "start": 2.7, "end": 3.4},
        {"word": "general", "start": 3.5, "end": 4.1},
        {"word": "topics.", "start": 4.2, "end": 4.8},
        {"word": "We", "start": 6.0, "end": 6.5},
        {"word": "will", "start": 6.6, "end": 7.0},
        {"word": "look", "start": 7.1, "end": 7.6},
        {"word": "at", "start": 7.7, "end": 8.0},
        {"word": "some", "start": 8.1, "end": 8.6},
        {"word": "charts", "start": 8.7, "end": 9.3},
        {"word": "from", "start": 9.4, "end": 9.9},
        {"word": "last", "start": 10.0, "end": 10.5},
        {"word": "year.", "start": 10.6, "end": 11.2}
    ]
    step = (118.0 - 12.0) / 280
    for i in range(280):
        words.append({"word": "analysis", "start": round(12.0 + i * step, 3), "end": round(12.0 + (i + 0.8) * step, 3)})

    with open(os.path.join(BAD_DIR, "words.json"), "w", encoding="utf-8") as f:
        json.dump({"all_words": words, "total_words": len(words)}, f, indent=2)

    script_content = """---
title: "Algorithmic Order Flow Liquidity Proof"
promise_sentence: "Show general market discussion."
thumbnail_concept: "Generic thumbnail concept"
pace_mode: "focused"
est_runtime_min: 2.0
chapters:
  - id: 1
    title: "Chapter 1"
  - id: 2
    title: "Chapter 2"
  - id: 3
    title: "Chapter 3"
cta_line: ""
---

# Bad Script
No pace statement and missing CTA.
"""
    with open(os.path.join(BAD_DIR, "script.md"), "w", encoding="utf-8") as f:
        f.write(script_content)

    loops = [
        {
            "id": 1,
            "question": "General curiosity question",
            "planted_at_s": 10.0,
            "paid_at_s": 9999.0,
            "payoff_type": "primary_insight"
        }
    ]
    with open(os.path.join(BAD_DIR, "loop_ledger.json"), "w", encoding="utf-8") as f:
        json.dump(loops, f, indent=2)

    shotlist = {
        "scenes": [
            {"id": 1, "chapter": 0, "scene_name": "Intro", "start_s": 0.0, "end_s": 30.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Intro", "word_count": 1}},
            {"id": 2, "chapter": 1, "scene_name": "Freeze Scene", "start_s": 30.0, "end_s": 35.0, "motion_tag": "manim_transform", "hold_tag": None, "pattern_interrupt": False, "end_screen_safe": False, "on_screen_text": {"text": "Static", "word_count": 1}},
            {"id": 3, "chapter": 1, "scene_name": "Main Body", "start_s": 35.0, "end_s": 70.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Body", "word_count": 1}},
            {"id": 4, "chapter": 2, "scene_name": "Section 2", "start_s": 70.0, "end_s": 100.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Section", "word_count": 1}},
            {"id": 5, "chapter": 3, "scene_name": "Ending without CTA", "start_s": 100.0, "end_s": 120.0, "motion_tag": "manim_draw", "pattern_interrupt": False, "end_screen_safe": False, "on_screen_text": {"text": "End", "word_count": 1}}
        ]
    }
    with open(os.path.join(BAD_DIR, "shotlist.json"), "w", encoding="utf-8") as f:
        json.dump(shotlist, f, indent=2)

    print("  [OK] Bad long-form fixtures ready.")

def build_bad2_fixtures():
    print("[+] Building BAD2 long-form fixtures (failing L4, L3, audio, text, end-screen)...")
    vid_path = os.path.join(BAD2_DIR, "video.mp4")
    # 120s moving video (testsrc has zero freezes -> Visual freeze passes)
    run_cmd(f'ffmpeg -y -f lavfi -i testsrc=size=1920x1080:rate=30:duration=120 -pix_fmt yuv420p -c:v libx264 "{vid_path}"')

    # Audio: Voice -14 LUFS, Music -20 LUFS -> Delta is only 6 dB (< 16 dB min) -> FAILS Audio!
    voice_path = os.path.join(BAD2_DIR, "voice.wav")
    music_path = os.path.join(BAD2_DIR, "music.wav")
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=440:duration=120" -af "volume=7.8dB" "{voice_path}"')
    run_cmd(f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=120" -af "volume=1.8dB" "{music_path}"')

    run_cmd(f'ffmpeg -y -i "{vid_path}" -i "{voice_path}" -c:v copy -c:a aac -b:a 192k "{vid_path}.tmp.mp4"')
    if os.path.exists(f"{vid_path}.tmp.mp4"):
        os.replace(f"{vid_path}.tmp.mp4", vid_path)

    # Words:
    # First 5s: "How algorithmic order flow operates." (title keywords present -> L2 passes)
    # Pace statement: "In the next 5 minutes, I will show you exactly how liquidity works." (promised 5 min vs real 2 min -> FAILS L3!)
    # WPM: 180 words over 120s -> 90 WPM (far below focused 150-165 range -> FAILS L3!)
    words = [
        {"word": "How", "start": 0.5, "end": 0.9},
        {"word": "algorithmic", "start": 1.0, "end": 1.8},
        {"word": "order", "start": 1.9, "end": 2.3},
        {"word": "flow", "start": 2.4, "end": 2.9},
        {"word": "operates.", "start": 3.0, "end": 3.8},
        {"word": "In", "start": 6.0, "end": 6.4},
        {"word": "the", "start": 6.5, "end": 6.8},
        {"word": "next", "start": 6.9, "end": 7.3},
        {"word": "5", "start": 7.4, "end": 7.8}, # Promised 5m!
        {"word": "minutes,", "start": 7.9, "end": 8.5},
        {"word": "I", "start": 8.6, "end": 8.9},
        {"word": "will", "start": 9.0, "end": 9.4},
        {"word": "show", "start": 9.5, "end": 9.9},
        {"word": "you", "start": 10.0, "end": 10.3},
        {"word": "exactly", "start": 10.4, "end": 11.0},
        {"word": "how", "start": 11.1, "end": 11.5},
        {"word": "liquidity", "start": 11.6, "end": 12.3},
        {"word": "works.", "start": 12.4, "end": 13.0}
    ]
    # Add slow spaced words (only 160 more words across 105s -> total ~178 words in 118s -> ~90 WPM)
    step = (118.0 - 13.0) / 160
    for i in range(160):
        words.append({"word": "concept", "start": round(13.0 + i * step, 3), "end": round(13.0 + (i + 0.6) * step, 3)})

    with open(os.path.join(BAD2_DIR, "words.json"), "w", encoding="utf-8") as f:
        json.dump({"all_words": words, "total_words": len(words)}, f, indent=2)

    # Script: Intro 45s, 7 chapters -> FAILS L4!
    # Promised runtime 5.0m vs real 2.0m -> FAILS L3!
    script_content = """---
title: "Algorithmic Order Flow Liquidity Proof"
promise_sentence: "Show how market makers exploit order book physics."
thumbnail_concept: "Gold liquidation wick piercing obsidian order book"
pace_mode: "focused"
est_runtime_min: 5.0
chapters:
  - id: 1
    title: "Chapter 1"
  - id: 2
    title: "Chapter 2"
  - id: 3
    title: "Chapter 3"
  - id: 4
    title: "Chapter 4"
  - id: 5
    title: "Chapter 5"
  - id: 6
    title: "Chapter 6"
  - id: 7
    title: "Chapter 7"
cta_line: "If you want to master how algorithmic order flow exploits this exact pattern, watch our breakdown on institutional liquidity right here."
---

# Bad2 Script
Intro is 45s long, contains 7 chapters.
"""
    with open(os.path.join(BAD2_DIR, "script.md"), "w", encoding="utf-8") as f:
        f.write(script_content)

    # Loop Ledger: 4 loops, first paid at 60s, primary paid at 105s, all paid -> L5 PASSES!
    loops = [
        {
            "id": 1,
            "question": "How do algorithms exploit retail liquidity?",
            "planted_at_s": 5.0,
            "paid_at_s": 105.0,
            "payoff_type": "primary_insight"
        },
        {
            "id": 2,
            "question": "Why does standard deviation understate extreme tail risk?",
            "planted_at_s": 8.0,
            "paid_at_s": 60.0,
            "payoff_type": "empirical_proof"
        },
        {
            "id": 3,
            "question": "What happens when limit order queues are deliberately stuffed?",
            "planted_at_s": 40.0,
            "paid_at_s": 85.0,
            "payoff_type": "mechanism_reveal"
        },
        {
            "id": 4,
            "question": "How can quantitative traders detect the institutional footprint?",
            "planted_at_s": 70.0,
            "paid_at_s": 112.0,
            "payoff_type": "strategic_resolution"
        }
    ]
    with open(os.path.join(BAD2_DIR, "loop_ledger.json"), "w", encoding="utf-8") as f:
        json.dump(loops, f, indent=2)

    # Shotlist:
    # Intro ends at 45.0s (> 35s max) -> FAILS L4!
    # 7 chapters -> FAILS L4!
    # Scene 2 has a 9-word text event ("Standard deviation fails to measure the real fat tail risk") -> FAILS Text!
    # Final scene (100-120s) has on_screen_text and end_screen_safe: false -> FAILS End-screen!
    # CTA in 80-98s with triad -> L7 passes!
    shotlist = {
        "scenes": [
            {"id": 1, "chapter": 0, "scene_name": "Cold Open Hook", "start_s": 0.0, "end_s": 45.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "The Liquidity Lie", "word_count": 3}},
            {"id": 2, "chapter": 1, "scene_name": "Chapter 1", "start_s": 45.0, "end_s": 55.0, "motion_tag": "manim_transform", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Standard deviation fails to measure the real fat tail risk", "word_count": 9}}, # 9 words -> FAILS Text!
            {"id": 3, "chapter": 2, "scene_name": "Chapter 2", "start_s": 55.0, "end_s": 65.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Order Book Cascades", "word_count": 3}},
            {"id": 4, "chapter": 3, "scene_name": "Chapter 3", "start_s": 65.0, "end_s": 75.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Liquidity Drain", "word_count": 2}},
            {"id": 5, "chapter": 4, "scene_name": "Chapter 4", "start_s": 75.0, "end_s": 82.0, "motion_tag": "manim_draw", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Harvest Phase", "word_count": 2}},
            {"id": 6, "chapter": 5, "scene_name": "Disciplined Spoken CTA", "start_s": 82.0, "end_s": 98.0, "motion_tag": "manim_transform", "pattern_interrupt": True, "end_screen_safe": False, "on_screen_text": {"text": "Watch Institutional Liquidity Next", "word_count": 4}},
            {"id": 7, "chapter": 6, "scene_name": "Chapter 6 Payoff", "start_s": 98.0, "end_s": 100.0, "motion_tag": "manim_draw", "pattern_interrupt": False, "end_screen_safe": False, "on_screen_text": None},
            {"id": 8, "chapter": 7, "scene_name": "Ending with illegal text", "start_s": 100.0, "end_s": 120.0, "motion_tag": "manim_draw", "pattern_interrupt": False, "end_screen_safe": False, "on_screen_text": {"text": "Don't forget to subscribe to our channel", "word_count": 7}} # Illegal text in last 20s & end_screen_safe=False -> FAILS End-screen!
        ]
    }
    with open(os.path.join(BAD2_DIR, "shotlist.json"), "w", encoding="utf-8") as f:
        json.dump(shotlist, f, indent=2)

    print("  [OK] Bad2 long-form fixtures ready.")

if __name__ == "__main__":
    build_good_fixtures()
    build_bad_fixtures()
    build_bad2_fixtures()
