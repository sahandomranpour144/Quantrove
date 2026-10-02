---
name: trade-journal-entry
description: Record structured paper or live trades into 03_TRADING_AI/01_JOURNAL/. Tracks setup date, asset, direction, entry, stop loss, take profit, R-multiple, trade thesis, emotional state, execution score, and post-mortem analysis.
---

# Trade Journal Entry Protocol

Mission: Standardize trade logging in `03_TRADING_AI/01_JOURNAL/` to ensure every executed trade serves as an empirical data point for skill refinement.

## Entry Schema

Every trade entry is saved as a markdown file: `03_TRADING_AI/01_JOURNAL/YYYY-MM-DD_[ASSET]_[LONG/SHORT].md`.

```markdown
# Trade: [ASSET] [LONG/SHORT] — YYYY-MM-DD

- **Asset**: BTCUSDT / ETHUSDT / SOLUSDT / SPY
- **Direction**: LONG / SHORT
- **Session / Time**: NY Open / London / Asia (HH:MM UTC)
- **Account**: Paper / Live

---

## 1. Trade Parameters
- **Entry Price**: $0.00
- **Stop Loss**: $0.00
- **Take Profit (Target)**: $0.00
- **Planned Risk ($R)**: $100 (1% of equity)
- **Risk:Reward (Planned)**: 1:X.X

---

## 2. Technical Thesis & Rules Cited
- **Higher Timeframe Context**: Daily/4H trend and key swing levels
- **Market Structure**: BOS (Break of Structure), CHoCH (Change of Character), Range sweep
- **Liquidity & Imbalance**: Swept buy-side / sell-side liquidity, FVG tapped
- **Rule Checklist**:
  - [ ] HTF alignment
  - [ ] Liquidity pool tapped
  - [ ] Clear invalidation point identified
  - [ ] Minimum 1:2 R:R available

---

## 3. Execution & Psychology
- **Emotional State Before Entry**: Calm / Anxious / FOMO / Impatient
- **Execution Quality (1–5)**: 5 = Followed plan 100%, 1 = Total discretionary impulse
- **Chart Screenshot**: `03_TRADING_AI/01_JOURNAL/screenshots/YYYY-MM-DD_entry.png`

---

## 4. Outcome & Post-Mortem
- **Exit Price**: $0.00
- **Realized R**: +X.X R or -1.0 R
- **What went right?**:
- **What was suboptimal?**:
- **Key Lesson**:
```
