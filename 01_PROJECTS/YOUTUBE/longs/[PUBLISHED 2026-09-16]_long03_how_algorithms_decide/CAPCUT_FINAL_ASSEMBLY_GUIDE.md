# EP03 CapCut Video Assembly Guide (Manim & AI Video Pipeline)
## "How Does The Algorithm Actually Decide What You See?"

> **Production Standard**: Exactly like Episode 2 (`ASSEMBLY_GUIDE_CAPCUT.md`), all data animations are **1080p 60fps Manim MP4 animations** located in `TIMELINE_MEDIA/` (and `02_assets_code/ALL_MEDIA_TIMELINE/`), layered alongside **Google Flow 4K AI video clips**, high-CTR thumbnail embed, and a pre-rendered **60fps transparent kinetic keyword overlay track**.

---

## 1. Master Project Settings
* **Aspect Ratio**: `16:9` (1920x1080 or 3840x2160)
* **Frame Rate**: `60 fps` (matches Manim native 60fps render rate for buttery smooth motion graphics)
* **Canvas Background Color**: Hex `#0B0E14` (Quantrove Deep Slate)
* **Master Voiceover Track**: `TIMELINE_MEDIA/00_AUDIO_00m00s_to_05m19s_full_voiceover_ep03_orus.mp3` (Duration: **05:18.60 / 318.600s**)
* **Master Kinetic Keyword Overlay**: `TIMELINE_MEDIA/00_OVERLAY_00m00s_to_05m19s_kinetic_word_pops_60fps.mov` (Duration: **05:18.60 / 318.600s**, Native RGBA Alpha Channel)

---

## 2. Thumbnail Integration (For High CTR & Guaranteed YouTube Auto-Select)

Because YouTube generates 3 automatic video preview frames during upload, use **this proven built-in CapCut technique** so YouTube automatically selects your custom high-CTR thumbnail:

### Method A: The Frame-1 Video Inject (Guaranteed YouTube Auto-Select)
1. In CapCut, import `00_FRAME1_00m00s_thumbnail_cover_embed.jpg` from `TIMELINE_MEDIA/`.
2. Place this image at the **very start of the timeline (`00:00.00`) on Track V1**.
3. Set its duration to **2–4 frames (approx. 0.05 to 0.1 seconds)** before Scene 1 begins.
4. When you upload the video to YouTube, YouTube generates 3 thumbnail previews from your video. The **1st preview frame will be this exact high-CTR thumbnail image**! Select it with one click during upload.

### Method B: CapCut Cover Setting (Embedded MP4 Cover)
1. On the left side of the CapCut timeline, click **"Cover"** (or click **"Edit Cover"** in the Export window).
2. Choose **"Select from computer"** and pick `99_thumbnail_ep03_youtube_cover.jpg` (or `00_FRAME1_00m00s_thumbnail_cover_embed.jpg`).
3. Click **Save**. This bakes the thumbnail metadata directly into the exported MP4 file.

---

## 3. Multi-Track Timeline Architecture

```
[TRACK V3 - Regular Captions / Badges] : (Optional) Small bottom-aligned auto-captions at Y: -720
[TRACK V2 - Kinetic Keyword Overlay]  : 00_OVERLAY_00m00s_to_05m19s_kinetic_word_pops_60fps.mov (Alpha Transparency)
[TRACK V1 - Base Visuals (Manim/Flow)]: 20 Sequenced Video Clips (Manim 60fps Math + Flow 4K AI Videos)
──────────────────────────────────────────────────────────────────────────────────────────────────────────
[TRACK A1 - Master Voiceover Audio]   : 00_AUDIO_00m00s_to_05m19s_full_voiceover_ep03_orus.mp3 (Lock @ 0.0dB)
[TRACK A2 - Sound Effects (SFX)]      : Sub-Bass Drops, Matrix Scans, Clock Ticks, Reward Pings, UI Pops
[TRACK A3 - Music Bed]                : Cyberpunk / Cerebral Ambient Synthwave (@ -24dB, swells to -14dB at outro)
```

---

## 4. Second-by-Second Assembly Timeline

