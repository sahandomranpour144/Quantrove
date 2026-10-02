# Quantrove AI Studio — Side Assistant Operational Brief (GPT / Grok)

> **Purpose**: Read-only operational handoff for external assistants (GPT, Grok) collaborating on the Quantrove workspace.
> **Scope**: High-density reference covering standards, paths, review gates, brand tokens, and operational rules.
> **Workspace Root**: `E:\Agentic Workspaces\ClaudeCode\`

---

## 1. Channel Snapshot

| Dimension | Specification | Reference |
|---|---|---|
| **Channel Name** | Quantrove (`@Quantrove`) | `CLAUDE.md` §1 |
| **Owner / CEO** | Sahand (Sole decision-maker; one-person AI enterprise) | `HOW_TO_RUN_THIS_COMPANY.md` |
| **Positioning** | Faceless, data-driven documentary style. "Institutional Data Intelligence" — Bloomberg-terminal precision, high data density, statistical rigor. Zero stock footage or hype. | `brand/brand_tokens.json` |
| **Format** | Faceless video: Manim math animations, Flow/Veo cinematic B-roll, kinetic captions. | `CLAUDE.md` §1 |
| **Voiceover** | ElevenLabs ("Adam") or Gemini TTS (per-project choice by Sahand; never assume). Tone: calm, authoritative. | `CLAUDE.md` §7 |
| **Pacing** | Longs: Relaxed (130–145 WPM) / Focused (150–165 WPM). Shorts: 145–160 WPM (0.3–0.5s pause between ideas). | `longs_style.json`, `shorts_style.json` |
| **Cadence** | **Longs**: Wed 10:00 AM ET (14:00 UTC). **Shorts**: Mon (hook), Tue (teaser), Thu (extract #1), Fri (extract #2), Sat (extract #3). Sun (batching). Slot mapping for 2 native + 1-2 extracted under the 2026-09-22 rule: UNDECIDED. The schedule file still lists 3 extraction slots (Thu/Fri/Sat). | `WEEKLY_PUBLISHING_SCHEDULE.md` |
| **Unlisted Buffer** | Long-form uploaded Unlisted at 06:00 AM ET (4h pre-premiere) for VP9/AV01 4K/1080p60 encoding. | `WEEKLY_PUBLISHING_SCHEDULE.md` §2 |
| **4 Pillars** | 1. 🤖 **AI & ML Real World** \| 2. 📈 **AI + Finance + Trading** \| 3. 💰 **Finance Simplified** \| 4. 📊 **Data Stories** (Strict rotation). | `CLAUDE.md` §2 |
### CEO Experiments in Progress (added by Sahand, 2026-09-23). These OVERRIDE the Cadence row above.
- **Upload-day test:** Sahand is testing different upload days and times. The Wed 10:00 AM ET cadence is a baseline, NOT fixed. EP04 is deliberately scheduled for Saturday 2026-09-26. Do not "correct" days back to Wednesday. Do not recommend a fixed day unless asked. Analyze results only from data Sahand pastes.
- **EP03 re-upload experiment:** EP03 (long03_how_algorithms_decide) was deleted and re-uploaded around 2026-09-21 to test whether it gains more views. Its analytics start at the re-upload; the original 2026-09-16 data is gone. Any EP03 ID or date from before the re-upload is obsolete. Treat EP03 comparisons as a single before/after test with confounders (new day, new time, reset history).
- **Shorts slot mapping (2 native + 1-2 extracted):** Sahand decides this himself. Do not propose a weekly schedule unless asked.
---

## 2. Episode Status Inventory

*Compiled from folder names, `01_PROJECTS/YOUTUBE/STATE.md`, `CHANGELOG.md`, and `publishing_plan/WEEKLY_PUBLISHING_SCHEDULE.md`.*

### Long-Form Episodes (`longs/`)

| Ep # | Title / Topic | Pillar | Folder / Path | Status | YouTube ID |
|---|---|---|---|---|---|
| **EP01** | Why Stock Market Crashes Happen | 📊 Data Stories | `1. [PUBLISHED 2026-09-02] long01_why_stock_market_crashes` | Published (2026-09-02) | UNKNOWN |
| **EP02** | 50 Years of Recession Data | 📊 Data Stories | `2. [PUBLISHED 2026-09-09] long02_50_years_recession_data` | Published (2026-09-09) | UNKNOWN |
| **EP03** | Recommendation Algorithms | 🤖 AI/ML Real World | `3. [PUBLISHED 2026-09-16] long03_how_algorithms_decide` | re-uploaded ~2026-09-21 (views experiment; see CEO Experiments) | `nx0oF7pxjds` |
| **EP04** | Can AI Predict Markets? | 📈 AI + Finance | `[PUBLISHED 2026-09-26]_long04_can_ai_predict_markets` | Published (2026-09-26) | `jwPcJSfDQPg` |
| **EP05** | Why "Free" Trading Isn't Free | 💰 Finance Simple | `5. [Published 2026-09-30]_long05_market_making_illusion` | Published / Uploaded (2026-09-30, ID: `-SH2kNLF3WA`; Studio verification required) | `-SH2kNLF3WA` |
| **EP06** | The Machines Trading Before You Blink | 📈 AI + Finance | `[IN_PROGRESS 2026-09-30]_long06_hft_microsecond_pricing` | In Progress (VO 420.91s, Flow & HTML verified; Manim awaits Gate 1) | TBD |
| **EP07** | Attention in Neural Networks / TBD | 🤖 AI/ML Real World | UNKNOWN [No folder] | Planned (Roadmap: Oct 14) | UNKNOWN |
| **EP08** | Dot-Com Bubble Raw Data / TBD | 📊 Data Stories | UNKNOWN [No folder] | Planned (Roadmap: Oct 21) | UNKNOWN |

### Short-Form Episodes (`shorts/`)

| Slug / Folder | Origin | Status | YouTube ID |
|---|---|---|---|
| `archived/[UPLOADED]_ep01_short_margin_call` | EP01 Extract | Published / Archived | UNKNOWN |
| `archived/[UPLOADED]_ep01_short_trigger_changes` | EP01 Extract | Published / Archived | UNKNOWN |
| `archived/[UPLOADED]_ep02_short_2009_bottom` | EP02 Extract | Published / Archived | UNKNOWN |
| `archived/[UPLOADED]_ep02_short_best_day_to_invest` | EP02 Extract | Published (2026-09-14) | UNKNOWN |
| `archived/[UPLOADED]_ep02_short_smart_money_panic` | EP02 Extract | Published / Archived | UNKNOWN |
| `archived/[UPLOADED]_standalone_short_ai_letter_blindspot` | Standalone AI | Published / Archived | `LfDIFgQaFL8` |
| `archived/[UPLOADED]_ep03_short_algorithm_hook` | EP03 Extract | Published (2026-09-22) | `ps7d0Qwz760` |
| `[SCHEDULED 2026-09-24]_ep03_short_clicks_to_watchtime` | EP03 Extract | Scheduled (2026-09-24) | `wDeqACCW4p0` |
| `[SCHEDULED 2026-09-25]_ep03_short_rabbit_hole` | EP03 Extract | Scheduled (2026-09-25) | `E0ta91FyIAI` |
| `[SCHEDULED 2026-09-27]_ep04_short_alpha_decay_death` | EP04 Extract | Scheduled (2026-09-27) | `1xv9sEeDAFo` |
| `[SCHEDULED 2026-09-28]_ep04_short_where_wall_street_uses_ai` | EP04 Extract | Scheduled (2026-09-28) | `nUd2oq6QWdg` |
| `[IN_PROGRESS 2026-09-23]_ep04_short_simons_5075_edge` | EP04 Extract | Uploaded Unlisted (Awaits date) | `fI8HnX9NVrM` |
| `[IN_PROGRESS 2026-09-23]_ep04_short_cat_vs_market_reflexivity` | EP04 Extract | Uploaded Unlisted (Awaits date) | `8eNIMgcangM` |
| `[IN_PROGRESS 2026-09-23]_ep04_short_reflexivity_cat` | EP04 Extract | In Progress (Raw cut ready) | UNKNOWN |
| `[IN_PROGRESS 2026-09-23]_ep04_short_99pct_backtest_trap` | EP04 Extract | In Progress (Raw cut ready) | UNKNOWN |
| `[NOT_UPLOADED]_short_standalone_head_and_shoulders` | Standalone Quant | Ready / Not Uploaded | UNKNOWN |
| `[NOT_UPLOADED]_short_standalone_medallion_fund` | Standalone Quant | Ready / Not Uploaded | UNKNOWN |

---

## 3. Brand System & Visual Tokens

Single source of truth: `brand/brand_tokens.json` (v2.0.0).

### 5-Color Institutional Palette

| Token | Hex | Role | Strict Restrictions |
|---|---|---|---|
| **BACKGROUND** | `#202322` | Raisin Black | Canvas background, dark surfaces, badge text. |
| **UI_STRUCTURE** | `#233D4C` | Charcoal Slate | Grid lines, borders, chrome, dividers. **NEVER text** (contrast failure). |
| **SUCCESS** | `#C3D809` | Power Lime | Positive validation, upward moves, green candles, keyword emphasis. |
| **RISK** | `#FD802E` | Pumpkin | Downward moves, red candles, anomalies, outliers, risk keywords. |
| **TEXT** | `#E6EDF3` | Off-White | Primary text, titles, numbers, wordmarks, badge background. |

