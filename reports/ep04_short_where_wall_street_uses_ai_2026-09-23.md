# Report: EP04 Standalone Short — Where Wall Street Actually Uses AI
Date: 2026-09-23
Episode: EP04 Related Standalone Short
Short Slug: ep04_short_where_wall_street_uses_ai
Folder: 01_PROJECTS/YOUTUBE/shorts/[IN_PROGRESS 2026-09-23]_ep04_short_where_wall_street_uses_ai/

## Executive Summary
Created a brand-new standalone short built around EP04's Scene 5 ("Where Wall Street Actually Uses AI").
Rather than extracting footage from the long-form master, this short features:
1. **Fresh Studio Voiceover**: Generated via Gemini TTS (Orus voice) calibrated to 48.05s measured duration.
2. **Brand-New Native 9:16 Manim Animation**: Custom-coded 1080x1920 @ 60fps vertical scenes with CleanText vector typography (Nohemi font) covering:
   - Hook: The Wall Street AI Paradox ($0 spent predicting prices)
   - Retail Illusion vs. Reflexivity Reality
   - The 4 Invisible Optimization Engines sequentially illuminated with live metrics
   - Quantitative Truth Verdict (AI = Optimization Engine, Not a Fortune Teller)
3. **Word-Level Transcription**: 110 words transcribed via faster-whisper.
4. **Unified Text System Captions**: 48 3-4 word chunk subtitles with Nohemi Bold, Off-White (#E6EDF3), Power Lime (#C3D809) emphasis, and Pumpkin (#FD802E) risk styling.
5. **Gate 2 QA**: Passed all automated checks in `shorts_qa.py` (Exit Code 0).

## Measurements & Specifications
- Total Media Duration: 48.050000s (measured via ffprobe)
- First Spoken Word: 0.00s ("Wall")
- First Text Event: 0.05s ("Wall Street")
- Outro Tail: 0.27s (after "teller.")
- Voice Pacing: 138.1 WPM (110 words in 47.8s)
- Audio Stems: Voice (-14 LUFS) mixed with subtle ambient bed (-18 dB)

## Asset Deliverables
1. `TIMELINE_MEDIA/`
   - `01_00m00s_to_00m48s_ep04_short_where_wall_street_uses_ai_audio.wav` (44.1kHz stereo)
   - `01_00m00s_to_00m48s_ep04_short_where_wall_street_uses_ai_manim_9x16.mp4` (Raw Manim render)
   - `01_00m00s_to_00m48s_ep04_short_where_wall_street_uses_ai_raw_9x16.mp4` (Composited audio+video)
2. Root Directory:
   - `ep04_short_where_wall_street_uses_ai_raw_9x16.mp4`
   - `ep04_short_where_wall_street_uses_ai_audio.wav`
   - `render_manim_9x16.py` (Manim script)
   - `exact_word_timestamps.json` (faster-whisper output)
   - `text_events.json` (48 compliant chunk events)
   - `shotlist.json` (4 structured scenes)
   - `ep04_short_where_wall_street_uses_ai_captions.srt` (SRT subtitles)
   - `thumbnail.jpg` (High-contrast 1080x1920 cover frame)
   - `assembly_notes.md` (CapCut styling guide)
   - `metadata.md` (Title, description, tags, pinned comment)

## Automated QA Gate Evaluation
- R1 (Hook): PASS (first_word=0.00s, text_start=0.05s)
- R2 (Static Frame): PASS (no unheld freeze > 3.5s)
- R3 (Audio Mix): WARN (voice -14 LUFS, music bed ducked)
- R4 (Voice WPM): WARN (138.1 WPM, within warn margin)
- R5/R6 (Text System): PASS (48 compliant chunks, Nohemi font)
- R7 (Structure & Length): PASS (extraction / concept length = 48.0s <= 60s)
- R8 (Motion): PASS (valid tags, flow = 0.0%)
- R9 (Clean Ending): PASS (tail = 0.27s, no outro card)
- Brand (Palette & Typography): PASS (5-color palette, Nohemi font)
- R10 (Premium Feel): MANUAL (pending CEO review)
