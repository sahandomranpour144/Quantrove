# Rule: Post-Publish Cleanup

## Trigger
Whenever an episode's status flips to **Published** — flagged by Sahand in-session (status-sync automation removed 2026-09-26; analytics are manual-only).

## What the Rule Is
When an episode transitions to Published, purge obsolete scratch files and intermediate assets to prevent disk bloat. Retain **strictly** the permanent archival assets.

### Retained Files (Whitelist — Keep ONLY These)
1. **Final Video File**: Master export (`*.mp4` in root or `final/`).
2. **Metadata**: Final publishing package (`READY_TO_PUBLISH.md` or metadata JSON) and thumbnail (`*.png` / `*.jpg`).
3. **Final Script**: Master script and shot list (`*script*.md` or `script_and_shot_list.md`).

### Purged Assets (Delete Everything Else)
- `TIMELINE_MEDIA/` directory (temporary timeline chunks, raw audio stems).
- Kinetic overlay files (alpha MOV renders, intermediate caption clips).
- Intermediate scene renders and build temp dirs (`temp/`, `temp_align/`, `scenes/*.mp4`).
- Working scratch documents, draft shot lists, and superseded assembly notes.

---

## Safety Gate & Confirmation Protocol

1. **First-Run Confirmation Required**:
   - Before deleting any file, Claude must generate a dry-run manifest listing every file slated for deletion and log it to `logs/cleanup_dryrun_<slug>_<date>.txt`.
   - Claude **must pause and wait for Sahand's explicit go-ahead** before proceeding with deletion on the first execution of this rule.
   - **Do not auto-delete on the first run.**

2. **Unattended Execution (Post-Confirmation)**:
   - Once Sahand has confirmed the cleanup protocol once, subsequent published episodes may run the cleanup unattended.
   - All deletions must be logged to `01_PROJECTS/YOUTUBE/CHANGELOG.md` with file counts, freed space, and timestamps.

---

## Verification Check

Confirm that only whitelisted files remain in the published episode folder:

```bash
# Verify only final video, script, and metadata remain; TIMELINE_MEDIA must not exist
test ! -d "01_PROJECTS/YOUTUBE/longs/<published_episode>/TIMELINE_MEDIA" && echo "PASS: TIMELINE_MEDIA purged"
```
