# Quantrove YouTube Production State

## Episodes
| Slug | Status Tag | Next Action | Key File Paths |
|---|---|---|---|
| long01_why_stock_market_crashes | [PUBLISHED 2026-09-02] | None (archive/monitor) | `longs/[PUBLISHED 2026-09-02]_long01_why_stock_market_crashes/` |
| long02_50_years_recession_data | [PUBLISHED 2026-09-09] | None (archive/monitor) | `longs/[PUBLISHED 2026-09-09]_long02_50_years_recession_data/` |
| long03_how_algorithms_decide | [PUBLISHED 2026-09-16] | Cleanup dry-run ready; awaits CEO | `longs/[PUBLISHED 2026-09-16]_long03_how_algorithms_decide/` |
| long04_can_ai_predict_markets | [PUBLISHED 2026-09-26] | None (live on YouTube: jwPcJSfDQPg) | `longs/[PUBLISHED 2026-09-26]_long04_can_ai_predict_markets/` |
| long05_market_making_illusion | [PUBLISHED 2026-09-30] | Confirmed Live on YouTube (-SH2kNLF3WA) | `longs/[PUBLISHED 2026-09-30]_long05_market_making_illusion/` |
| long06_hft_microsecond_pricing | [SCHEDULED 2026-10-04] | Final uploaded; UNLISTED in Studio until Sun 2026-10-04, then public. Do not touch. | `longs/[SCHEDULED 2026-10-04]_long06_hft_microsecond_pricing/` |
| long07_ai_words_geometry | [IN_PROGRESS 2026-10-02] | **GATE 1 awaiting CEO**: script + 46-scene/229-beat shot list, ≈10:59 | `longs/[IN_PROGRESS 2026-10-02]_long07_ai_words_geometry/EP07_SCRIPT_AND_SHOTLIST.md` |
| long08_attention_transformer | [IN_PROGRESS 2026-10-02] | **GATE 1 awaiting CEO**: script + 45-scene/219-beat shot list, ≈10:45; publish after EP07 | `longs/[IN_PROGRESS 2026-10-02]_long08_attention_transformer/EP08_SCRIPT_AND_SHOTLIST.md` |
| ep01_short_margin_call | [PUBLISHED] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep01_short_margin_call/` |
| ep01_short_trigger_changes | [PUBLISHED] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep01_short_trigger_changes/` |
| ep02_short_2009_bottom | [PUBLISHED] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep02_short_2009_bottom/` |
| ep02_short_best_day_to_invest | [PUBLISHED 2026-09-14] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep02_short_best_day_to_invest/` |
| ep02_short_smart_money_panic | [PUBLISHED] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep02_short_smart_money_panic/` |
| standalone_short_ai_letter_blindspot | [PUBLISHED] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_standalone_short_ai_letter_blindspot/` |
| ep03_short_algorithm_hook | [PUBLISHED 2026-09-22] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep03_short_algorithm_hook/` |
| ep03_short_clicks_to_watchtime | [PUBLISHED 2026-09-24] | None (live on YouTube) | `shorts/_ARCHIVE/published/[UPLOADED]_ep03_short_clicks_to_watchtime/` |
| ep03_short_rabbit_hole | [PUBLISHED 2026-09-25] | None (live on YouTube: E0ta91FyIAI) | `shorts/_ARCHIVE/published/[UPLOADED]_ep03_short_rabbit_hole/` |
| ep04_shorts (5 published) | [PUBLISHED 2026-09-27..29] | None (all 5 live on YouTube: 1xv9s, R7L_5, -TMK9, tP7F, PIsxfdkx4Q8) | `shorts/_ARCHIVE/published/[UPLOADED]_ep04_*/` |
| ep05_shorts (5) | [PUBLISHED / SCHEDULED] | 01, 03 live (archived); 02 (10-02), 04 + 05 (10-03) scheduled | `shorts/02,04,05_*/` + `shorts/_ARCHIVE/published/01,03_*` |
| ep06_shorts_package (4) | [QA_PASSED] | Sahand uploads manually AFTER EP06 goes public (2026-10-04) | `shorts/06..09_*_ep06_*/` |

## Review Gates
- Gate 1: CEO humanized script (quantrove-script-humanizer) + 4-engine classification (Manim/Remotion/Flow/html_motion) | Gate 2: Rendered assets verification

## Topic Strategy System
- Architecture: 4 Permanent Pillars + Season 1 Active (~10-15 eps, min 3 longs/pillar) + Season Boundary Review (CEO Enacted 2026-09-29)
- Framework: 6-dimension 100-point scoring (`topic_strategy/QUANTROVE_TOPIC_STRATEGY.md`)
- Database: `topic_strategy/Quantrove_Topic_Database.xlsx` (6 sheets, formulas, dropdowns)
- Ideas: `topic_strategy/IDEAS_AND_BRAINSTORMS.md` | Builder: `topic_strategy/build_topic_database.py`

## Standards, QA & Artifacts
- Brand: #202322, #233D4C, #C3D809, #FD802E, #E6EDF3 | Font: Nohemi (Inter fallback)
- QA: `ep_beatcheck.py` (density/runtime, `--sync` rebuilds shot list) | `longs_qa.py` | `shorts_qa.py` | `html_motion_qa.py` | `test_script_humanizer.py`
- Memory: `MEMORY.md` | Log: `CHANGELOG.md` | Reports: `reports/` | Logs: `logs/`
