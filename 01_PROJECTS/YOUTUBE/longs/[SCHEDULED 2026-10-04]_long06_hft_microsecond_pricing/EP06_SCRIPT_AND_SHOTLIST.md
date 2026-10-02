# EP06 — How HFT Algorithms Price Spreads in Microseconds
Slug: `long06_hft_microsecond_pricing` | Topic: QT-009 | Pillar: AI + Finance + Trading
Status: **GATE 1 — AWAITING CEO APPROVAL** (no asset generation before approval)

## 0. Production parameters
- Title (7 words, 48 chars): **How HFT Algorithms Price Spreads in Microseconds**
- Pace mode: **A (Relaxed)** — template line is inside Scene 1. Target 130–145 WPM. No runtime number is spoken, so no {N} to fix later.
- Narration ≈ 1,115 words → ≈ 8:20–8:50 narration + 20s end screen ≈ **8:40–9:10 total** (inside 8–12 min).
- Voiceover: Sahand supplies ElevenLabs audio. Adjust ElevenLabs speed until measured WPM is 130–145.
- Engines: Manim 16 scenes, html_motion 4 clips (32s ≈ 6%), Flow 5 clips (40s ≈ 8%). Remotion: not used (16:9 compositions not built yet).
- Kinetic keywords: **existing CleanText kinetic overlay (Track V2) — NOT Remotion.** Keywords below are cues only; the agent aligns them to word timestamps (words.json).
- Palette lock (only these): `#202322 #233D4C #C3D809 #FD802E #E6EDF3`. Nohemi, Inter fallback. Lime = up/positive, Pumpkin = risk/loss.
- Callbacks: EP04 (Simons tiny edge) in Scene 21. No callbacks to EP03. Outro does not tease a next topic.

## 1. Loop ledger (4–5 open loops)
| ID | Question planted | Planted | Paid |
|---|---|---|---|
| L1 (central) | How can machines price spreads in microseconds and lose money on one day in 1,238? | Scene 1 | Scene 21 (~87% of runtime) |
| L2 | Why does a spread exist at all? | Scene 3–4 | Scene 5 (first payoff, ≈ 1:25) |
| L3 | Who decides how cheap the spread may get? | Scene 7 | Scenes 8–10 |
| L4 | If price cannot compete, what do machines compete on? | Scene 11 | Scenes 18–20 |
| L5 | What if the next buyer knows more than the machine? | Scene 16 | Scene 19 |

## 2. Shot list (one engine per scene)
| Scene | Engine | Asset ID | Slot (target) | Chapter beat |
|---|---|---|---|---|
| 1 | Flow | F1_DATA_HALL | 8s | Hook + pace line |
| 2 | Manim | M01_GRID_1238 | 15s | Hook proof |
| 3 | html_motion | HM1_TWO_PRICES | 8s | Ch1 Human Question |
| 4 | Manim | M02_ZERO_COST | 20s | Ch1 Mystery |
| 5 | Manim | M03_ADVERSE_SELECTION | 25s | Ch1 Data Reveal |
| 6 | html_motion | HM2_PRICE_JUMPS | 8s | Ch1 Data Reveal |
| 7 | Flow | F2_TRADING_FLOOR | 8s | Ch1 Consequence |
| 8 | Manim | M04_TICK_HISTORY | 30s | Ch2 Question + Reveal |
| 9 | Manim | M05_SEC_SPREAD_DROP | 18s | Ch2 Data Reveal |
| 10 | Manim | M06_PINNED_SPREAD | 22s | Ch2 Problem |
| 11 | Flow | F3_FIBER_PULSES | 8s | Ch2 Consequence |
| 12 | Manim | M07_INVENTORY_RISK | 20s | Ch3 Question |
| 13 | Manim | M08_RESERVATION_PRICE | 30s | Ch3 Mystery/Reveal |
| 14 | html_motion | HM3_QUOTE_LEANS | 8s | Ch3 Data Reveal |
| 15 | Manim | M09_SPREAD_FORMULA | 20s | Ch3 Data Reveal |
| 16 | Manim | M10_REPRICE_SHAPE | 28s | Ch3 Consequence |
| 17 | Flow | F4_EMPTY_DESK | 8s | Ch4 Question |
| 18 | Manim | M11_MICROSECOND_LIGHT | 22s | Ch4 Mystery |
| 19 | html_motion | HM4_STALE_QUOTE_RACE | 8s | Ch4 Data Reveal |
| 20 | Manim | M12_QUEUE_LINE | 18s | Ch4 Data Reveal |
| 21 | Manim | M13_VIRTU_PAYOFF | 38s | Ch4 Reveal + central payoff |
| 22 | Manim | M14_BOTH_SIDES | 30s | Ch4 Consequence |
| 23 | Manim | M15_FINAL_INSIGHT | 20s | Close |
| 24 | Flow | F5_PULLBACK | 8s | CTA (T-45s..T-20s) |
| 25 | Manim | M16_END_SCREEN_BG | 20s | End screen, zero text, music only |

