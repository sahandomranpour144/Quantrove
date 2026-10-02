# Production Plan — Short 03: Why Does the Machine Change Its Price?
## Master Timeline: 50.62s Voiceover

### Visual Concepts
- Inventory tracking in algorithmic market making
- Accumulating +3 units at 00
- Adverse price drift to 9.85 causing inventory risk
- Avellaneda-Stoikov reservation price formula
- Sensitivity to volatility (sigma) and time horizon (T - t)
- Quote skew driven by position exposure, not asset fundamentals

### Scene Breakdown
- **Scene 1 [0.00s - 8.00s]**: AMM inventory HUD. Zero position target.
- **Scene 2 [8.00s - 13.00s]**: Machine buys 3 units at 00. Inventory meter climbs to +3. Balance tilts.
- **Scene 3 [13.00s - 22.20s]**: Stock drops to 9.85. Pumpkin risk warning: unhedged inventory risk.
- **Scene 4 [22.20s - 35.50s]**: Avellaneda-Stoikov model: Reservation price r(s,q) = s - q*gamma*sigma^2*(T-t). Quotes skew downward.
- **Scene 5 [35.50s - 44.00s]**: Volatility spike slider expands penalty; time horizon gauge dynamically recalibrates skew.
- **Scene 6 [44.00s - 50.62s]**: Final contrast: Fundamentals unchanged vs Quote skew driven by exposure. Clean cutoff.
