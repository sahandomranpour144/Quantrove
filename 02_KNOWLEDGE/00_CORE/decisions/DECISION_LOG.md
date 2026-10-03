# DECISION LOG

Version:
1.0

Purpose:
Record important decisions made by the CEO and AI organization.

---

# Decision Format

## Date:

## Decision:

## Context:

## Options Considered:

## Reasoning:

## Final Choice:

## Impact:

## Status:

---

# Decisions

## Date: 2026-08-26
## Decision: Architecture and MVP Scope for VaultPulse AI
## Context:
Initiative to build a high-leverage finance application. Explored market dynamics, competitor weaknesses (Plaid connection instability, cloud privacy issues, rigid envelope rules), and local-first AI opportunities.
## Options Considered:
1. Cloud SaaS with Plaid aggregator connection (High liability, brittle connections).
2. Pure spreadsheet tool (Manual, lacks intelligence and forward forecasting).
3. **Local-First, Sovereign Financial Platform with Universal Statement Ingestion + Predictive 90D Runway Engine (Chosen).**
## Reasoning:
Provides highest privacy guarantees, eliminates broken sync complaints, works cross-platform via web, and uses deterministic calculations to prevent AI hallucinations.
## Final Choice: Option 3 (VaultPulse AI).
## Impact:
Delivered working production web app running on `http://localhost:5173/` with zero backend credential liabilities and client-side encrypted backup capabilities.
## Status: Approved by CEO (Sahand) and Fully Built.

---

## Date: 2026-09-05
## Decision: Launch & Architecture of YouTube Channel 2 (Viral Ranking Shorts)
## Context:
Sahand proposed starting a 2nd YouTube channel focusing on ranking short viral videos (life hacks, viral gadgets, clever inventions) to drive rapid subscriber acquisition, viral distribution, and monetization.
## Options Considered:
1. Tech/AI tools ranking (overlaps with Quantrove and limits top-of-funnel reach).
2. Raw compilation reposting with minimal overlays (HIGH RISK: 100% rejection from YouTube Partner Program under Reused Content policy).
3. **Transformative Editorial & Automated Ranking Pipeline (Chosen):** General viral life hacks / inventions / odd products with structured Tier-List / 1-10 scorecard graphics, original energetic voice commentary, watermark removal, fair-use 3-7s clip pacing, and automated programmatic video rendering.
## Reasoning:
Maximizes viral mass audience appeal without cannibalizing Quantrove, strictly complies with YouTube's 2025/2026 YPP transformative requirements, and enables rapid multi-video daily production through Python/FFmpeg automation.
## Final Choice: Option 3 (Independent Brand, General Viral & Hack Rankings).
## Impact:
Target launch setup with zero risk to main Quantrove brand; establishes separate high-velocity monetization asset.
## Status: Approved by CEO (Sahand).

---

## Date: 2026-09-06
## Decision: Quantrove YouTube Workspace Reorganization, 2-Month Master Roadmap & Episode Lifecycle Convention
## Context:
The `01_PROJECTS/YOUTUBE` workspace required cleanup and alignment with the newly finalized 2-Month Content Plan (`2_MONTH_CONTENT_PLAN.md`) and Playlist Architecture (`PLAYLIST_STRUCTURE.md`). Sahand confirmed Video 02 is scheduled in YouTube Studio, requested a dedicated `instructions_and_workflows` directory, and mandated explicit folder naming for episode lifecycles (`[IN_PROGRESS]`, `[SCHEDULED]`, `[PUBLISHED]`).
## Options Considered:
1. Ad-hoc file tracking with loose naming conventions.
2. Rigid database tracking outside file system.
3. **Structured In-Repo System (Chosen):** Centralized `instructions_and_workflows/` manual, standardized bracketed prefix directory tags (`[IN_PROGRESS]`, `[SCHEDULED]`, `[PUBLISHED]`), internal confirmation markers (`SCHEDULED.md`, `UPLOADED.md`), and automated Python CLI (`pipeline/manage_episode_status.py`).
## Reasoning:
Provides instantaneous visual status directly in the file tree, prevents duplicate rendering or accidental re-work, eliminates root clutter, and synchronizes the 4 content pillars with YouTube playlists.
## Final Choice: Option 3 (Structured In-Repo System).
## Impact:
Root directory cleared of clutter; EP02 marked `[SCHEDULED]`; EP01/Short01/Short02 marked `[PUBLISHED]`; centralized operational playbooks established; automated lifecycle CLI available.
## Status: Executed per CEO Directive.

