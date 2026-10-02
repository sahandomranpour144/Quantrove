# Shorts Assembly Notes: standalone_short_ai_letter_blindspot

## Quick Start Deliverables
1. **Direct Upload (Ready to Publish)**:
   - Video File: `standalone_short_ai_letter_blindspot_FINAL.mp4`
   - Cover Thumbnail: `thumbnail.jpg` (1080x1920 high-CTR vertical cover frame)
   - Fully composited 1080x1920 @ 60fps with burned-in kinetic bouncing captions (#FFEE00 yellow boxes) and upper-third glassmorphism pop-up keyword pills.
2. **CapCut Custom Assembly Package**:
   - Background Video: `standalone_short_ai_letter_blindspot_raw_9x16.mp4`
   - Kinetic Overlay (Track V2): `TIMELINE_MEDIA/00_00m00s_to_00m43s_OVERLAY_kinetic_word_pops_60fps.mov` (ProRes 4444 RGBA with alpha channel)
   - Audio Stem: `standalone_short_ai_letter_blindspot_audio.wav` (44.1kHz stereo)
   - Subtitles (Optional): `ai_letter_blindspot_captions.srt`
   - Cover Thumbnail: `thumbnail.jpg`

---

## Timing & Measurements (CLAUDE.md §3.1)
- **Pacing**: Calibrated to natural, slightly slower delivery (tempo 1.10x vs previous 1.23x).
- **Measured Video Duration**: `43.12s` (`00:00:43,117` @ 60fps, 2587 frames)
- **Measured Audio Duration**: `43.12s` (`00:00:43,119`)
- **Tolerance**: ±0.002s (Strict compliance with ±0.1s threshold)
- **Ceiling**: Comfortably under the 60s Shorts limit.

---

## Visual Style Standard Compliance (.claude/rules/visual-style-standard.md)
1. **Typography Hierarchy**:
   - Font: Segoe UI Bold (`seguibl.ttf`) / Arial Bold (`arialbd.ttf`), UPPERCASE.
   - Weights: Bold for keywords/titles, medium/regular avoided on mobile text to ensure readability at small screen sizes.
2. **Color Palette (Dark Luxury Standard)**:
   - Canvas Background: Obsidian `#0B0F19`
   - Subtitle Bounding Box: Solid `#FFEE00` yellow with `#000000` text, 24px horizontal padding, 14px vertical padding, 14px border radius.
   - Pop-up Pills: Translucent glassmorphism `#0A1220` with glowing accent borders in Neon Cyan (`#00F0FF`), Radiant Gold (`#FFD700`), Mint Green (`#00FFA3`), and Warning Crimson (`#FF3366`).
3. **Pacing & Safe Margins**:
   - Subtitle Anchor: Y=1350 (Lower-third, cleared above bottom scrubber and right-side action buttons).
   - Pop-up Pill Anchor: Y=200 (Upper-third, centered).
   - Dynamic motion every 0.8–2.0s; zero static frames >3.0s.
