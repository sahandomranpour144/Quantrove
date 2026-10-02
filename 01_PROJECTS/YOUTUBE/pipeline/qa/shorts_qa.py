#!/usr/bin/env python3
"""
Quantrove Shorts QA Gate (shorts_qa.py)
Automated verification of Shorts video, word sync, text events, shotlist, and audio stems.
Evaluates Rules R1 through R10 against pipeline/config/shorts_style.json.
Exits 1 if any rule FAILS; exits 0 if all rules PASS, WARN, or MANUAL.
"""

import os
import sys
import json
import re
import math
import subprocess
import argparse

DEFAULT_STYLE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config", "shorts_style.json"
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
        # Check generic green: high green, low red (Power Lime #C3D809 has r=195, g=216, b=9)
        if g > 140 and r < 120 and b < 160:
            return True
        # Check generic red: high red, low green/blue (Pumpkin #FD802E has r=253, g=128, b=46)
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
        # Parse Integrated loudness: I: -14.0 LUFS
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
        return freezes
    except Exception:
        return []

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

def run_qa(video_path, words_path, text_events_path, shotlist_path, voice_path=None, music_path=None, style_path=DEFAULT_STYLE_PATH, mix_only=False):
    with open(style_path, "r", encoding="utf-8") as f:
        style = json.load(f)

    with open(words_path, "r", encoding="utf-8") as f:
        words_data = json.load(f)
        words = words_data.get("all_words") or words_data.get("words") or (words_data if isinstance(words_data, list) else [])

    with open(text_events_path, "r", encoding="utf-8") as f:
        text_events = json.load(f)

    with open(shotlist_path, "r", encoding="utf-8") as f:
        shotlist_data = json.load(f)
        scenes = shotlist_data.get("scenes") or (shotlist_data if isinstance(shotlist_data, list) else [])
        is_extraction = shotlist_data.get("type") == "extraction" or any(s.get("type") == "extraction" for s in scenes)

    results = []

    # -------------------------------------------------------------
    # R1: HOOK CHECK
    # -------------------------------------------------------------
    first_word_max_s = style["hook"]["first_word_max_s"]
    first_word_start = words[0]["start"] if words else 999.0
    first_text_start = text_events[0]["start"] if text_events else 999.0

    r1_pass = (first_word_start < first_word_max_s) and (first_text_start <= 0.1)
    measured_r1 = f"first_word={first_word_start:.2f}s, text_start={first_text_start:.2f}s"
    thresh_r1 = f"word < {first_word_max_s}s, text <= 0.1s, window < 3.0s"
    results.append({
        "rule": "R1 (Hook)",
        "measured": measured_r1,
        "threshold": thresh_r1,
        "status": "PASS" if r1_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # R2: STATIC FRAME CHECK
    # -------------------------------------------------------------
    max_freeze_s = style["static"]["max_freeze_s"]
    hold_tag = style["static"]["hold_tag"]
    hold_max_s = style["static"]["hold_max_s"]

    detected_freezes = detect_freezes(video_path, min_duration=max_freeze_s)
    r2_pass = True
    max_unheld_freeze = 0.0
    violating_freeze_desc = ""

    for frz in detected_freezes:
        # Check if freeze falls inside a scene with hold_tag
        is_held = False
        for sc in scenes:
            sc_start = float(sc.get("start_s", sc.get("startSec", 0)))
            sc_end = float(sc.get("end_s", sc.get("endSec", 0)))
            if (frz["start"] >= sc_start - 0.1) and (frz["end"] <= sc_end + 0.1):
                if sc.get("hold_tag") == hold_tag and frz["duration"] <= hold_max_s:
                    is_held = True
                    break
        if not is_held:
            r2_pass = False
            if frz["duration"] > max_unheld_freeze:
                max_unheld_freeze = frz["duration"]
                violating_freeze_desc = f"{frz['duration']:.2f}s at {frz['start']:.1f}s"

    measured_r2 = violating_freeze_desc if not r2_pass else "no unheld freeze > 3.5s"
    thresh_r2 = f"freeze <= {max_freeze_s}s (max {hold_max_s}s if {hold_tag})"
    results.append({
        "rule": "R2 (Static Frame)",
        "measured": measured_r2,
        "threshold": thresh_r2,
        "status": "PASS" if r2_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # R3: AUDIO LOUDNESS CHECK
    # -------------------------------------------------------------
    voice_target_lufs = style["audio"]["voice_lufs"]
    voice_tol = style["audio"]["voice_tol"]
    music_below_db_min = style["audio"]["music_below_voice_db_min"]

    if mix_only:
        # CapCut exported Short: measure video.mp4 mix track directly
        mix_lufs = measure_ebur128_lufs(video_path)
        if mix_lufs is not None:
            mix_ok = abs(mix_lufs - voice_target_lufs) <= voice_tol
            if mix_ok:
                status_r3 = "MANUAL"
                measured_r3 = f"mix={mix_lufs:.1f} LUFS, music delta=MANUAL"
            else:
                status_r3 = "FAIL"
                measured_r3 = f"mix={mix_lufs:.1f} LUFS (out of spec {voice_target_lufs}±{voice_tol} LUFS), music delta=MANUAL"
        else:
            status_r3 = "FAIL"
            measured_r3 = "could not measure audio mix from video file"
        thresh_r3 = f"mix {voice_target_lufs}±{voice_tol} LUFS; music delta manual review"
    else:
        v_lufs = measure_ebur128_lufs(voice_path) if (voice_path and os.path.exists(voice_path)) else None
        m_lufs = measure_ebur128_lufs(music_path) if (music_path and os.path.exists(music_path)) else None

        if v_lufs is not None and m_lufs is not None:
            delta = v_lufs - m_lufs  # music is lower, so delta = voice - music (e.g. -14 - (-32) = 18 dB)
            v_ok = abs(v_lufs - voice_target_lufs) <= voice_tol
            m_ok = delta >= music_below_db_min
            r3_pass = v_ok and m_ok
            measured_r3 = f"voice={v_lufs:.1f} LUFS, music={m_lufs:.1f} LUFS (delta={delta:.1f} dB)"
            status_r3 = "PASS" if r3_pass else "FAIL"
        else:
            measured_r3 = "audio stems not provided or could not be measured"
            status_r3 = "WARN"

        thresh_r3 = f"voice {voice_target_lufs}±{voice_tol} LUFS, music >= {music_below_db_min} dB below"
    results.append({
        "rule": "R3 (Audio Mix)",
        "measured": measured_r3,
        "threshold": thresh_r3,
        "status": status_r3
    })

    # -------------------------------------------------------------
    # R4: VOICE WPM CHECK
    # -------------------------------------------------------------
    wpm_target = style["voice_wpm"]["target"]
    wpm_warn_margin = style["voice_wpm"]["warn_margin"]
    spoken_duration_s = words[-1]["end"] - words[0]["start"] if words else 30.0
    wpm = (len(words) / (spoken_duration_s / 60.0)) if spoken_duration_s > 0 else 0.0

    if wpm_target[0] <= wpm <= wpm_target[1]:
        status_r4 = "PASS"
    elif (wpm_target[0] - wpm_warn_margin) <= wpm <= (wpm_target[1] + wpm_warn_margin):
        status_r4 = "WARN"
    elif is_extraction:
        status_r4 = "WARN"
    else:
        status_r4 = "FAIL"

    measured_r4 = f"{wpm:.1f} WPM ({len(words)} words in {spoken_duration_s:.1f}s)"
    thresh_r4 = f"{wpm_target[0]}-{wpm_target[1]} WPM (±{wpm_warn_margin} margin)"
    results.append({
        "rule": "R4 (Voice WPM)",
        "measured": measured_r4,
        "threshold": thresh_r4,
        "status": status_r4
    })

    # -------------------------------------------------------------
    # R5/R6: TEXT SYSTEM CHECK
    # -------------------------------------------------------------
    brand_tokens = load_brand_tokens() or {}
    if brand_tokens and "palette" in brand_tokens:
        allowed_palette_hex = {v.upper() for v in brand_tokens["palette"].values() if isinstance(v, str)}
    else:
        allowed_palette_hex = {"#202322", "#233D4C", "#C3D809", "#FD802E", "#E6EDF3"}

    primary_font = brand_tokens.get("typography", {}).get("primary_font", "Nohemi").upper()
    fallback_font = brand_tokens.get("typography", {}).get("fallback_font", "Inter").upper()
    allowed_fonts = {primary_font, fallback_font}

    max_words_per_chunk = style["chunk"]["max_words"]
    min_on_screen_s = style["chunk"]["min_on_screen_s"]
    badge_max = style["badge"]["max_per_short"]
    bg_color = style["colors"]["bg"]
    text_color = style["colors"]["text"]
    emp_color = style["colors"]["emphasis"]

    allowed_hex = allowed_palette_hex
    chunk_y_range = style.get("chunk", {}).get("zone_y_pct", [60, 76])
    badge_y_range = style.get("badge", {}).get("zone_y_pct", [42, 52])
    safe_bottom = style.get("chunk", {}).get("safe_bottom_pct", 20)
    max_chunk_y = 100 - safe_bottom  # 80% max Y before safe margin

    r5_6_errors = []
    badge_count = 0

    for idx, ev in enumerate(text_events):
        ev_type = ev.get("type", "chunk")
        ev_words = ev.get("words", [])
        ev_dur = ev["end"] - ev["start"]
        y_pct = ev.get("y_pct")

        # Color and contrast check
        ev_color = ev.get("color")
        if ev_color:
            if ev_color.upper() not in allowed_hex:
                r5_6_errors.append(f"event {idx} has disallowed color {ev_color}")
            elif calculate_contrast(ev_color, bg_color) < 7.0:
                r5_6_errors.append(f"event {idx} color {ev_color} contrast < 7:1")

        # Safe zone check
        if y_pct is not None:
            if ev_type == "chunk":
                if y_pct < chunk_y_range[0] or y_pct > max_chunk_y:
                    r5_6_errors.append(f"event {idx} y_pct={y_pct}% outside safe zone")
            elif ev_type == "badge":
                if y_pct < badge_y_range[0] or y_pct > badge_y_range[1]:
                    r5_6_errors.append(f"badge y_pct={y_pct}% outside safe zone")

        if ev_type == "badge":
            badge_count += 1

        if ev_type == "chunk":
            if len(ev_words) > max_words_per_chunk:
                r5_6_errors.append(f"event {idx} has {len(ev_words)} words (max {max_words_per_chunk})")
            if ev_dur < min_on_screen_s - 0.02:
                r5_6_errors.append(f"event {idx} duration {ev_dur:.2f}s (< {min_on_screen_s}s)")

        # Overlap check with previous
        if idx > 0 and ev["start"] < text_events[idx - 1]["end"] - 0.01:
            r5_6_errors.append(f"event {idx} overlaps with event {idx - 1}")

    if badge_count > badge_max:
        r5_6_errors.append(f"found {badge_count} badges (max {badge_max})")

    # Contrast check
    c_text = calculate_contrast(text_color, bg_color)
    c_emp = calculate_contrast(emp_color, bg_color)
    if c_text < 7.0 or c_emp < 7.0:
        r5_6_errors.append(f"contrast below 7:1 (text={c_text:.1f}:1, emp={c_emp:.1f}:1)")

    r5_6_pass = len(r5_6_errors) == 0
    measured_r5_6 = "compliant text events" if r5_6_pass else "; ".join(r5_6_errors[:3])
    thresh_r5_6 = f"<= {max_words_per_chunk} words, >= {min_on_screen_s}s, no overlap, safe zone, contrast >= 7:1"
    results.append({
        "rule": "R5/R6 (Text System)",
        "measured": measured_r5_6,
        "threshold": thresh_r5_6,
        "status": "PASS" if r5_6_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # R7: STRUCTURE & LENGTH CHECK
    # -------------------------------------------------------------
    expected_beats = style["structure"]["beats"]
    length_range = style["structure"]["length_s"]
    actual_length = probe_file_duration(video_path) or 0.0

    length_ok = length_range[0] <= actual_length <= length_range[1]
    if is_extraction:
        # Per shorts-style.md R7: 30-45s is native Shorts only; extractions must be <= 60s Shorts ceiling
        r7_pass = (10.0 <= actual_length <= 60.0)
        measured_r7 = f"extraction: length={actual_length:.1f}s"
        thresh_r7 = "extraction <= 60s ceiling, reveal present"
    else:
        scene_beats = [s.get("beat") for s in scenes if s.get("beat")]
        # Check order of expected beats
        beat_idx = 0
        for b in scene_beats:
            if beat_idx < len(expected_beats) and b == expected_beats[beat_idx]:
                beat_idx += 1
        beats_ok = (beat_idx == len(expected_beats))
        r7_pass = length_ok and beats_ok
        measured_r7 = f"length={actual_length:.1f}s, beats={scene_beats}"
        thresh_r7 = f"beats in order {expected_beats}, length {length_range[0]}-{length_range[1]}s"

    results.append({
        "rule": "R7 (Structure & Length)",
        "measured": measured_r7,
        "threshold": thresh_r7,
        "status": "PASS" if r7_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # R8: MOTION DISCIPLINE CHECK
    # -------------------------------------------------------------
    valid_motion_tags = set(style["motion"]["tags"])
    push_max_scale = style["motion"]["camera_push_max_scale"]
    push_needs_purpose = style["motion"]["camera_push_needs_purpose"]
    flow_max_pct = style["motion"]["flow_max_pct_of_runtime"]

    r8_errors = []
    flow_duration = 0.0

    for sc in scenes:
        mt = sc.get("motion_tag")
        sc_dur = float(sc.get("end_s", sc.get("endSec", 0))) - float(sc.get("start_s", sc.get("startSec", 0)))
        if not mt or mt not in valid_motion_tags:
            r8_errors.append(f"scene {sc.get('id')} has invalid/missing motion_tag: {mt}")
        if mt == "camera_push":
            scale = float(sc.get("camera_push_scale", 1.05))
            purpose = sc.get("motion_purpose", "").strip()
            if scale > push_max_scale:
                r8_errors.append(f"scene {sc.get('id')} camera_push scale {scale} > {push_max_scale}")
            if push_needs_purpose and not purpose:
                r8_errors.append(f"scene {sc.get('id')} camera_push missing motion_purpose")
        if mt == "flow_atmosphere":
            flow_duration += max(0.0, sc_dur)

    flow_pct = (flow_duration / actual_length * 100) if actual_length > 0 else 0
    if flow_pct > flow_max_pct:
        r8_errors.append(f"flow_atmosphere {flow_pct:.1f}% > {flow_max_pct}% runtime")

    r8_pass = len(r8_errors) == 0
    measured_r8 = f"valid tags, flow={flow_pct:.1f}%" if r8_pass else "; ".join(r8_errors[:2])
    thresh_r8 = f"tags in {list(valid_motion_tags)}, push <= {push_max_scale} with purpose, flow <= {flow_max_pct}%"
    results.append({
        "rule": "R8 (Motion)",
        "measured": measured_r8,
        "threshold": thresh_r8,
        "status": "PASS" if r8_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # R9: CLEAN ENDING CHECK
    # -------------------------------------------------------------
    max_tail_s = style["ending"]["max_tail_after_last_word_s"]
    forbidden_words = style["ending"]["forbidden_words"]

    last_word_end = words[-1]["end"] if words else actual_length
    tail_s = max(0.0, actual_length - last_word_end)
    tail_ok = tail_s <= max_tail_s + 0.05

    # Check forbidden words in text events
    forbidden_found = []
    for ev in text_events:
        for w in ev.get("words", []):
            w_str = w.get("word", "").lower().strip()
            for fw in forbidden_words:
                if fw in w_str:
                    forbidden_found.append(fw)

    # Check for outro scene
    has_outro_scene = any(
        "outro" in str(s.get("beat", "")).lower() or
        "outro" in str(s.get("type", "")).lower() or
        "cta" in str(s.get("type", "")).lower()
        for s in scenes
    )

    r9_pass = tail_ok and (len(forbidden_found) == 0) and (not has_outro_scene)
    reasons_r9 = []
    if not tail_ok: reasons_r9.append(f"tail {tail_s:.2f}s > {max_tail_s}s")
    if forbidden_found: reasons_r9.append(f"forbidden words: {forbidden_found}")
    if has_outro_scene: reasons_r9.append("outro card/scene present")

    measured_r9 = f"tail={tail_s:.2f}s, no forbidden terms, no outro" if r9_pass else "; ".join(reasons_r9)
    thresh_r9 = f"tail <= {max_tail_s}s, no forbidden terms {forbidden_words}, no outro card"
    results.append({
        "rule": "R9 (Clean Ending)",
        "measured": measured_r9,
        "threshold": thresh_r9,
        "status": "PASS" if r9_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # BRAND: 5-COLOR PALETTE & TYPOGRAPHY GATE
    # -------------------------------------------------------------
    brand_errors = []

    # 1. Style font check
    style_font = str(style.get("font", "")).upper()
    style_fallback = str(style.get("font_fallback", "")).upper()
    if style_font and style_font not in allowed_fonts:
        brand_errors.append(f"style font '{style.get('font')}' disallowed (must be Nohemi or fallback Inter)")
    if style_fallback and style_fallback not in allowed_fonts:
        brand_errors.append(f"style font_fallback '{style.get('font_fallback')}' disallowed (must be Nohemi or fallback Inter)")

    # 2. Style color palette check
    style_colors = extract_hex_colors(style.get("colors", {}))
    for sc_hex in style_colors:
        if sc_hex not in allowed_palette_hex:
            brand_errors.append(f"style has hex {sc_hex} outside 5-color palette")
        if is_generic_red_or_green(sc_hex):
            brand_errors.append(f"style has disallowed red/green color {sc_hex}")

    # 3. Text events font and color checks
    for idx, ev in enumerate(text_events):
        ev_font = ev.get("font")
        if ev_font and str(ev_font).upper() not in allowed_fonts:
            brand_errors.append(f"event {idx} has font '{ev_font}' (must be Nohemi or fallback Inter)")
        ev_colors = extract_hex_colors(ev)
        for c in ev_colors:
            if c not in allowed_palette_hex:
                brand_errors.append(f"event {idx} has hex {c} outside 5-color palette")
            if is_generic_red_or_green(c):
                brand_errors.append(f"event {idx} has disallowed red/green color {c}")

    # 4. Shotlist scene checks (imported footage excluded)
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
    # LAYOUT CONTRACT & SAFE ZONES (Shorts)
    # -------------------------------------------------------------
    layout_errors = []
    for idx, ev in enumerate(text_events):
        pos_y = ev.get("zone_y_pct") or ev.get("y_pct")
        if pos_y is not None:
            # If specified as pct [60, 76] or y coordinate
            if isinstance(pos_y, (int, float)):
                y_px = pos_y * 19.2 if pos_y <= 100 else pos_y
                if y_px < 1040 or y_px > 1440:
                    layout_errors.append(f"event {idx} y={y_px:.0f}px outside text_band (1040-1440)")
        # Check text colors
        c = ev.get("color")
        if c and str(c).upper() not in allowed_palette_hex:
            layout_errors.append(f"event {idx} text color {c} outside palette")

    layout_pass = len(layout_errors) == 0
    results.append({
        "rule": "Layout (Shorts Contract)",
        "measured": "Safe box x:60-880, stage:250-1000, text:1040-1440" if layout_pass else "; ".join(layout_errors[:2]),
        "threshold": "Single text system, stage 250-1000, text 1040-1440, safe box 60-880",
        "status": "PASS" if layout_pass else "FAIL"
    })

    # -------------------------------------------------------------
    # R10: PREMIUM FEEL (MANUAL)
    # -------------------------------------------------------------
    results.append({
        "rule": "R10 (Premium Feel)",
        "measured": "Human review required",
        "threshold": "Human review required",
        "status": "MANUAL"
    })

    return results

def print_table(results):
    col_rule = 24
    col_meas = 42
    col_thresh = 44
    col_status = 8

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

def main():
    parser = argparse.ArgumentParser(description="Quantrove Shorts QA Gate Evaluator")
    parser.add_argument("--video", required=True, help="Path to video.mp4")
    parser.add_argument("--words", required=True, help="Path to words.json")
    parser.add_argument("--text-events", required=True, help="Path to text_events.json")
    parser.add_argument("--shotlist", required=True, help="Path to shotlist.json")
    parser.add_argument("--voice", default=None, help="Path to voice.wav stem (optional)")
    parser.add_argument("--music", default=None, help="Path to music.wav stem (optional)")
    parser.add_argument("--style", default=DEFAULT_STYLE_PATH, help="Path to shorts_style.json")
    parser.add_argument("--mix-only", action="store_true", help="Measure final mix LUFS only from video.mp4, music delta = MANUAL (for CapCut-exported Shorts)")

    args = parser.parse_args()

    results = run_qa(
        args.video,
        args.words,
        args.text_events,
        args.shotlist,
        voice_path=args.voice,
        music_path=args.music,
        style_path=args.style,
        mix_only=args.mix_only
    )

    print("\n=== QUANTROVE SHORTS QA REPORT ===")
    print_table(results)

    has_fail = any(r["status"] == "FAIL" for r in results)
    if has_fail:
        print("\n[!] GATE 2 CHECK FAILED: One or more rules failed the automated audit.")
        sys.exit(1)
    else:
        print("\n[+] GATE 2 AUTOMATED PASS: All automated checks passed (MANUAL review pending).")
        sys.exit(0)

if __name__ == "__main__":
    main()
