# EP06 — html_motion Prompts (5 clips: 4 long-form, 1 vertical Short)
**How to use each prompt (Path A, manual):**
1. Copy the whole code block under 'PROMPT' into Claude, Gemini or Grok (run 2-3 and pick the best).
2. Open the HTML in Chrome. In the console run `setTime(0)`, then a mid time, then the final time, and compare with the spec.
3. If any color outside the palette appears, any text under the minimum size, or anything outside the safe box, ask the model to fix it and re-run.
4. Export MP4 (1080p, 60fps, exact duration). Save the MP4 and the HTML as `<scene_id>_<N>s.mp4` and `<scene_id>_<N>s.html`.
5. Put both in the `html_motion/` folder named in the agent prompt. The agent runs the QA check and adds the episode prefix.

QA command the agent will run: `python 01_PROJECTS/YOUTUBE/pipeline/qa/html_motion_qa.py <clip.mp4> --html <file.html> --aspect 16:9|9:16 --dur N`

---
## HM1_TWO_PRICES — Scene 3
| Field | Value |
|---|---|
| scene_id | HM1_TWO_PRICES |
| episode | long06_hft_microsecond_pricing |
| slot duration | 8.0s |
| aspect | 16:9 |
| concept | Bid and ask panels with the one-cent spread bracketed. |
| focal element | The bid/ask pair. |
| data source | ILLUSTRATIVE (tag: ILLUSTRATIVE DATA) |

**PROMPT**

```text
Create ONE self-contained HTML file (inline HTML/CSS/JS, no CDN, no audio, no external assets) that runs in Chrome.
- Stage fixed 1920x1080, scaled to fit the window, centered, background #202322.
- Duration exactly 8.0 s. Play once t=0..8, then hold the final frame. NOT a loop.
- Deterministic: all visuals are a pure function render(t). Expose window.setTime(t). Seeded PRNG only. No CSS animations, no Date.now drift, no free randomness. Autoplay drives render(t) from one clock.
- Colors only: #202322 (bg), #233D4C (grid/dividers), #C3D809 (primary accent), #FD802E (risk/anomaly), #E6EDF3 (text). Opacity variations allowed. No other colors, gradients, glow, shadows, particles, HUD circles.
- Font: "Nohemi","Inter",system-ui,sans-serif; tabular-nums for numbers.
- Legibility: min font 28px (16:9) / 40px (9:16); max 3 secondary readouts; one focal element; main line >=3px, grid 1px.
- Safe zone: For 16:9 (1920x1080): Safe stage box x=96..1824, y=190..856 (width 1728px, height 666px). Forbidden caption lane y=864..1080; popup band y=56..176. For 9:16 (1080x1920): Safe stage band x=60..880, y=250..1000 (visuals only). Forbidden text band y=1040..1440; reserved margins top=250, bottom=480, left=60, right=200. Keep the caption/pop-up region empty. No narration keywords in the graphic.
- Numbers: real data with source, or a corner tag "ILLUSTRATIVE DATA". Never present invented figures as real.
- Motion: ease-in-out, 0.4s stagger, no bounce, calm final hold >= 0.5s.
- Output only the complete HTML.

SCENE SPEC (use only the 16:9 safe zone; draw nothing outside x=96..1824, y=190..856):
Layout (px):
- Corner tag "ILLUSTRATIVE DATA": right-aligned at x=1824, y=190..226, 28px, #E6EDF3 at 60% opacity.
- BID panel: rect x=96..900, y=250..560, 1px border #233D4C, no fill. Label "BID" 32px #E6EDF3 at 70% opacity at x=128, y=282. Price "100.00" 132px bold #E6EDF3 centered at x=498, y=420. 4px underline #C3D809 under the price (x=330..666, y=500).
- ASK panel: rect x=1020..1824, y=250..560, same style. Label "ASK". Price "100.01" 132px bold, centered at x=1422. 4px underline #C3D809 (x=1254..1590, y=500).
- Spread bracket: horizontal line y=610 from x=498 to x=1422, 3px #C3D809, with 24px vertical end ticks (y=598..622).
- Spread block centered at x=960: label "SPREAD" 36px #E6EDF3 at 70% opacity (y=655..691); value "0.01" 96px bold #C3D809 (y=700..800).
- Last-trade line centered at x=960, y=820..852, 32px #E6EDF3, text "LAST  BUY 100.01" or "LAST  SELL 100.00".
Secondary readouts: spread value and last-trade line only.
Timeline (seconds):
0.00-0.50: panel borders fade in.
0.50-1.30: BID label, price, underline fade in and slide from 40px left to final position.
1.30-2.10: ASK label, price, underline fade in and slide from 40px right.
2.10-3.00: bracket draws outward from the center to both ends, end ticks appear; at 3.00 the SPREAD label and value fade in over 0.4s.
3.20: BUY at ask. ASK panel border flashes #C3D809 for 0.3s, ask price scales 1.00 -> 1.04 -> 1.00, last-trade line reads "LAST  BUY 100.01".
4.00: SELL at bid. BID panel border flashes #C3D809 for 0.3s, bid price pulses the same way, line reads "LAST  SELL 100.00".
4.80: BUY at ask (same effect). 5.60: SELL at bid. 6.40: BUY at ask.
6.50-8.00: calm hold. Prices stay 100.00 and 100.01, bracket and last-trade line visible. This is the final frame.
Self-check: call setTime(0), setTime(4), setTime(8) and confirm the three frames match this spec.
```

