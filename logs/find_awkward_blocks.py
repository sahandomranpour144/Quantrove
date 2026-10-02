import json

with open("logs/polished_dp_blocks.json", "r", encoding="utf-8") as f:
    blocks = json.load(f)

for i, b in enumerate(blocks):
    n_words = len(b["words"])
    dur = b["end"] - b["start"]
    text = " ".join(b["lines"])
    if n_words <= 2 or dur < 1.2:
        print(f"Block {i+1:2d} [{b['start']:6.2f}-{b['end']:6.2f}] ({dur:4.2f}s, {n_words}w): {text}")
