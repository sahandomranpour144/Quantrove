import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, "all_words.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

words = data["all_words"]

test_phrases = [
    # Scene 1: Hook & Simons Paradox (0:00 - 1:06.81)
    "1988", "Jim Simons", "mathematician", "sixty-six percent", "forty-two million",
    "strict rule", "banned", "finance background", "spend billions", "neural networks",
    "fifty-one percent", "real mathematics", "cannot predict",
    
    # Scene 2: 50.75% Edge & Reflexivity (1:06.81 - 2:29.46)
    "great illusion", "ninety percent", "microscopic", "fifty point seventy-five percent",
    "law of large numbers", "millions of micro-trades", "generative ai",
    "react to being predicted", "reflexivity", "cat photo", "zero-sum",
    "buying pressure", "erases the pattern", "self-destructs",
    
    # Scene 3: Alpha Decay (2:29.46 - 3:21.55)
    "alpha decay", "excess return", "statistical edge", "expiring patent",
    "anomaly", "high-frequency", "volume spikes", "crowd the trade",
    "equilibrium", "backtest", "four months", "market adapted",
    
    # Scene 4: Overfitting Trap (3:21.55 - 4:33.60)
    "fatal flaw", "overfitting trap", "memorizes historical noise",
    "repeatable law", "pure noise", "billions of parameters", "noisy price data",
    "guarantees", "straight line", "real capital", "evaporates",
    
    # Scene 5: The 4 Real Engines (4:33.60 - 6:07.53)
    "spend fortunes", "naive question", "four completely different engines",
    "risk modeling", "catastrophic", "probability of ruin", "slippage minimization",
    "five billion", "dark pools", "fraud", "anomaly detection",
    "portfolio rebalancing", "covariance matrix", "sharpe ratio",
    "optimization problems", "crystal balls",
    
    # Scene 6: The Verdict & Outro (6:07.53 - 7:05.47)
    "fundamental rule", "not a puzzle", "competing intelligences", "never search",
    "structural speed", "disciplined risk", "microscopic", "compounded",
    "recommendation algorithm", "quantrove"
]

def clean(s):
    return s.lower().strip(".,:;!?'\"-")

matches = []
for phrase in test_phrases:
    tokens = [clean(t) for t in phrase.split()]
    n = len(tokens)
    found = False
    for i in range(len(words) - n + 1):
        wt = [clean(words[i+j]["word"]) for j in range(n)]
        if wt == tokens:
            st = words[i]["start"]
            en = words[i+n-1]["end"]
            matches.append((phrase, st, en, " ".join([words[i+j]["word"] for j in range(n)])))
            found = True
            break
        elif len(wt) > 0 and wt[0].startswith(tokens[0][:4]) and all(wt[k].startswith(tokens[k][:3]) for k in range(n)):
            st = words[i]["start"]
            en = words[i+n-1]["end"]
            matches.append((phrase, st, en, " ".join([words[i+j]["word"] for j in range(n)])))
            found = True
            break
    if not found:
        print(f"MISS: {phrase}")

print(f"\nTotal matches: {len(matches)} / {len(test_phrases)}")
for m in matches:
    print(f"[{m[1]:6.2f} - {m[2]:6.2f}] {m[0].upper():32s} (actual: {m[3]})")
