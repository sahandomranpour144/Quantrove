import json, re

with open("logs/polished_words.json", "r", encoding="utf-8") as f:
    words = json.load(f)

def srt_ts(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    if ms >= 1000:
        ms = 999
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

import sys
sys.path.append("logs")
from run_polished_dp import result_blocks

print(f"Loaded {len(result_blocks)} initial blocks.")

refined_blocks = []
i = 0
while i < len(result_blocks):
    b = result_blocks[i]
    b_text = " ".join(" ".join(b["lines"]).split())
    
    # 1. In the 90s and 2000s, Wall Street charged $10 or $20 / every time you hit trade.
    if b_text == "In the 90s and 2000s," and i + 1 < len(result_blocks) and "Wall Street charged" in " ".join(result_blocks[i+1]["lines"]):
        b_next = result_blocks[i+1]
        all_w = b["words"] + b_next["words"]
        card1_words = all_w[:11]
        card2_words = all_w[11:]
        refined_blocks.append({
            "start": card1_words[0]["start"],
            "end": card1_words[-1]["end"],
            "lines": ["In the 90s and 2000s,", "Wall Street charged $10 or $20"],
            "words": card1_words
        })
        refined_blocks.append({
            "start": card2_words[0]["start"],
            "end": card2_words[-1]["end"],
            "lines": ["every time you hit trade."],
            "words": card2_words
        })
        i += 2
        continue

    # 2. You might think: if I only lose a fraction... / does it really matter? Here is the math.
    if b_text == "You might think:" and i + 3 < len(result_blocks):
        b1 = b
        b2 = result_blocks[i+1]
        b3 = result_blocks[i+2]
        b4 = result_blocks[i+3]
        if "if I only lose" in " ".join(b2["lines"]) and "does it really matter?" in " ".join(b3["lines"]):
            card1_w = b1["words"] + b2["words"]
            card2_w = b3["words"] + b4["words"]
            refined_blocks.append({
                "start": card1_w[0]["start"],
                "end": card1_w[-1]["end"],
                "lines": ["You might think: if I only lose", "a fraction of a cent per share,"],
                "words": card1_w
            })
            refined_blocks.append({
                "start": card2_w[0]["start"],
                "end": card2_w[-1]["end"],
                "lines": ["does it really matter?", "Here is the math."],
                "words": card2_w
            })
            i += 4
            continue

    # 3. By law, brokers are supposed to provide...
    if b_text == "By law," and i + 1 < len(result_blocks) and "brokers are supposed" in " ".join(result_blocks[i+1]["lines"]):
        b_next = result_blocks[i+1]
        all_w = b["words"] + b_next["words"]
        refined_blocks.append({
            "start": all_w[0]["start"],
            "end": all_w[-1]["end"],
            "lines": ["By law, brokers are supposed to provide", "what is called best execution,"],
            "words": all_w
        })
        i += 2
        continue

    # 4. Independent audits
    if b_text == "Independent audits" and i + 2 < len(result_blocks):
        b0 = b
        b1 = result_blocks[i+1]
        b2 = result_blocks[i+2]
        all_w = b0["words"] + b1["words"] + b2["words"]
        c1 = all_w[:9]
        c2 = all_w[9:14]
        c3 = all_w[14:]
        refined_blocks.append({
            "start": c1[0]["start"],
            "end": c1[-1]["end"],
            "lines": ["Independent audits comparing order", "routing have repeatedly shown"],
            "words": c1
        })
        refined_blocks.append({
            "start": c2[0]["start"],
            "end": c2[-1]["end"],
            "lines": ["that orders routed", "to wholesale internalizers"],
            "words": c2
        })
        refined_blocks.append({
            "start": c3[0]["start"],
            "end": c3[-1]["end"],
            "lines": ["frequently miss out on"],
            "words": c3
        })
        i += 3
        continue

    # 5. They sell it to high-frequency...
    if b_text == "They" and i + 1 < len(result_blocks) and "sell it to high-frequency" in " ".join(result_blocks[i+1]["lines"]):
        b_next = result_blocks[i+1]
        all_w = b["words"] + b_next["words"]
        refined_blocks.append({
            "start": all_w[0]["start"],
            "end": all_w[-1]["end"],
            "lines": ["They sell it to high-frequency", "market makers who profit off the spread."],
            "words": all_w
        })
        i += 2
        continue

    refined_blocks.append(b)
    i += 1

print(f"Refined into {len(refined_blocks)} blocks.")

# Strict validation
for idx, b in enumerate(refined_blocks):
    assert len(b["lines"]) <= 2, f"Block {idx+1} has > 2 lines"
    for l in b["lines"]:
        assert len(l) <= 42, f"Block {idx+1} line exceeds 42 chars: {l} ({len(l)} chars)"
    assert b["start"] < b["end"], f"Block {idx+1} has invalid duration"
    if idx > 0:
        prev_end = refined_blocks[idx-1]["end"]
        assert b["start"] >= prev_end - 0.001, f"Overlap at block {idx+1}"

print("All blocks PASSED strict validation!")

with open("logs/final_blocks.json", "w", encoding="utf-8") as f:
    json.dump(refined_blocks, f, indent=2, ensure_ascii=False)
