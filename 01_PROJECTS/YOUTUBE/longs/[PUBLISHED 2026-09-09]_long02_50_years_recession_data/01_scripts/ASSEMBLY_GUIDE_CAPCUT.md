# EP02 CapCut Video Assembly Guide (Manim & AI Video Pipeline)
## "What Does 50 Years of Data Say About Recessions?"

> **Production Standard**: Exactly like Episode 1 (`Crash2008Scene.mp4`), all data charts are **1080p 60fps Manim MP4 animations** located in `02_assets_code/renders/manim/`, layered alongside **8–10s cinematic AI video cutaways** from Google Flow / Gemini.

---

## 1. Master Project Settings
* **Aspect Ratio**: `16:9` (1920x1080)
* **Frame Rate**: `60 fps` (matches Manim native render rate)
* **Canvas Background Color**: Hex `#0B0E14` (Quantrove Deep Slate)
* **Master Voiceover Track**: `voiceover/generated_audio/full_voiceover_ep02.mp3` (Duration: **8:07 / 487s**)

---

## 2. Thumbnail Integration (For Unverified Channels & High CTR)

Because your YouTube channel cannot upload custom thumbnails directly in YouTube Studio without phone verification, use **this proven built-in CapCut technique** so YouTube automatically selects your custom high-CTR thumbnail:

### Method A: The Frame-1 Video Inject (Guaranteed YouTube Auto-Select)
1. In CapCut, import `00_FRAME1_00m00s_thumbnail_cover_embed.jpg` from `02_assets_code/ALL_MEDIA_TIMELINE/`.
2. Place this image at the **very start of the timeline (`00:00.00`) on Track V1**.
3. Set its duration to **2–4 frames (approx. 0.05 to 0.1 seconds)** before Scene 1 begins.
4. When you upload the video to YouTube, YouTube generates 3 thumbnail previews from your video. The **1st preview frame will be this exact high-CTR thumbnail image**! Select it with one click during the upload step.

### Method B: CapCut Cover Setting (Embedded MP4 Cover)
1. On the left side of the CapCut timeline, click **"Cover"** (or click **"Edit Cover"** in the Export window).
2. Choose **"Select from computer"** and pick `00_FRAME1_00m00s_thumbnail_cover_embed.jpg`.
3. Click **Save**. This bakes the thumbnail metadata directly into the exported MP4 file.

---

## 3. Multi-Track Timeline Architecture

```
[TRACK V3 - Text Callouts]   : Dynamic Title Overlays, Chapter Markers, Definition Badges
[TRACK V2 - AI Video Cutaways]: 8–10s Cinematic B-Roll from Flow / Gemini (Cross-Dissolved at key moments)
[TRACK V1 - Manim Animations]: 6 Full-Motion 1080p 60fps Manim MP4s (02_assets_code/renders/manim/)
──────────────────────────────────────────────────────────────────────────────────────────────────────────
[TRACK A1 - Voiceover Audio] : Gemini TTS 'Orus' Audio (generated_audio/scene01 – scene07)
[TRACK A2 - SFX / Accents]   : Whooshes, Alarm Bells, Stamp Impacts, Clock Ticks
[TRACK A3 - Music Bed]       : Ambient Documentary Music ("Tiburtina" @ -22dB, swells to -14dB at outro)
```

---

## 3. Second-by-Second Assembly Timeline

### SCENE 1: THE HOOK (0:00 – 0:43) | Voiceover: `scene01_hook.mp3` (43s)
* **0:00 – 0:25**: Place `renders/manim/Hook50YrRecessionScene.mp4` (25.0s) on **Track V1**.
  * Dynamic S&P 500 curve sweeps across 1970–2025 on log scale.
  * All 7 historical recession bands illuminate sequentially with glowing borders.
  * Green recovery beacon pulses at the 2009 bottom.
* **0:25 – 0:35**: Cut to **AI Video Clip 1** (Wall Street Panic / Red Ticker Glow from Flow) on **Track V2** with 0.4s cross-dissolve to inject human emotion.
* **0:35 – 0:43**: Hold `Hook50YrRecessionScene.mp4` endframe on Track V1 with Title Banner on Track V3: *"What Does 50 Years of Data Say About Recessions?"*.

---

### SCENE 2: THE TWO-QUARTER MYTH (0:43 – 1:42) | Voiceover: `scene02_two_quarter_myth.mp3` (59s)
* **0:43 – 1:09**: Place `renders/manim/NBERFrameworkScene.mp4` (26.0s) on **Track V1**.
  * Left panel "2 Quarters GDP" gets stamped with bold red ❌ *"NOT OFFICIAL"*.
  * Right panel reveals the 4 official NBER indicators (Payrolls, Income, Sales, Production) with green checkmarks.
  * Bottom callout reveals the true economic contraction definition.
* **1:09 – 1:20**: Cut to **AI Video Clip 2** (The 8 NBER Economists in moody dark boardroom from Flow) on **Track V2** for 10 seconds of cinematic documentary depth.
* **1:20 – 1:42**: Hold `NBERFrameworkScene.mp4` endframe on Track V1 highlighting the NBER standard.

---

### SCENE 3: THE 7-MONTH REFEREE LAG (1:42 – 2:47) | Voiceover: `scene03_referee_lag.mp3` (65s)
* **1:42 – 2:10**: Place `renders/manim/RefereeLagScene.mp4` (28.0s) on **Track V1**.
  * Timeline track runs from Month 0 (Recession Begins) to Month 10.4 (Average End).
  * At Month 7, red alarm strobe triggers: *"📢 NBER DECLARES RECESSION"*.
  * Highlights the psychological trap: **~70% of the recession is already in the rearview mirror**.
