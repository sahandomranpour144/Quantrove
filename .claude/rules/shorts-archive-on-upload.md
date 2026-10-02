# Rule: Shorts Archive on Upload

## What the Rule Is
Any time a YouTube Short is confirmed uploaded/live (or scheduled/published in YouTube Studio), its local folder must be moved into `01_PROJECTS/YOUTUBE/shorts/_ARCHIVE/published/` — not just relabeled in place.
- The folder name (e.g., `[UPLOADED]_<short_slug>`) and its contents are preserved exactly as-is.
- Top-level `01_PROJECTS/YOUTUBE/shorts/` is reserved strictly for active, in-progress, or not-yet-uploaded Shorts (`[NOT_UPLOADED]_...`).
- This applies to all future uploads, automated or manual, across all content pillars.

## Bug / Incident Prevented
Leaving uploaded Shorts folders at the top level of `shorts/` clutters the workspace, makes pipeline scanning and status audits error-prone, risks confusing active work with completed releases, and bloats directory listings for automated tools.

## Verification Check
Confirm top-level `01_PROJECTS/YOUTUBE/shorts/` contains zero `[UPLOADED]_` folders and all confirmed uploads reside inside `archived/`:

```bash
# Verify no uploaded folders remain at top-level shorts/
ls -d 01_PROJECTS/YOUTUBE/shorts/\[UPLOADED\]_* 2>/dev/null || echo "PASS: Top-level shorts clean"

# Verify uploaded folders reside in archived/
ls -d 01_PROJECTS/YOUTUBE/shorts/_ARCHIVE/published/\[UPLOADED\]_*
```
