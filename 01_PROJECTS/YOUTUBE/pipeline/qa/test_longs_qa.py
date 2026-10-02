#!/usr/bin/env python3
"""
Self-test suite for longs_qa.py
Tests:
  1. Good fixtures pass all automated checks.
  2. Un-waived failing rules (e.g. L4) fail.
  3. Waived rules convert status from FAIL to WAIVED, preserve reason, and allow QA pass.
  4. Loop ledger schema and C1 validation: min(paid_at_s, partial_payoff_at_s) <= 90s.
"""

import os
import sys
import json
import shutil
import tempfile
import subprocess

QA_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, QA_DIR)

from longs_qa import run_longs_qa, print_table, DEFAULT_STYLE_PATH

GOOD_DIR = os.path.join(QA_DIR, "_selftest_longs", "good")
BAD2_DIR = os.path.join(QA_DIR, "_selftest_longs", "bad2")

def test_good_fixtures():
    print("\n--- Test 1: Good Fixtures (Expect PASS) ---")
    results = run_longs_qa(
        video_path=os.path.join(GOOD_DIR, "video.mp4"),
        words_path=os.path.join(GOOD_DIR, "words.json"),
        script_path=os.path.join(GOOD_DIR, "script.md"),
        loop_ledger_path=os.path.join(GOOD_DIR, "loop_ledger.json"),
        shotlist_path=os.path.join(GOOD_DIR, "shotlist.json"),
        voice_path=os.path.join(GOOD_DIR, "voice.wav"),
        music_path=os.path.join(GOOD_DIR, "music.wav"),
        style_path=DEFAULT_STYLE_PATH
    )
    has_fail = any(r["status"] == "FAIL" for r in results)
    assert not has_fail, "Good fixtures should have 0 FAIL results"
    print("PASS: Good fixtures passed all automated checks.")

def test_unwaived_fails():
    print("\n--- Test 2: Bad Fixture Un-waived (Expect FAIL) ---")
    results = run_longs_qa(
        video_path=os.path.join(BAD2_DIR, "video.mp4"),
        words_path=os.path.join(BAD2_DIR, "words.json"),
        script_path=os.path.join(BAD2_DIR, "script.md"),
        loop_ledger_path=os.path.join(BAD2_DIR, "loop_ledger.json"),
        shotlist_path=os.path.join(BAD2_DIR, "shotlist.json"),
        voice_path=os.path.join(BAD2_DIR, "voice.wav"),
        music_path=os.path.join(BAD2_DIR, "music.wav"),
        style_path=DEFAULT_STYLE_PATH,
        waivers=[]
    )
    l4_result = next((r for r in results if "L4" in r["rule"]), None)
    assert l4_result is not None, "L4 rule must be present in report"
    assert l4_result["status"] == "FAIL", f"Expected L4 status FAIL, got {l4_result['status']}"
    has_fail = any(r["status"] == "FAIL" for r in results)
    assert has_fail, "Bad fixtures without waivers must fail"
    print("PASS: Un-waived L4 correctly failed.")

def test_waived_rule_passes():
    print("\n--- Test 3: Waived L4 Rule (Expect WAIVED + PASS) ---")
    tmp_dir = tempfile.mkdtemp(prefix="qa_waiver_test_")
    try:
        # Create a fixture identical to GOOD except intro ends at 66.8s (fails L4)
        with open(os.path.join(GOOD_DIR, "shotlist.json"), "r", encoding="utf-8") as f:
            shotlist = json.load(f)

        # Modify intro scene duration to 66.8s (> 35s max)
        for sc in shotlist["scenes"]:
            if sc.get("chapter", 0) == 0:
                sc["end_s"] = 66.8

        shotlist_file = os.path.join(tmp_dir, "shotlist.json")
        with open(shotlist_file, "w", encoding="utf-8") as f:
            json.dump(shotlist, f, indent=2)

        # 1. Test without waiver -> L4 must FAIL
        results_nowaiver = run_longs_qa(
            video_path=os.path.join(GOOD_DIR, "video.mp4"),
            words_path=os.path.join(GOOD_DIR, "words.json"),
            script_path=os.path.join(GOOD_DIR, "script.md"),
            loop_ledger_path=os.path.join(GOOD_DIR, "loop_ledger.json"),
            shotlist_path=shotlist_file,
            voice_path=os.path.join(GOOD_DIR, "voice.wav"),
            music_path=os.path.join(GOOD_DIR, "music.wav"),
            style_path=DEFAULT_STYLE_PATH,
            waivers=[]
        )
        l4_nowaiver = next(r for r in results_nowaiver if "L4" in r["rule"])
        assert l4_nowaiver["status"] == "FAIL", "Without waiver, 66.8s intro must fail L4"

        # 2. Test with waiver -> L4 must be WAIVED
        waiver_reason = "Scene 1 is 66.8s; hook, pace line and first loop complete by ~35s; timeline locked for release"
        waivers_list = [{"rule": "L4", "reason": waiver_reason}]

        results_waived = run_longs_qa(
            video_path=os.path.join(GOOD_DIR, "video.mp4"),
            words_path=os.path.join(GOOD_DIR, "words.json"),
            script_path=os.path.join(GOOD_DIR, "script.md"),
            loop_ledger_path=os.path.join(GOOD_DIR, "loop_ledger.json"),
            shotlist_path=shotlist_file,
            voice_path=os.path.join(GOOD_DIR, "voice.wav"),
            music_path=os.path.join(GOOD_DIR, "music.wav"),
            style_path=DEFAULT_STYLE_PATH,
            waivers=waivers_list
        )
        l4_waived = next(r for r in results_waived if "L4" in r["rule"])
        assert l4_waived["status"] == "WAIVED", f"Expected WAIVED, got {l4_waived['status']}"
        assert waiver_reason in l4_waived["measured"] or waiver_reason in l4_waived.get("waiver_reason", "")

        has_fail = any(r["status"] == "FAIL" for r in results_waived)
        assert not has_fail, "With L4 waived, overall QA check must pass"

        print_table(results_waived)
        print("PASS: Waived L4 converted to WAIVED and passed overall audit.")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

