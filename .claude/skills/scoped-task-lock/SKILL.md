---
name: scoped-task-lock
description: The discipline of explicitly declaring what is LOCKED (out of scope, must not be touched) before starting any narrow/scoped task. Use at the start of every small task — especially ones near manually-edited files, CapCut assembly packages, or in-progress episodes — to stop scope creep from destroying manual edits.
---

# Scoped Task Lock — Declare Boundaries Before Touching Anything

## Why

Narrow tasks drift. An agent asked to fix one caption re-renders a scene, "helpfully" renames a file, or regenerates a timeline — and destroys manual work: CapCut assembly edits, hand-tuned Manim constants, files Sahand touched outside the pipeline. The LOCK declaration makes scope creep structurally impossible instead of a good intention.

## Procedure

### 1. Before starting, enumerate in your reply

- **IN SCOPE**: the exact files/directories this task may create, modify, or delete.
- **LOCKED**: everything adjacent that must not be touched — named explicitly. Example: "IN SCOPE: `shorts/[SCHEDULED 2026-09-14] ep02_short_best_day_to_invest/` captions only. LOCKED: all `TIMELINE_MEDIA/` folders, every `STATUS.md`, all other shorts, `pipeline/`."

### 2. Rules during execution

- If a needed change falls outside the declared scope: **stop, surface it, ask**. Never silently expand.
- Renames within scope must delete the old file — never copy-and-leave-a-duplicate (CLAUDE.md §3.4).
- Manual-edit zones are LOCKED by default unless the task explicitly says otherwise:
  - CapCut handoff packages (`assembly_notes.md`, *_raw_9x16.mp4 already imported)
  - Anything under a `[PUBLISHED]` episode folder
  - Files modified after the last pipeline run
- State the LOCK even when the task looks trivially local — adjacency is where the damage happens.

### 3. Report at the end

List what was actually created/modified/deleted, and confirm nothing LOCKED was touched. If anything LOCKED had to change, that should have surfaced in step 2 — a surprise in the final report is a process failure.

## Origin

Sahand's standing rule (CLAUDE.md §3.3). No legacy or pipeline procedure existed for this — it is the operationalization of his instruction: "When given a narrow/scoped task, explicitly state what is LOCKED and must not be touched."