Slots are targets. After the voiceover exists, the agent re-times Manim scenes to the narration. Flow and html_motion clips keep their fixed length; if narration runs up to 4s longer, the next scene's visual starts at the clip end (J-cut).

---

## 3. Script

### INTRO

**Scene 1 — Engine: Flow (F1_DATA_HALL)**
[VISUAL] Slow dolly down a dark server aisle. Hook text appears on frame 1 via the overlay.
[NARRATION] "How do HFT algorithms price spreads in microseconds? One firm did it for five years, and lost money on exactly one day. Get comfortable, this one is worth going slowly."
[AUDIO] Low pulse bed fades in under the first word. No logo, no intro.
KEYWORDS: HFT ALGORITHMS | MICROSECONDS | 1 LOSING DAY

**Scene 2 — Engine: Manim (M01_GRID_1238)**
[VISUAL] 1,238 cells fill left to right; one turns orange.
[NARRATION] "That record is not a rumor. It sits in a 2014 SEC filing from a firm called Virtu: 1,238 trading days, one losing day. Start with the thing it sells. The spread."
[AUDIO] Soft tick per row. Accent on the orange cell.
KEYWORDS: 1,238 DAYS | SPREAD

### CHAPTER 1 — THE BET INSIDE EVERY SPREAD

**Scene 3 — Engine: html_motion (HM1_TWO_PRICES)**
[VISUAL] Bid and ask panels with the one-cent gap bracketed.
[NARRATION] "Look at any stock and you will see two prices. You buy at the higher one, the ask. You sell at the lower one, the bid. The gap between them is the spread, and it looks like a toll."
[AUDIO] Sparse clicks on each tick.
KEYWORDS: ASK | BID | SPREAD

**Scene 4 — Engine: Manim (M02_ZERO_COST)**
[VISUAL] Three zeros stack, then a question mark where the spread should vanish.
[NARRATION] "So why does the gap exist at all? In 1985, two economists, Lawrence Glosten and Paul Milgrom, took every cost out of the picture. No fees. No overhead. A market maker, a firm that quotes both a buy price and a sell price, expecting to earn exactly zero."
[AUDIO] Beat of silence after "exactly zero."
KEYWORDS: ZERO COSTS | MARKET MAKER

**Scene 5 — Engine: Manim (M03_ADVERSE_SELECTION)**
[VISUAL] Informed vs uninformed traders hit the ask; the price moves only after the informed one.
[NARRATION] "The gap did not disappear. Their model still produced a spread, for one reason. Some of the traders hitting a quote know something the market maker does not. Maybe they saw news a fraction earlier. Maybe they saw the price move on another exchange. So every time someone buys at the ask, the machine has to wonder: did they buy because the price is about to rise?"
[AUDIO] Low accent on "know something."
KEYWORDS: ADVERSE SELECTION | INFORMED TRADERS

**Scene 6 — Engine: html_motion (HM2_PRICE_JUMPS)**
[VISUAL] Buy at 100.01, then the price jumps ten cents; the old ask turns orange.
[NARRATION] "Slow it down. A machine quotes a sell price of one hundred dollars and one cent. Someone buys. Then the price jumps ten cents. It just sold to someone who knew."
[AUDIO] Sharp accent on the jump.
KEYWORDS: STALE QUOTE | -0.10

