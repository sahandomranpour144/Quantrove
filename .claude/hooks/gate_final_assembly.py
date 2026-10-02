#!/usr/bin/env python3
"""
Gate 2 — Final assembly/render approval hook (PreToolUse).
Fires before any Bash command that runs final episode assembly or master render.
Blocks with exit code 2 unless CEO explicit approval is provided.
"""
import json
import sys
import datetime
import os
import re

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gate_log.jsonl")

ASSEMBLY_PATTERNS = [
    r"python\s+.*(?:assemble_long_form|package_all.*shorts|batch_render\.py)",
    r"ffmpeg\s+.*(?:_MASTER\.mp4|MASTER_EP\d+)",
]

def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    cmd = (payload.get("tool_input", {}) or {}).get("command", "")

    entry = {
        "gate": "final-assembly-render",
        "ts": datetime.datetime.now().isoformat(timespec="seconds"),
        "tool": payload.get("tool_name", "?"),
        "command": cmd[:500],
    }

    is_approved = os.environ.get("GATE2_APPROVED") == "1" or "--ceo-approved" in cmd or "--force" in cmd
    is_triggered = any(re.search(p, cmd, re.IGNORECASE) for p in ASSEMBLY_PATTERNS)

    entry["triggered"] = is_triggered
    entry["approved"] = is_approved

    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception:
        pass

    if is_triggered and not is_approved:
        sys.stderr.write(
            "GATE 2 BLOCK (CEO REVIEW GATE): Final assembly/master render command detected. "
            "Per CLAUDE.md §4, present the full shot list and measured asset durations to Sahand. "
            "Once Sahand gives explicit confirmation, run with GATE2_APPROVED=1 or --ceo-approved.\n"
        )
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()
