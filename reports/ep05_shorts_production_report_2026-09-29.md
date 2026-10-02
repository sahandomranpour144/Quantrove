# EP05 Shorts Package Production & Selection Report
**Date**: 2026-09-29  
**Parent Long-Form Video**: EP05 — *Why "Free" Trading Isn't Free (The Market Making Illusion)* (ID: `-SH2kNLF3WA`)  
**Content Pillar**: Finance Simplified / AI + Finance  
**Aesthetic Standard**: Institutional Data Intelligence (`#202322`, `#233D4C`, `#C3D809`, `#FD802E`, `#E6EDF3`; Nohemi font)  
**QA Engine**: `pipeline/qa/shorts_qa.py` (Rule R1–R10 Automated Audit)  

---

## 1. Topic Selection Scoring Evaluation (100-Point Framework)

Applied the 6-dimension scoring framework from `topic_strategy/QUANTROVE_TOPIC_STRATEGY.md` (Curiosity 25%, Narrative 20%, Data 15%, Visual 15%, Educational 15%, Evergreen 10%):

| Candidate Short | Topic / Premise | Pillar | C | S | D | V | E | L | Total Score | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| **Native 1** | Where Your $0 Trade Actually Goes | Finance Simplified | 9.2 | 9.5 | 9.0 | 9.5 | 9.0 | 9.0 | **92.25** | Greenlit (Exceptional) |
| **Native 2** | The 2-Cent Drag ($1,000 Loss) | Finance Simplified | 9.5 | 9.5 | 9.5 | 9.5 | 9.5 | 9.0 | **94.50** | Greenlit (Exceptional) |
| **Standalone 1** | Why Wall Street Loves "Dumb Money" | AI + Finance | 9.4 | 8.5 | 9.0 | 9.0 | 9.5 | 9.5 | **91.25** | Greenlit (Exceptional) |
| **Standalone 2** | Airport Currency Booth Trap (Spread) | Finance Simplified | 8.0 | 8.5 | 9.0 | 8.5 | 8.5 | 9.0 | **85.00** | Greenlit (Strong) |
| *Alt Standalone* | What NBBO Actually Means | Finance Simplified | 6.5 | 8.0 | 8.5 | 7.0 | 8.0 | 8.5 | 76.25 | Rejected (Weak curiosity) |

---

## 2. Extracted Shorts (2 from EP05 Master Media)

### Extract #1: `ep05_short_pfof_kickback`
- **Source**: `TIMELINE_MEDIA/06_02m11s_to_02m47s_pfof_kickback_revenue_chart.mp4` + `00_...ep05_master_voiceover.wav`
- **Measured Time Window**: 131.80s – 167.04s (`02:11.80` to `02:47.04`)
- **Measured Duration**: `35.25s` (ffprobe verified: 35.250000s)
- **First Word**: "So" at `0.16s` (< 0.5s) | **Hook Text**: `0.05s` (< 0.1s)
- **Hook**: "So why do market makers want your retail trades so badly?"
- **Core Insight**: PFOF reverse pipeline & Robinhood $200M/qtr revenue bar eruption
- **9:16 Treatment**: Cinematic blur-pad (1080x608 centered on 1080x1920) with frame-indexed continuous camera push (`zoompan=z=1.0+0.05*(on/2115)`); 0 static freezes detected.
- **QA Status**: PASS (`pipeline/qa/shorts_qa.py`)

### Extract #2: `ep05_short_65m_penalty`
- **Source**: `TIMELINE_MEDIA/07_...flow_institutional_trading_floorREAL.mp4` (3.46s) + `07_...sec_65m_penalty_settlement.mp4` (29.66s) + `00_...ep05_master_voiceover.wav`
- **Measured Time Window**: 166.50s – 200.16s (`02:46.50` to `03:20.16`)
- **Measured Duration**: `33.67s` (ffprobe verified: 33.666667s)
- **First Word**: "If" at `0.18s` (< 0.5s) | **Hook Text**: `0.05s` (< 0.1s)
- **Hook**: "If market makers are paying brokers, who ends up paying the bill?"
- **Core Insight**: The 2020 SEC $65M settlement proving worse execution prices; customer receipt flip.
- **9:16 Treatment**: Concat Flow B-roll (10.3%) + Manim vector (89.7%) in 1080x1920 blur-pad with continuous camera push; 0 static freezes detected.
- **QA Status**: PASS (`pipeline/qa/shorts_qa.py`)

---

## 3. Native Shorts (2 Vertical 1080x1920 Manim Renders)

### Native #1: `ep05_short_where_trade_goes`
- **Topic**: Where Your $0 Trade Actually Goes (The Wholesale Routing Pipeline)
- **Score**: 92.25/100
- **Structure (4-Beat)**:
  - `IDEA` (0.0–8.0s): Phone app order initiation ("When you tap buy...")
  - `SIMPLE_WRONG` (8.0–16.5s): Blocked public NYSE barrier gate
  - `COMPLEX_WRONG` (16.5–25.5s): Retail broker node takes zero inventory risk
  - `INSIGHT` (25.5–35.0s): Wholesale internalizers (Citadel/Virtu) + reverse PFOF kickback
- **Insight Badge**: `WHOLESALE INTERNALIZERS`
- **Measured Duration**: `35.00s` | **Voice WPM**: `155.2 WPM` (88 words in 34.0s)
- **Render Engine**: Native Manim Community 1080x1920 @ 60fps (`render_scene.py`) + calibrated -14.0 LUFS audio
- **QA Status**: PASS (`pipeline/qa/shorts_qa.py`)

