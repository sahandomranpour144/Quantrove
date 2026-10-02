#!/usr/bin/env python3
"""
ffprobe duration validator (PreToolUse, matcher Write|Edit).

Runs whenever a scene manifest / timeline / batch queue file is written.
For every media file referenced with a duration value in the manifest, runs
ffprobe against the real file and compares. Fails loudly (exit 2, blocking)
if any manifest duration differs from the measured value by more than 0.1s
or if a referenced media file is missing.

Exit codes (Claude Code hook protocol):
  0 = pass (or nothing to check — non-manifest writes flow through freely)
  2 = block, reason printed to stderr is fed back to the model
"""
import json
import sys
import os
import re
import subprocess

TOLERANCE_S = 0.1
MEDIA_EXTS = (".mp4", ".mp3", ".wav", ".mov", ".m4a", ".aac", ".flac", ".mkv", ".webm")
MANIFEST_HINTS = ("manifest", "timeline", "batch_queue", "shot_list", "scene_list",
                  "TIMELINE_INDEX", "scene_offsets", "assembly")
DURATION_KEYS = ("duration", "duration_sec", "duration_s", "dur", "target_duration",
                 "nominal_duration", "end", "runtime", "length")


def ffprobe_duration(path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration",
           "-of", "default=noprint_wrappers=1:nokey=1", path]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if out.returncode != 0:
            return None
        return float(out.stdout.strip())
    except Exception:
        return None


def find_manifest(path):
    # NOTE: PreToolUse fires BEFORE the write, so the file may not exist yet
    # (new manifests). Decide by NAME, not existence.
    if not path:
        return None
    name = os.path.basename(path).lower()
    if name.endswith(".json") or any(h.lower() in name.lower() for h in MANIFEST_HINTS):
        return path
    return None


def walk_for_media_refs(node, refs, path_prefix=None):
    """Recursively collect (media_path_candidate, claimed_duration) pairs from a JSON tree."""
    if isinstance(node, dict):
        media = None
        dur = None
        for k, v in node.items():
            kl = str(k).lower()
            if isinstance(v, str) and v.lower().endswith(MEDIA_EXTS):
                media = v
            if any(d in kl for d in DURATION_KEYS) and isinstance(v, (int, float)):
                dur = float(v)
        if media is not None and dur is not None:
            refs.append((media, dur))
        for v in node.values():
            walk_for_media_refs(v, refs, path_prefix)
    elif isinstance(node, list):
        for v in node:
            walk_for_media_refs(v, refs, path_prefix)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # can't parse hook input — don't block the tool

    tool_input = payload.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path") or tool_input.get("filePath") or ""
    if not file_path:
        sys.exit(0)

    manifest = find_manifest(file_path)
    if manifest is None:
        sys.exit(0)  # not a manifest write — pass through

    content = tool_input.get("content") or tool_input.get("new_string") or ""
    if not content:
        sys.exit(0)  # nothing to validate (e.g., Edit with no content field visible)

    refs = []
    # JSON manifests: parse fully
    try:
        data = json.loads(content)
        walk_for_media_refs(data, refs)
    except Exception:
        # Non-JSON (or partial-edit) manifest: regex scan for "file": "...", "duration": N pairs
        pattern = re.compile(
            r'["\']?([\w\s\\/:\.\-\[\]\(\)]+\.(?:' + "|".join(e.lstrip(".") for e in MEDIA_EXTS) + r'))["\']?\s*[,:\]]?\s*["\']?(?:duration|dur|target_duration)["\']?\s*[:=]\s*([0-9]+(?:\.[0-9]+)?)',
            re.IGNORECASE)
        for m in pattern.finditer(content):
            refs.append((m.group(1), float(m.group(2))))

    if not refs:
        sys.exit(0)  # no duration-bearing media references found — nothing to verify

    manifest_dir = os.path.dirname(os.path.abspath(manifest))
    errors = []
    checked = 0
    for media_ref, claimed in refs:
        cand = media_ref if os.path.isabs(media_ref) else os.path.join(manifest_dir, media_ref)
        if not os.path.exists(cand):
            # also try relative to workspace root (manifests sometimes reference from project root)
            root_cand = os.path.normpath(os.path.join(manifest_dir, "..", "..", "..", media_ref))
            if os.path.exists(root_cand):
                cand = root_cand
            else:
                errors.append(f"MISSING media file: {media_ref} (resolved: {cand})")
                continue
        real = ffprobe_duration(cand)
        if real is None:
            errors.append(f"ffprobe failed on: {cand}")
            continue
        checked += 1
        if abs(real - claimed) > TOLERANCE_S:
            errors.append(
                f"DURATION MISMATCH: {os.path.basename(media_ref)} — manifest says {claimed}s, "
                f"real file is {real:.3f}s (diff {real - claimed:+.3f}s)")

    if errors:
        print("DURATION VALIDATION FAILED — this manifest was NOT written:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print(f"  ({checked} file(s) verified OK before failure)", file=sys.stderr)
        sys.exit(2)  # block the write

    # pass: optionally note verification count via stdout JSON systemMessage
    try:
        print(json.dumps({
            "systemMessage": f"duration-validator: {checked} media file(s) verified against ffprobe — all match."
        }))
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
