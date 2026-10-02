import os
import sys
import json
import asyncio
import subprocess
import datetime
import edge_tts

BASE_DIR = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\pipeline"
PROJECT_ROOT = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE"
SHORTS_DIR = os.path.join(PROJECT_ROOT, "shorts")
REMOTION_DIR = os.path.join(BASE_DIR, "remotion_engine")
PUBLIC_DIR = os.path.join(REMOTION_DIR, "public")
QUEUE_FILE = os.path.join(BASE_DIR, "batch_queue.json")

os.makedirs(PUBLIC_DIR, exist_ok=True)
os.makedirs(SHORTS_DIR, exist_ok=True)

def find_browser():
    for p in [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]:
        if os.path.exists(p): return p
    return None

def resolve_short_dir(slug):
    if os.path.exists(SHORTS_DIR):
        for entry in os.listdir(SHORTS_DIR):
            entry_path = os.path.join(SHORTS_DIR, entry)
            if os.path.isdir(entry_path):
                if entry == slug or entry.endswith(f" {slug}") or entry == f"[IN_PROGRESS] {slug}":
                    return entry_path
    return os.path.join(SHORTS_DIR, slug)

def normalize(w):
    return "".join(c for c in w.lower() if c.isalnum())

def find_word_index(words_norm, phrase, search_from, label):
    phrase_words = [normalize(w) for w in phrase.split() if normalize(w)]
    if not phrase_words:
        print(f"    [WARN] '{label}': empty segment_text, using fallback position")
        return search_from, False
    first = phrase_words[0]
    for i in range(search_from, len(words_norm)):
        if words_norm[i] == first:
            return i, True
    print(f"    [WARN] '{label}': phrase '{phrase}' NOT FOUND from position {search_from} onward — using fallback.")
    return search_from, False

def build_scenes(scene_segments, cta, words, total_audio_time):
    words_norm = [normalize(w["word"]) for w in words]
    print(f"  [DEBUG] TTS captured {len(words)} word timestamps for matching.")
    starts = []
    search_from = 0
    for seg in scene_segments:
        idx, found = find_word_index(words_norm, seg["segment_text"], search_from, seg.get("headline", "?"))
        start_sec = words[idx]["start"] if words else 0.0
        status = "OK" if found else "FALLBACK"
        print(f"    [{status}] '{seg.get('headline','?')}' -> '{seg['segment_text']}' -> {start_sec:.2f}s")
        starts.append(start_sec)
        search_from = idx + 1

    cta_duration = cta.get("duration", 3.0)
    last_content_start = starts[-1] if starts else 0.0
    cta_start = max(total_audio_time - cta_duration, last_content_start + 1.0)
    boundaries = starts + [cta_start]

    scenes = []
    for i, seg in enumerate(scene_segments):
        scenes.append({
            "id": i + 1,
            "startSec": round(boundaries[i], 2),
            "endSec": round(boundaries[i + 1], 2),
            "badge": seg["badge"], "headline": seg["headline"], "subtext": seg["subtext"],
            "accentColor": seg["accentColor"], "type": seg["type"],
        })
    scenes.append({
        "id": len(scene_segments) + 1,
        "startSec": round(cta_start, 2),
        "endSec": round(total_audio_time + 2.5, 2),
        "badge": cta.get("badge", "⚡ FOLLOW FOR PART 2"),
        "headline": cta.get("headline", "SUBSCRIBE FOR DAILY BREAKDOWNS"),
        "subtext": cta.get("subtext", "Drop your thoughts in the comments."),
        "accentColor": cta.get("accentColor", "#00ff88"),
        "type": "cta",
    })
    return scenes

