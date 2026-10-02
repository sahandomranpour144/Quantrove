#!/usr/bin/env python3
"""
Gate 1 — Gemini/Flow clip generation approval hook (PreToolUse).
Fires before any Bash command that would generate new Gemini/Flow video clips.
Blocks with exit code 2 if an automated generation script/API call is detected.
"""
import json
import sys
import datetime
import os
import re

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gate_log.jsonl")

GEN_PATTERNS = [
    r"python\s+.*(?:veo|gemini.*clip|flow.*gen)",
    r"curl\s+.*(?:generativelanguage\.googleapis\.com|veo)",
    r"api\.google.*generate_video",
]

def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    cmd = (payload.get("tool_input", {}) or {}).get("command", "")

    entry = {
        "gate": "gemini-flow-generation",
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "tool": payload.get("tool_name", "?"),
        "command": cmd[:500],
    }

    is_blocked = any(re.search(p, cmd, re.IGNORECASE) for p in GEN_PATTERNS)
    entry["blocked"] = is_blocked

    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass

    if is_blocked:
        sys.stderr.write(
            "GATE 1 BLOCK (CEO REVIEW GATE): Automated Gemini/Flow clip generation via API is prohibited "
            "per CLAUDE.md §3.6. Prompts must be executed manually by Sahand in labs.google/flow.\n"
        )
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()
