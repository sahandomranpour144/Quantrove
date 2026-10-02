# EP03 CapCut Editing & Visual Polish Master Guide
## "How Does The Algorithm Actually Decide What You See?" (Quantrove EP03)

> **Goal**: Transform the assembled video into a sleek, high-retention documentary (Vox / Bloomberg / Quantrove aesthetic) without complex editing tricks. Every step below is designed specifically for **CapCut Desktop** and can be executed quickly by non-experts.

---

## 🎧 1. Background Music (BGM) Selection & Mixing Strategy

Your video is **05:18.60** long. A single flat track can feel repetitive. We have pre-loaded the top royalty-free tracks directly into your `TIMELINE_MEDIA/` and `02_assets_code/ALL_MEDIA_TIMELINE/` folders.

### Pre-Loaded Music Files (Ready in `TIMELINE_MEDIA/`)

| File Name | Mood / Genre | Why It Works | Recommended Use |
| :--- | :--- | :--- | :--- |
| **`00_BGM_ALT1_A_Hand_In_The_Dark.mp3`** *(Underbelly & Ty Mayer)* | Suspenseful, Dark, Pulsing Bassline | Classic investigative journalism vibe. Creates tension around algorithmic black boxes and dopamine conditioning. | **Act 1: The Dark Mechanism & The Funnel** (`00:00 – 02:47`) |
| **`00_BGM_ALT2_Hovering_Thoughts.mp3`** *(Spence)* | Smooth, Intellectual, Tech Ambient | Clean synth pads, analytical, optimistic. Keeps viewer engaged on AI transformer attention and taking back control. | **Act 2: Attention & Taking Control** (`02:47 – 05:18`) |
| **`00_AUDIO_00m00s_bgm_tiburtina_schwartzy.mp3`** *(Schwartzy)* | Ambient Documentary | Steady, minimal, unobtrusive. | Alternative single track option |

---

### 🏆 The Pro "2-Act Dynamic" Strategy (Recommended)

Instead of 1 track for the whole 5 minutes, use **two complementary tracks** to match the psychological arc of the video:

1. **Act 1: The Hidden Machine & The Optimization Trap (`00:00 – 02:47`)**
   * Place `00_BGM_ALT1_A_Hand_In_The_Dark.mp3` on **Track A3** from `00:00.00`.
   * **Mood**: Tense, dark, investigative.
   * Covers: The Hook (500-Hour Problem), The Popularity Myth, Two-Stage Neural Funnel, and The Watch Time Revolution (B.F. Skinner box).
2. **Act 2: The Attention Paradox & Taking Back Agency (`02:47 – 05:18.60`)**
   * Place `00_BGM_ALT2_Hovering_Thoughts.mp3` on **Track A3** starting at **`02:47.76`** (when the voiceover transitions to *"Pattern number one, the exact same video can perform completely differently..."*).
   * Apply a **1.5-second Crossfade** between the two tracks.
   * **Mood**: High-tech, intellectual, empowering resolution.
   * Covers: Transformer Self-Attention, Divergent Retention, Echo Chambers vs Epsilon-Greedy, 3 Rules to Control the Algorithm, and the Episode 4 Teaser Bridge.

---

### CapCut Audio Mixing Levels (Crucial)

Select your audio clips and set these levels in CapCut's right-hand **Basic Audio** panel:
* **Master Voiceover (Track A1)**: 
  * Volume: `0.0 dB` (100%)
  * Check **"Loudness Normalization"** (ON)
  * Check **"Noise Reduction"** (ON)
* **Background Music (Track A3)**:
  * Volume: **`-23.0 dB` to `-25.0 dB`** during voiceover narration.
  * Enable **Auto-Ducking**: Ducking intensity set to `-18 dB to -22 dB`.
  * **Outro Swell (`04:56 – 05:18.60`)**: Fade BGM volume up to **`-14.0 dB`** as the narrator introduces Episode 4 and the subscribe end card appears.

---

## 🔊 2. Sound Effects (SFX) Master Guide

Sound effects give mathematical charts weight and keep viewer retention locked. Clean, production-ready SFX are located directly in `TIMELINE_MEDIA/` and `02_assets_code/ALL_MEDIA_TIMELINE/`.

### Available Local SFX Files
1. **`00_SFX_whoosh.wav`**: Crisp, clean transition swoosh for scene cuts and chart entries.
2. **`00_SFX_ding.wav`**: Elegant, positive metallic chime for checkmarks, rules, and optimal metrics.
3. **`00_SFX_buzzer.wav`**: Subtle error buzzer / warning thud for myth busting and negative retention drops.

