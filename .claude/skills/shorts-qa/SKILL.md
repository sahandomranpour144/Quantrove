---
name: shorts-qa
description: Automated Gate 2 QA verification for Quantrove Shorts. Audits video length, hook timing, freezedetect static frames, loudness mix, voice WPM, text event pacing/contrast, beat structure, motion tags, and clean outro against shorts_style.json.
---

# Shorts QA — Gate 2 Quality Assurance for Quantrove Shorts

## Overview
Every Quantrove Short must pass the automated QA gate before CEO review or publication. The checks enforce Rules R1 through R10 defined in `.claude/rules/shorts-style.md` and parameter thresholds in `01_PROJECTS/YOUTUBE/pipeline/config/shorts_style.json`.

## Command

```bash
python "01_PROJECTS/YOUTUBE/pipeline/qa/shorts_qa.py" \
  --video "path/to/short.mp4" \
  --words "path/to/words.json" \
  --text-events "path/to/text_events.json" \
  --shotlist "path/to/shotlist.json" \
  --voice "path/to/voice.wav" \
  --music "path/to/music.wav"
```

## Evaluated Rules
- **R1 (Hook)**: Spoken word starts < 0.5s, first text event starts <= 0.1s, hook in first 3.0s.
- **R2 (Static Frame Ceiling)**: `freezedetect` (d=3.5s). Freezes only permitted inside scenes tagged `HOLD_FOR_UNDERSTANDING` (max 5.0s).
- **R3 (Audio Mix)**: Voice stem -14 ± 1.5 LUFS; music stem >= 16 dB below voice.
- **R4 (Pacing & Delivery)**: 145–160 WPM (±10 WPM warn margin).
- **R5/R6 (Unified Text System)**: Max 4 words per chunk, min 0.7s on screen, no overlapping events, WCAG contrast >= 7:1, max 1 badge per Short.
- **R7 (Structure & Duration)**: Native Shorts require beats `IDEA -> SIMPLE_WRONG -> COMPLEX_WRONG -> INSIGHT`. Duration must be 30–45s (ffprobe measured).
- **R8 (Motion Discipline)**: Every scene has a valid motion tag (`manim_draw`, `manim_transform`, `camera_push`, `flow_atmosphere`, `html_motion`). Camera push <= 1.08 scale with explicit purpose. Flow atmosphere <= 20% of runtime. `html_motion` allowed at most 1 clip per Short (2–8s, terminal/UI metaphor, holds final frame; see [HTML_MOTION_STANDARD.md](../../01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md)).
- **R9 (Clean Exit)**: Video cut <= 1.0s after last spoken word. No CTA or forbidden engagement bait words (`subscribe`, `follow`, `like`, `comment`, `link in bio`, `ebook`). No outro card.
- **R10 (Premium Feel)**: Flagged for human review (`MANUAL`).

## Output & Exit Codes
- Output is a formatted table: `Rule | Measured | Threshold | Status`
- Exit Code `0`: All rules `PASS`, `WARN`, or `MANUAL`.
- Exit Code `1`: Any rule fails. Gate 2 blocked.
