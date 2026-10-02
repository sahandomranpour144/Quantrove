---
name: pre-publish-checklist
description: Use before publishing or scheduling any episode (long-form or Shorts) 
— runs a full technical and visual QA pass across every standing rule before the 
episode leaves [IN_PROGRESS] status. Complements episode-publish-package, which 
only handles metadata.
---

# Pre-Publish Checklist

Run this as the final gate before any episode moves to [SCHEDULED] or 
[PUBLISHED]. Do not skip items — report every check explicitly, pass or fail, 
don't just report failures.

## Checks (run all, report each)

1. **Duration anchoring** — every clip/scene duration in the manifest matches 
   ffprobe-measured real file length within ±0.1s (per duration-check skill)
2. **Word-sync accuracy** — captions/kinetic pop-ups align to faster-whisper 
   word-level timestamps, not proportional guessing (per word-sync skill)
3. **Scoped-task compliance** — no unintended files touched outside what was 
   explicitly worked on this session (per scoped-task-lock skill)
4. **CleanText compliance** — all Manim text uses native Text() with CleanText 
   vector scaling, no raw low-point bold text (per manim-text-fix skill)
5. **Asset centralization** — all episode assets live in one TIMELINE_MEDIA/ 
   folder with chronological timestamp-prefixed filenames
6. **Kinetic pop-ups present** — long-form has the 60fps RGBA MOV overlay on 
   CapCut Track V2; Shorts have burned-in bouncing word pops
7. **Visual style standard** — dark near-black background, correct font weight 
   hierarchy (bold titles/keywords, medium body), high-contrast text, no static 
   frame held >3-4s without an explicit deliberate-hold note
8. **Rename hygiene** — no duplicate/orphaned files left behind from any 
   rename operation this session
9. **Metadata package** — upload_metadata.md exists and is complete 
   (per episode-publish-package skill) — title, chapters, description, tags, 
   pinned comment

## On failure
If any check fails, stop and report which one(s) — do not proceed to publish 
status. Fix and re-run the full checklist, don't just re-check the failed item, 
since fixes sometimes break something else on the list.

## Output
A short pass/fail table, one row per check, at the end of the run.
