# HTML Motion Engine Standard

## Overview
`html_motion` is the 4th scene engine in the Quantrove pipeline (alongside Manim, Remotion, and Flow). It produces 4–8s terminal/UI-style visual metaphors built by coding models from a prompt, exported to MP4 manually by Sahand (Path A) and placed in timeline media like Flow clips.

- **Placement**: Data Reveal beat of the Chapter Quad.
- **Shorts**: Maximum 1 `html_motion` clip per Short.
- **Runtime Share**: Set per episode by story need (~20% is a guide, not a cap).
- **Clips**: Exact-slot (2–8s), play once `t=0..N`, hold final frame (`>=0.5s`). NOT a loop.
- **Overlay Boundary**: Kinetic pop-up overlay (V2) stays the ONLY keyword layer in every video. `html_motion` never renders narration keywords.
- **Execution Path**: Path A only (manual MP4 export). Do NOT build headless rendering.
- **Palette Lock**: Only `#202322` (bg), `#233D4C` (grid/chrome), `#C3D809` (primary accent), `#FD802E` (risk/anomaly), `#E6EDF3` (text). Opacity variations of these allowed; no other hues, gradients, glows, shadows, HUD circles, or particles. Font: Nohemi (Inter fallback).

---

## Per-Scene Specification Fields
Every `html_motion` scene specification must include:
- `scene_id`: Unique identifier (e.g., `SC04_ORDER_BOOK_DEPTH`)
- `episode`: Episode slug (e.g., `long06_hft_microsecond_pricing`)
- `slot duration`: Duration in seconds (2.0s to 8.0s, e.g., `5.0s`)
- `aspect`: `16:9` or `9:16`
- `concept`: High-level visual metaphor
- `focal element`: Single primary UI/terminal element commanding focus
- `data source`: `REAL + cite` (with specific source cited) | `ILLUSTRATIVE` (with corner tag "ILLUSTRATIVE DATA")

---

## Base Prompt Block (Verbatim)

```text
Create ONE self-contained HTML file (inline HTML/CSS/JS, no CDN, no audio, no external assets) that runs in Chrome.
- Stage fixed {1920x1080 | 1080x1920}, scaled to fit the window, centered, background #202322.
- Duration exactly {N}.0 s. Play once t=0..N, then hold the final frame. NOT a loop.
- Deterministic: all visuals are a pure function render(t). Expose window.setTime(t). Seeded PRNG only. No CSS animations, no Date.now drift, no free randomness. Autoplay drives render(t) from one clock.
- Colors only: #202322 (bg), #233D4C (grid/dividers), #C3D809 (primary accent), #FD802E (risk/anomaly), #E6EDF3 (text). Opacity variations allowed. No other colors, gradients, glow, shadows, particles, HUD circles.
- Font: "Nohemi","Inter",system-ui,sans-serif; tabular-nums for numbers.
- Legibility: min font 28px (16:9) / 40px (9:16); max 3 secondary readouts; one focal element; main line >=3px, grid 1px.
- Safe zone: For 16:9 (1920x1080): Safe stage box x=96..1824, y=190..856 (width 1728px, height 666px). Forbidden caption lane y=864..1080; popup band y=56..176. For 9:16 (1080x1920): Safe stage band x=60..880, y=250..1000 (visuals only). Forbidden text band y=1040..1440; reserved margins top=250, bottom=480, left=60, right=200. Keep the caption/pop-up region empty. No narration keywords in the graphic.
- Numbers: real data with source, or a corner tag "ILLUSTRATIVE DATA". Never present invented figures as real.
- Motion: ease-in-out, 0.4s stagger, no bounce, calm final hold >= 0.5s.
- Output only the complete HTML.
```

---

## Folder & File Conventions
In the timeline-media convention (where Flow clips go):
- Long-form: `TIMELINE_MEDIA/html_motion/<ep>_<scene_id>_<N>s.mp4` with source `<ep>_<scene_id>_<N>s.html` beside it.
- Shorts: `shorts/<short_dir>/html_motion/<ep>_<scene_id>_<N>s.mp4` with source `<ep>_<scene_id>_<N>s.html` beside it.
