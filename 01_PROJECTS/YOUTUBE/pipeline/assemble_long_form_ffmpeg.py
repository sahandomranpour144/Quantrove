"""
assemble_long_form_ffmpeg.py — Fast FFmpeg-based assembler for long01

Builds a single ffmpeg command with a complex filtergraph that:
  1. Loads all 29 scene assets (images + videos)
  2. Applies Ken Burns zoom on static images
  3. Concatenates with crossfade/fade transitions
  4. Overlays text definition cards at timed positions
  5. Mixes voiceover + looped BGM audio
  6. Exports 1080p 60fps with loudness normalization

Much faster than moviepy (~minutes vs ~hours).
"""
import os
import subprocess
import json
import sys

def find_ep_dir(slug):
    base = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\longs"
    if os.path.isdir(base):
        for d in os.listdir(base):
            if slug in d:
                return os.path.join(base, d)
    return os.path.join(base, f"[PUBLISHED] {slug}")

EP_DIR = find_ep_dir("long01_why_stock_market_crashes")
RENDERS = os.path.join(EP_DIR, "02_assets_code", "renders")
MANIM = os.path.join(RENDERS, "manim")
VOICEOVER = os.path.join(EP_DIR, "voiceover", "ElevenLabs_video_1 voiceover.mp3")
BGM = r"E:\Agentic Workspaces\ClaudeCode\assets\audio\BGM.mp3"
OUTPUT = os.path.join(EP_DIR, "long01_why_stock_market_crashes.mp4")

FONTS_DIR = r"E:\Agentic Workspaces\ClaudeCode\assets\fonts"
FONT_BOLD = os.path.join(FONTS_DIR, "Poppins-Bold.ttf")
FONT_REGULAR = os.path.join(FONTS_DIR, "Poppins-Regular.ttf")

W, H, FPS = 1920, 1080, 30  # 30fps for faster render; change to 60 for final

# Scene list: (filename, duration_seconds_or_None, transition_type)
SCENES = [
    ("Scene_01_sp500_crash_animation.mp4", None, "cut"),
    ("Scene_02_1929_vs_2008_comparison.png", 4, "xfade"),
    ("Scene_03_title_card.png", 8, "fade"),
    ("Scene_04_panic_symptom_concept.png", 6, "cut"),
    ("Scene_05_crash_architecture_diagram.png", 6, "xfade"),
    ("Scene_06_three_crashes_overview.png", 8, "xfade"),
    ("Scene_07_08_crowded_room_metaphor.mp4", None, "xfade"),
    ("Scene_09_order_book_liquidity_drain.mp4", None, "xfade"),
    ("Scene_10_market_decline_taxonomy.png", 6, "xfade"),
    ("Scene_11_three_fires_chapters.png", 5, "xfade"),
    ("Scene_12_roaring_twenties_bull_run.png", 8, "xfade"),
    ("Scene_13_margin_call_wipeout.mp4", None, "xfade"),
    ("Scene_14_black_thursday_tuesday_crash.png", 8, "xfade"),
    ("Scene_15_1929_1932_full_collapse.png", 8, "xfade"),
    ("Scene_16_1929_summary_card.png", 5, "xfade"),
    ("Scene_17_subprime_pipeline.png", 7, "fade"),
    ("Scene_18_largest_bankruptcies.png", 6, "xfade"),
    ("Scene_19_domino_cascade_2008.mp4", None, "xfade"),
    ("Scene_20_2008_summary_card.png", 5, "xfade"),
    ("Scene_21_pandemic_shock_backdrop.png", 6, "fade"),
    ("Scene_22_worst_one_day_point_drops.png", 7, "xfade"),
    ("Scene_23_circuit_breakers_halt.mp4", None, "xfade"),
    ("Scene_24_v_shaped_recovery.mp4", None, "xfade"),
    ("Scene_25_2020_summary_card.png", 5, "xfade"),
    ("Scene_26_master_comparison_matrix.png", 8, "xfade"),
    ("Scene_27_universal_mechanism.mp4", None, "xfade"),
    ("Scene_28_investor_takeaways.png", 5, "xfade"),
    ("Scene_29_fifty_years_macro_teaser.png", 6, "xfade"),
    ("Scene_30_outro_end_screen.png", 20, "fade"),
]

# Pacing holds — extra seconds added to these clips
HOLD_EXTRA = {
    "Scene_13_margin_call_wipeout.mp4": 1.5,
    "Scene_16_1929_summary_card.png": 1.0,
    "Scene_20_2008_summary_card.png": 1.0,
    "Scene_27_universal_mechanism.mp4": 2.0,
}

# Text definitions: (timecode_sec, term, definition)
DEFINITIONS = [
    (110, "Bear market", "when the market falls 20%+ from its recent peak"),
    (190, "Margin buying", "borrowing money to buy stocks, using stocks as collateral"),
    (205, "The Dow", "average of 30 major U.S. company stock prices"),
    (270, "Bankruptcy", "when a company legally admits it can't pay what it owes"),
    (305, "S&P 500", "broader index of 500 major U.S. companies"),
    (325, "Circuit breaker", "automatic trading pause when market falls too fast"),
]

