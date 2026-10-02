# Episode 04 CapCut Final Video Assembly Guide (Consolidated Edition)
## "Why AI Fails to Predict the Stock Market (And How Quants Win)"

> **Production Standard**: All necessary media assets for Episode 04 are centralized directly in **`TIMELINE_MEDIA/`**. Zero scattered folders, zero missing clips. All patch visuals, fact-checked Manim animations, Gemini voiceover stems, master overlays, and thumbnails are ready for drag-and-drop timeline assembly.

---

## 1. Master Project Settings

* **Canvas Resolution**: `1920x1080` (16:9 Landscape)
* **Frame Rate**: `60 fps` (matches native 60fps Manim render rate for smooth motion)
* **Canvas Background Color**: Hex `#0B0F19` (Quantrove Obsidian Dark Luxury)
* **Master Voiceover Track (Track A1)**: 
  * **Recommended**: `TIMELINE_MEDIA/00_AUDIO_00m00s_to_07m05s_full_voiceover_ep04_master_v3_patched.wav` (Duration: **425.20s / 07:05.20** — pre-spliced with all 4 fact-checked audio patches)
  * **Alternative**: `TIMELINE_MEDIA/00_AUDIO_00m00s_to_07m05s_full_voiceover_ep04_master.wav` (Original unpatched 425.47s stem) + 4 patch segment WAV files
* **Master Kinetic Overlay (Track V2)**: `TIMELINE_MEDIA/00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps.mov` (Raw: 425.48s, 60fps RGBA transparent alpha channel — **trimmed at 425.20s / 07:05.20**)
* **Ambient Background Bed (Track A3)**: `TIMELINE_MEDIA/00_AUDIO_00m00s_to_07m05s_ambient_bed.wav` (Raw: 425.47s, lock @ `-18 dB` to `-22 dB` ducked under voice — **trimmed at 425.20s / 07:05.20**)
* **End Screen Safe Zone**: `TIMELINE_MEDIA/06_07m05s_to_07m25s_end_screen_tail.mp4` (20.0s clean background for YouTube end cards)
* **Total Video Runtime**: **07:25.20** (425.20s master content + 20.0s end-screen card safe zone)

---

## 2. Thumbnail Integration (For High CTR & YouTube Auto-Select)

All thumbnail assets have been gathered into `TIMELINE_MEDIA/`:

* **Concept A (Recommended)**: `ep04_thumbnail_concept_a_5075_edge.jpg` ("THE 50.75% EDGE" + Jim Simons +66% Gold Seal)
* **Concept B**: `ep04_thumbnail_concept_b_why_ai_fails.jpg` ("WHY AI FAILS" + Renaissance Medallion Hologram)
* **YouTube Cover**: `99_thumbnail_ep04_youtube_cover.jpg`
* **Frame-1 Embed**: `00_FRAME1_00m00s_thumbnail_cover_embed.jpg`

### Method A: The Frame-1 Video Inject (Guaranteed YouTube Auto-Select)
1. In CapCut, import `00_FRAME1_00m00s_thumbnail_cover_embed.jpg` from `TIMELINE_MEDIA/`.
2. Place this image at the **very start of the timeline (`00:00.00`) on Track V3 (directly above Track V1)**.
   * *Critical*: Do NOT place it on Track V1. Placing an image on Track V1 ripples and shifts all 23 base video clips by 3 frames, desynchronizing the entire timeline. On Track V3, it overlays the first 3 frames seamlessly without altering V1 timecodes or audio sync.
3. Set its duration to exactly **3 frames (approx. 0.05s at 60fps)** from `00:00.00` to `00:00.05`.
4. When uploaded to YouTube Studio, the 1st auto-generated thumbnail preview will be your custom 4K cover image.

### Method B: CapCut Cover Setting (Embedded MP4 Cover)
1. Click **"Cover"** on the left side of the CapCut timeline (or "Edit Cover" in Export window).
2. Choose **"Select from computer"** → Select `99_thumbnail_ep04_youtube_cover.jpg`.
3. Click **Save**.

---

## 3. Multi-Track Timeline Architecture

```text
[TRACK V4 - Polish & Grain]          : Adjustment Layer (Film Grain 6%, Vignette 18%)
[TRACK V3 - Auto-Captions / Badges]  : Frame-1 Cover Embed (t=0, 3 frames) + Optional CapCut Auto-Captions
[TRACK V2 - Kinetic Keyword Overlay] : 00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps.mov (Alpha Transparency)
                                       + Patch Overlays (01_OVERLAY_...intro, 02_OVERLAY_...mercer, 06_OVERLAY_...cta)
[TRACK V1 - Base Visuals (23 Clips)] : 14 Flow AI 4K Clips + 8 Manim Math Animations + 1 End-Screen Tail (Zero Gaps)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[TRACK A1 - Master Voiceover]        : 00_AUDIO_00m00s_to_07m05s_full_voiceover_ep04_master_v3_patched.wav (0.0dB)
[TRACK A2 - Sound Effects (SFX)]     : 28 Calibrated Cues (Sub-Drops, Clicks, Whooshes, Alarms, Radar Pings)
[TRACK A3 - Ambient Music Bed]       : 00_AUDIO_00m00s_to_07m05s_ambient_bed.wav (@ -20dB ducked, fade out @ 7:05)
```

---

## 4. Master Chronological Visual Assembly Timeline (Track V1)

All files listed below are located in `TIMELINE_MEDIA/`:

