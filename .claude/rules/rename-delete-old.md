# Rule: Rename = Delete Old File

## What the Rule Is
Every rename or relocation operation must explicitly delete the original source file immediately after writing or moving to the new target. Never use a copy-and-forget pattern.

## Bug / Incident Prevented
Leaving obsolete source files behind creates phantom duplicates. Downstream automation (e.g., `batch_render.py` or timeline assemblers) globs the folder, finds both the old and renamed versions, and processes stale assets or renders scenes twice.

## Verification Check
Before considering any rename task complete, verify the old file path no longer exists:

```bash
# Verify the old path is deleted and the new path exists
test ! -f "path/to/old_file" && test -f "path/to/new_file" && echo "PASS: Rename clean"
```
Or check the directory listing to ensure zero duplicate stems remain.
