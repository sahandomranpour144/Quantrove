---
name: episode-publish-package
description: Generate and validate the final YouTube episode publishing package (metadata, titles, calibrated chapters, description, tags, pinned comment) anchored strictly to measured media length. Refuses to emit chapter timestamps that do not match ffprobe measurements of the final master or audio stems. Prevents metadata duration drift.
---

# Episode Publish Package Generator & Validator

Mission: Produce a 100% production-ready, calibrated YouTube publishing package in `03_metadata/upload_metadata.md` for any long-form episode or short, anchored strictly to measured file durations (§3.1).

## Mandatory Checks Before Emitting Metadata

1. **Duration Measurement**:
   - Probe the master video or master audio file with `ffprobe`:
     ```bash
     ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 <master_file>
     ```
   - Record the exact duration in seconds and format as `MM:SS`.

2. **Chapter Calibration**:
   - Every chapter timestamp must match the exact start time of that scene's audio stem or timeline cut.
   - Chapter 1 must start at `0:00`.
   - The final chapter must be earlier than the measured video duration.
   - Minimum chapter duration on YouTube is 10 seconds.

3. **Title Optimization**:
   - Offer 3 title variants: High Curiosity, Data-First, Search-Optimized.
   - Character count constraint: strictly under 60 characters for full visibility on mobile devices.

4. **Description & SEO Structure**:
   - Line 1–2: High-hook summary with target keywords before the fold ("...Show more").
   - Timestamps block: Auto-formatted clickable chapters.
   - Channel links: Subscribe CTA, Playlist link, previous episode link.
   - Disclaimers: Clear financial / analytical educational disclaimers.

5. **Tags & Pinned Comment**:
   - 15–20 high-relevance tags (comma-separated, under 500 characters total).
   - High-engagement pinned comment posing an open, analytical question to drive viewer debate.