### CapCut Built-In SFX Alternative
You can also use CapCut's built-in sound library with 1 click:
* Top Menu: **Audio** → **Sound effects** (left sidebar).
* Search: `"Impact"`, `"Whoosh"`, `"Click"`, `"Ding"`, or `"Glitch"`.

---

### Second-by-Second SFX Cue Sheet

| Timestamp | Event / Scene Action | Sound Effect | CapCut Source / Local File | Volume Level |
| :--- | :--- | :--- | :--- | :--- |
| **00:00.00** | Video starts / Infinite feed vortex push | **Deep Sub Bass Boom / Impact** | CapCut search: *"Impact"* or *"Boom"* | `-8 dB` |
| **00:10.00** | Cut to dark subway scrolling | **Whoosh** | `00_SFX_whoosh.wav` | `-14 dB` |
| **00:18.00** | Manim 500 hrs/min counter stacks up | **Digital Counter Ticker / Clicks** | CapCut search: *"Click"* or *"Counter"* | `-16 dB` |
| **00:36.00** | Cut to glass touchpoint finger hover | **Whoosh** | `00_SFX_whoosh.wav` | `-14 dB` |
| **00:42.04** | Scene 2 Two-Tower neural vector reveal | **Low Ambient Servo / Whoosh** | `00_SFX_whoosh.wav` | `-14 dB` |
| **00:58.00** | "THEY DO NOT" myth bust | **Buzzer / Warning Thud** | `00_SFX_buzzer.wav` | `-15 dB` |
| **01:05.24** | Split-screen two divergent feeds cut | **Digital Glitch / Swipe** | CapCut search: *"Glitch"* or *"Swipe"* | `-16 dB` |
| **01:22.32** | Scene 3 Three-Stage Funnel breakdown | **Clean UI Digital Thud / Laser** | CapCut search: *"UI"* or *"Digital"* | `-15 dB` |
| **01:47.48** | Neural Scoring Heatmap matrix scan | **High-Tech Matrix Heatmap Scan** | CapCut search: *"Scan"* or *"Tech"* | `-16 dB` |
| **01:54.00** | Rank #1 selection badge locked | **Positive Ding / UI Chime** | `00_SFX_ding.wav` | `-14 dB` |
| **02:02.72** | Scene 4 Dopamine trance cut | **Whoosh** | `00_SFX_whoosh.wav` | `-14 dB` |
| **02:12.72** | 2014 Clickbait thumbnail wall flood | **Glitch Static / Camera Click** | CapCut search: *"Shutter"* or *"Glitch"* | `-16 dB` |
| **02:21.00** | B.F. Skinner operant box reveal | **Subtle Mechanical Lock / Click** | CapCut search: *"Mechanical Click"* | `-15 dB` |
| **02:28.72** | Variable Reward Curve & Dopamine Ping | **Reward Slot Chime / Bell Ping** | `00_SFX_ding.wav` | `-14 dB` |
| **02:47.76** | Scene 5 SASRec Transformer Attention | **Whoosh / Data Sweep** | `00_SFX_whoosh.wav` | `-14 dB` |
| **03:07.98** | Dual Gauge reveal: 94% retention vs 3s | **Dual Gauge Meter Chime & Drop** | `00_SFX_ding.wav` + `00_SFX_buzzer.wav` | `-15 dB` |
| **03:32.24** | Scene 6 Infinite Hallway Echoes cut | **Whoosh** | `00_SFX_whoosh.wav` | `-14 dB` |
| **03:50.64** | Echo Chamber Diversity radar & Epsilon | **Synthetic Glitch / Glass Ping** | CapCut search: *"Glitch"* or *"Ping"* | `-15 dB` |
| **04:06.44** | User breaks through filter bubble | **Glass Break / Energy Whoosh** | CapCut search: *"Glass"* or *"Energy"* | `-14 dB` |
| **04:20.40** | 3 Rules Checkmark #1 (Not Popularity) | **UI Pop / Positive Ding** | `00_SFX_ding.wav` | `-13 dB` |
| **04:29.00** | 3 Rules Checkmark #2 (Attention Target) | **UI Pop / Positive Ding** | `00_SFX_ding.wav` | `-13 dB` |
| **04:37.00** | 3 Rules Checkmark #3 (Control Signals) | **UI Pop / Positive Ding** | `00_SFX_ding.wav` | `-13 dB` |
| **04:46.00** | Quantum Bridge to Episode 4 Teaser | **Cinematic Warp / Whoosh** | `00_SFX_whoosh.wav` | `-12 dB` |
| **04:56.00** | 3D Neural Market Outro Screen | **Deep Cinematic Impact / Swell** | CapCut search: *"Impact"* | `-10 dB` |

