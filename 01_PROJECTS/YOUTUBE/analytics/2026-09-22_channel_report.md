# Quantrove Channel Performance & Intelligence Report — 2026-09-22

> **Document Purpose**: Comprehensive channel performance report analyzing all published long-form and Shorts content, content pillar health, subscriber sources, performance anomalies, and audience behavior.  
> **Data Sources**: Live data pull via `youtube-studio-mcp` (YouTube Analytics API v2 & YouTube Data API v3).  
> **Channel**: [@Quantrove](https://youtube.com/@Quantrove) (`UCjEOgYbytvb9ocL48uotMsg`)  
> **Report Date**: September 22, 2026 (Day 28 of active channel life; first video August 25, 2026)  
> **Channel Totals**: **994 Public Views** / **997 API Views** | **387 Estimated Minutes Watched (~6.45 hrs)** | **8 Subscribers** | **61 Likes** | **37 Comments** | **12 Total Public Videos (3 Long-Form, 9 Shorts) + 3 Staged/Private**

---

## Executive Summary

1. **Growth Trajectory**: The channel reached **994 public views** (+30 views since Sept 19), **387 minutes of watch time** (+29 min), **61 likes** (+14 likes, +29.8%), and **37 comments**. Net subscribers hold steady at **8**.
2. **Fresh Releases (Sept 22)**:
   - **EP03 Long-Form** (`nx0oF7pxjds`): *"Why Everyone Gets Recommendation Algorithms Wrong"* published today at 12:30 UTC. Replaced prior upload `V0HzN0fKQ9A`. Accumulating 13 views, 3 likes, 5 comments in initial 6 hours.
   - **EP03 Short #1** (`ps7d0Qwz760`): *"The Algorithm Was Never Built to Inform You ⚡"* released at 15:30 UTC (10 views, 2 likes, 2 comments in first 3.5 hours).
   - Two additional EP03 Shorts (`wDeqACCW4p0`, `E0ta91FyIAI`) and **EP04 Flagship** (`jwPcJSfDQPg`) are staged in private status ready for rollout.
3. **The SUBSCRIBER Traffic-Source Anomaly**: **CONFIRMED STILL PRESENT**. 481 views (48.2%) and 236 min of watch time (61.0%) are attributed to `insightTrafficSourceType == "SUBSCRIBER"` across the channel, led by EP02 with 348 views. However, cross-referencing `subscribedStatus` proves that **782 views (78.4%) across the channel and 366 views (96.3%) on EP02 were from completely UNSUBSCRIBED viewers**. Only 13 views on EP02 came from subscribed accounts. (See Section 4 for full technical audit).
4. **Subscriber Source Origin**: **75.0% of subscribers (6 of 8)** converted directly via the **Channel Page / Profile Header**, 25.0% (2 of 8) converted on Long-Form Video on Demand (EP02), and **0.0% converted directly inside the Shorts feed player**.
5. **Shorts vs. Long-Form Dynamic**: Long-Form drives **79.3% of total channel watch time** (307 min vs 79 min). However, Shorts generate **65.6% of channel likes** (40 vs 21) and **59.5% of comments** (22 vs 15).

---

## 1. Complete Video Performance Catalog

*Note on Latency & CTR*: YouTube Analytics API has an inherent 48–72 hour batch processing delay. Videos published within the last 48 hours reflect real-time public counters from YouTube Data API v3; older videos reflect fully processed Analytics metrics. Thumbnail Impression Click-Through Rate (CTR) is restricted by Google to the YouTube Studio web dashboard and is not exposed via the public Analytics API v2.

### Published Long-Form Documentaries

| ID | Title / Episode | Pillar | Published | Duration | Views (Pub / API) | Watch Time | Avg View Dur (AVD) | Retention % | Likes | Comments | Subs Gained |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `3I84-kRga0s` | **What 50 Years of Recession Data Actually Show** (EP02) | 📊 Data Stories | 2026-09-09 | 8m 08s (488s) | 384 / 380 | 207 min | 111s (1m 51s) | **22.7%** | 6 | 9 | +2 |
| `oJstBJgNAi4` | **Why Do Stock Market Crashes Actually Happen?** (EP01) | 📊 Data Stories | 2026-09-01 | 6m 25s (385s) | 104 / 102 | 54 min | 104s (1m 44s) | **27.0%** | 6 | 5 | 0 |
| `nx0oF7pxjds` | **Why Everyone Gets Recommendation Algorithms Wrong** (EP03) | 🤖 AI & ML | 2026-09-22 | 5m 20s (320s) | 13 / *batch* | *batch* | *batch* | *batch* | 3 | 5 | 0 |
| `jwPcJSfDQPg` | **Can AI Actually Predict Stock Prices?** (EP04) | 📈 AI + Finance | 2026-09-21 | 7m 25s (445s) | 3 / *private* | *staging* | *staging* | *staging* | 0 | 0 | 0 |

---

### Published Short-Form Videos (Shorts)

| ID | Title / Topic | Pillar / Lineage | Published | Duration | Views (Pub / API) | Watch Time | AVD | Retention % | Likes | Comments |
|---|---|---|---|---|---|---|---|---|---|---|
| `K8I8dLyfZ78` | The Most Profitable Day in Stock Market History (March 9, 2009) 📈 | 💰 Finance (EP02 Cut) | 2026-09-11 | 28s | 124 / 123 | 15 min | 22.0s | **78.6%** | 7 | 3 |
| `sOyCCa6MGcw` | Welcome to Quantrove \| AI, Finance & Hidden Patterns | 🌐 Brand / Trailer | 2026-08-25 | 26s | 112 / 91 | 18 min | 21.0s | **80.8%** | 5 | 5 |
| `UJyKHdLnOJU` | How Margin Buying Triggered the 1929 Crash #shorts | 📊 Data (EP01 Cut) | 2026-09-03 | 29s | 59 / 59 | 11 min | 38.0s | **131.0%** *(Loop)* | 6 | 1 |
| `oHO-Om0TuLY` | How Microsoft Pulled Off The Ultimate AI Heist #shorts | 🤖 AI & ML Standalone | 2026-09-05 | 43s | 51 / 47 | 11 min | 34.0s | **79.1%** | 5 | 3 |
| `x_kkH0aFUEU` | The Best Day to Buy Stocks Happens During Peak Panic 📊 | 📊 Data (EP02 Cut) | 2026-09-14 | 33s | 45 / 45 | 9 min | 34.0s | **103.0%** *(Loop)* | 5 | 4 |
| `looNFUjN2hc` | The ONE Pattern Behind Every Market Crash #shorts | 📊 Data (EP01 Cut) | 2026-09-02 | 30s | 40 / 40 | 6 min | 27.0s | **90.0%** | 4 | 3 |
| `LfDIFgQaFL8` | AI Can't Count Letters? 🍓 (The Token Blind Spot) #shorts | 🤖 AI & ML Standalone | 2026-09-18 | ~50s | 39 / 38 | 12 min | 45.0s | **90.0%** | 5 | 7 |
| `bVx3K9U9zHM` | Why Official Recession News is Always 7 Months Too Late 📢 | 📊 Data (EP02 Cut) | 2026-09-15 | 44s | 25 / 25 | 6 min | 27.0s | **61.4%** | 5 | 6 |
| `ps7d0Qwz760` | The Algorithm Was Never Built to Inform You ⚡ #shorts | 🤖 AI & ML (EP03 Cut) | 2026-09-22 | ~40s | 10 / *batch* | *batch* | *batch* | *batch* | 2 | 2 |
| `wDeqACCW4p0` | Why Algorithms Stopped Optimizing for Clicks ⚡ | 🤖 AI & ML (EP03 Cut) | 2026-09-22 | ~45s | 0 / *private* | — | — | — | 0 | 0 |
| `E0ta91FyIAI` | How Recommendation Engines Narrow Your Reality 👁️ | 🤖 AI & ML (EP03 Cut) | 2026-09-22 | ~50s | 0 / *private* | — | — | — | 0 | 0 |

---

## 2. Content Pillar Performance & Cadence Audit

Quantrove rotates production across four core pillars per constitution:

```
Pillar Share of Public Views (994 Total):
[██████████████████████████████████████████████████████ 66.1% Pillar 4: Data Stories ]
[███████████████████ 23.7% Pillar 3: Finance Simplified ]
[████████ 11.4% Pillar 1: AI & ML ]
[ 0.0% Pillar 2: AI+Finance (EP04 drops Sept 23) ]
```

| Pillar | Status | Live Releases | Public Views | Watch Time | % Watch Time | Likes | Comments | Health Assessment |
|---|---|---|---|---|---|---|---|---|
| **Pillar 1: 🤖 AI & ML in the Real World** | Active & Scaling | 1 Long (`nx0oF7pxjds`), 3 Shorts (`LfDIFgQaFL8`, `oHO-Om0TuLY`, `ps7d0Qwz760`) | 113 | 40 min | 10.3% | 15 | 17 | **High Engagement Density**. Generates highest comment-to-view ratio (15.0%) and technical debate. |
| **Pillar 2: 📈 AI + Finance + Trading** | Staged / Imminent | 1 Long (`jwPcJSfDQPg` in private) | 3 | — | — | 0 | 0 | **Flagship EP04 Ready**. Will establish pillar authority upon public drop on Sept 23. |
| **Pillar 3: 💰 Finance & Trading, Simplified** | Primed | 2 Shorts (`K8I8dLyfZ78`, `sOyCCa6MGcw`) | 236 | 33 min | 8.5% | 12 | 8 | **High Viral Velocity**. Holds channel's #1 Short (`K8I8dLyfZ78` at 124 views). EP05 long scheduled Sept 30. |
| **Pillar 4: 📊 Data Stories** | Foundational Anchor | 2 Long (`3I84-kRga0s`, `oJstBJgNAi4`), 4 Shorts (`UJyKHdLnOJU`, `x_kkH0aFUEU`, `looNFUjN2hc`, `bVx3K9U9zHM`) | 657 | 293 min | **75.7%** | 32 | 28 | **Watch Time Engine**. Provides 75.7% of all channel minutes. EP02 is channel anchor. |

---

## 3. Subscriber Conversion Source Breakdown

Empirical analysis of subscriber acquisition via `creatorContentType` dimension:

| Conversion Surface / Source | Subscribers Gained | % of Total Subscribers | Associated Views | Conversion Rate | Strategic Takeaway |
|---|---|---|---|---|---|
| **Channel Page / Profile Header (`creatorContentTypeUnspecified`)** | **6** | **75.0%** | 0 direct watch views | — | Viewers who watch a video visit the channel page, inspect the catalog and branding, and subscribe from the profile. |
| **Long-Form VOD (`videoOnDemand`)** | **2** | **25.0%** | 594 API views | 0.34% | Both attributed directly to EP02 (`3I84-kRga0s`). Long-form converts high-intent subscribers. |
| **Shorts Feed (`shorts`)** | **0** | **0.0%** | 400 API views | 0.00% | Shorts drive massive likes (40) and comments (22) but **zero direct in-feed subscriptions**. |
| **Total** | **8** | **100.0%** | **997 API views** | **0.80%** | Channel-level conversion rate. |

> **Key Takeaway**: Shorts do not convert subscribers in the Shorts feed. Instead, Shorts act as a discovery mechanism that pushes viewers to visit the Channel Page or watch Long-Form, where 100% of subscriptions actually occur.

---

## 4. The SUBSCRIBER Traffic-Source Anomaly Investigation

### Status: CONFIRMED STILL PRESENT

The user flagged an apparent contradiction where `SUBSCRIBER` traffic source dominated channel metrics despite having only 8 subscribers. Live API auditing confirms this phenomenon is active and structural.

### Empirical Data Breakdown

```
Traffic Source Distribution (API Views = 997):
- SUBSCRIBER (Subscriptions Feed Placement): 481 views (48.2%) | 236 min (61.0%)
- YT_CHANNEL (Channel Page Browsing):        231 views (23.2%) | 86 min (22.2%)
- SHORTS (Shorts Algorithmic Feed):          119 views (11.9%) | 10 min (2.6%)
- YT_SEARCH (Organic Search Queries):        100 views (10.0%) | 20 min (5.2%)
- YT_OTHER_PAGE (Related / Embeds):          32 views (3.2%)   | 19 min (4.9%)
- NOTIFICATION (Direct Bell Clicks):         16 views (1.6%)   | 3 min (0.8%)
- PLAYLIST (Continuous Playback):            10 views (1.0%)   | 2 min (0.5%)
- END_SCREEN & OTHERS:                       8 views (0.8%)    | 8 min (2.1%)
```

### The Root Cause: Traffic Placement vs. User State

When cross-referencing `insightTrafficSourceType` with `subscribedStatus`, the anomaly unravels:

| Dimension / Metric | Total Channel | EP02 (`3I84-kRga0s`) | EP01 (`oJstBJgNAi4`) |
|---|---|---|---|
| **Traffic Source = `SUBSCRIBER`** | **481 views** (48.2%) | **348 views** (91.6%) | **72 views** (70.6%) |
| **User Status = `UNSUBSCRIBED`** | **782 views** (**78.4%**) | **366 views** (**96.3%**) | **82 views** (**80.4%**) |
| **User Status = `SUBSCRIBED`** | **212 views** (**21.3%**) | **13 views** (**3.4%**) | **20 views** (**19.6%**) |

### Diagnosis:
1. **Misleading Nomenclature**: In YouTube Analytics, the `SUBSCRIBER` traffic source represents views logged from the Subscriptions feed interface or attributed to subscription-related shelf testing.
2. **True Audience Reality**: **96.3% of EP02 viewers were completely unsubscribed**. EP02 did not reach an existing loyal base; it was served to non-subscribers via a YouTube algorithmic placement that YouTube internally tagged under the `SUBSCRIBER` traffic source enum.
3. **Latency Factor**: YouTube Analytics batch processing for daily breakdowns currently halts at `2026-09-19`. The data for Sept 20, 21, and 22 remains pending in Google's data warehouse. As a result, the anomaly recorded through Sept 19–20 remains locked and active in the official tables.

---

## 5. Performance Flags: Best, Worst & Outliers

### 1. Best Performing Video (Channel Champion)
- **Video**: `3I84-kRga0s` — *What 50 Years of Recession Data Actually Show* (EP02 Long-Form)
- **Metrics**: **384 public views**, **207 minutes watch time** (53.5% of total channel watch time), 6 likes, 9 comments, +2 net subscribers.
- **Why It Won**: The title challenged consensus macroeconomic assumptions ("Actually Show"). Historical long-term data (1970–2025) provides evergreen search and browse value.

### 2. Best Performing Short
- **Video**: `K8I8dLyfZ78` — *The Most Profitable Day in Stock Market History (March 9, 2009) 📈*
- **Metrics**: **124 public views**, **15 minutes watch time**, **7 likes** (highest like count on entire channel), 3 comments, 78.6% retention.
- **Why It Won**: Exact date, exact index level (S&P 666), and sharp counter-narrative (buying at peak panic).

### 3. Worst Performing Video
- **Day-1 New Release**: `ps7d0Qwz760` (*The Algorithm Was Never Built to Inform You*) with 10 views (released 3.5 hours ago).
- **Mature Content (>7 days)**: `bVx3K9U9zHM` — *Why Official Recession News is Always 7 Months Too Late 📢*
  - **Metrics**: **25 public views**, 6 minutes watch time, 61.4% retention (lowest retention of any mature short).
  - **Why It Lagged**: Hook ("The NBER takes 7 months...") was more bureaucratic and conceptual than emotional/monetary compared to the "March 9, 2009" and "Margin Buying" hooks.

### 4. Shorts Outperforming Parent Long-Form

| Comparison Type | Short Video | Short Views | Parent / Comparison Long-Form | Long-Form Views | Delta |
|---|---|---|---|---|---|
| **Cross-Pillar / Sibling Outperformance** | `K8I8dLyfZ78` (March 9, 2009 Short) | **124 views** | `oJstBJgNAi4` (EP01 Crashes Long-Form) | 104 views | **Short leads by +20 views (+19.2%)** |
| **Pillar Standalone vs. Pillar Long** | `oHO-Om0TuLY` (Microsoft AI Heist Short) | **51 views** | `nx0oF7pxjds` (EP03 Algorithms Long-Form) | 13 views | **Short leads by +38 views (+292%)** |
| **Pillar Standalone vs. Pillar Long** | `LfDIFgQaFL8` (Strawberry Token Short) | **39 views** | `nx0oF7pxjds` (EP03 Algorithms Long-Form) | 13 views | **Short leads by +26 views (+200%)** |
| **Direct Parent Pacing** | `ps7d0Qwz760` (Algorithm Hook Short) | **10 views** *(in 3.5h)* | `nx0oF7pxjds` (EP03 Parent Long) | 13 views *(in 6h)* | **Pacing to overtake parent on Day 1** |

> **Key Insight**: Standalone concept Shorts (`K8I8dLyfZ78`, `oHO-Om0TuLY`, `LfDIFgQaFL8`) consistently achieve 40–120 views within days, outpacing newer long-form releases during their initial distribution window.

---

## 6. Retention Benchmarking (EP01 vs. EP02)

Empirical audience watch ratio comparison at standardized timeline intervals:

| Timeline Checkpoint | Timestamp (EP01 / EP02) | EP01 Retention (`oJstBJgNAi4`) | EP02 Retention (`3I84-kRga0s`) | Structural Observation |
|---|---|---|---|---|
| **1% (Opening)** | 0:04 / 0:05 | 70.0% | **90.6%** | EP02 hook visual captured 20% more immediate attention. |
| **5% (Hook Complete)** | 0:19 / 0:24 | 43.3% | **52.3%** | EP02 held majority (>52%) through the initial thesis statement. |
| **10% (Intro End)** | 0:38 / 0:49 | 30.0% | **35.5%** | Initial drop-off window claims ~65–70% of viewers across both videos. |
| **25% (Body Act 1)** | 1:36 / 2:02 | **33.3%** | 22.4% | Both settle into extraordinarily flat retention plateaus. |
| **50% (Midpoint)** | 3:12 / 4:04 | **26.7%** | 20.6% | Zero pacing drop across 4+ minutes of dense economic charts. |
| **75% (Body Act 2)** | 4:48 / 6:06 | **26.7%** | 16.8% | High fidelity viewing through the core analytical payoff. |
| **90% (Pre-Outro)** | 5:46 / 7:19 | **20.0%** | 15.9% | Normal educational YouTube exit before outro sequence. |
| **100% (End Screen)** | 6:25 / 8:08 | **16.7%** | 11.2% | Final end-screen retention. |

---

## 7. Immediate Strategic Recommendations

1. **Leverage "Related Video" on EP03 Shorts**: `ps7d0Qwz760` is pacing rapidly (10 views in 3.5 hrs). Ensure the YouTube Studio "Related Video" selector is explicitly pointed to `nx0oF7pxjds` to funnel short-form traffic into long-form watch time.
2. **Prepare EP04 Launch (Tomorrow, Sept 23)**: EP04 (`jwPcJSfDQPg`) will activate Pillar 2 (AI + Finance + Trading), which currently has 0 public views. Its quantitative angle (Jim Simons / Medallion Fund / Overfitting) combines the proven appeal of finance with technical AI mechanics.
3. **Channel Page Optimization**: Because **75% of subscribers convert on the channel page**, maintain the channel trailer (`sOyCCa6MGcw`), featured playlists, and banner branding in institutional condition.