### SCENE 1: THE 500-HOUR PROBLEM (THE HOOK) (0:00 – 0:42) | Voiceover: `01_AUDIO_00m00s_to_00m42s_Scene_01_hook_voiceover.mp3` (42.04s)

* **0:00 – 0:10**: Place `01_00m00s_to_00m10s_Scene_01_flow_infinite_feed_vortex.mp4` (10.0s) on **Track V1**.
  * Visual: Colossal swirling camera push into an infinite vortex of glowing social feeds.
  * Voiceover Anchor: *"There is a system you interact with more times per day than you talk to any single human being in your life."*
  * Kinetic Keyword Pops: `THE SYSTEM` (0:01), `EVERY SINGLE DAY` (0:06).
* **0:10 – 0:18**: Cut to `01_00m10s_to_00m18s_Scene_01_flow_billions_scrolling_darkness.mp4` (8.0s) on **Track V1**.
  * Visual: Moody cinematic tracking shot through a dark subway car with commuters illuminated solely by cold phone screens.
  * Voiceover Anchor: *"It was never built to inform you. It was built to do exactly one thing: Keep you watching..."*
  * Kinetic Keyword Pops: `NEVER BUILT TO INFORM YOU` (0:10), `KEEP YOU WATCHING` (0:15).
* **0:18 – 0:36**: Place `01_00m18s_to_00m36s_Scene_01_ScaleOfUploads_manim.mp4` (18.0s) on **Track V1**.
  * Visual: 1080p 60fps Manim mathematical animation. Dual stat panels stack up to 500 hrs/min uploaded, 700k human lifetime hours, and the 50ms decision window.
  * Voiceover Anchor: *"500 hours uploaded every minute... 700k human lifetime hours... 50ms decision."*
  * Kinetic Keyword Pops: `500 HOURS / MINUTE` (0:20), `700,000 HOURS` (0:26), `50 MILLISECONDS` (0:32).
* **0:36 – 0:42**: Cut to `01_00m36s_to_00m42s_Scene_01_flow_glass_touchpoint.mp4` (6.04s) on **Track V1**.
  * Visual: Macro shot of a finger hovering over a glowing neural glass surface.
  * Voiceover Anchor: *"And once you understand the real mechanism, how does it change the way you use every platform you are on?"*
  * Kinetic Keyword Pops: `THE REAL MECHANISM` (0:38).
* **Track A2 (SFX)**:
  * `00:00.00`: Deep Sub-Bass Drop / Cinematic Boom (`-8 dB`).
  * `00:18.00`: Digital Counter Click / High-tech Ticker (`-16 dB`).

---

### SCENE 2: THE POPULARITY MYTH (0:42 – 1:22) | Voiceover: `02_AUDIO_00m42s_to_01m22s_Scene_02_the_myth_voiceover.mp3` (40.28s)

* **0:42 – 0:57**: Place `02_00m42s_to_00m57s_Scene_02_TwoTowerVectorSpace_manim.mp4` (14.70s) on **Track V1**.
  * Visual: 1080p 60fps Manim animation. Two-Tower neural network (User Tower vs Item Tower) projecting embeddings into 128D vector space with dot-product cosine similarity calculation.
  * Voiceover Anchor: *"Ask most people how recommendations work, and they will tell you it is about what is popular..."*
  * Kinetic Keyword Pops: `THE POPULARITY MYTH` (0:43), `128-DIMENSIONAL VECTOR` (0:49), `DOT PRODUCT SIMILARITY` (0:54).
* **0:57 – 1:05**: Hold final Two-Tower Vector Space frame on **Track V1** (8.50s hold).
  * Visual: Static visual hold on the completed 128D geometric vector space diagram.
  * Voiceover Anchor: *"If it were true, everyone logged in at the same moment would see the same recommended videos. They do not."*
  * Kinetic Keyword Pops: `THEY DO NOT` (0:58), `ZERO POPULARITY RANKING` (1:02).
* **1:05 – 1:13**: Cut to `02_01m05s_to_01m13s_Scene_02_flow_two_viewers_different_feeds.mp4` (8.0s) on **Track V1**.
  * Visual: Split-screen Flow AI video showing two users side-by-side receiving radically different feeds in real time.
  * Voiceover Anchor: *"Two people can open the same platform at the same second and see almost completely different feeds built from completely different signals."*
  * Kinetic Keyword Pops: `SAME SECOND` (1:06), `COMPLETELY DIFFERENT FEEDS` (1:09).