**Scene 7 — Engine: Flow (F2_TRADING_FLOOR)**
[VISUAL] Archive-style trading floor, no readable text.
[NARRATION] "So a spread is not a toll. It is insurance, priced one trade at a time. And for decades, the rulebook decided how cheap that insurance was allowed to get."
[AUDIO] Warm low swell, then cut.
KEYWORDS: INSURANCE | THE FLOOR

### CHAPTER 2 — THE FLOOR

**Scene 8 — Engine: Manim (M04_TICK_HISTORY)**
[VISUAL] Step chart of the minimum price move: 12.5¢, 6.25¢, 1¢.
[NARRATION] "Who decides how small a spread can be? The smallest price move allowed is called the tick. Until June 1997 on the New York Stock Exchange, it was one eighth of a dollar: twelve and a half cents. Then one sixteenth: six and a quarter cents. On January 29, 2001, it became one cent. On a fifty-dollar stock, that is the difference between a floor of 0.125 percent of the price, and 0.02."
[AUDIO] Accent on each step down.
KEYWORDS: TICK | 6.25¢ | 1¢

**Scene 9 — Engine: Manim (M05_SEC_SPREAD_DROP)**
[VISUAL] Two bars falling: NYSE and Nasdaq quoted spreads.
[NARRATION] "The result was immediate. SEC staff reported that quoted spreads on NYSE stocks narrowed by an average of 37 percent, and on Nasdaq stocks by about 50. Cheaper for investors. The firms making those markets reported lower trading revenues."
[AUDIO] Two descending tones.
KEYWORDS: -37% NYSE | -50% NASDAQ

**Scene 10 — Engine: Manim (M06_PINNED_SPREAD)**
[VISUAL] Bid 100.00 / ask 100.01 locked; dashed half-cent gap marked as not allowed; then a half-cent level appears.
[NARRATION] "Then came a stranger problem. For the most heavily traded stocks, the SEC concluded the penny itself had become the constraint. Quotes that could have been tighter were not allowed to be. In 2024 it adopted a half-cent tick for those stocks, though the start date has been pushed back more than once."
[AUDIO] Constrained, tight pulse.
KEYWORDS: TICK-CONSTRAINED | HALF-CENT

**Scene 11 — Engine: Flow (F3_FIBER_PULSES)**
[VISUAL] Parallel fiber strands, light pulses racing.
[NARRATION] "When the floor binds, nobody wins by cutting price. So the contest moves. To who is first in line. And first in line is a question of time."
[AUDIO] Pulse bed rises.
KEYWORDS: FIRST IN LINE

### CHAPTER 3 — THE FORMULA BEHIND THE QUOTE

**Scene 12 — Engine: Manim (M07_INVENTORY_RISK)**
[VISUAL] Units stack into an INVENTORY box while a price path wobbles.
[NARRATION] "So how does a machine choose where to quote? In 2008, Marco Avellaneda and Sasha Stoikov published a model for exactly this. It starts with a problem every market maker has. If you buy, you now own risk. And a market maker would rather own nothing."
[AUDIO] Light tension tone.
KEYWORDS: INVENTORY | 2008

**Scene 13 — Engine: Manim (M08_RESERVATION_PRICE)**
[VISUAL] r = s − q·γ·σ²·(T − t), built term by term with plain-language tags.
[NARRATION] "Their first move is to stop trusting the middle price. Instead, the machine uses a reservation price: the middle, minus a penalty for the inventory it holds. The penalty grows with how much it holds, how much the price jumps around, which is volatility, and how much time is left in the day. And with a number for how much the machine hates risk."
[AUDIO] Soft tick per term.
KEYWORDS: RESERVATION PRICE | VOLATILITY

**Scene 14 — Engine: html_motion (HM3_QUOTE_LEANS)**
[VISUAL] Three buys; reservation price and both quotes step down.
[NARRATION] "Say a stock sits at one hundred dollars. The machine buys three units. With textbook parameters, its reservation price falls to ninety-eight eighty. Both quotes slide down with it. It is trying to get rid of what it just bought."
[AUDIO] Three small accents, one per buy.
KEYWORDS: 98.80

