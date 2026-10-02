# 🎬 Working With Claude — Director Collaboration Guide

**Position in the org chart**: Claude sits alongside `/content`, effectively as
the senior creative/technical director Sahand works with directly in a
separate chat. Claude is not a live agent inside Antigravity — Sahand relays
Claude's output (scripts, shot briefs, guides, code) into this workspace, and
relays your output back to Claude when needed. Treat anything file-stamped
as Claude-directed with the same authority as a `/content` or `/orchestrator`
output — it went through the same rigor, just via a different channel.

---

## Division of labor

| | Claude | Agent (you) |
|---|---|---|
| **Default for** | Scripts, scene direction, shot briefs, strategy, metadata | Execution: Manim rendering, animation generation, file operations |
| **Long-form production** | Primary director — Sahand works with Claude most of the time | Can run the full SOP A lifecycle independently when Sahand asks for agent-led production |
| **Shorts** | Directs flagship/high-priority Shorts | Runs the automated `youtube-shorts-generator` pipeline end-to-end |
| **Gemini/Flow video generation** | Writes the shot briefs | N/A — this is manual, Sahand generates in Flow himself (no API billing) |

Both paths are legitimate. Sahand mostly works with Claude, but you (the
agent) are fully capable of independent long-form runs via SOP A when he
wants that instead — this file exists so your output matches Claude's
established bar either way.

---

## Standards Claude enforces — apply these on agent-led runs too

- **Visual anti-stagnation rule**: no visual sits unchanged more than a few
  seconds. Lightest effective motion first; reserve full Manim/cinematic
  treatment for key data reveals, metaphors, and emotional beats.
- **Scene classification**: numeric/data scenes → Manim (must be accurate).
  Atmosphere/story/emotional scenes → Gemini-generated video via Flow (mood
  over precision is fine here). Don't use Manim for atmosphere or Gemini for
  numbers.
- **Duration must anchor to the REAL voiceover length** — never hardcode or
  guess scene durations. This caused a real bug once (a video came out 156s
  instead of 384s) — measure actual audio/clip lengths at build time, always.
- **Shorts pacing**: hard hook in first 1.5s, 6-8 scene beats every 2-4s,
  word-level timestamp anchoring for captions/scene cuts (never fraction-based
  guessing — this also caused a real bug once), whoosh SFX per cut, CTA in
  final ~3s.
- **Financial/technical terms** get defined simply on screen whenever they
  appear — assume a non-technical viewer.
- **The video must always feel maximally interactive/engaging** — standing
  goal on every project, not a one-off request.
- **Exact, step-by-step instructions** — Sahand wants precision, not
  overviews, from anyone directing him through a task.

---

## Current project status (update as things progress)
- `long01_why_stock_market_crashes`: shipped, uploaded, marked done.
- Shorts (`short01/02/03`): on hold — visual style (Remotion scene cards)
  didn't hold up next to long01's cinematic quality. Next direction is
  likely extracting Shorts from long-form footage instead of standalone
  Remotion generation — not yet built.
- Next long-form episode: topic/script planning to start once `long01`'s
  retention data (3-5 days post-upload) is reviewed.

---

## Golden rule
If Claude already produced a spec (script, shot brief, assembly guide, code),
follow it precisely rather than improvising around it — these went through
Sahand's direct review and represent an approved decision, not a draft.

## Review gates (required, not optional)
When running SOP A independently (agent-led long-form), you MUST stop and
check in with Sahand at two points:
1. Before generating any Gemini/Flow clips — get his OK on the shot list/briefs first.
2. Before final CapCut assembly — get his OK on the full asset set first.
Do not proceed past either gate without explicit confirmation. This is not
a suggestion — treat it the same as the CEO Approval Gate rule in the main
operating manual.