* **1:13 – 1:22**: Hold Prediction System takeaway card on **Track V1** (9.08s hold).
  * Visual: Visual hold highlighting the core takeaway card.
  * Voiceover Anchor: *"This is not a popularity contest. It is a prediction system built individually for you specifically."*
  * Kinetic Keyword Pops: `NOT A POPULARITY CONTEST` (1:14), `BUILT SPECIFICALLY FOR YOU` (1:18).
* **Track A2 (SFX)**:
  * `00:42.04`: Low Ambient Servo / Whoosh (`-14 dB`).
  * `01:05.24`: Screen Split Digital Glitch / Swipe (`-16 dB`).

---

### SCENE 3: THE TWO-STAGE NEURAL ARCHITECTURE (1:22 – 2:03) | Voiceover: `03_AUDIO_01m22s_to_02m03s_Scene_03_two_stage_system_voiceover.mp3` (40.40s)

* **1:22 – 1:34**: Place `03_01m22s_to_01m34s_Scene_03_ThreeStageFunnel_manim.mp4` (11.70s) on **Track V1**.
  * Visual: 1080p 60fps Manim funnel: Millions of candidates $\to$ ScaNN retrieval (Hundreds) $\to$ Deep Ranking (Top 10).
  * Voiceover Anchor: *"Publicly documented research from YouTube and TikTok reveals a multi-stage funnel..."*
  * Kinetic Keyword Pops: `TWO-STAGE NEURAL FUNNEL` (1:23), `CANDIDATE GENERATION` (1:27), `DEEP RANKING` (1:31).
* **1:34 – 1:47**: Cut to `03_01m34s_to_01m47s_Scene_03_flow_holographic_sorting_prism.mp4` (13.46s) on **Track V1**.
  * Visual: Flow AI Video: Holographic 3D sorting prism filtering massive streams of data packets.
  * *Assembly Note: Clip is 10.0s; set speed to 0.75x (optical flow) or hold last frame for 3.46s until 01:47.48.*
  * Voiceover Anchor: *"Out of literally millions of available videos, a first system narrows the field down to a few hundred using your watch history..."*
  * Kinetic Keyword Pops: `MILLIONS DOWN TO HUNDREDS` (1:36), `VECTOR EMBEDDING LOOKUP` (1:42).
* **1:47 – 2:03**: Place `03_01m47s_to_02m03s_Scene_03_NeuralScoringMatrix_manim.mp4` (15.24s) on **Track V1**.
  * Visual: 1080p 60fps Manim heatmap: Candidate neural scoring matrix with cool-to-warm score bars and Rank #1 badge selection.
  * *Assembly Note: Animation runs 10.40s; hold final selected rank card for 4.84s until 02:02.72.*
  * Voiceover Anchor: *"Stage 2. Ranking. A second system takes that short list and scores every single one... not by how good the video objectively is, but by how likely it is to keep you watching."*
  * Kinetic Keyword Pops: `NEURAL SCORING MATRIX` (1:48), `RANK #1 SELECTION` (1:54), `KEEP YOU WATCHING` (1:59).
* **Track A2 (SFX)**:
  * `01:22.32`: UI Digital Thud / Funnel Cascade (`-15 dB`).
  * `01:47.48`: High-Tech Matrix Heatmap Scan (`-16 dB`).

---

### SCENE 4: THE WATCH TIME REVOLUTION (2:02 – 2:48) | Voiceover: `04_AUDIO_02m02s_to_02m48s_Scene_04_optimization_target_voiceover.mp3` (45.04s)

* **2:02 – 2:13**: Place `04_02m02s_to_02m13s_Scene_04_flow_dopamine_trance.mp4` (10.0s) on **Track V1**.
  * Visual: Moody Flow AI Video: Intimate face illuminated in dark by flickering phone glow.
  * Voiceover Anchor: *"Here is the detail almost nobody outside the industry knows. For years, recommendation systems were built to maximize clicks."*
  * Kinetic Keyword Pops: `MAXIMIZE CLICKS` (2:04), `THE HISTORICAL PIVOT` (2:08).
