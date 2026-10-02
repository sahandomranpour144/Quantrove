"""
EP03 Master Audio Word-Level Timestamp Extraction
Runs faster-whisper on the full master voiceover to extract globally-timed word-level timestamps.
Output: all_words.json — every word with absolute timing from 00:00 through 05:18.60
Run: python extract_all_words.py
"""
import os, json
from faster_whisper import WhisperModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA",
    "00_AUDIO_00m00s_to_05m19s_full_voiceover_ep03_orus.mp3"))
OUT_JSON = os.path.join(BASE_DIR, "all_words.json")

print(f"Transcribing master audio: {AUDIO_PATH}...")
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(
    AUDIO_PATH,
    beam_size=5,
    word_timestamps=True,
    language="en",
)

all_words = []
all_segments = []

for s in segments:
    seg_data = {
        "start": round(s.start, 3),
        "end": round(s.end, 3),
        "text": s.text.strip(),
    }
    all_segments.append(seg_data)
    if s.words:
        for w in s.words:
            all_words.append({
                "word": w.word.strip(),
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "probability": round(w.probability, 3),
            })
    print(f"[{s.start:6.2f} - {s.end:6.2f}] {s.text.strip()}")

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump({
        "total_words": len(all_words),
        "audio_file": os.path.basename(AUDIO_PATH),
        "total_duration_s": 318.6,
        "all_words": all_words,
        "all_segments": all_segments,
    }, f, indent=2, ensure_ascii=False)

print(f"\nSaved {len(all_words)} words to {OUT_JSON}")
print(f"Segments: {len(all_segments)}")
