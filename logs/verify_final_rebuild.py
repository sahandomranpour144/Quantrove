import os
import subprocess
import re

timeline_dir = r"01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion/TIMELINE_MEDIA"
manifest_path = r"01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion/01_scripts/TIMELINE_MANIFEST.md"

with open(manifest_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

manifest_items = []
for line in lines:
    m = re.search(r"\|\s*\*\*([^\*]+)\*\*\s*\|\s*`([^`]+)`\s*\|\s*([0-9:.]+)\s*\|\s*([0-9:.]+)\s*\|\s*([0-9.]+s)\s*\|\s*([^|]+)\|\s*([^|]+)\|", line)
    if m:
        scene = m.group(1).strip()
        filename = m.group(2).strip()
        start = m.group(3).strip()
        end = m.group(4).strip()
        dur = float(m.group(5).replace("s","").strip())
        engine = m.group(6).strip()
        desc = m.group(7).strip()
        manifest_items.append((scene, filename, start, end, dur, engine, desc))

log_lines = []
log_lines.append("=========================================================================================")
log_lines.append("EP05 REBUILD: FULL TIMELINE VERIFICATION AUDIT")
log_lines.append("=========================================================================================")
header = f"| {'Scene':6} | {'Assigned':8} | {'Actual (ffprobe)':16} | {'Delta':7} | {'Engine':22} | {'Status':6} |"
log_lines.append(header)
log_lines.append("|---|---|---|---|---|---|")

total_assigned = 0.0
total_actual = 0.0
all_passed = True

for item in manifest_items:
    scene, filename, start, end, dur, engine, desc = item
    total_assigned += dur
    filepath = os.path.join(timeline_dir, filename)
    if not os.path.exists(filepath):
        log_lines.append(f"| {scene:6} | {dur:6.2f}s | {'MISSING FILE':16} | {'N/A':7} | {engine:22} | FAIL   |")
        all_passed = False
        continue
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", filepath]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        actual_dur = float(res.stdout.strip())
        total_actual += actual_dur
        delta = actual_dur - dur
        status = "PASS" if abs(delta) < 0.05 else "FAIL"
        if status != "PASS":
            all_passed = False
        log_lines.append(f"| {scene:6} | {dur:6.2f}s | {actual_dur:14.2f}s | {delta:+6.2f}s | {engine:22} | {status:6} |")
    except Exception as e:
        log_lines.append(f"| {scene:6} | {dur:6.2f}s | ERROR: {e} | N/A | {engine:22} | FAIL   |")
        all_passed = False

log_lines.append("-----------------------------------------------------------------------------------------")
log_lines.append(f"TOTAL V1 TRACK: Assigned = {total_assigned:.2f}s | Actual = {total_actual:.2f}s | Delta = {total_actual - total_assigned:+.2f}s")

# Special stems
log_lines.append("\nSPECIAL STEMS:")
for s in ["00_00m00s_to_05m37s_ep05_master_voiceover.wav", "00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov"]:
    p = os.path.join(timeline_dir, s)
    if os.path.exists(p):
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", p]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        dur = float(res.stdout.strip())
        log_lines.append(f"- {s}: {dur:.2f}s")

output_str = "\n".join(log_lines)
with open("logs/ep05_final_rebuild_verification.txt", "w", encoding="utf-8") as out:
    out.write(output_str)

print(output_str)
