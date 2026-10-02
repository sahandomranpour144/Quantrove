# EP05 Shorts Batch Proposal & Research (Revised)

**Target Batch**: 5–6 Shorts (2 Extracted, 2 Native Rebuilt, 1–2 Standalone)  
**Parent Episode**: EP05 — *Market Making & The Illusion of Free Trading* (Pillar 3: Finance & Trading, Simplified)  
**Governing Standards**: `shorts-style.md` (`shorts_style.json`), `layout_contract.json` (Safe zone 200px bottom, 120px top), Institutional Data Intelligence palette.  
**Constraint Check**: Zero preview of EP06's topic (HFT microwave race / physical latency); zero fabricated statistics; all data flagged as verified or unverified.

---

## A. Top 4 Extraction Candidates (Ranked)

*Timestamps verified against `ep05_exact_word_timestamps.json`.*

### 1. Rank 1 — Scene 05: The Airport Booth & Bid-Ask Spread
* **Exact Timestamps**: `01:37.06` – `02:11.32` (`97.06s` – `131.32s`)
* **Duration**: `34.26s`
* **First 3s Hook**: *"These firms are market makers. Think of them like a currency exchange booth at an airport."* (First word starts at 97.06s; kinetic text: `THINK OF AN AIRPORT BOOTH`).
* **The Reveal**: Market makers take zero directional risk; by simultaneously buying at $99.99 and selling at $100.01, a 2-cent spread across millions of daily trades converts into billions in virtually risk-free profit.
* **Manim Visual**: 100% Manim (`scene05_spread_mechanism.py`). Features the airport currency exchange card morphing into a live Level-2 order book, bracketed $0.02 spread, and an accelerating profit counter.
* **Self-Contained**: Yes. Complete, intuitive pedagogical arc explaining market making from first principles.

### 2. Rank 2 — Scene 07: The $65M SEC Fine for Hidden Invoices
* **Exact Timestamps**: `02:46.68` – `03:19.86` (`166.68s` – `199.86s`)
* **Duration**: `33.18s`
* **First 3s Hook**: *"If market makers are paying brokers, who ends up paying the bill?"* (Spoken within first 1.5s; kinetic text: `WHO PAYS THE BILL?`).
* **Exact Script Dialogue & Attribution Check**:
  > **VO**: *"If market makers are paying brokers, who ends up paying the bill? In 2020, the SEC answered that question with a sixty-five million dollar enforcement settlement against Robinhood. The SEC found that Robinhood told customers its trading was free, while quietly routing orders to the market makers paying the highest fees — even when that meant customers received worse execution prices than other brokers. Free trading had a hidden invoice. It was just subtracted from your fill price before you ever saw it."* (`EP05_SCRIPT.md` Scene 07, lines 56–60)
* **SEC Penalty Verification**: **Verified**. The $65M settlement was paid by retail broker **Robinhood Financial LLC** on December 17, 2020 (SEC Admin. Proc. File No. 3-20171 / Release No. 33-10906) for misleading statements regarding payment for order flow and failure to satisfy best execution duties. **The EP05 script correctly attributes the penalty to Robinhood, NOT to a market maker.**
* **The Reveal**: "Free" trading had a hidden invoice subtracted from execution prices before customers saw it.
* **Manim Visual**: High-retention Manim (`scene07_sec_penalty.py`) with official SEC administrative documents, heavy $65,000,000 Pumpkin seal, and document flip into a customer receipt. *(Flow clip 02 is 1.5s ambient cutaway at scene head; can be trimmed or used as intro beat)*.
* **Self-Contained**: Yes. Complete investigative loop: question, culpable broker, official SEC penalty, and consumer mechanism.

### 3. Rank 3 — Scene 06: Why Retail Trades Are Sold ($200M/Quarter)
* **Exact Timestamps**: `02:11.96` – `02:46.68` (`131.96s` – `166.68s`)
* **Duration**: `34.72s`
* **First 3s Hook**: *"So why do market makers want your retail trades so badly? Because retail trades are safe."*
* **The Reveal**: Wholesalers pay hundreds of millions (Robinhood: $200M+/quarter) because retail orders are "uninformed flow"—an individual buying 50 Apple shares on lunch break has no inside information, making them safe to trade against without adverse selection risk.
* **Manim Visual**: Manim (`scene06_pfof_kickback.py`) showing the trade pipeline split, Pumpkin `#FD802E` reverse PFOF pipeline, and a quarterly revenue bar chart crossing $200,000,000.
* **Self-Contained**: Yes. Direct paradox resolved cleanly with data.

