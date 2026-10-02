---
name: shorts-extraction
description: The proven pipeline for cutting vertical 9:16 Shorts from real, already-rendered long-form master video/audio — ffmpeg cut, blur-pad reframe (no cropping of charts), kinetic SRT export for CapCut, and the mandatory raw-cut review gate. Use when a master episode exists and Shorts need pulling from it. Never generates new voiceover/footage — pure cutting of existing media.
---

# Shorts Extraction — Cut From Masters, Don't Generate

Core rule: extraction is pure cutting and reframing of real, pre-existing footage and audio. Do not generate new voiceover, scripts, or footage, and do not use the Remotion shorts generator for extraction tasks.

## Procedure

### 1. Locate master assets

- Master video: `longs/<episode>/Quantrove_EPxx_MASTER/<name>_MASTER.mp4`
- Scene audio: `longs/<episode>/voiceover/generated_audio/`

### 2. Identify exact timestamps (word-level, ms precision)

- Primary: faster-whisper word timestamps on the master (word-sync skill §1–2), then take the passage's first-word start and last-word end.
- Alternative: audio cross-correlation of the scene WAV against the master (word-sync §5).
- Verify boundaries with the energy check (word-sync §6) — no clipped syllables, no dead air.

### 3. Cut + reframe to 9:16 blur-pad (proven command)

From `pipeline/_legacy/cut_shorts_from_master.py`. Never crop data charts, numbers, or labels — the sharp foreground stays native 16:9, blurred fill behind:

```bash
ffmpeg -y -ss <START_SEC> -t <DUR_SEC> -i <MASTER> \
  -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5[bg];[0:v]scale=1080:-1[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" \
  -c:v libx264 -preset slow -crf 18 -r 60 \
  -c:a aac -b:a 192k -movflags +faststart \
  "<slug>_raw_9x16.mp4"
```

Encode settings are production-verified: libx264 slow / CRF 18 / 60fps / AAC 192k / faststart.

### 4. STOP — raw-cut review gate

Save raw outputs (`<slug>_raw_9x16.mp4`, `<slug>_audio.wav`) to `shorts/[IN_PROGRESS] <slug>/draft/`. Report per cut: `start_sec`, `end_sec`, duration, `MM:SS`, plus first/last five words. **Do not add captions, callouts, or CTA until Sahand approves the raw cut.**

### 5. Post-approval: captions + package

- Kinetic SRT from word timestamps, max 3 words per block → `<slug>_captions.srt` (word-sync §4).
- Audio stem: `<slug>_audio.wav`, 44.1kHz stereo (`ffmpeg -i <src> -ac 2 -ar 44100`).
- `assembly_notes.md` (CapCut import instructions, below) and `metadata.md` (title, pinned comment, related-video link back to the parent episode).
- CTA card on the final 2.5–3.0s: "Full Breakdown → Link in Bio / Related Video" with a whoosh swell.

### CapCut import styling (real specs from `shorts/ep01_short_fastest_recovery/assembly_notes.md`)

All typography, font weights, and contrast must adhere to [.claude/rules/visual-style-standard.md](../../rules/visual-style-standard.md):
1. Import the SRT directly onto the subtitle track; select all blocks and style at once.
2. Font: **Nohemi Bold (700)** for emphasis/risk and **Nohemi Medium (500)** for base text (Inter fallback).
3. Text color: Off-White (`#E6EDF3`) base, Power Lime (`#C3D809`) keyword emphasis, Pumpkin (`#FD802E`) risk words on Raisin Black (`#202322`) background. Zero yellow fill boxes.
4. Animation: Fade blur-up entrance with hard-cut exit per `shorts_style.json`.
5. Position: center X, lower-third Y (~**1300px** on the 1920 canvas — clear of the Shorts UI buttons).

## Output structure per Short

```
shorts/[IN_PROGRESS] <slug>/
├── <slug>_raw_9x16.mp4      ← step 3
├── <slug>_audio.wav         ← matching audio stem
├── <slug>_captions.srt      ← step 5 (kinetic, 3-word blocks)
├── assembly_notes.md        ← CapCut styling handoff
└── metadata.md             ← title, pinned comment, related link
```
