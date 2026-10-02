# Shorts Assembly Notes: ep03_short_rabbit_hole

## 1. Quick Start & Production Status
- **Status**: 100% Fully Rendered & Ready to Upload (Gate 2 QA: PASS).
- **Master Video File**: [`ep03_short_rabbit_hole.mp4`](./ep03_short_rabbit_hole.mp4) (Composited 1080x1920 @ 60fps with burned-in Remotion `shorts_v2` kinetic captions).
- **Upload Metadata**: [`metadata.md`](./metadata.md) (Optimized title, description, tags, pinned comment, and parent EP03 related video link).

---

## 2. Timing & Master Reference (CLAUDE.md §3.1)
- **Source Master**: `long03_how_algorithms_decide/TIMELINE_MEDIA/MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4`
- **Cold Open Hook (0.0s – 2.0s)**: Prepended 2.00s cold open hook *"It can actively reshape it."* extracted from master timestamp `247.650s` to `249.650s` (words 72–76 of raw extract / 30.95s–32.95s in raw audio).
- **Natural Segment (2.0s – 45.60s)**: Main narrative from master timestamp `216.700s` to `260.300s` (0.0s to 43.60s natural segment).
- **Measured Duration**: `45.60s` (2,736 frames @ 60fps — strictly under 60s Shorts ceiling).
- **Canvas Resolution**: `1080x1920` (9:16 Vertical).
- **Framerate**: `60.0 fps` (H.264 High Profile, CRF 18, faststart).
- **Reframe Method**: 9:16 blur-pad (Boxblur 25 background + 1080px crisp foreground, zero chart cropping).

---

## 3. Visual Style Standard Compliance (shorts_style.json & brand_tokens.json)
All typography, colors, and motion adhere to the **Institutional Data Intelligence** standard:
1. **Typography Hierarchy**:
   - **Primary Font**: `Nohemi` (with `Inter` fallback).
   - **Weights**: **Bold (700)** for emphasis and risk keywords; **Medium (500)** for standard body text. Never lighter than medium.
2. **Color Palette**:
   - **Background Canvas**: Raisin Black (`#202322`).
   - **Base Text**: High-contrast Off-White (`#E6EDF3`).
   - **Keyword Emphasis**: Power Lime (`#C3D809`) on key terms (`system`, `feed`, `watching`, `deliberately`, etc.).
   - **Risk / Warning**: Pumpkin (`#FD802E`) on anomaly/risk terms (`reshape`, `narrow`, `intense`, `extreme`, `emotionally`, `charged`, `unchecked`, `paranoia`).
   - **Lines & UI Chrome**: Charcoal Slate (`#233D4C`).
   - **Zero Yellow Fill Boxes**: Legacy `#FFEE00` yellow bounding boxes and neon cyan accents have been fully eliminated.
3. **Kinetic Caption System (R5/R6)**:
   - **Engine**: Remotion 60fps overlay (`ShortsV2TextLayer`) composited onto the concatenated blur-pad footage.
   - **Chunking**: Strict 2–4 words per chunk; zero 1-word chunks (39 total chunks in `text_events.json`).
   - **Animation**: Fade blur-up entrance with clean hard cut per chunk.
   - **Positioning**: Center X, lower-third Y at 68% (`y_pct: 68.0`, ~1305px on the 1920 canvas, safe from YouTube Shorts right-side buttons and bottom title bar).

---

## 4. Audio & Delivery Specs (R3, R4, R9)
- **Audio Codec**: AAC stereo @ 192 kbps.
- **Integrated Loudness**: `-14.1 LUFS` (Strict compliance with `-14.0 ± 1.5 LUFS`).
- **Pacing & Cadence**: `145.7 WPM` (110 words in 45.3s spoken duration — optimal conversational flow within the 145–160 WPM target).
- **Clean Exit (R9)**: Cut terminates `0.18s` after the last spoken word ("it."), with zero CTA, zero outro cards, and no subscriber requests.

---

## 5. Narrative Structure (6 Beats)
1. **Cold Open Hook** (0.0s – 2.0s): *"It can actively reshape it."* (Instant high-stakes hook).
2. **Mechanism / The Feed** (2.0s – 18.0s): Pure session-length optimization quietly narrows what you see toward more extreme content.
3. **Disclosure** (18.0s – 20.0s): *"This is not a secret."*
4. **Corporate Reality** (20.0s – 33.5s): Platforms publicly acknowledged the effect; an unchecked engagement system doesn't just reflect interest.
5. **Loop Payoff** (33.5s – 35.5s): *"It can actively reshape it."* (Full resolution of the cold open loop).
6. **Core Insight** (35.5s – 45.6s): Understanding this is about knowing what the system is doing, so you use it deliberately instead of being used by it.

---

## 6. Directory Asset Inventory
- `ep03_short_rabbit_hole.mp4` — Final composited master video (45.60s, 7.89 MB, 1080x1920 @ 60fps).
- `metadata.md` — Complete YouTube Shorts upload package.
- `text_events.json` — 39 calibrated text chunk events for the Remotion 60fps layer.
- `words.json` — 110 aligned word timestamps (prepended cold open + natural sequence).
- `shotlist.json` — Extraction shotlist metadata with motion and hold tags.
- `exact_word_timestamps.json` — Raw word timestamps from initial Whisper alignment.
- `_old_v1/ep03_short_rabbit_hole_captions.srt` — Archived legacy v1 captions file.