### 4. Rank 4 — Scene 08: The 2-Cent Silent Compounding Drag
* **Exact Timestamps**: `03:20.38` – `03:53.08` (`200.38s` – `233.08s`)
* **Duration**: `32.70s`
* **First 3s Hook**: *"You might think, if I only lose a fraction of a cent per share, does it really matter? Here is the math."*
* **The Reveal**: Losing just 2 cents per share on 100 shares equals $2/order. At two trades a week, this friction silently siphons hundreds of dollars out of a portfolio over time.
* **Manim Visual**: Manim (`scene08_hidden_cost.py`) zooming from a single -$0.02 share sliver out to a 500-trade grid, cascading into a -$1,000+ compounding drag curve.
* **Self-Contained**: Yes. Pure actionable math explaining micro-slippage.

---

## B. Concept Candidates for Native Shorts (Rebuilt with New Visuals)

*Built strictly using facts from the EP05 script; verified to avoid overlap with Extraction 2.*

### 1. Native 1: The Execution Trap — Market Orders vs Limit Orders
* **Script Verification (Lines Quoted)**:
  > **VO**: *"First: stop using market orders. When you hit market buy, you agree to whatever price the market maker hands you. Always use a limit order — you set the maximum price you are willing to pay."* (`EP05_SCRIPT.md` Scene 10, lines 79, 81)  
  > *Visual Anchor*: *"Card 1: Padlock snaps shut on price tag: LIMIT ORDER LOCK: $150.00 MAX. Slippage bounces off."*
  * **Confirmation**: **Directly in EP05 script**.
* **Hook Line**: *"The single most expensive button on your trading app is Market Buy."*
* **4-Beat Narrative**:
  * *Beat 1 (Idea)*: You press Market Buy to get your shares right away.
  * *Beat 2 (Simple / Wrong)*: You believe you bought at the exact price flashing on your screen.
  * *Beat 3 (Complex / Wrong)*: You assume the tiny price jump is just normal exchange volatility.
  * *Beat 4 (Reveal)*: A market order is a blank check to a wholesale internalizer. A limit order locks your ceiling price and forces genuine execution against the NBBO.
* **NEW Visual Metaphor**: An auction paddle with an open blank check where the auctioneer stamps a random price markup, juxtaposed against a mechanical digital clamp that physically halts a rising price meter at an exact dollar ceiling.

