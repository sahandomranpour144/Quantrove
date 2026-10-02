# EP05 Gate 2 Rebuild Report — Final Asset & Timing Verification
**Date**: 2026-09-26  
**Episode**: EP05 — *Why "Free" Trading Isn't Free* (Market Making & The Illusion of Free Trading)  
**Rebuild Folder**: `01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion/`  
**Master Narration**: 337.12s (Gemini TTS: Orus, -14.0 LUFS)  
**Kinetic Overlay**: 337.13s (60fps transparent argb QuickTime RLE)  

---

## 1. Scene-by-Scene: Built Duration vs. Assigned Duration

All files verified via `ffprobe` against `TIMELINE_MANIFEST.md`:

| Scene | Clip Filename in `TIMELINE_MEDIA/` | Assigned | Built (ffprobe) | Delta | Engine | Status |
|---|---|---|---|---|---|---|
| **01** | `01_00m00s_to_00m20s_hook_buy_button_shatter.mp4` | 20.00s | 20.00s | +0.00s | Manim (1080p60) | **PASS** |
| **02** | `02_00m20s_to_00m38s_pace_statement_progress_bar.mp4` | 18.24s | 18.27s | +0.03s | Manim (1080p60) | **PASS** |
| **03** | `03_00m38s_to_01m03s_illusion_ticket_to_zero_loupe.mp4` | 25.16s | 25.17s | +0.01s | Manim (1080p60) | **PASS** |
| **04a**| `04_01m03s_to_01m07s_flow_hft_server_rack_corridor.mp4` | 3.60s | 3.60s | +0.00s | Flow Placeholder | **PASS** |
| **04b**| `04_01m07s_to_01m36s_order_routing_citadel_virtu.mp4` | 29.84s | 29.87s | +0.03s | Manim (1080p60) | **PASS** |
| **05** | `05_01m36s_to_02m11s_bid_ask_spread_order_book.mp4` | 34.96s | 34.97s | +0.01s | Manim (1080p60) | **PASS** |
| **06** | `06_02m11s_to_02m47s_pfof_kickback_revenue_chart.mp4` | 35.24s | 35.27s | +0.03s | Manim (1080p60) | **PASS** |
| **07a**| `07_02m47s_to_02m50s_flow_institutional_trading_floor.mp4`| 3.46s | 3.47s | +0.01s | Flow Placeholder | **PASS** |
| **07b**| `07_02m50s_to_03m20s_sec_65m_penalty_settlement.mp4` | 29.66s | 29.67s | +0.01s | Manim (1080p60) | **PASS** |
| **08** | `08_03m20s_to_03m53s_compounding_penny_500_trade_grid.mp4` | 33.32s | 33.33s | +0.01s | Manim (1080p60) | **PASS** |
| **09** | `09_03m53s_to_04m23s_nbbo_vs_pfof_price_ladder.mp4` | 29.52s | 29.53s | +0.01s | Manim (1080p60) | **PASS** |
| **10** | `10_04m23s_to_04m59s_three_defense_steps_limit_orders.mp4` | 36.88s | 36.90s | +0.02s | Manim (1080p60) | **PASS** |
| **11** | `11_04m59s_to_05m16s_loop_ledger_four_checkmarks.mp4` | 16.92s | 16.93s | +0.01s | Manim (1080p60) | **PASS** |
| **12a**| `12_05m16s_to_05m20s_flow_macro_phone_trade_confirmation.mp4`| 3.70s | 3.70s | +0.00s | Flow Placeholder | **PASS** |
| **12b**| `12_05m20s_to_05m37s_cta_end_card_clear_zones.mp4` | 16.62s | 16.63s | +0.01s | Manim (1080p60) | **PASS** |

**Total V1 Track Runtime**: 337.30s (Assigned: 337.12s, net delta +0.18s across 15 clips, container packet alignment only).  
**Total Deficit Recovered**: +112.11 seconds of missing animation natively authored.

---

## 2. QA Gate Result
- `pipeline/qa/layout_qa.py`: **PASS (0 failures)**
  * Pop-up Contract: PASS (32 items verified, LRU slot rotation, zero time overlap, zero caption lane collisions).
  * Dynamic Font Scaling: PASS (every 3-4 word chunk <= 540px within 560px contract, zero clipped text).
  * Manim Stage Containment: PASS (zero non-chrome pixels outside x: [96, 1824], y: [190, 856]).
  * Text Colors & Contrast: PASS (Nohemi bold/medium, contrast >= 7:1 against #202322).

---

## 3. Flow Placeholder List (Awaiting Sahand's Renders)
1. `04_01m03s_to_01m07s_flow_hft_server_rack_corridor.mp4` (3.60s) — HFT Server Rack Corridor
2. `07_02m47s_to_02m50s_flow_institutional_trading_floor.mp4` (3.46s) — Institutional Trading Floor at Dusk
3. `12_05m16s_to_05m20s_flow_macro_phone_trade_confirmation.mp4` (3.70s) — Macro Smartphone Trade Confirmation

---

## 4. Visual Verification Artifacts
- Pop-up Screenshots: 6 extracted in `screenshots/popup_*.png`
- Scene Screenshots: 36 extracted (start, mid, end for all 12 scenes) in `screenshots/Scene*_*.png`
