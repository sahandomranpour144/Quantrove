# Quantrove Post-Assembly Finishing & Editorial Polish Guide

**Episode Title**: The Machines Trading Before You Blink  
**Episode ID**: QT-009  
**Master Standard**: Reusable Editorial Finishing Template for Quantrove Long-Form Production  
**Authority**: Institutional Data Intelligence Production Standard  

---

## 1. Transition Philosophy

Quantrove produces serious, analytical data documentaries. The editing style reflects institutional clarity, not creator-economy hyperactivity:

- **Information Clarity First**: Cuts must never obscure numbers, graphs, or narration keywords.
- **Minimalist Aesthetic**: Over 90% of transitions on the timeline are clean, instantaneous **hard cuts**.
- **No Flashy Transitions**: Strictly zero whip pans, zoom transitions, glitch effects, RGB chromatic aberration splits, page curls, or light leaks.
- **Where Hard Cuts Are Preferred**:
  - Between sequential vector scenes (Manim → Manim).
  - On strong rhetorical pauses and narration beats.
  - When cutting from narration setup into terminal UI (Manim → html_motion).
- **Where Fades / Dissolves Are Acceptable**:
  - Major chapter pivot points where tone shifts (e.g. historical archive footage in Flow).
  - Dark-to-dark transitions between server aisles and abstract spaces.
  - Duration: Strictly limited to **0.25s – 0.40s** (15–24 frames at 60fps).
- **Where Motion-Based Continuity Is Preferred**:
  - When a Flow clip's camera dolly-in momentum naturally carries the viewer's eye into a Manim data zoom or expanding grid.

---

## 2. Complete Scene-by-Scene Transition Table (S01 to S25)

| Transition | Outgoing Engine | Incoming Engine | Visual In Point | Recommended Transition | Duration | Editorial Rationale |
|---|---|---|---:|---|---:|---|
| **S01 → S02** | Flow (`F1_DATA_HALL`) | Manim (`M01_GRID_1238`) | `00:12.96` | **Hard Cut / J-Cut** | Instant | Server dolly momentum lands directly on the 1,238-cell grid as the hook line resolves. |
| **S02 → S03** | Manim (`M01_GRID_1238`) | html_motion (`HM1_TWO_PRICES`) | `00:28.58` | **Hard Cut** | Instant | "Start with the thing it sells: The spread." Clean cut from grid to Bid/Ask terminal bracket. |
| **S03 → S04** | html_motion (`HM1_TWO_PRICES`) | Manim (`M02_ZERO_COST`) | `00:41.28` | **Hard Cut** | Instant | "So why does the gap exist at all?" Cut from held terminal spread to Glosten-Milgrom zero-cost stack. |
| **S04 → S05** | Manim (`M02_ZERO_COST`) | Manim (`M03_ADVERSE_SELECTION`) | `01:00.86` | **Hard Cut** | Instant | "expecting to earn exactly zero." Clean cut to adverse selection market maker node. |
| **S05 → S06** | Manim (`M03_ADVERSE_SELECTION`) | html_motion (`HM2_PRICE_JUMPS`) | `01:24.48` | **Hard Cut** | Instant | "Slow it down." Immediate hard cut to the live price jump chart. |
| **S06 → S07** | html_motion (`HM2_PRICE_JUMPS`) | Flow (`F2_TRADING_FLOOR`) | `01:36.76` | **Soft Dissolve** | `0.30s` (18f) | Chapter 1 to Chapter 2 bridge. Dissolves from held terminal loss into archive trading floor silhouettes. |
| **S07 → S08** | Flow (`F2_TRADING_FLOOR`) | Manim (`M04_TICK_HISTORY`) | `01:47.48` | **Hard Cut** | Instant | "Who decides how small a spread can be?" Hard cut from dark floor into tick size step chart. |
| **S08 → S09** | Manim (`M04_TICK_HISTORY`) | Manim (`M05_SEC_SPREAD_DROP`) | `02:17.64` | **Hard Cut** | Instant | Step chart resolves to 1¢ floor; cut directly to SEC -37% and -50% spread drop comparison bars. |
| **S09 → S10** | Manim (`M05_SEC_SPREAD_DROP`) | Manim (`M06_PINNED_SPREAD`) | `02:35.58` | **Hard Cut** | Instant | "Then came a stranger problem." Cut to tick-constrained pinned spread at $100.00/100.01. |
| **S10 → S11** | Manim (`M06_PINNED_SPREAD`) | Flow (`F3_FIBER_PULSES`) | `02:54.24` | **Soft Dissolve** | `0.25s` (15f) | Chapter 2 to Chapter 3 bridge. Pinned spread dissolves into macro fiber-optic light pulses. |
| **S11 → S12** | Flow (`F3_FIBER_PULSES`) | Manim (`M07_INVENTORY_RISK`) | `03:05.48` | **Hard Cut** | Instant | "So how does a machine choose where to quote?" Cut from fiber speed to Avellaneda-Stoikov inventory box. |
| **S12 → S13** | Manim (`M07_INVENTORY_RISK`) | Manim (`M08_RESERVATION_PRICE`) | `03:23.84` | **Hard Cut** | Instant | "would rather own nothing." Direct cut into full reservation price mathematical formula breakdown. |
| **S13 → S14** | Manim (`M08_RESERVATION_PRICE`) | html_motion (`HM3_QUOTE_LEANS`) | `03:47.08` | **Hard Cut** | Instant | "how much the machine hates risk." Cut from formula to live quote leans simulation. |
| **S14 → S15** | html_motion (`HM3_QUOTE_LEANS`) | Manim (`M09_SPREAD_FORMULA`) | `04:01.70` | **Hard Cut** | Instant | "trying to get rid of what it just bought." Cut to spread formula decomposition ($0.40 + $1.29). |
| **S15 → S16** | Manim (`M09_SPREAD_FORMULA`) | Manim (`M10_REPRICE_SHAPE`) | `04:17.04` | **Hard Cut** | Instant | "The numbers are not the point. The shape is." Cut to dynamic repricing curve table. |
| **S16 → S17** | Manim (`M10_REPRICE_SHAPE`) | Flow (`F4_EMPTY_DESK`) | `04:41.16` | **Soft Dissolve** | `0.30s` (18f) | Chapter 3 to Chapter 4 bridge. Question mark dissolves into quiet empty trading desk at night. |
| **S17 → S18** | Flow (`F4_EMPTY_DESK`) | Manim (`M11_MICROSECOND_LIGHT`) | `04:51.34` | **Hard Cut** | Instant | "A microsecond is one millionth of a second." Hard cut to 300m physical distance ruler. |
| **S18 → S19** | Manim (`M11_MICROSECOND_LIGHT`) | html_motion (`HM4_STALE_QUOTE_RACE`) | `05:09.52` | **Hard Cut** | Instant | "one of them hears it first." Cut into dual-lane stale quote race simulation. |
| **S19 → S20** | html_motion (`HM4_STALE_QUOTE_RACE`) | Manim (`M12_QUEUE_LINE`) | `05:26.32` | **Hard Cut** | Instant | "now measured in microseconds." Cut to price-time priority order queue line. |
| **S20 → S21** | Manim (`M12_QUEUE_LINE`) | Manim (`M13_VIRTU_PAYOFF`) | `05:40.72` | **Hard Cut** | Instant | "Speed is how you get to the front." Cut to the Virtu central payoff grid and Simons law of large numbers. |
| **S21 → S22** | Manim (`M13_VIRTU_PAYOFF`) | Manim (`M14_BOTH_SIDES`) | `06:08.98` | **Hard Cut** | Instant | "the tiny edge in the Simons story." Cut to Knight Capital $460M loss vs unfair advantage debate. |
| **S22 → S23** | Manim (`M14_BOTH_SIDES`) | Manim (`M15_FINAL_INSIGHT`) | `06:36.06` | **Hard Cut** | Instant | "pricing risk, and arriving first." Cut to final insight spread bar (priced doubt). |
| **S23 → S24** | Manim (`M15_FINAL_INSIGHT`) | Flow (`F5_PULLBACK`) | `06:52.22` | **Soft Dissolve** | `0.30s` (18f) | Insight frame dissolves into slow server pullback aisle (spoken CTA window). |
| **S24 → S25** | Flow (`F5_PULLBACK`) | Manim (`M16_END_SCREEN_BG`) | `07:00.91` | **Dip to Black** | `0.40s` (24f) | Spoken narration ends; visual dips cleanly to black and rises into clean end-screen safe slate. |

