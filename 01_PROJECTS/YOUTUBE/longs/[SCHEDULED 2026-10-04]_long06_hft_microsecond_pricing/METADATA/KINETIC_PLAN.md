# EP06 Kinetic Keyword Pop-Up Plan (Track V2 Overlay)

**Episode Title**: The Machines Trading Before You Blink  
**Target Video**: 1920x1080 @ 60fps  
**Delivery Format**: QuickTime Apple ProRes 4444 (RGBA) / QuickTime RLE with alpha channel  
**Standard**: Track V2 Overlay per `.claude/rules/kinetic-popups.md` & `pipeline/config/layout_contract.json`  
**Timing Authority**: ElevenLabs Final VO (418.00s narration).  
*Note*: Exact word timestamps are currently marked UNAVAILABLE on disk. Pacing and cues below represent proportional scene timestamps; final keyframes will lock to word boundaries when `words.json` is generated via `faster-whisper`.

---

## 1. Design & Typography Tokens

| Element | Specification |
|---|---|
| **Font** | Nohemi Bold 700 (Fallback: Inter Bold 700) |
| **Font Size** | 38px – 44px (Uppercase, tracking +0.02em) |
| **Pill Background** | Raisin Black `#202322` at 85% opacity, border-radius 8px |
| **Pill Border** | 1px Charcoal Slate `#233D4C` |
| **Text Colors** | Off-White `#E6EDF3` (Standard text) <br> Power Lime `#C3D809` (Mechanisms, speed, positive edge) <br> Pumpkin `#FD802E` (Risk, loss, adverse selection, constraints) |
| **Safe Zone** | Pop-up upper band: `y = 56px .. 176px` (Centered horizontally `x = 960px` or staggered left/right within `x = 120px .. 1800px`) <br> Strictly forbidden in lower caption lane `y = 864px .. 1080px` |
| **Motion Physics** | `ease_out_back` entry scale 0.85 -> 1.05 -> 1.00 (0.22s); hold (1.5s–2.2s); linear opacity fade-out (0.18s) |

---

## 2. Kinetic Cue Schedule (Scenes 01 – 25)

