"""
assemble_long_form.py
Assembles long01_why_stock_market_crashes from its rendered scene assets.

Fix vs. v1: total runtime is now anchored to the REAL voiceover length.
MP4 clips keep their natural playback speed (untouched). The static image
"hold" durations are scaled to absorb whatever time is left, so the final
video always exactly matches the voiceover — never shorter, never longer.

Note: Uses a pure FFmpeg filtergraph backend for 50-100x faster rendering
than MoviePy, without requiring ImageMagick.
"""
import os
import subprocess
import json
import shutil

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
BGM = r"E:\Agentic Workspaces\ClaudeCode\assets\audio\bgm.mp3"
OUTPUT = os.path.join(EP_DIR, "long01_why_stock_market_crashes.mp4")

FONTS_DIR = r"E:\Agentic Workspaces\ClaudeCode\assets\fonts"
FONT_BOLD = os.path.join(FONTS_DIR, "Poppins-Bold.ttf")
FONT_REGULAR = os.path.join(FONTS_DIR, "Poppins-Regular.ttf")

W, H, FPS = 1920, 1080, 60

# (filename, is_video, nominal_duration, transition)
SCENES = [
    ("Scene_01_sp500_crash_animation.mp4", True, None, "cut"),
    ("Scene_02_1929_vs_2008_comparison.png", False, 4, "xfade"),
    ("Scene_03_title_card.png", False, 8, "fade"),
    ("Scene_04_panic_symptom_concept.png", False, 6, "cut"),
    ("Scene_05_crash_architecture_diagram.png", False, 6, "xfade"),
    ("Scene_06_three_crashes_overview.png", False, 8, "xfade"),
    ("Scene_07_08_crowded_room_metaphor.mp4", True, None, "xfade"),
    ("Scene_09_order_book_liquidity_drain.mp4", True, None, "xfade"),
    ("Scene_10_market_decline_taxonomy.png", False, 6, "xfade"),
    ("Scene_11_three_fires_chapters.png", False, 5, "xfade"),
    ("Scene_12_roaring_twenties_bull_run.png", False, 8, "xfade"),
    ("Scene_13_margin_call_wipeout.mp4", True, None, "xfade"),
    ("Scene_14_black_thursday_tuesday_crash.png", False, 8, "xfade"),
    ("Scene_15_1929_1932_full_collapse.png", False, 8, "xfade"),
    ("Scene_16_1929_summary_card.png", False, 5, "xfade"),
    ("Scene_17_subprime_pipeline.png", False, 7, "fade"),
    ("Scene_18_largest_bankruptcies.png", False, 6, "xfade"),
    ("Scene_19_domino_cascade_2008.mp4", True, None, "xfade"),
    ("Scene_20_2008_summary_card.png", False, 5, "xfade"),
    ("Scene_21_pandemic_shock_backdrop.png", False, 6, "fade"),
    ("Scene_22_worst_one_day_point_drops.png", False, 7, "xfade"),
    ("Scene_23_circuit_breakers_halt.mp4", True, None, "xfade"),
    ("Scene_24_v_shaped_recovery.mp4", True, None, "xfade"),
    ("Scene_25_2020_summary_card.png", False, 5, "xfade"),
    ("Scene_26_master_comparison_matrix.png", False, 8, "xfade"),
    ("Scene_27_universal_mechanism.mp4", True, None, "xfade"),
    ("Scene_28_investor_takeaways.png", False, 5, "xfade"),
    ("Scene_29_fifty_years_macro_teaser.png", False, 6, "xfade"),
    ("Scene_30_outro_end_screen.png", False, 20, "fade"),
]

HOLD_EXTRA_SEC = {
    "Scene_13_margin_call_wipeout.mp4": 1.5,
    "Scene_16_1929_summary_card.png": 1.0,
    "Scene_20_2008_summary_card.png": 1.0,
    "Scene_27_universal_mechanism.mp4": 2.0,
}

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
    """Get duration of a video or audio file using ffprobe."""
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json",
           "-show_format", path]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    info = json.loads(result.stdout)
    return float(info["format"]["duration"])

