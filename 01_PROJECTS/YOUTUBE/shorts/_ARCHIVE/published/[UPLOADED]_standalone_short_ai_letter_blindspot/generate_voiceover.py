import os
import re
import json
import subprocess
from google import genai
from google.genai import types
from faster_whisper import WhisperModel

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.join(CURRENT_DIR, "TIMELINE_MEDIA")
os.makedirs(TIMELINE_DIR, exist_ok=True)

RAW_PCM = os.path.join(CURRENT_DIR, "temp_voiceover_raw.pcm")
MASTER_WAV = os.path.join(TIMELINE_DIR, "00_VOICEOVER_master.wav")
WORD_TIMESTAMPS_JSON = os.path.join(CURRENT_DIR, "exact_word_timestamps.json")
SRT_PATH = os.path.join(CURRENT_DIR, "ai_letter_blindspot_captions.srt")

NARRATION_TEXT = (
    "AI can write you a full essay in two seconds. "
    "But ask it how many R's are in strawberry, and it might just guess wrong. "
    "Try it yourself right now. It's not bad at counting. It literally can't see the letters. "
    "AI doesn't read letter by letter like you do. It breaks words into chunks called tokens. "
    "Strawberry isn't ten letters to it—it's two blocks it's seen a million times. "
    "So when you ask it to count letters inside those chunks, it's not counting. "
    "It's guessing—like guessing how many seeds are in a watermelon without cutting it open. "
    "It's not lying to you. It genuinely can't see what you're asking for. "
    "And that one blind spot explains half of AI's weirdest mistakes. "
    "Follow for more of the tricks hiding inside the AI you use every day."
)

def generate_voiceover():
    print("🎙️ Generating voiceover using Gemini TTS (gemini-2.5-flash-preview-tts, Voice: Fenrir)...")
    client = genai.Client()
    config = types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Fenrir")
            )
        )
    )

    prompt = (
        "Read this documentary script with authoritative, engaging, pacing suitable for a high-retention tech breakdown:\n\n"
        f"{NARRATION_TEXT}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=prompt,
        config=config,
    )

    part = response.candidates[0].content.parts[0]
    with open(RAW_PCM, "wb") as f:
        f.write(part.inline_data.data)

    print(f"✅ Raw PCM bytes: {len(part.inline_data.data)}")

    # Convert 24kHz raw PCM to standard WAV via ffmpeg at natural energetic pace (atempo=1.23 -> ~38.8s)
    cmd = [
        "ffmpeg", "-y",
        "-f", "s16le",
        "-ar", "24000",
        "-ac", "1",
        "-i", RAW_PCM,
        "-filter:a", "atempo=1.23",
        "-ar", "44100",
        "-ac", "2",
        MASTER_WAV
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(RAW_PCM):
        os.remove(RAW_PCM)

    print(f"✅ Master WAV created: {MASTER_WAV}")

def format_timestamp_srt(seconds):
    millis = int((seconds - int(seconds)) * 1000)
    secs = int(seconds) % 60
    mins = (int(seconds) // 60) % 60
    hours = int(seconds) // 3600
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

def transcribe_and_align():
    print("🔍 Aligning words and generating timestamps with Faster-Whisper...")
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(MASTER_WAV, word_timestamps=True, language="en")

    words_list = []
    all_words = []

    for seg in segments:
        for w in seg.words:
            clean = w.word.strip()
            all_words.append({
                "word": clean,
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "probability": round(w.probability, 3)
            })

    # Group into max 3 words per block for kinetic SRT
    chunks = []
    current_chunk = []
    for w in all_words:
        current_chunk.append(w)
        word_text = w["word"]
        if len(current_chunk) >= 3 or word_text.endswith((".", ",", "?", "!")) or (len(current_chunk) >= 2 and len(" ".join([x["word"] for x in current_chunk])) > 14):
            chunks.append(current_chunk)
            current_chunk = []
    if current_chunk:
        chunks.append(current_chunk)

    srt_lines = []
    for idx, chunk in enumerate(chunks, 1):
        start_t = format_timestamp_srt(chunk[0]["start"])
        end_t = format_timestamp_srt(chunk[-1]["end"])
        text = " ".join([x["word"] for x in chunk])
        srt_lines.append(f"{idx}\n{start_t} --> {end_t}\n{text}\n")

    with open(SRT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    payload = {
        "slug": "standalone_short_ai_letter_blindspot",
        "audio_file": MASTER_WAV,
        "duration": round(info.duration, 3),
        "language": info.language,
        "total_words": len(all_words),
        "words": all_words
    }
    with open(WORD_TIMESTAMPS_JSON, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"✅ Extracted {len(all_words)} words spanning {info.duration:.2f}s.")
    print(f"✅ Saved word timestamps: {WORD_TIMESTAMPS_JSON}")
    print(f"✅ Saved SRT captions: {SRT_PATH}")

if __name__ == "__main__":
    generate_voiceover()
    transcribe_and_align()
