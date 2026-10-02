# CLAUDE.md — Quantrove AI Workspace

> Loads every session. Orientation only. Detail lives in `.claude/rules/`, `.claude/skills/`, and the handoff.

## 0. Session Start (read these, nothing else unless needed)

1. `01_PROJECTS/YOUTUBE/STATE.md` — episode status and next actions
2. `01_PROJECTS/YOUTUBE/DIRECTOR_HANDOFF.md` — **primary brief**: how to work with Sahand, channel identity, standing rules, EP06 quality bar, open items, operating mode
3. `CHANGELOG.md` — recent changes

Token discipline: follow `.claude/rules/token-discipline.md`.
Authority if sources conflict: `02_KNOWLEDGE/00_CORE/decisions/DECISION_LOG.md` > `DIRECTOR_HANDOFF.md` > this file > older docs.

---

## 1. Workspace

**Owner / CEO**: Sahand — one-person AI-powered enterprise. Claude Code is **director + executor** (chat-relay workflow retired).
**Channel**: [Quantrove](https://youtube.com/@Quantrove) — faceless, data-driven documentary YouTube. Identity, pillars, cadence, season rules: handoff §2.
**Brand**: single source of truth `brand/brand_tokens.json` + `brand/brand-style.md`. Palette lock summary: handoff §3. The old dark luxury palette (`#0B0F19`, `#00F0FF`, …) is historical.

**Workstreams**: YouTube production (`01_PROJECTS/YOUTUBE/`) · Trading AI (`03_TRADING_AI/`, in development) · ML learning (`02_KNOWLEDGE/`).

---

## 2. Hard Rules (non-negotiable; full playbooks in `.claude/rules/`)

- **Duration anchoring** — ffprobe-measured media length, never hardcoded (`duration-anchoring.md`)
- **Word-level transcription** — faster-whisper word timestamps for captions/cuts/pops (`word-level-transcription.md`)
- **Scoped tasks** — declare `IN SCOPE` / `LOCKED` before touching files (`scoped-task-locking.md`)
- **Rename = delete old** — remove the source on every rename/move (`rename-delete-old.md`)
- **Manim CleanText** — native `Text()`, `ref_size=72` scaled; glyph validation pre-render (`cleantext-manim.md`)
- **Flow is manual-only** — Sahand generates in `labs.google/flow`; zero API billing (`gemini-flow-manual-only.md`)
- **4 engines, one per scene** — Manim / Remotion / Flow / html_motion (`scene-classification.md`, `pipeline/motion/HTML_MOTION_STANDARD.md`)
- **Visual density (EP07+)** — new shot ≤6 s, beats of 3-6 s, camera move per Manim beat (`visual-density.md`)
- **Asset centralization** — one `TIMELINE_MEDIA/` per episode, chronological prefixes (`asset-centralization.md`)
- **Kinetic pop-ups** — long-form 60fps RGBA on V2; Shorts burned-in 3-4 word chunks (`kinetic-popups.md`, `shorts-style.md`)
- **Script humanization** — 4-pass workflow before Gate 1 (`script-humanization.md`, skill `quantrove-script-humanizer`)
- **Metadata** — 6-7 word titles, <60 chars; standard in `pipeline/metadata/METADATA_STANDARD.md`
- **Never automate** voiceover, Flow clips, html_motion MP4 export, or CapCut assembly — Sahand does these
- **Folder tags** `[IN_PROGRESS|SCHEDULED|PUBLISHED YYYY-MM-DD]` mandatory; update `STATE.md` + `CHANGELOG.md` on every change

### Analytics are manual-only

Never auto-run channel analytics, status sync, or post-publish cleanup — no cron, scheduled task, `SessionStart` hook, or unattended agent calling `youtube_studio_mcp`. Run only on an explicit in-session request ("check my channel stats"). Re-enabling a routine is a CEO decision logged in `DECISION_LOG.md` first. Disabled prior routine: `.claude/_disabled_tasks/youtube-studio-status-sync.SKILL.md.bak`.

---

## 3. CEO Review Gates (mandatory)

| Gate | When | Sahand reviews |
|---|---|---|
| **Gate 1** | Before any code or assets | Humanized script + scene shot list with 4-engine classification |
| **Gate 2** | Before CapCut assembly | Full rendered asset set (Manim, VO, Flow list, kinetic overlay) |

Never pass either gate on assumption.

---

## 4. Workspace Map

```
ClaudeCode/
├── CLAUDE.md · HOW_TO_RUN_THIS_COMPANY.md (full SOPs) · mine.md (prompt cheat-sheet)
├── 01_PROJECTS/YOUTUBE/
│   ├── STATE.md · CHANGELOG.md · DIRECTOR_HANDOFF.md   ← only 3 root files
│   ├── longs/     [STATUS YYYY-MM-DD]_longNN_slug/ + _long_template/
│   ├── shorts/    active only; published → _ARCHIVE/published/
│   ├── pipeline/  reusable tools · config/ metadata/ motion/ qa/ text_layer/ remotion_engine/ · _legacy/ (episode one-offs)
│   ├── topic_strategy/  scoring, database, research, my_ideas/
│   ├── publishing_plan/ · analytics/ (manual-only) · instructions_and_workflows/ (SOPs, templates)
│   └── media/     shared generated stills
├── brand/ (tokens, style) · assets/ (fonts, safe zones, audio/)
├── 02_KNOWLEDGE/  00_CORE/ (decisions, rules, knowledge) · 02_SHARED/ · ML/
├── 03_TRADING_AI/
├── logs/ · reports/   ← all task logs and reports (workspace-wide)
├── 99_ARCHIVE/        ← superseded docs, experiments, scratch (never read unless asked)
└── .claude/  agents/ skills/ rules/ hooks/
```

**Motion skills (on demand)**: `remotion-best-practices`, `remotion-render`, `hyperframes`, `hyperframes-cli`, `hyperframes-animation`, `motion-graphics`, `faceless-explainer`, `manim`, `kinetic-typography`. Render locally only; never HeyGen cloud (paid). Quantrove rules override skill defaults (palette, VO by Sahand, gates).

**Before a task**: check `.claude/agents/` for a named agent and `.claude/skills/` for a matching skill.
**Before strategy proposals**: read `DECISION_LOG.md`. **Before a new episode kickoff**: `HOW_TO_RUN_THIS_COMPANY.md`, `VIDEO_PROMPTING_GUIDE.md`, `00_CORE/rules/AGENT_RULES.md`.

**MEMORY.md**: lightweight index over `DECISION_LOG.md`, `COMPANY_KNOWLEDGE.md`, and `analytics/` via `[[wikilinks]]`, no duplicated content. Add a node only when something is logged canonically; prune wrong nodes.

---

## 5. Operating Principles

- **Files are permanent, chat is not.** Specs, decisions, outputs go to files.
- **Evidence before assumptions.** Validate data before recommending strategy.
- **Quality over speed.** One world-class output beats ten mediocre ones.
- **CEO signs off** on strategy, money, and public releases.
- **Challenge weak ideas.** Surface the risk; don't silently agree.
- **Exact, step-by-step instructions**, end every response with *Your task / My task* (handoff §1).
- **Keep this file ~90 lines.** New detail goes in rules, skills, or the handoff.
