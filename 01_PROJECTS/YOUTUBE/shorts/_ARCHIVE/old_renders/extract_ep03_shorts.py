import os
import sys
import json
import subprocess

MASTER_VIDEO = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\longs\3. [SCHEDULED 2026-09-16] long03_how_algorithms_decide\TIMELINE_MEDIA\MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4"
ALL_WORDS_PATH = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\longs\3. [SCHEDULED 2026-09-16] long03_how_algorithms_decide\02_assets_code\all_words.json"
SHORTS_ROOT = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\shorts"

CUTS = [
    {
        "slug": "ep03_short_algorithm_hook",
        "title": "The Algorithm Was Never Built to Inform You",
        "start_s": 8.10,
        "end_s": 42.0,
        "start_word_idx": 22,
        "end_word_idx": 98,
        "desc_hook": "It was never built to inform you. It was built to do exactly one thing: keep you watching. Here is how modern recommendation systems actually work.",
        "tags": "algorithm, youtube algorithm, recommendation system, tech documentary, quantrove, ai, shorts"
    },
    {
        "slug": "ep03_short_clicks_to_watchtime",
        "title": "Why Algorithms Stopped Optimizing for Clicks",
        "start_s": 127.90,
        "end_s": 167.6,
        "start_word_idx": 290,
        "end_word_idx": 367,
        "desc_hook": "For years, recommendation systems were built to maximize clicks. Then platforms noticed the clickbait crisis and made the single biggest change in modern algorithmic history: switching to watch time.",
        "tags": "watch time, clickbait, youtube algorithm, neural networks, machine learning, quantrove, shorts"
    },
    {
        "slug": "ep03_short_rabbit_hole",
        "title": "The Mathematical Architecture of the Rabbit Hole",
        "start_s": 216.70,
        "end_s": 260.35,
        "start_word_idx": 496,
        "end_word_idx": 600,
        "desc_hook": "When a recommendation engine is purely optimized for session length, it quietly narrows what you see, nudging toward more extreme content. Here is the mathematical mechanism behind the feed.",
        "tags": "rabbit hole, filter bubble, algorithm, recommendation engine, psychology of social media, quantrove, shorts"
    }
]

def format_srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def generate_srt(words, srt_path):
    chunks = []
    current_chunk = []
    for w in words:
        current_chunk.append(w)
        word_text = w["word"]
        # Strictly max 3 words per block, or break on punctuation or length for kinetic pop pacing
        if len(current_chunk) >= 3 or word_text.endswith((".", ",", "?", "!")) or (len(current_chunk) >= 2 and len(" ".join([x["word"] for x in current_chunk])) > 14):
            chunks.append(current_chunk)
            current_chunk = []
    if current_chunk:
        chunks.append(current_chunk)

    with open(srt_path, "w", encoding="utf-8") as f:
        for idx, chunk in enumerate(chunks, 1):
            start_t = format_srt_time(chunk[0]["start"])
            end_t = format_srt_time(chunk[-1]["end"])
            text = " ".join([x["word"] for x in chunk])
            f.write(f"{idx}\n{start_t} --> {end_t}\n{text}\n\n")

