"""Stop hook: checkpoint guard.

If work files changed this session but STATE.md / CHANGELOG.md were not
updated after them, block the stop once and ask Claude to update both.
Uses git status (fast, text-only repo) + mtimes vs the session start stamp.
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
YT = ROOT / "01_PROJECTS" / "YOUTUBE"
TRACKERS = [YT / "STATE.md", YT / "CHANGELOG.md"]
STAMPS = Path(__file__).resolve().parent / ".session_start"
IGNORE = ("logs/", "reports/", ".claude/hooks/", "99_ARCHIVE/")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    if data.get("stop_hook_active"):
        return  # already asked once; never loop
    stamp = STAMPS / data.get("session_id", "unknown")
    if not stamp.exists():
        return
    start = float(stamp.read_text())

    out = subprocess.run(["git", "status", "--porcelain", "-uall"], cwd=ROOT,
                         capture_output=True, text=True, encoding="utf-8").stdout
    changed = []
    for line in out.splitlines():
        rel = line[3:].strip().strip('"')
        p = ROOT / rel
        if rel.startswith(IGNORE) or p in TRACKERS or not p.exists():
            continue
        if p.stat().st_mtime > start:
            changed.append(rel)
    if not changed:
        return
    last_work = max((ROOT / r).stat().st_mtime for r in changed)
    stale = [t.name for t in TRACKERS if not t.exists() or t.stat().st_mtime < last_work]
    if not stale:
        return
    print(json.dumps({"decision": "block", "reason":
        f"Checkpoint: {len(changed)} file(s) changed this session (e.g. {changed[0]}) "
        f"but {' + '.join(stale)} not updated after them. Update {' and '.join(stale)} "
        "(STATE: next action / RESUME line; CHANGELOG: one dated line), keep STATE under 40 lines, then stop."}))


if __name__ == "__main__":
    main()