XFADE_DUR = 0.4  # crossfade duration in seconds


def find_asset(filename):
    for base in (RENDERS, MANIM):
        p = os.path.join(base, filename)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"[ERROR] Missing asset: {filename}")


def probe_duration(path):
    """Get duration of a video file using ffprobe."""
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json",
           "-show_format", path]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    return float(info["format"]["duration"])


def build_concat_file(scenes_with_durations, concat_path):
    """Build an ffmpeg concat demuxer file from prepared segments."""
    with open(concat_path, "w", encoding="utf-8") as f:
        for seg_path, dur in scenes_with_durations:
            # Escape single quotes in path for ffmpeg concat
            escaped = seg_path.replace("'", "'\\''")
            f.write(f"file '{escaped}'\n")
            if dur:
                f.write(f"duration {dur}\n")
    return concat_path


def prepare_segment(filename, duration, idx, tmp_dir):
    """Prepare a single scene segment as a standardized MP4 clip."""
    path = find_asset(filename)
    extra = HOLD_EXTRA.get(filename, 0)
    out_path = os.path.join(tmp_dir, f"seg_{idx:02d}.mp4")
    is_video = filename.lower().endswith(".mp4")

    if is_video:
        # Get native duration
        native_dur = probe_duration(path)
        total_dur = native_dur + extra

        if extra > 0:
            # Freeze last frame for extra seconds using tpad
            cmd = [
                "ffmpeg", "-y", "-i", path,
                "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                       f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x05070A,"
                       f"fps={FPS},tpad=stop_mode=clone:stop_duration={extra}",
                "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-t", str(total_dur),
                out_path
            ]
        else:
            cmd = [
                "ffmpeg", "-y", "-i", path,
                "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                       f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x05070A,"
                       f"fps={FPS}",
                "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                out_path
            ]
        actual_dur = total_dur
    else:
        # Static image — Ken Burns zoom + set duration
        img_dur = (duration or 5) + extra
        # zoompan: zoom from 100% to 104% over the duration (subtle Ken Burns)
        # z='min(zoom+0.0001,1.5)' is the zoom speed
        zoom_speed = 0.04 / (img_dur * FPS)  # total 4% zoom over duration
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-i", path,
            "-vf", f"scale=2000:-1,"  # upscale slightly for zoom headroom
                   f"zoompan=z='1+{zoom_speed}*in':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                   f":d={int(img_dur * FPS)}:s={W}x{H}:fps={FPS},"
                   f"format=yuv420p",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(img_dur),
            out_path
        ]
        actual_dur = img_dur

    print(f"  [{idx+1:2d}/{len(SCENES)}] {filename} → {actual_dur:.1f}s")
    subprocess.run(cmd, capture_output=True, check=True)
    return out_path, actual_dur


