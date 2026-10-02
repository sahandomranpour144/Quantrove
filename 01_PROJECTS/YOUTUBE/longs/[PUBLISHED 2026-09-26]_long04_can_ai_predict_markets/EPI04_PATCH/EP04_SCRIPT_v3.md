# EP04 Full Scene-by-Scene Production Script (v3 — fact-checked + Long-Form System retrofit)

## "Can AI Actually Predict the Stock Market?"

* **Channel**: Quantrove (@Quantrove)
* **Content Pillar**: 📈 AI + Finance + Trading
* **Packaging title (recommended)**: "Why AI Fails to Predict the Stock Market (And How Quants Win)"
* **Runtime**: master voiceover measured 7:05 (425.5 s) + 20 s end-screen tail = \~7:25
* **Voice**: Gemini AI Studio, "Orus" (all re-recorded segments MUST use the identical voice and settings)
* **pace\_mode**: relaxed (\~138 WPM, target band 130–145)
* **Retention Strategy**: hook restates the click reason in the first 5 s; pace line in the 5–20 s window; first partial payoff (the 50.75% edge) by 90 s; big loop pays at \~88% of runtime; one CTA in the T-45 s → T-20 s window; last 20 s clean for end-screen cards.

### PATCH KEY (what changes vs. the recorded master audio)

* `\[KEEP AUDIO]` = already in the master WAV. Do not touch.
* `\[RE-RECORD #n]` = replace with a new clip of the SAME duration (±0.5 s). Adjust pauses/pace, never add or drop content. Downstream timestamps must not move.
* `\[VISUAL FIX]` = on-screen text/graphics only. No audio change.

|#|Segment|Old audio span|Reason|
|-|-|-|-|
|1|Intro|0:00 → end of "...and mathematicians." (\~35 s)|Hook, pace line, and corrected facts (old text had wrong $42M and an overstated hiring claim)|
|2|Scene 2, two sentences|"In reality, Simons himself admitted..." → "...of the time."|The 50.75% remark is attributed to Robert Mercer, not Simons|
|3|Scene 4, one sentence|"Ninety-five percent of daily price movement is pure noise."|Unsourced statistic (recommended fix; skip only if short on time)|
|4|CTA|405.02 s → 425.26 s (\~20.2 s)|Old CTA called the algorithm video "our next breakdown" (already published) and sat inside the end-screen zone|

\---

### SCENE 1: THE HOOK \& THE SIMONS PARADOX (0:00–\~1:07 measured)

**\[VISUAL FIX — 0:00–\~0:12 hook visual]**: Dark background. A noisy price line drawing continuously (Manim). Large on-screen text at t = 0.0 s: **"Can AI predict the stock market?"** (6 words). No logo, no intro card.

**\[VISUAL FIX — \~0:14 onward, synced to "1988"]**: Cinematic dark room, single glowing terminal. Bold neon-emerald typography: **"≈66% / YEAR BEFORE FEES · 1988–2018"**. Portrait outline of Jim Simons beside a stylized Medallion Fund seal. Camera zooms into: **"$1,000 in 1988 → ≈$21M by 2018 (after fees, reported)"** with a small source line: *Zuckerman, "The Man Who Solved the Market"*. (Replaces the old "$42,000,000" card. Also replaces the invented "AI ACCURACY: 51.2%" flash.)

**\[VISUAL FIX — split-screen flash at the "Yet today..." line]**: Wall Street trading desks with red screens reading **"MOST ACTIVE FUNDS TRAIL THEIR INDEX OVER 15 YEARS — S\&P SPIVA"**.

