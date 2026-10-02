import os, json

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, "all_words.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data["all_segments"]:
    print(f"[{s['start']:6.2f} - {s['end']:6.2f}] {s['text']}")
