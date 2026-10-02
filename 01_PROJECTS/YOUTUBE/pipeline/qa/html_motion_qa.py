#!/usr/bin/env python3
"""
Quantrove html_motion QA Gate (html_motion_qa.py)
Automated verification of html_motion MP4 clips and HTML source against HTML_MOTION_STANDARD.md.

Usage:
    python html_motion_qa.py <clip.mp4> --html <source.html> --aspect 16:9|9:16 --dur <seconds>
"""

import sys
import os
import re
import json
import subprocess
import argparse

# Allowed palette colors (case-insensitive hex and corresponding RGB)
# Strict Palette Lock: #202322, #233D4C, #C3D809, #FD802E, #E6EDF3 (plus opacity)
ALLOWED_HEX_BASES = {
    "202322": (32, 35, 34),
    "233D4C": (35, 61, 76),
    "C3D809": (195, 216, 9),
    "FD802E": (253, 128, 46),
    "E6EDF3": (230, 237, 243)
}

ALLOWED_NAMED = {"transparent", "currentcolor", "inherit", "none", "initial"}

def parse_args():
    parser = argparse.ArgumentParser(description="Quantrove html_motion QA Gate")
    parser.add_argument("clip", nargs="?", default=None, help="Path to exported MP4 clip")
    parser.add_argument("--html", required=True, help="Path to HTML source file")
    parser.add_argument("--aspect", required=True, choices=["16:9", "9:16"], help="Aspect ratio")
    parser.add_argument("--dur", required=True, type=float, help="Expected duration in seconds")
    return parser.parse_args()

