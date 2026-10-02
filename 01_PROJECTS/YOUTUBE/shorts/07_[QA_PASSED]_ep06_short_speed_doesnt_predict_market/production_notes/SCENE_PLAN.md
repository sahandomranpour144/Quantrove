# Production Plan — Short 02: Speed Doesn't Predict the Market
## Master Timeline: 43.24s Voiceover

### Visual Concepts
- Dual exchange venues (Exchange A vs Exchange B)
- Asymmetric price update & 280µs stale quote window
- Sub-millisecond order packet race
- Price-time priority order book queue (10 machines at same price)
- Microsecond queue fill advantage

### Scene Breakdown
- **Scene 1 [0.00s - 6.00s]**: Dual exchange layout: Exchange A (Carteret) vs Exchange B (Secaucus) at 50.00/50.02.
- **Scene 2 [6.00s - 14.50s]**: Exchange A ticks to 50.05. Exchange B holds stale quote (50.02) during 280µs latency window.
- **Scene 3 [14.50s - 23.80s]**: Fast machine packet ray races across fiber, hits stale 50.02 quote before update. +/usr/bin/bash.03 arb locked.
- **Scene 4 [23.80s - 35.20s]**: Order book queue: 10 identical machines at 50.00 limit price. Queue priority mechanics.
- **Scene 5 [35.20s - 43.24s]**: Machine #1 gets first fill (+100%). Machines #2-#10 unfilled. Delta: 1.4 microseconds. Clean cutoff.
