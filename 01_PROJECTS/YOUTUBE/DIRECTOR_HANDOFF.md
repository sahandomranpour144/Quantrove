# Director Handoff — Quantrove (Chat → Claude Code)
Date: 2026-10-02 | Authority order if sources conflict: `DECISION_LOG.md` > this file > older docs.
Purpose: Claude Code now acts as **director + executor**. The old chat-relay workflow (Sahand copying output between a separate Claude chat and the agent) is retired.

## 1. Working with Sahand
- CEO, final decision-maker at every gate. Master's in AI, so do not over-explain ML.
- Wants: direct, precise, factual, well-structured answers. Exact step-by-step instructions, not overviews. Short but full of useful tips. Friend + mentor tone. Challenge weak ideas.
- Every response ends with **"Your task / My task"** (or open questions).
- Token-lean: he is on a Pro plan and has hit usage limits. Short sessions, no wasted reads, no unnecessary subagents.
- He brings these himself, so never build tools for them: ElevenLabs voiceover, Google Flow clips, html_motion MP4 export (Vivaldi extension), CapCut assembly.
- Side assistants: **GPT** (senior observer/reviewer, own Project), Grok (minor). They advise; they do not decide.

## 2. Channel identity
- **Quantrove**: AI/ML + finance/trading + data storytelling. Aesthetic "Institutional Data Intelligence" (Bloomberg-terminal precision, no stock imagery, no fluff). Must never feel like generic AI content.
- **Permanent pillars (playlists):** AI & ML in the Real World | AI + Finance + Trading | Finance & Trading, Simplified | Data Stories. He prefers these full playlist names.
- **Season 1** (Hidden Mechanics of Modern Markets) is open, about 10-15 episodes. Minimum 3 longs per pillar before Season 2. Season 2 starts only when Sahand says so (formal Season Boundary Review).
- **Cadence:** 2 longs + 5-6 Shorts per week, one pillar per week. Long-form target 10-15 min from EP07 (CEO 2026-10-02).
- **Outro rule (from EP06):** never tease the next episode's topic. Generic CTA and playlist pointer only.
- **Topic scoring:** 100-point formula in `topic_strategy/QUANTROVE_TOPIC_STRATEGY.md` (Curiosity 25, Narrative 20, Data 15, Visual 15, Educational 15, Evergreen 10). Scores guide; Sahand greenlights.

## 3. Standing rules (full text lives in the files named)
- **Palette lock:** `#202322` bg, `#233D4C` lines/chrome only (never text), `#C3D809` positive/accent, `#FD802E` risk/loss, `#E6EDF3` text. No generic red/green. Font Nohemi (Inter fallback). Source: `brand/brand_tokens.json`.
- **Manim:** CleanText engine (ref_size 72, scaled). Nohemi lacks arrows/Greek/≈/µ, so CleanText falls back to Segoe UI for them. Glyph validation is a mandatory pre-render gate.
- **4 engines, one per scene:** Manim (math/ML mechanics, accurate numbers), Remotion (data graphics; 16:9 compositions not built yet), Flow (cinematic atmosphere only), html_motion (4-8 s terminal/UI metaphors, Path A manual export, deterministic `render(t)`, hold final frame ≥0.5 s). Standard: `pipeline/motion/HTML_MOTION_STANDARD.md`.
- **Kinetic overlay:** 60fps RGBA MOV on Track V2, the only keyword layer, in every video.
- **Layout Contract v1:** 16:9 stage x=96..1824, y=190..856; caption lane y=864..1080; pop-up band y=56..176. 9:16 stage x=60..880, y=250..1000; caption band y=1040..1440.
- **Script rules:** packaging first (3 titles, 6-7 words, <60 chars, plus thumbnail concept before any script); hook in 5 s stating why they clicked; pace statement 5-20 s; Chapter Quad (Human Question → Mystery → Data Reveal → Consequence); 4-5 open loops, first payoff by 90 s; CTA tells exactly what to do; 4-pass humanizer (`quantrove-script-humanizer`) before Gate 1.
- **Sourcing:** every figure sourced, or labeled ILLUSTRATIVE on screen. Every script ends with a VERIFY BEFORE PUBLISH list.
- **Gates:** Gate 1 = humanized script + engine classification. Gate 2 = rendered asset verification. Never pass either without Sahand.
- **Durations:** always anchor to the real VO length and word timestamps. Never hardcode.
- **Shorts:** value or question in 3 s; 3-4 word chunks are the captions (single text system); no static frame over 3-4 s; calm, premium tone; per-episode set = 2 native + 1-2 extracted from the long, plus standalone topics chosen together. Shorts go to `shorts/_ARCHIVE/published/` once published.
- **Metadata:** 6-7 word titles, 3 hashtags, tags ≤300 chars, default description + per-video additions, disclaimer line. Framework in `pipeline/metadata/`.
- **Post-publish cleanup:** keep final video, metadata, final script; delete the rest. First run is dry-run only, with explicit Sahand confirmation before deletion (EP03 dry-run is still awaiting it).
- **Analytics are manual-only.** Never auto-run, schedule, or re-enable (Rule 10.5).
- **Folder tags:** `[IN_PROGRESS date]`, `[SCHEDULED date]`, `[PUBLISHED date]`; update `STATE.md` and `CHANGELOG.md` on every change.