| # | Timecode Range | Span | File Name in `TIMELINE_MEDIA/` | Visual Type | Narration Anchor & Visual Directive |
| :---: | :---: | :---: | :--- | :---: | :--- |
| **01** | `00:00.00 – 00:12.00` | 12.0s | `00_00m00s_to_00m12s_Scene_01_hook_visual.mp4` | Manim Hook | *"Can AI actually predict the stock market?..."* — Continuous drawing price walk + On-screen hook text |
| **02** | `00:12.00 – 00:20.00` | 8.0s | `01_00m10s_to_00m20s_Scene_01_flow_terminal_numbers_cascade.mp4` | Flow AI | *"Get comfortable. This one is worth going slowly..."* — Cascading terminal numbers matrix |
| **03** | `00:20.00 – 00:35.00` | 15.0s | `01_00m20s_to_00m35s_Scene_01_manim_simons_21m_counter.mp4` | Manim Math | *"It starts in 1988... $1,000 into ~$21M by 2018..."* — Compounding curve + Medallion Fund net report |
| **04** | `00:35.00 – 00:45.00` | 10.0s | `01_00m35s_to_00m45s_Scene_01_spiva_warning.mp4` | Manim Card | *"Yet today, across the rest of Wall Street... 92.4% underperform"* — S&P SPIVA 15-Year institutional benchmark |
| **05** | `00:45.00 – 01:06.81` | 21.8s | `01_00m45s_to_01m06s_Scene_01_manim_hook_title_slam.mp4` | Manim Title | *"How did mathematicians crack the market... Let's look at the mathematics..."* — Split comparison + **Title Slam** |
| **06a** | `01:06.81 – 01:16.81` | 10.0s | `02_01m06s_to_01m16s_Scene_02_flow_secretive_math_office.mp4` | Flow AI | *"Here is the first great illusion about quantitative trading..."* — Dark math research office |
| **06b** | `01:16.81 – 01:26.81` | 10.0s | `02_01m16s_to_01m26s_Scene_02_flow_chalkboard_equations.mp4` | Flow AI | *"Renaissance co-CEO Robert Mercer reportedly said..."* — Macro chalkboard probability equations |
| **07** | `01:26.81 – 01:50.81` | 24.0s | `02_01m26s_to_01m50s_Scene_02_BellCurve5075_manim_v3_patched.mp4` | Manim Math | *"They were right roughly 50.75% of the time..."* — Gaussian bell curve, glowing gold 50.75% micro-edge |
| **08** | `01:50.81 – 02:00.81` | 10.0s | `02_01m50s_to_02m00s_Scene_02_flow_neural_network_nodes.mp4` | Flow AI | *"Why can't deep neural networks just learn the patterns?"* — 3D glowing volumetric neural lattice |
| **09** | `02:00.81 – 02:29.46` | 28.7s | `02_02m00s_to_02m29s_Scene_02_Reflexivity_manim.mp4` | Manim Math | *"George Soros called it Reflexivity. Predicting the price changes the price..."* — Cat image vs reflexive curve |
| **10** | `02:29.46 – 03:00.00` | 30.5s | `03_02m29s_to_03m00s_Scene_03_AlphaDecay_manim_v3_patched.mp4` | Manim Math | *"Pattern number one: Alpha Decay. The moment an algorithm discovers an anomaly..."* — Exponential decay curve |
| **11** | `03:00.00 – 03:10.01` | 10.0s | `03_03m00s_to_03m10s_Scene_03_flow_hft_server_rack.mp4` | Flow AI | *"Thousands of competing bots detect the same anomaly..."* — HFT server room with flickering LED blades |
| **12** | `03:10.01 – 03:21.55` | 11.5s | `03_03m10s_to_03m22s_Scene_03_manim_market_adaptation.mp4` | Manim Math | *"This is why an AI model that looks brilliant in a backtest stops making money..."* — 4-Month Decay Cycle |
| **13** | `03:21.55 – 03:50.00` | 28.5s | `04_03m21s_to_03m50s_Scene_04_OverfittingTrapPart1_manim_v3_patched.mp4` | Manim Math | *"Pattern number two: The Overfitting Trap. You give an LSTM 10 years of data..."* — Chaotic points + polynomial |
| **14** | `03:50.00 – 04:00.00` | 10.0s | `04_03m50s_to_04m00s_Scene_04_flow_code_overfitting_divergence.mp4` | Flow AI | *"It memorized historical noise. Most of any day's price movement is pure noise..."* — Machine learning code screen |
| **15** | `04:00.00 – 04:33.60` | 33.6s | `04_04m00s_to_04m33s_Scene_04_OverfittingTrapPart2_manim.mp4` | Manim Math | *"The moment you deploy live capital, the regime shifts..."* — Boundary crossing into catastrophic red crash |
| **16** | `04:33.60 – 04:43.60` | 10.0s | `05_04m33s_to_04m43s_Scene_05_flow_command_bridge_wide.mp4` | Flow AI | *"So if AI can't predict directional prices, why spend billions?"* — High-tech command center |
| **17** | `04:43.60 – 04:58.60` | 15.0s | `05_04m45s_to_04m55s_Scene_05_flow_monte_carlo_risk.mp4` | Flow AI | *"Engine 1: Extreme Risk Modeling and Stress Testing..."* — 3D Monte Carlo risk topography *(Set speed 0.67x / Optical Flow)* |
| **18** | `04:58.60 – 05:18.60` | 20.0s | `05_05m10s_to_05m20s_Scene_05_flow_fiber_optic_execution.mp4` | Flow AI | *"Engine 2: Microsecond Execution and Smart Order Routing..."* — Pulsing fiber optics *(Duplicate + Reverse ping-pong)* |
| **19** | `05:18.60 – 05:40.00` | 21.4s | `05_05m30s_to_05m40s_Scene_05_flow_fraud_anomaly_network.mp4` | Flow AI | *"Engine 3: Fraud, Manipulation and Anomaly Detection..."* — Red anomaly cluster isolation *(Duplicate + Reverse @ 0.93x)* |
| **20** | `05:40.00 – 06:07.53` | 27.5s | `05_05m40s_to_06m07s_Scene_05_manim_engine4_covariance.mp4` | Manim Math | *"Engine 4: Mathematical Portfolio Rebalancing... Optimization, not crystal balls"* — Covariance Matrix & Frontier |
| **21a** | `06:07.53 – 06:17.53` | 10.0s | `06_06m07s_to_06m17s_Scene_06_flow_penthouse_terminal_pullback.mp4` | Flow AI | *"The retail dream of a magic AI bot that predicts tomorrow is a myth..."* — Penthouse trading desk pullback |
| **21b** | `06:17.53 – 06:27.53` | 10.0s | `06_06m17s_to_06m27s_Scene_06_flow_studio_reveal.mp4` | Flow AI | *"Real quantitative advantage is built on risk discipline and microscopic edges..."* — Prestige dark studio reveal |
| **22** | `06:27.53 – 07:05.20` | 37.7s | `06_06m27s_to_07m05s_Scene_06_manim_outro_subscribe.mp4` | Manim Outro | *"If this changed how you see AI and markets, watch this next... subscribe to Quantrove."* — Disciplined CTA + Radar |
| **23** | `07:05.20 – 07:25.20` | 20.0s | `06_07m05s_to_07m25s_end_screen_tail.mp4` | End Screen | Clean end-screen visual hold for YouTube video/playlist/subscribe recommendation cards |