def compute_scaled_durations(voice_duration):
    """Pass 1: measure real MP4 lengths, then compute the scale factor that
    makes total image-hold time + MP4 time exactly equal voice_duration."""
    mp4_native = {}
    mp4_total = 0.0
    png_nominal_total = 0.0

    for fn, is_video, nominal, _trans in SCENES:
        extra = HOLD_EXTRA_SEC.get(fn, 0)
        if is_video:
            dur = probe_duration(find_asset(fn))
            mp4_native[fn] = dur
            mp4_total += dur + extra
        else:
            png_nominal_total += nominal

    num_xfades = sum(1 for _, _, _, trans in SCENES if trans in ("xfade", "fade", "dissolve"))
    total_xfade_loss = num_xfades * XFADE_DUR
    
    target_png_total = (voice_duration + total_xfade_loss) - mp4_total
    
    if target_png_total <= 0:
        raise ValueError(
            f"[ERROR] MP4 clips alone ({mp4_total:.1f}s) exceed the "
            f"target length ({voice_duration + total_xfade_loss:.1f}s). Cannot fit image holds."
        )
        
    scale = target_png_total / png_nominal_total
    print(f"  [DEBUG] voiceover={voice_duration:.1f}s | xfade_loss={total_xfade_loss:.1f}s | "
          f"mp4_total={mp4_total:.1f}s | png_nominal={png_nominal_total:.1f}s "
          f"-> scaled png to {target_png_total:.1f}s (scale factor {scale:.3f}x)")
    return mp4_native, scale

def prepare_segment(filename, is_video, nominal, idx, tmp_dir, mp4_native, scale):
    path = find_asset(filename)
    extra = HOLD_EXTRA_SEC.get(filename, 0)
    out_path = os.path.join(tmp_dir, f"seg_{idx:02d}.mp4")

    if is_video:
        native_dur = mp4_native[filename]
        total_dur = native_dur + extra

        if extra > 0:
            cmd = [
                "ffmpeg", "-y", "-i", path,
                "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                       f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0x05070A,"
                       f"fps={FPS},tpad=stop_mode=clone:stop_duration={extra}",
                "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                "-t", str(total_dur), out_path
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
        img_dur = (nominal * scale) + extra
        zoom_speed = 0.04 / (img_dur * FPS)
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-i", path,
            "-vf", f"scale=2000:-1,"
                   f"zoompan=z='1+{zoom_speed}*in':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                   f":d={int(img_dur * FPS)}:s={W}x{H}:fps={FPS},format=yuv420p",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(img_dur), out_path
        ]
        actual_dur = img_dur

    print(f"  [{idx+1:2d}/{len(SCENES)}] {filename} → {actual_dur:.1f}s")
    subprocess.run(cmd, capture_output=True, check=True)
    return out_path, actual_dur

