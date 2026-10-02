# Token Discipline Implementation & Context Audit Report
**Date**: 2026-09-21  
**Author**: Claude Code

---

## 1. Context Measurement Audit (Always-Loaded Overhead)

| Item | Size (KB) | Estimated Tokens (bytes/4) | Flag (>2,000 tokens) |
|---|---|---|---|
| `CLAUDE.md` | 9.85 KB | ~2,521 tokens | **FLAGGED (>2k)** |
| `.claude/rules/*.md` (Total) | 14.23 KB | ~3,642 tokens | **FLAGGED (>2k)** |
| ├─ `asset-centralization.md` | 0.86 KB | ~220 tokens | |
| ├─ `cleantext-manim.md` | 0.27 KB | ~68 tokens | |
| ├─ `duration-anchoring.md` | 0.29 KB | ~75 tokens | |
| ├─ `gemini-flow-manual-only.md` | 0.23 KB | ~60 tokens | |
| ├─ `hook-discipline.md` | 1.09 KB | ~278 tokens | |
| ├─ `kinetic-popups.md` | 1.19 KB | ~305 tokens | |
| ├─ `longs-style.md` | 3.94 KB | ~1,008 tokens | |
| ├─ `rename-delete-old.md` | 0.83 KB | ~212 tokens | |
| ├─ `scene-classification.md` | 1.00 KB | ~256 tokens | |
| ├─ `scoped-task-locking.md` | 0.26 KB | ~66 tokens | |
| ├─ `shorts-style.md` | 2.28 KB | ~584 tokens | |
| ├─ `token-discipline.md` (New) | 1.14 KB | ~285 tokens | |
| ├─ `visual-style-standard.md` | 1.74 KB | ~446 tokens | |
| └─ `word-level-transcription.md` | 0.26 KB | ~66 tokens | |
| Local Skills Descriptions (14 total) | 4.04 KB | ~1,034 tokens | |
| Plugin Skills Descriptions (Installed) | 18.99 KB | ~4,861 tokens | **FLAGGED (>2k)** |
| MCP: `youtube_studio_mcp` (37 tools) | ~18.50 KB | ~4,625 tokens | **FLAGGED (>2k)** |
| MCP: `browser-use` (2 tools) | ~1.20 KB | ~300 tokens | |
| MCP: Desktop Internal (`ccd_*`, browser, tasks, term) | ~22.00 KB | ~5,500 tokens | **FLAGGED (>2k)** |
| **Total Always-Loaded Context** | **~88.81 KB** | **~22,483 tokens** | **CRITICAL OVERHEAD** |

---

## 2. Rule File Created (`.claude/rules/token-discipline.md`)
Created 13-line rule file defining standing token discipline constraints T1 through T10:
- **T1**: Read `01_PROJECTS/YOUTUBE/STATE.md` first; avoid directory tree scanning.
- **T2**: Enforce <=150 line print limit; slice large JSON/manifest files.
- **T3**: Max 20 lines tool output in chat; redirect raw logs/ffprobe/QA output to `logs\<task>_<date>.txt`.
- **T4**: No redundant re-reads of unchanged files.
- **T5**: Final reports capped at 40 lines (format: DONE / FILES CHANGED / TEST RESULT / OPEN ISSUES); full details to `reports\<task>_<date>.md`.
- **T6**: Delegate multi-file reads (>5) and web audits to subagents (max 30 line return).
- **T7**: MCP servers default to off; explicitly announce usage before invocation.
- **T8**: Single task per session; update `STATE.md` (<=40 lines) and recommend `/clear`.
- **T9**: Asset regeneration prevented if existing files pass `ffprobe`.
- **T10**: Explicit user approval required for tasks >5 min or paid API calls.

---

## 3. Production State File (`01_PROJECTS/YOUTUBE/STATE.md`)
Created 27-line state tracker containing:
- High-level episode status table across all published and in-progress long/short episodes.
- Active CEO Review Gates (Gate 1 script/shot-list, Gate 2 rendered assets).
- Standing QA commands (`longs_qa.py`, `shorts_qa.py`, `verify_manifest_durations.py`).
- Standard paths for `reports\` and `logs\`.
- Mandatory trailing directive: `"Update this file at the end of every task."`

---

## 4. CLAUDE.md Update
Appended single required token discipline directive under the Critical Context Compression block:
```diff
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -7,2 +7,3 @@
 > When `codebase-memory-mcp` is connected in the active session, you must use its tools (such as `query_graph`, `search_graph`, `index_repository`) to gather compressed codebase context before taking actions on a task to burn fewer tokens. When unavailable, fall back to targeted ripgrep and specific file reads.
