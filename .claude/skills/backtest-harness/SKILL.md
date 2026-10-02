---
name: backtest-harness
description: Standardized quantitative backtesting framework in Python for trading rules and crypto/equity strategies. Calculates key institutional metrics (CAGR, Sharpe, Sortino, Max Drawdown, Win Rate, Expectancy, Profit Factor), enforces train/test out-of-sample splits, and checks for lookahead bias and overfitting traps.
---

# Quantitative Backtest Harness

Mission: Provide a standardized, mathematically honest backtesting protocol in `03_TRADING_AI/02_BACKTESTS/`. Prevent the common traps highlighted in Episode 04: lookahead bias, non-stationarity ignorance, and overfitting to historical noise.

## Core Rules

1. **No Lookahead Bias**:
   - Indicator values at bar $t$ must only use information available at or before $t$.
   - Entry orders trigger on bar $t+1$ open (or close of bar $t$ with realistic slippage).
2. **Realistic Frictions**:
   - Always include exchange fee (e.g., 0.05% maker, 0.07% taker for crypto) and estimated slippage (e.g., 0.02% to 0.05%).
3. **Out-of-Sample Discipline**:
   - Strict 70/30 train/test split or rolling walk-forward cross-validation.
   - Strategy parameters optimized ONLY on the in-sample period.

## Standard Python Template

```python
import numpy as np
import pandas as pd

def run_backtest(df: pd.DataFrame, initial_capital: float = 10000.0, fee_rate: float = 0.0006):
    """
    df requires: ['open', 'high', 'low', 'close', 'volume', 'signal']
    signal: 1 (long), -1 (short), 0 (cash)
    """
    # 1. Shift signal by 1 bar to execute on next bar to eliminate lookahead bias
    df['position'] = df['signal'].shift(1).fillna(0)
    
    # 2. Returns calculation
    df['market_ret'] = df['close'].pct_change().fillna(0)
    df['trade_ret'] = df['position'] * df['market_ret']
    
    # 3. Transaction costs
    trades = df['position'].diff().abs().fillna(0)
    df['costs'] = trades * fee_rate
    df['net_ret'] = df['trade_ret'] - df['costs']
    
    # 4. Cumulative Equity Curve
    df['equity'] = initial_capital * (1 + df['net_ret']).cumprod()
    df['peak'] = df['equity'].cummax()
    df['drawdown'] = (df['equity'] - df['peak']) / df['peak']
    
    # 5. Summary Metrics
    total_trades = int(trades.sum() / 2)
    max_dd = df['drawdown'].min()
    total_return = (df['equity'].iloc[-1] / initial_capital) - 1.0
    sharpe = (df['net_ret'].mean() / df['net_ret'].std()) * np.sqrt(365 * 24) if df['net_ret'].std() != 0 else 0
    
    return {
        "Total Return": f"{total_return * 100:.2f}%",
        "Max Drawdown": f"{max_dd * 100:.2f}%",
        "Sharpe Ratio": f"{sharpe:.2f}",
        "Total Roundtrip Trades": total_trades,
    }
```

## Mandatory Reporting Output
Save results to `03_TRADING_AI/02_BACKTESTS/<strategy_name>_report.md` with:
- Summary Metrics Table
- Equity Curve & Drawdown Plot (PNG or ASCII)
- Overfitting Assessment (number of free parameters, in-sample vs out-of-sample degradation).
