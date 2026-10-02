import os
import sys
import re
import datetime

PROJECT_ROOT = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE"
CATEGORIES = ["longs", "shorts"]

PREFIX_MAP = {
    "in_progress": "[IN_PROGRESS]",
    "scheduled": "[SCHEDULED]",
    "published": "[PUBLISHED]",
    "done": "[PUBLISHED]"
}

def clean_slug_name(dir_name):
    # Remove any existing bracketed prefix or status prefix (e.g. [PUBLISHED 2026-09-02], [IN_PROGRESS], etc.)
    cleaned = re.sub(r"^(\[[A-Z0-9_\s-]+\]|\b(DONE|PUBLISHED|SCHEDULED|IN_PROGRESS)\b)[\s_-]*", "", dir_name, flags=re.IGNORECASE)
    return cleaned.strip()

def find_target_directory(slug):
    slug_norm = slug.lower().strip()
    matches = []
    
    for cat in CATEGORIES:
        cat_path = os.path.join(PROJECT_ROOT, cat)
        if not os.path.isdir(cat_path):
            continue
        for entry in os.listdir(cat_path):
            full_entry = os.path.join(cat_path, entry)
            if not os.path.isdir(full_entry) or entry.startswith("_"):
                continue
            
            clean_name = clean_slug_name(entry).lower()
            if slug_norm in clean_name or clean_name in slug_norm or slug_norm == entry.lower():
                matches.append((cat_path, entry, clean_slug_name(entry)))
                
    return matches

def mark_uploaded(slug, status="published", pub_date=None):
    status_key = status.lower()
    if status_key not in PREFIX_MAP:
        print(f"[ERROR] Invalid status '{status}'. Valid options: {list(PREFIX_MAP.keys())}")
        return False

    raw_prefix = PREFIX_MAP[status_key].strip("[]")
    if not pub_date:
        pub_date = datetime.date.today().strftime("%Y-%m-%d")
    
    prefix = f"[{raw_prefix} {pub_date}]"
    matches = find_target_directory(slug)
    
    if not matches:
        print(f"[ERROR] No folder matching '{slug}' found in {CATEGORIES}.")
        return False
    
    if len(matches) > 1:
        print(f"[WARN] Multiple folders matched '{slug}': {[m[1] for m in matches]}. Using first match: {matches[0][1]}")

    parent_dir, current_dir_name, base_slug = matches[0]
    new_dir_name = f"{prefix} {base_slug}"
    
    current_full_path = os.path.join(parent_dir, current_dir_name)
    new_full_path = os.path.join(parent_dir, new_dir_name)

    if current_dir_name != new_dir_name:
        try:
            os.rename(current_full_path, new_full_path)
            print(f"[OK] Renamed folder: '{current_dir_name}' -> '{new_dir_name}'")
            target_path = new_full_path
        except Exception as e:
            print(f"[ERROR] Failed to rename folder: {e}")
            target_path = current_full_path
    else:
        print(f"[INFO] Folder already named '{new_dir_name}'")
        target_path = new_full_path

    # Update status markers inside folder
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if status_key in ("published", "done"):
        # Remove SCHEDULED.md if exists
        sched_file = os.path.join(target_path, "SCHEDULED.md")
        if os.path.exists(sched_file):
            try:
                os.remove(sched_file)
            except Exception:
                pass
        marker = os.path.join(target_path, "UPLOADED.md")
        with open(marker, "w", encoding="utf-8") as f:
            f.write(f"# Uploaded\n\nConfirmed published on {now_str}.\nStatus: LIVE on YouTube.\n")
        print(f"[OK] Wrote marker: {marker}")
    elif status_key == "scheduled":
        marker = os.path.join(target_path, "SCHEDULED.md")
        with open(marker, "w", encoding="utf-8") as f:
            f.write(f"# Scheduled\n\nConfirmed scheduled on {now_str}.\nStatus: Scheduled in YouTube Studio.\n")
        print(f"[OK] Wrote marker: {marker}")
    elif status_key == "in_progress":
        marker = os.path.join(target_path, "STATUS.md")
        with open(marker, "w", encoding="utf-8") as f:
            f.write(f"# In Progress\n\nStarted on {now_str}.\nActive production underway.\n")
        print(f"[OK] Wrote marker: {marker}")

    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mark_uploaded.py <episode_slug> [--status published|scheduled|in_progress] [--date YYYY-MM-DD]")
        sys.exit(1)
    
    slug_arg = sys.argv[1]
    status_arg = "published"
    date_arg = None

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--status" and i + 1 < len(sys.argv):
            status_arg = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--date" and i + 1 < len(sys.argv):
            date_arg = sys.argv[i + 1]
            i += 2
        elif not sys.argv[i].startswith("--"):
            status_arg = sys.argv[i]
            i += 1
        else:
            i += 1

    success = mark_uploaded(slug_arg, status_arg, date_arg)
    sys.exit(0 if success else 1)