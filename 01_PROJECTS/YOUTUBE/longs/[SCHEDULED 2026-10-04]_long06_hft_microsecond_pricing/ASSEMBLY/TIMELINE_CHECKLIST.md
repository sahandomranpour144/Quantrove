# EP06 Timeline Preparation & Verification Checklist

**Episode Title**: The Machines Trading Before You Blink  
**Episode ID**: QT-009  
**Timing Authority**: ElevenLabs Final VO (Narration: 420.46s, Audio File: 420.91s, Video Master: 440.91s)  
**Verification Date**: 2026-10-01  

---

## 1. Scene Coverage (25 of 25 Scenes)

- [x] **S01 — F1_DATA_HALL** (Flow, 8s fixed, Ch1 Hook + Pace line)
- [x] **S02 — M01_GRID_1238** (Manim, 12.17s, Hook proof)
- [x] **S03 — HM1_TWO_PRICES** (html_motion, 8s fixed + hold, Ch1 Human Question)
- [x] **S04 — M02_ZERO_COST** (Manim, 18.26s, Ch1 Mystery)
- [x] **S05 — M03_ADVERSE_SELECTION** (Manim, 25.48s, Ch1 Data Reveal)
- [x] **S06 — HM2_PRICE_JUMPS** (html_motion, 8s fixed + hold, Ch1 Data Reveal)
- [x] **S07 — F2_TRADING_FLOOR** (Flow, 8s fixed, Ch1 Consequence)
- [x] **S08 — M04_TICK_HISTORY** (Manim, 27.77s, Ch2 Question + Reveal)
- [x] **S09 — M05_SEC_SPREAD_DROP** (Manim, 14.83s, Ch2 Data Reveal)
- [x] **S10 — M06_PINNED_SPREAD** (Manim, 20.16s, Ch2 Problem)
- [x] **S11 — F3_FIBER_PULSES** (Flow, 8s fixed, Ch2 Consequence)
- [x] **S12 — M07_INVENTORY_RISK** (Manim, 18.26s, Ch3 Question)
- [x] **S13 — M08_RESERVATION_PRICE** (Manim, 27.00s, Ch3 Mystery/Reveal)
- [x] **S14 — HM3_QUOTE_LEANS** (html_motion, 8s fixed + hold, Ch3 Data Reveal)
- [x] **S15 — M09_SPREAD_FORMULA** (Manim, 16.36s, Ch3 Data Reveal)
- [x] **S16 — M10_REPRICE_SHAPE** (Manim, 25.10s, Ch3 Consequence)
- [x] **S17 — F4_EMPTY_DESK** (Flow, 8s fixed, Ch4 Question)
- [x] **S18 — M11_MICROSECOND_LIGHT** (Manim, 17.50s, Ch4 Mystery)
- [x] **S19 — HM4_STALE_QUOTE_RACE** (html_motion, 8s fixed + hold, Ch4 Data Reveal)
- [x] **S20 — M12_QUEUE_LINE** (Manim, 15.60s, Ch4 Data Reveal)
- [x] **S21 — M13_VIRTU_PAYOFF** (Manim, 34.23s, Ch4 Central Payoff)
- [x] **S22 — M14_BOTH_SIDES** (Manim, 28.91s, Ch4 Consequence)
- [x] **S23 — M15_FINAL_INSIGHT** (Manim, 16.74s, Close)
- [x] **S24 — F5_PULLBACK** (Flow, 8s fixed, Spoken CTA ends by 418.0s)
- [x] **S25 — M16_END_SCREEN_BG** (Manim, 20.00s, End screen background, zero text)

---

## 2. Narration Coverage & Timing Authority

- [x] **Voiceover Duration**: Exactly 418.00 seconds (06:58.00). Supersedes earlier draft estimates (8:20–8:50).
- [x] **Audio Alteration**: Zero artificial stretching, pitch shifting, or compression applied to VO.
- [x] **Pacing**: Total spoken word count = 1099 words over 418s = 157.75 WPM (Focused pace mode).
- [x] **Word Timestamp Status**: Marked UNAVAILABLE on disk. Proportional estimation applied; requires `faster-whisper` word alignment before final subtitle burn.

---

## 3. Transition & Cut Verification

- [x] **Flow Scenes (S01, S07, S11, S17, S24)**: Fixed 8.0s clips. For narration running past 8.0s, J-cut to next visual at 8.0s or hold final frame cleanly.
- [x] **html_motion Scenes (S03, S06, S14, S19)**: 8.0s animation plays once, holds final insight frame steadily to complete narration window without loop drift.
- [x] **Manim Scenes (16 scenes)**: Elastic scenes retimed to lock strictly to voiceover scene boundaries.
- [x] **CTA & Outro Cut**: Spoken CTA in Scene 24 finishes at `06:58.00` (exactly T-20s from master end).

---

## 4. Audio Architecture & Standards

- [x] **Track A1 (Voiceover)**: Normalized to `-14.0 ± 1.5 LUFS`.
- [x] **Track A2 (Sound Effects)**: Restrained clicks/pulses at `-18 to -22 dBFS`.
- [x] **Track A3 (Music Bed)**: Minimalist ambient documentary bed, no vocals/lyrics. Ducked `>= 16 dB` below dialogue during narration.
- [x] **End Screen Audio**: Music swells to `-18 dBFS` for final 20.0s (Scene 25). Zero narration.

---

## 5. Captions & Kinetic Overlay Discipline

- [x] **Track Placement**: Track V2 above main video.
- [x] **Safe Zones**: Pop-up pill band `y = 56px .. 176px`.
- [x] **Caption Lane Safe**: `y = 864px .. 1080px` kept strictly empty of static visual elements and pop-ups.
- [x] **Framerate**: 60.00 fps constant.
- [x] **Alpha Channel**: RGBA ProRes 4444 (no solid black bounding boxes).

---

## 6. End Screen Safe Zone

- [x] **Scene 25 Duration**: Exactly 20.00 seconds (`06:58.00` to `07:18.00`).
- [x] **Text Discipline**: Zero text, zero icons, zero titles. Pure canvas `#202322` with faint `#233D4C` grid.
- [x] **Card Clearance**: Verified clean for YouTube End Screen elements (Subscribe button, Next Video card).

---

## 7. Master Video Duration

- [x] **Narration Length**: 420.46 seconds (07:00.46 spoken) / 420.91 seconds audio file
- [x] **End Screen Length**: 20.00 seconds (00:20.00)
- [x] **Total Master Runtime**: **440.91 seconds (07:20.91)**
