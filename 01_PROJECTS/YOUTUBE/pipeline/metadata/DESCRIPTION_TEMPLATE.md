# Quantrove Long-Form Description Template

**Purpose**: Standardize the 6-block YouTube video description architecture across all releases. Guarantees strong click-to-retention alignment, proper attribution, search optimization, and strict legal compliance.  
**Authority**: Standing Channel Architecture  

---

## 1. Description Architecture (6 Mandatory Blocks)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ BLOCK 1: THE HOOK PARAGRAPH (Max 150 chars)                                │
│ Spoken click promise + core title keywords in first 2 lines.                │
├─────────────────────────────────────────────────────────────────────────────┤
│ BLOCK 2: NARRATIVE SYNOPSIS (2–3 sentences)                                 │
│ What the empirical data shows, why it matters, and the core insight.        │
├─────────────────────────────────────────────────────────────────────────────┤
│ BLOCK 3: TIMESTAMPS / CHAPTERS                                              │
│ Word-aligned chronological chapter boundaries (>= 10s per chapter).         │
├─────────────────────────────────────────────────────────────────────────────┤
│ BLOCK 4: DATA & PRIMARY SOURCES                                             │
│ Explicit academic citations, regulatory filings, and empirical sources.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ BLOCK 5: WATCH NEXT / PLAYLIST ROUTING                                      │
│ Companion video title and dedicated playlist link.                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ BLOCK 6: CHANNEL POSITIONING, DISCLAIMER & HASHTAGS                         │
│ Permanent identity block + regulatory disclaimer + exactly 3 hashtags.      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Reusable Description Template

```text
{BLOCK_1: HOOK_PARAGRAPH — Max 150 characters. Must restate title keywords and core promise.}

{BLOCK_2: NARRATIVE_SYNOPSIS — 2 to 3 sentences. State the central question, what the mathematical or historical data shows, and why the outcome contradicts common intuition.}

CHAPTERS
00:00 {Chapter 1 Title}
{mm:ss} {Chapter 2 Title}
{mm:ss} {Chapter 3 Title}
...
{mm:ss} End Screen

DATA & SOURCES
- {Source 1: Primary paper / regulatory filing / dataset}
- {Source 2: Academic citation / institutional reference}
- {Source 3: Methodology / historical archive}

WATCH NEXT
{COMPANION_VIDEO_TITLE}: {COMPANION_VIDEO_URL}

Quantrove: data-driven documentaries on AI, markets, and the systems behind them. Every episode is built from primary data.

Channel: https://youtube.com/@Quantrove
Playlists: {PILLAR_PLAYLIST_URL}

Educational content only. Not financial, investment, or trading advice. Markets involve risk.

#Quantrove #{PillarHashtag} #{TopicHashtag}
```

---

## 3. SEO Rules for Description Writing

1. **First 150 Characters Count Most**: The first two lines appear in YouTube search snippets and above the "Show more" fold on mobile devices. They must contain the primary search terms naturally.
2. **Never Paste Tags into Descriptions**: YouTube explicitly penalizes comma-separated keyword blocks in descriptions (tag stuffing). Keywords must live inside natural, grammatical sentences.
3. **Exact Timestamp Synchronization**: Timestamps must be derived from `ffprobe` or word alignment outputs, never estimated from draft scripts. First chapter must begin at `00:00`.
4. **Hashtag Strictness**: Exactly three hashtags at the very bottom. Format:
   `#Quantrove #{PillarHashtag} #{TopicHashtag}` (e.g. `#Quantrove #MachineLearning #VectorEmbeddings`).