| Scene | Est. Time | Spoken Narration Phrase | Highlighted Keywords | Pill / Accent Color | Treatment |
|---|---|---|---|---|---|
| **S01** | `00:01.5` | "How do HFT algorithms price spreads in microseconds?" | **HFT ALGORITHMS** | `#C3D809` (Lime) | Center pop-up pill, scale in |
| **S01** | `00:04.2` | "...price spreads in microseconds?" | **MICROSECONDS** | `#C3D809` (Lime) | Right-aligned pop-up pill |
| **S01** | `00:07.8` | "...and lost money on exactly one day." | **1 LOSING DAY** | `#FD802E` (Pumpkin) | Center warning pill |
| **S02** | `00:13.2` | "...1,238 trading days, one losing day." | **1,238 DAYS** | `#C3D809` (Lime) | Left-aligned pop-up pill |
| **S02** | `00:19.5` | "Start with the thing it sells. The spread." | **THE SPREAD** | `#C3D809` (Lime) | Center pop-up pill |
| **S03** | `00:26.0` | "You buy at the higher one, the ask." | **ASK PRICE** | `#E6EDF3` (Off-White) | Right-aligned pill above ASK panel |
| **S03** | `00:29.5` | "You sell at the lower one, the bid." | **BID PRICE** | `#E6EDF3` (Off-White) | Left-aligned pill above BID panel |
| **S03** | `00:34.0` | "The gap between them is the spread..." | **0.01 SPREAD** | `#C3D809` (Lime) | Center accent pill |
| **S04** | `00:43.0` | "No fees. No overhead." | **ZERO COSTS** | `#E6EDF3` (Off-White) | Center stack pill |
| **S04** | `00:50.0` | "A market maker... expecting to earn exactly zero." | **MARKET MAKER** | `#C3D809` (Lime) | Center pop-up pill |
| **S05** | `01:03.0` | "Some of the traders hitting a quote know something..." | **INFORMED TRADERS** | `#FD802E` (Pumpkin) | Right-aligned warning pill |
| **S05** | `01:14.0` | "Their model still produced a spread, for one reason." | **ADVERSE SELECTION** | `#FD802E` (Pumpkin) | Center warning pill |
| **S06** | `01:25.5` | "Someone buys. Then the price jumps ten cents." | **STALE QUOTE** | `#FD802E` (Pumpkin) | Flash warning pill |
| **S06** | `01:30.0` | "It just sold to someone who knew." | **-0.10 LOSS** | `#FD802E` (Pumpkin) | Danger accent pill |
| **S07** | `01:37.0` | "So a spread is not a toll. It is insurance..." | **INSURANCE** | `#C3D809` (Lime) | Center pop-up pill |
| **S07** | `01:42.0` | "...for decades, the rulebook decided..." | **THE FLOOR** | `#E6EDF3` (Off-White) | Center historical pill |
| **S08** | `01:48.5` | "The smallest price move allowed is called the tick." | **THE TICK** | `#C3D809` (Lime) | Center definition pill |
| **S08** | `01:57.0` | "Then one sixteenth: six and a quarter cents." | **6.25¢ (1/16)** | `#E6EDF3` (Off-White) | Staggered step pill |
| **S08** | `02:03.0` | "On January 29, 2001, it became one cent." | **1¢ DECIMAL** | `#C3D809` (Lime) | Accent highlight pill |
| **S09** | `02:16.5` | "...quoted spreads on NYSE stocks narrowed by an average of 37 percent..." | **-37% NYSE** | `#C3D809` (Lime) | Left metric pill |
| **S09** | `02:22.0` | "...and on Nasdaq stocks by about 50." | **-50% NASDAQ** | `#C3D809` (Lime) | Right metric pill |
| **S10** | `02:32.0` | "...the SEC concluded the penny itself had become the constraint." | **TICK-CONSTRAINED** | `#FD802E` (Pumpkin) | Warning pill |
| **S10** | `02:40.0` | "In 2024 it adopted a half-cent tick..." | **HALF-CENT TICK** | `#C3D809` (Lime) | Center policy pill |
| **S11** | `02:52.0` | "So the contest moves. To who is first in line." | **FIRST IN LINE** | `#C3D809` (Lime) | Center priority pill |
| **S12** | `03:04.0` | "...Marco Avellaneda and Sasha Stoikov published a model..." | **AVELLANEDA-STOIKOV** | `#C3D809` (Lime) | Center citation pill |
| **S12** | `03:12.0` | "If you buy, you now own risk. And a market maker would rather own nothing." | **INVENTORY RISK** | `#FD802E` (Pumpkin) | Warning pill |
| **S13** | `03:22.0` | "Instead, the machine uses a reservation price..." | **RESERVATION PRICE** | `#C3D809` (Lime) | Formula header pill |
| **S13** | `03:35.0` | "...how much the price jumps around, which is volatility..." | **VOLATILITY (σ²)** | `#FD802E` (Pumpkin) | Risk parameter pill |
| **S14** | `03:52.0` | "...its reservation price falls to ninety-eight eighty." | **98.80 (LEAN)** | `#FD802E` (Pumpkin) | Center readout pill |
| **S15** | `04:08.0` | "With the same textbook numbers, they add up to about a dollar sixty-nine." | **TEXTBOOK NUMBERS** | `#E6EDF3` (Off-White) | Disclaimer pill |
| **S16** | `04:22.0` | "It reprices every time its inventory or the risk changes." | **DYNAMIC REPRICE** | `#C3D809` (Lime) | Center dynamic pill |
| **S17** | `04:45.0` | "Why does any of this need to happen in microseconds?" | **MICROSECONDS** | `#C3D809` (Lime) | Chapter question pill |
| **S18** | `04:54.0` | "A microsecond is one millionth of a second." | **1 µs = 10⁻⁶ s** | `#E6EDF3` (Off-White) | Metric pill |
| **S18** | `05:02.0` | "...about three hundred meters in a vacuum, and about two hundred in glass fiber." | **200 M IN FIBER** | `#C3D809` (Lime) | Physical limit pill |
| **S19** | `05:12.0` | "If a machine's quote is stale for even a moment..." | **STALE QUOTE** | `#FD802E` (Pumpkin) | Danger pill |
| **S19** | `05:17.0` | "That is adverse selection again, now measured in microseconds." | **ADVERSE SELECTION** | `#FD802E` (Pumpkin) | Mechanism pill |
| **S20** | `05:28.0` | "On most exchanges, orders at the same price fill in the order they arrived." | **PRICE-TIME PRIORITY**| `#C3D809` (Lime) | Exchange rule pill |
| **S21** | `05:44.0` | "It described a market-neutral approach: it does not need prices to rise or fall."| **MARKET NEUTRAL** | `#C3D809` (Lime) | Core concept pill |
| **S21** | `05:54.0` | "...hedging each position almost the instant it takes it on." | **INSTANT HEDGE** | `#C3D809` (Lime) | Execution pill |
| **S21** | `06:04.0` | "...luck averages out. It is the same arithmetic as the tiny edge in the Simons story." | **LAW OF LARGE NUMBERS**| `#C3D809` (Lime) | Mathematical payoff pill |
| **S22** | `06:17.0` | "...cost the firm about 460 million dollars in a single trading day." | **KNIGHT CAPITAL (-$460M)** | `#FD802E` (Pumpkin) | Historical warning pill |
| **S22** | `06:28.0` | "...critics read it as proof that high-speed traders hold an unfair advantage." | **UNFAIR ADVANTAGE?** | `#E6EDF3` (Off-White) | Debate pill |
| **S23** | `06:44.0` | "So the next time you see a spread of one cent, do not read it as a fee." | **NOT A FEE** | `#E6EDF3` (Off-White) | Insight pill |
| **S23** | `06:51.0` | "Read it as an answer... And it priced that doubt before you finished clicking." | **PRICED DOUBT** | `#C3D809` (Lime) | Core thesis resolve pill |
| **S24** | `07:00.0` | CTA Window | *None* | — | Zero overlay text |
| **S25** | `07:18.0` | End Screen | *None* | — | Zero overlay text |

---

## 3. Kinetic Engine Handoff & Drift Note
- In `EP06_SCRIPT_AND_SHOTLIST.md`, Section 0, the script specifies:
  `Kinetic keywords: existing CleanText kinetic overlay (Track V2) — NOT Remotion. Keywords below are cues only; the agent aligns them to word timestamps (words.json).`
- In current Quantrove channel architecture, Remotion has been designated for kinetic overlays and typography, while CleanText is the Manim text-scaling standard.
- Per strict instructions, the production agent preserves existing CleanText references and flags this documentation discrepancy in `FINAL_QA_REPORT.md` without silently overriding the approved script.
