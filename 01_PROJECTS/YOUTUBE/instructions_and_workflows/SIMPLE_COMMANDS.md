# Simple Commands & Auto-Lock Mapping

> Give plain-language commands. Claude internally wraps each in an explicit `IN SCOPE` / `LOCKED` boundary before execution (CLAUDE.md §3.3).

---

## 1. Everyday Command Mappings

| # | Sahand's Plain Input | Internal Scoped-Lock Expansion |
|---|---|---|
| 1 | `make a Short from <long_slug> <start>-<end> [short_slug]` | **IN SCOPE**: `shorts/[NOT_UPLOADED]_[short_slug]/` (raw cut, SRT via faster-whisper, assembly notes).<br>**LOCKED**: `longs/<long_slug>/*`, master renders, `TIMELINE_MEDIA/*`, all other shorts. |
| 2 | `update <slug> status to <NEW_STATUS>` | **IN SCOPE**: Rename `longs/[OLD]_<slug>/` → `[NEW]_<slug>/` (delete old source per §3.4); update `STATE.md`.<br>**LOCKED**: Episode contents, media, scripts, adjacent episode folders. |
| 3 | `run QA on shorts/` (or `shorts/<slug>`) | **IN SCOPE**: Read-only `python pipeline/qa/shorts_qa.py`; report table + `logs/qa_shorts_<date>.txt`.<br>**LOCKED**: All video/audio assets, transcripts, shot lists (zero edits/re-renders). |
| 4 | `run QA on <long_slug>` | **IN SCOPE**: Read-only `python pipeline/qa/longs_qa.py`; report table + `logs/qa_longs_<date>.txt`.<br>**LOCKED**: All media in `TIMELINE_MEDIA/`, scene code, scripts, manifests. |
| 5 | `render scene <N> in <long_slug>` | **IN SCOPE**: `longs/<long_slug>/scenes/scene_<N>.py` & target `TIMELINE_MEDIA/<NN>_scene_<N>.mp4`.<br>**LOCKED**: All other scenes, voiceover stems, CapCut packages, timeline manifests. |
| 6 | `check durations for <long_slug>` | **IN SCOPE**: Read-only `python .claude/hooks/verify_manifest_durations.py`; log to `logs/`.<br>**LOCKED**: All audio/video files (no regeneration per Rule T9), manifests, scenes. |
| 7 | `sync captions for <media_path>` | **IN SCOPE**: Output `captions.srt` & `all_words.json` via faster-whisper.<br>**LOCKED**: Source media file, `TIMELINE_MEDIA/` video files, scene code. |
| 8 | `archive uploaded short <slug>` | **IN SCOPE**: Move `shorts/[UPLOADED]_<slug>/` → `shorts/archived/` (delete old per §3.4); update `STATE.md`.<br>**LOCKED**: Short internal assets, all active `[NOT_UPLOADED]` folders. |
| 9 | `mark uploaded <long_slug>` | **IN SCOPE**: `python pipeline/mark_uploaded.py <long_slug>`, rename to `[PUBLISHED...]`, update `STATE.md`.<br>**LOCKED**: Video/audio assets, all other long-form folders. |
| 10 | `cleanup published <slug>` | **IN SCOPE**: Purge `TIMELINE_MEDIA/`, overlays, intermediate renders, scratch files per `.claude/rules/post-publish-cleanup.md` (first run requires dry-run confirmation).<br>**LOCKED**: Final master video, metadata (`READY_TO_PUBLISH.md`, thumbnail), final script. |

---

## 2. When I Will Stop & Ask You First

Claude halts execution and requires explicit CEO confirmation before proceeding if a command touches:

1. **CEO Review Gates**: Passing Gate 1 (script & shot list approval) or Gate 2 (rendered asset review before CapCut assembly).
2. **Post-Publish Cleanup (First Run)**: Outputting a dry-run manifest and requiring Sahand's go-ahead before deleting any files per `.claude/rules/post-publish-cleanup.md`.
3. **Asset Regeneration**: Overwriting or re-rendering any existing media file that passes `ffprobe` (Rule T9).
4. **Manual Assembly Packages**: Modifying CapCut handoff packages (`assembly_notes.md`, imported cuts, manual timeline files).
5. **Permanent Deletions**: Deleting any source media, scripts, or directories outside of routine rename/temp cleanups.
6. **Billing & Runtime Triggers**: Calling any paid API (Gemini Flow generation is manual-only per §3.6) or tasks running >5 minutes (Rule T10).
7. **Ambiguous Inputs**: Missing timestamp boundaries, missing audio stems, or conflicting episode/short slugs.
