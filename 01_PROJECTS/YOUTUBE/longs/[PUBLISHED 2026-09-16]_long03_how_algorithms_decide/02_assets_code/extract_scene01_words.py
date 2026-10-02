import os, json
from faster_whisper import WhisperModel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_PATH = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA", "01_AUDIO_00m00s_to_00m42s_Scene_01_hook_voiceover.mp3"))
OUT_JSON = os.path.join(BASE_DIR, "scene01_words.json")

print(f"Transcribing {AUDIO_PATH}...")
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(AUDIO_PATH, word_timestamps=True)

words = []
for segment in segments:
    for w in segment.words:
        cleaned = w.word.strip()
        words.append({
            "word": cleaned,
            "start": round(w.start, 3),
            "end": round(w.end, 3),
            "probability": round(w.probability, 3)
        })

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(words, f, indent=2)

print(f"Saved {len(words)} words to {OUT_JSON}")
