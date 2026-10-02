"""Workspace reorg 2026-10-02. Moves only (no deletes). Writes manifest + undo script."""
import json, os, shutil

ROOT = r"E:\Agentic Workspaces\ClaudeCode"
YT = "01_PROJECTS/YOUTUBE"
SCRATCH = "99_ARCHIVE/_root_scratch_2026-10-02"
YT_OLD = "99_ARCHIVE/YOUTUBE_superseded_2026-10-02"
LEG = f"{YT}/pipeline/_legacy"

MOVES = [
    # archive root rename (fixes 03_ARCHIVE / 03_TRADING_AI number clash)
    ("03_ARCHIVE", "99_ARCHIVE"),
    # root scratch
    *[(f, f"{SCRATCH}/{f}") for f in [
        "frame_clean_24s.jpg", "frame_clean_9s.jpg", "frame_rg_18s.jpg", "frame_rg_2s.jpg",
        "frame_rg_30s.jpg", "temp_test.js", "test_greek.py", "test_read.tmp", "test_s13_frame.png",
        "__pycache__", ".playwright-mcp"]],
    ("media", f"{SCRATCH}/manim_media_cache"),
    ("experiments", "99_ARCHIVE/experiments"),
    ("brand/manim_theme.py", f"{SCRATCH}/brand_manim_theme_STALE_2026-09-21.py"),
    ("QUANTROVE_CHANNEL_STATUS_REPORT_CLAUDE.md", "reports/QUANTROVE_CHANNEL_STATUS_REPORT_CLAUDE.md"),
    # YouTube root docs
    (f"{YT}/QUANTROVE_CHANNEL_STATE_REPORT_CLAUDE.md", "reports/QUANTROVE_CHANNEL_STATE_REPORT_CLAUDE.md"),
    (f"{YT}/QUANTROVE_CHANNEL_STATE_REPORT_GPT.md", "reports/QUANTROVE_CHANNEL_STATE_REPORT_GPT.md"),
    (f"{YT}/MIGRATION_MANIFEST.md", f"{YT_OLD}/MIGRATION_MANIFEST.md"),
    (f"{YT}/shorts-workstyle-director-SKILL.md", f"{YT_OLD}/shorts-workstyle-director-SKILL.md"),
    (f"{YT}/instructions_and_workflows/SIDE_ASSISTANT_BRIEF.md", f"{YT_OLD}/SIDE_ASSISTANT_BRIEF.md"),
    (f"{YT}/instructions_and_workflows/SIDE_ASSISTANT_BRIEF_v3.md", f"{YT_OLD}/SIDE_ASSISTANT_BRIEF_v3.md"),
    (f"{YT}/My Ideas", f"{YT}/topic_strategy/my_ideas"),
    # single logs/ and reports/ at workspace root
    *[(f"{YT}/logs/{f}", f"logs/{f}") for f in ["ep05_shorts_qa_2026-09-29.txt", "ep05_shorts_revised_qa_2026-09-29.txt"]],
    (f"{YT}/reports/ep05_shorts_production_report_2026-09-29.md", "reports/ep05_shorts_production_report_2026-09-29.md"),
    # longs: uniform [STATUS DATE]_longNN_slug
    (f"{YT}/longs/1. [PUBLISHED 2026-09-02] long01_why_stock_market_crashes", f"{YT}/longs/[PUBLISHED 2026-09-02]_long01_why_stock_market_crashes"),
    (f"{YT}/longs/2. [PUBLISHED 2026-09-09] long02_50_years_recession_data", f"{YT}/longs/[PUBLISHED 2026-09-09]_long02_50_years_recession_data"),
    (f"{YT}/longs/3. [PUBLISHED 2026-09-16] long03_how_algorithms_decide", f"{YT}/longs/[PUBLISHED 2026-09-16]_long03_how_algorithms_decide"),
    (f"{YT}/longs/4. [PUBLISHED 2026-09-26]_long04_can_ai_predict_markets", f"{YT}/longs/[PUBLISHED 2026-09-26]_long04_can_ai_predict_markets"),
    (f"{YT}/longs/5. [Published 2026-09-30]_long05_market_making_illusion", f"{YT}/longs/[PUBLISHED 2026-09-30]_long05_market_making_illusion"),
    (f"{YT}/longs/[IN_PROGRESS 2026-09-30]_long06_hft_microsecond_pricing", f"{YT}/longs/[SCHEDULED 2026-10-04]_long06_hft_microsecond_pricing"),
    # published shorts -> archive (shorts-archive-on-upload.md)
    (f"{YT}/shorts/01_[PUBLISHED 2026-10-01]_ep05_short_65m_penalty", f"{YT}/shorts/_ARCHIVE/published/01_[PUBLISHED 2026-10-01]_ep05_short_65m_penalty"),
    (f"{YT}/shorts/03_[PUBLISHED 2026-10-02]_ep05_Why Wall Street Pays to Trade with You 💸📉", f"{YT}/shorts/_ARCHIVE/published/03_[PUBLISHED 2026-10-02]_ep05_Why Wall Street Pays to Trade with You 💸📉"),
    # pipeline: episode one-offs + temp files -> _legacy
    *[(f"{YT}/pipeline/{f}", f"{LEG}/{f}") for f in [
        "ep02_master_audio.mp3", "ep02_short_best_day_to_invest_words.json", "ep03_build.py",
        "ep06_shorts_qa.py", "extract_ep06_shorts.py", "generate_ep06_native_shorts.py",
        "get_ep02_timestamps.py", "get_scene_sub_timestamps.py", "scene_sub_timestamps.json",
        "package_all_6_shorts.py", "render_ep03_shorts_v2.py", "render_raw_ep02_extracts.py",
        "transcribe_ep02.py", "transcribe_ep02_words.py", "temp_test_blur.mp4", "temp_align", "__pycache__"]],
]

def main():
    os.chdir(ROOT)
    done, skipped = [], []
    for src, dst in MOVES:
        if not os.path.exists(src):
            skipped.append((src, "missing")); continue
        if os.path.exists(dst):
            skipped.append((src, "target exists")); continue
        os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
        shutil.move(src, dst)
        assert not os.path.exists(src) and os.path.exists(dst), src  # rule 3.4
        done.append((src, dst))
    # now-empty YouTube logs/ reports/
    for d in (f"{YT}/logs", f"{YT}/reports"):
        if os.path.isdir(d) and not os.listdir(d):
            os.rmdir(d)
    json.dump({"moved": done, "skipped": skipped}, open("logs/reorg_2026-10-02_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open("logs/reorg_2026-10-02_UNDO.py", "w", encoding="utf-8") as f:
        f.write("import os, shutil\nos.chdir(r'%s')\n" % ROOT)
        for src, dst in reversed(done):
            f.write(f"os.makedirs(os.path.dirname({src!r}) or '.', exist_ok=True); shutil.move({dst!r}, {src!r})\n")
    print(f"moved {len(done)}, skipped {len(skipped)}")
    for s in skipped: print("SKIP", s)

if __name__ == "__main__":
    main()
