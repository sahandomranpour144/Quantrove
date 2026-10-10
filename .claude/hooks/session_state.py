"""SessionStart hook: inject a compact STATE digest so sessions start oriented.

Reads 01_PROJECTS/YOUTUBE/STATE.md, keeps only active episode rows (drops
finished PUBLISHED rows), adds a size warning when STATE grows past budget,
and records the session start time for state_checkpoint.py.
Local files only; never calls any MCP / network (see CLAUDE.md analytics rule).
"""
import json, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "01_PROJECTS" / "YOUTUBE" / "STATE.md"
STAMPS = Path(__file__).resolve().parent / ".session_start"
MAX_LINES, MAX_BYTES = 40, 6000
DONE = ("none", "confirmed")


def digest(text):
    out = []
    for line in text.splitlines():
        if line.startswith("|") and "[PUBLISHED" in line:
            cells = [c.strip().lower() for c in line.strip("|").split("|")]
            if len(cells) > 2 and cells[2].startswith(DONE):
                continue
        out.append(line)
    return "\n".join(out)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    sid = data.get("session_id", "unknown")
    STAMPS.mkdir(exist_ok=True)
    (STAMPS / sid).write_text(str(time.time()))
    for old in STAMPS.iterdir():  # prune stamps older than 7 days
        if time.time() - old.stat().st_mtime > 7 * 86400:
            old.unlink(missing_ok=True)

    if not STATE.exists():
        return
    text = STATE.read_text(encoding="utf-8")
    msg = ["# STATE digest (auto-injected; do not re-read STATE.md unless editing it)",
           digest(text)]
    lines, size = len(text.splitlines()), len(text.encode("utf-8"))
    if lines > MAX_LINES or size > MAX_BYTES:
        msg.append(f"\n> STATE.md over budget ({lines} lines / {size} bytes; limit "
                   f"{MAX_LINES}/{MAX_BYTES}). Move finished detail to CHANGELOG.md this session.")
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": "\n".join(msg)}}))


if __name__ == "__main__":
    main()
