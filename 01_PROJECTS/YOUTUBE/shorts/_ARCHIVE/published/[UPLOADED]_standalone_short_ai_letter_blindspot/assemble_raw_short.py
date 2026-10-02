import os
import subprocess

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.join(CURRENT_DIR, "TIMELINE_MEDIA")

MASTER_AUDIO = os.path.join(TIMELINE_DIR, "00_VOICEOVER_master.wav")
CONCAT_TXT = os.path.join(CURRENT_DIR, "scenes_concat.txt")
RAW_VIDEO = os.path.join(CURRENT_DIR, "standalone_short_ai_letter_blindspot_raw_9x16.mp4")
RAW_AUDIO = os.path.join(CURRENT_DIR, "standalone_short_ai_letter_blindspot_audio.wav")

SCENES = [
    "01_00m00s_to_00m06s_hook_novel_vs_count.mp4",
    "02_00m06s_to_00m12s_strawberry_guesses.mp4",
    "03_00m12s_to_00m22s_token_blocks_split.mp4",
    "04_00m22s_to_00m31s_transformer_blackbox_seeds.mp4",
    "05_00m31s_to_00m39s_tokenizer_blindspot_comparison.mp4",
    "06_00m39s_to_00m43s_cta_which_mistake_next.mp4"
]

def assemble():
    print("🎬 Assembling scenes into raw 9:16 master cut...")
    with open(CONCAT_TXT, "w", encoding="utf-8") as f:
        for s in SCENES:
            f.write(f"file 'TIMELINE_MEDIA/{s}'\n")

    # 1. Assemble raw video + voiceover audio
    cmd_assemble = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", CONCAT_TXT,
        "-i", MASTER_AUDIO,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-r", "60",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        RAW_VIDEO
    ]
    subprocess.run(cmd_assemble, check=True)
    print(f"✅ Raw cut video created: {RAW_VIDEO}")

    # 2. Copy audio stem
    cmd_audio = [
        "ffmpeg", "-y",
        "-i", MASTER_AUDIO,
        "-ac", "2",
        "-ar", "44100",
        RAW_AUDIO
    ]
    subprocess.run(cmd_audio, check=True)
    print(f"✅ Audio stem created: {RAW_AUDIO}")

    if os.path.exists(CONCAT_TXT):
        os.remove(CONCAT_TXT)

    # 3. Generate preview frames for raw-cut review
    frame_times = [
        ("02s_hook", "00:00:02"),
        ("08s_guesses", "00:00:08"),
        ("17s_tokens", "00:00:17"),
        ("26s_blackbox", "00:00:26"),
        ("35s_blindspot", "00:00:35"),
        ("41s_cta", "00:00:41")
    ]
    for label, t in frame_times:
        out_frame = os.path.join(CURRENT_DIR, f"preview_frame_{label}.jpg")
        cmd_frame = [
            "ffmpeg", "-y",
            "-ss", t,
            "-i", RAW_VIDEO,
            "-vframes", "1",
            "-q:v", "2",
            out_frame
        ]
        subprocess.run(cmd_frame, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"📸 Preview frame saved: {os.path.basename(out_frame)}")

if __name__ == "__main__":
    assemble()
