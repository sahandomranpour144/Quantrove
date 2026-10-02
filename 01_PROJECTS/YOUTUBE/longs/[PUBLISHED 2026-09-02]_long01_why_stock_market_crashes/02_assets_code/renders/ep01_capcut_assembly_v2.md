# CapCut Assembly Guide — EP01 (v2 — Gemini/Flow hybrid edit)
## "Why Do Stock Market Crashes Actually Happen?"

**Project Name**: `Quantrove_EP01_StockMarketCrashes`
**Target Runtime**: `6:24`
**Export Resolution**: `1920 × 1080` (16:9 Full HD)
**Frame Rate**: `60 fps`
**Audio Target**: `-14 LUFS` (YouTube Standard)
**Editor**: CapCut (Desktop version recommended for 1080p export)

**What's new in v2**: 9 scenes that were static charts/images are now real Gemini
(Flow)-generated video clips, directed by Claude for atmosphere and emotional
weight. Everything else — timeline layout, transitions, text overlays, SFX,
audio mix, export settings — is unchanged from the original guide.

---

## Step 1: Project Setup

1. Open **CapCut Desktop** → Click **New Project**
2. In project settings (top bar or gear icon):
   - Aspect Ratio: `16:9`
   - Resolution: `1080p`
   - Frame Rate: `60 fps`
3. Name the project: `Quantrove_EP01_WhyMarketsCrash`

> **Tip:** Use CapCut Desktop (not mobile) for best quality export and multi-track control.

---

## Step 2: Import All Media

Click **Import** and add all files from these folders:

### From `02_assets_code/renders/` — Import these as videos (MP4), NOT the matching PNG:
These 14 scenes now use video instead of a static image. 8 are original Manim
renders, 6 are new Gemini/Flow clips — visually it doesn't matter to CapCut,
but noted here for your own reference:

| Filename | Source |
|---|---|
| `Scene_01_sp500_crash_animation.mp4` | Manim |
| `Scene_04_panic_symptom_concept.mp4` | **Gemini (new)** |
| `Scene_07_08_crowded_room_metaphor.mp4` | **Gemini (replaces old Manim version)** |
| `Scene_09_order_book_liquidity_drain.mp4` | Manim |
| `Scene_11_three_fires_chapters.mp4` | **Gemini (new)** |
| `Scene_12_roaring_twenties_bull_run.mp4` | **Gemini (new)** |
| `Scene_13_margin_call_wipeout.mp4` | **Gemini (replaces old Manim version)** |
| `Scene_14_black_thursday_tuesday_crash.mp4` | **Gemini (new)** |
| `Scene_19_domino_cascade_2008.mp4` | **Gemini (replaces old Manim version)** |
| `Scene_21_pandemic_shock_backdrop.mp4` | **Gemini (new)** |
| `Scene_23_circuit_breakers_halt.mp4` | Manim |
| `Scene_24_v_shaped_recovery.mp4` | Manim |
| `Scene_27_universal_mechanism.mp4` | **Gemini (replaces old Manim version)** |
| `Scene_29_fifty_years_macro_teaser.mp4` | **Gemini (new)** |

**⚠️ Mute the audio track on all 6 "Gemini (new/replaces)" clips above when you
place them on the timeline** — your voiceover and BGM are the only audio tracks
that should play.

### From `02_assets_code/renders/` — Images (PNG), all remaining scenes:
- `Scene_02_1929_vs_2008_comparison.png`
- `Scene_03_title_card.png`
- `Scene_05_crash_architecture_diagram.png`
- `Scene_06_three_crashes_overview.png`
- `Scene_10_market_decline_taxonomy.png`
- `Scene_15_1929_1932_full_collapse.png`
- `Scene_16_1929_summary_card.png`
- `Scene_17_subprime_pipeline.png`
- `Scene_18_largest_bankruptcies.png`
- `Scene_20_2008_summary_card.png`
- `Scene_22_worst_one_day_point_drops.png`
- `Scene_25_2020_summary_card.png`
- `Scene_26_master_comparison_matrix.png`
- `Scene_28_investor_takeaways.png`
- `Scene_30_outro_end_screen.png`

### Optional supplementary B-roll (not required, available if you want variety):
From `02_assets_code/renders/manim/`:
- `Crash1929Scene.mp4`, `Crash2008Scene.mp4`, `Crash2020Scene.mp4`, `PatternRevealScene.mp4`

> **Note:** `The crowd is standing and walking slowly at a steady.mp4` (the old
> generic crowd placeholder) is now superseded by the directed
> `Scene_07_08_crowded_room_metaphor.mp4` Gemini clip — skip importing it.

### From `voiceover/`:
- `ElevenLabs_video_1 voiceover.mp3`

### From `_channel_brand/background music/`:
- `Tiburtina - Schwartzy.mp3`

---

## Step 3: Timeline Track Layout

```
[Track 3 — TOP]    Text overlays, definition cards, title cards
[Track 2]          SFX audio clips (whooshes, impacts, pings)
[Track 1 — BASE]   All video clips (scenes in order)
─────────────────────────────────────────────────────
[Audio 1]          Voiceover: ElevenLabs_video_1 voiceover.mp3
[Audio 2]          BGM: Tiburtina - Schwartzy.mp3
```