* **2:13 – 2:21**: Cut to `04_02m13s_to_02m21s_Scene_04_flow_clickbait_history_trap.mp4` (8.0s) on **Track V1**.
  * Visual: Flow AI Video: Chaotic retro wall of 2014 clickbait thumbnails with neon red arrows and sensational titles.
  * Voiceover Anchor: *"And that created an obvious problem. Creators learned that outrageous, misleading thumbnails and titles got clicked more..."*
  * Kinetic Keyword Pops: `CLICKBAIT ERA (2012-2015)` (2:14), `MISLEADING THUMBNAILS` (2:17).
* **2:21 – 2:29**: Cut to `04_02m21s_to_02m29s_Scene_04_flow_bf_skinner_behavioral_box.mp4` (8.0s) on **Track V1**.
  * Visual: Flow AI Video: Futuristic B.F. Skinner operant conditioning box with pulsing reward levers.
  * Voiceover Anchor: *"So platforms changed the target. Not clicks. Watch time."*
  * Kinetic Keyword Pops: `NOT CLICKS. WATCH TIME.` (2:22), `OPERANT CONDITIONING` (2:26).
* **2:29 – 2:48**: Place `04_02m29s_to_02m48s_Scene_04_VariableRewardCurve_manim.mp4` (19.04s) on **Track V1**.
  * Visual: 1080p 60fps Manim curve: Variable ratio reward schedule curve vs predictable curve with dopamine pulse markers.
  * *Assembly Note: Animation runs 12.00s; hold final reward curve card for 7.04s until 02:47.76.*
  * Voiceover Anchor: *"The system stopped asking what will get clicked and started asking what will this specific person actually keep watching? Variable reward schedule..."*
  * Kinetic Keyword Pops: `VARIABLE REWARD SCHEDULE` (2:30), `DOPAMINE PULSE` (2:37), `EXPECTED WATCH TIME` (2:43).
* **Track A2 (SFX)**:
  * `02:12.72`: Glitch Static / Camera Click (`-16 dB`).
  * `02:28.72`: Slot Machine Reward Ping / Chime (`-16 dB`).

---

### SCENE 5: THE PERSONALIZATION PARADOX (2:48 – 3:32) | Voiceover: `05_AUDIO_02m48s_to_03m32s_Scene_05_personalization_paradox_voiceover.mp3` (44.48s)

* **2:48 – 2:59**: Place `05_02m48s_to_02m59s_Scene_05_TransformerAttention_manim.mp4` (11.40s) on **Track V1**.
  * Visual: 1080p 60fps Manim animation: SASRec sequential transformer self-attention matrix showing weighted past watch events.
  * Voiceover Anchor: *"Pattern number one, the exact same video can perform completely differently depending on who is watching it... SASRec Transformer Attention."*
  * Kinetic Keyword Pops: `SASRec TRANSFORMER` (2:49), `SELF-ATTENTION MATRIX` (2:54).
* **2:59 – 3:08**: Hold Attention Network Matrix on **Track V1** (8.82s hold).
  * Visual: Static visual hold on the completed self-attention matrix diagram.
  * Voiceover Anchor: *"Show a video to someone whose history is full of long-form documentaries, and the system predicts a high completion probability."*
  * Kinetic Keyword Pops: `HIGH COMPLETION PROBABILITY` (3:00), `LONG-FORM PROFILE` (3:05).
* **3:08 – 3:32**: Place `05_03m08s_to_03m32s_Scene_05_DivergentMetrics_manim.mp4` (24.26s) on **Track V1**.
  * Visual: 1080p 60fps Manim animation: Dual real-time metric gauges (Viewer A: 94% retention rising green curve vs Viewer B: 3.0s drop-off falling red curve).
  * *Assembly Note: Animation runs 11.60s; hold final dual comparison card for 12.66s until 03:32.24.*
  * Voiceover Anchor: *"Show the identical video to someone who only watches short clips... 94% retention vs 3s drop-off... It is predicting a specific outcome for a specific person."*
  * Kinetic Keyword Pops: `94% RETENTION vs 3 SECONDS` (3:09), `IDENTICAL VIDEO, DIFFERENT OUTCOME` (3:16), `PREDICTED SATISFACTION` (3:25).
