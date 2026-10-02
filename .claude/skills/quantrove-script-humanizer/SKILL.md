---
name: quantrove-script-humanizer
description: Transform raw or draft YouTube scripts into gripping documentary narration. Eliminates generic AI clichés, enforces problem-led storytelling (Human Question -> Mystery -> Data Reveal -> Consequence), and sharpens curiosity while preserving mathematical and quantitative accuracy.
---

# Quantrove Documentary Script Humanization Playbook

The **Quantrove Script Humanizer** is the mandatory bridge between an initial script draft and Gate 1 CEO review. Its single goal is to elevate all narration from sounding like an AI assistant answering a prompt into the voice of an experienced, investigative documentary writer uncovering a hidden mathematical or institutional reality.

---

## 1. Role in the Production Lifecycle & Gate 1 Prerequisite

```
[Phase 1: Topic Research]
       ▼
[Phase 2: Narrative Architecture & Loop Ledger]
       ▼
[Phase 3: Initial Director Script Draft]
       ▼
[★ HUMANIZATION PASS (quantrove-script-humanizer)] ◄── THIS SKILL
  ├─ Pass 1: AI Cliché & Pattern Detection
  ├─ Pass 2: Documentary Section-by-Section Rewrite
  ├─ Pass 3: Believability & Curiosity Audit
  └─ Pass 4: Humanization Package & Change Manifest
       ▼
[🛑 GATE 1: CEO APPROVAL (Sahand)]
       ▼
[Phase 4: Asset Production (Manim / Flow / Voiceover)]
```

### Locked Boundaries (Non-Negotiable)
When running the humanizer workflow, never violate these standing constraints:
- **Preserve Rules L1–L8**: Retain hook timing (<= 5s window with >= 2 title keywords), pace statement template (5–20s), chapter count (3–5), loop ledger tracking (`loop_ledger.json`), single CTA window (T-45s to T-20s), and end-screen clearance (final 20s).
- **Preserve Quantitative Rigor**: Never round, modify, or drop validated numbers, equations, historical dates, or source citations.
- **Preserve Media Sync & Budget**: Stay within target word count budgets (e.g. ~1,000–1,800 words, ±5%) and maintain designated Manim / Flow scene boundaries.
- **Preserve Brand Palette & Tone**: No hype, no get-rich-quick sensationalism, no generic red/green terminology. Maintain Institutional Data Intelligence neutrality.

---

## 2. The 7 Documentary Humanization Rules

### Rule 1: Banish Generic AI Language & Tropes
Eliminate sterile, formulaic LLM buzzwords and boilerplate connectors. 

**Strictly Forbidden AI Vocabulary**:
- ❌ *"In today's world"* / *"In our modern world"* / *"In a world where"*
- ❌ *"rapidly evolving"* / *"ever-changing"* / *"fast-paced"*
- ❌ *"landscape"* (e.g., *"the financial landscape"*, *"the AI landscape"*)
- ❌ *"revolutionary"* / *"game-changing"* / *"groundbreaking"*
- ❌ *"it is important to understand"* / *"it's crucial to note"* / *"vital to remember"*
- ❌ *"delve into"* / *"dive into"* / *"unpack"* / *"explore"*
- ❌ *"testament to"* / *"tapestry"* / *"beacon"* / *"pivotal role"*

**Documentary Replacement Principle**:
Anchor immediately to physical objects, specific dates, mechanical actions, or tangible market frictions.
- *Before*: "In today's rapidly evolving financial landscape, algorithmic trading plays a pivotal role."
- *After*: "On October 19, 1987, fifty-four automated trading systems at the New York Stock Exchange began selling S&P 500 futures at the exact same millisecond."

---

### Rule 2: Documentary Storytelling Chapter Quad
Every chapter must move through a 4-part narrative progression:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 1. HUMAN        │ ──► │ 2. MYSTERY /    │ ──► │ 3. DATA         │ ──► │ 4. CONSEQUENCE  │
│    QUESTION     │     │    PROBLEM      │     │    REVEAL       │     │    & MEANING    │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

