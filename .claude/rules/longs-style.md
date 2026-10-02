# Rule: Quantrove Long-Form System (L1–L8 & Visual Standards)

Numbers live in pipeline/config/longs_style.json. If rule text and JSON differ, JSON wins.

## Rules (L1–L8)

- **L1 (Packaging First)**: Research patterns across 5-8 top references, generate >=3 ORIGINAL concepts, never reuse competitor pixels, and lock title + thumbnail before scripting.
  - Config keys: `packaging.research_refs`, `packaging.thumbnail_concepts_min`, `packaging.thumbnail_text_max_words`, `packaging.reuse_competitor_assets`, `packaging.lock_title_and_thumb_before_script`
- **L2 (Hook Discipline)**: First 5s restates the specific click reason and includes >=2 title keywords spoken and visible.
  - Config keys: `hook.window_s`, `hook.must_state_click_reason`, `hook.title_keywords_in_window_min`
- **L3 (Pace Statement & Runtime Integrity)**: State pace mode within 5-20s; promised runtime in minutes must match measured runtime within +/-1 min; voice WPM calibrated to mode (relaxed: 130-145, focused: 150-165).
  - Config keys: `pace.statement_window_s`, `pace.runtime_promise_tolerance_min`, `pace.modes.relaxed`, `pace.modes.focused`
- **L4 (Narrative Architecture)**: Cold open/intro <=35s; 3-5 structured chapters where every chapter delivers a mini-hook, partial payoff, and new loop.
  - Config keys: `structure.intro_max_s`, `structure.chapters`, `structure.chapter_needs`
- **L5 (Loop Ledger Method)**: Maintain a ledger of 4-5 open loops; first partial payoff must occur by 90s; >=2 loops must remain open between 10% and 80% runtime; the primary loop resolves in the final payoff window (80-95%); 100% of loops paid before ending.
  - Config keys: `loops.count`, `loops.first_payoff_max_s`, `loops.min_open_between_pct`, `loops.min_open_count`, `loops.all_paid_by_end`, `loops.final_payoff_window_pct`
- **L6 (Pattern Interrupts)**: Visual or dynamic auditory pattern interrupt occurs at least once every <=40s to maintain viewer retention.
  - Config keys: `structure.pattern_interrupt_max_s`
- **L7 (Disciplined Exit & CTA)**: Exactly ONE spoken CTA starting no earlier than T-45s and ending by T-20s (duration <=25s) combining action + reason + next video; strictly forbidden to ask before the first payoff.
  - Config keys: `cta.window_from_end_s`, `cta.max_s`, `cta.count`, `cta.must_include`, `cta.no_ask_before_first_payoff`
- **L8 (Payoff Fidelity)**: The hook must never promise more than the episode delivers; every claim and data point must be mathematically accurate and thoroughly resolved.
  - Config keys: `packaging.lock_title_and_thumb_before_script`, `loops.all_paid_by_end`

## Visual & Audio Standards (Carry-Overs)

- **Static Frame Ceiling**: No static frame >3.5s unless tagged `HOLD_FOR_UNDERSTANDING` (max 5.0s).
  - Config keys: `visual.static.max_freeze_s`, `visual.static.hold_tag`, `visual.static.hold_max_s`
- **Audio Mix & Bed**: Voice stem normalized to -14 ± 1.5 LUFS; ambient music bed >=16 dB below voice with automatic ducking and no lyrics.
  - Config keys: `visual.audio.voice_lufs`, `visual.audio.voice_tol`, `visual.audio.music_below_voice_db_min`, `visual.audio.music_ducks_under_voice`, `visual.audio.music_lyrics`
- **Typography & Colors**: Font = Nohemi (`font = Nohemi`, fallback Inter). Raisin Black canvas `#202322`, high-contrast Off-White text `#E6EDF3`, Power Lime emphasis `#C3D809`, Pumpkin risk accent `#FD802E`, and Charcoal Slate lines/chrome `#233D4C`. Contrast ratio >=7:1. Max 6 words per on-screen text event, safe margin >=5%. Reads from `brand/brand_tokens.json`.
  - Config keys: `visual.text.font`, `visual.text.font_fallback`, `visual.text.colors`, `visual.text.bg`, `visual.text.ui_structure`, `visual.text.contrast_min`, `visual.text.max_words_per_event`, `visual.text.safe_margin_pct`
- **Motion & End Screen**: Camera push scale <=1.08 with explicit stated purpose (`camera_push_needs_purpose: true`). End-screen final 20s must remain clear of competing focal graphics for YouTube cards (`end_screen_clear_s: 20`).
  - Config keys: `visual.motion.camera_push_max_scale`, `visual.motion.camera_push_needs_purpose`, `visual.end_screen_clear_s`

Kinetic pop-ups continue per kinetic-popups.md; font = Nohemi (fallback Inter).
Layout framing, caption lanes, and safe zones are governed by `pipeline/config/layout_contract.json`. Every video must pass layout_qa before GATE2_READY.
JSON wins over rule text if they differ.