**\[RE-RECORD #1 — INTRO, replaces the old first \~35 s]**

> Can AI actually predict the stock market? That's what you clicked to find out. The honest answer is mostly no, but the reason is not what most people think.
>
> Get comfortable. This one is worth going slowly.
>
> It starts in 1988, when Jim Simons launched the Medallion Fund, and for three decades it averaged about sixty-six percent a year before fees. He hired physicists, mathematicians, and computer scientists, and deliberately avoided Wall Street traders.

*(74 words. Pace line lands at \~13 s, inside the 5–20 s window. First loop planted at \~8 s.)*

**\[KEEP AUDIO — unchanged]**

> Yet today, across the rest of Wall Street, firms spend billions on deep neural networks and supercomputers to predict stock prices... and the vast majority still fail to beat a simple index fund.
>
> How did a team of mathematicians crack the market with an edge that was barely fifty-one percent, while today's most powerful AI models fail every single day?
>
> Let's look at the real mathematics of why AI cannot predict the stock market the way most people think.

**\[TEXT OVERLAY (Neon Cyan on Dark Charcoal): "Can AI Actually Predict the Stock Market?"]**

\---

### SCENE 2: THE 50.75% EDGE \& THE REFLEXIVITY TRAP (\~1:07–2:15)

**\[VISUAL: Manim animated bell curve. A glowing vertical line sits at exactly 50.75% — just a hair past the 50/50 center. As thousands of micro-trades pulse across the screen, the tiny sliver of edge compounds into a massive green balance. Then transition to a split comparison: Left: Computer vision neural net identifying a cat photo (checkmarks accumulate). Right: Stock market chart where the future price line actively dodges away from the AI's predicted trajectory.]**

**\[KEEP AUDIO]**

> Here is the first great illusion about quantitative trading: people assume Jim Simons built an oracle that predicted the future with ninety percent accuracy.

**\[RE-RECORD #2 — replaces the old two sentences "In reality, Simons himself admitted... of the time."]**

> In reality, Renaissance co-CEO Robert Mercer reportedly said the fund was right only about fifty point seven five percent of the time.

*(22 words, same length as the old pair.)*

**\[VISUAL FIX]**: add a small line under the 50.75% marker: *"Reported by G. Zuckerman, quoting R. Mercer"*.

**\[KEEP AUDIO]**

> Their entire fortune was built on the law of large numbers — executing millions of micro-trades where a tiny probability edge turned into billions of dollars.
>
> But if it's just math and probability, why can't today's generative AI models simply look at decades of price data and do the same thing?
>
> Because markets have a property almost no other prediction problem in computer science possesses: they react to being predicted.
>
> \*\*\[TEXT DEFINITION: "Reflexivity = When an asset's price changes because market participants are acting on a prediction about it." (George Soros / Modern Market Microstructure)]\*\*
>
> Think about how an image recognition AI works. If a neural network learns to identify a cat, the cat does not change its shape because the computer got good at recognizing it.
>
> But the financial market is a competitive, zero-sum game of human and algorithmic participants. If an AI discovers a genuine, profitable pattern that says Apple will rise tomorrow, and traders deploy capital on that signal... their own buying pressure instantly drives the price up today.
>
> The prediction itself erases the pattern. The moment an edge becomes predictable, it self-destructs.

\---

### SCENE 3: PATTERN #1 — THE ALPHA DECAY CURVE (2:15–3:30)  **\[KEEP AUDIO — entire scene]**

**\[VISUAL: Manim animated chart. The vertical axis shows "Excess Profit (Alpha)", horizontal axis shows "Time / Market Adoption". A brilliant neon line starts high at Alpha = +12%. As competing algorithm icons flood the screen, the curve drops steeply along an exponential decay curve down to zero. The word "EQUILIBRIUM" stamps across the flatline.]**

> In quantitative finance, this inevitable self-destruction is known as alpha decay.
>
> \*\*\[TEXT DEFINITION: "Alpha = Excess return earned above the market benchmark through an informational or statistical edge." ]\*\*
>
> In the physical world, gravity doesn't stop working because millions of physicists understand it. But in finance, alpha behaves like an expiring patent.
>
> The second a profitable trading anomaly appears in price data, competing quantitative funds, high-frequency algorithms, and market makers sniff out the same volume spikes.
>
> As hundreds of automated systems rush in to exploit the exact same inefficiency, they crowd the trade. They bid up the entry price, compress the profit spread, and push the market back to mathematical equilibrium.
>
> This is why an AI model that looks brilliant in a backtest can quietly stop making money within four months of going live. It isn't that the code failed. It's that the market adapted around it.

*(Note: the "+12%" on the chart is illustrative. Add a small label: "Illustrative".)*

\---

### SCENE 4: PATTERN #2 — THE OVERFITTING ILLUSION (3:30–4:45)

**\[VISUAL: Manim animated visual. Left side: Historical Data. A hyper-complex, wiggly glowing curve twists and turns to hit every single point on a chaotic chart with a label: "Training Accuracy: 99.8%". Then the timeline advances past the dotted "LIVE TRADING" line. The market moves naturally, while the wiggly curve violently plunges into a deep red drawdown. A red stamp appears: "OVERFITTED TO NOISE".]**
*(Add a small label: "Illustrative".)*

**\[KEEP AUDIO]**

> The second fatal flaw is something every machine learning engineer knows, but almost every retail trader ignores: the overfitting trap.
>
> \*\*\[TEXT DEFINITION: "Overfitting = When a machine learning model memorizes historical noise instead of learning a fundamental, repeatable law." ]\*\*
>
> Stock prices are what statisticians call low signal-to-noise ratio data. On any given Tuesday, a stock price moves due to institutional rebalancing, algorithmic hedging, geopolitical rumors, or random liquidity flows.

**\[RE-RECORD #3 — replaces "Ninety-five percent of daily price movement is pure noise."]**

> Most of any day's price movement is pure noise.

**\[KEEP AUDIO]**

> But modern deep neural networks have millions, sometimes billions, of parameters. If you feed thirty years of noisy price data into a deep learning model, the mathematics guarantees it will find correlations.
>
> It might discover that every time the temperature in Chicago drops by three degrees on a Thursday, semiconductor stocks rally on Friday morning.
>
> In a backtest, the curve looks like a straight line up and to the right. But the moment you connect that model to real capital, it encounters new data it hasn't memorized. And the phantom pattern evaporates immediately.

\---

### SCENE 5: THE 4 ENGINES: WHERE AI ACTUALLY DOMINATES WALL STREET (4:45–6:15)  **\[KEEP AUDIO — entire scene]**

**\[VISUAL: Sleek four-quadrant dashboard lighting up sequentially with clean, glowing data telemetry — no price fortune-telling charts.]**

> So does this mean institutional Wall Street doesn't use AI?
>
> Not at all. Institutional firms spend fortunes on AI. But they don't ask it the naive question: \*"What will Tesla stock trade at tomorrow at noon?"\*
>
> Instead, they deploy AI across four completely different engines:
>
> \*\*\[PANEL 1 LIGHTS UP: 1. Extreme Risk Modeling]\*\*
> Rather than predicting direction, machine learning simulates hundreds of thousands of catastrophic market scenarios — extreme liquidity freezes, interest rate shocks, currency collapses — to calculate the exact probability of portfolio ruin.
>
> \*\*\[PANEL 2 LIGHTS UP: 2. Execution \& Slippage Minimization]\*\*
> When a pension fund needs to buy five billion dollars of stock, placing that order in one block would crash the price against them. Reinforcement learning agents break massive orders into thousands of micro-slices, hiding order flow across dark pools and saving millions in execution costs.
>
> \*\*\[PANEL 3 LIGHTS UP: 3. Real-Time Fraud \& Anomaly Detection]\*\*
> Scanning hundreds of thousands of institutional transactions per second to detect spoofing, wash trading, and unusual order cancellations before regulators even notice.
>
> \*\*\[PANEL 4 LIGHTS UP: 4. Mathematical Portfolio Rebalancing]\*\*
> Given five hundred correlated assets, calculating the mathematically optimal covariance matrix to maximize Sharpe ratio while minimizing volatility.
>
> Notice what all four of these have in common: none of them require predicting the future. They are optimization problems, not crystal balls.

\---

### SCENE 6: THE VERDICT \& THE CTA (6:15–7:05, then 20 s end-screen tail)

**\[VISUAL: The wide four-panel dashboard pulls back into a clean Quantrove visual environment. The original Medallion 50.75% bell curve reappears, fading into the final Quantrove branded card.]**

**\[KEEP AUDIO]**

> If you want to understand the modern intersection of artificial intelligence and finance, remember this fundamental rule:
>
> The stock market is not a puzzle to be solved like chess or protein folding. It is an evolving, reflexive ecosystem of competing intelligences.
>
> The funds that survive long term never search for magic prediction algorithms. They focus on structural speed, disciplined risk control, and microscopic statistical edges compounded across millions of trades — just like Jim Simons did almost forty years ago.

**\[RE-RECORD #4 — CTA, replaces the old "In our next breakdown..." paragraphs. Must be ≤ 20.2 s and start at \~405.0 s]**

> If this changed how you see AI and markets, watch this next: how YouTube's recommendation algorithm actually works, the system that put this video in front of you. And if you want real data and mathematics without the hype, subscribe to Quantrove.

*(45 words. One CTA: action + reason + next video.)*

**\[END-SCREEN TAIL — 20.0 s appended after the last narration]**: no narration, no on-screen text, music bed only, slow ambient Manim motion (no frame static > 3.5 s). Cards appear at the start of the tail: **Subscribe (center) + Next Video: "EP03: How Does The Algorithm Actually Decide What You See?" + Related: "EP02: What 50 Years of Recession Data Actually Show"**.

\---

## LOOP LEDGER (for `loop\_ledger.json`; agent re-measures times from words.json)

|#|Question raised|Planted|Partial payoff|Paid|
|-|-|-|-|-|
|1|How did mathematicians crack the market with a \~51% edge while AI fails?|sentence "How did a team of mathematicians crack the market..."|\~86 s (the 50.75% edge is revealed)|\~375 s (survivors use microscopic edges + risk control)|
|2|Why is the honest answer "mostly no", and why isn't the reason what most people think?|\~8 s (intro)|—|\~135 s (reflexivity)|
|3|Why does a 99%-accurate backtest collapse live?|\~160 s|—|\~205 s|
|4|Why does 30 years of data guarantee false correlations?|\~220 s|—|\~270 s|
|5|Where does Wall Street actually use AI?|\~285 s|—|\~365 s|

## FACT SOURCES (keep for the description / pinned comment)

* Medallion Fund averaged about 66% a year before fees and about 39% after fees over 1988–2018 (widely cited figures from Gregory Zuckerman, *The Man Who Solved the Market*, 2019; reported, not audited).
* After fees, $100 invested in 1988 grew to roughly $2.1M by 2018, so $1,000 → roughly $21M. Before fees, an academic reconstruction (Bradford Cornell) puts $100 at roughly $398M, a 63.3% compound annual rate. (The old script's "$1,000 → $42M" matched neither.)
* "Right 50.75 percent of the time... you can make billions that way" is reported as a remark by Robert Mercer, then Renaissance co-CEO, to a friend. It is not a Jim Simons quote.
* Simons deliberately avoided hiring traditional Wall Street traders and recruited scientists and mathematicians, most of whom knew little about finance. He did not enforce a formal "ban".