+Token discipline: follow .claude/rules/token-discipline.md; start every task by reading 01_PROJECTS/YOUTUBE/STATE.md.
```

---

## 5. Heavy Reads Permission Deny Enforcement
Updated `.claude/settings.local.json` to add `permissions.deny` rules blocking `Read` tool execution against media, timeline media, and node_modules:
```diff
--- a/.claude/settings.local.json
+++ b/.claude/settings.local.json
@@ -6,3 +6,19 @@
       "Bash(ffmpeg -i *)"
     ],
+    "deny": [
+      "Read(*.wav)",
+      "Read(*.mp3)",
+      "Read(*.mp4)",
+      "Read(*.mov)",
+      "Read(**/*.wav)",
+      "Read(**/*.mp3)",
+      "Read(**/*.mp4)",
+      "Read(**/*.mov)",
+      "Read(TIMELINE_MEDIA/**)",
+      "Read(**/TIMELINE_MEDIA/**)",
+      "Read(media/**)",
+      "Read(**/media/**)",
+      "Read(node_modules/**)",
+      "Read(**/node_modules/**)"
+    ]
   },
```
### Verification Tests:
1. `Read` on `01_PROJECTS/.../00_SFX_buzzer.wav` -> **BLOCKED** with error: `<tool_use_error>File is in a directory that is denied by your permission settings.</tool_use_error>`.
2. `Read` on `01_PROJECTS/YOUTUBE/pipeline/temp_test_blur.mp4` -> **BLOCKED** with error: `<tool_use_error>File is in a directory that is denied by your permission settings.</tool_use_error>`.
3. `ffprobe` via `Bash` on `00_SFX_buzzer.wav` -> **PASSED** (returned `0.5`s).
4. `ffprobe` via `Bash` on `temp_test_blur.mp4` -> **PASSED** (returned `2.02`s).

---

## 6. Deduplication Audit (Proposals Only)
1. **CLAUDE.md Section 3 vs `.claude/rules/*.md`**:
   - CLAUDE.md Section 3 duplicates 9 standing technical rules almost verbatim from `.claude/rules/` (`duration-anchoring`, `word-level-transcription`, `scoped-task-locking`, `rename-delete-old`, `cleantext-manim`, `gemini-flow-manual-only`, `scene-classification`, `asset-centralization`, `kinetic-popups`).
   - Because `.claude/rules/*.md` is auto-loaded into context on every session alongside `CLAUDE.md`, these 9 rules are loaded twice, consuming ~1,500 duplicate tokens per turn.
   - **Proposal**: Condense Section 3 of `CLAUDE.md` to a concise 1-line pointer per rule pointing to `.claude/rules/`.
2. **Rule Text vs Config JSON**:
   - `longs-style.md` and `pipeline/config/longs_style.json` duplicate numeric targets (freeze times, LUFS, dB delta, WPM, camera push).
   - `shorts-style.md` and `pipeline/config/shorts_style.json` duplicate numeric targets.
   - **Proposal**: Let JSON remain the single source of truth; keep rule markdown files strictly as high-level architectural guidelines referencing the JSON schema.
3. **CleanText Manim Helper**:
   - CleanText code implementation exists in `CLAUDE.md`, `cleantext-manim.md`, and `.claude/skills/manim-text-fix/SKILL.md`.
   - **Proposal**: Move code into shared library (`_shared_lib/`) and reference it as an import rather than repeating the snippet.

---

## 7. MCP Server Optimization (Proposals Only)
1. **`youtube_studio_mcp`** (37 tools, ~4,625 tokens):
   - Currently registered in global `~/.claude.json`. It connects automatically on every session regardless of whether the task involves publishing or YouTube metadata.
   - **Proposal**: Move `youtube_studio_mcp` out of `~/.claude.json` and into a publishing-specific config profile or enable it via `disabledMcpServers` allowlist only when running episode release tasks.
2. **`browser-use`** (2 tools, ~300 tokens):
   - Currently registered as a plugin in `~/.claude.json`.
   - **Proposal**: Keep browser-use opt-in by defaulting `BH_DOMAIN_SKILLS=0` and gating invocations to dedicated packaging/thumbnail research subagents.
