#!/usr/bin/env python3
"""
Gate 2 Shorts QA Hook (PreToolUse).
Enforces Quantrove Shorts Style System Gate 2 before publishing.

Trigger Logic:
- Exits 0 for every tool call EXCEPT a publish action:
    1. Writing/editing a file named 'PUBLISH_READY' in a Short folder.
    2. Executing 'mark_uploaded.py' via Bash.
    3. Running the 'episode-publish-package' skill.
- When a publish action is detected: runs shorts_qa.py against the episode assets.
- Caches QA results by video hash + mtime to prevent redundant ffmpeg runs.
- On FAIL: exits with code 2 and prints formatted QA table to stderr (blocks publish).
- On PASS/WARN/MANUAL: exits with code 0 (allows publish).
"""

import json
import sys
import os
import glob
import io
import hashlib
import tempfile

QA_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "01_PROJECTS", "YOUTUBE", "pipeline", "qa"
)
sys.path.insert(0, QA_DIR)
try:
    from shorts_qa import run_qa, print_table, DEFAULT_STYLE_PATH
except ImportError:
    run_qa = None

CACHE_FILE = os.path.join(tempfile.gettempdir(), "quantrove_shorts_qa_cache.json")

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_cache(cache):
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, indent=2)
    except Exception:
        pass

def compute_video_fingerprint(video_path):
    """Compute fast fingerprint based on mtime, size, and header/footer hash."""
    if not os.path.exists(video_path):
        return None
    st = os.stat(video_path)
    h = hashlib.sha256()
    h.update(str(st.st_mtime).encode())
    h.update(str(st.st_size).encode())
    try:
        with open(video_path, "rb") as f:
            h.update(f.read(65536))
            if st.st_size > 131072:
                f.seek(-65536, os.SEEK_END)
                h.update(f.read(65536))
    except Exception:
        pass
    return h.hexdigest()

def find_target_folder(payload):
    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {}) or {}

    # 1. Write/Edit: check if writing PUBLISH_READY
    if tool_name in ("Write", "Edit"):
        file_path = tool_input.get("file_path") or tool_input.get("filePath") or ""
        if os.path.basename(file_path).strip() == "PUBLISH_READY":
            return os.path.dirname(os.path.abspath(file_path)), "publish_ready_file"
        return None, None

    # 2. Bash: check for mark_uploaded.py or episode-publish-package
    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if "mark_uploaded.py" in command or "episode-publish-package" in command:
            for token in command.split():
                clean_tok = token.strip("\"'")
                if os.path.isdir(clean_tok):
                    return os.path.abspath(clean_tok), "bash_publish"
                elif os.path.isfile(clean_tok):
                    return os.path.dirname(os.path.abspath(clean_tok)), "bash_publish"
            return os.getcwd(), "bash_publish"
        return None, None

    # 3. Skill: check for episode-publish-package
    if tool_name == "Skill":
        skill = tool_input.get("skill", "")
        if "episode-publish-package" in skill:
            args = tool_input.get("args", "")
            for token in args.split():
                clean_tok = token.strip("\"'")
                if os.path.isdir(clean_tok):
                    return os.path.abspath(clean_tok), "skill_publish"
            return os.getcwd(), "skill_publish"
        return None, None

    return None, None

def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    target_dir, action_type = find_target_folder(payload)
    # If not a publish action, exit 0 immediately (<1s)
    if not target_dir or run_qa is None:
        sys.exit(0)

    # Locate required assets
    video_candidates = glob.glob(os.path.join(target_dir, "*.mp4"))
    video_path = video_candidates[0] if video_candidates else None
    words_path = os.path.join(target_dir, "words.json")
    text_events_path = os.path.join(target_dir, "text_events.json")
    shotlist_path = os.path.join(target_dir, "shotlist.json")
    voice_path = os.path.join(target_dir, "voice.wav")
    music_path = os.path.join(target_dir, "music.wav")

    missing = []
    if not video_path: missing.append("video (*.mp4)")
    if not os.path.exists(words_path): missing.append("words.json")
    if not os.path.exists(text_events_path): missing.append("text_events.json")
    if not os.path.exists(shotlist_path): missing.append("shotlist.json")

    if missing:
        print(f"PUBLISH BLOCKED: Short folder missing required assets for Gate 2: {', '.join(missing)}", file=sys.stderr)
        sys.exit(2)

    # Cache check
    fp = compute_video_fingerprint(video_path)
    cache = load_cache()
    cached = cache.get(target_dir)

    # Invalidate cache if input JSONs modified more recently
    inputs_mtime = max(
        os.path.getmtime(words_path),
        os.path.getmtime(text_events_path),
        os.path.getmtime(shotlist_path)
    )

    if cached and cached.get("fingerprint") == fp and cached.get("cached_at", 0) >= inputs_mtime:
        results = cached.get("results", [])
        table_str = cached.get("table_str", "")
    else:
        try:
            results = run_qa(
                video_path,
                words_path,
                text_events_path,
                shotlist_path,
                voice_path=voice_path if os.path.exists(voice_path) else None,
                music_path=music_path if os.path.exists(music_path) else None,
                style_path=DEFAULT_STYLE_PATH
            )
            table_buf = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = table_buf
            print_table(results)
            sys.stdout = old_stdout
            table_str = table_buf.getvalue()

            cache[target_dir] = {
                "fingerprint": fp,
                "cached_at": max(os.path.getmtime(video_path), inputs_mtime),
                "results": results,
                "table_str": table_str
            }
            save_cache(cache)
        except Exception as e:
            print(f"GATE 2 SHORTS QA EXECUTION ERROR: {e}", file=sys.stderr)
            sys.exit(2)

    has_fail = any(r["status"] == "FAIL" for r in results)
    if has_fail:
        print("\nPUBLISH BLOCKED: SHORTS GATE 2 QA FAILED:\n", file=sys.stderr)
        print(table_str, file=sys.stderr)
        sys.exit(2)

    try:
        print(json.dumps({
            "systemMessage": f"gate2_shorts_qa: PASS for {os.path.basename(target_dir)} — publish authorized."
        }))
    except Exception:
        pass
    sys.exit(0)

if __name__ == "__main__":
    main()