---

## 🔀 3. Transitions (Simple, Clean & Professional)

Avoid distracting 3D spinning transitions. A top-tier documentary uses **3 clean transition types**:

### The 3 Master Transitions in CapCut Desktop:
1. **Mix / Cross Dissolve** (`0.3s – 0.5s`): Seamlessly blends Flow AI videos and Manim charts.
2. **Dip to Black / Black Fade** (`0.4s`): Used between major scene chapter breaks to give the viewer time to digest complex technical ideas.
3. **Glitch / White Flash** (`0.15s – 0.2s`): Quick flash on dramatic paradigm shifts (clickbait era shift, filter bubble break).

### Exact Second-by-Second Transition Locations:

* **`00:42.04` (Scene 1 to Scene 2)**: **Dip to Black** (`0.4s`) — Marks the transition from Hook into The Popularity Myth.
* **`01:22.32` (Scene 2 to Scene 3)**: **Dip to Black** (`0.4s`) — Transition into Two-Stage Neural Architecture.
* **`02:02.72` (Scene 3 to Scene 4)**: **Dip to Black** (`0.4s`) — Transition into The Watch Time Revolution.
* **`02:47.76` (Scene 4 to Scene 5 — Act 2 Shift)**: **Dip to Black** (`0.4s`) + **Audio Crossfade** — Major chapter transition.
* **`03:32.24` (Scene 5 to Scene 6)**: **Dip to Black** (`0.4s`) — Transition into The Rabbit Hole Effect.
* **`04:20.40` (Scene 6 to Scene 7)**: **Dip to Black** (`0.4s`) — Transition into 3 Rules & Conclusion.
* **`04:45.94` (Manim Rules to Teaser Bridge)**: **Dissolve / Mix** (`0.4s`) — Smooth glide into 3D AI candlestick teaser.
* **`05:17.80` (End of Video Outro)**: **Fade to Black** (`0.8s`).

---

## ✍️ 4. On-Screen Texts, Titles & Lower Thirds

Use text to anchor the viewer's memory on core terminology.

### Master Text Style Settings (CapCut Right-Hand Panel)
* **Font**: `Montserrat`, `Inter`, or `System` (Bold).
* **Case**: UPPERCASE for titles, Title Case for technical definitions.
* **Color Palette**:
  * Primary Text: Pure White (`#FFFFFF`)
  * Data / Neural Vector Highlights: Electric Cyan (`#00F0FF`) or Amber Gold (`#FFB800`)
  * Warning / Myth: Crimson Red (`#EF4444`)
  * Optimization / Optimal Score: Emerald Green (`#10B981`)
* **Text Shadow**: Black, Opacity `85%`, Blur `12`, Distance `4`.
* **In Animation**: Under "Animation" → "In", choose **"Fade In"** or **"Slide Up"** (`0.25s`).
* **Out Animation**: Under "Animation" → "Out", choose **"Fade Out"** (`0.25s`).

### Exact Copy-Paste Text Overlays

| Timecode | Track | On-Screen Text Content | Color & Style | Notes |
| :--- | :---: | :--- | :--- | :--- |
| **00:00 – 00:08** | V3 | **HOW ALGORITHMS DECIDE**<br>*The Hidden Prediction Engine* | Line 1: Cyan (`#00F0FF`)<br>Line 2: White | Top-Center badge hook. |
| **00:36 – 00:42** | V3 | **"How Does It Actually Decide?"** | Amber Gold (`#FFB800`) | Lower-third hook question. |
| **00:43 – 00:55** | V3 | **THE POPULARITY MYTH**<br>*Why Views Do Not Dictate Recommendations* | Line 1: Crimson Red (`#EF4444`)<br>Line 2: White | Chapter 2 header badge. |
| **01:23 – 01:34** | V3 | **THE 2-STAGE NEURAL PIPELINE**<br>*ScaNN Retrieval → Deep Ranking* | Line 1: Cyan (`#00F0FF`)<br>Line 2: Gold | Technical architecture badge. |
| **02:03 – 02:14** | V3 | **THE OPTIMIZATION SHIFT**<br>*Clicks (2012) → Watch Time (Today)* | Line 1: White<br>Line 2: Amber Gold | Historical transition card. |
| **02:48 – 02:59** | V3 | **PATTERN #1: THE PERSONALIZATION PARADOX**<br>*SASRec Sequential Transformer Attention* | Line 1: Cyan (`#00F0FF`)<br>Line 2: White | Chapter 5 header badge. |
| **03:33 – 03:44** | V3 | **PATTERN #2: THE RABBIT HOLE EFFECT**<br>*Feedback Loops & Diversity Injection* | Line 1: Amber Gold (`#FFB800`)<br>Line 2: White | Chapter 6 header badge. |
| **04:21 – 04:45** | V3 | **THE 3 IMMUTABLE ALGORITHM RULES** | Pure White with Gold glow | Summary section header. |
| **04:56 – 05:18** | V3 | **SUBSCRIBE TO QUANTROVE**<br>*Next Episode: How AI Trades Wall Street* | Line 1: Emerald Green / White<br>Line 2: Cyan | Outro call to action. |