---

## Date: 2026-09-12
## Decision: Mandatory Manim Visual Standard (CleanText Engine) & Kinetic Keyword Pop-Up Overlay Standard for All Videos
## Context:
In Episode 03 and Episode 04, significant visual enhancements were evaluated. GLM produced inspiration charts with high visual appeal, but earlier attempts suffered from Pango text quantization resulting in broken character spacing (e.g. `m ar ket`). Furthermore, Episode 03 demonstrated superior audience retention using 60fps kinetic keyword pop-up overlays. Sahand (CEO) mandated that all future videos (long-form and short-form) must strictly follow these two visual standards.
## Options Considered:
1. Ad-hoc styling per episode with standard Manim `Text(..., weight=BOLD)` (Rejected due to recurring font scattering and inconsistent brand appearance).
2. Manually keyframing hundreds of subtitle pops in CapCut (Rejected due to high human editing overhead and misalignment).
3. **Automated CleanText Vector Engine + Master 60fps Kinetic Keyword Overlay Track (Chosen)**:
   - Enforce Institutional Data Intelligence palette (`#202322`, `#233D4C`, `#C3D809`, `#FD802E`, `#E6EDF3`; Nohemi font) and `CleanText` vector scaling (`ref_size=72`, scaled down) across all Manim scripts.
   - Mandate dedicated 60fps transparent RGBA MOV kinetic keyword pop overlays (`00_OVERLAY_...mov` on CapCut Track V2) for long-form, and burned-in kinetic word pops for shorts.
## Reasoning:
Guarantees razor-sharp typography with zero character scattering across all rendering environments, maintains luxury Quantrove brand identity, and maximizes viewer retention through kinetic pop-in visual anchors without adding manual editing friction.
## Final Choice: Option 3 (Automated CleanText Vector Engine & Kinetic Keyword Pop-Up Standard).
## Impact:
Recorded into `ai-company-core.md`, `AGENT_RULES.md`, `COMPANY_KNOWLEDGE.md`, and `PROJECT_MEMORY.md`. All future episode pipelines will systematically implement these standards.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-09-27
## Decision: Mandatory Documentary Script Humanization Workflow Prior to Gate 1 CEO Review
## Context:
Raw AI script drafts risk defaulting to generic corporate/textbook writing patterns ("In today's world", "rapidly evolving landscape", "Definition -> Explanation -> Example") which flatten viewer engagement and damage Quantrove's cinematic documentary authority. Sahand mandated that all future long-form scripts must undergo a dedicated 4-pass humanization process before Gate 1 submission.
## Options Considered:
1. Ad-hoc editing during CapCut voiceover recording (Inefficient, leads to disjointed narration and pacing mismatch).
2. Manual rewriting by CEO only (Bottlenecks production velocity).
3. **Integrated 4-Pass Documentary Script Humanizer Workflow (Chosen)**:
   - Enforce 7 non-negotiable rules via `.claude/skills/quantrove-script-humanizer/SKILL.md` and `.claude/rules/script-humanization.md`.
   - Purge AI clichés; enforce Chapter Quad (Human Question -> Mystery/Problem -> Data Reveal -> Consequence); apply tension pivots ("The crash happened because..." -> "But something strange appears when we look at every crash together..."); adopt investigative observer voice; eliminate textbook pedagogy.
   - Mandatory prerequisite before presenting for Gate 1 CEO approval while strictly preserving quantitative accuracy, L1-L8 structure, and brand tokens.