def check_ffprobe(clip_path, expected_aspect, expected_dur):
    results = []
    if not clip_path or not os.path.exists(clip_path):
        results.append(("MP4 Exists", "Not Found", "File must exist", "FAIL"))
        return results

    expected_res = (1920, 1080) if expected_aspect == "16:9" else (1080, 1920)

    try:
        cmd = [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height,r_frame_rate,duration",
            "-show_entries", "format=duration",
            "-of", "json",
            clip_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(res.stdout)
        stream = data["streams"][0]
        w = int(stream["width"])
        h = int(stream["height"])

        # Check resolution
        res_str = f"{w}x{h}"
        expected_res_str = f"{expected_res[0]}x{expected_res[1]}"
        if (w, h) == expected_res:
            results.append(("Resolution", res_str, expected_res_str, "PASS"))
        else:
            results.append(("Resolution", res_str, expected_res_str, "FAIL"))

        # Check frame rate (must be 60/1 fps)
        fps_raw = stream.get("r_frame_rate", "")
        if fps_raw == "60/1":
            results.append(("Framerate", fps_raw, "60/1", "PASS"))
        else:
            try:
                num, den = map(float, fps_raw.split("/"))
                fps_val = num / den if den != 0 else 0
                if abs(fps_val - 60.0) < 0.05:
                    results.append(("Framerate", f"{fps_val:.2f} fps", "60/1", "PASS"))
                else:
                    results.append(("Framerate", f"{fps_raw} ({fps_val:.2f})", "60/1", "FAIL"))
            except Exception:
                results.append(("Framerate", fps_raw, "60/1", "FAIL"))

        # Check duration (+-0.05s tolerance)
        dur_val = float(stream.get("duration") or data.get("format", {}).get("duration", 0))
        diff = abs(dur_val - expected_dur)
        if diff <= 0.05:
            results.append(("Duration", f"{dur_val:.2f}s", f"{expected_dur:.2f}s (±0.05s)", "PASS"))
        else:
            results.append(("Duration", f"{dur_val:.2f}s (diff {diff:.2f}s)", f"{expected_dur:.2f}s (±0.05s)", "FAIL"))

    except Exception as e:
        results.append(("ffprobe Probe", f"Error: {e}", "Valid media probe", "FAIL"))

    return results

def check_html(html_path, aspect):
    results = []
    if not os.path.exists(html_path):
        results.append(("HTML Exists", "Not Found", "File must exist", "FAIL"))
        return results

    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 1. External URLs (FAIL)
    # Check for http:// or https:// (outside of xmlns or doctype)
    external_urls = []
    for match in re.finditer(r'https?://[^\s\'"<>]+', content, re.IGNORECASE):
        url = match.group(0)
        if "w3.org" in url:
            continue
        external_urls.append(url)

    if external_urls:
        results.append(("External Assets/URLs", f"Found {len(external_urls)} external URL(s)", "0 external URLs (self-contained)", "FAIL"))
    else:
        results.append(("External Assets/URLs", "None found", "0 external URLs (self-contained)", "PASS"))

    # 2. Audio APIs (FAIL)
    audio_hits = re.findall(r'\b(AudioContext|webkitAudioContext|OscillatorNode|createAudioBuffer|<audio\b|new\s+Audio\b)', content, re.IGNORECASE)
    if audio_hits:
        results.append(("Audio APIs", f"Found: {', '.join(set(audio_hits))}", "Zero audio elements or APIs", "FAIL"))
    else:
        results.append(("Audio APIs", "None", "Zero audio elements or APIs", "PASS"))

    # 3. Gradients (FAIL)
    gradient_hits = re.findall(r'(linear-gradient|radial-gradient|conic-gradient|<linearGradient|<radialGradient)', content, re.IGNORECASE)
    if gradient_hits:
        results.append(("Gradients", f"Found {len(gradient_hits)} gradient occurrence(s)", "Zero gradients (flat color lock)", "FAIL"))
    else:
        results.append(("Gradients", "None", "Zero gradients (flat color lock)", "PASS"))

    # 4. Box/Text Shadow Glow (FAIL)
    shadow_hits = re.findall(r'\b(box-shadow|text-shadow)\s*:\s*([^;>]+)', content, re.IGNORECASE)
    disallowed_shadows = [val.strip() for prop, val in shadow_hits if val.strip().lower() not in ("none", "0")]
    if disallowed_shadows:
        results.append(("Shadows/Glows", f"Found {len(disallowed_shadows)} shadow(s)", "Zero box/text shadows or glow", "FAIL"))
    else:
        results.append(("Shadows/Glows", "None", "Zero box/text shadows or glow", "PASS"))

    # 5. Font size check
    min_font_px = 28 if aspect == "16:9" else 40
    # Match font-size: Xpx or font-size = Xpx
    font_sizes = []
    for m in re.finditer(r'font-size\s*:\s*(\d+)(?:\.\d+)?px', content, re.IGNORECASE):
        font_sizes.append(int(m.group(1)))
    for m in re.finditer(r'fontSize\s*[:=]\s*["\']?(\d+)(?:\.\d+)?px', content, re.IGNORECASE):
        font_sizes.append(int(m.group(1)))

    small_fonts = [s for s in font_sizes if s < min_font_px]
    if small_fonts:
        results.append(("Min Font Size", f"Found {min(small_fonts)}px (min allowed {min_font_px}px)", f">={min_font_px}px", "FAIL"))
    else:
        val_str = f"Min observed: {min(font_sizes)}px" if font_sizes else "None declared in px"
        results.append(("Min Font Size", val_str, f">={min_font_px}px", "PASS"))

    # 6. Palette Color Lock (FAIL on any hex/rgb/rgba/named outside palette)
    # Extract hex colors
    invalid_colors = []
    for m in re.finditer(r'#([0-9a-fA-F]{3,8})\b', content):
        hex_code = m.group(1).upper()
        if len(hex_code) in (3, 4):
            expanded = "".join(c * 2 for c in hex_code[:3])
        elif len(hex_code) in (6, 8):
            expanded = hex_code[:6]
        else:
            invalid_colors.append(f"#{hex_code}")
            continue

        if expanded not in ALLOWED_HEX_BASES:
            invalid_colors.append(f"#{hex_code}")

    # Extract rgb / rgba colors
    for m in re.finditer(r'rgba?\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', content, re.IGNORECASE):
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        matched = False
        for allowed_rgb in ALLOWED_HEX_BASES.values():
            if (r, g, b) == allowed_rgb:
                matched = True
                break
        if not matched:
            invalid_colors.append(f"rgb({r},{g},{b})")

    # Common named colors to block
    named_color_pattern = re.findall(r'\b(color|background|fill|stroke)\s*:\s*(red|green|blue|white|black|yellow|cyan|magenta|orange|purple|gray|grey)\b', content, re.IGNORECASE)
    for prop, name in named_color_pattern:
        invalid_colors.append(f"{name} (named)")

    if invalid_colors:
        sample = list(set(invalid_colors))[:5]
        results.append(("Palette Lock", f"Disallowed colors: {', '.join(sample)}", "Only #202322, #233D4C, #C3D809, #FD802E, #E6EDF3", "FAIL"))
    else:
        results.append(("Palette Lock", "Strict palette preserved", "Only #202322, #233D4C, #C3D809, #FD802E, #E6EDF3", "PASS"))

    # 7. Data source or ILLUSTRATIVE marker (WARN if missing)
    has_marker = bool(re.search(r'(ILLUSTRATIVE\s*DATA|DATA\s*SOURCE|SOURCE\s*:|CITE\s*:)', content, re.IGNORECASE))
    if has_marker:
        results.append(("Data Integrity Marker", "Data source or ILLUSTRATIVE tag present", "Source citation or ILLUSTRATIVE DATA marker", "PASS"))
    else:
        results.append(("Data Integrity Marker", "No citation or ILLUSTRATIVE DATA tag found", "Source citation or ILLUSTRATIVE DATA marker", "WARN"))

    return results

def main():
    args = parse_args()
    results = []

    # Run HTML checks
    results.extend(check_html(args.html, args.aspect))

    # Run MP4 checks if clip provided
    if args.clip:
        results.extend(check_ffprobe(args.clip, args.aspect, args.dur))

    # Print summary table
    print("\n=== Quantrove html_motion QA Gate ===")
    print(f"{'Check':<24} | {'Measured':<32} | {'Requirement':<35} | {'Status':<6}")
    print("-" * 105)

    has_fail = False
    for name, measured, requirement, status in results:
        if status == "FAIL":
            has_fail = True
        print(f"{name:<24} | {measured:<32} | {requirement:<35} | {status:<6}")

    print("-" * 105)
    if has_fail:
        print("RESULT: FAILED (Exit Code 1)\n")
        sys.exit(1)
    else:
        print("RESULT: PASSED\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