**Scene 15 — Engine: Manim (M09_SPREAD_FORMULA)**
[VISUAL] Spread = risk term + competition term; 0.40 + 1.29 = 1.69; "TEXTBOOK PARAMETERS — NOT A REAL QUOTE".
[NARRATION] "The spread has two parts. One grows with volatility. The other shrinks when customers would walk away if the quote got wider. With the same textbook numbers, they add up to about a dollar sixty-nine. Not a real quote. A shape."
[AUDIO] Resolve tone on 1.69.
KEYWORDS: TEXTBOOK NUMBERS

**Scene 16 — Engine: Manim (M10_REPRICE_SHAPE)**
[VISUAL] Inventory steps move the reservation price; the bid-ask band shifts with it; a question mark appears over "who is buying?".
[NARRATION] "The numbers are not the point. The shape is. The machine does not hold one price. It reprices every time its inventory or the risk changes. Later papers treat this model as the starting point for inventory-based high-frequency trading. It is a simplification. But there is one input it cannot know: whether the next buyer knows more than the machine does."
[AUDIO] Held tone on the last sentence.
KEYWORDS: REPRICE

### CHAPTER 4 — WHAT A MICROSECOND BUYS

**Scene 17 — Engine: Flow (F4_EMPTY_DESK)**
[VISUAL] Empty desk at night, soft unreadable monitor glow.
[NARRATION] "Which leads to the last question. Why does any of this need to happen in microseconds? Because a quote is only correct for as long as nothing changes."
[AUDIO] Clock-like tick, very quiet.
KEYWORDS: MICROSECONDS

**Scene 18 — Engine: Manim (M11_MICROSECOND_LIGHT)**
[VISUAL] A ruler in meters; two light pulses race: vacuum reaches 300 m, fiber reaches about 200 m in the same microsecond.
[NARRATION] "A microsecond is one millionth of a second. In that time, light travels about three hundred meters in a vacuum, and about two hundred in glass fiber. Picture two machines, one a few hundred meters closer to the exchange. When news moves the price, one of them hears it first."
[AUDIO] Single high ping on the finish.
KEYWORDS: 1 MICROSECOND | 200 M IN FIBER

**Scene 19 — Engine: html_motion (HM4_STALE_QUOTE_RACE)**
[VISUAL] Two lanes: fast quote pulled, slow quote filled at the old price.
[NARRATION] "Stocks trade on many venues at once. A price move on one is news on all the others. If a machine's quote is stale for even a moment, someone faster buys it at the old price. That is adverse selection again, now measured in microseconds."
[AUDIO] Cut sound on the pulled quote; hit sound on the stale fill.
KEYWORDS: STALE QUOTE | ADVERSE SELECTION

**Scene 20 — Engine: Manim (M12_QUEUE_LINE)**
[VISUAL] Orders at one price form a line numbered by arrival; an incoming order fills from the front.
[NARRATION] "And when every machine quotes the same price, the order book becomes a line. On most exchanges, orders at the same price fill in the order they arrived. The first in line gets filled first. Speed is how you get to the front."
[AUDIO] Soft thud per fill.
KEYWORDS: PRICE-TIME PRIORITY | QUEUE

**Scene 21 — Engine: Manim (M13_VIRTU_PAYOFF)**
[VISUAL] The 1,238-day grid returns. Overlay: small spread captures + instant hedge arrows. Then a seeded illustrative simulation of many tiny edges averaging out.
[NARRATION] "Which brings us back to Virtu. Its filing credited that record to real-time risk management. It described a market-neutral approach: it does not need prices to rise or fall. It needs to be paid a little, over and over, while hedging each position almost the instant it takes it on. When an edge is that small and repeated that many times, luck averages out. It is the same arithmetic as the tiny edge in the Simons story."
[AUDIO] Payoff swell, resolves on "averages out."
KEYWORDS: MARKET NEUTRAL | HEDGE | LAW OF LARGE NUMBERS

**Scene 22 — Engine: Manim (M14_BOTH_SIDES)**
[VISUAL] Left card: Knight Capital, August 2012. Right card: critics' view vs the filing's view.
[NARRATION] "Speed cuts both ways. In August 2012, a technology failure at Knight Capital cost the firm about 460 million dollars in a single trading day. And when Virtu's record became public, critics read it as proof that high-speed traders hold an unfair advantage. This video cannot settle that argument. What the data shows is where the edge comes from: pricing risk, and arriving first."
[AUDIO] Low, neutral bed. No stinger.
KEYWORDS: KNIGHT CAPITAL 2012 | UNFAIR ADVANTAGE?