1. **Human Question**: A question grounded in real incentives, fear, greed, or curiosity.
   *Example*: *"Why would the world's most sophisticated hedge fund completely ban Wall Street traders from its trading floor?"*
2. **Mystery / Problem**: A paradox or friction where standard intuition collapses.
   *Example*: *"Standard financial theory says market movements follow a Gaussian bell curve. If that's true, the 2008 crash was an event that should occur once every four billion years."*
3. **Data Reveal**: The hard empirical proof, historical tape, or mathematical equation that answers the mystery.
   *Example*: *"When Benoit Mandelbrot plotted seventy years of cotton prices on a logarithmic scale, the distribution wasn't normal. The tails were fat, stubborn, and mathematically predictable."*
4. **Consequence & Meaning**: What this structural truth changes for capital, institutions, or the viewer.
   *Example*: *"This means Wall Street's primary risk equations weren't just slightly inaccurate; they were systematically blind to the exact events that bankrupt banks."*

---

### Rule 3: Increase Curiosity & Tension
Never state a conclusion before generating an unanswered question. Replace textbook causal statements with suspenseful investigative pivots.

- ❌ *Textbook Causal Statement*:
  > *"The stock market crash happened because portfolio insurance algorithms triggered a cascade of automated sell orders."*
- ✅ *Documentary Curiosity Pivot*:
  > *"But something strange appears when we look at every crash together: the selling didn't start with human panic. It started with a mathematical rule specifically designed to prevent it."*

- ❌ *Textbook Transition*:
  > *"Next, we will look at how order books work."*
- ✅ *Documentary Tension Transition*:
  > *"To see why this model failed, we have to look at the one place retail traders almost never look: the millisecond order queue inside the matching engine."*

---

### Rule 4: Human Investigative Observer Voice
The narrator must not sound like a detached lecture slide or an encyclopedia. The voice is that of an **investigative researcher** who has spent months analyzing the raw trade tape and is showing the viewer what they found.

**Phrasing Techniques**:
- *"Notice what happens to the spread the moment the large order hits the book."*
- *"On paper, the equation looked bulletproof. But inside the exchange servers..."*
- *"If you pull the raw tick data from that morning, a bizarre pattern emerges."*
- *"This isn't an accident. It's the intended mechanics of the protocol."*

---

### Rule 5: Anti-Textbook Architecture
Completely eliminate the academic lecture pattern.

| ❌ AVOID (Textbook Lecture) | ✅ PREFER (Documentary Narrative) |
|---|---|
| **1. Definition**: *"Reflexivity is defined as..."* | **1. Problem**: *"A computer vision model identifies a cat, and the cat doesn't react. But when an AI predicts a stock price, the price vanishes."* |
| **2. Explanation**: *"This occurs because traders act on signals..."* | **2. Unexpected Pattern**: *"Every time a proprietary signal is turned on, its profitability begins to decay along a steep downward curve."* |
| **3. Example**: *"For example, if Apple stock is predicted to rise..."* | **3. Data Reveal**: *"Plotting alpha decay across 10,000 quantitative strategies reveals an average half-life of just fourteen days."* |
| *(Passive ending)* | **4. Meaning**: *"The prediction doesn't forecast the future; it actively burns the anomaly out of existence."* |

---

### Rule 6: Preserve Quantitative Rigor & Neutrality
Humanization does NOT mean sensationalism, dumbing down, or editorializing.
- **Keep Exact Math**: Preserve percentages, dollar amounts, formulas, and statistical margins (e.g. *50.75%*, *22.6%*, *R-squared*, *VaR*).
- **Keep Attribution**: Name original papers, mathematicians, institutional reports, and regulatory filings.
- **Maintain Neutrality**: Zero get-rich-quick claims, zero hype, zero financial advice. Frame as institutional system analysis.

---

### Rule 7: Zero Fabrication (Strictly Grounded)
A documentary writer is constrained by historical reality.
- **Never Invent Personal Anecdotes**: Do NOT write *"When I was trading back in 2018..."* or *"I remember the panic when..."*.
- **Never Invent Emotions**: Avoid theatrical hyperbole (*"Everyone was weeping on the floor"* unless documented in historical records).
- **Never Fabricate Motives**: Attribute institutional behavior to mathematical rules, regulatory mandates, and structural incentives—not fictional villains.