### Native #2: `ep05_short_the_2_cent_drag`
- **Topic**: The 2-Cent Drag: How Free Trading Steals $1,000 (The Compounding Penny)
- **Score**: 94.50/100
- **Structure (4-Beat)**:
  - `IDEA` (0.0–7.5s): Split price cards: Public Best Bid ($150.00) vs App Fill ($150.02)
  - `SIMPLE_WRONG` (7.5–16.0s): Math equation: $0.02 x 100 shares = -$2.00 ("Basically free")
  - `COMPLEX_WRONG` (16.0–24.5s): 1999 $19.95 ticket vs invisible compounding
  - `INSIGHT` (24.5–35.0s): 500-trade lifetime grid turning Pumpkin, -$1,000.00 loss tally
- **Insight Badge**: `SILENT COMPOUNDING`
- **Measured Duration**: `35.00s` | **Voice WPM**: `148.2 WPM` (84 words in 34.0s)
- **Render Engine**: Native Manim Community 1080x1920 @ 60fps (`render_scene.py`) + calibrated -14.0 LUFS audio
- **QA Status**: PASS (`pipeline/qa/shorts_qa.py`)

---

## 4. Standalone Shorts (2 Independent Concept Renders)

### Standalone #1: `ep05_short_why_dumb_money_prized`
- **Topic**: Why Wall Street Loves "Dumb Money" (Adverse Selection & Uninformed Flow)
- **Score**: 91.25/100
- **Independent Premise**: Completely self-contained explanation of adverse selection in market microstructure — why HFTs pay for retail flow and avoid hedge fund flow.
- **Structure (4-Beat)**:
  - `IDEA` (0.0–7.5s): Multi-billion dollar HFTs paying to trade with beginners
  - `SIMPLE_WRONG` (7.5–15.5s): Debunking front-running retail predictions
  - `COMPLEX_WRONG` (15.5–23.5s): Debunking directional market bets (Zero inventory risk)
  - `INSIGHT` (23.5–35.0s): Adverse selection comparison: Toxic Institutional (98%) vs Safe Retail (0%)
- **Insight Badge**: `UNINFORMED FLOW`
- **Measured Duration**: `35.00s` | **Voice WPM**: `148.1 WPM` (84 words in 34.0s)
- **Render Engine**: Native Manim Community 1080x1920 @ 60fps (`render_scene.py`) + calibrated -14.0 LUFS audio
- **QA Status**: PASS (`pipeline/qa/shorts_qa.py`)

### Standalone #2: `ep05_short_airport_currency_trap`
- **Topic**: The Airport Currency Booth Trap (What the Bid-Ask Spread Actually Is)
- **Score**: 85.00/100
- **Independent Premise**: Intuitive universal entry point for viewers who have never traded stocks. Compares airport 0% fee exchange kiosks with stock market spread harvesting.
- **Structure (4-Beat)**:
  - `IDEA` (0.0–7.5s): 0% commission airport currency booth taking $100 bill
  - `SIMPLE_WRONG` (7.5–15.5s): Expecting Google market rate (1 USD = 0.90 EUR)
  - `COMPLEX_WRONG` (15.5–23.5s): Receiving 82 EUR and assuming government tax
  - `INSIGHT` (23.5–35.0s): Bid/Ask spread profit bracket ($0.95 sell vs $0.85 buy = $0.10 spread)
- **Insight Badge**: `SPREAD GAP`
- **Measured Duration**: `35.00s` | **Voice WPM**: `155.2 WPM` (88 words in 34.0s)
- **Render Engine**: Native Manim Community 1080x1920 @ 60fps (`render_scene.py`) + calibrated -14.0 LUFS audio
- **QA Status**: PASS (`pipeline/qa/shorts_qa.py`)

---

## 5. Strategic Check & Topic Scoring History Audit
1. **Was the scoring method previously applied to decisions already made for EP01–EP05?**
   - **Answer**: PARTIAL / RETROACTIVELY DOCUMENTED.
   - **Details**: The 6-dimension 100-point scoring framework (`QUANTROVE_TOPIC_STRATEGY.md`) was formally codified and enacted on 2026-09-29. In `Quantrove_Topic_Database.xlsx` (via `build_topic_database.py`), EP01–EP05 (QT-001 to QT-005) have retroactively populated scores (e.g., QT-005 scored 90.5/100). However, at the time EP01–EP05 production greenlights were made (August–September 2026), they were selected via the 2-Month Master Roadmap and the historical 5-part arc (*Money → Markets → Algorithms → AI → Speed*), prior to the formal scoring engine's existence.
2. **What did applying the framework change for EP05 Shorts?**
   - Filtered out low-curiosity technical topics (e.g. "What is NBBO?", which scored 76.25 and was rejected).
   - Validated that both Standalone candidates (Adverse Selection and Currency Booth Spread) clear the strict 80.0+ threshold (91.25 and 85.00), preventing filler.
3. **Season-Wide Topic Decisions**:
   - Zero season-wide decisions made. Season 1 remains OPEN (~10–15 episodes, minimum 3 longs per pillar) per CEO Decision 2026-09-29. Season Boundary Review will be triggered exclusively by Sahand.
