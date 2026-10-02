# Rule: Quantrove Shorts Style System (R1–R10)

Numbers live in pipeline/config/shorts_style.json. If rule text and JSON differ, JSON wins.

## Rules

- **R1 (Hook)**: Value/question spoken AND on screen within first 3s; first word <0.5s; no logo/intro.
  - Config keys: `hook.first_word_max_s`, `hook.text_at_s`, `hook.window_s`
- **R2 (Static Frame Ceiling)**: No static frame >3.5s (tagged HOLD_FOR_UNDERSTANDING max 5s).
  - Config keys: `static.max_freeze_s`, `static.hold_tag`, `static.hold_max_s`
- **R3 (Audio Mix & Ducking)**: Music low, ducked under voice, no lyrics; voice ~-14 LUFS, music >=16 dB below.
  - Config keys: `audio.voice_lufs`, `audio.voice_tol`, `audio.music_below_voice_db_min`, `audio.music_below_voice_db_target`, `audio.music_ducks_under_voice`, `audio.music_lyrics`
- **R4 (Pacing & Delivery)**: Calm/precise/premium; voice 145-160 wpm, 0.3-0.5s pauses between ideas, no hype words.
  - Config keys: `voice_wpm.target`, `voice_wpm.warn_margin`, `chunk.break_on_pause_s`
- **R5+R6+R10 (Unified Text System & Premium Polish)**: One text system only. 3-4 word chunks ARE the captions. No separate full captions, no separate pop-up keywords on Shorts. Style/animation exactly per shorts_style.json and brand/brand_tokens.json (Nohemi font with Inter fallback; Off-White #E6EDF3 text, Power Lime #C3D809 emphasis, Pumpkin #FD802E risk, Raisin Black #202322 bg, Charcoal Slate #233D4C lines/chrome).
  - Config keys: `font`, `font_fallback`, `weights`, `tracking_em_headline`, `colors`, `text_effects`, `size_pct_frame_height`, `chunk`, `animation`, `badge`
- **R7 (Narrative Architecture)**: Structure IDEA -> SIMPLE_WRONG -> COMPLEX_WRONG -> INSIGHT, 30-45s, native Shorts only; extractions must pick a segment that already contains a reveal.
  - Config keys: `structure.beats`, `structure.length_s`, `structure.applies_to`
- **R8 (Motion Discipline)**: Manim-first continuous math-style motion; camera push <=1.08 scale only with a stated purpose; Flow clips atmosphere only, <=20% runtime; html_motion max 1 clip per Short (2–8s, terminal/UI metaphor, holds final frame; see `01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md`).
  - Config keys: `motion.tags`, `motion.camera_push_max_scale`, `motion.camera_push_needs_purpose`, `motion.flow_max_pct_of_runtime`
- **R9 (Clean Exit)**: Clean ending: cut <=1.0s after last spoken word; no CTA, no outro card; last frame = insight visual.
  - Config keys: `ending.max_tail_after_last_word_s`, `ending.forbidden_words`, `ending.no_outro_card`
- **R10 (Human Verification)**: Qualitative feel review evaluated via Gate 2 Shorts QA inspection.
  - Config keys: `text_effects`, `animation`, `colors`

Layout framing, stage band, and text safe box are governed by `pipeline/config/layout_contract.json`. Every video must pass layout_qa before GATE2_READY.
