# Rule: Asset Centralization in TIMELINE_MEDIA/

## What the Rule Is
All generated visual and audio assets for an episode must be placed into a single `TIMELINE_MEDIA/` folder using standardized chronological prefixes:
`NN_XXmYYs_to_AAmBBs_<description>.<ext>` (e.g., `01_00m00s_to_00m20s_intro_hook.mp4`).

## Bug / Incident Prevented
Decentralized assets spread across temp directories, voiceover subfolders, and code outputs lead to missing media on CapCut import, broken relative paths, and scenes assembled out of sequence.

## Verification Check
Run an inventory check before requesting Gate 2 approval:

```bash
# Verify all files in TIMELINE_MEDIA/ adhere to the chronological prefix format
ls TIMELINE_MEDIA/ | grep -vE '^[0-9]{2}_[0-9]{2}m[0-9]{2}s_to_'
```
The command must return zero lines (empty output). Verify all required scenes from the shot list are present.