def apply_xfades(segments, tmp_dir):
    """
    Apply crossfade transitions between segments using ffmpeg xfade filter.
    Uses iterative pairwise xfade to avoid overly complex filtergraph.
    """
    if len(segments) < 2:
        return segments[0][0]

    current_path = segments[0][0]
    current_dur = segments[0][1]

    for i in range(1, len(segments)):
        next_path = segments[i][0]
        next_dur = segments[i][1]
        transition = SCENES[i][2]
        out_path = os.path.join(tmp_dir, f"xfade_{i:02d}.mp4")

        offset = current_dur - XFADE_DUR

        if transition == "xfade":
            xfade_filter = f"xfade=transition=dissolve:duration={XFADE_DUR}:offset={offset:.3f}"
        elif transition == "fade":
            xfade_filter = f"xfade=transition=fade:duration={XFADE_DUR}:offset={offset:.3f}"
        else:
            # Hard cut — just concatenate
            concat_tmp = os.path.join(tmp_dir, f"concat_{i:02d}.txt")
            with open(concat_tmp, "w") as f:
                f.write(f"file '{current_path}'\n")
                f.write(f"file '{next_path}'\n")
            cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
                   "-i", concat_tmp,
                   "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                   out_path]
            subprocess.run(cmd, capture_output=True, check=True)
            current_path = out_path
            current_dur = current_dur + next_dur
            print(f"  Cut {i}: {current_dur:.1f}s total")
            continue

        cmd = [
            "ffmpeg", "-y",
            "-i", current_path,
            "-i", next_path,
            "-filter_complex", xfade_filter,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            out_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  [WARN] xfade failed at segment {i}, falling back to hard cut")
            print(f"  stderr: {result.stderr[-300:]}")
            # Fallback: concat without transition
            concat_tmp = os.path.join(tmp_dir, f"concat_{i:02d}.txt")
            with open(concat_tmp, "w") as f:
                f.write(f"file '{current_path}'\n")
                f.write(f"file '{next_path}'\n")
            cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
                   "-i", concat_tmp,
                   "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                   out_path]
            subprocess.run(cmd, capture_output=True, check=True)
            current_dur = current_dur + next_dur
        else:
            current_dur = current_dur + next_dur - XFADE_DUR

        current_path = out_path
        print(f"  Transition {i}/{len(segments)-1}: {current_dur:.1f}s total")

    return current_path


def add_text_overlays(video_path, output_path):
    """Add text definition overlays using ffmpeg drawtext filter."""
    # Build drawtext filter chain
    font_bold_escaped = FONT_BOLD.replace("\\", "/").replace(":", "\\:")
    font_regular_escaped = FONT_REGULAR.replace("\\", "/").replace(":", "\\:")

    drawtext_filters = []
    for t, term, definition in DEFINITIONS:
        t_end = t + 3.5
        # Replace single quotes with smart quotes to avoid breaking ffmpeg syntax
        term_clean = term.replace("'", "’").replace("%", "％")
        def_clean = definition.replace("'", "’").replace("%", "％")
        
        # Term label (gold, bold)
        drawtext_filters.append(
            f"drawtext=fontfile='{font_bold_escaped}':text='{term_clean}'"
            f":fontsize=44:fontcolor=#F59E0B:borderw=2:bordercolor=black"
            f":x=40:y=h-120:enable='between(t,{t},{t_end})'"
            f":box=1:boxcolor=#0B0E14@0.8:boxborderw=8"
        )
        # Definition (white, regular)
        drawtext_filters.append(
            f"drawtext=fontfile='{font_regular_escaped}':text='{def_clean}'"
            f":fontsize=32:fontcolor=white:borderw=1:bordercolor=black"
            f":x=40:y=h-65:enable='between(t,{t},{t_end})'"
            f":box=1:boxcolor=#0B0E14@0.8:boxborderw=6"
        )

    vf = ",".join(drawtext_filters)

    cmd = [
        "ffmpeg", "-y", "-i", video_path,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "copy",
        output_path
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def mix_audio(video_path, output_path):
    """Mix voiceover + looped BGM onto the video, with loudness normalization."""
    # Get video duration
    vid_dur = probe_duration(video_path)

    # Step 1: Mix audio — loop BGM, set volume, fade in/out
    mix_tmp = output_path.replace(".mp4", "_premix.mp4")
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", VOICEOVER,
        "-stream_loop", "-1", "-i", BGM,
        "-filter_complex",
        f"[2:a]atrim=0:{vid_dur},volume=0.18,afade=t=in:st=0:d=2,afade=t=out:st={vid_dur-8}:d=8[bgm];"
        f"[1:a]apad[voice];"
        f"[voice][bgm]amix=inputs=2:duration=first:dropout_transition=3[aout]",
        "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-t", str(vid_dur),
        mix_tmp
    ]
    print("  Mixing voiceover + BGM...")
    subprocess.run(cmd, capture_output=True, check=True)

    # Step 2: Loudness normalize to -14 LUFS
    cmd = [
        "ffmpeg", "-y", "-i", mix_tmp,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        output_path
    ]
    print("  Normalizing loudness to -14 LUFS...")
    subprocess.run(cmd, capture_output=True, check=True)

    # Cleanup
    os.remove(mix_tmp)


def main():
    tmp_dir = os.path.join(EP_DIR, "_assembly_tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    # Step 1: Prepare individual segments
    print(f"[1/4] Preparing {len(SCENES)} scene segments...")
    segments = []
    for idx, (filename, duration, transition) in enumerate(SCENES):
        seg_path, seg_dur = prepare_segment(filename, duration, idx, tmp_dir)
        segments.append((seg_path, seg_dur))

    # Step 2: Apply transitions (xfade between segments)
    print(f"\n[2/4] Applying transitions...")
    video_no_text = apply_xfades(segments, tmp_dir)

    # Step 3: Add text overlays
    print(f"\n[3/4] Adding text definition overlays...")
    video_with_text = os.path.join(tmp_dir, "video_with_text.mp4")
    add_text_overlays(video_no_text, video_with_text)

    # Step 4: Mix audio + loudness normalize
    print(f"\n[4/4] Mixing audio and normalizing...")
    mix_audio(video_with_text, OUTPUT)

    # Report
    final_dur = probe_duration(OUTPUT)
    final_size = os.path.getsize(OUTPUT) / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"[DONE] Assembly complete!")
    print(f"  Output:   {OUTPUT}")
    print(f"  Duration: {final_dur:.1f}s ({int(final_dur//60)}:{int(final_dur%60):02d})")
    print(f"  Size:     {final_size:.1f} MB")
    print(f"{'='*60}")

    # Cleanup tmp
    print("\nCleaning up temp files...")
    import shutil
    shutil.rmtree(tmp_dir, ignore_errors=True)
    print("Done.")


if __name__ == "__main__":
    main()
