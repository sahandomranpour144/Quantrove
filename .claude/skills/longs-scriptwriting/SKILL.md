---
name: longs-scriptwriting
description: Master framework for Quantrove long-form video scripting. Enforces hook discipline, pace-phrase templates, loop-ledger retention mechanics, 3-5 chapter structures, and disciplined single-CTA exits against longs_style.json.
---

# Long-Form Scriptwriting Playbook

Every Quantrove long-form episode script must adhere to the narrative engineering standards defined in `.claude/rules/longs-style.md` and parameter thresholds in `01_PROJECTS/YOUTUBE/pipeline/config/longs_style.json`.

---

## 1. Hook Formula (First 5 Seconds)

The viewer clicked for a specific reason (title + thumbnail promise). The first 5 seconds must immediately validate that click:
- **Rule**: Must state the specific question or paradox within 5 seconds (`hook.window_s: 5`).
- **Keyword Requirement**: Must contain at least **2 primary keywords** from the video title (`hook.title_keywords_in_window_min: 2`).
- **Anti-Pattern**: No channel branding, no logo animations, no generic "Hello guys", no slow philosophical wind-up.

---

## 2. Pace Statement Templates (5–20 Seconds)

Between second 5 and second 20, the script must explicitly anchor viewer pacing expectations using one of two calibrated modes:

### Mode A: Relaxed (Deep Dive / Historical / Architectural)
- **Target WPM**: 130–145 WPM
- **Mandatory Template**:
  > *"Get comfortable, this one is worth going slowly."*
- **Purpose**: Signals to the viewer that deep nuance, historical diagrams, and foundational proofs are coming, preventing early impatience.

### Mode B: Focused (System Breakdown / Tactical / Urgent)
- **Target WPM**: 150–165 WPM
- **Mandatory Template**:
  > *"In the next {N} minutes, I will show you exactly {promise}."*
- **Precision Rule**: `{N}` must be within **±1 minute** of the real measured runtime (`pace.runtime_promise_tolerance_min: 1`). Never estimate or guess `{N}` before media is measured.

---

## 3. Loop-Ledger Retention Method