---

## 3. Color Adjustment & Grade Guide

Quantrove enforces a strict 5-token palette single source of truth (`brand/brand_tokens.json`):
- **Canvas / Background**: Raisin Black `#202322` (RGB: `32, 35, 34`)
- **Grids / Wireframes / Chrome**: Charcoal Slate `#233D4C` (RGB: `35, 61, 76`)
- **Primary / Upward Moves**: Power Lime `#C3D809` (RGB: `195, 216, 9`)
- **Risk / Anomalies / Loss**: Pumpkin `#FD802E` (RGB: `253, 128, 46`)
- **Text / Readouts**: Off-White `#E6EDF3` (RGB: `230, 237, 243`)

### Color Workflow in CapCut
1. **Manim Scenes (16 scenes)**:
   - **Adjustment**: **NONE (Zero Grade)**.
   - Manim scenes are mathematically rendered to exact hex coordinates. Applying global LUTs or contrast filters distorts `#C3D809` and `#FD802E`.
2. **html_motion Clips (4 scenes)**:
   - **Adjustment**: **NONE (Zero Grade)**.
   - HTML exports render exact CSS hex codes. Keep untouched.
3. **Google Flow Cinematic Footage (5 scenes)**:
   - **Adjustment**: **Targeted Match to Brand Canvas**.
   - Flow clips feature organic lighting. Check shadow values in CapCut scopes:
     - **Shadows**: Black point must align with `#202322` (Lift shadows slightly if crushed to pure `0,0,0`; pull down if washed out above RGB 45).
     - **Midtone Tint**: Cool slate-blue bias to match `#233D4C`.
     - **Saturation**: Desaturate by `-5%` to `-10%` if organic colors show warm yellows or reds.
     - **Highlights**: Controlled; no blown-out neon clips.
