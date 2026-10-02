# Visual Density Standard v1 (effective EP07)

**Why:** EP06 had 25 scenes over 441 s, one visual every ~17.6 s on average. Manim holds ran 14-30 s with no camera change, and 8 s Flow clips were stretched over 10-12 s of narration. This rule fixes the "lacks motion" feedback. **The palette and brand are unchanged.**

## Hard numbers (checked at Gate 1 shot list and Gate 2)
- **Something visibly changes every 2-4 s; a new shot every ≤6 s.** No frame is static for more than 3 s.
- A *scene* (one engine) is split into **beats** of 3-6 s. Each beat has its own VO word anchor (faster-whisper) in the shot list.
- A 12 min episode has ~35-45 scenes and **≥120 beats**. Gate 1 shot lists list beats, not just scenes.
- Flow clips are never time-stretched. A Flow clip covers ≤8 s of VO; longer spans cut to a second clip or another engine.

## Manim
- Push scale stays ≤1.08 (`longs_style.json`). The stated purpose of a push = guide attention to that beat's focal element.
- Use `MovingCameraScene` / `ThreeDScene` by default. **Every beat has a camera move** (slow push-in 1.00→1.08, pan, or orbit).
- Ambient layer on every scene: slow-drifting `#233D4C` grid at 15-25% opacity plus subtle particle/noise drift. Never a flat empty background.
- Reveal with `LaggedStart`, `TransformMatchingShapes`, and `ValueTracker`-driven counters. Numbers count up; they never pop in.
- Rate functions: `smooth` / `ease_in_out_cubic` only. No linear motion except tickers.

## Remotion (data graphics)
- Every chart, timeline, counter or ranked bar sequence goes to Remotion, not Manim. Use `spring()` with fixed damping per the brand. 16:9 compositions get built during EP07 production.

## html_motion / HyperFrames
- Terminal/UI metaphors become 4-8 s HyperFrames (HTML + GSAP) compositions rendered locally to MP4. Path A manual export is kept as a fallback.

## Transitions and finishing
- Hard cuts stay dominant (>85%). Add **match cuts** (shape/position continuity between engines) at 6-10 chapter points.
- Each chapter opens with a 2-3 s **chapter card** (Remotion; kinetic title on the brand grid).
- Sound design: a whoosh/tick SFX on ≥50% of beat changes (-20 to -24 dBFS), so motion is *heard* as well as seen.

## Gate checks
- Gate 1: the shot list shows the beat count, median beat length (target 4 s), and any beat longer than 6 s with a justification.
- Gate 2: `longs_qa.py` freeze-frame scan flags any >3 s window with <1% pixel change.
