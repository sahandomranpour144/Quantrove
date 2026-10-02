# Rule: Scene Classification (4 Engines)

## What the Rule Is
Every scene must be tagged with exactly ONE approved engine:
- **Manim**: Mathematical, algorithmic, and machine learning mechanics (precise vector rendering).
- **Remotion**: Reusable, parameterized data-driven graphics backed by real data.
- **Google Flow**: Cinematic footage, mood, and atmospheric storytelling (manual generation in `labs.google/flow`).
- **html_motion**: 4–8s terminal/UI-style visual metaphors built as HyperFrames HTML+GSAP compositions rendered locally (skills `hyperframes`, `hyperframes-animation`; manual Vivaldi export = fallback; see [HTML_MOTION_STANDARD.md](../../01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md)).

## Engine Boundaries & Anti-Patterns
- Never render narrative atmosphere in Manim or generate technical data charts with Flow.
- `html_motion` is strictly for 2–8s exact-slot UI/terminal metaphors; never loops; holds final frame; never renders narration keywords (V2 kinetic pop-up overlay owns all keywords).
- Shorts: maximum 1 `html_motion` clip.

## Verification Check
Before proceeding past Gate 1, verify the shot list classification table:

```bash
# Ensure every scene in the script shot list has an explicit tool designation
grep -E "Scene [0-9]+" script_and_shot_list.md | grep -iE "Manim|Remotion|Flow|html_motion"
```
Audit that no chart or numerical concept is tagged for Flow, and no cinematic scene is tagged for Manim.