---

## 💬 5. Captions & Kinetic Keyword Pop Layer

You have two powerful subtitle layers available:

### Option A: The Pre-Rendered Kinetic Keyword Pop Track (Included)
* Simply drag `00_OVERLAY_00m00s_to_05m19s_kinetic_word_pops_60fps.mov` onto **Track V2** starting at **`00:00.00`**.
* It contains 60+ pre-timed kinetic power words with elastic spring punch-ins, glowing cyan/amber halos, and soft drop shadows with native alpha transparency!

### Option B: CapCut 1-Click Auto-Captions (For Full Word-by-Word Narration)
1. Click **"Text"** in top bar → Click **"Auto captions"** in left panel.
2. Select Language: **"English"** → Click **"Create"**.
3. In inspector: Set **Font Size: `10`**, **Style: Bold (B)**, and **Position Y: `-380`** so captions sit in the lower-third comfortably below all Manim charts and kinetic popups.

---

## 🎨 6. Visual Polish & Effects (Simple 1-Click Polish)

These 4 simple CapCut techniques make the entire video feel like a high-budget documentary:

### Technique A: Ken Burns / Slow Drift on Static Images (1 Click!)
For the 2 static Gemini AI cinematic images in Scene 6:
* `03:32 – 03:43` (`06_03m32s_to_03m43s_Scene_06_gemini_infinite_hallway_echoes.jpg`):
  * Select clip → Go to **Animation** → **Combo** → Choose **"Zoom 1"** (or Scale `100% → 108%`).
* `04:06 – 04:20` (`06_04m06s_to_04m20s_Scene_06_gemini_deliberate_agency_control.jpg`):
  * Select clip → Go to **Animation** → **Combo** → Choose **"Slow Zoom"** (or Scale `100% → 106%`).

### Technique B: Cinematic Vignette (Draws Focus to Center)
* Go to: **Effects** → **Video Effects** → search **"Vignette"**.
* Drag Vignette onto **Track V4** (spanning the entire timeline `00:00 – 05:18.60`).
* In the right panel, set intensity to **`12% – 15%`**.

### Technique C: Subtle Screen Shake on Paradigm Shifts (0.4s Burst)
* At `02:13` (2014 clickbait flood) and `03:43` (filter bubble trap):
* Go to **Effects** → **Video Effects** → search **"Camera Shake"** (or **"Shake"**).
* Drag over the 0.4s moment of impact.
* Adjust settings: **Speed: `15`**, **Intensity: `8`** (subtle, high-impact).

### Technique D: Global Color Adjustment Layer
* Drag a **Default Adjustment Layer** across the timeline on Track V4.
* Set these values in the right panel:
  * **Contrast**: `+7`
  * **Saturation**: `+4`
  * **Sharpen**: `+12`
  * **Highlights**: `-3`
  * **Shadows**: `-4`
* *Result*: Deeper slate blacks, luminous neon cyan vectors, and crystal-clear formulas.

---

## 🚀 7. Final Export Checklist (60fps High Quality)

1. **Watermark Check**: Ensure CapCut's default outro watermark is deleted from the timeline.
2. **Audio Levels Check**: Verify voiceover is crisp at 0dB, BGM is comfortably seated at -24dB, and SFX punch through cleanly.
3. **Thumbnail Cover Check**: Confirm `00_FRAME1_00m00s_thumbnail_cover_embed.jpg` is set at the 1st frame or via CapCut's **Cover** button.
4. **Click "Export" (Top Right Button)**:
   * **Title**: `Quantrove_EP03_How_Algorithms_Decide_MASTER`
   * **Resolution**: `3840 x 2160 (4K UHD)` or `1080p`
   * **Bitrate**: `Higher` (**50 – 70 Mbps** VBR)
   * **Codec**: `H.264` or `HEVC (H.265)`
   * **Format**: `MP4`
   * **Frame Rate**: `60 fps` *(matches 60fps Manim animations)*
5. Export and upload to YouTube!
