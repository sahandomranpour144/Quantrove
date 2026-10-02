---
name: word-sync
description: Word-level transcription and timestamp alignment workflow for syncing captions, kinetic word pops, and visual cuts to narration. Use when generating SRT captions, kinetic pop overlays, scene-cut timestamps, or verifying a cut starts/ends on a word boundary. Always faster-whisper word timestamps or audio cross-correlation — never fraction-based guessing.
---

# Word Sync — Word-Level Timestamps for Caption/Visual Sync

Standing rule (CLAUDE.md §3.2): sync visuals and captions to narration via word-level transcription. Never fraction-based guessing — misaligned captions shipped once from fraction math.

## Procedure

### 1. Transcribe with faster-whisper (canonical config)

Proven identical across `pipeline/_legacy/transcribe_ep02.py`, `long03/02_assets_code/extract_all_words.py`, and `long04/02_assets_code/extract_all_words.py`:

```python
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(
    AUDIO_PATH,
    beam_size=5,
    word_timestamps=True,
    language="en",
)
```

### 2. Write the standard JSON schema

Keep this exact shape — downstream scripts (kinetic pop generators, SRT builders, cut tools) depend on it:

```json
{
  "total_words": 1080,
  "audio_file": "00_AUDIO_....wav",
  "total_duration_s": 425.47,
  "all_words": [{"word": "...", "start": 0.0, "end": 0.32, "probability": 0.98}],
  "all_segments": [{"start": 0.0, "end": 4.5, "text": "..."}]
}
```

(`total_duration_s` must itself come from a probe — see duration-check skill.)

### 3. Fix known mis-transcriptions (spelling dictionary)

Technical terms get mangled by whisper-base. Production corrections from `shorts/short_standalone_ai_ml_engineer_roadmap/generate_voiceover_and_align.py`:

| Misheard | Correct |
|---|---|
| quantral, quantro, kwan-trove | **Quantrove** |
| laura | **LoRA** |
| sicket learn, psychic learn | **Scikit-Learn** |
| number py | **NumPy** |
| infants | **inference** |

Apply per-word and per-segment (regex on segment text) before writing JSON/SRT. Extend the dictionary when a new term appears.

### 4. Generate SRT from word timestamps

Timestamp format `HH:MM:SS,mmm`. For kinetic caption blocks, group **max 3 words per block** (from `pipeline/_legacy/package_all_6_shorts.py::make_kinetic_srt`) — block start = first word start, end = last word end. Typography and styling rules (weights, contrast, pacing) must conform to [.claude/rules/visual-style-standard.md](../../rules/visual-style-standard.md).

### 5. Alternative: cross-correlation (locating known audio inside a master)

When you need where a scene WAV sits inside the master audio — proven in `pipeline/_legacy/align_scenes_in_master.py`:

1. Extract master audio to 16kHz mono: `ffmpeg -y -i <master> -vn -ac 1 -ar 16000 master_mono.wav`
2. Convert the scene WAV to 16kHz mono the same way; normalize both to peak 1.0.
3. Correlate the first 5s of the scene against the master:
   ```python
   corr = scipy.signal.fftconvolve(master_audio, probe[::-1], mode='valid')
   offset_sec = np.argmax(corr) / 16000.0
   ```
4. Scene end = offset + measured scene duration. Write offsets to `scene_offsets.json`.

### 6. Boundary verification (energy check)

Before accepting any cut boundary, extract the cut as 16kHz mono WAV and check mean absolute amplitude in the first and last 0.5s (~8000 samples, from `pipeline/_legacy/verify_cuts.py`). Near-zero energy at either end means clipped syllables or dead air — adjust and re-check.