---

## 5. Audio & Kinetic Overlay Alignment

### Audio Options (Track A1)
* **Option 1 (Recommended — Single File)**:
  Import `00_AUDIO_00m00s_to_07m05s_full_voiceover_ep04_master_v3_patched.wav` and place it at `00:00.00`. It contains the complete narration with all 4 corrected sections seamlessly integrated. Lock Track A1.
* **Option 2 (Modular Stems)**:
  If you prefer scene-by-scene editing, use the 6 scene audio files (`01_AUDIO_...` through `06_AUDIO_...`) and swap the 4 patch clips:
  * `01_AUDIO_00m00s_to_00m35s_patch_segment_1_intro.wav` (0:00 → 0:34.85)
  * `02_AUDIO_01m18s_to_01m28s_patch_segment_2_mercer.wav` (1:17.80 → 1:27.63)
  * `04_AUDIO_03m50s_to_03m54s_patch_segment_3_noise.wav` (3:49.60 → 3:53.55)
  * `06_AUDIO_06m45s_to_07m05s_patch_segment_4_cta.wav` (6:45.02 → 7:05.00)

### Kinetic Overlay Alignment (Track V2)
1. Import `00_OVERLAY_00m00s_to_07m05s_kinetic_word_pops_60fps.mov` onto Track V2 aligned at `00:00.00`.
2. For the patched sections, drop the matching patch overlay MOVs on Track V2 (or Track V3 above it):
  * `01_OVERLAY_00m00s_to_00m35s_patch_segment_1_intro_60fps.mov` at `00:00.00`
  * `02_OVERLAY_01m18s_to_01m28s_patch_segment_2_mercer_60fps.mov` at `01:17.80`
  * `04_OVERLAY_03m50s_to_03m54s_patch_segment_3_noise_60fps.mov` at `03:49.60`
  * `06_OVERLAY_06m45s_to_07m05s_patch_segment_4_cta_60fps.mov` at `06:45.02`

### Tail Trimming & Master Sync (Playhead @ 07:05.20)
Before proceeding to audio mix and export, trim the overlay and ambient bed tracks to match the exact end of narration:
1. Position the timeline playhead at **`07:05.20`** (`425.20s`, the exact end of Voiceover Track A1).
2. Select Track V2 (`00_OVERLAY_...` raw length 425.48s) → Split (`Ctrl+B`) → Select and Delete the trailing 0.28s tail.
3. Select Track A3 (`00_AUDIO_..._ambient_bed.wav` raw length 425.47s) → Split (`Ctrl+B`) → Select and Delete the trailing 0.27s tail.
4. Apply a 2.0s audio fade-out to Track A3 ending exactly at `07:05.20` (see Section 8).

---

## 6. Pro Editing & Polish Checklist

