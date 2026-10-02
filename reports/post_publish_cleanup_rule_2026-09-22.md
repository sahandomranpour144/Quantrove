# Task Report: Post-Publish Cleanup Rule & Pipeline Integration

- **Date**: 2026-09-22
- **Task**: Author `.claude/rules/post-publish-cleanup.md` and wire into recurring `youtube-studio-status-sync` automation.

## Summary
Created the post-publish cleanup rule enforcing a strict whitelist-retention model:
- Retain: final video (`*.mp4`), metadata (`READY_TO_PUBLISH.md`, thumbnail), and final script (`*script*.md`).
- Delete: `TIMELINE_MEDIA/`, overlays, intermediate renders, and working scratch docs.
- First-run safety gate: Requires a dry-run list and Sahand's explicit confirmation before executing deletions. Unattended execution allowed only post-confirmation.
- Integration: Updated the scheduled task `youtube-studio-status-sync` to seamlessly trigger this cleanup check upon detecting an episode's flip to `PUBLISHED` (`privacyStatus: public`).
- Updated `SIMPLE_COMMANDS.md` and `STATE.md` with pointers to the new rule.
