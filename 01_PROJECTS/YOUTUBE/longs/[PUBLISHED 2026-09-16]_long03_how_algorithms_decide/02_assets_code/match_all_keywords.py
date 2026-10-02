import os, json, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "all_words.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

all_words = data["all_words"]
print(f"Loaded {len(all_words)} words.")

def find_phrase(words, search_phrase, min_time=0.0):
    search_tokens = [w.lower().strip(".,:;!?'\"-") for w in search_phrase.split()]
    n = len(search_tokens)
    for i in range(len(words) - n + 1):
        if words[i]["start"] < min_time:
            continue
        window_tokens = [words[i+j]["word"].lower().strip(".,:;!?'\"-") for j in range(n)]
        if window_tokens == search_tokens:
            start_t = words[i]["start"]
            end_t = words[i+n-1]["end"]
            return {"text": search_phrase.upper(), "start": round(start_t, 2), "end": round(end_t, 2)}
        # Fuzzy match start
        if window_tokens[0].startswith(search_tokens[0][:4]):
            match = True
            for j in range(1, n):
                if not window_tokens[j].startswith(search_tokens[j][:3]):
                    match = False
                    break
            if match:
                start_t = words[i]["start"]
                end_t = words[i+n-1]["end"]
                return {"text": search_phrase.upper(), "start": round(start_t, 2), "end": round(end_t, 2)}
    return None

curated_phrases = [
    # Scene 1 (0.00 - 42.04)
    ("system", 0.0),
    ("interact", 1.0),
    ("human being", 4.0),
    ("never built", 8.0),
    ("keep you watching", 12.0),
    ("frighteningly good", 15.0),
    ("always wrong", 20.0),
    ("actually optimizing", 25.0),
    ("wildly different", 30.0),
    ("real mechanism", 35.0),
    ("every platform", 38.0),
    
    # Scene 2 (42.04 - 82.32)
    ("most people", 42.0),
    ("popular", 47.0),
    ("trending", 50.0),
    ("actually happening", 52.0),
    ("same moment", 56.0),
    ("do not", 60.0),
    ("two people", 62.0),
    ("different feeds", 66.0),
    ("different signals", 69.0),
    ("prediction system", 74.0),
    ("specifically", 77.0),
    
    # Scene 3 (82.32 - 122.72)
    ("research", 83.0),
    ("two-stage", 85.0),
    ("candidate generation", 92.0),
    ("millions", 95.0),
    ("few hundred", 100.0),
    ("watch history", 103.0),
    ("ranking", 108.0),
    ("scores every", 111.0),
    ("objectively", 115.0),
    ("keep you", 118.0),
    
    # Scene 4 (122.72 - 167.76)
    ("nobody", 123.0),
    ("maximize clicks", 129.0),
    ("misleading", 134.0),
    ("clicked more", 138.0),
    ("changed the target", 142.0),
    ("watch time", 146.0),
    ("keep watching", 153.0),
    ("single change", 157.0),
    ("your feed", 163.0),
    
    # Scene 5 (167.76 - 212.24)
    ("exact same", 168.0),
    ("differently", 172.0),
    ("prediction target", 177.0),
    ("documentaries", 182.0),
    ("watch it fully", 186.0),
    ("identical video", 190.0),
    ("short clips", 193.0),
    ("seconds", 197.0),
    ("two creators", 201.0),
    ("specific outcome", 207.0),
    
    # Scene 6 (212.24 - 260.40)
    ("scrutiny", 214.0),
    ("narrow", 221.0),
    ("extreme", 226.0),
    ("not a secret", 232.0),
    ("actively reshape", 242.0),
    ("paranoia", 246.0),
    ("deliberately", 251.0),
    
    # Scene 7 (260.40 - 318.60)
    ("actually change", 261.0),
    ("individual prediction", 267.0),
    ("attention", 274.0),
    ("accuracy", 277.0),
    ("different signals", 285.0),
    ("different feed", 289.0),
    ("markets crash", 293.0),
    ("next breakdown", 303.0),
    ("quantrove", 312.0),
]

matched = []
for phrase, t_min in curated_phrases:
    res = find_phrase(all_words, phrase, t_min)
    if res:
        print(f"MATCH: {phrase:30s} -> {res['start']:6.2f}s - {res['end']:6.2f}s ({res['text']})")
        matched.append(res)
    else:
        print(f"MISS:  {phrase:30s} at t >= {t_min}")

print(f"\nTotal matched: {len(matched)} / {len(curated_phrases)}")