1. **Flow Clip Span Filling & Speed Ramping (Scenes 17–19)**:
   * Each source Flow clip in Scene 5 is 10.0s (`10.005s` measured via ffprobe). Setting speed to 0.7x alone yields only ~14.3s, which fails to fill the required spans (15.0s, 20.0s, 21.4s) and causes freeze frames. Follow the exact clip-by-clip methods below:
     * **Scene 17 (Risk — 15.0s span, `04:43.60 – 04:58.60`, file `05_04m45s_to_04m55s_Scene_05_flow_monte_carlo_risk.mp4`)**:
       * Select clip on Track V1 → **Speed** tab → **Normal** → Set to **0.67x** (or 66.7%).
       * Toggle **Smooth slow-mo** → Select **Optical Flow**.
       * Extends the 10.0s source to exactly 15.0s with clean, artifact-free slow motion.
     * **Scene 18 (Execution — 20.0s span, `04:58.60 – 05:18.60`, file `05_05m10s_to_05m20s_Scene_05_flow_fiber_optic_execution.mp4`)**:
       * Select clip on Track V1 → Copy (`Ctrl+C`) and Paste (`Ctrl+V`) directly adjacent on Track V1.
       * Select instance 2 (`05:08.60 – 05:18.60`) → Click toolbar **Reverse** (`Ctrl+R`).
       * This creates a seamless 20.0s forward-reverse (ping-pong) pulsing fiber-optic loop at 100% native resolution with zero freeze frames and zero jump cuts.
     * **Scene 19 (Fraud — 21.4s span, `05:18.60 – 05:40.00`, file `05_05m30s_to_05m40s_Scene_05_flow_fraud_anomaly_network.mp4`)**:
       * Duplicate clip on Track V1 (`Ctrl+C` then `Ctrl+V` to create instance 1 and instance 2).
       * Select instance 2 → Click toolbar **Reverse** (`Ctrl+R`).
       * Select both instances (total 20.0s) → Right-click → **Create compound clip** (or adjust both clips).
       * Set **Speed → 0.93x** (93.5%), toggle **Smooth slow-mo** → **Optical Flow**.
       * Extends the 20.0s loop to 21.4s; snap/trim the tail cleanly at `05:40.00`.
2. **SFX Placement on Track A2**:
   * *Comprehensive Cue Sheet*: To provide professional institutional sound design, the SFX library has been expanded from 8 to 28 visual-anchored cues across the timeline. Refer to **Section 9: SFX CUE SHEET (Track A2)** for exact timecodes, narration anchor words from transcription, library search terms, and calibrated dB levels.
3. **End-Screen Cards in YouTube Studio**:
   * During upload, place the End Screen video card for **EP03 ("How the Algorithm Decides")** and the **Subscribe Button** at timestamp `07:05.20 → 07:25.20` over `06_07m05s_to_07m25s_end_screen_tail.mp4`.

---

## 7. TRANSITION MAP

All 24 edit boundaries between Track V1 visual clips are mapped below. Transitions are strictly centered on cuts and capped at <=0.4s (except the 1.0s fade into the end-screen tail) to ensure timeline synchronization remains frame-perfect without shifting audio alignment.

| Boundary | Timecode | From Scene -> To Scene | Transition Type | Duration | CapCut Search Term | Narrative & Visual Rationale |
| :---: | :---: | :--- | :---: | :---: | :--- | :--- |
| **01** | `00:12.00` | 01 (Manim Hook) -> 02 (Flow Terminal) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Soft cinematic shift from vector line chart to atmospheric terminal numbers matrix. |
| **02** | `00:20.00` | 02 (Flow Terminal) -> 03 (Manim Simons) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Blends ambient numbers into the Simons compounding curve as narration introduces "1988". |
| **03** | `00:35.00` | 03 (Manim Simons) -> 04 (Manim SPIVA) | Hard Cut | 0.0s | *None* (Clean Cut) | Instant tonal contrast from $21M Medallion compounding to the harsh reality of 92.4% failure. |
| **04** | `00:45.00` | 04 (Manim SPIVA) -> 05 (Manim Title Slam) | Hard Cut + Impact | 0.0s | *None* (Impact Cut) | Hard slam into title card accompanied by Heavy Slam SFX and micro camera shake. |
| **05** | `01:06.81` | 05 (Manim Title) -> 06a (Flow Office) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Smooth visual bridge exiting intro title into dark, secretive math research office. |
| **06** | `01:16.81` | 06a (Flow Office) -> 06b (Flow Chalkboard) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Continuity transition from wide office shot to macro chalkboard probability formulas. |
| **07** | `01:26.81` | 06b (Flow Chalkboard) -> 07 (Manim Bell Curve) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Transitions from physical chalkboard to precision digital Gaussian distribution curve. |
| **08** | `01:50.81` | 07 (Manim Bell Curve) -> 08 (Flow Neural Net) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Connects statistical probability concept into 3D volumetric neural network lattice. |
| **09** | `02:00.81` | 08 (Flow Neural Net) -> 09 (Manim Reflexivity) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Moves from abstract neural network to interactive Cat vs Market Reflexivity proof. |
| **10** | `02:29.46` | 09 (Manim Reflexivity) -> 10 (Manim Alpha Decay) | Hard Cut | 0.0s | *None* (Clean Cut) | Crisp chapter boundary cut into Pattern #1 (Alpha Decay) to keep vector math sharp. |
| **11** | `03:00.00` | 10 (Manim Alpha Decay) -> 11 (Flow HFT Server) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Bridges mathematical decay formula into real-world physical high-frequency trading server room. |
| **12** | `03:10.01` | 11 (Flow HFT Server) -> 12 (Manim Adaptation) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Glides from flickering server LEDs into the 4-month market adaptation timeline graph. |
| **13** | `03:21.55` | 12 (Manim Adaptation) -> 13 (Manim Overfitting) | Cross Dissolve | 0.2s | Transitions > Basic > "Dissolve" | Tight 0.2s dissolve separates Pattern 1 conclusion from Pattern 2 polynomial graph. |
| **14** | `03:50.00` | 13 (Manim Overfitting) -> 14 (Flow Code Screen) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Blends polynomial curve into machine learning training code as narration mentions "pure noise". |
| **15** | `04:00.00` | 14 (Flow Code Screen) -> 15 (Manim Crash) | Hard Cut + Crash | 0.0s | *None* (Impact Cut) | Violent cut into catastrophic red crash line accompanied by System Error Alert SFX. |
| **16** | `04:33.60` | 15 (Manim Crash) -> 16 (Flow Command Bridge) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Dissolves from crash graph to institutional command bridge as narrator asks "why spend billions?". |
| **17** | `04:43.60` | 16 (Flow Bridge) -> 17 (Flow Monte Carlo) | Hard Cut | 0.0s | *None* (Clean Cut) | Dynamic direct cut into Engine 1 (3D Monte Carlo risk topography) on narration beat. |
| **18** | `04:58.60` | 17 (Flow Monte Carlo) -> 18 (Flow Fiber Optic) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Smooth flow between risk topography and microsecond fiber-optic network. |
| **19** | `05:18.60` | 18 (Flow Fiber Optic) -> 19 (Flow Fraud Anomaly) | Hard Cut | 0.0s | *None* (Clean Cut) | Clean cut into Engine 3 (red anomaly cluster) prevents repetitive dissolves across Flow scenes. |
| **20** | `05:40.00` | 19 (Flow Fraud Anomaly) -> 20 (Manim Covariance) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Glides from anomaly graph into precision Markowitz efficient frontier & covariance matrix. |
| **21** | `06:07.53` | 20 (Manim Covariance) -> 21a (Flow Penthouse) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Dissolves out of data formulas into reflective cinematic penthouse desk for final thesis. |
| **22** | `06:17.53` | 21a (Flow Penthouse) -> 21b (Flow Studio) | Cross Dissolve | 0.3s | Transitions > Basic > "Dissolve" | Seamless continuity progression to dark prestige studio as narration delivers "microscopic edges". |
| **23** | `06:27.53` | 21b (Flow Studio) -> 22 (Manim Outro) | Hard Cut + Impact | 0.0s | *None* (Impact Cut) | Hard slam into outro sequence accompanied by sub-impact SFX and radar scan initiation. |
| **24** | `07:05.20` | 22 (Manim Outro) -> 23 (End Screen Tail) | Fade to Black | 1.0s | Transitions > Basic > "Fade to Black" | Elegant 1.0s dip to black transitioning into clean 20.0s canvas for YouTube recommendation cards. |

