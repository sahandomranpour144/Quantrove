import json

with open("logs/mp4_whisper_raw.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print(f"Total segments: {len(d['segments'])}")
for i, s in enumerate(d['segments']):
    text = s['text']
    dur = s['end'] - s['start']
    n_words = len(s['words'])
    if len(text) > 42 or dur > 4.0:
        print(f"Seg {i+1:2d} [{s['start']:6.2f}-{s['end']:6.2f}] ({dur:4.1f}s, {len(text):2d} chars, {n_words:2d} words): {text}")
