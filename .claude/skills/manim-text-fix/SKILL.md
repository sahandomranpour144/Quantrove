---
name: manim-text-fix
description: Enforce native Manim Text() objects with CleanText vector scaling — never raw low-point bold text (the Pango scattering bug producing 'm ar ket') and never manual letter-by-letter positioning. Use when writing or reviewing any Manim scene, fixing scattered/broken text in rendered animations, or porting older scenes to the current CEO-mandated standard.
---

# Manim Text Standard — Native Text() + CleanText Scaling

## The bug (real, recurring)

Manim's Pango rasterizer snaps character glyphs to discrete pixel advances when text renders at small point sizes with `weight=BOLD`. Result: scattered words — `m ar ket` instead of `market`. Manual letter-by-letter positioning (one `Text` per character, positioned by hand) was the bad workaround — it drifts, breaks at scale, and is equally banned. **Both patterns are forbidden.**

## The fix (real production code)

Read from single source of truth in `brand/brand_tokens.json` via `pipeline/manim_theme.py`:

```python
from manim import Text
from pipeline.manim_theme import CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT

# Implementation in pipeline/manim_theme.py:
def CleanText(text, font="Nohemi", font_size=24, color="#E6EDF3", **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    try:
        t = Text(text, font=font, font_size=ref_size, color=color, **kwargs)
    except Exception:
        t = Text(text, font="Inter", font_size=ref_size, color=color, **kwargs)
    t.scale(scale_factor)
    return t
```

Rules:
1. All text via native `Text()` objects rendered at `ref_size=72`, scaled down to target size.
2. Fonts: **Nohemi** (with **Inter** fallback only). Typography and font weight hierarchy follow `brand/brand_tokens.json` (Bold 700 = titles/numbers/key terms, Medium 500 = supporting text).
3. Never `weight=BOLD` on low-point text; never per-character construction loops with manual offsets.
4. Institutional Data Intelligence palette (brand/brand_tokens.json): canvas `#202322`, structural lines/chrome `#233D4C`, primary validation/upward `#C3D809`, risk/downward/outliers `#FD802E`, text `#E6EDF3`. Zero generic red/green. Charcoal Slate is for lines and chrome ONLY, never text.

## Applying to an existing scene

1. Find every `Text(...)` call. Danger zone: `font_size` below ~60 combined with `weight=BOLD`.
2. Find per-letter loops (`for ch in text:` building individual Text mobjects) — replace with a single `Text`/CleanText call.
3. Replace with `CleanText(...)`, preserving the original position/color arguments.
4. Re-render and inspect a frame at 100% zoom — no letter gaps, no scattered words.
5. If the scene feeds a timeline, re-verify runtime after the change (duration-check skill) — text changes can shift animation timing.

## Authority chain

- `.claude/rules/visual-style-standard.md` — Visual Style Standard (Typography, Weights, Pacing)
- `02_KNOWLEDGE/00_CORE/rules/AGENT_RULES.md` §10.1 — Manim Visual Standard
- `02_KNOWLEDGE/00_CORE/knowledge/COMPANY_KNOWLEDGE.md` — failed-strategy record + helper
- `02_KNOWLEDGE/00_CORE/decisions/DECISION_LOG.md` (2026-09-12) — standing company policy