## Reasoning:
Guarantees all Quantrove episodes sound like gripping, investigative financial documentaries (Bloomberg/Vox/Veritasium style) while maintaining mathematical rigor and eliminating AI writing artifacts.
## Final Choice: Option 3 (Integrated 4-Pass Documentary Script Humanizer Workflow).
## Impact:
Integrated into `CLAUDE.md`, `.claude/agents/content.md`, `.claude/skills/longs-scriptwriting/SKILL.md`, `HOW_TO_RUN_THIS_COMPANY.md`, and `VIDEO_PROMPTING_GUIDE.md`. All future scripts must pass humanization audit before Gate 1.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-09-29
## Decision: Quantrove Topic Strategy Architecture: Permanent Four Pillars vs. Season Boundary Narrative Design
## Context:
Previous topic strategy drafts elevated the Season 1 working arc (*Money → Markets → Algorithms → AI → Speed*) into a proposed working channel narrative architecture and drafted predetermined Season 2–4 roadmaps. Sahand (CEO) clarified the governing architecture: the four CEO-approved pillars (*AI & ML Real World*, *AI + Finance + Trading*, *Finance Simplified*, *Data Stories*) are the permanent channel architecture, while seasons are temporary narrative groupings designed only at season boundaries after reviewing completed work and empirical evidence.
## Options Considered:
1. Elevating *Money → Markets → Algorithms → AI → Speed* into a permanent channel architecture (Rejected: overly rigid, conflates temporary season themes with permanent channel scope, restricts organic topic selection).
2. Predetermining Season 2–4 episode roadmaps in advance (Rejected: assumes audience reception and topic performance before empirical data exists).
3. **Permanent Four-Pillar Content Architecture with Season Boundary Narrative Reviews (Chosen)**:
   - Pillars answer: *"What kind of content is Quantrove?"* (Permanent: *AI & ML Real World*, *AI + Finance + Trading*, *Finance Simplified*, *Data Stories*).
   - Seasons answer: *"What larger question or narrative connects this group of episodes?"* (Temporary: typical guideline, not a rule).
   - Season 1's arc (*Money → Markets → Algorithms → AI → Speed*) is preserved as historical documentation.
   - Future seasons are never predetermined; each new season is architected at the formal End-of-Season Review based on empirical evidence (views, retention, CTR, conversions, comments, callbacks).
   - Sahand (CEO) retains sole selection authority at the CEO Season Gate.
