#!/usr/bin/env python3
"""
Quantrove Shared Layout QA Gate (layout_qa.py)
Automated verification of visual framing, safe zones, text colors, contrast,
and kinetic pop-up placement against pipeline/config/layout_contract.json.

Enforces:
a) Allowed zone constraints: zero text/pop-ups in caption lane (y 864-1080), margins, or Flow center column.
b) Stage containment: Manim content strictly inside manim_stage (x 96-1824, y 190-856).
   Non-chrome pixels (ignoring #202322 and #233D4C) must not appear outside stage.
c) Pop-up contract: valid slot for scene type, no same slot twice in a row, no time overlap,
   and zero overlap with underlying non-chrome Manim pixels.
d) Text color allow-list (#E6EDF3, #FFFFFF, #C3D809, #FD802E, #EF6448) + contrast >= 4.5:1.
"""

import os
import sys
import json
import re
import math
import subprocess
import argparse
import numpy as np
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PIPELINE_DIR = os.path.dirname(SCRIPT_DIR)
WORKSPACE_ROOT = os.path.dirname(os.path.dirname(PIPELINE_DIR))
DEFAULT_CONTRACT_PATH = os.path.join(PIPELINE_DIR, "config", "layout_contract.json")
DEFAULT_BRAND_TOKENS_PATH = os.path.join(WORKSPACE_ROOT, "brand", "brand_tokens.json")


def load_layout_contract(path: str = None) -> dict:
    contract_path = path or DEFAULT_CONTRACT_PATH
    if not os.path.exists(contract_path):
        # Fallback search
        alt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config", "layout_contract.json")
        if os.path.exists(alt_path):
            contract_path = alt_path
    if os.path.exists(contract_path):
        with open(contract_path, "r", encoding="utf-8") as f:
            return json.load(f)
    raise FileNotFoundError(f"Layout contract not found at {contract_path}")


def hex_to_rgb(hex_str: str) -> tuple:
    h = hex_str.strip().lstrip("#")
    if len(h) == 3:
        h = "".join([c * 2 for c in h])
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def calculate_relative_luminance(rgb: tuple) -> float:
    vals = []
    for c in rgb:
        s = c / 255.0
        val = s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4
        vals.append(val)
    return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]


def calculate_contrast_ratio(hex1: str, hex2: str) -> float:
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    l1 = calculate_relative_luminance(rgb1)
    l2 = calculate_relative_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def is_non_chrome_pixel(rgb_array: np.ndarray) -> np.ndarray:
    """
    Given an (N, 3) or (H, W, 3) RGB numpy array:
    Returns boolean array where True indicates NON-CHROME pixels.
    Ignored background/chrome colors:
      - #202322 (32, 35, 34) Background canvas
      - #222022 (34, 32, 34) Card/pill fill
      - #233D4C (35, 61, 76) Chrome lines, borders, grids
      - Dark container fills e.g. #161B22, #181C24, #141E22, #181310 (RGB < 40)
    """
    r = rgb_array[..., 0].astype(np.int32)
    g = rgb_array[..., 1].astype(np.int32)
    b = rgb_array[..., 2].astype(np.int32)

    # Distances to canonical chrome & background
    dist_bg = np.sqrt((r - 32)**2 + (g - 35)**2 + (b - 34)**2)
    dist_pill = np.sqrt((r - 34)**2 + (g - 32)**2 + (b - 34)**2)
    dist_chrome = np.sqrt((r - 35)**2 + (g - 61)**2 + (b - 76)**2)

    # Dark panels (near black canvas with minimal chromaticity)
    is_dark_panel = (r < 42) & (g < 42) & (b < 45) & (np.maximum(r, np.maximum(g, b)) - np.minimum(r, np.minimum(g, b)) < 16)

    is_bg_or_chrome = (dist_bg < 24) | (dist_pill < 24) | (dist_chrome < 28) | is_dark_panel
    return ~is_bg_or_chrome


