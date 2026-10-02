---
name: chart-read
description: Systematic multi-timeframe chart reading framework for crypto and equities. Enforces disciplined market structure breakdown (HTF bias, key swing levels, liquidity pools, order blocks/FVGs, invalidation levels, targets) before any trade execution or backtest design.
---

# Systematic Chart Reading Protocol

Mission: Prevent emotional, unanchored chart analysis. Force every market observation into falsifiable technical hypotheses across three distinct timeframes.

## 1. Top-Down Multi-Timeframe Workflow

### Step 1: Higher Timeframe (HTF) — Daily / 4-Hour (The Macro Direction)
- **Macro Trend**: Bullish / Bearish / Consolidating
- **Key Swings**: Mark major Daily swing highs (Buy-side liquidity) and swing lows (Sell-side liquidity).
- **Premium vs. Discount**: Is price currently in the upper 50% (Premium, favorable for shorts) or lower 50% (Discount, favorable for longs) of the macro dealing range?

### Step 2: Intermediate Timeframe (ITF) — 1-Hour / 15-Minute (The Setup)
- **Market Structure Shift**: Did price produce a CHoCH (Change of Character) or BOS (Break of Structure)?
- **Liquidity Sweep**: Has price swept a key previous high/low and rejected aggressively?
- **Imbalance / Fair Value Gap (FVG)**: Identify unfilled price inefficiencies left behind by impulsive moves.

### Step 3: Lower Timeframe (LTF) — 5-Minute / 1-Minute (The Trigger)
- **Confirmation**: LTF shift in direction of HTF thesis.
- **Exact Invalidation**: Place stop-loss where the setup thesis is objectively proven wrong (not an arbitrary dollar amount).
- **Target**: Next major opposing liquidity pool.

## 2. Standardized Chart Note Template

Record chart reads in `03_TRADING_AI/01_JOURNAL/CHART_READS/YYYY-MM-DD_[ASSET].md`:

```markdown
# Chart Read: [ASSET] — YYYY-MM-DD HH:MM UTC

- **Current Price**: $X,XXX
- **HTF Bias (4H/Daily)**: Bullish / Bearish / Neutral
- **Key Range**: High: $X,XXX | Low: $X,XXX | Equilibrium (50%): $X,XXX
- **Recent Liquidity Event**: Swept Asia high / Reclaimed weekly low
- **Bullish Thesis**: If price holds $X,XXX, target $Y,YYY (Invalidation below $Z,ZZZ)
- **Bearish Thesis**: If price loses $X,XXX, target $Y,YYY (Invalidation above $Z,ZZZ)
- **Immediate Action**: Wait for trigger / Setup valid / No edge
```
