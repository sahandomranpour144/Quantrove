# Workspace Audit & Style Verification Report
Date: 2026-09-22
Author: Quantrove Assistant (Pair Programmer with Sahand)

---

## Task 1: EP03 Shorts Build Status

| Short Slug | File Path & Location | Status | Style System Version |
|---|---|---|---|
| `ep03_short_algorithm_hook` | `01_PROJECTS/YOUTUBE/shorts/ep03_short_algorithm_hook/ep03_short_algorithm_hook.mp4` | **Fully Rendered** (16.65s, 1080x1920 @ 60fps, QA: PASS) | **NEW** (shorts_v2, Nohemi 700/500, #202322/#E6EDF3/#C3D809/#FD802E). Note: `assembly_notes.md` has stale v1 text. |
| `ep03_short_clicks_to_watchtime` | `01_PROJECTS/YOUTUBE/shorts/ep03_short_clicks_to_watchtime/ep03_short_clicks_to_watchtime.mp4` | **Partial / Corrupt Export** (File is audio-only WAV renamed .mp4 due to `normalize_to_minus_14` bug; raw 9x16 exists) | **NEW Spec / Broken Render** (v2 `text_events.json` ready, but final MP4 composite missing video stream). |
| `ep03_short_rabbit_hole` | `01_PROJECTS/YOUTUBE/shorts/ep03_short_rabbit_hole/` (No final MP4 exists; has `concat_vid.mp4` & 338MB `overlay.mov`) | **Partial / Uncomposited** (Overlay & video segments rendered, but final ffmpeg composite step not run) | **NEW Spec / Incomplete** (v2 overlay & text events rendered, cold open prepended, final composite needed). |

---

## Task 2: Workspace Audit (Inventory of Overhead)

### 1. Connected MCP Servers & Plugins
| Name | Purpose | Used Recently? | Weight | Recommendation |
|---|---|---|---|---|
| `youtube_studio_mcp` | Remote YouTube Studio management (29 tools) | N | High | **Disable** (load only during live publishing) |
| `brightdata-plugin` | Web scraping, proxy, SERP SDKs (21 skills) | N | High | **Remove / Disable** (never used, huge prompt overhead) |
| `browser-use` | Direct browser automation via CDP | N | Med | **Disable** (enable only during visual research tasks) |
| `postiz` | Social media posting (28+ networks) | N | Low | **Remove / Disable** |
| `claude-code-setup` | Automation recommender plugin | N | Low | **Disable** |
| `codebase-memory-mcp` | Graph memory indexer (in `.claude.json`) | N (disconnected) | High | **Remove config** (referenced in CLAUDE.md banner but offline) |
| `filesystem` (MCP) | Local file operations via MCP | N | Med | **Remove config** (redundant with native Read/Write/Grep/Glob) |
| `sequential-thinking` | Reasoning tool server | N | Low | **Remove config** |
| `mcp_ccd_*` | Claude Desktop window, session & sidebar mgmt | Y | Med | **Keep** (core desktop UI functions) |
| `mcp_terminal_*` | Interactive desktop terminal view | Y | Low | **Keep** |
| `mcp_Claude_Browser_*` | Built-in preview server | N | Med | **Keep** |

### 2. Hooks & Automation Overhead
| Name | Purpose | Used Recently? | Weight | Recommendation |
|---|---|---|---|---|
| `PreToolUse: Bash (prompt: Gate 1)` | LLM prompt evaluating Gemini/Flow gen | Y (fires on ALL bash) | **CRITICAL** | **Remove prompt hook** (causes massive quota drain on every command) |
| `PreToolUse: Bash (prompt: Gate 2)` | LLM prompt evaluating final render | Y (fires on ALL bash) | **CRITICAL** | **Remove prompt hook** (duplicate of python regex gate) |
| `gate_gemini_flow.py` | Command hook logging generation attempts | Y | Low | **Keep regex command hook only** |
| `gate_final_assembly.py` | Command hook logging assembly attempts | Y | Low | **Keep regex command hook only** |
| `verify_manifest_durations.py` | Validates durations against ffprobe | Y (runs on every Write) | Med | **Refine matcher** (run only on manifests/timelines, not all writes) |
| `gate2_shorts_qa.py` (Write hook) | Validates QA before publish | Y (runs on every Write) | Med | **Remove from Write/Edit** (keep only on publish command) |
| `gate2_longs_qa.py` (Write hook) | Validates QA before publish | Y (runs on every Write) | Med | **Remove from Write/Edit** (keep only on publish command) |

### 3. Agents & Skills
| Name | Purpose | Used Recently? | Weight | Recommendation |
|---|---|---|---|---|
| `orchestrator`, `content`, `content-editor`, `builder`, `video-qa`, `research` | Core YouTube production team | Y | Low | **Keep** (fix tool references & update palette in `video-qa`/`content`) |
| `product` | Product / MVP definition | N | Low | **Keep** |
| `ml-mentor` | Adversarial ML advisor | N | Low | **Keep** (or archive to `02_KNOWLEDGE/ML`) |
| `trade-journal-reviewer` | Trading performance auditor | N | Low | **Keep** (or archive to `03_TRADING_AI`) |
| 8 Core YouTube Skills (`shorts-qa`, `shorts-extraction`, `duration-check`, etc.) | Core video pipeline playbooks | Y | Low | **Keep** |
| `pre-publish-checklist` | General pre-publish list | N | Low | **Merge into `video-qa` / Remove** |
| 4 Trading / ML Skills (`backtest-harness`, `trade-journal-entry`, `chart-read`, `ml-experiment-log`) | Trading/ML playbooks | N | Med | **Keep or archive** depending on current CEO focus |

### 4. CLAUDE.md & Rules Overhead
| Section / File | Purpose | Used Recently? | Weight | Recommendation |
|---|---|---|---|---|
| `CLAUDE.md` §3 (Rules 3.1-3.9) | Full duplicate text of `.claude/rules/*.md` | Y | High | **Trim** to 1-line pointers (cuts ~80 lines from every prompt) |
| `CLAUDE.md` top banner | Codebase-memory-mcp warning | Y | Med | **Remove** (tool is inactive, banner burns tokens) |
| 14 Rule files in `.claude/rules/` | Auto-loaded system instructions | Y | High | **Consolidate** overlapping rules (e.g. merge text/visual rules) |

---

## Task 3: Efficiency Pass (Proposed Action List)

1. **Eliminate LLM Prompt Hooks in `settings.local.json`** (Impact: ~30-50% reduction in API calls & latency).
2. **Disable Unused Plugins (`brightdata`, `browser-use`, `postiz`, `claude-code-setup`)** (Impact: Saves ~3,000-5,000 system prompt tokens per turn).
3. **Disable / On-Demand `youtube_studio_mcp`** (Impact: Drops 29 tool schemas from every API request).
4. **Remove Unused/Dormant MCP Server Configs in `.claude.json`** (`codebase-memory-mcp`, `filesystem`, `sequential-thinking`).
5. **Optimize `Write|Edit` Tool Hooks** (Restrict `verify_manifest_durations.py` to manifest files; remove `gate2_*_qa.py` from Write/Edit so it runs only before publish).
6. **Trim `CLAUDE.md` by ~50%** (Remove duplicated rule text, prune outdated map/dates, eliminate dormant MCP instructions).
7. **Clean Stale Color References in Agent & Rule Files** (Update `video-qa.md`, `content.md`, `kinetic-popups.md`, and `shorts-extraction/SKILL.md` to Institutional Data Intelligence tokens).

---

## Task 4: New Style Verification (Audit Evidence)

| Item | Status | Evidence (File & Line) |
|---|---|---|
| **Palette in `shorts_style.json`** | **Applied** | `01_PROJECTS/YOUTUBE/pipeline/config/shorts_style.json:8-16` (`#202322`, `#233D4C`, `#C3D809`, `#FD802E`, `#E6EDF3`) |
| **Palette in `longs_style.json`** | **Applied** | `01_PROJECTS/YOUTUBE/pipeline/config/longs_style.json:13` (`#202322`, `#233D4C`, `#C3D809`, `#FD802E`, `#E6EDF3`) |
| **Palette in Brand Configs** | **Applied** | `brand/brand_tokens.json:11-16`, `brand/brand-style.md:21-27`, `brand/manim_theme.py:17-22`, `remotion_engine/src/brandTokens.ts:1-15` |
| **Palette in Rules & Agents** | **Partially Applied** | **Old colors lingering in**: `.claude/agents/video-qa.md:24`, `.claude/agents/content.md:39`, `.claude/rules/kinetic-popups.md:10` (`#FFEE00`), `.claude/skills/shorts-extraction/SKILL.md:53` (`#FFEE00`), `02_KNOWLEDGE/00_CORE/rules/AGENT_RULES.md:148` |
| **Font: Nohemi replacing Inter** | **Applied in Configs** | `shorts_style.json:3-4`, `longs_style.json:13`, `brand/brand_tokens.json:57-58`, `ShortsV2TextLayer.tsx:12-16`. (Note: `shorts-extraction/SKILL.md:52` still mentions Poppins/Montserrat). |
| **Shorts Spec v2 (4-beat structure)** | **Applied** | `shorts-style.md:23` (R7), `shorts_style.json:65`, `shorts_qa.py:380-400` |
| **Shorts Spec v2 (3-4 word chunks)** | **Applied** | `shorts-style.md:17` (R5/R6), `shorts_style.json:20`, `shorts_qa.py:306,349` |
| **Shorts Spec v2 (Blur-up entrance & hard cuts)** | **Applied in Code / Manual in QA** | `shorts_style.json:32,36`, `ShortsV2TextLayer.tsx:270-293` (blur-up translateY/blurPx), `ShortsV2TextLayer.tsx:201` (hard cut). `shorts_qa.py` delegates animation check to R10 Manual Review. |