def process_short(cut):
    slug = cut["slug"]
    target_dir = os.path.join(SHORTS_ROOT, slug)
    os.makedirs(target_dir, exist_ok=True)

    start_s = cut["start_s"]
    end_s = cut["end_s"]
    duration = end_s - start_s

    out_video = os.path.join(target_dir, f"{slug}_raw_9x16.mp4")
    out_audio = os.path.join(target_dir, f"{slug}_audio.wav")
    out_words_json = os.path.join(target_dir, "exact_word_timestamps.json")
    out_srt = os.path.join(target_dir, f"{slug}_captions.srt")
    out_metadata = os.path.join(target_dir, "metadata.md")
    out_assembly = os.path.join(target_dir, "assembly_notes.md")

    print(f"\n=======================================================")
    print(f"🎬 Processing Short: {slug}")
    print(f"⏱️ In/Out: {start_s:.2f}s -> {end_s:.2f}s (Duration: {duration:.2f}s)")
    print(f"📁 Target: {target_dir}")
    print(f"=======================================================")

    # 1. Video 9:16 blur-pad reframe cut
    # Gaussian boxblur background + 1080px wide sharp foreground overlay
    filter_complex = (
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5[bg];"
        "[0:v]scale=1080:-1[fg];"
        "[bg][fg]overlay=(W-w)/2:(H-h)/2"
    )

    cmd_video = [
        "ffmpeg", "-y",
        "-ss", f"{start_s:.3f}",
        "-to", f"{end_s:.3f}",
        "-i", MASTER_VIDEO,
        "-filter_complex", filter_complex,
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-r", "60",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        out_video
    ]
    subprocess.run(cmd_video, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"✅ Rendered 9:16 video: {os.path.basename(out_video)} ({os.path.getsize(out_video)/1024/1024:.2f} MB)")

    # 2. Extract dedicated WAV audio
    cmd_audio = [
        "ffmpeg", "-y",
        "-ss", f"{start_s:.3f}",
        "-to", f"{end_s:.3f}",
        "-i", MASTER_VIDEO,
        "-vn",
        "-c:a", "pcm_s16le",
        "-ar", "44100",
        out_audio
    ]
    subprocess.run(cmd_audio, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"✅ Extracted WAV audio: {os.path.basename(out_audio)}")

    # 3. Extract and normalize word-level timestamps
    with open(ALL_WORDS_PATH, "r", encoding="utf-8") as f:
        full_data = json.load(f)

    raw_words = full_data["all_words"][cut["start_word_idx"]:cut["end_word_idx"]+1]
    norm_words = []
    for w in raw_words:
        norm_words.append({
            "word": w["word"],
            "start": round(max(0.0, w["start"] - start_s), 3),
            "end": round(max(0.0, w["end"] - start_s), 3),
            "orig_start": w["start"],
            "orig_end": w["end"]
        })

    with open(out_words_json, "w", encoding="utf-8") as f:
        json.dump({
            "slug": slug,
            "total_words": len(norm_words),
            "duration_s": duration,
            "source_range": {"start_s": start_s, "end_s": end_s},
            "words": norm_words
        }, f, indent=2)
    print(f"✅ Extracted word timestamps: {len(norm_words)} words")

    # 4. Generate SRT subtitles
    generate_srt(norm_words, out_srt)
    print(f"✅ Generated SRT captions: {os.path.basename(out_srt)}")

    # 5. Metadata
    with open(out_metadata, "w", encoding="utf-8") as f:
        f.write(f"""# YouTube Shorts Upload Metadata
## {cut['title']}

### 📺 1. Title
```text
{cut['title']} ⚡ #shorts
```

---

### 📝 2. Description
```text
{cut['desc_hook']}

Watch the full documentary breakdown on Quantrove: "How Does The Algorithm Actually Decide What You See?"

#YouTubeAlgorithm #AI #MachineLearning #TechDocumentary #Quantrove #Shorts
```

---

### 🏷️ 3. Tags
```text
{cut['tags']}
```

---

### 💬 4. Pinned Comment
```text
💬 Have you noticed your feed changing lately? What's your algorithm recommending? Watch the full breakdown in the related video!
```

---

### 🔗 5. Related Video Link (Funnel)
- **Parent Long-Form Video**: EP03 ("How Does The Algorithm Actually Decide What You See?")
- **Setting in YouTube Studio**: Under Video Details ➔ **Related video**, select **"How Does The Algorithm Actually Decide What You See?"**.
""")
    print(f"✅ Generated metadata.md")

    # 6. Assembly notes
    with open(out_assembly, "w", encoding="utf-8") as f:
        f.write(f"""# Shorts Assembly Notes: {slug}

## Timing & Master Reference
- **Source Master**: `long03_how_algorithms_decide/TIMELINE_MEDIA/MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4`
- **Clip In Timestamp**: `{start_s:.3f}s` ({format_srt_time(start_s)})
- **Clip Out Timestamp**: `{end_s:.3f}s` ({format_srt_time(end_s)})
- **Duration**: `{duration:.2f}s` (Under 60s Shorts ceiling)
- **Canvas Resolution**: `1080x1920` (9:16 Vertical)
- **Framerate**: 60.0 fps
- **Reframe Method**: 9:16 blur-pad (Boxblur 25 background + 1080px crisp foreground)

## Visual Style Standard Compliance (.claude/rules/visual-style-standard.md)
1. **Typography Hierarchy**:
   - Font: **Poppins Bold / Montserrat ExtraBold** (or Segoe UI / Arial Bold), UPPERCASE.
   - Weights: **Bold** for keywords, metrics, and titles; **Medium** for secondary body text. Never use weights lighter than medium.
2. **High-Contrast Text Box**:
   - Solid **`#FFEE00`** yellow fill box with `#000000` text, 12–14px border padding.
   - Accent colors: Neon cyan `#00F0FF` for key technical terms.
3. **Pacing & Animation**:
   - Caption animation: Pop-up / Bounce at 0.08s.
   - Kinetic pacing: Max 3 words per caption block. Visual change every 2–3 seconds; no static frame held >3-4s.
4. **Positioning**:
   - Center X, lower-third Y at approximately **1300px** on the 1920 canvas (clearing YouTube Shorts native right-side action buttons).

## Asset Files
- Video: `{slug}_raw_9x16.mp4`
- Audio: `{slug}_audio.wav` (44.1kHz stereo)
- Captions: `{slug}_captions.srt` (calibrated 2–3 word kinetic blocks)
- Word Timestamps: `exact_word_timestamps.json` (millisecond-accurate word-level sync)
""")
    print(f"✅ Generated assembly_notes.md")

def main():
    if not os.path.exists(MASTER_VIDEO):
        raise FileNotFoundError(f"Master video missing at: {MASTER_VIDEO}")

    for c in CUTS:
        process_short(c)

    print("\n🎉 ALL 3 SHORTS SUCCESSFULLY EXTRACTED FROM EP03 MASTER!")

if __name__ == "__main__":
    main()
