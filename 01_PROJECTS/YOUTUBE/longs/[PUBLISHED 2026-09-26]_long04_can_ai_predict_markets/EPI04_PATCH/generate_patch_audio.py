#!/usr/bin/env python3
"""
Generate EP04 Patch Audio Segments
Generates 4 replacement voiceover clips using Gemini TTS (Orus voice) with identical system context.
Measures durations, adjusts pacing/pauses to hit old_duration +/-0.5s (#4 <= 20.2s),
transcribes word timestamps via faster-whisper, and updates patch_map.json.
"""

import os
import sys
import wave
import json
import subprocess
import time
from google import genai
from google.genai import types
from faster_whisper import WhisperModel

PATCH_DIR = os.path.dirname(os.path.abspath(__file__))

SYSTEM_CONTEXT = (
    "Scene: A sleek, dark technology studio. The narrator is a calm, analytical, "
    "authoritative voice -- the voice of someone who understands complex systems deeply "
    "and explains them with precision, clarity, and intellectual weight. Deliberate pacing, "
    "no dramatic exaggeration, measured intelligence. Channel: Quantrove."
)

SEGMENTS_CONFIG = [
    {
        "id": 1,
        "filename": "segment_1_intro.wav",
        "words_filename": "segment_1_words.json",
        "target_dur": 34.86,
        "max_dur": 35.36,
        "min_dur": 34.36,
        "text": (
            "Can AI actually predict the stock market? That's what you clicked to find out. "
            "The honest answer is mostly no, but the reason is not what most people think.\n\n"
            "Get comfortable. This one is worth going slowly.\n\n"
            "It starts in 1988, when Jim Simons launched the Medallion Fund, and for three decades "
            "it averaged about sixty-six percent a year before fees. He hired physicists, mathematicians, "
            "and computer scientists, and deliberately avoided Wall Street traders."
        )
    },
    {
        "id": 2,
        "filename": "segment_2_mercer.wav",
        "words_filename": "segment_2_words.json",
        "target_dur": 9.82,
        "max_dur": 10.32,
        "min_dur": 9.32,
        "text": (
            "In reality, Renaissance co-CEO Robert Mercer reportedly said the fund was right only "
            "about fifty point seven five percent of the time."
        )
    },
    {
        "id": 3,
        "filename": "segment_3_noise.wav",
        "words_filename": "segment_3_words.json",
        "target_dur": 3.96,
        "max_dur": 4.46,
        "min_dur": 3.46,
        "text": "Most of any day's price movement is pure noise."
    },
    {
        "id": 4,
        "filename": "segment_4_cta.wav",
        "words_filename": "segment_4_words.json",
        "target_dur": 20.0,
        "max_dur": 20.20,
        "min_dur": 19.0,
        "text": (
            "If this changed how you see AI and markets, watch this next: how YouTube's "
            "recommendation algorithm actually works, the system that put this video in front of you. "
            "And if you want real data and mathematics without the hype, subscribe to Quantrove."
        )
    }
]

def save_pcm_to_wav(pcm_bytes, wav_path, sample_rate=24000, channels=1, sampwidth=2):
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_bytes)