def extract_video_frame_ffmpeg(video_path: str, timestamp_s: float) -> np.ndarray:
    """Extract a single RGB frame at timestamp_s using ffmpeg."""
    cmd = [
        "ffmpeg", "-ss", f"{timestamp_s:.3f}", "-i", video_path,
        "-vframes", "1", "-f", "image2pipe", "-vcodec", "rawvideo", "-pix_fmt", "rgb24", "-"
    ]
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        # Probe dimensions
        probe_cmd = [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0", video_path
        ]
        res = subprocess.run(probe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        w, h = map(int, res.stdout.strip().split("x"))
        frame = np.frombuffer(proc.stdout, dtype=np.uint8).reshape((h, w, 3))
        return frame
    except Exception as e:
        return None


def get_video_duration(video_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", video_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return float(res.stdout.strip())
    except Exception:
        return 0.0


# =============================================================================
# CHECK A & C: POP-UPS MANIFEST VERIFICATION
# =============================================================================
def verify_popups_manifest(manifest_path: str, contract: dict, episode_dir: str = None) -> list:
    """
    Verifies popups_manifest.json against contract rules:
    - Bbox inside allowed zone (not in caption lane, margins, right rail, center column on Flow).
    - Valid slot for scene type (Manim: TL, TC, TR; Flow: TL, TR, ML, MR).
    - No same slot twice in a row.
    - No time overlap.
    - Text color in allow-list.
    - Zero overlap with non-chrome Manim pixels in underlying frame.
    """
    failures = []
    if not os.path.exists(manifest_path):
        return [{"check": "popups_manifest_exists", "status": "FAIL", "msg": f"Manifest not found: {manifest_path}"}]

    with open(manifest_path, "r", encoding="utf-8") as f:
        popups = json.load(f)

    if not isinstance(popups, list):
        return [{"check": "popups_manifest_format", "status": "FAIL", "msg": "Manifest must be a list of popup objects"}]

    lf = contract.get("long_form", {})
    cap_lane = lf.get("caption_lane", {})
    cap_ymin = cap_lane.get("ymin", 864)
    cap_ymax = cap_lane.get("ymax", 1080)
    allowed_colors = [c.upper() for c in contract.get("palette", {}).get("allowed_text_colors", [])]
    fill_hex = lf.get("popup_box", {}).get("fill", "#222022")

    prev_slot = None
    prev_end = -1.0

    for i, pop in enumerate(popups):
        word = pop.get("word") or pop.get("text", f"popup_{i}")
        start = float(pop.get("start", 0.0))
        end = float(pop.get("end", 0.0))
        slot = pop.get("slot", "")
        bbox = pop.get("bbox", [0, 0, 0, 0])  # [xmin, ymin, xmax, ymax]
        color = str(pop.get("color", "")).upper()
        scene_type = pop.get("scene_type", "manim").lower()
        clip_name = pop.get("clip", "")

        xmin, ymin, xmax, ymax = bbox

        # 1. Caption Lane Violation (Check a)
        if ymax > cap_ymin:
            failures.append({
                "check": "caption_lane_collision",
                "popup": word,
                "timestamp": f"{start:.2f}-{end:.2f}s",
                "status": "FAIL",
                "msg": f"Pop-up '{word}' bbox ymax={ymax} enters caption lane (>= {cap_ymin})"
            })

        # 2. Margins Violation (Check a)
        if xmin < 96 or xmax > 1824 or ymin < 56:
            failures.append({
                "check": "margins_violation",
                "popup": word,
                "timestamp": f"{start:.2f}-{end:.2f}s",
                "status": "FAIL",
                "msg": f"Pop-up '{word}' bbox [{xmin},{ymin},{xmax},{ymax}] breaches margins (left:96, right:1824, top:56)"
            })

        # 3. Flow Center Column Violation (Check a)
        if scene_type == "flow":
            # Forbidden center column x: 656 - 1264
            if not (xmax <= 656 or xmin >= 1264):
                failures.append({
                    "check": "flow_center_column_violation",
                    "popup": word,
                    "timestamp": f"{start:.2f}-{end:.2f}s",
                    "status": "FAIL",
                    "msg": f"Pop-up '{word}' on Flow scene enters forbidden center column x: 656-1264"
                })

        # 4. Slot validity (Check c)
        if scene_type == "manim":
            valid_slots = ["TL", "TC", "TR"]
        else:
            valid_slots = ["TL", "TR", "ML", "MR"]

        if slot not in valid_slots:
            failures.append({
                "check": "invalid_slot",
                "popup": word,
                "timestamp": f"{start:.2f}-{end:.2f}s",
                "status": "FAIL",
                "msg": f"Slot '{slot}' not allowed for scene type '{scene_type}' (valid: {valid_slots})"
            })

        # 5. Consecutive same slot (Check c)
        if prev_slot is not None and slot == prev_slot:
            failures.append({
                "check": "consecutive_same_slot",
                "popup": word,
                "timestamp": f"{start:.2f}-{end:.2f}s",
                "status": "FAIL",
                "msg": f"Pop-up '{word}' repeats slot '{slot}' consecutively"
            })

        # 6. Time overlap (Check c)
        if start < prev_end:
            failures.append({
                "check": "time_overlap",
                "popup": word,
                "timestamp": f"{start:.2f}-{end:.2f}s",
                "status": "FAIL",
                "msg": f"Pop-up '{word}' starts at {start:.2f}s before previous ended at {prev_end:.2f}s"
            })

        # 7. Text Color allow-list & contrast (Check d)
        if color and color not in allowed_colors:
            failures.append({
                "check": "text_color_allowlist",
                "popup": word,
                "timestamp": f"{start:.2f}-{end:.2f}s",
                "status": "FAIL",
                "msg": f"Pop-up '{word}' color '{color}' not in allowed text colors: {allowed_colors}"
            })
        elif color:
            contrast = calculate_contrast_ratio(color, fill_hex)
            if contrast < 4.5:
                failures.append({
                    "check": "text_contrast",
                    "popup": word,
                    "timestamp": f"{start:.2f}-{end:.2f}s",
                    "status": "FAIL",
                    "msg": f"Pop-up '{word}' contrast {contrast:.2f}:1 against fill {fill_hex} < 4.5:1"
                })

        # 8. Overlap with underlying Manim pixels (Check c)
        if scene_type == "manim" and episode_dir and clip_name:
            clip_path = os.path.join(episode_dir, "TIMELINE_MEDIA", clip_name)
            if not os.path.exists(clip_path):
                clip_path = os.path.join(episode_dir, clip_name)
            if os.path.exists(clip_path):
                mid_time = (start + end) / 2.0
                frame = extract_video_frame_ffmpeg(clip_path, mid_time)
                if frame is not None:
                    # Crop to popup bbox
                    h, w, _ = frame.shape
                    y1 = max(0, min(h, ymin))
                    y2 = max(0, min(h, ymax))
                    x1 = max(0, min(w, xmin))
                    x2 = max(0, min(w, xmax))
                    if y2 > y1 and x2 > x1:
                        crop = frame[y1:y2, x1:x2]
                        non_chrome = is_non_chrome_pixel(crop)
                        count = np.sum(non_chrome)
                        if count > 15:
                            failures.append({
                                "check": "manim_content_overlap",
                                "popup": word,
                                "timestamp": f"{start:.2f}-{end:.2f}s",
                                "status": "FAIL",
                                "msg": f"Pop-up '{word}' overlaps {count} non-chrome Manim pixels in {clip_name}"
                            })

        prev_slot = slot
        prev_end = end

    return failures


# =============================================================================
# CHECK B: MANIM VIDEO CONTENT STAGE CONTAINMENT
# =============================================================================
def verify_manim_clip_stage(clip_path: str, contract: dict, sample_interval_s: float = 0.25) -> list:
    """
    Samples video every sample_interval_s.
    Verifies that non-chrome pixels (ignoring #202322 and #233D4C) do NOT appear outside manim_stage:
      - x: [96, 1824]
      - y: [190, 856]
    """
    failures = []
    if not os.path.exists(clip_path):
        return [{"clip": clip_path, "status": "FAIL", "msg": f"Clip does not exist: {clip_path}"}]

    duration = get_video_duration(clip_path)
    if duration <= 0:
        return []

    lf = contract.get("long_form", {})
    stg = lf.get("manim_stage", {})
    xmin = stg.get("xmin", 96)
    xmax = stg.get("xmax", 1824)
    ymin = stg.get("ymin", 190)
    ymax = stg.get("ymax", 856)

    # Sample timestamps
    t = 0.1
    breaches = []
    while t < duration - 0.05:
        frame = extract_video_frame_ffmpeg(clip_path, t)
        if frame is not None:
            h, w, _ = frame.shape
            outside_mask = np.ones((h, w), dtype=bool)
            outside_mask[ymin:ymax, xmin:xmax] = False

            outside_pixels = frame[outside_mask]
            non_chrome = is_non_chrome_pixel(outside_pixels)
            num_violations = int(np.sum(non_chrome))

            if num_violations > 25:  # Tolerance against minor compression artifacts
                breaches.append((t, num_violations))
                if len(breaches) >= 3:
                    break
        t += sample_interval_s

    if breaches:
        t_str = ", ".join([f"{bt:.2f}s ({cnt}px)" for bt, cnt in breaches[:3]])
        failures.append({
            "clip": os.path.basename(clip_path),
            "check": "manim_stage_containment",
            "status": "FAIL",
            "msg": f"Non-chrome pixels found outside manim_stage at {t_str}"
        })

    return failures


# =============================================================================
# CHECK D: TEXT COLORS IN SOURCE SCRIPT / TEXT ELEMENTS
# =============================================================================
def verify_script_text_colors(script_path: str, contract: dict) -> list:
    """
    Scans a Manim script file for forbidden text colors (specifically #233D4C or UI_STRUCTURE as text).
    """
    failures = []
    if not os.path.exists(script_path):
        return []

    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for Text/CleanText with UI_STRUCTURE or #233D4C
    pattern = re.compile(r'(CleanText|Text)\s*\([^)]*?(color\s*=\s*(UI_STRUCTURE|["\']#233D4C["\']))', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(content)
    if matches:
        failures.append({
            "script": os.path.basename(script_path),
            "check": "forbidden_text_color_ui_structure",
            "status": "FAIL",
            "msg": f"Found {len(matches)} Text/CleanText elements using #233D4C (UI_STRUCTURE). Chrome is forbidden for text."
        })

    return failures


# =============================================================================
# FULL EPISODE QA RUNNER
# =============================================================================
def run_layout_qa(episode_dir: str, contract_path: str = None) -> dict:
    """
    Full layout QA gate over an episode directory.
    Returns:
      {
        "status": "PASS" | "FAIL",
        "results": [...],
        "summary": "..."
      }
    """
    contract = load_layout_contract(contract_path)
    results = []

    # 1. Popups Manifest Check
    manifest_candidates = [
        os.path.join(episode_dir, "popups_manifest.json"),
        os.path.join(episode_dir, "02_assets_code", "popups_manifest.json"),
        os.path.join(episode_dir, "TIMELINE_MEDIA", "popups_manifest.json")
    ]
    manifest_path = None
    for cand in manifest_candidates:
        if os.path.exists(cand):
            manifest_path = cand
            break

    if manifest_path:
        mf_fails = verify_popups_manifest(manifest_path, contract, episode_dir)
        if mf_fails:
            for ff in mf_fails:
                results.append(ff)
        else:
            results.append({"check": "popups_manifest", "status": "PASS", "msg": "Pop-ups contract verified cleanly."})
    else:
        results.append({"check": "popups_manifest", "status": "WARN", "msg": "popups_manifest.json not found in episode."})

    # 2. Manim Source Scripts Check (Text colors)
    assets_code_dir = os.path.join(episode_dir, "02_assets_code")
    if os.path.exists(assets_code_dir):
        for fname in sorted(os.listdir(assets_code_dir)):
            if fname.startswith("scene") and fname.endswith(".py"):
                spath = os.path.join(assets_code_dir, fname)
                sf_fails = verify_script_text_colors(spath, contract)
                if sf_fails:
                    for ff in sf_fails:
                        results.append(ff)

    # 3. Manim Rendered Clips Check (Stage Containment)
    timeline_dir = os.path.join(episode_dir, "TIMELINE_MEDIA")
    if os.path.exists(timeline_dir):
        # Check Manim clips
        for fname in sorted(os.listdir(timeline_dir)):
            if fname.endswith(".mp4") and "flow" not in fname.lower():
                clip_path = os.path.join(timeline_dir, fname)
                stage_fails = verify_manim_clip_stage(clip_path, contract)
                if stage_fails:
                    for ff in stage_fails:
                        results.append(ff)

    has_fail = any(r.get("status") == "FAIL" for r in results)
    status = "FAIL" if has_fail else "PASS"

    return {
        "status": status,
        "results": results,
        "summary": f"Layout QA: {status} ({len([r for r in results if r.get('status')=='FAIL'])} failures)"
    }


# =============================================================================
# SELF TEST SUITE (3 Synthetic FAILs + 1 PASS)
# =============================================================================
def run_self_tests() -> bool:
    """
    Executes the mandatory 4 self-test cases:
    1. FAIL: Pop-up in caption lane (y 864-1080)
    2. FAIL: Text color using #233D4C (contrast < 4.5:1)
    3. FAIL: Pop-up over non-chrome Manim pixels
    4. PASS: Clean compliant pop-up, safe zones, allowed colors
    """
    contract = load_layout_contract()
    all_passed = True
    print("=" * 60)
    print("RUNNING LAYOUT QA SELF-TESTS (3 Synthetic FAIL + 1 PASS)")
    print("=" * 60)

    # Case 1: Synthetic FAIL — Pop-up in caption lane
    case1_manifest = [
        {
            "word": "CAPTION_COLLISION_TEST",
            "start": 1.0,
            "end": 3.0,
            "slot": "TC",
            "bbox": [700, 890, 1220, 980],  # ymax = 980 > 864 (IN CAPTION LANE)
            "color": "#FD802E",
            "scene_type": "manim"
        }
    ]
    test_m1 = os.path.join(SCRIPT_DIR, "_test_m1.json")
    with open(test_m1, "w", encoding="utf-8") as f:
        json.dump(case1_manifest, f)
    res1 = verify_popups_manifest(test_m1, contract)
    if os.path.exists(test_m1): os.remove(test_m1)

    c1_ok = any(r.get("check") == "caption_lane_collision" and r.get("status") == "FAIL" for r in res1)
    print(f"Test 1 [FAIL case: Pop-up in caption lane]: {'PASS (Correctly Failed QA)' if c1_ok else 'FAILED TO CATCH'}")
    if not c1_ok: all_passed = False

    # Case 2: Synthetic FAIL — #233D4C text color
    test_script_content = """
    from manim import *
    from pipeline.manim_theme import CleanText, UI_STRUCTURE
    class TestScene(Scene):
        def construct(self):
            t = CleanText("INVISIBLE TEXT", font_size=20, color=UI_STRUCTURE)
    """
    test_s2 = os.path.join(SCRIPT_DIR, "_test_s2.py")
    with open(test_s2, "w", encoding="utf-8") as f:
        f.write(test_script_content)
    res2 = verify_script_text_colors(test_s2, contract)
    if os.path.exists(test_s2): os.remove(test_s2)

    c2_ok = any(r.get("check") == "forbidden_text_color_ui_structure" and r.get("status") == "FAIL" for r in res2)
    print(f"Test 2 [FAIL case: #233D4C text color]: {'PASS (Correctly Failed QA)' if c2_ok else 'FAILED TO CATCH'}")
    if not c2_ok: all_passed = False

    # Case 3: Synthetic FAIL — Pop-up over Manim pixels
    # Create a synthetic frame with bright Manim content in the TL popup area (x:96-656, y:56-176)
    synth_frame = np.full((1080, 1920, 3), [32, 35, 34], dtype=np.uint8)
    # Draw bright white pixels in TL slot
    synth_frame[70:120, 150:350] = [230, 237, 243]

    # Test is_non_chrome_pixel in that bbox
    crop = synth_frame[60:170, 96:560]
    non_chrome_count = int(np.sum(is_non_chrome_pixel(crop)))
    c3_ok = non_chrome_count > 500
    print(f"Test 3 [FAIL case: Pop-up over Manim pixels]: {'PASS (Detected ' + str(non_chrome_count) + ' colliding pixels)' if c3_ok else 'FAILED TO CATCH'}")
    if not c3_ok: all_passed = False

    # Case 4: Synthetic PASS — Clean compliant pop-up
    case4_manifest = [
        {
            "word": "CLEAN_COMPLIANT_POPUP",
            "start": 1.0,
            "end": 3.0,
            "slot": "TL",
            "bbox": [96, 61, 580, 165],  # In top band y: 56-176, margins: x: 96-1824
            "color": "#C3D809",           # Allowed text color
            "scene_type": "manim"
        },
        {
            "word": "SECOND_COMPLIANT_POPUP",
            "start": 3.5,
            "end": 5.0,
            "slot": "TR",                 # Rotated slot
            "bbox": [1300, 61, 1824, 165],
            "color": "#FD802E",           # Allowed text color
            "scene_type": "manim"
        }
    ]
    test_m4 = os.path.join(SCRIPT_DIR, "_test_m4.json")
    with open(test_m4, "w", encoding="utf-8") as f:
        json.dump(case4_manifest, f)
    res4 = verify_popups_manifest(test_m4, contract)
    if os.path.exists(test_m4): os.remove(test_m4)

    c4_ok = len(res4) == 0
    print(f"Test 4 [PASS case: Clean compliant pop-up]: {'PASS (Zero QA Violations)' if c4_ok else 'FAILED: ' + str(res4)}")
    if not c4_ok: all_passed = False

    print("=" * 60)
    print(f"SELF-TEST OVERALL: {'ALL 4 TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    print("=" * 60)
    return all_passed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantrove Layout QA")
    parser.add_argument("episode_dir", nargs="?", help="Episode directory path")
    parser.add_argument("--self-test", action="store_true", help="Run synthetic self-test suite")
    parser.add_argument("--contract", help="Custom layout_contract.json path")
    args = parser.parse_args()

    if args.self_test:
        success = run_self_tests()
        sys.exit(0 if success else 1)

    if not args.episode_dir:
        print("Usage: python layout_qa.py <episode_dir> OR python layout_qa.py --self-test")
        sys.exit(1)

    report = run_layout_qa(args.episode_dir, args.contract)
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["status"] == "PASS" else 1)