---

## 8. FADES & MOTION

### 8.1 Video Fades
1. **Head Fade-In (00:00.00 – 00:00.30)**:
   * Track V3 holds the Frame-1 cover embed image for 3 frames (`00:00.00 – 00:00.05`) at 100% opacity.
   * Underneath on Track V1, apply a **0.3s Fade In** from black on Scene 01 (`00_00m00s_to_00m12s_Scene_01_hook_visual.mp4`).
   * CapCut steps: Select Scene 01 on Track V1 → Inspector **Video** tab → **Basic** → Opacity: Keyframe at `00:00.05` (`0%`) to `00:00.35` (`100%`) (or **Transitions** > "Fade In" set to 0.3s).
2. **Tail Fade-Out (07:05.20 & 07:25.20)**:
   * Boundary between Scene 22 and 23 at `07:05.20`: Apply **1.0s Fade to Black** (Transitions > Basic > "Fade to Black").
   * End of Scene 23 at `07:25.20`: Apply a **0.5s Fade to Black** on the final tail clip to exit into YouTube black canvas.

### 8.2 Audio Fades
1. **Track A1 (Master Voiceover)**: **Untouched**. Keep 0.0 dB unity gain with zero fade-in or fade-out.
2. **Track A3 (Ambient Bed)**:
   * **Fade-In**: Set a **1.0s Fade-In** from silence starting at `00:00.00`.
   * **Fade-Out**: Set a **2.0s Fade-Out** ending exactly at `07:05.20` (`423.20s → 425.20s`).
   * CapCut steps: Select Track A3 clip → Inspector **Audio** tab → Set **Fade In** to `1.0s` and **Fade Out** to `2.0s`.

### 8.3 Ken Burns Motion on Flow Clips (100% -> 106%)
Apply slow, majestic push-ins to all Flow AI atmospheric clips to eliminate static frames while keeping movement restrained and premium.
* **Step-by-Step Instructions**:
  1. Select a Flow clip on Track V1 (e.g., Scene 02, 06a, 06b, 08, 11, 14, 16, 17, 18, 19, 21a, 21b).
  2. In the top-right Inspector, select **Video** tab → **Basic**.
  3. Move timeline playhead to the very first frame of the clip.
  4. Beside **Scale**, click the diamond icon to **Add Keyframe** (confirm value is `100.0%`).
  5. Move playhead to the very last frame of the clip.
  6. Change **Scale** value to `106.0%` (CapCut automatically generates the ending keyframe).
  7. Confirm **Position X: 0**, **Position Y: 0** to keep the zoom centered.
* **CRITICAL RULE — NO ZOOM ON MANIM CLIPS**:
  * Never apply Scale keyframes, zoom, or camera push to Manim animation clips (Scenes 01, 03, 04, 05, 07, 09, 10, 12, 13, 15, 20, 22). Manim renders are vector-rendered at native 1080p; scaling degrades line weight consistency and glyph sharpness.

