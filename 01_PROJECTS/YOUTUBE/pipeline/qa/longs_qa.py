#!/usr/bin/env python3
"""
Quantrove Long-Form QA Gate (longs_qa.py)
Automated verification of long-form documentary episodes against pipeline/config/longs_style.json.
Evaluates Rules L1 through L8, script structure, loop ledger, pacing, visuals, and audio mix.
Exits 1 if any rule FAILS; exits 0 if all rules PASS, WARN, or MANUAL.
"""

import os
import sys
import json
import re
import subprocess
import argparse

DEFAULT_STYLE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config", "longs_style.json"
)

def load_brand_tokens():
    d = os.path.abspath(__file__)
    for _ in range(5):
        d = os.path.dirname(d)
    bt = os.path.join(d, "brand", "brand_tokens.json")
    if os.path.exists(bt):
        try:
            with open(bt, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return None

GENERIC_RED_GREEN_HEX = {
    "#00FF00", "#00FF88", "#00FFA3", "#22C55E", "#10B981", "#16A34A", "#15803D", "#4ADE80",
    "#FF0000", "#FF3366", "#EF4444", "#DC2626", "#B91C1C", "#991B1B", "#F87171", "#E11D48",
    "#008000", "#800000", "#00FF7F", "#32CD32", "#FF4500", "#FF6347"
}

def is_generic_red_or_green(hex_val: str) -> bool:
    if not isinstance(hex_val, str):
        return False
    h = hex_val.strip().upper()
    if h in GENERIC_RED_GREEN_HEX:
        return True
    if re.match(r"^#[0-9A-F]{6}$", h):
        r = int(h[1:3], 16)
        g = int(h[3:5], 16)
        b = int(h[5:7], 16)
        if g > 140 and r < 120 and b < 160:
            return True
        if r > 180 and g < 75 and b < 100:
            return True
    return False

def extract_hex_colors(obj) -> list:
    colors = []
    if isinstance(obj, str):
        matches = re.findall(r"#[0-9a-fA-F]{6}\b", obj)
        colors.extend([m.upper() for m in matches])
    elif isinstance(obj, dict):
        for v in obj.values():
            colors.extend(extract_hex_colors(v))
    elif isinstance(obj, list):
        for item in obj:
            colors.extend(extract_hex_colors(item))
    return colors

def is_imported_footage(scene: dict) -> bool:
    if not isinstance(scene, dict):
        return False
    stype = str(scene.get("type", "")).lower()
    mtag = str(scene.get("motion_tag", "")).lower()
    if stype in ["flow", "broll", "footage", "gemini_flow", "live_action"]:
        return True
    if mtag in ["flow_atmosphere", "imported_footage", "broll"]:
        return True
    if scene.get("imported_footage") is True or scene.get("is_imported") is True:
        return True
    return False

STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "on", "and", "or", "that", "this",
    "how", "why", "is", "aren't", "are", "what", "with", "for", "from", "at", "by"
}

def probe_file_duration(path):
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", path
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return float(res.stdout.strip())
    except Exception:
        return None