### Typography & Styling Rules
- **Font**: `Nohemi` (clean geometric sans-serif); fallback `Inter`.
- **Weights**: Bold (`700`) for titles, numbers, key terms, risk metrics, kinetic pops. Medium (`500`) for body/captions. *Never <500*.
- **Contrast**: >=7:1 against `#202322`. Direction: Up = Power Lime (`#C3D809`), Down/Risk = Pumpkin (`#FD802E`).

### What to Avoid
- **NO generic red/green** (`#FF0000`, `#00FF00` banned; use Pumpkin and Power Lime).
- **NO Charcoal Slate text**: `#233D4C` is lines and chrome ONLY.
- **NO yellow fill boxes** behind captions.
- **NO decorative, serif, or script fonts**.
- **NO unscaled Manim bold text**: Triggers Pango glyph scattering (`m ar ket`).
- **NO legacy dark luxury palette**: `#0B0F19`, `#00F0FF`, `#00FFA3`, `#FFD700`, `#FF3366` are obsolete.

---

## 4. Shorts Standing Specifications & Sourcing Rule

Governing references: `.claude/rules/shorts-style.md`, `pipeline/config/shorts_style.json`, `.claude/rules/shorts-archive-on-upload.md`.

### Sourcing Rule: Hybrid Native & Extracted (CEO Directive, 2026-09-22)
- **Per episode**: 2 NEW native Shorts (generated with Manim or other non-Flow tools, keeping that episode's concepts) + 1-2 Shorts EXTRACTED from the existing long-form footage, prioritizing segments that contain Manim animation.
- **Flow-generated video**: Avoided for Shorts unless necessary.
- **Core goal**: Shorts must not feel like generic AI-generated content; they must be crafted enough that viewers stay locked to the screen.
- **Narrative mapping**: Native Shorts follow the 4-beat structure (idea, simple/wrong version, complex/wrong version, reveal). Extractions pick segments that already contain a reveal.
- **Extraction mechanics**: Extraction mechanics (pure cuts via `ffmpeg`, blur-pad 9:16 reframe, never crop charts, no synthetic VO) apply ONLY to the extracted Shorts.

### Shorts Rules (R1–R10)
- **R1 (Hook)**: Value spoken AND visible within 3.0s. First word <0.5s. Text at 0.0s. No logo/intro.
- **R2 (Freeze Ceiling)**: No static frame >3.5s (max 5.0s if tagged `HOLD_FOR_UNDERSTANDING`).
- **R3 (Audio Mix)**: Voice -14 ± 1.5 LUFS. Music >=16 dB below voice (target 18–20 dB), ducked, no lyrics.
- **R4 (Pacing)**: 145–160 WPM. 0.3–0.5s pause between ideas. No hype words.
- **R5 & R6 (Unified Text)**: **3–4 word chunks ARE the captions**. No separate subtitles.
  - Safe zone: Y 60–76%, max 2 lines, safe bottom 20%, safe right 15%.
  - Palette: `#E6EDF3` text, `#C3D809` emphasis (max 1/chunk), `#FD802E` risk.
  - Animation: `fade_blur_up` (10–15px travel, 180–250ms, hard cut exit). Zero glow, stroke, or shadow.
- **Insight Badge**: Max 1 per short on `INSIGHT` beat. Y 42–52%, max 3 words uppercase, `#E6EDF3` badge with `#202322` text, hold 1.2–1.8s.
- **R7 (Structure)**: 30–45s duration. 4 beats: `IDEA` → `SIMPLE_WRONG` → `COMPLEX_WRONG` → `INSIGHT`.
- **R8 (Motion)**: Continuous math motion; camera push scale <=1.08 with stated purpose; Flow clips <=20% runtime.
- **R9 (Clean Exit)**: Cut <=1.0s after last word. **Zero spoken CTA, zero outro card**. Banned: *"subscribe", "like", "follow", "comment", "link in bio"*.
- **R10 (QA Gate)**: Verified via `python pipeline/qa/shorts_qa.py <short_dir>`.

---

## 5. Long-Form Standing Rules (L1–L8)

Governing references: `.claude/rules/longs-style.md`, `pipeline/config/longs_style.json`, `.claude/rules/hook-discipline.md`.

- **L1 (Packaging First)**: Research 5–8 references (`thumbnail-research`). Draft >=3 concepts (Nohemi, max 3 words, brand palette). Zero competitor pixels. Lock title + thumbnail before scripting.
- **L2 (Hook Discipline)**: First 5.0s must state click reason and include >=2 title keywords spoken and visible. Cold open <=35s.
- **L3 (Pace & Runtime)**: State pace mode within 5–20s:
  - *Relaxed*: 130–145 WPM (*"Get comfortable, this one is worth going slowly."*).
  - *Focused*: 150–165 WPM (*"In the next {N} minutes, I will show you exactly {promise}."*).
  - Promised runtime in minutes must match measured runtime within ±1 min.
- **L4 (Narrative Architecture)**: 3–5 chapters. Every chapter delivers: mini-hook, partial payoff, and new loop.
- **L5 (Loop Ledger)**: Maintain 4–5 open loops. First payoff <=90s. >=2 loops open between 10%–80% runtime. Primary loop resolves at 80%–95%. 100% closed before ending.
- **L6 (Pattern Interrupts)**: Visual or auditory interrupt every <=40s.
- **L7 (Disciplined CTA)**: Exactly ONE spoken CTA between T-45s and T-20s (duration <=25s). Formula: `Action + Reason + Next Video`. Forbidden before first payoff. End screen final 20s clear of competing graphics.
- **L8 (Payoff Fidelity)**: Script must never promise what data cannot prove. Every claim mathematically resolved.
- **Kinetic Overlays**: CapCut Track V2 uses 60fps transparent RGBA MOV (`00_OVERLAY_..._kinetic_word_pops_60fps.mov`) from `all_words.json`. Max 6 words/event, safe margin >=5%.

---

## 6. Pipeline Architecture, Roles & Review Gates

### Division of Labor

| Role / Tool | Responsibilities | Key Rules |
|---|---|---|
| **Sahand (CEO)** | Approvals, manual Flow video prompting, VO choice, CapCut assembly, YouTube scheduling. | Sole decision-maker; signs Gates 1 & 2. |
| **AI Agents** | `/orchestrator` (routing), `/research` (validation), `/content` (scripts), `/builder` (Manim), `/content-editor` (Shorts), `/video-qa` (QA). | Propose and execute; CEO decides. |
| **Claude CLI** | File ops, ffprobe checks, faster-whisper alignments, status sync, cleanup manifests. | Zero automated API billing; token discipline. |
| **Google Flow** | Atmospheric/cinematic B-roll (`labs.google/flow` via Gemini/Veo). | **Manual-only by Sahand. Zero API billing**. |
| **CapCut Desktop** | Track V1 (Manim + Flow), Track V2 (60fps RGBA overlay), Audio (VO -14 LUFS, music -18dB ducked). | Final polish and master export. |

### The Two Mandatory CEO Review Gates

| Gate | Timing | Deliverables Reviewed by Sahand | Blocked Actions Until Approved |
|---|---|---|---|
| **Gate 1** | Prior to code or asset generation | 1. Script.<br>2. Shot list with **Manim vs. Flow** table.<br>3. Locked Title & Thumbnail concept. | Do NOT write render scripts, generate VO, or prompt Flow clips. |
| **Gate 2** | Prior to CapCut final assembly | 1. Rendered Manim charts.<br>2. Measured VO stems.<br>3. Flow B-roll inventory.<br>4. Kinetic overlay MOV files. | Do NOT assemble CapCut timeline or finalize publishing package. |

### Visual Tooling Distribution
- **Manim / Python**: Data, charts, mathematical curves, order book depth, algorithmic vector visualizations.
- **Google Flow**: Atmospheric, cinematic, narrative, and emotional B-roll clips. Never use Flow for charts or numbers.

---

## 7. Top Recurring Bugs & Lessons Learned

| Bug Class & Incident | Root Cause | Enforced Solution | Rule File |
|---|---|---|---|
| **Duration Drift** *(156s vs 384s)* | Hardcoding durations before measuring audio files. | **Duration Anchoring**: Probe audio with `ffprobe` before writing scenes or manifests. Never estimate. | `duration-anchoring.md` |
| **Subtitle Desync** | Calculating subtitle cuts via character counts or fractions. | **Word-Level Sync**: Always extract word timestamps with `faster-whisper` (`all_words.json`). | `word-level-transcription.md` |
| **Scope Creep / File Loss** | Unscoped edits overwriting CapCut notes or manual assets. | **Scoped-Task Locking**: Explicitly declare `IN SCOPE` and `LOCKED` boundaries before touching files. | `scoped-task-locking.md` |
| **Phantom Duplicate Assets** | Renaming/moving files without deleting the original source. | **Rename = Delete Old**: Every rename or move must delete the source file immediately. | `rename-delete-old.md` |
| **Pango Text Scattering** *(e.g. `m ar ket`)* | Rendering small bold Manim `Text()` objects. | **CleanText Scaling**: Render native Manim `Text()` at `ref_size=72` and scale down. | `cleantext-manim.md` |
| **Solid Black Pop-Up Box** | Exporting kinetic overlays in RGB instead of RGBA. | **Alpha Transparency**: Long-form overlays must export as 60fps QuickTime RLE with alpha (`yuva420p`/`rgba`). | `kinetic-popups.md` |
| **Diffusion Chart Artifacts** | Prompting AI video models (Flow) to render charts or numbers. | **Scene Classification**: Data/charts go to Manim. Story/atmosphere goes to Flow. Never mix. | `scene-classification.md` |

---

## 8. Standing Operational Rules

### 8.1 Post-Publish Cleanup
Governing file: `.claude/rules/post-publish-cleanup.md`.
When an episode transitions to `[PUBLISHED]`:
- **Retained Whitelist (Keep ONLY These)**: 1. Master export (`*.mp4` in root or `final/`), 2. Publishing metadata (`READY_TO_PUBLISH.md` or JSON) and thumbnail, 3. Master script and shot list (`*.md`).
- **Purged Assets**: `TIMELINE_MEDIA/` directory, kinetic overlay MOV files, temporary caption cuts, intermediate scene renders (`temp/`, `scenes/*.mp4`).
- **First-Run Confirmation Gate**: Claude outputs a dry-run manifest to `logs/cleanup_dryrun_<slug>_<date>.txt` and awaits Sahand's confirmation before deletion.

### 8.2 Shorts Archive on Upload
Governing file: `.claude/rules/shorts-archive-on-upload.md`.
- Confirmed uploaded/published Shorts folders must be moved to `01_PROJECTS/YOUTUBE/shorts/archived/`.
- Top-level `01_PROJECTS/YOUTUBE/shorts/` is strictly for active work (`[NOT_UPLOADED]`, `[IN_PROGRESS]`, `[SCHEDULED]`).

### 8.3 Folder Naming Conventions
- **Long-Form**: `longs/[STATUS YYYY-MM-DD]_<slug>` (`[IN_PROGRESS]`, `[SCHEDULED]`, `[PUBLISHED]`).
- **Shorts**: `shorts/[STATUS YYYY-MM-DD]_<slug>` (`[NOT_UPLOADED]`, `[IN_PROGRESS]`, `[SCHEDULED]`, `[UPLOADED]`).
- **Media Naming**: `TIMELINE_MEDIA/NN_XXmYYs_to_AAmBBs_<description>.<ext>`.

### 8.4 Token Discipline
Governing file: `.claude/rules/token-discipline.md`.
- Read `01_PROJECTS/YOUTUBE/STATE.md` first; avoid full directory scans.
- Never output tool responses >20 lines directly into chat; redirect to `logs/` or `reports/`.
- Never regenerate assets that pass `ffprobe` verification (Rule T9).
- Final reports: max 40 lines. Conclude sessions with `/clear` suggestion.

---

## 9. Standard Prompt Template for This Agent

```markdown
TASK: [Clear 1-sentence statement of deliverable]

IN SCOPE:
- [Exact file path or folder to create / edit]
- [Specific command or test to run]

LOCKED (DO NOT TOUCH):
- All episode folders except [target folder]
- TIMELINE_MEDIA/, master renders, existing video/audio files
- Pipeline code, .claude/ configuration, CLAUDE.md, and MEMORY.md
- No renames, moves, or deletes outside IN SCOPE targets
- Zero API calls to paid services or video diffusion models

RESOURCES & CONTEXT:
- Config: [pipeline/config/longs_style.json | shorts_style.json]
- Palette: brand/brand_tokens.json
- Target Script: [path/to/script.md]

REPORT BACK:
- Max 10 lines: changes made, verification result, next action.
```

---

## 10. Open Items & Next 5 Actions

*Current state as of 2026-09-23:*

1. **EP03 Post-Publish Cleanup Approval**: Dry-run manifest ready (`logs/cleanup_dryrun_long03_how_algorithms_decide_2026-09-23.txt`). Slated: 1,769 scratch files (1.08 GB) to purge; 14 whitelisted files preserved. Awaiting Sahand's Gate 1 go-ahead.
2. **EP04 Long-Form Release Monitoring**: Episode `long04_can_ai_predict_markets` scheduled in YouTube Studio for **2026-09-26 at 10:30 UTC** (`jwPcJSfDQPg`). Monitor premiere.
3. **EP05 Long-Form Production**: Complete. Released/Uploaded 2026-09-30 (ID: `-SH2kNLF3WA`). Measured runtime: 05m 37s.
   3a. **EP06 Long-Form Production**: In progress (`[IN_PROGRESS 2026-09-30]_long06_hft_microsecond_pricing`). ElevenLabs VO locked at 420.91s (07:00.91), 5 Flow clips verified on disk, 4 HTML motion packages verified on disk. 16 Manim scenes await Gate 1 CEO authorization. Master timeline locked to 440.91s (07:20.91).
4. **Scheduled Shorts Funnel Oversight**: Monitor scheduled releases:
   - `ep03_short_clicks_to_watchtime` (Sept 24, `wDeqACCW4p0`)
   - `ep03_short_rabbit_hole` (Sept 25, `E0ta91FyIAI`)
   - `ep04_short_alpha_decay_death` (Sept 27, `1xv9sEeDAFo`)
   - `ep04_short_where_wall_street_uses_ai` (Sept 28, `nUd2oq6QWdg`)
5. **Unlisted Shorts Release Scheduling**: Assign dates in YouTube Studio for `ep04_short_simons_5075_edge` (`fI8HnX9NVrM`) and `ep04_short_cat_vs_market_reflexivity` (`8eNIMgcangM`), then promote folder prefixes to `[SCHEDULED]`.

---

## 11. Glossary of Key Skills & Workspace Files

### Specialized Skills (`.claude/skills/`)

| Skill | One-Line Purpose |
|---|---|
| `duration-check` | Verify media durations via `ffprobe` to prevent timing drift. |
| `word-sync` | Generate word-level timestamps via `faster-whisper` for frame-accurate sync. |
| `scoped-task-lock` | Enforce explicit `IN SCOPE` vs `LOCKED` boundaries to protect manual edits. |
| `manim-text-fix` | Enforce native Manim `Text()` with `CleanText` vector scaling (`ref_size=72`). |
| `longs-scriptwriting` | Enforce long-form rules (L1–L8): hooks, pacing, loop ledgers, single CTA. |
| `shorts-extraction` | Cut 9:16 vertical Shorts from long-form masters with blur-pad reframing. |
| `shorts-qa` | Automated Gate 2 QA auditing freeze frames, loudness, WPM, and beats. |
| `thumbnail-research` | Deconstruct 5–8 reference videos and draft 3 original thumbnail concepts. |
| `episode-publish-package`| Generate verified YouTube metadata (titles, calibrated chapters, tags). |
| `pre-publish-checklist` | Final release audit: audio normalization, codecs, and end-screen clearance. |
| `backtest-harness` | Quantitative strategy backtesting with out-of-sample split enforcement. |
| `chart-read` | Multi-timeframe chart reading and liquidity breakdown framework. |
| `trade-journal-entry` | Structured trade thesis recording (R-multiples, execution, psychology). |
| `ml-experiment-log` | Scientific documentation of ML models, loss curves, and benchmarks. |

### Core Workspace Files

| File Path | One-Line Purpose |
|---|---|
| `CLAUDE.md` | Primary workspace orientation, CEO directives, and pillar cadence. |
| `01_PROJECTS/YOUTUBE/STATE.md` | Live ledger of episode lifecycle states and next actions. |
| `01_PROJECTS/YOUTUBE/CHANGELOG.md` | Audit log of folder renames, status promotions, and Studio syncs. |
| `brand/brand_tokens.json` | Single source of truth for 5-color palette and typography. |
| `pipeline/config/longs_style.json` | Machine-readable threshold config for long-form rules L1–L8. |
| `pipeline/config/shorts_style.json` | Machine-readable threshold config for Shorts rules R1–R10. |
| `02_KNOWLEDGE/00_CORE/decisions/DECISION_LOG.md` | Immutable record of CEO architectural and channel decisions. |
| `HOW_TO_RUN_THIS_COMPANY.md` | Operating manual defining agent fleet roles and SOP workflows. |
| `01_PROJECTS/YOUTUBE/instructions_and_workflows/SIMPLE_COMMANDS.md` | Command mappings showing automatic `IN SCOPE` / `LOCKED` boundaries. |