---

## Step 4: Scene Assembly Order

Place the following clips on **Track 1** in this exact order. Use the
**voiceover on Audio 1 as your timing anchor** — sync each visual to the
narration. Durations below are starting points; drag clip edges to match
where the narration actually lands. **The 6 new Gemini clips are fixed
8-second generations** — trim in/out points as needed to fit their beat,
rather than stretching them.

| # | Asset | Duration | Notes |
|---|---|---|---|
| 1 | `Scene_01_sp500_crash_animation.mp4` | Full clip | Opening hook — hard cut start |
| 2 | `Scene_02_1929_vs_2008_comparison.png` | 4s | Ken Burns zoom-in |
| 3 | `Scene_03_title_card.png` | 8s | Title reveal — slow fade in |
| 4 | `Scene_04_panic_symptom_concept.mp4` | ~6-8s, trim to fit | **Gemini** — extreme close-up, trader's anxious face |
| 5 | `Scene_05_crash_architecture_diagram.png` | 6s | |
| 6 | `Scene_06_three_crashes_overview.png` | 8s | |
| 7 | `Scene_07_08_crowded_room_metaphor.mp4` | Full clip | **Gemini** — calm crowd → panic rush, covers both scenes |
| 8 | `Scene_09_order_book_liquidity_drain.mp4` | Full clip | |
| 9 | `Scene_10_market_decline_taxonomy.png` | 6s | |
| 10 | `Scene_11_three_fires_chapters.mp4` | ~5-8s, trim to fit | **Gemini** — three fires, chapter break moment |
| 11 | `Scene_12_roaring_twenties_bull_run.mp4` | Full clip | **Gemini** — 1920s trading floor euphoria |
| 12 | `Scene_13_margin_call_wipeout.mp4` | Full clip + hold | **Gemini** — trader's realization, impact moment |
| 13 | `Scene_14_black_thursday_tuesday_crash.mp4` | Full clip | **Gemini** — same floor, now chaos (mirrors Scene 12) |
| 14 | `Scene_15_1929_1932_full_collapse.png` | 8s | |
| 15 | `Scene_16_1929_summary_card.png` | 5s | 1929 chapter summary |
| 16 | `Scene_17_subprime_pipeline.png` | 7s | |
| 17 | `Scene_18_largest_bankruptcies.png` | 6s | |
| 18 | `Scene_19_domino_cascade_2008.mp4` | Full clip | **Gemini** — falling dominoes, contagion metaphor |
| 19 | `Scene_20_2008_summary_card.png` | 5s | 2008 chapter summary |
| 20 | `Scene_21_pandemic_shock_backdrop.mp4` | ~6-8s, trim to fit | **Gemini** — empty city street, 2020 opener |
| 21 | `Scene_22_worst_one_day_point_drops.png` | 7s | |
| 22 | `Scene_23_circuit_breakers_halt.mp4` | Full clip | |
| 23 | `Scene_24_v_shaped_recovery.mp4` | Full clip | |
| 24 | `Scene_25_2020_summary_card.png` | 5s | 2020 chapter summary |
| 25 | `Scene_26_master_comparison_matrix.png` | 8s | |
| 26 | `Scene_27_universal_mechanism.mp4` | Full clip + hold | **Gemini — KEY MOMENT**, the pattern reveal |
| 27 | `Scene_28_investor_takeaways.png` | 5s | |
| 28 | `Scene_29_fifty_years_macro_teaser.mp4` | Full clip | **Gemini** — skyline time-lapse, tease next episode |
| 29 | `Scene_30_outro_end_screen.png` | 20s | End screen — keep last 20s for YouTube cards |

---

## Step 5: Ken Burns Effect (Zoom) on Static Images ONLY