4. **Sharpness & Noise**:
   - Zero added digital sharpness.
   - Flow footage grain: leave natural. Do not apply heavy temporal denoisers that cause smearing.

---

## 4. Master Fade Rules & Timing

| Fade Point | Visual Fade Duration | Audio Fade Duration | Mechanics |
|---|---|---|---|
| **Opening Head** | `0.50s` (30 frames) | `0.05s` (3 frames) | Visual fades up smoothly from pure black into Scene 1 server aisle. Voiceover begins cleanly at `00:00.00` without click or pop. |
| **Major Chapter Bridges** | `0.25s – 0.30s` (15–18f) | Cross-continuous | Soft cross-dissolve between narrative chapters (S06→S07, S10→S11, S16→S17, S23→S24). |
| **End Screen Entrance** | `0.40s` (24 frames) | Continuous bed swell | Scene 24 CTA ends at `07:00.46`. Visual dips to black over 0.20s and resolves onto Scene 25 `#202322` slate at `07:00.91`. |
| **Outro Tail (Master Exit)** | `0.50s` (30 frames) | `0.50s` (30 frames) | Video and music bed fade smoothly to black from `07:20.41` to `07:20.91`. |

---

## 5. Visual Effects Policy

### Permitted Effects (Restrained Editorial Use Only)
- **Subtle Camera Push (Slow Scale)**: Permitted on long held visual frames (max scale factor `<= 1.08` over 10–15 seconds). Must serve an editorial purpose (e.g. slowly pushing toward the center of the 1,238-grid or focusing on the formula term).
- **Background Defocus**: Permitted in Flow footage to keep background unreadable and text-safe.
- **Micro-Shake / Handheld Emulation**: **FORBIDDEN**. Camera must feel mounted, smooth, tripod or steady dolly.

### Strictly Forbidden Effects
- ❌ Flashy transition packs (film burn, light leak, zoom, glitch, slice).
- ❌ Artificial particles, sparks, glowing floating dust.
- ❌ HUD circular gauges, sci-fi overlays, holographic interfaces.
- ❌ Stylized color LUTs (teal & orange, vintage film, hyper-saturated commercial).
- ❌ Speed ramping / time warp on data animations.

---

## 6. Master Audio Finishing Architecture

### Track Hierarchy & Standards
1. **Track A1: Master Voiceover (`EP06_VO_FINAL.mp3`)**
   - **Target Loudness**: `-14.0 ± 1.0 LUFS` integrated.
   - **True Peak**: Max `-1.0 dBFS`.
   - **EQ Profile**: Clean high-pass filter at `80 Hz` (18 dB/octave) to eliminate sub-rumble; gentle dip at `300 Hz` if boomy; subtle air shelf above `10 kHz`.
   - **Dynamics**: Transparent dialogue compression (2:1 ratio, slow attack, fast release, 2–3 dB gain reduction max).
2. **Track A2: Foley & Sound Design**
   - **Peak Level**: `-18.0 to -22.0 dBFS` (never compete with vocal clarity).
   - **Placement**: Clean clicks on order executions and queue line fills (S03, S06, S14, S20); subtle ominous pulse on Knight Capital loss (S22). Zero cartoon whooshes or loud boom risers.
3. **Track A3: Ambient Documentary Music Bed**
   - **Style**: Minimalist, rhythmic pulse, dark electronic, zero vocals/lyrics.
   - **Ducking Policy**: Ducked strictly by `>= 16 dB` under dialogue throughout speech (`-28.0 to -32.0 dBFS`).
   - **End Screen Swell**: At `07:00.46` (dialogue end), music volume rises smoothly (+10 dB to `-18.0 dBFS`) to carry viewer energy into YouTube end cards through `07:20.41`.

---

## 7. Pre-Export Final Master Checklist

Execute this verification pass immediately before exporting from CapCut:

### Visual Quality Check
- [ ] No single black frame between scene cuts (all 25 clips snap head-to-tail).
- [ ] Track V2 kinetic overlay runs continuously from `00:00.00` to `07:00.92` with transparency intact.
- [ ] Zero white squares, tofu boxes, or broken glyphs across all 25 scenes.
- [ ] All 4 HTML motion clips hold their final data frames steadily without looping or snapping to black.
- [ ] Scene 25 end screen (`07:00.91` to `07:20.91`) is completely free of text and graphics.

### Audio Mix Check
- [ ] Dialogue is consistently audible, punchy, and centered at `-14.0 LUFS`.
- [ ] Music bed never drowns out voiceover during fast-paced passages.
- [ ] No digital clipping, distortion, or harsh sibilance on peaks.
- [ ] Outro music fades smoothly to silence at `07:20.91`.

### Packaging & YouTube Integration
- [ ] Official Title verified: *The Machines Trading Before You Blink* (6 words, 37 chars).
- [ ] YouTube description chapters match the exact timeline (`00:00`, `00:28`, `01:47`, `03:05`, `04:41`, `05:40`, `06:36`, `07:00`).
- [ ] End screen card coordinates configured for Subscribe button and EP05 video link.