---

## 3. The 4-Pass Humanization Execution Workflow

When invoked on a draft script, execute these four passes sequentially:

### Pass 1: AI Cliché & Pattern Detection (Diagnostic)
1. Scan script text against the banned AI phrase index.
2. Flag all passive "Definition → Explanation" structures.
3. Identify low-tension transitions (*"Next, let's look at..."*, *"In addition..."*).
4. Verify all quantitative claims and title keywords are intact.

### Pass 2: Documentary Section-by-Section Rewrite (Transformation)
1. **Cold Open**: Ensure hook states the paradox/click promise in <= 5s, delivers 2 title keywords, and applies the calibrated pace statement (Mode A: relaxed, Mode B: focused).
2. **Chapters**: Restructure each chapter into the Chapter Quad:
   - Human Question
   - Mystery / Problem
   - Data Reveal
   - Consequence & Meaning
3. **Dialogue / Narration Pacing**: Break long academic sentences into punchy spoken phrases (average < 15 words/sentence).
4. **Curiosity Bridges**: Add high-tension investigative transitions between scenes.

### Pass 3: The Believability & Quality Audit
Evaluate against the core question:
> *"Would an intelligent viewer believe this documentary was written by a veteran financial investigative journalist, or does it smell like ChatGPT?"*

Checklist:
- [ ] Are 100% of generic AI cliches eradicated?
- [ ] Does every chapter follow Problem/Mystery -> Data Reveal -> Consequence?
- [ ] Does the narrator sound like an observer examining evidence?
- [ ] Are all numbers, calculations, and historical citations preserved exactly?
- [ ] Is there zero invented personal experience or fake emotion?
- [ ] Does the script comply with L1–L8 rules from `longs_style.json`?

### Pass 4: Final Output Package Delivery
Present the humanized deliverable with three distinct components:
1. **The Humanized Script**: Complete production-ready script with `[VISUAL]`, `[NARRATION]`, and `[AUDIO CUE]` tags.
2. **Manifest of Major Transformations**: Before-and-after breakdown of key sections showing how AI boilerplate was replaced with documentary storytelling.
3. **Weak Sections & Risk Register**: Flag any scenes where data was sparse or where CEO editorial judgment is recommended.

---

## 4. Before & After Reference Table

| Raw / AI Draft Pattern | Humanized Documentary Pattern |
|---|---|
| *"In today's fast-paced financial markets, algorithmic trading has become increasingly important."* | *"Inside the server racks in Secaucus, New Jersey, human judgment has been completely removed from the trade loop."* |
| *"Market makers provide liquidity by buying and selling stocks, which reduces volatility."* | *"Market makers don't take risks out of benevolence. They sell you liquidity when you don't need it, and vanish the microsecond panic strikes."* |
| *"It is crucial to understand that backtests often suffer from overfitting."* | *"Run a quantitative model through enough historical data, and you can mathematically prove that buying stocks on a full moon produces a 400% Sharpe ratio."* |
| *"The flash crash occurred due to a complex interaction of trading algorithms."* | *"At 2:32 PM on May 6, 2010, an algorithm placed a sell order for 75,000 contracts. Within thirty-six minutes, one trillion dollars evaporated."* |

---

## 5. Gate 1 Review Submission Template

Before submitting to Sahand (CEO) for Gate 1 approval, append this humanization validation stamp:

```markdown
### 🛡️ Humanization Quality Validation
- **Banned AI Tropes**: 0 detected (100% purged)
- **Documentary Quad**: Verified across all Chapters (Human Question -> Mystery -> Data Reveal -> Consequence)
- **Curiosity Mechanics**: Verified (all chapter transitions use investigative pivots)
- **Quantitative Fidelity**: 100% preserved (all metrics, dates, and citations verified)
- **Narrator Persona**: Investigative observer (zero personal fabrication)
- **Gate 1 Status**: READY FOR CEO REVIEW
```