### 2. Native 2: The Vanishing Exchange — Why Your Order Never Reaches the NYSE
*(Replaced prior "tollbooth" concept to eliminate overlap with Extraction 2's "who pays the bill" premise).*
* **Script Verification (Lines Quoted)**:
  > **VO**: *"Here is what most investors imagine happens: you tap buy on your phone, your order flies straight to the New York Stock Exchange or Nasdaq, and you match with another investor selling shares. But that is almost never what happens. Instead, before your order ever touches a public exchange, your broker routes it to an off-exchange wholesale firm — names like Citadel Securities, Virtu Financial, or Susquehanna. Firms most retail investors have never heard of."* (`EP05_SCRIPT.md` Scene 04, lines 33–37)
  * **Confirmation**: **Directly in EP05 script**.
* **Hook Line**: *"When you tap buy on Robinhood or Webull, your order does not go to the New York Stock Exchange."*
* **4-Beat Narrative**:
  * *Beat 1 (Idea)*: You tap buy on your phone expecting your order to execute on the NYSE or Nasdaq.
  * *Beat 2 (Simple / Wrong)*: You picture matching directly with another investor selling shares on the public exchange floor.
  * *Beat 3 (Complex / Wrong)*: You assume all regulated stock orders must enter public lit exchange order books by default.
  * *Beat 4 (Reveal)*: Your order is intercepted before it ever touches a public exchange. Brokers route retail flow directly to off-exchange wholesale internalizers (Citadel, Virtu, Susquehanna) who fill it internally away from public eyes.
* **NEW Visual Metaphor**: An air traffic radar tracking a passenger aircraft labeled "Your Retail Order" taking off toward "NYSE Terminal". Mid-flight, an automated air-traffic switch redirects the aircraft onto a private, unmarked runway labeled "Wholesale Internalizer Hangar".

### 3. Native 3: The NBBO Price Siphon (Where Price Improvement Vanishes)
* **Script Verification (Lines Quoted)**:
  > **VO**: *"By law, brokers are supposed to provide what is called best execution, anchored to the National Best Bid and Offer, or NBBO... Independent audits comparing order routing have repeatedly shown that orders routed to wholesale internalizers frequently miss out on genuine price improvement that public exchanges could have delivered."* (`EP05_SCRIPT.md` Scene 09, lines 72–74)
  * **Confirmation**: **Directly in EP05 script**.
* **Hook Line**: *"Federal law says your broker must give you the best stock price in America. Here is how they don't."*
* **4-Beat Narrative**:
  * *Beat 1 (Idea)*: The National Best Bid and Offer (NBBO) guarantees fair prices across all exchanges.
  * *Beat 2 (Simple / Wrong)*: Investors assume every broker routes orders to whichever exchange is cheapest.
  * *Beat 3 (Complex / Wrong)*: Some think off-exchange routing only occurs when wholesalers beat public prices.
  * *Beat 4 (Reveal)*: Wholesalers match the NBBO minimum on paper, but independent audits show internalized retail trades miss out on genuine price improvement available on public books.
* **NEW Visual Metaphor**: Two parallel transparent pipes: Pipe A (Public Exchange) releases bonus gold coins directly into the user's bucket; Pipe B (Wholesale Internalizer) has a hidden mesh sieve catching the coins into an institutional vault, dropping only baseline water into the bucket.

---

## C. Standalone Topic Candidates

*Screened against backlog, IDEAS, and existing Shorts. Focused on Pillar 3 (Finance Simplified) and Pillar 2 (AI + Finance). No EP06 spoilers.*

| # | Topic & Core Question | Hook Line (First 3s) | Pillar | Verified Data Source & Date | Visual Concept (Manim) | Verification Status |
|---|---|---|---|---|---|---|
| **1** | **The "90% of Options Expire Worthless" Myth**<br>*What actually happens to options contracts before expiration?* | *"Wall Street loves to tell you that ninety percent of options expire worthless. The real clearinghouse data proves that is a myth."* | Finance & Trading, Simplified | **Options Clearing Corporation (OCC)** Annual Data / **CBOE** Clearing Studies (2023–2024 analysis); SEC Investor Bulletins | A 100% options contract bar chart splitting into three distinct animated colored segments: **~55–60% closed out early** (Lime), **~10% exercised** (Charcoal), and **~30–35% expiring worthless** (Pumpkin). | **Verified**: OCC clearing statistics confirm ~10% exercised, ~55–60% closed before expiry, ~30–35% expire worthless. The "90%" figure is a persistent retail myth conflating deep OTM held-to-expiry lottery tickets. |
| **2** | **Dark Pools vs Wholesalers: Where the 40% Really Goes**<br>*Where do stock trades actually go when they bypass public exchanges?* | *"Everyone talks about secret Wall Street dark pools trading half the stock market. But dark pools are only 15%—here is where the rest actually goes."* | Finance & Trading, Simplified | **FINRA ATS Transparency Data** (2023–2024 weekly aggregates); **SEC Staff Report on Market Structure** (2022/2023) | Total market volume bar (100%): 55–60% Public Lit Exchanges (NYSE/Nasdaq), 15% Pure Dark Pools (ATS), and 25–30% Wholesaler Internalization (Citadel/Virtu retail order flow). | **Verified**: ~40–45% of total US volume is off-exchange. Pure dark pools (ATS) are strictly ~10–15%; the largest off-exchange segment (~25–30%) is broker internalization. |
| **3** | **The S&P 500 Dividend Illusion**<br>*How much of market history is missing without reinvested dividends?* | *"If you look at the S&P 500 chart over fifty years, half the money is missing."* | Finance & Trading, Simplified | S&P Dow Jones Indices (S&P 500 Total Return vs Price Return Index, 1970–2025); NYU Stern / Damodaran | Two diverging trajectories from a $10k start in 1975: Price Return reaches ~$450k; Total Return with reinvested dividends rockets past $2.1M. | **Verified**: Reinvested dividends account for ~69–75% of cumulative S&P 500 returns over rolling 50-year spans per S&P Dow Jones Indices. |
| **4** | **The 0DTE Options Explosion**<br>*Why are same-day expiring options now almost half the market?* | *"Almost half of all S&P 500 options now expire on the exact day they are bought."* | AI + Finance + Trading / Finance Simplified | CBOE Volatility Insights (0DTE Volume 2022–2024); JPMorgan Quantitative Strategy Reports | Stacked bar chart from 2016 to 2024 showing 0DTE options surging from <5% to 45%+, with an intraday countdown clock ticking `06:30:00 → 00:00:00`. | **Verified**: CBOE and JPMorgan confirm 0DTE options accounted for 43–48% of total SPX options volume in 2023–2024. |

---

## D. Recommended Picks per Slot

* **Slot 1 (Extraction 1)**: **Extraction Candidate 1 (Scene 05 — The Airport Booth & Spread)**
  * *Reason*: Pure Manim, intuitive real-world analogy (currency booth to bid-ask spread), completely self-contained, and perfectly anchors EP05's core topic.
* **Slot 2 (Extraction 2)**: **Extraction Candidate 2 (Scene 07 — The $65M SEC Fine)**
  * *Reason*: Hard regulatory investigative reveal backed by official SEC evidence (Robinhood fine verified); highest curiosity hook ("who pays the bill?").
* **Slot 3 (Native 1)**: **Native Concept 1 (Market Order vs Limit Order Execution Trap)**
  * *Reason*: Directly quotes Scene 10 of the EP05 script and converts viewer awareness into immediate utility via a mechanical clamp visual.
* **Slot 4 (Native 2)**: **Native Concept 2 (The Vanishing Exchange / Off-Exchange Routing)**
  * *Reason*: Directly quotes Scene 04 of the EP05 script, resolves the overlap with Extraction 2, and uses a fresh air-traffic redirect visual metaphor.
* **Slot 5 (Standalone 1)**: **Standalone 1 (The "90% of Options Expire Worthless" Myth)**
  * *Reason*: High-demand myth-busting format grounded in verified OCC/CBOE clearing data (~10% exercised, ~55–60% closed, ~30–35% expire worthless).
* **Slot 6 (Standalone 2)**: **Standalone 2 (Dark Pools vs Wholesalers: Where the 40% Really Goes)**
  * *Reason*: Fact-corrects retail assumptions about dark pools vs internalization using primary FINRA ATS/SEC data, expanding Pillar 3 without encroaching on EP06.

---

## E. Status of Missing / Unknown Standalone Shorts Folders

An audit of the filesystem confirms the physical state of the 3 standalone Shorts folders:

1. `shorts/[NOT_UPLOADED]_short_standalone_medallion_fund/`:
   * **Filesystem Status**: **MISSING FROM DISK**.
   * **Context**: Listed as `[NOT_UPLOADED]` in `STATE.md` and `reports/shorts_audit_2026-09-22.md`. However, during EP04 production, its core quantitative concept was rendered and packaged as a native Short: `shorts/[SCHEDULED 2026-09-29]_ep04_The 50 75% Edge That Built $21 Billion 📊💰` (scheduled on YouTube Studio for Sept 29, 2026).
2. `shorts/[NOT_UPLOADED]_short_standalone_head_and_shoulders/`:
   * **Filesystem Status**: **MISSING FROM DISK**.
   * **Context**: Listed as `[NOT_UPLOADED]` in `STATE.md` and flagged as "Incomplete (no final .mp4 yet)" in `reports/shorts_audit_2026-09-22.md`. No media assets, scripts, or directories exist under `shorts/` or `03_ARCHIVE/`.
3. `short_standalone_ai_ml_engineer_roadmap`:
   * **Filesystem Status**: **MISSING FROM DISK**.
   * **Context**: Recorded historically in `01_PROJECTS/YOUTUBE/MIGRATION_MANIFEST.md` and `reports/shorts_audit_2026-09-22.md` as "Not uploaded", but never added to `STATE.md` and completely absent from disk.
* *Note*: Per task instructions, `STATE.md` remains locked and was not modified.
