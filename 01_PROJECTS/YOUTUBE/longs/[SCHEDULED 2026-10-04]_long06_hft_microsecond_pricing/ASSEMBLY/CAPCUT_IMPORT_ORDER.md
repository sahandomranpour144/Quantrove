# CapCut Final Assembly Guide — EP06

**Episode Title**: The Machines Trading Before You Blink  
**Episode ID**: QT-009  
**Canvas / Resolution**: 1920x1080 (16:9) @ 60.00 fps  
**Master Timing Authority**: `EP06_VO_FINAL.mp3` (Spoken Narration: 420.46s / 07:00.46, Audio File: 420.91s / 07:00.91)  
**Total Master Video Runtime**: **440.91s (07:20.91)** (including 20.00s YouTube End Screen)  
**Gate 2 Status**: **APPROVED 100% BY CEO (Ready for Final Assembly)**  

---

## 1. Track Architecture & Routing

```text
Track V2 (Overlay) : 00_OVERLAY_EP06_kinetic_word_pops_60fps.mov (1080p60 RGBA QuickTime RLE)
Track V1 (Main)    : Scene Visuals S01–S25 (1080p MP4s from Flow, HTML Motion, and Manim)
--------------------------------------------------------------------------------------------------
Track A1 (VO)      : EP06_VO_FINAL.mp3 (Master Narration, normalized to -14.0 ± 1.0 LUFS)
Track A2 (SFX)     : Accent ticks, thuds, queue clicks, alert tones (-18 to -22 dBFS)
Track A3 (Music)   : Ambient Documentary Pulse Bed (Ducked >= 16 dB below VO; swells at 07:00)
```

---

## 2. Sequential Assembly Guide (Track V1 & A1 Sync)

All media files reside directly in `TIMELINE_MEDIA/`. Ingest them in this exact order:

### Step 1: Voiceover Base (Track A1)
- Import `EP06_VO_FINAL.mp3`.
- Snap to timeline start: `00:00:00.00`.
- Verify total clip length: `07:00.91` (420.91s).
- Lock Track A1. *Zero speed or pitch adjustment.*

### Step 2: Scene Visuals Sequence (Track V1)