---
## HM2_PRICE_JUMPS — Scene 6
| Field | Value |
|---|---|
| scene_id | HM2_PRICE_JUMPS |
| episode | long06_hft_microsecond_pricing |
| slot duration | 8.0s |
| aspect | 16:9 |
| concept | A machine sells at 100.01, then the price jumps ten cents and its old ask becomes stale. |
| focal element | The price chart with the machine's bid and ask lines. |
| data source | ILLUSTRATIVE (tag: ILLUSTRATIVE DATA) |

**PROMPT**

```text
Create ONE self-contained HTML file (inline HTML/CSS/JS, no CDN, no audio, no external assets) that runs in Chrome.
- Stage fixed 1920x1080, scaled to fit the window, centered, background #202322.
- Duration exactly 8.0 s. Play once t=0..8, then hold the final frame. NOT a loop.
- Deterministic: all visuals are a pure function render(t). Expose window.setTime(t). Seeded PRNG only. No CSS animations, no Date.now drift, no free randomness. Autoplay drives render(t) from one clock.
- Colors only: #202322 (bg), #233D4C (grid/dividers), #C3D809 (primary accent), #FD802E (risk/anomaly), #E6EDF3 (text). Opacity variations allowed. No other colors, gradients, glow, shadows, particles, HUD circles.
- Font: "Nohemi","Inter",system-ui,sans-serif; tabular-nums for numbers.
- Legibility: min font 28px (16:9) / 40px (9:16); max 3 secondary readouts; one focal element; main line >=3px, grid 1px.
- Safe zone: For 16:9 (1920x1080): Safe stage box x=96..1824, y=190..856 (width 1728px, height 666px). Forbidden caption lane y=864..1080; popup band y=56..176. For 9:16 (1080x1920): Safe stage band x=60..880, y=250..1000 (visuals only). Forbidden text band y=1040..1440; reserved margins top=250, bottom=480, left=60, right=200. Keep the caption/pop-up region empty. No narration keywords in the graphic.
- Numbers: real data with source, or a corner tag "ILLUSTRATIVE DATA". Never present invented figures as real.
- Motion: ease-in-out, 0.4s stagger, no bounce, calm final hold >= 0.5s.
- Output only the complete HTML.

SCENE SPEC (use only the 16:9 safe zone; draw nothing outside x=96..1824, y=190..856):
Layout (px):
- Corner tag "ILLUSTRATIVE DATA": right-aligned at x=1824, y=190..226, 28px, #E6EDF3 at 60% opacity.
- Plot area: x=200..1480, y=240..800. Price axis: 100.20 at y=240, 99.90 at y=800 (1866.7 px per 1.00). Gridlines 1px #233D4C at 100.20 (y=240), 100.10 (y=427), 100.00 (y=613), 99.90 (y=800). Axis labels 28px #E6EDF3 at 70% opacity, right-aligned at x=190: "100.20", "100.10", "100.00", "99.90".
- Three lines, each 3px: BID line at 100.00 (y=613) in #C3D809; ASK line at 100.01 (y=595) in #C3D809; PRICE line (the market price) in #E6EDF3, starting at 100.01 (y=595).
- Reveal cursor: lines are drawn left to right; the cursor x(t) = 200 + (t-0.6)/5.9*1280 for t from 0.6 to 6.5. Draw each line only up to the cursor.
- Right column x=1540..1824, three readouts only: "SOLD AT" (label 28px #E6EDF3 at 70%, value 56px bold #E6EDF3, y=300), "PRICE NOW" (y=480), "LOSS" (y=660; value in #FD802E).
Timeline (seconds):
0.00-0.60: gridlines and axis labels fade in.
0.60-3.00: BID, ASK and PRICE lines draw to the cursor. Label "MACHINE QUOTES" 28px #E6EDF3 near x=260, y=560 fades in at 1.2.
3.00: a 14px square marker in #E6EDF3 appears on the ask line at the cursor, label "SOLD @ 100.01" 28px #E6EDF3 above-left of it. Readout SOLD AT shows "100.01".
3.40-3.60: PRICE line steps up to 100.11 (y=408) over 0.2s with ease. Readout PRICE NOW shows "100.11".
3.80-4.60: ASK line turns #FD802E. Label "STALE ASK" 28px #FD802E at x=850, y=560. A vertical bracket at x=900 from y=595 up to y=408, 3px #FD802E, with label "-0.10" 40px bold #FD802E beside it. Readout LOSS shows "-0.10" in #FD802E.
5.20-5.80: BID and ASK lines step up to 100.10 (y=427) and 100.11 (y=408) over 0.5s with ease; the ask line turns back to #C3D809. Label "REPRICED" 28px #C3D809 at x=1100, y=470.
6.50-8.00: calm hold, cursor at x=1480. This is the final frame.
Self-check: call setTime(2), setTime(4.5), setTime(8) and confirm the frames match this spec.
```

