# Token Discipline

T1 Read 01_PROJECTS/YOUTUBE/STATE.md first. Never list or scan directory trees; use paths from STATE.md.
T2 Never print a whole file over 150 lines. Use line ranges, grep -n, or a python one-liner to extract a slice. Never load all_words.json, manifests or any JSON over 100 lines whole; slice it.
T3 Never put tool output over 20 lines into the conversation. Redirect logs, renders, ffprobe and QA output to logs\<task>_<date>.txt and show only the last 20 lines or a summary table.
T4 Do not re-read a file already read this session unless it changed.
T5 Final reports: max 40 lines. Format: DONE / FILES CHANGED (relative paths, grouped by folder, no absolute prefixes) / TEST RESULT (one table, max 12 rows) / OPEN ISSUES. Full detail goes to reports\<task>_<date>.md, not the reply.
T6 Delegate to a subagent (if available) any task that reads more than 5 files or needs web research (audits, grep sweeps, thumbnail research). It returns a summary of max 30 lines.
T7 MCP servers (vidiq, youtube_studio_mcp, others) are off by default. Use one only when the task needs it, and say which before starting.
T8 One task per session. At the end, update STATE.md (max 40 lines), then stop and suggest /clear.
T9 Never regenerate audio/video/render assets that already exist and pass ffprobe. Check the file first.
T10 Ask before any operation that runs >5 min or calls a paid/limited API. vidIQ: free tier ~150 credits/month; outliers = 5 credits; check vidiq_balance first.
T11 No PreToolUse LLM prompt hooks may be added on high-frequency tools (Bash, Read, Write) — enforcement must use zero-token Python command hooks only. Prompt hooks evaluate on every tool call, causing silent quota and token exhaustion.