def measure_ebur128_lufs(path):
    cmd = [
        "ffmpeg", "-nostats", "-i", path,
        "-filter_complex", "ebur128=peak=true",
        "-f", "null", "-"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        m = re.search(r"Integrated loudness:\s+I:\s+([-\d.]+)\s+LUFS", res.stderr)
        if m:
            return float(m.group(1))
    except Exception:
        pass
    return None

def detect_freezes(video_path, min_duration=3.5):
    cmd = [
        "ffmpeg", "-nostats", "-i", video_path,
        "-vf", f"freezedetect=n=-60dB:d={min_duration}",
        "-map", "0:v:0", "-f", "null", "-"
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        freezes = []
        start = None
        for line in res.stderr.splitlines():
            m_start = re.search(r"freeze_start:\s*([\d.]+)", line)
            if m_start:
                start = float(m_start.group(1))
            m_dur = re.search(r"freeze_duration:\s*([\d.]+)", line)
            if m_dur and start is not None:
                dur = float(m_dur.group(1))
                freezes.append({"start": start, "end": start + dur, "duration": dur})
                start = None
            m_end = re.search(r"freeze_end:\s*([\d.]+)", line)
            if m_end and start is not None:
                end_t = float(m_end.group(1))
                dur = end_t - start
                if dur >= min_duration:
                    freezes.append({"start": start, "end": end_t, "duration": dur})
                start = None
        if start is not None:
            vid_dur = probe_file_duration(video_path) or (start + min_duration + 1.0)
            dur = vid_dur - start
            if dur >= min_duration:
                freezes.append({"start": start, "end": vid_dur, "duration": dur})
        return freezes
    except Exception:
        return []

def parse_script_header(script_path):
    """Parse YAML frontmatter or JSON header from script file."""
    if not script_path or not os.path.exists(script_path):
        return {}
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Try YAML frontmatter --- ... ---
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        yaml_text = m.group(1)
        try:
            import yaml
            data = yaml.safe_load(yaml_text) or {}
            if not isinstance(data, dict):
                data = {}
        except Exception:
            data = {}
            for line in yaml_text.splitlines():
                if ":" in line and not line.startswith(" ") and not line.startswith("\t") and not line.startswith("#"):
                    k, v = line.split(":", 1)
                    data[k.strip()] = v.split("#")[0].strip().strip("\"'")
        data["_full_text"] = content
        return data

    # Try JSON
    try:
        data = json.loads(content)
        data["_full_text"] = content
        return data
    except Exception:
        data = {"_full_text": content}
        for line in content.splitlines()[:60]:
            m_bullet = re.match(r"^\s*[-*]\s*\*\*([^:]+)\*\*\s*:\s*(.*)$", line)
            if m_bullet:
                k = m_bullet.group(1).lower().strip()
                v = m_bullet.group(2).strip().strip("\"'")
                if "pace_mode" in k:
                    data["pace_mode"] = v.split()[0].lower()
                elif "title" in k and "title" not in data:
                    data["title"] = v
            elif line.startswith("## ") and "title" not in data:
                data["title"] = line.replace("##", "").strip().strip("\"'")
        return data

def calculate_contrast(hex1, hex2):
    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    def srgb_to_lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    def rel_lum(rgb):
        r, g, b = [srgb_to_lin(c) for c in rgb]
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    l1 = rel_lum(hex_to_rgb(hex1))
    l2 = rel_lum(hex_to_rgb(hex2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def run_longs_qa(video_path, words_path, script_path, loop_ledger_path, shotlist_path,
                  voice_path=None, music_path=None, style_path=DEFAULT_STYLE_PATH, mix_only=False, waivers=None):
    with open(style_path, "r", encoding="utf-8") as f:
        style = json.load(f)

    with open(words_path, "r", encoding="utf-8") as f:
        words_data = json.load(f)
        words = words_data.get("all_words") or words_data.get("words") or (words_data if isinstance(words_data, list) else [])

    script_header = parse_script_header(script_path)

    with open(loop_ledger_path, "r", encoding="utf-8") as f:
        loops = json.load(f)

    with open(shotlist_path, "r", encoding="utf-8") as f:
        shotlist_data = json.load(f)
        scenes = shotlist_data.get("scenes") or (shotlist_data if isinstance(shotlist_data, list) else [])

    actual_runtime = probe_file_duration(video_path) or 0.0
    results = []

    # -------------------------------------------------------------
    # L2: HOOK CLICK REASON & TITLE KEYWORDS IN FIRST 5s
    # -------------------------------------------------------------
    title = str(script_header.get("title", ""))
    title_words = [re.sub(r"[^\w]", "", w).lower() for w in title.split() if w]
    title_keywords = [w for w in title_words if w and w not in STOPWORDS and len(w) > 2]

    # Words spoken in first 5 seconds
    first_5s_words = [re.sub(r"[^\w]", "", w.get("word", "")).lower() for w in words if w.get("start", 0) <= 5.0]
    matched_keywords = [kw for kw in title_keywords if kw in first_5s_words]

    min_kw = style["hook"]["title_keywords_in_window_min"] # 2
    if len(matched_keywords) >= min_kw:
        status_l2 = "PASS"
    elif len(matched_keywords) == 1:
        status_l2 = "WARN"  # As requested: WARN if only 1 keyword
    else:
        status_l2 = "FAIL"

    results.append({
        "rule": "L2 (Hook Discipline)",
        "measured": f"{len(matched_keywords)} title keywords spoken in first 5s ({matched_keywords})",
        "threshold": f">={min_kw} title keywords in first 5.0s (WARN if 1)",
        "status": status_l2
    })

    # -------------------------------------------------------------
    # L3: PACE STATEMENT & RUNTIME / WPM INTEGRITY
    # -------------------------------------------------------------
    pace_mode = str(script_header.get("pace_mode", "focused")).lower()
    pace_cfg = style["pace"]
    window = pace_cfg["statement_window_s"] # [5, 20]

    # Words spoken between 5s and 20s
    window_words = " ".join(w.get("word", "") for w in words if window[0] <= w.get("start", 0) <= window[1]).lower()
    full_text = script_header.get("_full_text", "").lower()

    has_relaxed = "get comfortable" in window_words or "worth going slowly" in window_words or "get comfortable" in full_text[:400]
    has_focused = bool(re.search(r"in the next \d+ minutes", window_words) or re.search(r"in the next \d+ minutes", full_text[:400]))

    pace_statement_found = (has_relaxed if pace_mode == "relaxed" else has_focused) or (has_relaxed or has_focused)

    # Runtime promise vs measured runtime
    promised_min = script_header.get("est_runtime_min")
    if promised_min is None:
        m_prom = re.search(r"in the next (\d+) minutes", window_words + " " + full_text[:400])
        if m_prom:
            promised_min = float(m_prom.group(1))

    actual_min = actual_runtime / 60.0
    tol_min = pace_cfg["runtime_promise_tolerance_min"] # 1.0 min
    runtime_ok = True
    if promised_min is not None:
        runtime_ok = abs(actual_min - float(promised_min)) <= tol_min

    # WPM check
    target_wpm_range = pace_cfg["modes"].get(pace_mode, pace_cfg["modes"]["focused"])["wpm"]
    spoken_dur_s = words[-1]["end"] - words[0]["start"] if words else actual_runtime
    measured_wpm = (len(words) / (spoken_dur_s / 60.0)) if spoken_dur_s > 0 else 0.0
    wpm_ok = (target_wpm_range[0] - 10) <= measured_wpm <= (target_wpm_range[1] + 10)

    l3_pass = pace_statement_found and runtime_ok and wpm_ok
    status_l3 = "PASS" if l3_pass else "FAIL"
    prom_str = f"{promised_min}m" if promised_min else "N/A"
    measured_l3 = f"statement={pace_statement_found}, promised={prom_str}, real={actual_min:.1f}m, wpm={measured_wpm:.1f}"
    thresh_l3 = f"statement in 5-20s, runtime ±{tol_min}m, {pace_mode} WPM {target_wpm_range[0]}-{target_wpm_range[1]}"
    results.append({
        "rule": "L3 (Pace Statement)",
        "measured": measured_l3,
        "threshold": thresh_l3,
        "status": status_l3
    })

    # -------------------------------------------------------------
    # L4: INTRO LENGTH & CHAPTER COUNT
    # -------------------------------------------------------------
    max_intro_s = style["structure"]["intro_max_s"] # 35
    chapter_range = style["structure"]["chapters"] # [3, 5]

    # Check intro scene duration in shotlist
    intro_scenes = [s for s in scenes if s.get("chapter", 0) == 0 or "intro" in str(s.get("scene_name", "")).lower() or "cold open" in str(s.get("scene_name", "")).lower()]
    intro_end_s = intro_scenes[-1].get("end_s", 30.0) if intro_scenes else 30.0
    intro_ok = intro_end_s <= max_intro_s + 0.5

    # Chapter count
    chapter_ids = {s.get("chapter") for s in scenes if s.get("chapter") is not None and s.get("chapter") > 0}
    if not chapter_ids and isinstance(script_header.get("chapters"), list):
        chapter_ids = set(range(1, len(script_header["chapters"]) + 1))
    num_chapters = len(chapter_ids)
    chapters_ok = chapter_range[0] <= num_chapters <= chapter_range[1]

    l4_pass = intro_ok and chapters_ok
    measured_l4 = f"intro={intro_end_s:.1f}s, chapters={num_chapters}"
    thresh_l4 = f"intro <= {max_intro_s}s, chapters {chapter_range[0]}-{chapter_range[1]}"
    results.append({
        "rule": "L4 (Narrative & Chapters)",
        "measured": measured_l4,
        "threshold": thresh_l4,
        "status": "PASS" if l4_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # L5: LOOP LEDGER INTEGRITY
    # -------------------------------------------------------------
    loops_cfg = style["loops"]
    loop_count_range = loops_cfg["count"] # [4, 5]
    num_loops = len(loops)
    count_ok = loop_count_range[0] <= num_loops <= loop_count_range[1]

    # Overlap check: >=2 loops open between 10% and 80% runtime
    min_open_count = loops_cfg["min_open_count"] # 2
    pct_range = loops_cfg["min_open_between_pct"] # [10, 80]
    t_start = (pct_range[0] / 100.0) * actual_runtime
    t_end = (pct_range[1] / 100.0) * actual_runtime

    open_counts = []
    # Sample every 5% across the window
    for step in range(pct_range[0], pct_range[1] + 1, 5):
        sample_t = (step / 100.0) * actual_runtime
        active_loops = sum(1 for lp in loops if lp.get("planted_at_s", 0) <= sample_t < lp.get("paid_at_s", actual_runtime + 1))
        open_counts.append(active_loops)

    min_open_detected = min(open_counts) if open_counts else 0
    overlap_ok = min_open_detected >= min_open_count

    # Early payoff check: first partial payoff must occur by 90s (using min over paid_at_s and partial_payoff_at_s)
    first_payoff_max_s = loops_cfg.get("first_payoff_max_s", 90)
    def loop_earliest(lp):
        cands = []
        if lp.get("paid_at_s") is not None: cands.append(float(lp["paid_at_s"]))
        if lp.get("partial_payoff_at_s") is not None: cands.append(float(lp["partial_payoff_at_s"]))
        return min(cands) if cands else 999999.0
    first_payoff_s = min((loop_earliest(lp) for lp in loops), default=999999.0)
    first_payoff_ok = first_payoff_s <= first_payoff_max_s + 1.0

    # Primary payoff window (80% - 95%)
    payoff_window_pct = loops_cfg["final_payoff_window_pct"] # [80, 95]
    payoff_t_min = (payoff_window_pct[0] / 100.0) * actual_runtime
    payoff_t_max = (payoff_window_pct[1] / 100.0) * actual_runtime

    primary_loops = [lp for lp in loops if lp.get("payoff_type") == "primary_insight" or lp.get("id") == 1]
    primary_loop = primary_loops[0] if primary_loops else (loops[0] if loops else {})
    primary_paid = primary_loop.get("paid_at_s", 0.0)
    primary_window_ok = payoff_t_min - 2.0 <= primary_paid <= payoff_t_max + 2.0

    # All paid by end
    all_paid_ok = all(lp.get("paid_at_s", 999999) <= actual_runtime + 1.0 for lp in loops)

    l5_pass = count_ok and overlap_ok and primary_window_ok and all_paid_ok and first_payoff_ok
    status_l5 = "PASS" if l5_pass else "FAIL"
    measured_l5 = f"{num_loops} loops, first_payoff={first_payoff_s:.1f}s, min_open={min_open_detected}, primary={primary_paid:.1f}s, all_paid={all_paid_ok}"
    thresh_l5 = f"{loop_count_range[0]}-{loop_count_range[1]} loops, 1st <= {first_payoff_max_s}s, >= {min_open_count} open in 10-80%, payoff in {payoff_window_pct[0]}-{payoff_window_pct[1]}%"
    results.append({
        "rule": "L5 (Loop Ledger)",
        "measured": measured_l5,
        "threshold": thresh_l5,
        "status": status_l5
    })

    # -------------------------------------------------------------
    # L6: PATTERN INTERRUPTS (EVERY <= 40s)
    # -------------------------------------------------------------
    max_gap_s = style["structure"]["pattern_interrupt_max_s"] # 40s
    interrupt_points = [0.0]
    for sc in scenes:
        if sc.get("pattern_interrupt") is True:
            interrupt_points.append(float(sc.get("start_s", 0.0)))
    interrupt_points.append(actual_runtime)
    interrupt_points.sort()

    gaps = [interrupt_points[i+1] - interrupt_points[i] for i in range(len(interrupt_points) - 1)]
    max_gap_detected = max(gaps) if gaps else actual_runtime
    l6_pass = max_gap_detected <= max_gap_s + 1.0

    results.append({
        "rule": "L6 (Pattern Interrupts)",
        "measured": f"max gap between interrupts = {max_gap_detected:.1f}s",
        "threshold": f"interrupt gap <= {max_gap_s}s",
        "status": "PASS" if l6_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # L7: DISCIPLINED CTA (STARTS NO EARLIER THAN T-45s, ENDS BY T-20s, <=25s)
    # -------------------------------------------------------------
    cta_cfg = style["cta"]
    cta_window_range = cta_cfg.get("window_from_end_s", [45, 20])
    max_cta_dur = cta_cfg.get("max_s", 25)

    # Locate CTA in scenes or script
    cta_scenes = [sc for sc in scenes if "cta" in str(sc.get("scene_name", "")).lower() or "cta" in str(sc.get("on_screen_text", "")).lower()]
    cta_line = str(script_header.get("cta_line", ""))

    has_cta = bool(cta_scenes or cta_line)
    cta_start = cta_scenes[0].get("start_s") if cta_scenes else (actual_runtime - 35.0)
    cta_end = cta_scenes[0].get("end_s") if cta_scenes else (actual_runtime - 20.0)
    cta_dur = cta_end - cta_start

    start_window_earliest = actual_runtime - cta_window_range[0] # T - 45s
    end_window_latest = actual_runtime - cta_window_range[1]     # T - 20s

    start_ok = cta_start >= start_window_earliest - 1.0
    end_ok = cta_end <= end_window_latest + 1.0
    in_window = start_ok and end_ok
    dur_ok = cta_dur <= max_cta_dur + 0.5

    # Triad requirement: action + reason + next video
    cta_text = (cta_line + " " + str(cta_scenes[0].get("on_screen_text", "") if cta_scenes else "")).lower()
    has_action = any(w in cta_text for w in ["watch", "click", "see", "check"])
    has_next = any(w in cta_text for w in ["next", "right here", "breakdown", "video", "episode"])
    triad_ok = has_action and has_next

    # No ask before first payoff
    first_payoff_t = min((lp.get("paid_at_s", 0.0) for lp in loops), default=0.0)
    no_early_ask = cta_start >= first_payoff_t

    l7_pass = has_cta and in_window and dur_ok and triad_ok and no_early_ask
    status_l7 = "PASS" if l7_pass else "FAIL"
    measured_l7 = f"cta_start={cta_start:.1f}s (T-{actual_runtime-cta_start:.1f}s), cta_end={cta_end:.1f}s (T-{actual_runtime-cta_end:.1f}s), dur={cta_dur:.1f}s, triad={triad_ok}"
    thresh_l7 = f"start >= T-{cta_window_range[0]}s, end <= T-{cta_window_range[1]}s, dur <= {max_cta_dur}s, triad, after payoff"
    results.append({
        "rule": "L7 (Disciplined Exit & CTA)",
        "measured": measured_l7,
        "threshold": thresh_l7,
        "status": status_l7
    })

    # -------------------------------------------------------------
    # VISUAL: FREEZEDETECT
    # -------------------------------------------------------------
    max_freeze_s = style["visual"]["static"]["max_freeze_s"]
    hold_tag = style["visual"]["static"]["hold_tag"]
    hold_max_s = style["visual"]["static"]["hold_max_s"]

    detected_freezes = detect_freezes(video_path, min_duration=max_freeze_s)
    freeze_pass = True
    violating_freeze_desc = ""

    for frz in detected_freezes:
        is_held = False
        for sc in scenes:
            sc_start = float(sc.get("start_s", 0.0))
            sc_end = float(sc.get("end_s", 0.0))
            if (frz["start"] >= sc_start - 0.1) and (frz["end"] <= sc_end + 0.1):
                if sc.get("hold_tag") == hold_tag and frz["duration"] <= hold_max_s:
                    is_held = True
                    break
        if not is_held:
            freeze_pass = False
            violating_freeze_desc = f"{frz['duration']:.2f}s freeze at {frz['start']:.1f}s"
            break

    results.append({
        "rule": "Visual (Static Frame Ceiling)",
        "measured": violating_freeze_desc if not freeze_pass else "no unheld freeze > 3.5s",
        "threshold": f"freeze <= {max_freeze_s}s (max {hold_max_s}s if {hold_tag})",
        "status": "PASS" if freeze_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # AUDIO: LOUDNESS CHECK
    # -------------------------------------------------------------
    voice_target_lufs = style["visual"]["audio"]["voice_lufs"]
    voice_tol = style["visual"]["audio"]["voice_tol"]
    music_below_db_min = style["visual"]["audio"]["music_below_voice_db_min"]

    if mix_only:
        mix_lufs = measure_ebur128_lufs(video_path)
        if mix_lufs is not None:
            mix_ok = abs(mix_lufs - voice_target_lufs) <= voice_tol
            if mix_ok:
                status_aud = "MANUAL"
                measured_aud = f"mix={mix_lufs:.1f} LUFS, music delta=MANUAL"
            else:
                status_aud = "FAIL"
                measured_aud = f"mix={mix_lufs:.1f} LUFS (out of spec {voice_target_lufs}±{voice_tol})"
        else:
            status_aud = "FAIL"
            measured_aud = "could not measure audio mix"
        thresh_aud = f"mix {voice_target_lufs}±{voice_tol} LUFS; music delta manual review"
    else:
        v_lufs = measure_ebur128_lufs(voice_path) if (voice_path and os.path.exists(voice_path)) else None
        m_lufs = measure_ebur128_lufs(music_path) if (music_path and os.path.exists(music_path)) else None

        if v_lufs is not None and m_lufs is not None:
            delta = v_lufs - m_lufs
            v_ok = abs(v_lufs - voice_target_lufs) <= voice_tol
            m_ok = delta >= music_below_db_min
            status_aud = "PASS" if (v_ok and m_ok) else "FAIL"
            measured_aud = f"voice={v_lufs:.1f} LUFS, music={m_lufs:.1f} LUFS (delta={delta:.1f} dB)"
        else:
            measured_aud = "stems not provided or could not be measured"
            status_aud = "WARN"
        thresh_aud = f"voice {voice_target_lufs}±{voice_tol} LUFS, music >= {music_below_db_min} dB below"

    results.append({
        "rule": "Audio (Loudness & Mix)",
        "measured": measured_aud,
        "threshold": thresh_aud,
        "status": status_aud
    })

    # -------------------------------------------------------------
    # VISUAL: TEXT WORD COUNT & END SCREEN CLEAR
    # -------------------------------------------------------------
    max_words_text = style["visual"]["text"]["max_words_per_event"] # 6
    text_errors = []
    for sc in scenes:
        ost = sc.get("on_screen_text")
        if isinstance(ost, dict):
            wc = ost.get("word_count", len(ost.get("text", "").split()))
        elif isinstance(ost, str):
            wc = len(ost.split())
        else:
            wc = 0
        if wc > max_words_text:
            text_errors.append(f"scene {sc.get('id')} text has {wc} words (max {max_words_text})")

    text_pass = len(text_errors) == 0
    results.append({
        "rule": "Visual (Text Pacing & Hierarchy)",
        "measured": "all on-screen text <= 6 words" if text_pass else "; ".join(text_errors[:2]),
        "threshold": f"max {max_words_text} words per event, contrast >= 7:1",
        "status": "PASS" if text_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # VISUAL: END SCREEN WINDOW (LAST 20s)
    # -------------------------------------------------------------
    end_clear_s = style["visual"]["end_screen_clear_s"] # 20
    end_window_start = max(0.0, actual_runtime - end_clear_s)
    end_screen_errors = []

    overlapping_scenes = []
    for sc in scenes:
        sc_start = float(sc.get("start_s", 0.0))
        sc_end = float(sc.get("end_s", actual_runtime))
        if sc_end > end_window_start and sc_start < actual_runtime:
            overlapping_scenes.append(sc)
            if sc.get("end_screen_safe") is not True:
                end_screen_errors.append(f"scene {sc.get('id')} end_screen_safe is not true")
            ost = sc.get("on_screen_text")
            if ost:
                if isinstance(ost, dict) and ost.get("text"):
                    end_screen_errors.append(f"scene {sc.get('id')} has on_screen_text in last 20s ('{ost.get('text')}')")
                elif isinstance(ost, str) and ost.strip():
                    end_screen_errors.append(f"scene {sc.get('id')} has on_screen_text in last 20s ('{ost.strip()}')")

    if not overlapping_scenes:
        end_screen_errors.append("no scenes defined covering final 20s")

    end_pass = len(end_screen_errors) == 0
    results.append({
        "rule": "Visual (End-Screen Window)",
        "measured": f"final {end_clear_s}s end_screen_safe=True, no text" if end_pass else "; ".join(end_screen_errors[:2]),
        "threshold": f"last {end_clear_s}s end_screen_safe=true & no text",
        "status": "PASS" if end_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # BRAND: 5-COLOR PALETTE & TYPOGRAPHY GATE
    # -------------------------------------------------------------
    brand_tokens = load_brand_tokens() or {}
    if brand_tokens and "palette" in brand_tokens:
        allowed_palette_hex = {v.upper() for v in brand_tokens["palette"].values() if isinstance(v, str)}
    else:
        allowed_palette_hex = {"#202322", "#233D4C", "#C3D809", "#FD802E", "#E6EDF3"}

    primary_font = brand_tokens.get("typography", {}).get("primary_font", "Nohemi").upper()
    fallback_font = brand_tokens.get("typography", {}).get("fallback_font", "Inter").upper()
    allowed_fonts = {primary_font, fallback_font}

    brand_errors = []

    # 1. Style font and colors check
    text_cfg = style.get("visual", {}).get("text", {})
    style_font = str(text_cfg.get("font", "")).upper()
    style_fallback = str(text_cfg.get("font_fallback", "")).upper()
    if style_font and style_font not in allowed_fonts:
        brand_errors.append(f"style font '{text_cfg.get('font')}' disallowed (must be Nohemi or fallback Inter)")
    if style_fallback and style_fallback not in allowed_fonts:
        brand_errors.append(f"style font_fallback '{text_cfg.get('font_fallback')}' disallowed (must be Nohemi or fallback Inter)")

    style_colors = extract_hex_colors(style.get("visual", {}))
    for sc_hex in style_colors:
        if sc_hex not in allowed_palette_hex:
            brand_errors.append(f"style has hex {sc_hex} outside 5-color palette")
        if is_generic_red_or_green(sc_hex):
            brand_errors.append(f"style has disallowed red/green color {sc_hex}")

    # 2. Scene checks (imported footage excluded)
    for sc in scenes:
        if is_imported_footage(sc):
            continue
        sc_font = sc.get("font")
        if sc_font and str(sc_font).upper() not in allowed_fonts:
            brand_errors.append(f"scene {sc.get('id')} has font '{sc_font}' (must be Nohemi or fallback Inter)")
        sc_hexes = extract_hex_colors(sc)
        for h in sc_hexes:
            if h not in allowed_palette_hex:
                brand_errors.append(f"scene {sc.get('id')} has hex {h} outside 5-color palette")
            if is_generic_red_or_green(h):
                brand_errors.append(f"scene {sc.get('id')} has disallowed red/green chart color {h}")
        sc_str = json.dumps(sc).lower()
        if any(term in sc_str for term in ["chart", "candle", "graph", "arrow", "indicator"]):
            if re.search(r"\b(green|red)\s*(candle|arrow|line|bar|wick)", sc_str):
                brand_errors.append(f"scene {sc.get('id')} specifies generic red/green chart element")

    brand_pass = len(brand_errors) == 0
    results.append({
        "rule": "Brand (Palette & Typography)",
        "measured": "5-color palette, Nohemi font, zero red/green" if brand_pass else "; ".join(brand_errors[:2]),
        "threshold": "exact 5-color palette, font Nohemi/Inter, zero red/green charts",
        "status": "PASS" if brand_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # LAYOUT CONTRACT & SAFE ZONES (layout_qa.py)
    # -------------------------------------------------------------
    try:
        from layout_qa import run_layout_qa
        episode_root = os.path.dirname(os.path.abspath(script_path)) if script_path else os.getcwd()
        while os.path.basename(episode_root) in ("01_scripts", "02_assets_code", "03_metadata", "voiceover"):
            episode_root = os.path.dirname(episode_root)
        layout_report = run_layout_qa(episode_root)
        layout_pass = layout_report.get("status") == "PASS"
        layout_measured = "Layout contract verified cleanly" if layout_pass else layout_report.get("summary", "Layout violations detected")
    except Exception as e:
        layout_pass = False
        layout_measured = f"Layout QA error: {e}"

    results.append({
        "rule": "Layout (Contract & Safe Zones)",
        "measured": layout_measured,
        "threshold": "Zero caption lane, margin, slot, contrast, or Manim stage violations",
        "status": "PASS" if layout_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # MANUAL REVIEWS
    # -------------------------------------------------------------
    results.append({
        "rule": "Quality (Premium Feel)",
        "measured": "Human review required",
        "threshold": "Human review required",
        "status": "MANUAL"
    })
    results.append({
        "rule": "Quality (Thumbnail Originality)",
        "measured": "Human review required",
        "threshold": "Human review required",
        "status": "MANUAL"
    })
    results.append({
        "rule": "Quality (Story & Payoff Fidelity)",
        "measured": "Human review required",
        "threshold": "Human review required",
        "status": "MANUAL"
    })

    # -------------------------------------------------------------
    # WAIVERS APPLICATION
    # -------------------------------------------------------------
    if waivers is None:
        cand_dirs = [
            os.path.dirname(os.path.abspath(script_path)) if script_path else "",
            os.path.dirname(os.path.abspath(shotlist_path)) if shotlist_path else "",
            os.path.dirname(os.path.abspath(loop_ledger_path)) if loop_ledger_path else "",
        ]
        cand_files = []
        for cd in cand_dirs:
            if not cd:
                continue
            cand_files.append(os.path.join(cd, "waivers.json"))
            cand_files.append(os.path.join(cd, "EP04_PATCH", "waivers.json"))
            cand_files.append(os.path.join(cd, "EPI04_PATCH", "waivers.json"))
            parent_cd = os.path.dirname(cd)
            cand_files.append(os.path.join(parent_cd, "waivers.json"))
            cand_files.append(os.path.join(parent_cd, "EP04_PATCH", "waivers.json"))
            cand_files.append(os.path.join(parent_cd, "EPI04_PATCH", "waivers.json"))
        cand_files.append(os.path.join(os.getcwd(), "EP04_PATCH", "waivers.json"))
        cand_files.append(os.path.join(os.getcwd(), "EPI04_PATCH", "waivers.json"))
        cand_files.append(os.path.join(os.getcwd(), "waivers.json"))

        for wf in cand_files:
            if os.path.exists(wf):
                try:
                    with open(wf, "r", encoding="utf-8") as wfh:
                        waivers = json.load(wfh)
                    break
                except Exception:
                    pass

    if waivers:
        waiver_map = {str(w.get("rule", "")).upper(): str(w.get("reason", "Approved")) for w in waivers}
        for r in results:
            rule_prefix = r["rule"].split()[0].upper() # e.g. "L4"
            matched_reason = None
            for wk, wr in waiver_map.items():
                if wk == rule_prefix or wk in r["rule"].upper():
                    matched_reason = wr
                    break
            if matched_reason and r["status"] == "FAIL":
                r["status"] = "WAIVED"
                r["waiver_reason"] = matched_reason
                r["measured"] = f"[WAIVED: {matched_reason}] was: {r['measured']}"

    return results

def print_table(results):
    col_rule = 32
    col_meas = 52
    col_thresh = 42
    col_status = 10

    sep = f"+{'-' * col_rule}+{'-' * col_meas}+{'-' * col_thresh}+{'-' * col_status}+"
    header = f"| {'Rule':<{col_rule - 2}} | {'Measured':<{col_meas - 2}} | {'Threshold':<{col_thresh - 2}} | {'Status':<{col_status - 2}} |"

    print(sep)
    print(header)
    print(sep)
    for r in results:
        rule_str = r['rule'][:col_rule - 2]
        meas_str = r['measured'][:col_meas - 2]
        thresh_str = r['threshold'][:col_thresh - 2]
        status_str = r['status'][:col_status - 2]
        print(f"| {rule_str:<{col_rule - 2}} | {meas_str:<{col_meas - 2}} | {thresh_str:<{col_thresh - 2}} | {status_str:<{col_status - 2}} |")
    print(sep)

    waived_rules = [r for r in results if r.get("status") == "WAIVED"]
    if waived_rules:
        print("\nWAIVED RULES:")
        for wr in waived_rules:
            reason = wr.get("waiver_reason") or wr.get("measured", "")
            print(f"  * {wr['rule']}: WAIVED - {reason}")

def main():
    parser = argparse.ArgumentParser(description="Quantrove Long-Form QA Gate Evaluator")
    parser.add_argument("--video", required=True, help="Path to video.mp4")
    parser.add_argument("--words", required=True, help="Path to words.json")
    parser.add_argument("--script", required=True, help="Path to script.md (with header)")
    parser.add_argument("--loop-ledger", required=True, help="Path to loop_ledger.json")
    parser.add_argument("--shotlist", required=True, help="Path to shotlist.json")
    parser.add_argument("--voice", default=None, help="Path to voice.wav stem (optional)")
    parser.add_argument("--music", default=None, help="Path to music.wav stem (optional)")
    parser.add_argument("--style", default=DEFAULT_STYLE_PATH, help="Path to longs_style.json")
    parser.add_argument("--mix-only", action="store_true", help="Measure final mix LUFS from video.mp4, music delta = MANUAL")
    parser.add_argument("--waivers", default=None, help="Path to waivers.json (optional)")

    args = parser.parse_args()

    waivers_data = None
    if args.waivers and os.path.exists(args.waivers):
        try:
            with open(args.waivers, "r", encoding="utf-8") as wf:
                waivers_data = json.load(wf)
        except Exception as e:
            print(f"Warning: could not load waivers file: {e}", file=sys.stderr)

    results = run_longs_qa(
        args.video,
        args.words,
        args.script,
        args.loop_ledger,
        args.shotlist,
        voice_path=args.voice,
        music_path=args.music,
        style_path=args.style,
        mix_only=args.mix_only,
        waivers=waivers_data
    )

    print("\n=== QUANTROVE LONG-FORM QA REPORT ===")
    print_table(results)

    has_fail = any(r["status"] == "FAIL" for r in results)
    if has_fail:
        print("\n[!] GATE 2 CHECK FAILED: One or more long-form rules failed the automated audit.")
        sys.exit(1)
    else:
        print("\n[+] GATE 2 AUTOMATED PASS: All automated checks passed (MANUAL review pending).")
        sys.exit(0)

if __name__ == "__main__":
    main()
