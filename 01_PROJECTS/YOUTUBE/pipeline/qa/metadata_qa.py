#!/usr/bin/env python3
"""
Quantrove Metadata QA Gate (metadata_qa.py)
Validates upload_metadata.md against pipeline/metadata/METADATA_STANDARD.md.

Checks:
- Long-form title: exactly 6-7 words and <60 characters
- Description hook: <= 150 characters
- Hashtag count: exactly 3
- Mandatory disclaimer present
- Chapters start at 0:00
- Tags character count: <= 500 chars (hard ceiling)

Usage:
    python metadata_qa.py <upload_metadata.md> [--short]
"""

import sys
import os
import re
import argparse

DISCLAIMER_KEYPHRASE = "not financial, investment, or trading advice"

def parse_args():
    parser = argparse.ArgumentParser(description="Quantrove Metadata QA Validator")
    parser.add_argument("file", help="Path to upload_metadata.md or READY_TO_PUBLISH.md")
    parser.add_argument("--short", action="store_true", help="Flag if validating a YouTube Short")
    return parser.parse_args()

def extract_section(content, section_name):
    pattern = rf"(?:^|\n)##?\s*{section_name}[:\s]*\n(.*?)(?=\n##?\s|\Z)"
    m = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else ""

def validate_metadata(filepath, is_short=False):
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    results = []

    # 1. Title Validation
    title = ""
    title_match = re.search(r"(?:Title|TITLE)[:\s]+([^\n]+)", content)
    if not title_match:
        # Check first level-1 heading
        h1_match = re.search(r"^#\s+([^\n]+)", content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
    else:
        title = title_match.group(1).strip()

    title = title.strip('"\'')
    if not title:
        results.append(("Title Extraction", "Missing", "Title must be declared", "FAIL"))
    else:
        words = title.split()
        word_count = len(words)
        char_len = len(title)
        if is_short:
            results.append(("Short Title", f"{char_len} chars", "<=100 chars", "PASS" if char_len <= 100 else "FAIL"))
        else:
            len_ok = (char_len < 60)
            words_ok = (word_count in (6, 7))
            status = "PASS" if (len_ok and words_ok) else "FAIL"
            desc = f"{word_count} words, {char_len} chars"
            results.append(("Long-Form Title", desc, "6-7 words and <60 chars", status))

    # 2. Hook Validation (max 150 chars)
    # Hook is line 1 of description or explicit Hook field
    hook = ""
    hook_match = re.search(r"(?:Hook|HOOK)[:\s]+([^\n]+)", content)
    if hook_match:
        hook = hook_match.group(1).strip()
    else:
        desc_sec = extract_section(content, "Description")
        if desc_sec:
            lines = [l.strip() for l in desc_sec.split("\n") if l.strip()]
            if lines:
                hook = lines[0]

    if hook:
        hook_len = len(hook)
        status = "PASS" if hook_len <= 150 else "FAIL"
        results.append(("Description Hook", f"{hook_len} chars", "<=150 chars", status))
    else:
        results.append(("Description Hook", "Missing", "<=150 chars", "FAIL"))

    # 3. Hashtag Count (strictly 3)
    hashtags = re.findall(r"#[A-Za-z0-9_]+", content)
    ht_count = len(hashtags)
    status = "PASS" if ht_count == 3 else "FAIL"
    results.append(("Hashtag Count", f"{ht_count} hashtags ({', '.join(hashtags)})", "Exactly 3 hashtags", status))

    # 4. Mandatory Disclaimer
    has_disclaimer = DISCLAIMER_KEYPHRASE in content.lower() and "markets involve risk" in content.lower()
    status = "PASS" if has_disclaimer else "FAIL"
    results.append(("Legal Disclaimer", "Present" if has_disclaimer else "Missing", "Mandatory standard disclaimer", status))

    # 5. Chapters start at 0:00 (for long-form)
    if not is_short:
        timestamps = re.findall(r"\b(\d{1,2}:\d{2})\b", content)
        if timestamps:
            first_ts = timestamps[0]
            status = "PASS" if first_ts in ("0:00", "00:00") else "FAIL"
            results.append(("Chapters Start", f"First timestamp: {first_ts}", "Must start at 0:00", status))
        else:
            results.append(("Chapters Start", "No timestamps found", "Must include chapters starting at 0:00", "FAIL"))

    # 6. Tags Length (<=500 chars hard ceiling, <=300 target)
    tags_text = ""
    tags_match = re.search(r"(?:Tags|TAGS)[:\s]+([^\n]+(?:\n[^\n#]+)*)", content)
    if tags_match:
        raw_tags = tags_match.group(1).strip()
        # Clean lines
        tags_text = " ".join([l.strip() for l in raw_tags.split("\n") if l.strip()])
    else:
        tags_sec = extract_section(content, "Tags")
        if tags_sec:
            tags_text = " ".join([l.strip() for l in tags_sec.split("\n") if l.strip()])

    if tags_text:
        tags_len = len(tags_text)
        if tags_len > 500:
            status = "FAIL"
        elif tags_len > 300:
            status = "WARN"
        else:
            status = "PASS"
        results.append(("Tags Char Count", f"{tags_len} chars", "<=300 target, <=500 hard cap", status))
    else:
        results.append(("Tags Char Count", "Missing tags", "<=500 chars", "FAIL"))

    # Print summary
    print(f"\n=== Quantrove Metadata QA: {os.path.basename(filepath)} ===")
    print(f"{'Check':<22} | {'Measured':<35} | {'Requirement':<32} | {'Status':<6}")
    print("-" * 102)

    has_fail = False
    for name, measured, requirement, status in results:
        if status == "FAIL":
            has_fail = True
        print(f"{name:<22} | {measured:<35} | {requirement:<32} | {status:<6}")

    print("-" * 102)
    if has_fail:
        print("RESULT: FAILED (Exit Code 1)\n")
        sys.exit(1)
    else:
        print("RESULT: PASSED\n")
        sys.exit(0)

if __name__ == "__main__":
    args = parse_args()
    validate_metadata(args.file, is_short=args.short)