### 8.4 Micro Camera Shake on Impact Moments
Apply subtle high-frequency camera shakes strictly to the 3 major narrative punchlines:
1. **Title Slam (`00:45.00`)**: Length 15 frames (`0.25s`).
2. **Overfitting Crash (`04:00.00`)**: Length 18 frames (`0.30s`).
3. **Outro Slam (`06:27.53`)**: Length 12 frames (`0.20s`).
* CapCut steps: Go to **Effects** → **Video Effects** → Search `"Camera Shake"` (or `"Shake"`). Drag effect onto Track V4 directly above the cut. Set **Speed: 10**, **Intensity: 10** (micro-jolt; never use disorienting high values).

---

## 9. SFX CUE SHEET (Track A2)

All 28 sound effects are anchored strictly to visual events and verified against transcription word timestamps (`00_TIMING_all_words_v3_patched_transcription.json`). SFX are never placed over key spoken numbers (such as "50.75" or "$21 million") to preserve narration intelligibility.

> *CapCut Tip*: In **Audio** → **Sound Effects**, check the **"Commercial use"** filter toggle where available to guarantee monetization safety.

| # | Timecode | Anchor Word (JSON) | Sound Design Event | CapCut Search Term | Level (dB) | Editing Notes & Rationale |
| :---: | :---: | :--- | :--- | :--- | :---: | :--- |
| **01** | `00:00.00` | *"Can AI"* (0.00s) | Deep Sub-Bass Drop / Impact | Audio > "Sub Bass Drop" / "Deep Impact" | `-10 dB` | Opening hook slam; establishes cinematic weight immediately. |
| **02** | `00:06.60` | *"honest"* (6.60s) | Muted Tech Transition Swoosh | Audio > "Tech Whoosh" / "Swoosh" | `-18 dB` | Price walk chart inflection point; accents the reality pivot. |
| **03** | `00:20.00` | *"1988"* (19.22s) | High-Tech Ticker / Counter Click | Audio > "Digital Counter" / "Click" | `-16 dB` | Simons compounding counter starts rolling upward. |
| **04** | `00:27.50` | *"compounding"* (26.80s) | High-Frequency Data Shimmer | Audio > "Data Stream" / "Digital Shimmer" | `-20 dB` | Compounding curve accelerates past the $1M milestone. |
| **05** | `00:35.00` | *"rest"* (33.80s) | Low Warning Horn / Sub Alert | Audio > "Sub Alert" / "Low Horn" | `-14 dB` | SPIVA benchmark card reveals 92.4% failure rate. |
| **06** | `00:45.00` | *"fail"* (46.16s / cut 45s) | Title Card Impact Slam | Audio > "Heavy Slam" / "Cinematic Hit" | `-8 dB` | Title card slam; synchronizes with micro-shake and title text. |
| **07** | `01:06.81` | *"Here"* (66.81s) | Atmospheric Sub Swell | Audio > "Ambient Rise" / "Sub Drone" | `-18 dB` | Dissolve into secretive math research office. |
| **08** | `01:26.81` | *"right"* (83.58s / cut 86s) | Smooth Digital Servo Whoosh | Audio > "Servo Whoosh" / "Digital Swoosh"| `-16 dB` | Gaussian bell curve draws on screen; leads into 50.75% reveal. |
| **09** | `01:36.50` | *"fortune"* (89.00s / 96s) | Gold Coin Ping / Micro Tone | Audio > "Ding" / "Bell Ping" | `-20 dB` | Golden 50.75% micro-edge highlight illuminates. |
| **10** | `01:50.81` | *"Why"* (110.81s) | Digital Grid Initialization | Audio > "Tech Activation" / "Cyber Hum" | `-18 dB` | Neural network volumetric 3D grid energizes. |
| **11** | `02:00.81` | *"cat"* (120.94s) | Soft Interface UI Click | Audio > "UI Click" / "Futuristic Beep" | `-20 dB` | Cat image vs price chart boundary comparison card. |
| **12** | `02:18.00` | *"signal"* (139.06s) | Upward Pitch Swell | Audio > "Pitch Riser" / "Micro Sweep" | `-19 dB` | Buying pressure drives price upward on reflexive chart. |
| **13** | `02:29.46` | *"quantitative"* (149.94s)| Low Filter Sweep / Drop | Audio > "Filter Sweep" / "Downer" | `-18 dB` | Alpha decay curve initialization; pattern self-destructs. |
| **14** | `02:44.00` | *"decay"* (155.18s) | Downward Exponential Whine | Audio > "Tone Fall" / "Decay Tone" | `-21 dB` | Alpha decay curve slopes downwards toward zero. |
| **15** | `03:00.00` | *"competing"* (180.00s) | Fast Servo Pass / Flyby | Audio > "Fast Whoosh" / "Flyby" | `-17 dB` | Cut to HFT server blades flickering in server room. |
| **16** | `03:10.01` | *"adaptation"* (190.01s) | Metallic Mechanism Latch | Audio > "Mechanical Click" / "Latch" | `-18 dB` | 4-month market adaptation timeline locks in. |
| **17** | `03:21.55` | *"overfitting"* (210.82s)| Low Digital Tone / Dark Drone | Audio > "Dark Synth Drone" / "Sub Pulse" | `-19 dB` | Scene 13: Overfitting chaotic data points appear. |
| **18** | `03:38.00` | *"data"* (218.00s) | Rapid Ticker Scribble | Audio > "Data Ticker" / "Pen Draw" | `-22 dB` | High-degree polynomial curve snakes wildly through points. |
| **19** | `03:50.00` | *"noise"* (232.66s) | Brief Static Glitch Flutter | Audio > "Radio Static" / "Glitch Hit" | `-22 dB` | 0.1s static flutter into machine learning code screen. |
| **20** | `04:00.00` | *"parameters"* (239.06s)| System Error Alert + Impact | Audio > "System Glitch" / "Alarm Alert" | `-12 dB` | Overfitting crash: line crosses boundary into red plunge. |
| **21** | `04:33.60` | *"Instead"* (288.68s) | Heavy Sub Drone / Pulse | Audio > "Sub Pulse" / "Cinematic Drone" | `-16 dB` | Command Bridge wide reveal; transition to institutional reality. |
| **22** | `04:53.26` | *"First"* (293.26s) | High-Tech Glass Panel Click | Audio > "Tech Click" / "Glass Tap" | `-18 dB` | Highlight Engine 1: Extreme Risk Modeling topography. |
| **23** | `05:11.40` | *"Second"* (311.40s) | Digital Switch Toggle | Audio > "UI Toggle" / "Switch Click" | `-18 dB` | Highlight Engine 2: Microsecond Execution & Slippage. |
| **24** | `05:32.68` | *"Third"* (332.68s) | Cyber Ping / Chirp | Audio > "Digital Chirp" / "Sonar Blip" | `-18 dB` | Highlight Engine 3: Fraud & Anomaly Detection. |
| **25** | `05:46.36` | *"fourth"* (346.36s) | Mechanical Relay Snick | Audio > "Relay Click" / "Modern Snap" | `-18 dB` | Highlight Engine 4: Mathematical Portfolio Rebalancing. |
| **26** | `06:07.53` | *"myth"* (367.53s) | Warm Ambient Air Whoosh | Audio > "Soft Whoosh" / "Air Release" | `-18 dB` | Shift to final perspective at penthouse trading desk. |
| **27** | `06:27.53` | *"Quantrove"* (387.53s)| Outro Transition Sub Impact | Audio > "Sub Impact" / "Clean Hit" | `-12 dB` | Hard cut into outro sequence with radar scan line. |
| **28** | `07:03.04` | *"subscribe"* (423.04s)| Resonant Radar Ping / Bell | Audio > "Radar Ping" / "Crystal Chime" | `-15 dB` | Precise chime on narration "subscribe to Quantrove". |