async def render_single_episode(ep_data, browser_path, force=False, style=None, overlay_only=False):
    slug = ep_data["slug"]
    title = ep_data["title"]
    stat = ep_data["stat_callout"]
    script = ep_data["script"]
    voice = ep_data.get("voice", "en-US-GuyNeural")
    scene_segments = ep_data.get("scene_segments")
    cta = ep_data.get("cta", {})

    ep_dir = resolve_short_dir(slug)
    output_mp4 = os.path.join(ep_dir, f"{slug}.mp4")
    output_target = os.path.join(ep_dir, f"{slug}_overlay_alpha.mov") if overlay_only else output_mp4
    uploaded_marker = os.path.join(ep_dir, "UPLOADED.md")

    if os.path.exists(uploaded_marker):
        print(f"[SKIP] '{slug}' already marked UPLOADED — not touching it.")
        return
    if os.path.exists(output_target) and not (force or ep_data.get("force_rerender", False)):
        print(f"[SKIP] '{slug}' already has a rendered video. Add \"force_rerender\": true "
              f"in batch_queue.json or use --force to re-render it.")
        return

    if not scene_segments:
        raise ValueError(f"[!] Episode '{slug}' has no 'scene_segments' in batch_queue.json.")

    os.makedirs(ep_dir, exist_ok=True)

    audio_output = os.path.join(PUBLIC_DIR, "voiceover.mp3")
    print(f"\n--- [1/3] Generating Audio & Subtitles: {title} ---")

    words = []
    comm = edge_tts.Communicate(script, voice, boundary="WordBoundary")
    with open(audio_output, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append({
                    "word": chunk["text"],
                    "start": chunk["offset"] / 10_000_000,
                    "end": (chunk["offset"] + chunk["duration"]) / 10_000_000
                })

    final_audio_time = (words[-1]["end"] + 2.0) if words else 30.0
    fps = 60 if overlay_only else 30
    total_frames = int((final_audio_time + 1.5) * fps)

    print(f"--- [DEBUG] Matching {len(scene_segments)} scenes against script audio ---")
    scenes = build_scenes(scene_segments, cta, words, final_audio_time)

    props = {
        "title": title, "statCallout": stat, "audioFileName": "voiceover.mp3",
        "words": words, "scenes": scenes,
    }
    if overlay_only:
        props["overlayOnly"] = True
    style_val = style or ep_data.get("style")
    if style_val:
        props["style"] = style_val
        if style_val == "shorts_v2":
            try:
                from text_layer.generate_text_events import generate_text_events, DEFAULT_STYLE_PATH
                if os.path.exists(DEFAULT_STYLE_PATH):
                    with open(DEFAULT_STYLE_PATH, "r", encoding="utf-8") as sf:
                        style_cfg = json.load(sf)
                    props["textEvents"] = generate_text_events(words, style_cfg, scenes)
            except Exception as e:
                print(f"  [WARN] Could not pre-generate text_events: {e}")
    props_path = os.path.join(PUBLIC_DIR, "input_props.json")
    with open(props_path, "w", encoding="utf-8") as pf:
        json.dump(props, pf, indent=2)

    meta_path = os.path.join(ep_dir, "metadata.md")
    with open(meta_path, "w", encoding="utf-8") as mf:
        mf.write(f"# YouTube Shorts Metadata\n\n")
        mf.write(f"**Title:** {ep_data.get('yt_title', title)} #shorts #tech #business\n")
        mf.write(f"**Description:** {ep_data.get('yt_desc', script[:150])} Subscribe for daily business breakdowns.\n")
        mf.write(f"**Pinned Comment:** {ep_data.get('yt_comment', 'What do you think about this move? Let us know below!')}\n\n")
        mf.write(f"## Full Script\n{script}\n")

    print(f"--- [2/3] Rendering Video ({total_frames} frames @ {fps}fps / {final_audio_time:.1f}s) [overlayOnly={overlay_only}] ---")
    comp_id = "ShortVideoOverlay60fps" if overlay_only else "ShortVideo"
    cmd = [
        "npx.cmd", "remotion", "render", comp_id, output_target,
        f"--props={props_path}", f"--frames=0-{total_frames - 1}", "--concurrency=2"
    ]
    if overlay_only:
        cmd.extend(["--image-format=png", "--pixel-format=yuva444p10le", "--codec=prores", "--prores-profile=4444"])
    if browser_path: cmd.append(f"--browser-executable={browser_path}")
    subprocess.run(cmd, cwd=REMOTION_DIR, check=True)
    print(f"--- [3/3] [COMPLETED] Episode saved at: {output_target} ---")

async def main():
    if not os.path.exists(QUEUE_FILE):
        print(f"[!] No queue file found at {QUEUE_FILE}")
        return
    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        queue = json.load(f)
    browser = find_browser()
    force = "--force" in sys.argv
    overlay_only = "--overlay-only" in sys.argv
    style = None
    if "--style" in sys.argv:
        try:
            s_idx = sys.argv.index("--style")
            if s_idx + 1 < len(sys.argv):
                style = sys.argv[s_idx + 1]
        except Exception:
            pass
    print(f"[+] Starting batch render of {len(queue)} episodes (force={force}, style={style}, overlay_only={overlay_only}) using browser: {browser}")
    for ep in queue:
        await render_single_episode(ep, browser, force=force, style=style, overlay_only=overlay_only)
    print("\n[DONE] Batch complete.")

if __name__ == "__main__":
    asyncio.run(main())