* **Track A2 (SFX)**:
  * `02:47.76`: Transformer Data Sweep (`-15 dB`).
  * `03:07.98`: Dual Meter Rising Chime & Low Drop (`-16 dB`).

---

### SCENE 6: THE RABBIT HOLE EFFECT & EXPLORATION (3:32 – 4:20) | Voiceover: `06_AUDIO_03m32s_to_04m20s_Scene_06_rabbit_hole_voiceover.mp3` (48.16s)

* **3:32 – 3:43**: Place `06_03m32s_to_03m43s_Scene_06_gemini_infinite_hallway_echoes.jpg` (10.40s) on **Track V1**.
  * Visual: Solitary figure walking down infinite mirrored hallway with glowing amber recursive echo silhouettes.
  * *Assembly Note: Apply smooth Ken Burns slow zoom-in (Scale: 100% $\to$ 108%, Ease-in-out).*
  * Voiceover Anchor: *"Pattern number two is the one that has drawn the most public scrutiny. When a system is purely optimized for keeping you watching..."*
  * Kinetic Keyword Pops: `THE RABBIT HOLE EFFECT` (3:33), `OPTIMIZED FOR RETENTION` (3:38).
* **3:43 – 3:51**: Cut to `06_03m43s_to_03m51s_Scene_06_flow_filter_bubble_isolated_mind.mp4` (8.0s) on **Track V1**.
  * Visual: Flow AI Video: Human silhouette trapped inside a pulsing amber algorithmic filter bubble.
  * Voiceover Anchor: *"...it can quietly narrow what you see, nudging toward more intense, more extreme, or more emotionally charged versions..."*
  * Kinetic Keyword Pops: `FILTER BUBBLE ISOLATION` (3:44), `EMOTIONALLY CHARGED NUDGING` (3:48).
* **3:51 – 4:06**: Place `06_03m51s_to_04m06s_Scene_06_EchoChamberDiversity_manim.mp4` (15.80s) on **Track V1**.
  * Visual: 1080p 60fps Manim radar: Feedback loop decay vs Epsilon-Greedy ($\varepsilon = 0.15$) exploration diversity injection.
  * Voiceover Anchor: *"This is not a secret. Platforms have publicly acknowledged the effect... Epsilon-Greedy (ε=0.15) & Diversity injection."*
  * Kinetic Keyword Pops: `EPSILON-GREEDY (ε = 0.15)` (3:52), `EXPLORATION vs EXPLOITATION` (3:57), `DIVERSITY INJECTION` (4:02).
* **4:06 – 4:20**: Place `06_04m06s_to_04m20s_Scene_06_gemini_deliberate_agency_control.jpg` (13.96s) on **Track V1**.
  * Visual: User shattering the filter bubble, actively controlling glowing cyan/amber holographic algorithmic dials.
  * *Assembly Note: Apply smooth Ken Burns slow drift/zoom (Scale: 100% $\to$ 106%).*
  * Voiceover Anchor: *"Understanding that is not about paranoia. It is about knowing what the system is actually doing so you can use it deliberately..."*
  * Kinetic Keyword Pops: `DELIBERATE AGENCY` (4:07), `TAKE BACK CONTROL` (4:14).
* **Track A2 (SFX)**:
  * `03:50.64`: Synthetic Glitch / Glass Ping (`-15 dB`).

---

### SCENE 7: CONCLUSION & 3 SYSTEM LEVERS (4:20 – 5:19) | Voiceover: `07_AUDIO_04m20s_to_05m19s_Scene_07_conclusion_voiceover.mp3` (58.20s)

* **4:20 – 4:46**: Place `07_04m20s_to_04m46s_Scene_07_AlgorithmSummaryRules_manim.mp4` (25.54s) on **Track V1**.
  * Visual: 1080p 60fps Manim summary: 3 Immutable Algorithmic Rules unlock sequentially with neon glow borders and checkmarks.
  * *Assembly Note: Animation runs 10.50s; hold 3 rules card for 15.04s while narrator walks through Rule 1, Rule 2, Rule 3.*
  * Voiceover Anchor: *"So, what does understanding the algorithm actually change? Rule 1: Not popularity... Rule 2: Attention not accuracy... Rule 3: Your signals build your reality."*
  * Kinetic Keyword Pops: `RULE 1: PREDICTION NOT POPULARITY` (4:22), `RULE 2: ATTENTION NOT ACCURACY` (4:30), `RULE 3: CONTROL YOUR SIGNALS` (4:38).