## 4. Status
| Item | Status |
|---|---|
| EP01-EP05 | Published |
| EP06 "The Machines Trading Before You Blink" (QT-009, Pillar 2) | Uploaded, UNLISTED until Sun 2026-10-04. **Do not touch.** Sahand uploads its 4 Shorts manually after it goes public. |
| EP07 "How AI Turns Every Word Into Geometry" (embeddings, Pillar 1) | Approved 2026-10-02; 10-15 min; package as "how LLMs work" |
| EP08 "The 2017 Paper That Rebuilt Modern AI" (attention, Pillar 1) | Approved 2026-10-02; 10-15 min |
| Series map (proposal) | Representation → Attention → Optimization → Generalization → Full architecture (numbers fluid) |
| Pillar counts after EP07/08 | P1=3, P2=2, P3=1, P4=2 |

## 5. EP06 quality bar (replicate on EP07/EP08)
- 25 scenes, one engine each; Manim re-timed to the VO within 0.01 s.
- Over 90% hard cuts; only 4 dissolves (0.25-0.40 s) at chapter bridges; end-screen dip to black.
- No grading on Manim or html_motion; Flow matched to the brand canvas only. No flashy effects, no handheld shake.
- Audio: VO about -14 LUFS, bed ducked at least 16 dB, SFX -18 to -22 dBFS, bed swell on the end screen.
- Assets named `EPxx_SCyy_*.mp4` in `TIMELINE_MEDIA/`, with `MASTER_TIMELINE.json`, `CAPCUT_IMPORT_ORDER.md`, `CAPCUT_ASSEMBLY_CHECKLIST.md`, `ASSET_INVENTORY.md`, and a post-assembly finishing guide with a pre-export checklist.

## 6. Open items
1. EP09 candidate: "Why AI Confidently Makes Things Up" (hallucinations, score 88). See `topic_strategy/EP07_EP08_TOPIC_RESEARCH.md`.
2. EP06 metadata: durations shown as 418/438 s vs final 420.91/440.91 s; Avellaneda-Stoikov framing line for the Studio description; verify Knight Capital figure and half-cent tick status on publish day.
3. EP07 and EP08: packaging → scripts → Gate 1, built in parallel, with manual steps batched for both.
4. Remotion 16:9 compositions (steps 1-5) still not built; do not start unless asked.
5. EP03 post-publish cleanup awaiting confirmation.
6. Docs drift: `QUANTROVE_TOPIC_STRATEGY.md` still to sync (STATE.md synced 2026-10-02).

## 7. Operating mode in Claude Code
- Main session = director + executor. Read `STATE.md`, `CHANGELOG.md`, this file at session start; nothing else unless needed.
- Heavy or parallel work (Manim batches, QA sweeps) may use subagents; otherwise stay in one session to save tokens.
- Update `DECISION_LOG.md` when Sahand decides something; update `STATE.md` and `CHANGELOG.md` after each milestone.
- Keep `CLAUDE.md` lean (about 90 lines). Put detail in skills and rules loaded on demand.
