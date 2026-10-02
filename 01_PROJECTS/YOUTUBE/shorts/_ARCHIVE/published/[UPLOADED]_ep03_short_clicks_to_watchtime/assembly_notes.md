# Shorts Assembly Notes: ep03_short_clicks_to_watchtime

## 1. Quick Start & Production Status
- **Status**: 100% Fully Rendered & Ready to Upload (Gate 2 QA: PASS).
- **Master Video File**: [`ep03_short_clicks_to_watchtime.mp4`](./ep03_short_clicks_to_watchtime.mp4) (Composited 1080x1920 @ 60fps with burned-in Remotion `shorts_v2` kinetic captions).
- **Upload Metadata**: [`metadata.md`](./metadata.md) (Optimized title, description, tags, pinned comment, and parent EP03 related video link).

---

## 2. Timing & Master Reference (CLAUDE.md §3.1)
- **Source Master**: `long03_how_algorithms_decide/TIMELINE_MEDIA/MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4`
- **Master Clip In Timestamp**: `135.800s` (00:02:15,800) — dropped introductory sentence, starts cleanly on *"Creators..."* (raw extract word 15).
- **Master Clip Out Timestamp**: `167.600s` (00:02:47,600).
- **Measured Duration**: `31.80s` (1,908 frames @ 60fps — strictly under 60s Shorts ceiling).
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
   - **Keyword Emphasis**: Power Lime (`#C3D809`) on key terms (`creators`, `clicks`, `watch`, `time`, `feed`, etc.).
   - **Risk / Warning**: Pumpkin (`#FD802E`) on anomaly/risk terms (`misleading`, `disappointed`).
   - **Lines & UI Chrome**: Charcoal Slate (`#233D4C`).
   - **Zero Yellow Fill Boxes**: Legacy `#FFEE00` yellow bounding boxes and neon cyan accents have been fully eliminated.
3. **Kinetic Caption System (R5/R6)**:
   - **Engine**: Remotion 60fps overlay (`ShortsV2TextLayer`) composited onto the blur-padded video.
   - **Chunking**: Strict 2–4 words per chunk; zero 1-word chunks (21 total chunks in `text_events.json`).
   - **Animation**: Fade blur-up entrance with clean hard cut per chunk.
   - **Positioning**: Center X, lower-third Y at 68% (`y_pct: 68.0`, ~1305px on the 1920 canvas, safe from YouTube Shorts right-side buttons and bottom title bar).

---

## 4. Audio & Delivery Specs (R3, R4, R9)
- **Audio Codec**: AAC stereo @ 192 kbps.
- **Integrated Loudness**: `-14.2 LUFS` (Strict compliance with `-14.0 ± 1.5 LUFS`).
- **Pacing & Cadence**: `121.4 WPM` (63 words in 31.1s spoken duration — calm, authoritative documentary pacing).
- **Clean Exit (R9)**: Cut terminates `0.36s` after the last spoken word ("today."), with zero CTA, zero outro cards, and no subscriber requests.

---

## 5. Narrative Structure (4 Beats)
1. **Problem / Clickbait Crisis** (0.0s – 11.0s): Creators learned misleading thumbnails and titles got clicked even when the video disappointed viewers.
2. **The Pivot** (11.0s – 16.0s): Platforms changed the target from clicks to watch time.
3. **The Algorithmic Mechanism** (16.0s – 23.5s): The system stopped asking what gets clicked, started asking what this specific person will actually keep watching.
4. **Core Insight** (23.5s – 31.8s): That single change is the most important thing to understand about how modern feeds operate.

---

## 6. Directory Asset Inventory
- `ep03_short_clicks_to_watchtime.mp4` — Final composited master video (31.80s, 9.49 MB, 1080x1920 @ 60fps).
- `metadata.md` — Complete YouTube Shorts upload package.
- `text_events.json` — 21 calibrated text chunk events for the Remotion 60fps layer.
- `words.json` — 63 shifted word timestamps aligned to the 31.80s timeline.
- `shotlist.json` — Extraction shotlist metadata with motion and hold tags.
- `exact_word_timestamps.json` — Raw word timestamps from initial Whisper alignment.
- `_old_v1/ep03_short_clicks_to_watchtime_captions.srt` — Archived legacy v1 captions file.