This now applies only to the 15 remaining PNG clips (the 6 new Gemini clips
already have their own camera movement built into the generation — do NOT
add Ken Burns on top of them, it'll look doubled-up):

1. Select the PNG clip on the timeline
2. Click **Animation** in the right panel
3. Choose **"Zoom In"** or **"Ken Burns"** under Entrance animations
4. Set duration to `0.5s`

---

## Step 6: Pacing Pauses (Storytelling)

After these key "dark moment" lines in the narration, add **a 1–2 second
hold** by extending the current clip (for the Gemini clips, freeze the last
frame rather than stretching the whole clip):

| Moment | Scene | Narration line ending |
|---|---|---|
| ~03:25 | 13 (Gemini) | *"...your entire investment instantly."* — pause before cutting away from the margin call clip |
| ~04:10 | 15/16 | *"...the very same collapsing market."* — pause before 1929 summary card |
| ~04:42 | 19 (Gemini) | *"...already spreading underneath the surface before Lehman ever made headlines."* |
| ~06:05 | 27 (Gemini) | *"The trigger changes. The panic doesn't."* — **the most important line — hold 2s minimum, don't rush this** |

---

## Step 7: Text Overlays (Track 3)

### How to add a text overlay:
1. Move playhead to the target timecode
2. Click **Text → Add Text**
3. Drag the text clip to **Track 3** (above the video)
4. Set duration to match the narration line (~3–4 seconds)

### Style Guide:
- Font: **Inter Bold** (or "Poppins Bold")
- Background: dark (`#0B0E14`), rounded corners, ~80% opacity
- Label (term name): Color `#F59E0B` (Gold)
- Definition: Color `#FFFFFF` (White)
- Animation: Slide Up (Entrance), Fade (Exit)
- Position: Lower-left or lower-center

### Definitions to Add:

| Timecode | Term | Definition |
|---|---|---|
| ~01:50 | **Bear market** | when the market falls 20%+ from its recent peak |
| ~03:10 | **Margin buying** | borrowing money to buy stocks, using stocks as collateral |
| ~03:25 | **The Dow** | average of 30 major U.S. company stock prices |
| ~04:30 | **Bankruptcy** | when a company legally admits it can't pay what it owes |
| ~05:05 | **S&P 500** | broader index of 500 major U.S. companies |
| ~05:25 | **Circuit breaker** | automatic trading pause when market falls too fast |

---

## Step 8: Transitions

| Between | CapCut Transition | Duration |
|---|---|---|
| Scene 01 → 02 | Dissolve | 0.4s |
| Scene 02 → 03 | Fade to Black | 0.3s |
| Scene 03 → 04 | None (Hard Cut) | — |
| 1929 Summary → 2008 intro (16→17) | Fade to Black | 0.5s |
| 2008 Summary → 2020 intro (20→21) | Fade to Black | 0.5s |
| Scene 27 → 28 (Pattern Reveal → Takeaway) | Dissolve | 0.4s |
| Scene 29 → 30 (Teaser → Outro) | Fade to Black | 0.8s |
| All other cuts | Dissolve | 0.3s |

---

## Step 9: Audio Mix

### Audio 1 — Voiceover
1. Drag `ElevenLabs_video_1 voiceover.mp3` to **Audio 1**, starting at `00:00`
2. Volume: `100%`

### Audio 2 — Background Music
1. Drag `Tiburtina - Schwartzy.mp3` to **Audio 2**, starting at `00:00`
2. Volume: `15–20%`
3. Fade In: `2s` / Fade Out: `8s`

### Clip audio (new step)
Confirm all 6 Gemini clips are muted on the timeline — check each one
individually, since Flow sometimes generates ambient audio you don't want
bleeding into the mix.

### SFX Layer
| Timecode | Scene | SFX Type | CapCut Search Term |
|---|---|---|---|
| `00:00` | 01 | Sub-bass boom/impact | "market crash impact" / "bass drop" |
| `~01:00` | 04 | Data ping | "ui notification" / "data ping" |
| `~02:10` | 08 | Trading alarm (muffled) | "alarm siren" / "crowd panic" |
| `~02:30` | 09 | Fast downward whoosh | "whoosh down" / "swipe down" |
| `~03:00` | 11 | Short chord hit | "transition sting" / "impact hit" |
| `~03:25` | 13 | Harsh impact | "hit hard" / "glass break" |
| `~04:20` | 17 | Data ping | "click ui" / "data tick" |
| `~04:42` | 19 | Domino clicks | "domino fall" / "click sequence" |
| `~05:25` | 23 | Loud alarm | "stock market alarm" / "halt siren" |
| `~05:35` | 24 | Rising tone | "uplifting rise" / "sweep up" |
| `~06:05` | 27 | Soft whoosh cascade | "soft whoosh" / "reveal transition" |

---

## Step 10: Color Adjustment

Apply to the PNG/Manim clips as before:
- **Brightness**: `-5` / **Contrast**: `+10` / **Saturation**: `+8` / **Highlights**: `-10`
- Manim MP4s: add a **Glow** filter for the glowing chart lines

For the 6 Gemini clips, apply this more conservatively — eyeball each one
first, since Flow's generations often already have cinematic grading baked
in and a full pass on top can look over-processed.

---

## Step 11: Export Settings

1. Click **Export** (top right)
2. Resolution: `1080p` / Frame Rate: `60 fps` / Format: `MP4` / Quality: **Recommended** or **High**
3. Output filename: `Quantrove_EP01_WhyMarketsCrash_MASTER.mp4`
4. Save to: `E:\AI_COMPANY\01_PROJECTS\YOUTUBE\long_form\long01_why_stock_market_crashes\`

> **Note:** Turn off the CapCut watermark before exporting (Settings → Watermark).

---

## Final Pre-Upload Checklist

- [ ] Runtime is 6:24 (±5s acceptable)
- [ ] No black frames mid-video
- [ ] All 6 Gemini clips have audio MUTED
- [ ] Ken Burns NOT applied to the 6 Gemini video clips (PNGs only)
- [ ] All 6 text definitions appear and are readable
- [ ] Audio voiceover is clear, BGM is in background (~15-20% volume)
- [ ] No CapCut watermark on exported file
- [ ] Outro (Scene 30) is 20s long for YouTube end screen cards
- [ ] Pacing pauses in place at the 4 key moments (esp. Scene 27 — don't rush it)
- [ ] Ken Burns applied to all remaining static PNG clips
