import os
import sys

EPISODE_DIR = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\longs\[PUBLISHED 2026-09-16]_long03_how_algorithms_decide"
OUTPUT_FILE = r"E:\Agentic Workspaces\ClaudeCode\logs\cleanup_dryrun_long03_how_algorithms_decide_2026-09-23.txt"

def format_size(bytes_val):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} TB"

def analyze():
    whitelist_files = []
    deletion_files = []

    total_bytes = 0
    whitelist_bytes = 0
    deletion_bytes = 0

    for root, dirs, files in os.walk(EPISODE_DIR):
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, EPISODE_DIR)
            size = os.path.getsize(full_path)
            total_bytes += size

            # Check Whitelist
            # 1. Master Video File (preserve MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4 or how_algorithms_decide.mp4)
            # 2. Metadata (upload_metadata.md, thumbnails)
            # 3. Final Script (EP03_SCRIPT.md, VISUAL_SHOT_LIST.md, etc.)
            # 4. Status confirmation (PUBLISHED.md, STATUS.md)
            norm_rel = rel_path.replace("\\", "/")

            is_whitelist = False

            if f in ["MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4", "how_algorithms_decide.mp4"]:
                # Master video candidates
                is_whitelist = True
            elif norm_rel.startswith("01_scripts/") and f.endswith(".md"):
                is_whitelist = True
            elif norm_rel.startswith("03_metadata/"):
                is_whitelist = True
            elif f in ["PUBLISHED.md", "STATUS.md", "README.md", "READY_TO_PUBLISH.md"]:
                is_whitelist = True

            if is_whitelist:
                whitelist_files.append((rel_path, size))
                whitelist_bytes += size
            else:
                deletion_files.append((rel_path, size))
                deletion_bytes += size

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("================================================================================\n")
        out.write("QUANTROVE POST-PUBLISH CLEANUP DRY-RUN MANIFEST (FIRST-RUN SAFETY GATE)\n")
        out.write("Episode: long03_how_algorithms_decide (EP03)\n")
        out.write("Date: 2026-09-23\n")
        out.write("Rule: .claude/rules/post-publish-cleanup.md\n")
        out.write("Status: DRY-RUN ONLY — No files have been deleted. Awaiting CEO confirmation.\n")
        out.write("================================================================================\n\n")

        out.write("SUMMARY STATISTICS:\n")
        out.write(f"- Total Files Scanned: {len(whitelist_files) + len(deletion_files)}\n")
        out.write(f"- Total Directory Size: {format_size(total_bytes)}\n")
        out.write(f"- Whitelisted Files (to KEEP): {len(whitelist_files)} files ({format_size(whitelist_bytes)})\n")
        out.write(f"- Files Slated for DELETION: {len(deletion_files)} files ({format_size(deletion_bytes)})\n")
        out.write(f"- Projected Space Recovered: {format_size(deletion_bytes)}\n\n")

        out.write("SAFETY PRESERVATION NOTE:\n")
        out.write("The master final video 'MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4' is currently located in 'TIMELINE_MEDIA/'.\n")
        out.write("Prior to purging 'TIMELINE_MEDIA/', this file MUST be safely relocated to the episode root folder\n")
        out.write("(as 'Quantrove_EP03_HowAlgorithmsDecide_MASTER.mp4') so it is never deleted.\n\n")

        out.write("--------------------------------------------------------------------------------\n")
        out.write("SECTION 1: WHITELISTED FILES TO RETAIN (PERMANENT ARCHIVE)\n")
        out.write("--------------------------------------------------------------------------------\n")
        for p, s in sorted(whitelist_files):
            out.write(f"[KEEP] ({format_size(s):>10}) {p}\n")

        out.write("\n--------------------------------------------------------------------------------\n")
        out.write("SECTION 2: OBSOLETE SCRATCH ASSETS SLATED FOR PURGE (UPON CEO APPROVAL)\n")
        out.write("--------------------------------------------------------------------------------\n")
        for p, s in sorted(deletion_files):
            out.write(f"[DELETE] ({format_size(s):>10}) {p}\n")

    print(f"Manifest written to: {OUTPUT_FILE}")
    print(f"Total: {format_size(total_bytes)} | Whitelist: {format_size(whitelist_bytes)} ({len(whitelist_files)} files) | Purge: {format_size(deletion_bytes)} ({len(deletion_files)} files)")

if __name__ == "__main__":
    analyze()