| Scene | In Point | Out Point | Visual Dur | Asset Filename | Engine | Cut Mechanics & Visual Handling |
|---|---|---|---:|---|---|---|
| **S01** | `00:00.00` | `00:12.26` | 12.26s | `EP06_SC01_DATA_HALL.mp4` | Flow | 8s Flow clip plays 00:00–00:08. Holds final frame 00:08–00:12.26 (or J-cut S02 at 00:08). |
| **S02** | `00:12.96` | `00:27.96` | 15.00s | `EP06_SC02_GRID_1238.mp4` | Manim | 1,238-cell grid. "ONE LOSING DAY" callout badge pops at 00:20. |
| **S03** | `00:28.58` | `00:40.58` | 12.00s | `EP06_SC03_TWO_PRICES.mp4` | html_motion | 8s HTML MP4; holds final 1¢ spread frame to 00:40.58. |
| **S04** | `00:41.28` | `01:00.18` | 18.90s | `EP06_SC04_ZERO_COST.mp4` | Manim | Glosten-Milgrom zero cost stack resolves to Spread > 0. |
| **S05** | `01:00.86` | `01:23.64` | 22.78s | `EP06_SC05_ADVERSE_SELECTION.mp4` | Manim | Uninformed vs informed traders hitting quote node. |
| **S06** | `01:24.48` | `01:36.14` | 11.66s | `EP06_SC06_PRICE_JUMPS.mp4` | html_motion | 8s HTML MP4; holds -0.10 loss readout frame to 01:36.14. |
| **S07** | `01:36.76` | `01:46.84` | 10.08s | `EP06_SC07_TRADING_FLOOR.mp4` | Flow | 8s Flow archive floor clip; holds final frame to 01:46.84. |
| **S08** | `01:47.48` | `02:17.00` | 29.52s | `EP06_SC08_TICK_HISTORY.mp4` | Manim | Step chart: 12.5¢ -> 6.25¢ -> 1¢. Bottom tag: 0.125% -> 0.020%. |
| **S09** | `02:17.64` | `02:34.92` | 17.28s | `EP06_SC09_SEC_SPREAD_DROP.mp4` | Manim | Quoted spread drop bars: NYSE -37%, Nasdaq -50%. |
| **S10** | `02:35.58` | `02:53.60` | 18.02s | `EP06_SC10_PINNED_SPREAD.mp4` | Manim | Pinned spread at $100.00/100.01; dashed 0.5¢ level. |
| **S11** | `02:54.24` | `03:04.86` | 10.62s | `EP06_SC11_FIBER_PULSES.mp4` | Flow | 8s Flow fiber pulse macro clip; holds frame to 03:04.86. |
| **S12** | `03:05.48` | `03:23.20` | 17.72s | `EP06_SC12_INVENTORY_RISK.mp4` | Manim | Inventory box units q=0->3 stacking with risk penalty. |
| **S13** | `03:23.84` | `03:46.44` | 22.60s | `EP06_SC13_RESERVATION_PRICE.mp4` | Manim | Avellaneda-Stoikov formula: `r = s - q·γ·σ²·(T-t)`. |
| **S14** | `03:47.08` | `04:01.06` | 13.98s | `EP06_SC14_QUOTE_LEANS.mp4` | html_motion | 9s HTML MP4; holds 98.80 reservation shift frame to 04:01.06. |
| **S15** | `04:01.70` | `04:16.38` | 14.68s | `EP06_SC15_SPREAD_FORMULA.mp4` | Manim | Risk penalty (~$0.40) + Competition (~$1.29) = $1.69. |
| **S16** | `04:17.04` | `04:40.58` | 23.54s | `EP06_SC16_REPRICE_SHAPE.mp4` | Manim | Dynamic repricing curve table & next buyer uncertainty. |
| **S17** | `04:41.16` | `04:50.68` | 9.52s | `EP06_SC17_EMPTY_DESK.mp4` | Flow | 8s Flow empty trading desk clip; holds frame to 04:50.68. |
| **S18** | `04:51.34` | `05:08.90` | 17.56s | `EP06_SC18_MICROSECOND_LIGHT.mp4` | Manim | Speed of light ruler: 300m vacuum vs 200m fiber in 1 us. |
| **S19** | `05:09.52` | `05:25.70` | 16.18s | `EP06_SC19_STALE_QUOTE_RACE.mp4` | html_motion | 9s HTML MP4; holds stale quote race result frame to 05:25.70. |
| **S20** | `05:26.32` | `05:40.10` | 13.78s | `EP06_SC20_QUEUE_LINE.mp4` | Manim | Price-time priority queue at $100.00: incoming fills #1, #2. |
| **S21** | `05:40.72` | `06:08.34` | 27.62s | `EP06_SC21_VIRTU_PAYOFF.mp4` | Manim | Virtu central payoff: market-neutral instant hedge simulation. |
| **S22** | `06:08.98` | `06:35.42` | 26.44s | `EP06_SC22_BOTH_SIDES.mp4` | Manim | Knight Capital ~$460M loss vs unfair advantage debate. |
| **S23** | `06:36.06` | `06:51.54` | 15.48s | `EP06_SC23_FINAL_INSIGHT.mp4` | Manim | Final insight frame: 1¢ spread is priced doubt before click. |
| **S24** | `06:52.22` | `07:00.46` | 8.24s | `EP06_SC24_PULLBACK.mp4` | Flow | 8s Flow server pullback clip. Narration ends at 07:00.46. |
| **S25** | `07:00.91` | `07:20.91` | 20.00s | `EP06_SC25_END_SCREEN_BG.mp4` | Manim | Clean #202322 background with faint #233D4C grid. Zero text. |

---

### Step 3: Kinetic Overlay Placement (Track V2)
- Import `00_OVERLAY_EP06_kinetic_word_pops_60fps.mov`.
- Place on **Track V2** starting at `00:00:00.00`.
- Duration: exactly `07:00.92`.
- Blending mode: Normal (alpha channel automatically recognized).

---

### Step 4: Music & Sound Design (Tracks A2 & A3)
- Track A2: Place soft click SFX on queue fills (S03, S06, S14, S20) and subtle alert tone on Knight Capital loss (S22). Keep at `-18 to -22 dBFS`.
- Track A3: Ambient electronic pulse bed. Ducked `>= 16 dB` below dialogue during narration (levels `-28 to -32 dBFS`).
- Swell at End Screen: At `07:00.46` (narration end), music fades up to `-18 dBFS` and plays solo through `07:20.41`, fading to black over the final 0.5s.

---

## 3. Final Export Specifications
- **Container**: MP4 (H.264 / AAC)
- **Resolution**: 1920 x 1080
- **Framerate**: 60.00 fps constant
- **Bitrate**: VBR 2-pass, Target 25 Mbps, Max 30 Mbps
- **Audio Profile**: Stereo, 48 kHz, 320 kbps AAC, Integrated Loudness `-14.0 ± 1.0 LUFS`, Max True Peak `-1.0 dBFS`.