def test_loop_ledger_partial_payoff():
    print("\n--- Test 4: Loop Ledger C1 Partial Payoff Logic ---")
    tmp_dir = tempfile.mkdtemp(prefix="qa_ledger_test_")
    try:
        # Loop 1 has paid_at_s = 375.0 (> 90s)
        # Case A: with partial_payoff_at_s = 86.1 (<= 90s) -> C1 PASSES
        loops_pass = [
            {"id": 1, "question": "Q1", "planted_at_s": 8.0, "paid_at_s": 105.0, "partial_payoff_at_s": 86.1, "payoff_type": "primary_insight"},
            {"id": 2, "question": "Q2", "planted_at_s": 10.0, "paid_at_s": 115.0, "payoff_type": "empirical_proof"},
            {"id": 3, "question": "Q3", "planted_at_s": 40.0, "paid_at_s": 115.0, "payoff_type": "mechanism_reveal"},
            {"id": 4, "question": "Q4", "planted_at_s": 70.0, "paid_at_s": 115.0, "payoff_type": "strategic_resolution"}
        ]
        ledger_pass_file = os.path.join(tmp_dir, "ledger_pass.json")
        with open(ledger_pass_file, "w", encoding="utf-8") as f:
            json.dump(loops_pass, f)

        res_pass = run_longs_qa(
            video_path=os.path.join(GOOD_DIR, "video.mp4"),
            words_path=os.path.join(GOOD_DIR, "words.json"),
            script_path=os.path.join(GOOD_DIR, "script.md"),
            loop_ledger_path=ledger_pass_file,
            shotlist_path=os.path.join(GOOD_DIR, "shotlist.json"),
            style_path=DEFAULT_STYLE_PATH
        )
        l5_pass = next(r for r in res_pass if "L5" in r["rule"])
        assert l5_pass["status"] == "PASS", f"Expected L5 PASS with partial_payoff_at_s=86.1, got {l5_pass['status']}"

        # Case B: both paid_at_s and partial_payoff_at_s > 90s -> C1 FAILS
        loops_fail = [
            {"id": 1, "question": "Q1", "planted_at_s": 8.0, "paid_at_s": 105.0, "partial_payoff_at_s": 95.0, "payoff_type": "primary_insight"},
            {"id": 2, "question": "Q2", "planted_at_s": 10.0, "paid_at_s": 115.0, "payoff_type": "empirical_proof"},
            {"id": 3, "question": "Q3", "planted_at_s": 40.0, "paid_at_s": 115.0, "payoff_type": "mechanism_reveal"},
            {"id": 4, "question": "Q4", "planted_at_s": 70.0, "paid_at_s": 115.0, "payoff_type": "strategic_resolution"}
        ]
        ledger_fail_file = os.path.join(tmp_dir, "ledger_fail.json")
        with open(ledger_fail_file, "w", encoding="utf-8") as f:
            json.dump(loops_fail, f)

        res_fail = run_longs_qa(
            video_path=os.path.join(GOOD_DIR, "video.mp4"),
            words_path=os.path.join(GOOD_DIR, "words.json"),
            script_path=os.path.join(GOOD_DIR, "script.md"),
            loop_ledger_path=ledger_fail_file,
            shotlist_path=os.path.join(GOOD_DIR, "shotlist.json"),
            style_path=DEFAULT_STYLE_PATH
        )
        l5_fail = next(r for r in res_fail if "L5" in r["rule"])
        assert l5_fail["status"] == "FAIL", f"Expected L5 FAIL when early payoff > 90s, got {l5_fail['status']}"

        print("PASS: Loop ledger C1 min(paid_at_s, partial_payoff_at_s) verified.")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

def main():
    print("========================================")
    print("RUNNING LONGS QA AUDIT SELF-TEST SUITE")
    print("========================================")
    test_good_fixtures()
    test_unwaived_fails()
    test_waived_rule_passes()
    test_loop_ledger_partial_payoff()
    print("\n========================================")
    print("[+] ALL 4 LONGS QA SELF-TESTS PASSED!")
    print("========================================")

if __name__ == "__main__":
    main()
