# Quantrove Tag Library & Tagging Standard

**Purpose**: Provide a modular, 3-tier tag architecture for all video releases. Eliminates manual brainstorming, avoids keyword stuffing, and guarantees optimal character budgets (`<= 300` chars target, `<= 500` hard ceiling).  
**Authority**: Standing Channel Architecture  

---

## 1. The 3-Tier Assembly Formula

Every video's tag string is assembled automatically from three distinct tiers:

$$\text{Total Tag String} = \text{Tier 3: Exact Topic (First)} + \text{Tier 2: Pillar Anchor} + \text{Tier 1: Core Channel Foundation}$$

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. TIER 3: EXACT EPISODE TAGS (5–7 tags, ~120–140 chars)                    │
│    • Exact spoken title phrase                                              │
│    • Primary mathematical / technical keywords                              │
│    • 1–2 close variants or common search queries                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. TIER 2: PILLAR / PLAYLIST TAGS (3–4 tags, ~70–80 chars)                  │
│    • Permanent pillar tags selected from PLAYLIST_METADATA.md               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. TIER 1: CORE CHANNEL TAGS (5 tags, 87 chars)                             │
│    Quantrove, quantitative finance, finance explained, financial markets,   │
│    how markets work                                                         │
└─────────────────────────────────────────────────────────────────────────────┘
Total Length: Target ~270–300 characters (Strictly <= 500 ceiling)
```

---

## 2. Character Budget & Hard Rules

- **Target Budget**: `<= 300` characters total (including commas and spaces).
- **Hard Ceiling**: `<= 500` characters (YouTube maximum).
- **Rule 1 (Position Priority)**: The first tag **MUST** be the exact primary subject matter phrase (e.g. `high frequency trading`, `vector embeddings`, `recession data`).
- **Rule 2 (No Keyword Stuffing)**: Every tag must represent a concept actually explained in the audio/visual timeline. Never include unrelated celebrity or trending keywords.
- **Rule 3 (No Single-Word Fluff)**: Avoid useless isolated tags like `money`, `video`, `cool`, `new`. Use multi-word semantic phrases.

---

## 3. Tier 1: Permanent Core Channel Tags (87 Chars)
```text
Quantrove, quantitative finance, finance explained, financial markets, how markets work
```

---

## 4. Tier 2: Pillar Anchor Tag Sets

### Pillar 1: AI & ML in the Real World (67 Chars)
```text
machine learning explained, how AI works, real world AI, deep learning
```

### Pillar 2: AI + Finance + Trading (74 Chars)
```text
AI trading, algorithmic trading, quantitative trading, backtesting, HFT
```

### Pillar 3: Finance & Trading Simplified (77 Chars)
```text
finance simplified, investing explained, market mechanics, liquidity, PFOF
```

### Pillar 4: Data Stories (79 Chars)
```text
data storytelling, stock market history, market data analysis, macro data
```

---

## 5. Tier 3: Episode Template Generator Examples

### Example: EP06 (The Machines Trading Before You Blink — Pillar 2)
- **Tier 3 (Episode Specific)**: `high frequency trading, HFT algorithms, market making, bid ask spread, Avellaneda Stoikov, adverse selection, latency arbitrage` (132 chars)
- **Tier 2 (Pillar 2)**: `AI trading, algorithmic trading, quantitative trading, backtesting` (68 chars)
- **Tier 1 (Core)**: `Quantrove, quantitative finance, finance explained, financial markets, how markets work` (87 chars)
- **Final Combined Tag String (287 chars)**:
```text
high frequency trading, HFT algorithms, market making, bid ask spread, Avellaneda Stoikov, adverse selection, latency arbitrage, AI trading, algorithmic trading, quantitative trading, backtesting, Quantrove, quantitative finance, finance explained, financial markets, how markets work
```

### Example: EP07 Planned (How AI Turns Words into Geometry — Pillar 1)
- **Tier 3 (Episode Specific)**: `vector embeddings, word embeddings, word2vec explained, how AI understands words, semantic space, embedding vectors, high dimensional space` (144 chars)
- **Tier 2 (Pillar 1)**: `machine learning explained, how AI works, real world AI, deep learning` (67 chars)
- **Tier 1 (Core)**: `Quantrove, quantitative finance, finance explained, financial markets, how markets work` (87 chars)
- **Estimated Combined Tag String**: `~298 characters` (optimal).
