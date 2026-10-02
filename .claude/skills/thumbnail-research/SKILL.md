---
name: thumbnail-research
description: Empirical packaging research workflow using vidIQ MCP (outliers + similar thumbnails). Analyzes 5-8 top-performing reference videos to deconstruct visual patterns (focal objects, typography, palettes, emotional hooks) and produces 3 original thumbnail concepts in Quantrove's Institutional Data Intelligence aesthetic (Nohemi font, brand_tokens.json palette) before scripting begins.
---

# Thumbnail & Packaging Research Playbook

Standing rule (L1): Packaging research occurs **before scripting begins**. The thumbnail concept and title must be locked before scene writing. "Restyle to our look" strictly means the 5-color Institutional Data Intelligence palette (`#202322`, `#233D4C`, `#C3D809`, `#FD802E`, `#E6EDF3`) and Nohemi typography from `brand/brand_tokens.json`.

---

## 1. Procedure: Empirical Competitive Deconstruction

Use vidIQ (check `vidiq_balance` first; ~5 credits per call):
- `vidiq_outliers(keyword=TOPIC, contentType="long", publishedWithin="sixMonths", limit=12)` gives the top references by breakout score.
- `vidiq_similar_thumbnails` finds visual patterns for a concept description.
- Open specific references in the built-in browser only if the thumbnail image itself must be inspected.

### Reference Collection Standard
Document 5 to 8 high-performing videos in `thumbnail_research.md`:
- Video Title & URL
- View count, upload date, and View/Like ratio (if visible)
- **Extracted Structural Patterns**:
  - **Focal Object**: Central hero visual (e.g. glowing neural network node, collapsing candlestick chart, central bank building).
  - **Text Elements**: Word count (max 3 words per rule), wording style, case.
  - **Color Palette**: Dominant foreground and background tones, contrast ratios.
  - **Emotional Trigger**: Curiosity gap, institutional warning, technical revelation, urgency.

---

## 2. Strict Boundary Rules

- **Pattern Extraction Only**: Deconstruct composition, lighting, and hierarchy.
- **NEVER Download Competitor Assets**: Strictly forbidden to scrape, download, trace, or edit competitor thumbnail images (`packaging.reuse_competitor_assets: false`).
- **Text Length Ceiling**: On-thumbnail copy must be **3 words or fewer** (`packaging.thumbnail_text_max_words: 3`).

---

## 3. Output Requirements (Gate 1 Prerequisite)

Save the findings to `01_PROJECTS/YOUTUBE/longs/<EPISODE_DIR>/thumbnail_research.md` containing:
1. **Reference Matrix Table** (5–8 videos with URLs and pattern breakdowns).
2. **3 Original Thumbnail Concepts** styled strictly in Quantrove's Institutional Data Intelligence aesthetic (`brand/brand_tokens.json`):
   - **Background**: Raisin Black `#202322` with subtle Charcoal Slate `#233D4C` vector grid or depth vignetting.
   - **Accents**: Power Lime `#C3D809` (primary / validation / upward), Pumpkin `#FD802E` (risk / outlier / anomaly), Off-White `#E6EDF3` (titles / text). Zero generic red/green.
   - **Typography**: Clean modern sans-serif `Nohemi` (fallback `Inter`), bold weight (700), max 3 words.
   - **Hero Visual**: Mathematical vector visualization or high-fidelity technical diagram.
3. **Primary Recommendation**: Selected title + thumbnail pair to lock into the script header.