---
## HM3_QUOTE_LEANS — Scene 14
| Field | Value |
|---|---|
| scene_id | HM3_QUOTE_LEANS |
| episode | long06_hft_microsecond_pricing |
| slot duration | 8.0s |
| aspect | 16:9 |
| concept | Three buys push a market maker's reservation price and both quotes down. |
| focal element | The reservation line with the bid and ask lines around it. |
| data source | ILLUSTRATIVE textbook parameters (tag: ILLUSTRATIVE DATA, second line TEXTBOOK PARAMETERS) |

**PROMPT**

```text
Create ONE self-contained HTML file (inline HTML/CSS/JS, no CDN, no audio, no external assets) that runs in Chrome.
- Stage fixed 1920x1080, scaled to fit the window, centered, background #202322.
- Duration exactly 8.0 s. Play once t=0..8, then hold the final frame. NOT a loop.
- Deterministic: all visuals are a pure function render(t). Expose window.setTime(t). Seeded PRNG only. No CSS animations, no Date.now drift, no free randomness. Autoplay drives render(t) from one clock.
- Colors only: #202322 (bg), #233D4C (grid/dividers), #C3D809 (primary accent), #FD802E (risk/anomaly), #E6EDF3 (text). Opacity variations allowed. No other colors, gradients, glow, shadows, particles, HUD circles.
- Font: "Nohemi","Inter",system-ui,sans-serif; tabular-nums for numbers.
- Legibility: min font 28px (16:9) / 40px (9:16); max 3 secondary readouts; one focal element; main line >=3px, grid 1px.
- Safe zone: For 16:9 (1920x1080): Safe stage box x=96..1824, y=190..856 (width 1728px, height 666px). Forbidden caption lane y=864..1080; popup band y=56..176. For 9:16 (1080x1920): Safe stage band x=60..880, y=250..1000 (visuals only). Forbidden text band y=1040..1440; reserved margins top=250, bottom=480, left=60, right=200. Keep the caption/pop-up region empty. No narration keywords in the graphic.
- Numbers: real data with source, or a corner tag "ILLUSTRATIVE DATA". Never present invented figures as real.
- Motion: ease-in-out, 0.4s stagger, no bounce, calm final hold >= 0.5s.
- Output only the complete HTML.

SCENE SPEC (use only the 16:9 safe zone; draw nothing outside x=96..1824, y=190..856):
Model (Avellaneda-Stoikov, textbook parameters s=100, gamma=0.1, sigma=2, k=1.5, T-t=1; spread 1.69; penalty 0.40 per unit). Use EXACTLY these values, do not recompute:
q=0: reservation 100.00, bid 99.16, ask 100.85
q=1: reservation 99.60, bid 98.76, ask 100.45
q=2: reservation 99.20, bid 98.36, ask 100.05
q=3: reservation 98.80, bid 97.96, ask 99.65
Layout (px):
- Corner tag "ILLUSTRATIVE DATA" right-aligned at x=1824, y=190..226, 28px, #E6EDF3 at 60% opacity; second line "TEXTBOOK PARAMETERS" y=228..260, same style.
- Plot area: x=210..1290, y=290..820. Price axis: 101.00 at y=290, 97.50 at y=820 (151.43 px per 1.00). Gridlines 1px #233D4C at 101.00 (y=290), 100.00 (y=441), 99.00 (y=593), 98.00 (y=744). Axis labels 28px #E6EDF3 at 70% opacity, right-aligned at x=200: "101.00", "100.00", "99.00", "98.00".
- Dashed 1px reference line at 100.00 in #E6EDF3 at 40% opacity with label "MID 100.00" 28px at x=1100..1280, y=405.
- RESERVATION line: 3px #C3D809, full plot width; label "RESERVATION" 28px #C3D809 at x=230, 40px above the line.
- BID and ASK lines: 2px #E6EDF3 at 85% opacity, full plot width; labels "ASK" and "BID" 28px at x=230 (ASK 40px above its line, BID 40px below its line... keep labels inside the plot).
- Right column x=1380..1824, exactly three readouts: "INVENTORY" (y=300, value "q = 0"), "RESERVATION" (y=470, value 72px bold #C3D809), "SPREAD" (y=640, value "1.69" 72px bold #E6EDF3). Labels 28px #E6EDF3 at 70% opacity.
Timeline (seconds):
0.00-0.60: gridlines, axis labels, reference line fade in.
0.60-1.20: RESERVATION, BID, ASK lines draw left to right at the q=0 values; readouts fade in.
1.40, 2.60, 3.80: a buy happens. A 16px square in #C3D809 flashes on the bid line at x=1250 for 0.25s, INVENTORY value increments (q = 1, 2, 3), then over 0.5s with ease the three lines move to the next row of the table and the RESERVATION readout counts to the new value.
4.80-5.20: bracket at x=1330 between 100.00 (y=441) and 98.80 (y=623), 3px #FD802E, label "-1.20" 36px bold #FD802E (with a #202322 label background so the text is readable over lines).
6.50-8.00: calm hold at q=3. This is the final frame.
Self-check: call setTime(0.9), setTime(4.4), setTime(8) and confirm lines sit at the table values.
```