def probe_duration(path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(res.stdout.strip())

def adjust_duration(in_wav, out_wav, target_dur, max_dur, min_dur):
    current_dur = probe_duration(in_wav)
    print(f"    Raw duration: {current_dur:.3f}s (target: {target_dur:.2f}s, bounds: [{min_dur:.2f}, {max_dur:.2f}])")

    # If within tolerance, just copy/normalize
    if min_dur <= current_dur <= max_dur:
        subprocess.run(f'ffmpeg -y -i "{in_wav}" -ar 24000 -ac 1 "{out_wav}"', shell=True, check=True)
        return probe_duration(out_wav)

    # If needs adjustment, calculate tempo factor
    ratio = current_dur / target_dur
    # If ratio is close (e.g. 0.8 to 1.25), use atempo filter to adjust pace slightly without changing pitch or words
    print(f"    Adjusting duration via atempo filter (ratio: {ratio:.3f})...")
    tempo = max(0.75, min(1.35, ratio))
    cmd = f'ffmpeg -y -i "{in_wav}" -filter:a "atempo={tempo}" -ar 24000 -ac 1 "{out_wav}"'
    subprocess.run(cmd, shell=True, check=True)
    final_dur = probe_duration(out_wav)

    # If still slightly off or need exact tail trim/pad
    if final_dur > max_dur:
        # Pad/trim to exact max_dur
        trim_wav = out_wav + ".trimmed.wav"
        subprocess.run(f'ffmpeg -y -i "{out_wav}" -t {max_dur - 0.05} -ar 24000 -ac 1 "{trim_wav}"', shell=True, check=True)
        os.replace(trim_wav, out_wav)
        final_dur = probe_duration(out_wav)
    elif final_dur < min_dur:
        # Pad with silence at the end
        pad_s = min_dur + 0.1 - final_dur
        pad_wav = out_wav + ".padded.wav"
        subprocess.run(f'ffmpeg -y -i "{out_wav}" -af "apad=pad_dur={pad_s}" -ar 24000 -ac 1 "{pad_wav}"', shell=True, check=True)
        os.replace(pad_wav, out_wav)
        final_dur = probe_duration(out_wav)

    print(f"    Final adjusted duration: {final_dur:.3f}s")
    return final_dur

def transcribe_words(wav_path, output_json, model):
    print(f"    Transcribing word timestamps with faster-whisper...")
    segments, info = model.transcribe(wav_path, beam_size=5, word_timestamps=True, language="en")
    all_words = []
    for s in segments:
        for w in s.words:
            all_words.append({
                "word": w.word.strip(),
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "probability": round(w.probability, 3)
            })
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump({"total_words": len(all_words), "words": all_words}, f, indent=2)
    print(f"    Captured {len(all_words)} words -> {os.path.basename(output_json)}")
    return all_words

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY not found in environment.", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    whisper_model = WhisperModel("base", device="cpu", compute_type="int8")

    patch_map_file = os.path.join(PATCH_DIR, "patch_map.json")
    with open(patch_map_file, "r", encoding="utf-8") as f:
        patch_map = json.load(f)

    for cfg in SEGMENTS_CONFIG:
        seg_id = cfg["id"]
        print(f"\n--- Generating Segment #{seg_id}: {cfg['filename']} ---")
        prompt = f"{SYSTEM_CONTEXT}\n\nRead the following script verbatim with clear, deliberate articulation:\n\n{cfg['text']}"
        raw_wav = os.path.join(PATCH_DIR, f"raw_{cfg['filename']}")
        final_wav = os.path.join(PATCH_DIR, cfg["filename"])
        words_json = os.path.join(PATCH_DIR, cfg["words_filename"])

        # 1. Call Gemini TTS
        audio_bytes = None
        for attempt in range(4):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash-preview-tts",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["AUDIO"],
                        speech_config=types.SpeechConfig(
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Orus")
                            )
                        ),
                    ),
                )
                for part in response.candidates[0].content.parts:
                    if part.inline_data and part.inline_data.data:
                        audio_bytes = part.inline_data.data
                        break
                if audio_bytes:
                    break
            except Exception as e:
                print(f"  Attempt {attempt+1} failed: {e}. Retrying in 2s...")
                time.sleep(2)

        if not audio_bytes:
            print(f"[ERROR] Failed to generate audio for segment #{seg_id}", file=sys.stderr)
            sys.exit(1)

        save_pcm_to_wav(audio_bytes, raw_wav)

        # 2. Adjust duration to match target bounds
        new_dur = adjust_duration(raw_wav, final_wav, cfg["target_dur"], cfg["max_dur"], cfg["min_dur"])

        # 3. Transcribe with faster-whisper
        transcribe_words(final_wav, words_json, whisper_model)

        # 4. Clean raw temp file
        if os.path.exists(raw_wav):
            os.remove(raw_wav)

        # 5. Update patch_map
        for p in patch_map:
            if p["id"] == seg_id:
                p["new_duration"] = round(new_dur, 3)
                p["diff_s"] = round(new_dur - p["old_duration"], 3)

    # Save updated patch_map.json
    with open(patch_map_file, "w", encoding="utf-8") as f:
        json.dump(patch_map, f, indent=2)
    print("\n[+] All 4 patch audio segments generated, transcribed, and patch_map.json updated!")

if __name__ == "__main__":
    main()