* **4:46 – 4:56**: Cut to `07_04m46s_to_04m56s_Scene_07_flow_quantum_bridge_ep04_teaser.mp4` (10.0s) on **Track V1**.
  * Visual: Flow AI Video: Recommendation vector lattice morphing into 3D quantum financial candlestick charts.
  * Voiceover Anchor: *"And third, the moment you understand what it is actually predicting, you can deliberately feed it different signals..."*
  * Kinetic Keyword Pops: `NEXT EPISODE: MARKET INTELLIGENCE` (4:47), `QUANTUM BRIDGE` (4:52).
* **4:56 – 5:19**: Cut to `07_04m56s_to_05m19s_Scene_07_flow_ep04_ai_stock_market_bridge.mp4` (22.66s) on **Track V1**.
  * Visual: Flow AI Video: 3D neural financial market forecasting network with glowing volumetric price projections.
  * *Assembly Note: Play 8.0s clip, hold final frame with Outro Card / Subscribe CTA until 05:18.60.*
  * Voiceover Anchor: *"We have now covered how markets crash, how recessions really move, and how the algorithm decides what reaches you. In our next breakdown, we are going back to the data... Subscribe to Quantrove."*
  * Kinetic Keyword Pops: `EP01: CRASHES` (4:57), `EP02: RECESSIONS` (5:01), `EP03: ALGORITHMS` (5:05), `SUBSCRIBE TO QUANTROVE` (5:12).
* **Track A2 / A3 (Audio & SFX)**:
  * `04:20.40`: UI Pop / Checkmark Ping for each rule (`-14 dB`) on Track A2.
  * `04:56.00`: Background music swells from `-22 dB` up to `-14 dB` during the outro end card, then smoothly fades out.

---

## 5. Master Assets Checklist