---
## HM4_STALE_QUOTE_RACE — Scene 19
| Field | Value |
|---|---|
| scene_id | HM4_STALE_QUOTE_RACE |
| episode | long06_hft_microsecond_pricing |
| slot duration | 8.0s |
| aspect | 16:9 |
| concept | A price moves on another venue. A fast machine pulls its quote; a slow machine's quote is hit at the old price. |
| focal element | Two lanes (fast and slow) with a sweeping playhead. |
| data source | ILLUSTRATIVE (tag: ILLUSTRATIVE DATA); times are not measurements |

**PROMPT**

```text
Create ONE self-contained HTML file (inline HTML/CSS/JS, no CDN, no audio, no external assets) that runs in Chrome.
- Stage fixed 1920x1080, scaled to fit the window, centered, background #202322.
- Duration exactly 8.0 s. Play once t=0..8, then hold the final frame. NOT a loop.
- Deterministic: all visuals are a pure function render(t). Expose window.setTime(t). Seeded PRNG only. No CSS animations, no Date.now drift, no free randomness. Autoplay drives render(t) from one clock.
- Colors only: #202322 (bg), #233D4C (grid/dividers), #C3D809 (primary accent), #FD802E (risk/anomaly), #E6EDF3 (text). Opacity variations allowed. No other colors, gradients, glow, shadows, particles, HUD circles.
- Font: "Nohemi","Inter",system-ui,sans-serif; tabular-nums for numbers.
- Legibility: min font 28px (16:9) / 40px (9:16); max 3 secondary readouts; one focal element; main line >=3px, grid 1px.
- Safe zone: For 16:9 (1920x1080): Safe stage box x=96..1824, y=190..856 (width 1728px, height 666px). Forbidden caption lane y=864..1080; popup band y=56..176. For 9:16 (1080x1920): Safe stage band x=60..880, y=250..1000 (visuals only). Forbidden text band y=1040..1440; reserved margins top=250, bottom=480, left=60, right=200. Keep the caption/pop-up region empty. No narration keywords in the graphic.
- Numbers: real data with source, or a corner tag "ILLUSTRATIVE DATA". Never present invented figures as real.
- Motion: ease-in-out, 0.4s stagger, no bounce, calm final hold >= 0.5s.
- Output only the complete HTML.

SCENE SPEC (use only the 16:9 safe zone; draw nothing outside x=96..1824, y=190..856):
Layout (px):
- Corner tag "ILLUSTRATIVE DATA" right-aligned at x=1824, y=190..226, 28px, #E6EDF3 at 60% opacity.
- Event label "PRICE MOVES ELSEWHERE" 28px #E6EDF3 at x=300, y=240..270.
- FAST lane: label "FAST UPDATE" 32px #E6EDF3 at x=96, y=330; lane rect x=300..1700, y=290..450, 1px border #233D4C. Resting quote bar: 24px high, centered in the lane (y=358..382), x=300..1700, #C3D809.
- SLOW lane: label "SLOW UPDATE" 32px #E6EDF3 at x=96, y=550; lane rect x=300..1700, y=510..670, 1px border #233D4C. Resting quote bar: y=578..602, x=300..1700, #C3D809.
- Time axis ticks (1px #233D4C vertical lines through both lanes) at x=300, 767, 1233, 1700 with labels 28px #E6EDF3 at 70% opacity at y=720..756: "0", "+50 us", "+100 us", "+150 us" (write the microsecond sign as the character mu followed by s).
- Event line: vertical 3px #E6EDF3 at x=300 from y=270 to y=670.
- Playhead: vertical 2px #E6EDF3 at 80% opacity, y=270..670, sweeping from x=300 to x=1700 linearly between t=1.5 and t=6.0 (150 microseconds maps to 1400px).
- Bottom readouts (exactly two, 28px, y=800..840): left at x=300 "FAST: QUOTE PULLED" in #C3D809; right at x=1000 "SLOW: FILLED AT OLD PRICE" in #FD802E.
Timeline (seconds):
0.00-0.60: lanes, ticks and axis labels fade in.
0.60-1.30: lane labels and resting bars fade in.
1.30-1.50: event line and its label appear (short pulse on the label).
1.50-6.00: playhead sweeps.
2.70 (playhead reaches x=673): the FAST bar is cut off at x=673 and fades out over 0.3s; label "QUOTE PULLED" 28px #C3D809 at x=680, y=330; bottom-left readout fades in.
4.20 (playhead reaches x=1140): the SLOW bar turns #FD802E and a 20px square flashes at x=1140 on the bar; label "HIT AT OLD PRICE" 28px #FD802E at x=1150, y=550; bottom-right readout fades in.
6.00-6.50: playhead fades out.
6.50-8.00: calm hold with both readouts visible. This is the final frame.
Self-check: call setTime(2), setTime(3.5), setTime(5), setTime(8) and confirm the frames match this spec.
```