## Reasoning:
Maintains permanent editorial scope across the 4 approved pillars, prevents premature commitment to untested themes, grounds season planning in real audience data, and preserves narrative continuity without sacrificing strategic flexibility.
## Final Choice: Option 3 (Permanent Four-Pillar Content Architecture with Season Boundary Narrative Reviews).
## Impact:
Updated `QUANTROVE_TOPIC_STRATEGY.md`, `Quantrove_Topic_Database.xlsx`, `IDEAS_AND_BRAINSTORMS.md`, `STATE.md`, and `CLAUDE.md`.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-09-29
## Decision: Production Cadence Acceleration (2 Longs + 5–6 Shorts/Week), Weekly Pillar Focus & Outro Topic Decoupling
## Context:
To accelerate channel momentum and audience acquisition across the 4 permanent pillars, Sahand (CEO) evaluated production cadence, weekly playlist focus, and end-screen outro continuity. Previously, production was calibrated to 1 episode every 1–2 weeks with strictly sequential episode-to-episode topic teases in outro voiceovers.
## Options Considered:
1. Maintain 1 episode every 1–2 weeks with rigid outro topic teases (Slow growth, locks production sequence prematurely).
2. Daily unscripted releases without pillar discipline (Destroys Quantrove's documentary quality standard).
3. **Structured Cadence Acceleration with Weekly Pillar Focus & Generic Outro CTAs (Chosen)**:
   - **Cadence**: 2 long-form documentary episodes + 5–6 Shorts per week.
   - **Pillar Focus**: One pillar (playlist) per week, rotating through the 4 permanent pillars (*AI & ML Real World*, *AI + Finance + Trading*, *Finance Simplified*, *Data Stories*).
   - **Outro Decoupling**: From EP06 onward, an episode's outro must NOT announce or tease the specific next episode's topic. Use generic high-retention CTAs and playlist recommendations only.
## Reasoning:
Cadence acceleration drives channel velocity while weekly pillar batching maintains thematic focus for viewers and production efficiency. Decoupling the outro from the next episode's topic eliminates production bottlenecks, prevents out-of-order continuity breaks if schedules shift, and gives complete editorial agility while preserving L1–L8 quality standards.
## Final Choice: Option 3 (2 Longs + 5–6 Shorts/Week, One Pillar/Week, Generic Outro CTAs from EP06 Onward).
## Impact:
Updated `QUANTROVE_TOPIC_STRATEGY.md`, `CLAUDE.md` §2, and production scheduling guidelines.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-09-29
## Decision: Season 1 Expansion (~10–15 Episodes), Pillar Threshold (Min 3 Longs/Pillar), and CEO-Triggered Season Boundary Review
## Context:
Previous drafts suggested Season 1 concluded with EP05 and scheduled an immediate Season Boundary Review post-EP05 release. Sahand (CEO) clarified the season lifecycle: Season 1 remains OPEN and expands to ~10–15 episodes, establishing substantial channel depth across all four permanent pillars before any Season 2 is initiated.
## Options Considered:
1. Conclude Season 1 at EP05 and force a Season 2 transition now (Rejected: only 5 episodes produced, uneven pillar representation with only 1 video in AI & ML, AI+Finance, and Finance Simplified).
2. Open-ended production without season boundaries or narrative groupings (Rejected: loses the intellectual depth and binge-watch continuity of seasonal themes).
3. **Expand Season 1 to ~10–15 Episodes with Strict 3-Longs-Per-Pillar Minimum (Chosen)**:
   - Season 1 remains active and open, targeting ~10–15 episodes total.
   - The initial arc *Money → Markets → Algorithms → AI → Speed* (EP01–EP05) represents the foundational first five chapters of Season 1 (historical context), not a completed season.
   - Minimum threshold: At least 3 long-form episodes per permanent pillar must be published/produced before Season 2 can begin.
   - Season 2 starts ONLY when Sahand (CEO) explicitly decides to initiate it.
   - The Season Boundary Review remains a formal governance gate, but is triggered exclusively when Sahand decides to close Season 1 and start Season 2.
   - Topic QT-009 (*How HFT Algorithms Price Spreads in Microseconds*) is marked "Committed (EP05 outro tease)" rather than "Scheduled".
## Reasoning:
With only 5 episodes, three of the four pillars have only a single representative video. Expanding Season 1 ensures a robust, balanced library across all 4 pillars (minimum 3 per pillar = 12 minimum long-forms), while honoring the outro commitment made in EP05 without prematurely closing the season.
## Final Choice: Option 3 (Season 1 stays OPEN to ~10–15 episodes, minimum 3 longs per pillar, Season Boundary Review triggered by Sahand).
## Impact:
Updated `QUANTROVE_TOPIC_STRATEGY.md`, `Quantrove_Topic_Database.xlsx`, `build_topic_database.py`, `IDEAS_AND_BRAINSTORMS.md`, and `CLAUDE.md` §2.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-09-30
## Decision: Adoption of `html_motion` Scene Engine, Formal Remotion Approval, Palette Lock, Path A Manual MP4 Export, and Dropping After Effects / Cavalry
## Context:
To expand Quantrove's visual storytelling capabilities beyond purely mathematical vector plots (Manim) and AI B-roll (Flow), Sahand (CEO) evaluated approaches for generating high-density terminal, order-book, and financial UI visual metaphors. Motion design tools and headless web renderers were reviewed for workflow efficiency and maintenance burden.
## Options Considered:
1. Traditional Motion Design Suites (After Effects, Cavalry): Dropped due to manual GUI overhead, proprietary project formats, and lack of agentic prompt-driven codeability.
2. Automated Headless Web Rendering (Puppeteer / Playwright headless screen capture): Dropped due to brittle browser environment dependencies, frame-drop risks, and unnecessary infrastructure complexity.
3. **4-Engine Visual Stack with `html_motion` via Path A (Chosen)**:
   - **4 Approved Engines**: `Manim` (math/ML mechanics), `Remotion` (parameterized data graphics, real data), `Google Flow` (cinematic atmosphere), and `html_motion` (4–8s terminal/UI visual metaphors).
   - **Path A Only**: Coding models generate self-contained HTML/JS from prompts; Sahand manually exports to MP4 (1080p/60fps) and drops assets into `TIMELINE_MEDIA/html_motion/`. Zero headless rendering built.
   - **Placement**: Data Reveal beat of the Chapter Quad. Exact-slot (2–8s), deterministic `render(t)`, play once and hold final frame (`>=0.5s`), no loops. Shorts: maximum 1 `html_motion` clip.
   - **Palette Lock**: Strictly `#202322` (bg), `#233D4C` (chrome/grid), `#C3D809` (primary accent), `#FD802E` (risk/anomaly), `#E6EDF3` (text). Opacity variations allowed; no other hues, gradients, glows, or shadows.
   - **Keyword Isolation**: Kinetic pop-up overlay (V2) remains the exclusive narration keyword layer. `html_motion` never renders spoken keywords.
## Reasoning:
`html_motion` allows rapid generation of precise financial UI and terminal metaphors that are painful to build in Manim and impossible in Flow. Path A eliminates headless rendering maintenance debt while maintaining CEO quality control.
## Final Choice: Option 3 (`html_motion` engine added, Remotion approved, palette locked, Path A manual export only, AE/Cavalry dropped).
## Impact:
Created `01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md`, `01_PROJECTS/YOUTUBE/pipeline/qa/html_motion_qa.py`, updated `CLAUDE.md`, `.claude/rules/scene-classification.md`, `.claude/agents/content.md`, `longs-scriptwriting`, `shorts-qa`, `HOW_TO_RUN_THIS_COMPANY.md`, and `VIDEO_PROMPTING_GUIDE.md`.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-09-30 | Decision: YouTube Metadata Standard Enacted (6–7 word titles <60 chars, <=300 char tags, 3 hashtags, disclaimer); Standing rule: Sahand brings ElevenLabs voiceover himself.

---

## Date: 2026-10-01
## Decision: EP05 Confirmed Live, EP06 Gate 1 Approved (16 Manim Renders Authorized, VO Locked), and EP07 Pillar Selected (AI & ML in the Real World)
## Context:
Sahand (CEO) reviewed the channel state and production status on 2026-10-01, confirming operational status and authorizing the next phase of production.
## Choices Enacted:
1. **EP05 Confirmed Live**: *Why Free Trading Isn't Free* (ID: `-SH2kNLF3WA`) confirmed public/live on YouTube. All workspace records updated to [PUBLISHED 2026-09-30]. The previous publication blocker for EP06 Scene 24 CTA is cleared.
2. **EP06 Gate 1 Approved**: Humanized script, 4-engine classification, locked 420.91s ElevenLabs VO, and scene-by-scene timing approved. Full batch rendering of all 16 Manim scenes authorized and executed at 1080p60. VO speed modification is ruled NOT REQUIRED.
3. **EP07 Pillar Selected**: Pillar 1 (🤖 AI & ML in the Real World) selected for EP07 to deepen library depth in pure AI/ML, aligning with Sahand's master's degree background and personal interest while building toward Season 1's minimum 3-video-per-pillar threshold.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-10-01
## Decision: EP06 Gate 2 Approved 100% (Transition to CapCut Assembly) & Next AI/ML Concept Selected ("How AI Turns Words into Geometry")
## Context:
Sahand (CEO) completed visual QA review of the EP06 rendered asset package following targeted Manim fixes on scenes S02, S08, S13, S15, S18, and S22. All 25 scenes, the 60fps QuickTime RLE kinetic overlay, and the 420.91s ElevenLabs master audio are verified on disk with zero remaining defects.
## Choices Enacted:
1. **EP06 Gate 2 Approved 100%**: Flow footage, voiceover pacing, visual rhythm, and Manim vector animations approved. EP06 transitions from production into final CapCut assembly.
2. **Next AI/ML Episode Concept Selected**: "How AI Turns Words into Geometry" (Vector Embeddings) chosen as the next educational concept under Pillar 1 (AI & ML in the Real World), serving as Chapter 1 of a structured first-principles AI series (*Representation -> Interface -> Optimization -> Generalization -> Architecture*). Future episode numbers remain fluid.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.

---

## Date: 2026-10-02
## Decision: Shorts Archive Consolidation to Canonical `shorts/_ARCHIVE/`, Channel State Reconciliation, and EP06 Shorts Approved
## Context:
Following autonomous Remotion production of the four approved EP06 Shorts, Sahand (CEO) completed review and approved all four videos. Workspace organization was audited to eliminate duplicate archive directories, reconcile local folder statuses against live YouTube Studio state via read-only MCP, and establish single-archive hygiene.
## Choices Enacted:
1. **Canonical Archive Consolidation**: Merged legacy `shorts/archived` (13 published releases) into `shorts/_ARCHIVE/published/`. Obsolete empty `shorts/archived` folder removed after verified zero data loss. Canonical archive now cleanly partitions into `published/`, `rejected/`, `superseded/`, and `old_renders/`.
2. **Read-Only Channel Reconciliation**: Polled YouTube Studio via MCP to verify actual live states:
   - EP05 Shorts #1 (`Cb_WXdFSk1s`) and #3 (`atM9NzpwPKQ`) are confirmed Public/Live; folders updated to `[PUBLISHED]`.
   - EP05 Shorts #2 (`SSFzhfnUAuw`), #4 (`WfTsYZXEkRk`), and #5 (`LVLjievqILs`) confirmed uploaded as Scheduled/Private in Studio.
   - EP05 Long-form (`-SH2kNLF3WA`) confirmed Public/Live.
3. **EP06 Shorts Ready for Manual Upload**: The 4 approved EP06 Shorts (`06` through `09`) remain 100% QA-passed and staged locally for Sahand to manually upload and schedule per the strict read-only upload boundary.
## Status: Approved by CEO (Sahand) and Enacted as Standing Company Policy.
---

## Date: 2026-10-02
## Decision: EP07/EP08 Topics, 10-15 Min Long-Form, Visual Density v1, Motion Tooling & Workspace Reorganization
## Context:
After EP06, Sahand judged the visuals better but still lacking motion (EP06 averaged one visual per 17.6 s). Sahand asked for longer, more sophisticated episodes, free motion tools, and a fully reorganized, token-efficient workspace.
## Choices Enacted:
1. **Topics**: EP07 = "How AI Turns Every Word Into Geometry" (embeddings, packaged as "how LLMs work"); EP08 = "The 2017 Paper That Rebuilt Modern AI" (attention/transformers). Both Pillar 1. EP09 candidate = hallucinations. Evidence: `topic_strategy/EP07_EP08_TOPIC_RESEARCH.md`.
2. **Runtime**: Long-form target changes from 8-12 min to **10-15 min**, starting with EP07.
3. **Visual Density Standard v1** (`.claude/rules/visual-density.md`): new shot ≤6 s, 3-6 s beats, camera move per Manim beat, Remotion for all data graphics, no time-stretched Flow clips.
4. **Motion tooling (all free)**: Installed the Remotion official skills (best-practices, render) and HyperFrames (Apache 2.0; skills + CLI 0.8.113, telemetry off). html_motion now renders locally via HyperFrames; manual Vivaldi export is the fallback. Removed the After Effects MCP (no Adobe) and the Playwright MCP (broken; the built-in browser covers it). HeyGen cloud rendering is not allowed (paid).
5. **Workspace reorg**: 55 moves, zero deletions (manifest + undo in `logs/reorg_2026-10-02_*`). Uniform longs naming, `03_ARCHIVE` → `99_ARCHIVE`, single root `logs/` + `reports/`, episode one-off scripts → `pipeline/_legacy/`, stale `E:\AI_COMPANY` paths fixed in the live pipeline tools.
6. **EP06**: folder `[SCHEDULED 2026-10-04]`; Sahand uploads its 4 Shorts manually after EP06 goes public.
## Status: Approved by CEO (Sahand) and Enacted.

---

## Date: 2026-10-03
## Decision: EP07 + EP08 Gate 1 Approved
## Context:
Sahand approved the titles "How AI Turns Every Word Into Geometry" (EP07) and "The 2017 Paper That Rebuilt Modern AI" (EP08), delivered both ElevenLabs voiceovers (EP07 667.64 s, EP08 641.80 s), and instructed production to proceed.
## Choices Enacted:
1. Scripts and beat-level shot lists locked as approved at Gate 1. Thumbnails default to concept A for both (swappable before upload).
2. Asset production started against word-aligned master timelines (`ASSEMBLY/EPxx_MASTER_TIMELINE.json`, 96.9% / 97.7% word match).
3. GitHub remote set to `github.com/sahandomranpour144/Quantrove` (text-only repo). The first push is pending Sahand's browser sign-in.
## Status: Approved by CEO (Sahand). Gate 2 review follows the asset build.

---

## Date: 2026-10-03
## Decision: EP07 Gate 2 Approved; Sequential Production; EP08 in a New Session
## Context:
Sahand watched every EP07 timeline clip ("perfect") and approved Gate 2. CPU load from parallel builders was too high.
## Choices Enacted:
1. EP07 Gate 2 approved. Sahand assembles EP07 in CapCut after EP08 is finished; EP07 publishes before EP08.
2. Production runs one task at a time (one render, one builder) on this CPU-only machine.
3. EP08 production continues in a fresh Claude Code session from `EP08_SESSION_BRIEF.md` to keep context small.
## Status: Approved by CEO (Sahand) and Enacted.

---

## Date: 2026-10-03
## Decision: EP08 Gate 2 Approved; Title Optimized for Search
## Context:
All 46 EP08 scenes rendered sequentially (24 Manim, 17 Remotion, 3 Flow, 2 HyperFrames + overlay). gate2_package: 46/46 present, 0 to check, overlay OK. Frame review fixed edge clipping (focus clamp), the √ fill bug, label overlaps (M11, M18, M18B, R1, R7, R8, R10, R11B) and safe-area overruns (R4B, R8B). Sahand approved the contact sheet and asked for best-in-class SEO and packaging to reach monetization fast.
## Choices Enacted:
1. EP08 Gate 2 approved. Sahand assembles EP07 then EP08 in CapCut; EP07 publishes first.
2. Publish title changed from the Gate 1 "The 2017 Paper That Rebuilt Modern AI" (vidIQ 77) to **"The 2017 Paper That Built ChatGPT"** (85). It keeps rule L2 ("2017" and "paper" spoken in the first 3 s). "Attention Is All You Need, Explained" (88; 35.3k searches/mo, competition 34.7) is the title A/B variant.
3. Two thumbnails (A "2017" attention fan = primary, B "GPT" glowing T) go into YouTube Test & Compare.
## Status: Approved by CEO (Sahand) and Enacted (title change made under the CEO's SEO mandate; revert to the Gate 1 title on request).