### CLOSE

**Scene 23 — Engine: Manim (M15_FINAL_INSIGHT)**
[VISUAL] A one-cent spread bar with three inputs feeding it: inventory, volatility, odds you know more. Microsecond counter ticks. This is the insight frame.
[NARRATION] "So the next time you see a spread of one cent, do not read it as a fee. Read it as an answer. A machine weighed its inventory, the volatility, and the chance that you know more than it does. And it priced that doubt before you finished clicking."
[AUDIO] Music resolves.
KEYWORDS: AN ANSWER | PRICED DOUBT

**Scene 24 — Engine: Flow (F5_PULLBACK)**
[VISUAL] Slow pull-back from the data hall into darkness. CTA window.
[NARRATION] "If you want to see what happens when these machines pull their quotes, watch why free trading isn't free next, in the Finance Simplified playlist."
[AUDIO] Music bed only after the CTA ends. CTA must end by T-20s.
KEYWORDS: none

**Scene 25 — Engine: Manim (M16_END_SCREEN_BG)**
[VISUAL] Clean `#202322` with a faint `#233D4C` grid. **Zero text.** End-screen safe, 20s.
[NARRATION] none. [AUDIO] Music bed only.
KEYWORDS: none

---

## 4. Manim specs (for the agent; CleanText engine, 1920x1080, 60fps, palette lock)
| Asset | Content | Numbers / labels |
|---|---|---|
| M01 | 62-column grid of 1,238 cells (19 full rows + 60); fill lime row by row; one cell turns orange at an arbitrary position | "1,238 TRADING DAYS", "JAN 2009 – DEC 2013", "Source: Virtu Financial S-1 (2014)"; small tag "POSITION ILLUSTRATIVE" |
| M02 | Stack: FEES = 0, OVERHEAD = 0, EXPECTED PROFIT = 0, then SPREAD = ? pulsing | "Glosten & Milgrom (1985)" |
| M03 | Market-maker node center; two traders feed it; informed trader's buy is followed by an upward price move; the quote band must cover the expected loss | Lime = uninformed, Orange = informed |
| M04 | Step chart of minimum tick (NYSE): 12.5¢ until 24 Jun 1997, 6.25¢ until 29 Jan 2001, 1¢ after | Second panel: 6.25¢ = 0.125% of a $50 price; 1¢ = 0.02%. Source: UK Government Office for Science tick-size review; SEC staff speech (2001) |
| M05 | Two bars: NYSE quoted spreads −37% (average), Nasdaq −50% (average) | Footnote: effective spreads NYSE about −15%. Source: SEC staff speech, 8 Jun 2001 |
| M06 | Bid 100.00 / ask 100.01 locked; dashed half-cent gap in orange labeled TICK-CONSTRAINED; then a 100.005 level appears | "SEC adopted half-cent tick in 2024 · start date delayed". Source: SEC fact sheet 34-101070 |
| M07 | Units stack into INVENTORY box q=0→3; seeded price path | Plain-language labels only |
| M08 | r = s − q·γ·σ²·(T − t); tags: s = mid, q = inventory, γ = risk aversion, σ² = volatility, (T − t) = time left | Source: Avellaneda & Stoikov (2008) |
| M09 | spread = γσ²(T − t) + (2/γ)·ln(1 + γ/k) | Textbook parameters: s=100, γ=0.1, σ=2, k=1.5, T−t=1 → 0.40 + 1.29 = 1.69. Tag "TEXTBOOK PARAMETERS — NOT A REAL QUOTE" |
| M10 | Inventory steps vs reservation price line; bid-ask band shifts | Values from M09 parameters (r = 100, 99.60, 99.20, 98.80) |
| M11 | Ruler 0–300 m; vacuum pulse reaches 300 m, fiber pulse 200 m in the same microsecond; two machine markers 300 m apart | "≈ 300 m/µs vacuum · ≈ 200 m/µs fiber" |
| M12 | Six order blocks at 100.00 numbered #1–#6; incoming sell fills #1, #2 from the front | Tag "ILLUSTRATIVE" |
| M13 | Reuse M01 grid, overlay spread-capture and hedge arrows, then seeded simulation of many tiny edges converging | Tag "ILLUSTRATIVE SIMULATION"; "MARKET NEUTRAL (as reported)" |
| M14 | Left card: KNIGHT CAPITAL · AUG 2012 · ≈ $460M IN ONE TRADING DAY. Right: two short lines, CRITICS: UNFAIR ADVANTAGE / FILING: REAL-TIME RISK MANAGEMENT | Sources on card |
| M15 | Spread bar bid 100.00 / ask 100.01; three inputs feed it; µs counter | Final insight frame, hold ≥ 1s |
| M16 | `#202322` background, faint `#233D4C` grid, nothing else | 20s, no text |