| Asset File | Type | Duration | Location |
| :--- | :--- | :---: | :--- |
| `00_AUDIO_00m00s_to_05m19s_full_voiceover_ep03_orus.mp3` | Master Voiceover Audio | 05:18.60 (318.60s) | `TIMELINE_MEDIA/` |
| `00_OVERLAY_00m00s_to_05m19s_kinetic_word_pops_60fps.mov` | 60fps Alpha MOV Overlay | 05:18.60 (318.60s) | `TIMELINE_MEDIA/` |
| `00_FRAME1_00m00s_thumbnail_cover_embed.jpg` | YouTube Frame 1 Embed Cover | — | `TIMELINE_MEDIA/` |
| `01_00m00s_to_00m10s_Scene_01_flow_infinite_feed_vortex.mp4` | Flow 4K AI Video | 10.00s | `TIMELINE_MEDIA/` |
| `01_00m10s_to_00m18s_Scene_01_flow_billions_scrolling_darkness.mp4` | Flow 4K AI Video | 8.00s | `TIMELINE_MEDIA/` |
| `01_00m18s_to_00m36s_Scene_01_ScaleOfUploads_manim.mp4` | Manim Animation | 18.00s (60fps) | `TIMELINE_MEDIA/` |
| `01_00m36s_to_00m42s_Scene_01_flow_glass_touchpoint.mp4` | Flow 4K AI Video | 6.04s | `TIMELINE_MEDIA/` |
| `02_00m42s_to_00m57s_Scene_02_TwoTowerVectorSpace_manim.mp4` | Manim Animation | 14.70s (60fps) | `TIMELINE_MEDIA/` |
| `02_01m05s_to_01m13s_Scene_02_flow_two_viewers_different_feeds.mp4` | Flow 4K AI Video | 8.00s | `TIMELINE_MEDIA/` |
| `03_01m22s_to_01m34s_Scene_03_ThreeStageFunnel_manim.mp4` | Manim Animation | 11.70s (60fps) | `TIMELINE_MEDIA/` |
| `03_01m34s_to_01m47s_Scene_03_flow_holographic_sorting_prism.mp4` | Flow 4K AI Video | 13.46s | `TIMELINE_MEDIA/` |
| `03_01m47s_to_02m03s_Scene_03_NeuralScoringMatrix_manim.mp4` | Manim Animation | 15.24s (60fps) | `TIMELINE_MEDIA/` |
| `04_02m02s_to_02m13s_Scene_04_flow_dopamine_trance.mp4` | Flow 4K AI Video | 10.00s | `TIMELINE_MEDIA/` |
| `04_02m13s_to_02m21s_Scene_04_flow_clickbait_history_trap.mp4` | Flow 4K AI Video | 8.00s | `TIMELINE_MEDIA/` |
| `04_02m21s_to_02m29s_Scene_04_flow_bf_skinner_behavioral_box.mp4` | Flow 4K AI Video | 8.00s | `TIMELINE_MEDIA/` |
| `04_02m29s_to_02m48s_Scene_04_VariableRewardCurve_manim.mp4` | Manim Animation | 19.04s (60fps) | `TIMELINE_MEDIA/` |
| `05_02m48s_to_02m59s_Scene_05_TransformerAttention_manim.mp4` | Manim Animation | 11.40s (60fps) | `TIMELINE_MEDIA/` |
| `05_03m08s_to_03m32s_Scene_05_DivergentMetrics_manim.mp4` | Manim Animation | 24.26s (60fps) | `TIMELINE_MEDIA/` |
| `06_03m32s_to_03m43s_Scene_06_gemini_infinite_hallway_echoes.jpg` | Gemini 4K Cinematic Image | 10.40s | `TIMELINE_MEDIA/` |
| `06_03m43s_to_03m51s_Scene_06_flow_filter_bubble_isolated_mind.mp4` | Flow 4K AI Video | 8.00s | `TIMELINE_MEDIA/` |
| `06_03m51s_to_04m06s_Scene_06_EchoChamberDiversity_manim.mp4` | Manim Animation | 15.80s (60fps) | `TIMELINE_MEDIA/` |
| `06_04m06s_to_04m20s_Scene_06_gemini_deliberate_agency_control.jpg` | Gemini 4K Cinematic Image | 13.96s | `TIMELINE_MEDIA/` |
| `07_04m20s_to_04m46s_Scene_07_AlgorithmSummaryRules_manim.mp4` | Manim Animation | 25.54s (60fps) | `TIMELINE_MEDIA/` |
| `07_04m46s_to_04m56s_Scene_07_flow_quantum_bridge_ep04_teaser.mp4` | Flow 4K AI Video | 10.00s | `TIMELINE_MEDIA/` |
| `07_04m56s_to_05m19s_Scene_07_flow_ep04_ai_stock_market_bridge.mp4` | Flow 4K AI Video | 22.66s | `TIMELINE_MEDIA/` |
| `99_thumbnail_ep03_youtube_cover.jpg` | Official 4K Master Cover | — | `TIMELINE_MEDIA/` |

---

## 6. Color Grading, Audio Mix & YouTube 4K Export Settings

### Color Grading Adjustment Layer:
* **Contrast**: `+5` to `+8` (enhances deep slate `#0B0E14` blacks)
* **Saturation**: `+2` to `+4` (gives electric cyan & amber neon vectors extra vitality)
* **Highlights**: `-3` (prevents neon peaking / clipping)
* **Shadows**: `-2` (deepens dynamic range)
* **Sharpen**: `+10` to `+15` (gives razor-sharp clarity to vectors and mathematical formulas)
* **Vignette**: `10% – 15%` (focuses viewer eye toward screen center)

### YouTube 4K Export Profile:
* **Resolution**: `3840 x 2160 (4K UHD)` *(Forces YouTube to allocate high-bitrate VP09/AV01 codecs even on 1080p displays)*
* **Frame Rate**: `60 fps`
* **Bitrate**: `Higher` (**50 – 70 Mbps** VBR)
* **Codec**: `H.264` or `HEVC (H.265)`
* **Audio**: `320 kbps`, `48,000 Hz`
