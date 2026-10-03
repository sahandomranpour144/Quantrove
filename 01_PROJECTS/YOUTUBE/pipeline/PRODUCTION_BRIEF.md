# Long-Form Asset Production Brief (EP07+)

Read this whole file before building any asset. It is the contract between the director (main session) and asset builders.

## Inputs (per episode)
| What | Path |
|---|---|
| Script + beat list (`‖` in [NARRATION] = beat; `[VISUAL] b1 · b2 …` = what each beat shows) | `longs/<EP folder>/EPxx_SCRIPT_AND_SHOTLIST.md` §4 (scenes), §5 (asset specs) |
| Exact beat timings (from real VO words) | `longs/<EP folder>/ASSEMBLY/EPxx_MASTER_TIMELINE.json` → `scenes[].beats[].start/end` |
| Rules | `.claude/rules/visual-density.md`, `visual-style-standard.md`, `cleantext-manim.md` |

EP folders: `longs/[IN_PROGRESS 2026-10-02]_long07_ai_words_geometry`, `longs/[IN_PROGRESS 2026-10-02]_long08_attention_transformer`.

**Timeline notes:** a scene may contain MORE beats than its script lists (`moved_in_beats` > 0: leading beats moved in from an over-long Flow scene before it; build a visual for them from that beat's text). Number of beats to play = `len(scene.beats)` in the timeline, never the script count. Beats > 6 s need a visible sub-change mid-beat.

## Non-negotiables
- Palette ONLY `#202322` bg · `#233D4C` lines/chrome (never text) · `#C3D809` lime (signal/positive) · `#FD802E` pumpkin (risk) · `#E6EDF3` text. Font Nohemi (Inter fallback). No other colors, no gradients to other hues, no red/green.
- Nothing static > 3 s. Something visibly changes every 2-4 s; every beat starts with a visible change.
- On-screen text ≤ 6 words per text event; never narrate keywords on screen as captions (the V2 kinetic overlay owns spoken keywords). Labels, numbers, tags are fine.
- Every number shown must match the script/sources exactly. Illustrative values carry an `ILLUSTRATIVE` tag (Manim: `self.hud(...)`).
- Safe area: content inside x 96..1824, y 190..856 px (1920x1080). Top band y 56..176 and caption lane y 864..1080 stay clear.
- Output length must equal the timeline scene duration (±1 frame at 60 fps).
- 1920x1080, 60 fps, H.264 MP4 (yuv420p), no audio track.
- Output file: `longs/<EP folder>/TIMELINE_MEDIA/EPxx_SCnn_<ASSET>.mp4` (nn = timeline scene number, 2 digits). Move (not copy) renders there.

## Manim (`pipeline/qvis.py`)
- Code in `pipeline/scenes/epXX/<chapter>.py` (bracket-free path; Manim crashes on `[` `]` in paths). Pattern: `pipeline/scenes/ep07/ep07_intro.py` (reference implementation, already final).
- `class <ASSET>(QScene): ASSET = "<ASSET>"`; `self.setup_q()`; one `self.beat(...)` call per timeline beat; end with `self.finish()`.
- NEVER call `self.play`/`self.wait` directly (breaks timing). Everything happens inside `self.beat(*anims, run=..., focus=...)`; persistent motion via updaters.
- Text via `txt()` / `CleanText` only. Glyphs Nohemi lacks (→ ≈ √ ‖ Greek) fall back automatically.
- Use `glow_dot`, `label_dot`, `counter` (ValueTracker count-ups), `self.hud` for pinned tags.
- Render: `QTIMELINE="<abs path to EPxx_MASTER_TIMELINE.json>" manim -q h --disable_caching --media_dir ../_media <file>.py <ASSET>` from `pipeline/scenes/epXX/`.
- Preview without timeline (4 s/beat) for fast iteration: omit QTIMELINE, add `-q l`.

## Remotion (`pipeline/remotion_engine`)
- New compositions in `src/longs/ep07/` and `src/longs/ep08/`, registered in `src/Root.tsx` as `EP07-<ASSET>` etc. 1920x1080, fps 60, `durationInFrames = round(scene.end*60) - round(scene.start*60)`.
- Beats: one `<Sequence from={beatStartFrame - sceneStartFrame}>` per timeline beat (load timeline JSON copied to `src/data/ep07_timeline.json`).
- Colors and fonts from `src/brandTokens.ts`; Nohemi from `public/fonts/`. Motion via `spring({fps, frame, config:{damping:200}})` and `interpolate`; numbers count up.
- Ambient layer on every composition: slow-drifting `#233D4C` grid at ~30% opacity (reuse one shared `<AmbientGrid/>` component).
- Render: `npx remotion render src/index.ts EP07-<ASSET> <out.mp4> --codec h264` from `remotion_engine/`.

## HyperFrames html_motion
- One composition per HM asset under `pipeline/hyperframes/epXX/<ASSET>/`. Terminal/UI aesthetic, palette lock, deterministic GSAP timeline, plays once, holds the final frame ≥ 0.5 s, duration = timeline scene duration. Render locally only (never cloud). Read the `hyperframes` skill first.

## Self-QA before handing back (mandatory per asset)
1. `ffprobe` duration == timeline duration (±1 frame).
2. Tile 4 frames (`ffmpeg -vf "select=...,scale=800:-1,tile=2x2"`) and LOOK at them: palette, legibility, no overlap/clipping, safe area, nothing broken.
3. Log one line per asset to `logs/<task>_2026-10-03.txt`: asset, duration, frames OK, notes.
Return a ≤ 25-line summary: assets done, any skipped/failed with reason, any number you could not verify.
