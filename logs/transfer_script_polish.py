import json, re, difflib

with open("01_PROJECTS/YOUTUBE/longs/[REBUILD]_long05_market_making_illusion/01_scripts/EP05_SCRIPT.md", "r", encoding="utf-8") as f:
    script_raw = f.read()

vo_matches = re.findall(r'\*\*VO\*\*:\s*\"(.*?)\"', script_raw, re.DOTALL)
full_script = " ".join(" ".join(m.split()) for m in vo_matches)
script_words = full_script.split()

with open("logs/fixed_words.json", "r", encoding="utf-8") as f:
    clean_words = json.load(f)

def norm(w):
    return re.sub(r'[^\w]', '', w).lower()

s_norm = [norm(w) for w in script_words]
w_norm = [norm(w["word"]) for w in clean_words]

matcher = difflib.SequenceMatcher(None, s_norm, w_norm)
opcodes = matcher.get_opcodes()

polished_words = []
for tag, i1, i2, j1, j2 in opcodes:
    s_slice = script_words[i1:i2]
    w_slice = clean_words[j1:j2]
    
    if tag == 'equal':
        # 1-to-1 word alignment! Transfer exact script capitalization and punctuation
        for s_w, w_w in zip(s_slice, w_slice):
            polished_words.append({
                "word": s_w,
                "start": w_w["start"],
                "end": w_w["end"]
            })
    elif tag == 'delete':
        # Word in script but not in whisper (e.g. em-dash '—' or 'dollars')
        # If it's punctuation like '—', attach to previous word
        if s_slice and s_slice[0] == '—' and polished_words:
            if not polished_words[-1]["word"].endswith("—"):
                polished_words[-1]["word"] += " —"
        # If words like 'dollars', ignore since whisper combined them into '$20' or '$200 million'
    elif tag == 'replace':
        # E.g. 'nineties and two-thousands,' <---> '90s and 2000s,'
        # E.g. 'ten' <---> '$10'
        # E.g. 'twenty dollars' <---> '$20'
        # E.g. 'two hundred million dollars' <---> '$200 million'
        # E.g. 'sixty-five million dollar' <---> '$65 million'
        # E.g. 'one hundred' <---> '100'
        # E.g. 'two' <---> '2'
        # E.g. 'two dollars' <---> '$2'
        # E.g. 'PFOF.' <---> 'PFOF.'
        # Keep whisper's concise representation, but ensure punctuation matches script
        # Check last word of s_slice for punctuation
        last_s = s_slice[-1]
        last_punct = ""
        for p in [',', '.', '?', '!', ':', ';', '—']:
            if last_s.endswith(p):
                last_punct = p
                break
        
        for idx, w_w in enumerate(w_slice):
            w_text = w_w["word"]
            if idx == len(w_slice) - 1 and last_punct:
                # remove any trailing punct and attach script's punct
                w_text = re.sub(r'[,.\?!:;—]+$', '', w_text) + last_punct
            polished_words.append({
                "word": w_text,
                "start": w_w["start"],
                "end": w_w["end"]
            })

print(f"Total polished words: {len(polished_words)}")
with open("logs/polished_words.json", "w", encoding="utf-8") as f:
    json.dump(polished_words, f, indent=2, ensure_ascii=False)

print("First 20 polished words:")
for w in polished_words[:20]:
    print(f"  [{w['start']:6.2f} - {w['end']:6.2f}] {w['word']}")