## 5. Sources (REAL + cite)
- Virtu Financial Form S-1 (2014): one losing day in 1,238 trading days, 1 Jan 2009 – 31 Dec 2013. Also reported by CNBC (11 Mar 2014) and Quartz. Market-neutral description and "precise and nearly instantaneous hedging": CNBC. Critics' reaction: Reuters/Fortune (6 Apr 2015).
- Avellaneda & Stoikov (2008), "High-frequency trading in a limit order book", Quantitative Finance 8(3), 217–224.
- Glosten & Milgrom (1985), Journal of Financial Economics 14(1), 71–100.
- NYSE tick history: UK Government Office for Science tick-size review (8th→16th 24 Jun 1997; 1¢ 29 Jan 2001). SEC staff speech, 8 Jun 2001 (6.25¢; −37% NYSE, −50% Nasdaq, effective NYSE −15%). Revenue-decline reports: cited from WSJ (25 May 2001) in the ScienceDirect decimalization paper.
- SEC fact sheet 34-101070 (half-cent tick adopted 18 Sep 2024); compliance delays: SEC exemptive order (Oct 2025) and later reported extension.
- Knight Capital, Aug 2012 loss: KCG Holdings reference.
- Physics: light in glass fiber ≈ two-thirds the speed of light (≈ 200 m/µs); vacuum ≈ 300 m/µs.

## 6. VERIFY BEFORE PUBLISH
1. Half-cent tick status/date: re-check SEC site on publish day; adjust Scene 10 wording if the rule's start date has changed.
2. Knight Capital figure (Scene 22): confirm against the SEC order; if it differs, change to "hundreds of millions of dollars".
3. Revenue-decline sentence (Scene 9): confirm the WSJ 25 May 2001 citation or soften to "some firms reported".
4. `{EP05_TITLE}` and its playlist (Scene 24): EP05 must be public before EP06 publishes.
5. Docs drift: `QUANTROVE_TOPIC_STRATEGY.md` describes EP03/EP05 differently from the published titles. Sync.

## 7. ElevenLabs pronunciation hints (approximate)
HFT = "H-F-T" · Glosten = GLOSS-ten · Milgrom = MIL-grum · Avellaneda = ah-veh-yah-NEH-dah · Stoikov = STOY-kov · Virtu = VER-too · Nasdaq = NAZ-dak · µs = "microseconds".

## 8. Chapters (agent computes timestamps from the final timeline)
0:00 The one-loss record · Scene 3 The Bet Inside Every Spread · Scene 8 The Floor · Scene 12 The Formula Behind the Quote · Scene 17 What a Microsecond Buys · Scene 23 The Answer

## 9. Thumbnail spec (1280x720, palette lock)
Left: big "1" in lime over small "LOSS"; right: a tight 1,238-dot grid, one dot orange. No face, no extra text. Generate via Manim still or PIL.

## 10. Humanization self-audit (manual; agent re-runs `test_script_humanizer.py`)
- Banned cliché phrases: 0 found. Chapter Quad mapped in every chapter. Curiosity pivots in Scenes 5, 10, 16. Investigator voice, no textbook "definition first" openings.
- Quantitative fidelity: all figures sourced above. Illustrative numbers are labeled in the graphics.
- Zero fabrication: no invented anecdotes. Unknown facts are flagged in section 6.
