import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "all_words.json"), "r", encoding="utf-8") as f:
    words = json.load(f)["all_words"]

windows = [(80.0, 110.0), (185.0, 205.0), (288.0, 305.0)]
for w1, w2 in windows:
    print(f"\n--- WINDOW {w1} to {w2} ---")
    phrase = " ".join([w["word"] for w in words if w1 <= w["start"] <= w2])
    print(phrase)
    for w in words:
        if w1 <= w["start"] <= w2:
            print(f"  {w['start']:6.2f}s - {w['end']:6.2f}s: {w['word']}")
