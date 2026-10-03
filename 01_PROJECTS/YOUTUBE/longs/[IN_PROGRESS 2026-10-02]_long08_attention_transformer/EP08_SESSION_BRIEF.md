# EP08 Session Brief: finish production → Gate 2 → docs
*The 2017 Paper That Rebuilt Modern AI* · Gate 1 approved 2026-10-03 · VO 641.80 s · master 661.80 s (11:02)
Written 2026-10-03 at the end of the EP07 session. **EP07 is fully done** (Gate 2 approved; only CapCut assembly by Sahand remains). Use EP07 as the reference for everything below.

## Hard working rules (CEO, 2026-10-03)
- **One task at a time.** One render at a time, foreground, wait for it to finish. Never parallel renders, never several builder subagents at once. Remotion uses `--concurrency=2`. (Memory: sequential-renders-light-cpu.)
- Token-lean: read files by section, don't re-read, and keep outputs short. If you use a builder subagent, use one, on Sonnet.
- Before rendering, check for orphaned `manim` / `node` / puppeteer `chrome` processes and kill any left over from earlier sessions.

## Read first (in this order, nothing else unless needed)
1. `01_PROJECTS/YOUTUBE/pipeline/PRODUCTION_BRIEF.md`: the asset contract (palette, timing, QA, naming).
2. This file.
3. Per scene only: `EP08_SCRIPT_AND_SHOTLIST.md` §4 block (`grep -n "Scene N —"`) and §5 specs.

## Status of EP08 assets (`TIMELINE_MEDIA/`)
| Engine | Done | Left |
|---|---|---|
| Flow (3) | ✅ all, conformed | none |
| HyperFrames (2) | ✅ SC07, SC37 | none |
| Kinetic overlay | ✅ `00_OVERLAY_EP08_kinetic_word_pops_60fps.mov` | none |
| Manim (24) | ❌ none rendered | **All 24 classes are already written**, unreviewed: `pipeline/scenes/ep08/ep08_{intro,ch1..ch5,close}.py`, shared `ep08_common.py`. Ignore and delete `list1-4.txt`, `run_one.sh`, `media/` (leftovers from a parallel-render attempt). |
| Remotion (17) | SC42 R13_RECAP, SC43 R12_AUTHORS_GRID | **15 not rendered; all are coded** in `pipeline/remotion_engine/src/longs/ep08/scenes.tsx` (registered as `EP08-<ASSET>`). **Re-render R13_RECAP** too: the shared `RecapStack` changed during EP07 Gate 2 (cards now land directly in their row). R11B and R11 failed or were killed under load; just re-render. |

## Steps
1. **Manim**: for each class, preview at `-q l` (no QTIMELINE) to catch errors. Then final render: `QTIMELINE=<abs path>/ASSEMBLY/EP08_MASTER_TIMELINE.json manim -q h --disable_caching --media_dir ../_media <file> <ASSET>` from `pipeline/scenes/ep08/`. Move the output to `TIMELINE_MEDIA/EP08_SCnn_<ASSET>.mp4` (nn = timeline scene number). After each scene: confirm the frame count matches the timeline (±1), then tile 4 frames and **look** at them. Fix overlaps, off-palette colors, static frames and clipped text.
2. **Remotion**: render each with `npx remotion render src/index.ts EP08-<ASSET> <out> --codec h264 --muted --concurrency=2 --timeout=300000`. Template loop: `pipeline/remotion_engine/render_ep07.sh`. **Then convert pixel format.** Remotion outputs `yuvj420p`. Re-encode every Remotion clip with `-vf "scale=in_range=full:out_range=limited,format=yuv420p" -color_range tv -c:v libx264 -crf 16 -an` (as done for EP07).
3. **Gate 2**: `python pipeline/qa/gate2_package.py "<EP08 folder>" EP08`. It must report 46/46 present, 0 to check and overlay OK. Then review `ASSEMBLY/GATE2_CONTACT_SHEET.png` scene by scene, and pull 4-frame strips for anything suspicious. Known failure classes from EP07:
   - Manim `set_opacity()` on arcs or lines also fills them; use `set_stroke(opacity=…)`.
   - Labels collide when an orbiting map rotates too far; keep the orbit slow.
   - Stacked cards can hide earlier text.
   - A frame caught mid-count-up looks like a wrong number; check the final frame.
4. Send Sahand the contact sheet for **Gate 2 approval**.
5. **After approval**, produce the docs, mirroring EP07:
   - `METADATA/EP08_METADATA.md`: model it on `../[IN_PROGRESS 2026-10-02]_long07_ai_words_geometry/METADATA/EP07_METADATA.md`. Chapters come from the timeline chapter-start scenes S3, S12, S21, S28, S34, S39, plus the end screen. Hook ≤150 chars leading with "transformer architecture explained" or "how LLMs work". Include the music credit block, the 14-item VERIFY table from script §7 resolved, and a pinned comment. The CTA points to EP07: confirm the title spoken in `VOICEOVER/EP08_words.json`.
   - `METADATA/EP08_THUMBNAIL.png`: concept A from script §1 (big lime "2017", attention lines fanning from one word). Base it on `pipeline/thumbnail_ep07.py`.
   - `ASSEMBLY/EP08_ASSEMBLY_GUIDE.md`: copy EP07's guide structure with EP08 times and chapter dissolves.
6. Update `STATE.md`, `CHANGELOG.md`, `02_KNOWLEDGE/00_CORE/decisions/DECISION_LOG.md` (Gate 2). Commit, then push (`git push`; the GitHub remote is authenticated).
