# Quantrove Brand Style Guide: Institutional Data Intelligence

> **Single Source of Truth**: This document and [`brand/brand_tokens.json`](brand_tokens.json) define the visual language for all Quantrove assets across long-form episodes, Shorts, thumbnails, Manim scenes, and motion overlays.

---

## 1. Core Aesthetic

**"Institutional Data Intelligence"** — Bloomberg-terminal precision.
- **Data Density**: High information density structured with mathematical rigor.
- **Interface Feel**: Clean UI wireframes, calibrated coordinate grids, telemetry readouts.
- **Discipline**: Statistical rigor, strict hierarchical layout.
- **Zero Fluff**: No decorative flair, no generic stock imagery, no rounded cartoonish shapes, no generic hype graphics.

---

## 2. Color Palette (Exact HEX Only)

The brand uses an exclusive 5-color palette. No external colors are permitted in generative or programmed assets (imported live-action/documentary B-roll footage excepted).

| Token | Hex | Name / Designation | Semantic Role & Application |
|---|---|---|---|
| `BACKGROUND` | `#202322` | Raisin Black | All canvases, video backgrounds, card surfaces, letterboxing. |
| `UI_STRUCTURE` | `#233D4C` | Charcoal Slate | Grid lines, panel dividers, coordinate axes, bracketed tags (e.g. `[ML/AI]`), interface chrome. **Lines and chrome ONLY — never text.** |
| `SUCCESS` | `#C3D809` | Power Lime | Primary accent: positive validation, active predictions, upward price moves, convergence lines, keyword emphasis. |
| `RISK` | `#FD802E` | Pumpkin | Secondary accent: anomalies, statistical outliers, targets, high-risk indicators, downward price moves, risk keywords. |
| `TEXT` | `#E6EDF3` | Off-White | All text, numbers, typography, headings, and wordmarks. |

---

## 3. Strict Color Rules

1. **No Generic Red / Green Anywhere**:
   - Candlesticks, chart lines, vectors, and directional arrows MUST NOT use standard green (`#00FF00`, `#00FFA3`, `#22C55E`) or standard red (`#FF0000`, `#FF3366`, `#DC2626`).
   - **Upward Moves / Bullish / Validated** = Power Lime (`#C3D809`).
   - **Downward Moves / Bearish / Risk / Anomalies** = Pumpkin (`#FD802E`).

2. **Charcoal Slate Restriction**:
   - `#233D4C` has a low contrast ratio (~1.39:1) against the canvas background (`#202322`).
   - **It is strictly prohibited for body text, titles, subtitles, or captions.**
   - It is reserved exclusively for structural elements: subtle grid lines, axis spines, tick marks, card borders, and telemetry brackets.

3. **Text & Accent Hierarchy**:
   - Primary narrative text: Off-White (`#E6EDF3`).
   - Keyword emphasis: Power Lime (`#C3D809`).
   - Risk / anomaly callouts: Pumpkin (`#FD802E`).

---

## 4. Typography: Nohemi

The Quantrove primary typeface is **Nohemi**, backed by a two-tier weight discipline.

- **Primary Font**: `Nohemi` (stored in [`assets/fonts/`](../assets/fonts/))
- **Fallback Font**: `Inter` (used ONLY if Nohemi fails to load)

### Two-Tier Weight Rule

| Weight | Numeric | Semantic Role | Applied Color |
|---|---|---|---|
| **Bold** | `700` | Titles, KPI metrics, numbers, formula tokens, key terms, kinetic pops | `#E6EDF3` (Off-White) or `#C3D809` (Lime) / `#FD802E` (Pumpkin) |
| **Medium** | `500` | Supporting text, body captions, axis labels, subtitles, secondary telemetry | `#E6EDF3` (Off-White) |

*Note*: Never use a weight lighter than Medium (`500`) on screen to preserve legibility on mobile viewports.

---

## 5. System Integrations

All automated tools, QA evaluators, and rendering scripts read tokens directly from [`brand/brand_tokens.json`](brand_tokens.json):
- **Shorts Configuration**: [`pipeline/config/shorts_style.json`](../01_PROJECTS/YOUTUBE/pipeline/config/shorts_style.json)
- **Longs Configuration**: [`pipeline/config/longs_style.json`](../01_PROJECTS/YOUTUBE/pipeline/config/longs_style.json)
- **Remotion Shorts Engine**: `01_PROJECTS/YOUTUBE/pipeline/remotion_engine/`
- **Manim Theme Module**: `01_PROJECTS/YOUTUBE/pipeline/manim_theme.py`
- **Automated QA Gates**: [`shorts_qa.py`](../01_PROJECTS/YOUTUBE/pipeline/qa/shorts_qa.py) & [`longs_qa.py`](../01_PROJECTS/YOUTUBE/pipeline/qa/longs_qa.py)