---
## HMS4_QUOTE_LEANS_VERTICAL — Short 4 (ep06_short_04)
| Field | Value |
|---|---|
| scene_id | HMS4_QUOTE_LEANS_VERTICAL |
| episode | long06_hft_microsecond_pricing |
| slot duration | 7.0s |
| aspect | 9:16 |
| concept | Vertical version of the quote-leans scene for the Short 'How Machines Price Their Own Risk'. |
| focal element | The reservation line with the bid and ask lines around it. |
| data source | ILLUSTRATIVE textbook parameters (tag: ILLUSTRATIVE DATA) |

**PROMPT**

```text
Create ONE self-contained HTML file (inline HTML/CSS/JS, no CDN, no audio, no external assets) that runs in Chrome.
- Stage fixed 1080x1920, scaled to fit the window, centered, background #202322.
- Duration exactly 7.0 s. Play once t=0..7, then hold the final frame. NOT a loop.
- Deterministic: all visuals are a pure function render(t). Expose window.setTime(t). Seeded PRNG only. No CSS animations, no Date.now drift, no free randomness. Autoplay drives render(t) from one clock.
- Colors only: #202322 (bg), #233D4C (grid/dividers), #C3D809 (primary accent), #FD802E (risk/anomaly), #E6EDF3 (text). Opacity variations allowed. No other colors, gradients, glow, shadows, particles, HUD circles.
- Font: "Nohemi","Inter",system-ui,sans-serif; tabular-nums for numbers.
- Legibility: min font 28px (16:9) / 40px (9:16); max 3 secondary readouts; one focal element; main line >=3px, grid 1px.
- Safe zone: For 16:9 (1920x1080): Safe stage box x=96..1824, y=190..856 (width 1728px, height 666px). Forbidden caption lane y=864..1080; popup band y=56..176. For 9:16 (1080x1920): Safe stage band x=60..880, y=250..1000 (visuals only). Forbidden text band y=1040..1440; reserved margins top=250, bottom=480, left=60, right=200. Keep the caption/pop-up region empty. No narration keywords in the graphic.
- Numbers: real data with source, or a corner tag "ILLUSTRATIVE DATA". Never present invented figures as real.
- Motion: ease-in-out, 0.4s stagger, no bounce, calm final hold >= 0.5s.
- Output only the complete HTML.

SCENE SPEC (use only the 9:16 safe zone; draw nothing outside x=60..880, y=250..1000; min font 40px):
Use EXACTLY these values, do not recompute (textbook parameters s=100, gamma=0.1, sigma=2, k=1.5, T-t=1; spread 1.69):
q=0: reservation 100.00, bid 99.16, ask 100.85
q=1: reservation 99.60, bid 98.76, ask 100.45
q=2: reservation 99.20, bid 98.36, ask 100.05
q=3: reservation 98.80, bid 97.96, ask 99.65
Layout (px):
- Corner tag "ILLUSTRATIVE DATA" right-aligned at x=880, y=250..290, 40px, #E6EDF3 at 60% opacity.
- Plot area: x=190..880, y=330..740. Price axis: 101.50 at y=330, 97.50 at y=740 (102.5 px per 1.00). Gridlines 1px #233D4C at 101.00 (y=381), 100.00 (y=484), 99.00 (y=586), 98.00 (y=689). Axis labels 40px #E6EDF3 at 70% opacity, right-aligned at x=180: "101", "100", "99", "98".
- Dashed 1px line at 100.00 in #E6EDF3 at 40% opacity, label "MID 100.00" 40px right-aligned at x=880, 46px above the line.
- RESERVATION line 3px #C3D809 full plot width; label "RESERVATION" 40px #C3D809 at x=200, 46px above the line. BID and ASK lines 2px #E6EDF3 at 85% opacity; label "ASK" at x=200, 46px above the ask line; label "BID" at x=200, 6px below the bid line.
- Stacked readouts below the plot, three rows only, label left-aligned at x=60 (40px, #E6EDF3 at 70%) and value right-aligned at x=880 (56px bold): row 1 y=770..840 "INVENTORY" value "q = 0"; row 2 y=850..920 "RESERVATION" value #C3D809; row 3 y=920..990 "SPREAD" value "1.69".
Timeline (seconds):
0.00-0.50: gridlines, labels and dashed line fade in.
0.50-1.00: RESERVATION, BID, ASK lines draw left to right at q=0; readouts fade in.
1.20, 2.20, 3.20: a buy happens. A 20px square in #C3D809 flashes at the right end of the bid line for 0.25s, INVENTORY increments, then over 0.45s with ease the three lines move to the next row of the table and the RESERVATION value counts to the new number.
4.20-4.60: a vertical bracket at x=850 between 100.00 (y=484) and 98.80 (y=607), 3px #FD802E, label "-1.20" 48px bold #FD802E left of it, with a #202322 label background.
5.50-7.00: calm hold at q=3. This is the final frame.
Self-check: call setTime(0.8), setTime(4), setTime(7) and confirm the lines sit at the table values.
```

---