---

## 10. AUDIO MIX & MASTERING

### 10.1 Track Level Hierarchy
To achieve institutional broadcast clarity, maintain strict decibel separation between dialogue, ambient bed, and Foley effects:

1. **Track A1 (Master Voiceover)**:
   * **Reference Level**: `0.0 dB` (Unity Gain).
   * Voiceover master is pre-normalized to `-14.0 LUFS` with a `-1.0 dB` true peak ceiling.
2. **Track A2 (Sound Effects / SFX)**:
   * **Target Level**: `-12 dB` to `-22 dB` per clip (see Section 9 cue sheet).
   * Sub-bass impacts peak at `-10 dB` to `-12 dB`; delicate UI clicks and ticks sit at `-18 dB` to `-22 dB`.
3. **Track A3 (Ambient Music Bed)**:
   * **Target Level**: `-20 dB` (Range: `-18 dB` to `-22 dB`).
   * Music must sit completely underneath dialogue to maintain 100% vocal intelligibility.

### 10.2 Ducking Setup in CapCut
* **Method 1 (Automatic Ducking — Recommended)**:
  1. Select the Ambient Bed audio clip on Track A3 (`00_AUDIO_..._ambient_bed.wav`).
  2. In the right-hand Inspector, navigate to the **Audio** tab → **Basic**.
  3. Check the box for **"Ducking"** (or **"Auto-Ducking"**).
  4. Set the Ducking slider to **`-20 dB`** (or 60-70% reduction).
  5. Set **Fade Length** to **`0.5s`** for smooth gain transitions during speech pauses.
* **Method 2 (Manual Gain Ceiling)**:
  * If auto-ducking is not supported in your CapCut version, select Track A3 → Inspector **Audio** → Set **Volume** slider directly to **`-20.0 dB`**.

### 10.3 Final Loudness Validation (FFmpeg)
After exporting the final assembled master (`ep04_master_final.mp4`), execute this command in terminal to verify YouTube broadcast compliance:

```bash
ffmpeg -i ep04_master_final.mp4 -af loudnorm=I=-14:TP=-1:LRA=11:print_format=summary -f null -
```

* **Pass Criteria Checklist**:
  * **Input Integrated (`I`)**: Target `-14.0 LUFS` (Tolerance: `±1.5 LUFS`, i.e., `-12.5` to `-15.5 LUFS`).
  * **Input True Peak (`TP`)**: Must be `<= -1.0 dB` (guarantees zero inter-sample clipping on YouTube transcoding).
  * **Input LRA (Loudness Range)**: `~9.0 – 12.0 LU` (indicates healthy dynamic contrast between dialogue and impacts).

---

## 11. VISUAL POLISH (SUBTLE INSTITUTIONAL LAYERS)

Quantrove's visual identity is "dark luxury data intelligence." Visual polish layers must remain restrained and functional. Never add flashy TikTok transitions, chromatic aberration, or heavy vignette.

