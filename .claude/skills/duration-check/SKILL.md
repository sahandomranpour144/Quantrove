---
name: duration-check
description: Verify real file durations via ffprobe before any render or assembly step hardcodes a duration number. Use before writing Manim scene runtimes, building ffmpeg timelines, generating chapter timestamps, or reviewing any script that references a media length. Prevents the 156s-instead-of-384s bug class.
---

# Duration Check — Measure, Never Estimate

Standing rule (CLAUDE.md §3.1): every scene/video duration must anchor to the real measured file length. Never hardcode or estimate. This bug shipped once for real: a video rendered at 156s instead of 384s because durations were assumed, not measured.

## Procedure

### 1. Measure with ffprobe (canonical command)

From `longs/.../long02_.../02_assets_code/render_manim_ep02.py`:

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 <file>
```

JSON variant for scripts, from `pipeline/assemble_long_form_ffmpeg.py::probe_duration`:

```python
import json, subprocess

def probe_duration(path):
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", path]
    info = json.loads(subprocess.run(cmd, capture_output=True, text=True).stdout)
    return float(info["format"]["duration"])
```

### 2. Verify after every render — fail loudly on mismatch

Post-render, compare actual vs intended duration. Production tolerance is ±0.1s (the exact check `render_manim_ep02.py` runs on all 6 scenes):

```python
status = "PASSED (Exact)" if abs(target_dur - actual_dur) < 0.1 else f"DIFF ({actual_dur - target_dur:+.2f}s)"
```

A `DIFF` is a blocker — fix the scene timing and re-render. Never ship a duration mismatch.

### 3. Anchor durations to audio, not plans

- Manim scene runtimes must match the measured voiceover segment for that scene (`voiceover/generated_audio/sceneXX.wav` — ffprobe the WAV itself).
- Assembly scripts must probe every input file at runtime — never trust durations from planning docs (plans go stale; files are truth).
- Chapter timestamps in `upload_metadata.md` must be recalculated from the final exported master, not from the script.

### 4. Reviewing pipeline code

Grep for bare float durations. Each one must either (a) come from a runtime probe, or (b) be a documented probe result with the source file named next to it. Anything else is a latent bug.