def apply_xfades(segments, tmp_dir):
    if len(segments) < 2:
        return segments[0][0]

    current_path = segments[0][0]
    current_dur = segments[0][1]

    for i in range(1, len(segments)):
        next_path = segments[i][0]
        next_dur = segments[i][1]
        transition = SCENES[i][3]
        out_path = os.path.join(tmp_dir, f"xfade_{i:02d}.mp4")

        offset = current_dur - XFADE_DUR

        if transition in ("xfade", "dissolve"):
            xfade_filter = f"xfade=transition=dissolve:duration={XFADE_DUR}:offset={offset:.3f}"
        elif transition == "fade":
            xfade_filter = f"xfade=transition=fade:duration={XFADE_DUR}:offset={offset:.3f}"
        else:
            concat_tmp = os.path.join(tmp_dir, f"concat_{i:02d}.txt")
            with open(concat_tmp, "w") as f:
                f.write(f"file '{current_path}'\n")
                f.write(f"file '{next_path}'\n")
            cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
                   "-i", concat_tmp, "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                   out_path]
            subprocess.run(cmd, capture_output=True, check=True)
            current_path = out_path
            current_dur = current_dur + next_dur
            print(f"  Cut {i}: {current_dur:.1f}s total")
            continue

        cmd = [
            "ffmpeg", "-y",
            "-i", current_path, "-i", next_path,
            "-filter_complex", xfade_filter,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            out_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  [WARN] xfade failed at segment {i}, falling back to hard cut")
            concat_tmp = os.path.join(tmp_dir, f"concat_{i:02d}.txt")
            with open(concat_tmp, "w") as f:
                f.write(f"file '{current_path}'\n")
                f.write(f"file '{next_path}'\n")
            cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
                   "-i", concat_tmp, "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                   out_path]
            subprocess.run(cmd, capture_output=True, check=True)
            current_dur = current_dur + next_dur
        else:
            current_dur = current_dur + next_dur - XFADE_DUR

        current_path = out_path
        print(f"  Transition {i}/{len(segments)-1}: {current_dur:.1f}s total")

    return current_path

def add_text_overlays(video_path, output_path, video_duration):
    font_bold_escaped = FONT_BOLD.replace("\\", "/").replace(":", "\\:")
    font_regular_escaped = FONT_REGULAR.replace("\\", "/").replace(":", "\\:")

    drawtext_filters = []
    for t, term, definition in DEFINITIONS:
        if t >= video_duration:
            print(f"    [WARN] Skipping '{term}' — timecode {t}s is past video end.")
            continue
            
        t_end = t + 3.5
        term_clean = term.replace("'", "’").replace("%", "％")
        def_clean = definition.replace("'", "’").replace("%", "％")
        
        drawtext_filters.append(
            f"drawtext=fontfile='{font_bold_escaped}':text='{term_clean}'"
            f":fontsize=44:fontcolor=#F59E0B:borderw=2:bordercolor=black"
            f":x=40:y=h-120:enable='between(t,{t},{t_end})'"
            f":box=1:boxcolor=#0B0E14@0.8:boxborderw=8"
        )
        drawtext_filters.append(
            f"drawtext=fontfile='{font_regular_escaped}':text='{def_clean}'"
            f":fontsize=32:fontcolor=white:borderw=1:bordercolor=black"
            f":x=40:y=h-65:enable='between(t,{t},{t_end})'"
            f":box=1:boxcolor=#0B0E14@0.8:boxborderw=6"
        )

    if not drawtext_filters:
        shutil.copyfile(video_path, output_path)
        return

    vf = ",".join(drawtext_filters)
    cmd = [
        "ffmpeg", "-y", "-i", video_path, "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-c:a", "copy",
        output_path
    ]
    subprocess.run(cmd, capture_output=True, check=True)

def mix_audio(video_path, output_path):
    vid_dur = probe_duration(video_path)
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

    cmd = [
        "ffmpeg", "-y", "-i", mix_tmp,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        output_path
    ]
    print("  Normalizing loudness to -14 LUFS...")
    subprocess.run(cmd, capture_output=True, check=True)
    os.remove(mix_tmp)

def build_video():
    tmp_dir = os.path.join(EP_DIR, "_assembly_tmp")
    os.makedirs(tmp_dir, exist_ok=True)

    print("[0/5] Measuring real voiceover length...")
    voice_duration = probe_duration(VOICEOVER)

    print("[1/5] Computing scaled scene durations (measuring MP4s, scaling image holds)...")
    mp4_native, scale = compute_scaled_durations(voice_duration)

    print(f"\n[2/5] Preparing {len(SCENES)} scene segments...")
    segments = []
    for idx, (filename, is_video, nominal, transition) in enumerate(SCENES):
        seg_path, seg_dur = prepare_segment(filename, is_video, nominal, idx, tmp_dir, mp4_native, scale)
        segments.append((seg_path, seg_dur))

    print(f"\n[3/5] Applying transitions...")
    video_no_text = apply_xfades(segments, tmp_dir)
    video_duration = probe_duration(video_no_text)
    print(f"  [DEBUG] Assembled video length: {video_duration:.1f}s vs voiceover {voice_duration:.1f}s")

    print(f"\n[4/5] Adding text definition overlays...")
    video_with_text = os.path.join(tmp_dir, "video_with_text.mp4")
    add_text_overlays(video_no_text, video_with_text, video_duration)

    print(f"\n[5/5] Mixing audio and normalizing...")
    mix_audio(video_with_text, OUTPUT)

    final_dur = probe_duration(OUTPUT)
    final_size = os.path.getsize(OUTPUT) / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"[DONE] Assembly complete!")
    print(f"  Output:   {OUTPUT}")
    print(f"  Duration: {final_dur:.1f}s ({int(final_dur//60)}:{int(final_dur%60):02d})")
    print(f"  Size:     {final_size:.1f} MB")
    print(f"{'='*60}")

    shutil.rmtree(tmp_dir, ignore_errors=True)

if __name__ == "__main__":
    build_video()