* **2:10 – 2:20**: Cut to **AI Video Clip 1 (Alt Angle)** or press conference flashbulbs on **Track V2**.
* **2:20 – 2:47**: Hold `RefereeLagScene.mp4` endframe on Track V1 showing the 1980 and 2020 lag data points.
* **Track A2 (SFX)**: Subtle clock ticking on Track A2, followed by a metallic chime when the Month 7 alarm pulses.

---

### SCENE 4: THE 50-YEAR AUTOPSY (2:47 – 4:26) | Voiceover: `scene04_autopsy.mp3` (99s)
* **2:47 – 3:05**: Place `renders/scene04_era1_1973_oil_shock.png` on **Track V1** with Ken Burns slow zoom (1973 Stagflation).
* **3:05 – 3:15**: Cut to **AI Video Clip 3** (1973 Vintage Gas Station "NO GAS TODAY" queue from Flow) on **Track V2**.
* **3:15 – 3:42**: Sequence `renders/scene04_era2_1981_volcker.png` (Volcker 20% rates) and `renders/scene04_era3_2001_dotcom.png` (Dot-com bubble).
* **3:42 – 3:58**: Place `renders/scene04_era4_2008_gfc.png` (2008 Lehman Brothers freeze).
* **3:58 – 4:08**: Cut to **AI Video Clip 4** (Wall Street banker walking out with cardboard box from Flow) on **Track V2**.
* **4:08 – 4:26**: Place `renders/scene04_era5_2020_covid.png` (2020 2-Month COVID freeze & recovery).

---

### SCENE 5: PATTERN #1 — THE LEAD-LAG PARADOX (4:26 – 5:39) | Voiceover: `scene05_lead_lag.mp3` (73s)
* **4:26 – 4:56**: Place `renders/manim/LeadLagParadoxScene.mp4` (30.0s) on **Track V1**.
  * S&P 500 curve plunges into the gray recession window.
  * Locks onto an emerald beacon at -4 months (*"MARKET BOTTOMS HERE — 3 to 5 Months Before Economy Ends!"*).
  * Surges violently upward while the recession window is still active.
  * Reveals the March 9, 2009 case study (+68% 12-month rally).
* **4:56 – 5:06**: Cut to **AI Video Clip 1 / 4** (Traders reacting to the unexpected green surge) on **Track V2**.
* **5:06 – 5:39**: Hold `LeadLagParadoxScene.mp4` on Track V1 focusing on the forward-looking market principle.

---

### SCENE 6: PATTERN #2 — THE ASYMMETRY OF TIME & JOBS (5:39 – 6:56) | Voiceover: `scene06_time_jobs.mp3` (77s)
* **5:39 – 6:09**: Place `renders/manim/TimeJobsAsymmetryScene.mp4` (30.0s) on **Track V1**.
  * Top: Duration comparison bars animate out: **10.4-Month Red Recession** vs **64-Month Emerald Expansion (5.3 Years / 6x Longer!)**.
  * Bottom: Unemployment Rate curve tracing: *"Elevator Down in weeks, Stairs Down over 3–5 years"*.
* **6:09 – 6:20**: Cut to **AI Video Clip 5** (Cavernous modern tech office with empty desks at twilight from Flow) on **Track V2** for poignant human impact.
* **6:20 – 6:56**: Hold `TimeJobsAsymmetryScene.mp4` on Track V1 showing the multi-year jobs recovery slope.

---

### SCENE 7: CONCLUSION & NEXT BREAKDOWN (6:56 – 8:07) | Voiceover: `scene07_outro.mp3` (71s)
* **6:56 – 7:21**: Place `renders/manim/MacroRulesSummaryScene.mp4` (25.0s) on **Track V1**.
  * 3 Immutable Macro Rules unlock sequentially with glowing borders and green checkmarks.
  * Teaser bridge appears for Episode 3 (AI Recommendation Algorithm).
* **7:21 – 7:35**: Cut to **AI Video Clip 6** (3D glowing recommendation vector highway from Flow) on **Track V2** as the visual climax bridge!
* **7:35 – 8:07**: Outro screen template with Subscribe button and Episode 1 / Episode 3 preview cards.
* **Track A3**: Background music swells from `-22dB` to `-14dB` for 4 seconds during the end screen, then fades out smoothly.

---

## 4. Master Assets Checklist

| Asset File | Type | Resolution | Location |
| :--- | :--- | :--- | :--- |
| `Hook50YrRecessionScene.mp4` | Manim Animation (25.0s) | 1080p 60fps | `02_assets_code/renders/manim/` |
| `NBERFrameworkScene.mp4` | Manim Animation (26.0s) | 1080p 60fps | `02_assets_code/renders/manim/` |
| `RefereeLagScene.mp4` | Manim Animation (28.0s) | 1080p 60fps | `02_assets_code/renders/manim/` |
| `LeadLagParadoxScene.mp4` | Manim Animation (30.0s) | 1080p 60fps | `02_assets_code/renders/manim/` |
| `TimeJobsAsymmetryScene.mp4` | Manim Animation (30.0s) | 1080p 60fps | `02_assets_code/renders/manim/` |
| `MacroRulesSummaryScene.mp4` | Manim Animation (25.0s) | 1080p 60fps | `02_assets_code/renders/manim/` |
| `full_voiceover_ep02.mp3` | Master Voiceover (8:07) | 192 kbps | `voiceover/generated_audio/` |
