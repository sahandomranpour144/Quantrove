# EP05 Production Phase 1 Report: Script Expansion, Voiceover & Timing Anchoring
**Date**: September 23, 2026  
**Episode**: EP05 — *Why "Free" Trading Isn't Free*  
**Pillar**: 3 — Finance & Trading, Simplified  
**Folder**: `01_PROJECTS/YOUTUBE/longs/[IN_PROGRESS 2026-09-23]_long05_market_making_illusion/`  
**Status**: [IN_PROGRESS 2026-09-23]  

---

## 1. Executive Summary & Deliverables Completed
1. **Script Expanded to ~5:00**:
   - Total spoken words: 807 words.
   - Narrative flow expanded with relatable real-world examples (airport currency exchange booth, buying 50 AAPL shares on lunch break, losing $2/order compounding to hundreds).
   - Spoken line calibrated: *"in the next five minutes, I'll show you..."*
2. **Title Refined (5 Words) & Thumbnail Alignment**:
   - Title: **Why "Free" Trading Isn't Free** (5 words).
   - Thumbnail Text: **`$0 ISN'T FREE`** (3 words, Nohemi Bold, Power Lime on Raisin Black).
   - Hook Alignment (00:00–00:05): Spoken line *"free trading isn't free"* matches title, thumbnail, and on-screen pop (`FREE → ISN'T FREE`) per Rule L2.
3. **Master Voiceover Generated & Normalized**:
   - Engine: Gemini TTS (`gemini-3.1-flash-tts-preview`, Voice: Orus).
   - Measured Duration (`ffprobe`): **337.12s (05m 37s)**.
   - Normalization: -14.0 LUFS EBU R128 broadcast standard.
   - Output File: `TIMELINE_MEDIA/00_00m00s_to_05m37s_ep05_master_voiceover.wav`.
4. **Exact Word-Level Timestamp Extraction**:
   - Engine: Local `faster-whisper` (base model, CPU int8).
   - 807 individual words timestamped down to millisecond precision.
   - Outputs: `voiceover/ep05_exact_word_timestamps.json`, `02_assets_code/ep05_exact_word_timestamps.json`, `01_scripts/ep05_transcript.srt`.
5. **3 Google Flow Video Prompts (Fintech YouTube Aesthetic)**:
   - Clip 01 (Scene 04): Data center high-frequency server corridor (`labs.google/flow`).
   - Clip 02 (Scene 07): Institutional trading floor at dusk overlooking financial skyline.
   - Clip 03 (Scene 12): Top-down macro shot of phone trade confirmation on matte desk.
   - Documented in: `01_scripts/FLOW_VIDEO_PROMPTS.md`.
6. **Timeline & Assembly Guide Synchronized**:
   - All 12 scenes calibrated with exact measured timestamps from `ffprobe` in `01_scripts/VISUAL_SHOT_LIST.md` and `01_scripts/CAPCUT_FINAL_ASSEMBLY_GUIDE.md`.

---

## 2. File Index
- Master Voiceover: `TIMELINE_MEDIA/00_00m00s_to_05m37s_ep05_master_voiceover.wav`
- Scene Audio Stems: `voiceover/generated_audio/scene01_hook.wav` through `scene12_cta_outro.wav`
- Word Timestamps: `voiceover/ep05_exact_word_timestamps.json`
- SRT Subtitles: `01_scripts/ep05_transcript.srt`
- Expanded Script: `01_scripts/EP05_SCRIPT.md`
- Calibrated Shot List: `01_scripts/VISUAL_SHOT_LIST.md`
- Flow Video Prompts: `01_scripts/FLOW_VIDEO_PROMPTS.md`
- CapCut Assembly Guide: `01_scripts/CAPCUT_FINAL_ASSEMBLY_GUIDE.md`
- Refined Metadata: `03_metadata/upload_metadata.md`
