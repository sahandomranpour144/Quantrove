#!/usr/bin/env python3
"""
Quantrove Shorts Text Events Generator
Reads words.json (faster-whisper word timestamps) + shorts_style.json (+ optional shotlist.json)
Outputs text_events.json adhering to Quantrove Shorts Style System rules R5/R6/R10.
"""

import json
import os
import sys
import re
import argparse

DEFAULT_STYLE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config", "shorts_style.json"
)

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def clean_word(w):
    return re.sub(r"[^\w]", "", w).strip()

def is_emphasis_candidate(word_str):
    """Identify candidate words for emphasis: numbers, currency, percentages, acronyms, key terms."""
    w = word_str.strip(".,!?;:\"'()[]{}")
    if re.search(r"\d", w):  # numbers like 80%, 2008, 10x
        return True
    if w.isupper() and len(w) >= 2:  # acronyms like AI, GPU, Fed
        return True
    if w.startswith("$") or w.endswith("%"):
        return True
    return False

def generate_text_events(words_data, style_config, shotlist=None):
    # Extract words list
    if isinstance(words_data, dict):
        words = words_data.get("all_words") or words_data.get("words") or []
    elif isinstance(words_data, list):
        words = words_data
    else:
        words = []

    if not words:
        return []

    chunk_cfg = style_config.get("chunk", {})
    anim_cfg = style_config.get("animation", {})
    badge_cfg = style_config.get("badge", {})

    max_words = chunk_cfg.get("max_words", 4)
    min_on_screen_s = chunk_cfg.get("min_on_screen_s", 0.7)
    pause_thresh = chunk_cfg.get("break_on_pause_s", 0.25)
    stop_words = set(w.lower() for w in chunk_cfg.get("never_end_on", []))
    zone_y_range = chunk_cfg.get("zone_y_pct", [60, 76])
    default_chunk_y = round((zone_y_range[0] + zone_y_range[1]) / 2.0, 1)

    # 1. Group words into raw chunks
    raw_chunks = []
    curr = []

    for i, w in enumerate(words):
        curr.append(w)
        is_last = (i == len(words) - 1)
        next_w = words[i + 1] if not is_last else None

        should_break = False

        if is_last:
            should_break = True
        elif len(curr) >= max_words:
            should_break = True
        elif next_w and (next_w["start"] - w["end"] >= pause_thresh):
            should_break = True
        elif any(w["word"].endswith(p) for p in [".", "!", "?", ";"]):
            should_break = True

        # Stop words check: if breaking now, check if w is in stop_words
        w_clean = clean_word(w["word"]).lower()
        if should_break and not is_last and w_clean in stop_words:
            # Try to avoid ending on stop word
            if len(curr) < max_words and next_w and (next_w["start"] - w["end"] < pause_thresh):
                # We can take one more word instead of breaking here
                should_break = False
            elif len(curr) > 1:
                # Break BEFORE the stop word so stop word starts the next chunk
                curr.pop()
                raw_chunks.append(curr)
                curr = [w]
                should_break = False

        if should_break and curr:
            raw_chunks.append(curr)
            curr = []

    if curr:
        raw_chunks.append(curr)

    # 2. Fix orphan lone words if not emphasis
    merged_chunks = []
    i = 0
    while i < len(raw_chunks):
        c = raw_chunks[i]
        if len(c) == 1 and not is_emphasis_candidate(c[0]["word"]):
            # Lone word that is not emphasis -> merge with previous if space
            if merged_chunks and len(merged_chunks[-1]) + 1 <= max_words:
                merged_chunks[-1].extend(c)
            elif i + 1 < len(raw_chunks) and len(raw_chunks[i + 1]) + 1 <= max_words:
                raw_chunks[i + 1] = c + raw_chunks[i + 1]
            else:
                merged_chunks.append(c)
        else:
            merged_chunks.append(c)
        i += 1

    # 3. Locate INSIGHT badge if present in shotlist
    badge_event = None
    badge_start = None
    badge_end = None
    if shotlist and badge_cfg:
        scenes = shotlist.get("scenes") or shotlist if isinstance(shotlist, list) else []
        for s in scenes:
            if s.get("beat") == badge_cfg.get("beat", "INSIGHT"):
                b_start = round(float(s.get("start_s", s.get("startSec", 0.0))), 2)
                b_hold = badge_cfg.get("hold_s", [1.2, 1.8])[0]
                b_end = round(b_start + b_hold, 2)
                badge_words_raw = s.get("badge") or s.get("headline", "INSIGHT")
                b_words = [clean_word(w).upper() for w in badge_words_raw.split()][:badge_cfg.get("max_words", 3)]
                b_y_range = badge_cfg.get("zone_y_pct", [42, 52])
                b_y = round((b_y_range[0] + b_y_range[1]) / 2.0, 1)

                badge_event = {
                    "start": b_start,
                    "end": b_end,
                    "words": [{"word": bw, "start": b_start, "end": b_end} for bw in b_words],
                    "type": "badge",
                    "y_pct": b_y,
                    "emphasis_word": None
                }
                badge_start = b_start
                badge_end = b_end
                break

    # 4. Build text events with timing & emphasis
    events = []
    for c_idx, c in enumerate(merged_chunks):
        first_w = c[0]
        last_w = c[-1]

        # Onset offset: starts 0-20ms before word onset
        start_t = max(0.0, round(first_w["start"] - 0.02, 3))
        end_t = round(last_w["end"], 3)

        # Minimum on-screen duration enforcement
        if round(end_t - start_t, 3) < min_on_screen_s:
            end_t = round(start_t + min_on_screen_s, 3)

        # Emphasis word selection (at most 1 per chunk)
        emphasis_word = None
        for w in c:
            if is_emphasis_candidate(w["word"]):
                emphasis_word = clean_word(w["word"])
                break

        # If badge is alone_on_screen, adjust or avoid overlapping
        if badge_event and badge_cfg.get("alone_on_screen", True):
            if not (end_t <= badge_start or start_t >= badge_end):
                # Overlaps with badge
                if start_t < badge_start:
                    end_t = min(end_t, badge_start)
                else:
                    start_t = max(start_t, badge_end)

        events.append({
            "start": start_t,
            "end": end_t,
            "words": [{"word": w["word"], "start": round(w["start"], 3), "end": round(w["end"], 3)} for w in c],
            "type": "chunk",
            "y_pct": default_chunk_y,
            "emphasis_word": emphasis_word
        })

    # 5. Fix overlaps between adjacent chunk events (gap_ms: 0, hard_cut exit)
    # Sort events by start time
    all_events = events
    if badge_event:
        all_events.append(badge_event)
    all_events.sort(key=lambda x: x["start"])

    # Ensure no overlaps and minimum duration
    cleaned_events = []
    for i, ev in enumerate(all_events):
        if i > 0 and ev["start"] < cleaned_events[-1]["end"]:
            # Adjust previous end to eliminate overlap
            cleaned_events[-1]["end"] = ev["start"]
            # Recheck min duration: if prev is too short due to collision, adjust start if possible
            if cleaned_events[-1]["end"] - cleaned_events[-1]["start"] < min_on_screen_s:
                pass
        cleaned_events.append(ev)

    return cleaned_events

def main():
    parser = argparse.ArgumentParser(description="Generate text_events.json for Quantrove Shorts")
    parser.add_argument("--words", required=True, help="Path to words.json")
    parser.add_argument("--style", default=DEFAULT_STYLE_PATH, help="Path to shorts_style.json")
    parser.add_argument("--shotlist", default=None, help="Path to shotlist.json (optional)")
    parser.add_argument("--output", default="text_events.json", help="Path to output text_events.json")

    args = parser.parse_args()

    words_data = load_json(args.words)
    style_config = load_json(args.style)
    shotlist = load_json(args.shotlist) if args.shotlist and os.path.exists(args.shotlist) else None

    events = generate_text_events(words_data, style_config, shotlist)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)

    print(f"Generated {len(events)} text events -> {args.output}")

if __name__ == "__main__":
    main()