### 11.1 Light Film Grain (Track V4 Adjustment Layer)
Adds tactile cinema texture and prevents digital banding on dark gradient backgrounds.
1. Click **Effects** in top navigation → **Video Effects** → Search `"Film Grain"`.
2. Drag the Film Grain effect onto **Track V4** (above Track V3), spanning from `00:00.00` to `07:05.20`.
3. In top-right Inspector, configure:
   * **Intensity**: `6%` (Strict tolerance: `5% – 8%`).
   * **Size / Speed**: `10%` (fine grain; non-distracting).

### 11.2 Soft Vignette (Framing Polish)
Draws viewer eye toward central data visualizations.
1. In **Video Effects**, search `"Vignette"`.
2. Drag onto Track V4 or apply directly to Flow clips.
3. In Inspector, configure:
   * **Intensity**: `18%` (subtle edge burn).
   * **Feather / Range**: `80%` (wide, soft radial gradient).

### 11.3 Subtle Glow on Flow AI Clips (Optional)
To accentuate glowing neon server LEDs and terminal monitors on Flow clips:
1. Select individual Flow clips on Track V1 (e.g., Scenes 02, 06b, 08, 11, 18).
2. Go to **Video Effects** → Search `"Soft Glow"` (or `"Luminescence"`).
3. Set **Glow Intensity: 10%**, **Range: 20%**.

> ⚠️ **HARD RULE — ZERO POLISH ON MANIM CLIPS**:
> NEVER apply Film Grain, Vignette, Glow, or Sharpen effects directly to Manim math animation clips (Scenes 01, 03, 04, 05, 07, 09, 10, 12, 13, 15, 20, 22). Manim scenes rely on mathematically exact `#0B0F19` obsidian background levels and native 7:1 text contrast. Altering them causes color halos and glyph blurring.

---

## 12. EXPORT & YOUTUBE PUBLISHING CHECKLIST

### 12.1 CapCut Master Export Settings
Click **Export** in the top-right corner of CapCut and configure the following broadcast parameters:

* **Export Name**: `Quantrove_EP04_Why_AI_Fails_Stock_Market_Master_1080p60`
* **Export To**: Select your local output drive / `TIMELINE_MEDIA/`
* **Resolution**: `1080P (1920x1080)`
* **Codec**: `H.264`
* **Format**: `MP4`
* **Frame Rate**: `60 fps` (Essential: matches 60fps Manim renders)
* **Bitrate**: `Higher` (or Custom: `25,000 – 30,000 kbps`, VBR 2-pass if available)
* **Audio Format**: `AAC`
* **Audio Bitrate**: `320 kbps` (Sample Rate: `48,000 Hz`)

### 12.2 Three-Checkpoint Quality Assurance Spot Check
Before uploading to YouTube, play back the exported MP4 at three critical timeline checkpoints:
1. **Checkpoint 1 (~00:45 – 01:00)**:
   * Confirm Frame-1 cover at `00:00.00` flashes for exactly 3 frames without stutter.
   * Confirm Title Slam at `00:45.00` aligns precisely with the Heavy Slam SFX and micro camera shake.
   * Confirm kinetic word pops on Track V2 render with clean alpha transparency (zero black bounding boxes).
2. **Checkpoint 2 (~02:25 – 02:40)**:
   * Verify Gaussian Bell Curve at `01:26.81` and 50.75% text display cleanly.
   * Verify hard cut transition into Alpha Decay at `02:29.46` with downward filter sweep SFX.
   * Confirm zero audio drift between voiceover narration and kinetic keyword pop-ups.
3. **Checkpoint 3 (~05:30 – 06:00)**:
   * Verify Scene 5 Flow clips (Risk, Execution, Fraud) play smoothly with no freeze frames or abrupt cuts.
   * Verify smooth cross dissolve into Scene 20 Markowitz Covariance matrix at `05:40.00`.
   * Verify audio ducking keeps ambient bed transparently below dialogue.

### 12.3 YouTube Studio Publishing Package

1. **Video File**: Upload `Quantrove_EP04_Why_AI_Fails_Stock_Market_Master_1080p60.mp4`.
2. **Custom Thumbnail**:
   * If Frame-1 auto-selected thumbnail is active: Verify crisp display in preview.
   * Or upload manual cover: `TIMELINE_MEDIA/ep04_thumbnail_concept_a_5075_edge.jpg` (or `99_thumbnail_ep04_youtube_cover.jpg`).
3. **Subtitles / Closed Captions (.SRT)**:
   * In YouTube Studio → **Subtitles** → **Add** → **Upload file** → **With timing**.
   * Upload: **`TIMELINE_MEDIA/ep04_captions.srt`** (163 calibrated subtitle blocks derived from faster-whisper word transcription).
4. **End Screen Setup (07:05.20 – 07:25.20)**:
   * Add **Video Element**: Select **EP03 ("How the Algorithm Decides")**.
   * Add **Subscribe Element**: Select **@Quantrove**.
   * Snap both elements from `07:05.20` to `07:25.20` over `06_07m05s_to_07m25s_end_screen_tail.mp4`.
5. **YouTube Description Chapters (Copy-Paste Block)**:
   * Paste the following calibrated chapter block into the YouTube video description:

```text
00:00 - The Simons Paradox & The $21M Edge
01:07 - The 50.75% Edge & The Reflexivity Trap
02:29 - Pattern #1: The Alpha Decay Curve
03:21 - Pattern #2: The Overfitting Illusion
04:33 - The 4 Engines: Where AI Actually Wins
06:07 - The Quantitative Verdict
07:05 - Next Video: Inside YouTube's Recommendation Algorithm
```