To sustain 50%+ retention across 10–30 minute documentaries, write with an explicit **Open Loop Ledger** (`loop_ledger.json`):
1. **Target Count**: Maintain 4–5 nested open narrative loops (`loops.count: [4, 5]`).
2. **Early Payoff Rule**: The first partial payoff must occur by 90 seconds (`loops.first_payoff_max_s: 90`).
3. **Overlap Rule**: Between 10% and 80% of video runtime, at least **2 loops must remain open simultaneously** (`loops.min_open_count: 2`). As soon as one loop pays off, plant a new one immediately.
4. **Primary Payoff**: The biggest core loop (the video's central question) must pay off in the **80%–95% window** (`loops.final_payoff_window_pct: [80, 95]`).
5. **Resolution**: 100% of open loops must be completely paid before the end of the episode (`loops.all_paid_by_end: true`).

```json
[
  {
    "id": 1,
    "question": "Why did the 1987 portfolio insurance algorithms trigger a liquidity vacuum?",
    "planted_at_s": 12.0,
    "paid_at_s": 540.0,
    "payoff_type": "primary_insight"
  }
]
```

---

## 4. Chapter Architecture (3–5 Chapters)

Every episode consists of an intro (<= 35s) and 3 to 5 distinct chapters (`structure.chapters: [3, 5]`):

### Chapter Triad Requirement
Every single chapter must deliver three components:
1. **Mini-Hook**: Opening 10–15 seconds of the chapter raising a localized tension point.
2. **Partial Payoff**: Answers a piece of a previous loop with concrete mathematical or empirical proof.
3. **New Loop**: Plants the next tension point before transitioning to the next chapter.

### Pattern Interrupts
- Every **<= 40 seconds**, introduce a visual, structural, or auditory pattern interrupt (Manim camera push, animated data re-sort, sound design accent, or dramatic pause).

### Scene Engine Classification (Gate 1 Requirement)
Every scene in the director shot list must be tagged with exactly ONE approved engine:
1. **Manim**: Mathematical, algorithmic, and ML mechanics (precise vector animations).
2. **Remotion**: Parameterized, reusable data-driven charts and metrics.
3. **Google Flow**: Cinematic footage and atmospheric storytelling (manual `labs.google/flow`).
4. **html_motion**: 4–8s terminal/UI visual metaphors placed at the **Data Reveal beat** of the Chapter Quad. Exact-slot (2–8s), play once `t=0..N`, hold final frame (`>=0.5s`), no loops. Keywords remain strictly on the V2 kinetic pop-up overlay. Full prompt standard and layout contract integration in [HTML_MOTION_STANDARD.md](../../01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md).

---

## 5. Disciplined Exit & CTA Template

Quantrove episodes maintain Institutional Data Intelligence authority by avoiding desperate creator asks:
- **Placement**: Exactly **ONE spoken CTA** starting no earlier than **T-45s** and ending by **T-20s** (`cta.window_from_end_s: [45, 20]`).
- **Duration**: Maximum **25 seconds** (`cta.max_s: 25`).
- **Timing Rule**: Strictly forbidden to make any audience ask before the first payoff has landed (`cta.no_ask_before_first_payoff: true`).
- **Triad Content**: Must contain **Action + Reason + Next Video**:
  > *"If you want to understand how algorithmic order flow exploits this exact pattern, watch our breakdown on institutional liquidity right here."*
- **End-Screen Window**: The final 20 seconds (`T-20s` to `T`) must remain designated with `end_screen_safe: true` and zero on-screen text, leaving the frame clear for native YouTube end-screen cards (`visual.end_screen_clear_s: 20`).

---

## 6. Documentary Script Humanization Pass (Mandatory Before Gate 1)

Every initial script draft must pass the 4-pass documentary humanization workflow (`quantrove-script-humanizer`) before submission to Sahand for Gate 1 approval:
- **Rule 1 (Banish AI Cliches)**: Completely purge LLM boilerplate ("in today's world", "rapidly evolving", "landscape", "revolutionary", "it is important to understand", "delve into"). Anchor immediately in dates, mechanical actions, and physical exchange infrastructure.
- **Rule 2 (Chapter Quad)**: Structure every chapter through the 4-part progression: Human Question → Mystery / Problem → Data Reveal → Consequence & Meaning.
- **Rule 3 (Curiosity-Driven Pacing)**: Replace dry causal explanations ("The crash happened because...") with tension-driven investigative pivots ("But something strange appears when we look at every crash together...").
- **Rule 4 (Investigative Observer Voice)**: Narrator speaks as a researcher uncovering system mechanics alongside the audience, not a detached textbook lecturer.
- **Rule 5 (Anti-Textbook Flow)**: Strictly reject "Definition → Explanation → Example". Enforce "Problem → Unexpected pattern → Data reveal → Meaning".
- **Rule 6 (Quantitative Fidelity)**: Keep 100% of mathematical formulas, statistical edges, percentages, dates, and citations intact.
- **Rule 7 (Zero Fabrication)**: Strictly forbidden to invent personal experiences, fake emotional anecdotes, or unfounded conspiracy theories.
- **Audit Gate**: Before Gate 1, provide the humanization report (0 AI tropes detected, Chapter Quad verified, change log manifest).

---

## 7. Visual Style & "Restyle to Our Look" Standard

Whenever instructed to "restyle to our look" or styling scenes, scripts, and overlays, strictly apply `brand/brand_tokens.json`:
- **Aesthetic**: "Institutional Data Intelligence", Bloomberg-terminal precision. High data density, clean UI wireframes, statistical rigor, clear hierarchy. No decorative flair, no generic stock imagery.
- **Palette (Exact HEX Only)**:
  - `BACKGROUND` (`#202322` Raisin Black): all canvases and backgrounds.
  - `UI_STRUCTURE` (`#233D4C` Charcoal Slate): grid lines, panel dividers, bracketed tags like `[ML/AI]`, interface chrome. Lines and chrome ONLY, never text.
  - `SUCCESS` (`#C3D809` Power Lime): primary accent (positive validation, active predictions, upward moves, convergence lines, keyword emphasis).
  - `RISK` (`#FD802E` Pumpkin): secondary accent (anomalies, outliers, targets, high-risk indicators, downward moves).
  - `TEXT` (`#E6EDF3` Off-White): all text, numbers, and wordmarks.
- **Rules**:
  - No generic red/green anywhere (charts, candles, arrows). Up = Lime (`#C3D809`), down/risk = Pumpkin (`#FD802E`).
  - Charcoal Slate is for lines and chrome ONLY, never text (low contrast).
- **Typography**:
  - Primary: `Nohemi` (stored in `assets/fonts/`).
  - Fallback: `Inter` (only if Nohemi fails to load).
  - Weight hierarchy: Bold (700) = titles, numbers, key terms; Medium (500) = supporting text.
- **Text Color Scheme**:
  - Off-White (`#E6EDF3`) for body and headings.
  - Power Lime (`#C3D809`) for keyword emphasis.
  - Pumpkin (`#FD802E`) only for risk/anomaly words.

