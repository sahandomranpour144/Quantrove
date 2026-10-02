# Episode 04 Assets Code Directory
Contains Python Manim scripts and chart generator code.

## Files
- `Scene_02_Bell_Curve_5075.py` — 50.75% win-rate bell curve + compounding counter (24s, window 01:26–01:50)
- `Scene_02_Reflexivity.py` — stationary 4×4 grid vs. reflexive market curve (29s, window 02:00–02:29)
- `Scene_03_Alpha_Decay.py` — alpha decay from +12% to equilibrium (31s, window 02:29–03:00)
- `Scene_04_Overfitting_Trap.py` — two scenes: `OverfittingTrapPart1` (29s, 03:21–03:50) + `OverfittingTrapPart2` (33s, 04:00–04:33)
- `render_all_ep04.py` — render driver: renders all 5 clips at 1080p60 and installs them into `TIMELINE_MEDIA/` with final filenames, verifying each duration against the timeline window (±0.35s)

## Render command (from the episode root)
```
py -3.12 02_assets_code/render_all_ep04.py
```

Requires: `manim` on Python 3.12, `ffmpeg`/`ffprobe` on PATH. Typography uses high-resolution `CleanText` vector scaling (`font="Segoe UI"`) to avoid Pango font-hinting advance quantization and character scattering.

**Why the scratch dir**: manim's scene-name parser treats this folder's `[IN_PROGRESS 2026-09-23]` brackets as regex character classes and crashes. The driver copies scene files to `_render_scratch_ep04/` (bracket-free), renders there, then moves finished MP4s into `TIMELINE_MEDIA/`. Keep the status brackets in the episode folder name — the driver handles it.
