# EP07 — How AI Turns Every Word Into Geometry
Slug: `long07_ai_words_geometry` | Pillar: AI & ML in the Real World | Season 1
Status: **GATE 1 — AWAITING CEO APPROVAL** (no asset generation before approval)

## 0. Production parameters
- **Title (recommended, 7 words, 37 chars): How AI Turns Every Word Into Geometry**
- Pace mode: **A (Relaxed)**. The template line is in Scene 2. No runtime number is spoken.
- Narration **1674 words, 229 beats (median 2.8 s)**. At EP06's measured 157 WPM: **≈10:59** incl. 20 s end screen (inside 10-15 min). Check: `python pipeline/qa/ep_beatcheck.py <this file> 157`.
- Voiceover: Sahand supplies it (ElevenLabs Adam or Gemini TTS). Paste **`VO_SCRIPT_CLEAN.txt`**, not this file; `‖` beat marks are removed there.
- **Visual Density v1** (`.claude/rules/visual-density.md`): `‖` in the narration = a visual change (beat). Beats target 3-6 s. Each beat is anchored to its first word via faster-whisper after VO.
- Engines: Manim (math/geometry), Remotion (data graphics, first 16:9 build), HyperFrames html_motion (terminal metaphors, local render), Flow (atmosphere only, ≤8 s, never stretched).
- Kinetic keywords: existing CleanText V2 overlay. KEYWORDS lines are cues only.
- Palette lock: `#202322 #233D4C #C3D809 #FD802E #E6EDF3`. Nohemi, Inter fallback. Lime = signal/positive, Pumpkin = risk/bias.
- Music: `assets/audio/BGM.mp3` (CC BY-ND 3.0). The credit block from `assets/audio/CREDITS.md` goes in the description.
- Callback: EP04 in the CTA (published). The outro does not tease the next episode's topic.

## 1. Packaging (L1, locked at Gate 1)
| # | Title (6-7 words, <60 chars) | Chars | Note |
|---|---|---|---|
| **1 (rec.)** | How AI Turns Every Word Into Geometry | 37 | Curiosity + mechanism; matches the concept |
| 2 | How ChatGPT Actually Understands Your Words | 43 | Highest search pull ("how chatgpt works" 22.9k/mo) |
| 3 | The Hidden Map Inside Every AI | 30 | 6 words; strongest mystery, weakest search |

Description and tags lead with **"how LLMs work"** (36k/mo, +117%, competition 36.5), the searched phrase. "Word embeddings" goes in tags only (<750/mo).

| # | Thumbnail concept (1280x720, palette lock, ≤3 words) |
|---|---|
| **A (rec.)** | Dark 3D constellation of lime points. One thick lime arrow sweeps from a point labeled KING to a glowing point labeled QUEEN. Big text top-left: **"KING − MAN + WOMAN"** set as an equation, and a large lime **"= ?"** (counts as the 3-word cap: the equation is the image). |
| B | Split frame. Left: a tall column of zeros with one lime "1" (one-hot). Right: the same word as a bright point inside a dense cluster. Text: **"AI SEES THIS"**. |
| C | The word "BANK" as a single point, pulled between a Lime cluster (RATES, LOAN) and a Pumpkin cluster (RIVER, SHORE) by two arrows. Text: **"WHICH BANK?"** |

## 2. Loop ledger (5 open loops)
| ID | Question planted | Planted | Paid |
|---|---|---|---|
| L1 (central) | How does a machine that only does arithmetic know king relates to queen, and what else is in the map? | S1-S2 | S41-S44 (84%-91% of runtime) |
| L2 | Why did decades of teaching computers language keep failing? | S3-S5 | S8-S9 (S8 starts 1:19; payoff lands before 1:30) |
| L3 | How do you give a number meaning? | S10 | S13-S21 |
| L4 | What is hiding in the directions between words? | S22 | S23-S26 |
| L5 | What else did the map learn from us? / which bank? | S27 / S36 | S28-S30 / S37 |

## 3. Shot list (auto-built from §4 by ep_beatcheck.py --sync)
| Scene | Engine | Asset ID | Chapter |
|---|---|---|---|
| 1 | Manim | M01_WORDS_TO_POINTS | Intro |
| 2 | Manim | M02_MAP_CLUSTERS | Intro |
| 3 | Flow | F1_MAINFRAME_1954 | The Word A Computer Cannot See |
| 4 | Remotion | R1_GEORGETOWN_CARD | The Word A Computer Cannot See |
| 5 | Remotion | R2_ALPAC_1966 | The Word A Computer Cannot See |
| 6 | Manim | M04_RULES_PILE | The Word A Computer Cannot See |
| 7 | html_motion | HM1_ONE_HOT_SCROLL | The Word A Computer Cannot See |
| 8 | Manim | M03_EQUAL_DISTANCE | The Word A Computer Cannot See |
| 9 | Manim | M03B_NO_SIMILARITY | The Word A Computer Cannot See |
| 10 | Remotion | R3_TIMELINE_1957 | The Word A Computer Cannot See |
| 11 | Manim | M05_FIRTH_QUOTE | The Company A Word Keeps |
| 12 | html_motion | HM2_FILL_BLANK | The Company A Word Keeps |
| 13 | Manim | M06_CONTEXT_PULL | The Company A Word Keeps |
| 14 | Manim | M06B_PUSH_APART | The Company A Word Keeps |
| 15 | Manim | M06D_CONTEXT_WINDOW | The Company A Word Keeps |
| 16 | Flow | F2_PAPER_ARCHIVE | The Company A Word Keeps |
| 17 | Remotion | R4_SCALE_COUNTERS | The Company A Word Keeps |
| 18 | Manim | M06C_SIDE_EFFECT | The Company A Word Keeps |
| 19 | Manim | M07_300D_TO_3D | The Company A Word Keeps |
| 20 | Manim | M07B_NO_NAMED_AXIS | The Company A Word Keeps |
| 21 | Manim | M08_COSINE_ANGLE | The Company A Word Keeps |
| 22 | Manim | M09_DIRECTION_TEASE | The Company A Word Keeps |
| 23 | Manim | M10_KING_QUEEN | The Directions Nobody Programmed |
| 24 | Manim | M11_PARALLEL_ARROWS | The Directions Nobody Programmed |
| 25 | Remotion | R5_ANALOGY_TEST | The Directions Nobody Programmed |
| 26 | Remotion | R6_GLOVE_2014 | The Directions Nobody Programmed |
| 27 | Flow | F3_PRINTING_PRESS | The Directions Nobody Programmed |
| 28 | Manim | M12_BIAS_ARROW | The Directions Nobody Programmed |
| 29 | Manim | M13_DEBIAS_PROJECTION | The Directions Nobody Programmed |
| 30 | Remotion | R6B_FAIR_ANALOGY_2020 | The Directions Nobody Programmed |
| 31 | html_motion | HM3_TOKENIZER | From 300 Numbers To 12,288 |
| 32 | Remotion | R7_DIMENSION_GROWTH | From 300 Numbers To 12,288 |
| 33 | Remotion | R8_EMBEDDING_MATRIX | From 300 Numbers To 12,288 |
| 34 | Manim | M14A_ROOM_IN_HIGH_DIMS | From 300 Numbers To 12,288 |
| 35 | Remotion | R8B_TRAINED_TOGETHER | From 300 Numbers To 12,288 |
| 36 | Manim | M14_BANK_SPLIT | From 300 Numbers To 12,288 |
| 37 | Manim | M15_CONTEXT_SHIFT | From 300 Numbers To 12,288 |
| 38 | Flow | F4_SEARCH_HANDS | From 300 Numbers To 12,288 |
| 39 | Remotion | R9_BERT_SEARCH | From 300 Numbers To 12,288 |
| 40 | html_motion | HM4_VECTOR_SEARCH | From 300 Numbers To 12,288 |
| 41 | Manim | M16_FULL_MAP_PULLBACK | The Answer |
| 42 | Manim | M16B_CLOSE_NOT_TRUE | The Answer |
| 43 | Manim | M16C_YOUR_PROMPT | The Answer |
| 44 | Manim | M17_TEXT_TO_POINTS | The Answer |
| 45 | Remotion | R10_RECAP_STACK | The Answer |
| 46 | Manim | M18_CTA_SPLIT | Close |
| 47 | Manim | M19_END_SCREEN_BG | Close |

## 4. Script

### INTRO

**Scene 1 — Manim (M01_WORDS_TO_POINTS)**
[VISUAL] b1 sentence types on; each word lifts off as a lime point · b2 points settle into a 3D cloud, slow orbit · b3 coordinate brackets snap onto one point · b4 KING highlights · b5 arrow MAN→WOMAN slides onto KING · b6 arrow lands on QUEEN; push-in 1.00→1.06.
[NARRATION] "Every AI model you used this year turns every word into geometry. ‖ Not as a metaphor. ‖ Each word becomes a point, with real coordinates. ‖ Take the point for king, ‖ subtract man, add woman, ‖ and you land almost exactly on queen."
[AUDIO] No logo. Soft pulse under the first word; tick on each arrow move.
KEYWORDS: AI | EVERY WORD | GEOMETRY | KING − MAN + WOMAN ≈ QUEEN

**Scene 2 — Manim (M02_MAP_CLUSTERS)**
[VISUAL] b1 camera pulls back: thousands of points · b2 faint sentences stream into the cloud from the edges · b3 clusters glow one by one · b4 one Pumpkin cluster flickers (foreshadow, unlabeled) · b5 slow drift.
[NARRATION] "Nobody typed that rule in. ‖ The machine found it by itself, in billions of sentences written by people. ‖ So what is this map, ‖ and what else did it pick up from us? ‖ Get comfortable, this one is worth going slowly."
KEYWORDS: NOBODY PROGRAMMED IT | WHAT ELSE?

### CHAPTER 1 — THE WORD A COMPUTER CANNOT SEE

**Scene 3 — Flow (F1_MAINFRAME_1954, 8 s)**
[VISUAL] b1 slow dolly past a 1950s mainframe, tape reels turning · b2 rack-focus to punched cards in a tray.
[NARRATION] "January 1954, New York. ‖ An IBM 701 computer translates more than sixty Russian sentences into English, ‖ live, in front of the press."
KEYWORDS: 1954 | IBM 701

**Scene 4 — Remotion (R1_GEORGETOWN_CARD)**
[VISUAL] b1 card "GEORGETOWN–IBM EXPERIMENT · 1954" · b2 counter `250 WORDS` · b3 counter `6 GRAMMAR RULES` · b4 quote card "SOLVED IN 3–5 YEARS" (lime) · b5 "3–5" strikes through in Pumpkin on "It was not".
[NARRATION] "The system knew 250 words ‖ and six rules of grammar. ‖ The researchers predicted ‖ machine translation would be a solved problem within three to five years. ‖ It was not."
KEYWORDS: 250 WORDS | 6 RULES | "3–5 YEARS"

**Scene 5 — Remotion (R2_ALPAC_1966)**
[VISUAL] b1 timeline jumps to 1966, card "ALPAC REPORT" · b2 three bars vs human translator: SPEED, ACCURACY, COST · b3 COST bar doubles in Pumpkin, label "≈2× THE COST" · b4 funding line drops off a cliff.
[NARRATION] "In 1966, a U.S. government committee called ALPAC reviewed a decade of work. ‖ Its verdict: machine translation was slower than humans, ‖ less accurate, ‖ and about twice as expensive. ‖ Funding collapsed."
KEYWORDS: 1966 | SLOWER | LESS ACCURATE | 2× COST

**Scene 6 — Manim (M04_RULES_PILE)**
[VISUAL] b1 rule cards stack up fast (IF / THEN / EXCEPT), camera tilts up · b2 a demo sentence passes cleanly · b3 a real sentence hits the stack; it topples, cards scatter.
[NARRATION] "The fix, for decades, was more rules. ‖ It worked in demos, ‖ and broke on real sentences."
KEYWORDS: MORE RULES | BROKE ON REAL TEXT

**Scene 7 — html_motion (HM1_ONE_HOT_SCROLL, 8 s)**
[VISUAL] b1 terminal header `ONE-HOT ENCODING` · b2 a vector of slots scrolls: 0 0 0 0… · b3 counter rolls to `50,257 SLOTS` · b4 one slot flips to lime `1`; hold ≥0.5 s.
[NARRATION] "Underneath, a word was just a label. ‖ One common scheme gives every word its own slot. ‖ For a vocabulary the size of GPT-3's, that is 50,257 slots, ‖ all zeros except one."
KEYWORDS: ONE-HOT | 50,257 SLOTS

**Scene 8 — Manim (M03_EQUAL_DISTANCE)**
[VISUAL] b1 three axes; HOTEL, MOTEL, BANANA on the unit points · b2 lime edge HOTEL–MOTEL, label √2 · b3 identical edge HOTEL–BANANA, label √2 · b4 all three edges equal, triangle pulses Pumpkin.
[NARRATION] "Here is the problem. ‖ In that system, hotel and motel are exactly as far apart ‖ as hotel and banana. ‖ Every word sits at the same distance from every other word."
KEYWORDS: SAME DISTANCE

**Scene 9 — Manim (M03B_NO_SIMILARITY)**
[VISUAL] b1 a lime "SIMILAR?" probe touches HOTEL and MOTEL · b2 the readout returns 0 · b3 probe tries every pair, all 0 · b4 the triangle dims; caption NO MEANING INSIDE.
[NARRATION] "So the math has no way to say these two belong together. ‖ Ask it how similar any two words are, ‖ and the answer is always the same: zero. ‖ That is why sixty years of rules kept hitting a wall."
KEYWORDS: SIMILARITY = 0

**Scene 10 — Remotion (R3_TIMELINE_1957)**
[VISUAL] b1 timeline 1950 → 2025 draws in · b2 marker drops on 1957, label LINGUISTICS · b3 a quotation mark glyph pulses above it.
[NARRATION] "The way out had been sitting in plain sight since 1957. ‖ It came from a linguist, not an engineer. ‖ John Rupert Firth wrote one sentence that the whole field would later build on."
KEYWORDS: 1957 | ONE SENTENCE

### CHAPTER 2 — THE COMPANY A WORD KEEPS

**Scene 11 — Manim (M05_FIRTH_QUOTE)**
[VISUAL] b1 quote assembles word by word from drifting points · b2 "COMPANY IT KEEPS" turns lime · b3 quote dissolves into one word surrounded by neighbor words.
[NARRATION] "You shall know a word by the company it keeps. ‖ Meaning, in other words, is not stored inside a word. ‖ It is a pattern of neighbors."
KEYWORDS: THE COMPANY IT KEEPS

**Scene 12 — html_motion (HM2_FILL_BLANK, 8 s)**
[VISUAL] b1 prompt `I drank a hot cup of ____` · b2 candidates fade in with bars: coffee, tea, cocoa · b3 `banana` with a near-zero Pumpkin bar · b4 tag ILLUSTRATIVE; hold.
[NARRATION] "Try it. I drank a hot cup of blank. ‖ You already know the answers: ‖ coffee, tea, maybe cocoa. ‖ Never banana."
KEYWORDS: FILL THE BLANK

**Scene 13 — Manim (M06_CONTEXT_PULL)**
[VISUAL] b1 two sentences with a shared context window highlighted · b2 COFFEE and TEA start far apart · b3 numbers under each point shown as short columns, random values · b4 a context match: a lime spring pulls them closer · b5 many pulls in sequence, ticker "UPDATES" climbing · b6 coffee and tea settle side by side.
[NARRATION] "Words that show up in the same places are probably related. ‖ So give each word a list of numbers, ‖ and start those numbers at random. ‖ Then read real text. ‖ Every time two words appear in similar company, ‖ nudge their numbers a little closer."
KEYWORDS: SAME COMPANY → CLOSER

**Scene 14 — Manim (M06B_PUSH_APART)**
[VISUAL] b1 all points start sliding toward the center (collapse) · b2 freeze; Pumpkin warning ring · b3 random words (BANANA, VOLCANO) sampled, Pumpkin springs push them away from COFFEE · b4 the cloud re-expands into clean clusters.
[NARRATION] "But if you only pull things together, everything collapses into one blob. ‖ So the trick has a second half. ‖ Pick a few random words, like banana or volcano, ‖ and push those away. ‖ Pull the real neighbors in, push the random ones out, ‖ millions of times."
KEYWORDS: PULL IN | PUSH OUT

**Scene 15 — Manim (M06D_CONTEXT_WINDOW)**
[VISUAL] b1 a long sentence scrolls · b2 a lime window frames five words either side of COFFEE · b3 the window slides one word at a time · b4 words outside the window fade to grey.
[NARRATION] "How close counts as company? ‖ A small window, usually a handful of words on either side. ‖ Slide that window across every sentence, ‖ one word at a time, ‖ and you have your training data, for free."
KEYWORDS: CONTEXT WINDOW

**Scene 16 — Flow (F2_PAPER_ARCHIVE, 8 s)**
[VISUAL] b1 endless aisles of stacked newspapers, dim cold light · b2 slow push toward one stack.
[NARRATION] "In 2013, a team at Google led by Tomas Mikolov ‖ ran that idea at a scale nobody had tried."
KEYWORDS: 2013 | GOOGLE

**Scene 17 — Remotion (R4_SCALE_COUNTERS)**
[VISUAL] b1 title card WORD2VEC · b2 counter `~100,000,000,000 WORDS READ` · b3 counter `3,000,000 WORDS & PHRASES` · b4 counter `300 NUMBERS PER WORD` · b5 one word card flips to a 300-cell strip.
[NARRATION] "They called it word2vec. ‖ Their public model read about a hundred billion words of news. ‖ It ended with three million words and phrases, ‖ each one stored as a list of 300 numbers. ‖ Three hundred coordinates per word."
KEYWORDS: WORD2VEC | 100 BILLION WORDS | 300 NUMBERS

**Scene 18 — Manim (M06C_SIDE_EFFECT)**
[VISUAL] b1 a "guessing machine" box predicts neighbor words around COFFEE · b2 training bar fills · b3 the box lifts out of frame and dissolves · b4 the left-behind table of word vectors glows lime: KEPT.
[NARRATION] "Here is the strange part. ‖ The model was trained on a task nobody cared about: ‖ guessing which words sit near which. ‖ When training finished, the guessing part was thrown away. ‖ What they kept was the side effect: ‖ the numbers for each word. ‖ Like walking a city every day to run errands. ‖ The errands end. ‖ The map in your head stays."
KEYWORDS: THE SIDE EFFECT

**Scene 19 — Manim (M07_300D_TO_3D)**
[VISUAL] b1 300-cell strip folds into a single point · b2 3D cloud appears, tag "300D → 3D PROJECTION · ILLUSTRATIVE" · b3 country cluster lights · b4 food cluster lights · b5 motion-verb cluster lights; slow orbit throughout.
[NARRATION] "Nobody can picture 300 dimensions. ‖ But squash them down to three, and the cloud is not random. ‖ Countries gather in one region. ‖ Foods in another. ‖ Verbs of motion in another."
KEYWORDS: NOT RANDOM | CLUSTERS

**Scene 20 — Manim (M07B_NO_NAMED_AXIS)**
[VISUAL] b1 the 300-cell strip; cell 17 highlighted with "= ANIMAL?" · b2 Pumpkin cross over the label · b3 cells light randomly for CAT; no single cell dominates · b4 a diagonal arrow cuts across many axes: MEANING LIVES HERE.
[NARRATION] "So does number seventeen mean animal? ‖ No. ‖ No single number means anything you could name. ‖ Meaning is spread across all 300 at once, ‖ and it shows up as directions through the space, not as axes."
KEYWORDS: DIRECTIONS, NOT AXES

**Scene 21 — Manim (M08_COSINE_ANGLE)**
[VISUAL] b1 arrows from origin to COFFEE and TEA · b2 small angle arc in lime, cos ≈ 0.8 · b3 arrow to TAX, wide angle, cos ≈ 0.1 · b4 formula cos θ = a·b / (‖a‖‖b‖) writes on · b5 label COSINE SIMILARITY.
[NARRATION] "To measure closeness, these models usually skip the ruler and use the angle. ‖ Draw an arrow from the center to each word. ‖ A small angle means similar. ‖ A wide angle means unrelated. ‖ It is called cosine similarity."
KEYWORDS: ANGLE = SIMILARITY

**Scene 22 — Manim (M09_DIRECTION_TEASE)**
[VISUAL] b1 clusters dim · b2 faint arrows appear between clusters, unlabeled · b3 one arrow brightens; push-in.
[NARRATION] "Then the team noticed something they had not asked for. ‖ The positions mattered. ‖ But so did the directions between them."
KEYWORDS: DIRECTIONS

### CHAPTER 3 — THE DIRECTIONS NOBODY PROGRAMMED

**Scene 23 — Manim (M10_KING_QUEEN)**
[VISUAL] b1 KING point, camera orbit · b2 MAN→WOMAN arrow drawn in lime · b3 arrow copies to KING's tip · b4 nearest-neighbor ring pulses around QUEEN · b5 note "INPUT WORDS EXCLUDED FROM SEARCH" · b6 arrow locks; hold.
[NARRATION] "Start at king. ‖ Walk along the arrow that runs from man to woman. ‖ The nearest word to where you stop is queen. ‖ One honest detail: the starting words are left out of that search, ‖ or king itself would often win. ‖ But the direction is real."
KEYWORDS: KING − MAN + WOMAN ≈ QUEEN

**Scene 24 — Manim (M11_PARALLEL_ARROWS)**
[VISUAL] b1 FRANCE→PARIS arrow · b2 ITALY→ROME arrow, parallel, lime · b3 JAPAN→TOKYO joins · b4 cut to grammar plane: WALKING→WALKED · b5 SWIMMING→SWAM parallel · b6 both planes side by side, "NO RULE WRITTEN".
[NARRATION] "The same move works for capitals. ‖ France to Paris points the same way as Italy to Rome. ‖ It works for grammar. ‖ Walking to walked runs roughly parallel to swimming to swam. ‖ Nobody wrote a rule for capitals or past tense. ‖ They fell out of the statistics."
KEYWORDS: CAPITALS | PAST TENSE | NO RULES

**Scene 25 — Remotion (R5_ANALOGY_TEST)**
[VISUAL] b1 counter `19,544 ANALOGY QUESTIONS` · b2 bar MEANING 55% · b3 bar GRAMMAR 59% · b4 footnote "Skip-gram, 640 dims, 6B words · Mikolov et al. 2013" · b5 "FACTS TAUGHT: 0".
[NARRATION] "Mikolov's team measured it. ‖ They wrote 19,544 analogy questions. ‖ One of their models, trained on six billion words, ‖ got about 55 percent of the meaning questions right, ‖ and 59 percent of the grammar ones. ‖ Not perfect. ‖ But nobody had taught it a single fact."
KEYWORDS: 19,544 QUESTIONS | 55% | 59% | 0 FACTS TAUGHT

**Scene 26 — Remotion (R6_GLOVE_2014)**
[VISUAL] b1 card "2014 · STANFORD · GLOVE" · b2 a co-occurrence count grid fills (ICE×SOLID, STEAM×GAS) · b3 the same analogy arrows appear beside it · b4 two methods → one geometry, lime check.
[NARRATION] "A year later, a team at Stanford tried a different route, called GloVe. ‖ No guessing game. ‖ It simply counted how often words appear near each other ‖ across a huge pile of text. ‖ The same directions appeared. ‖ That was the tell. ‖ The geometry was not a quirk of one algorithm. ‖ It was in the language itself."
KEYWORDS: 2014 | GLOVE | IN THE LANGUAGE ITSELF

**Scene 27 — Flow (F3_PRINTING_PRESS, 8 s)**
[VISUAL] b1 newspaper press rolling at night, macro on ink · b2 pages flying past.
[NARRATION] "But if the geometry lives in the language, ‖ it carries everything people wrote, including what they assume."
KEYWORDS: LEARNED FROM US

**Scene 28 — Manim (M12_BIAS_ARROW)**
[VISUAL] b1 header "2016 · Bolukbasi et al." · b2 MAN→COMPUTER PROGRAMMER arrow · b3 same arrow from WOMAN, endpoint hidden · b4 endpoint reveals HOMEMAKER in Pumpkin · b5 camera holds on the two parallel arrows.
[NARRATION] "In 2016, researchers from Boston University and Microsoft Research ‖ ran the same arithmetic on those Google News vectors. ‖ Man is to computer programmer ‖ as woman is to… ‖ homemaker. ‖ The map had learned a stereotype ‖ with the same precision it learned capitals."
KEYWORDS: 2016 | HOMEMAKER | SAME PRECISION

**Scene 29 — Manim (M13_DEBIAS_PROJECTION)**
[VISUAL] b1 a single axis labeled GENDER DIRECTION · b2 occupation points (NURSE, PROGRAMMER, ENGINEER) cast projections onto it · b3 projections collapse to zero (lime) · b4 small Pumpkin residue clusters remain, tag "2019 follow-up: bias persists".
[NARRATION] "Their fix was geometric too. ‖ Find the direction that encodes gender, ‖ and for words that should be neutral, like nurse or programmer, remove it. ‖ A 2019 follow-up found the bias still hiding in the remaining directions. ‖ It is still not fully solved."
KEYWORDS: REMOVE THE DIRECTION | NOT SOLVED


**Scene 30 — Remotion (R6B_FAIR_ANALOGY_2020)**
[VISUAL] b1 card "2020 · Nissim, van Noord & van der Goot" · b2 analogy MAN : DOCTOR :: WOMAN : ? with the exclusion rule ON → NURSE (Pumpkin) · b3 toggle rule OFF → DOCTOR (lime) · b4 caption "THE BIAS IS REAL · SOME FAMOUS EXAMPLES OVERSTATED IT".
[NARRATION] "There is a twist to that story. ‖ A 2020 paper pointed out that the rule banning the input words shapes the answer. ‖ Lift the ban, ‖ and for some famous examples, man is to doctor as woman is to… doctor. ‖ The bias is real, and other tests confirm it. ‖ But some of the most quoted analogies overstated it."
KEYWORDS: THE SEARCH RULE MATTERS

### CHAPTER 4 — FROM 300 NUMBERS TO 12,288

**Scene 31 — html_motion (HM3_TOKENIZER, 8 s)**
[VISUAL] b1 input `Unbelievably, the bank closed.` · b2 text splits into token chips (ILLUSTRATIVE split) · b3 each chip gets a token ID · b4 footer `VOCAB: 50,257 (GPT-3)`; hold.
[NARRATION] "Today's chatbots start the same way, with one change. ‖ They cut text into tokens, whole words or pieces of words. ‖ GPT-3 used a vocabulary of 50,257 of them."
KEYWORDS: TOKENS | 50,257

**Scene 32 — Remotion (R7_DIMENSION_GROWTH)**
[VISUAL] b1 log-scale bar chart frame · b2 bar word2vec 2013: 300 · b3 bar BERT 2018: 768 · b4 bar GPT-3 2020: 12,288 rises past the frame top; camera tilts up to follow.
[NARRATION] "Each token still gets a list of numbers, just a much longer one. ‖ Word2vec used 300. ‖ Google's BERT, in 2018, used 768. ‖ GPT-3, in 2020, used 12,288 numbers for every single token."
KEYWORDS: 300 → 768 → 12,288

**Scene 33 — Remotion (R8_EMBEDDING_MATRIX)**
[VISUAL] b1 grid: rows = 50,257 tokens · b2 columns = 12,288 numbers · b3 multiplication writes on · b4 counter `617,558,016` · b5 label "THE DICTIONARY ALONE".
[NARRATION] "Do the multiplication. ‖ 50,257 tokens, ‖ times 12,288 numbers each. ‖ That is about 617 million numbers, ‖ just for the model's dictionary, ‖ before it has done any thinking at all."
KEYWORDS: 617 MILLION NUMBERS

**Scene 34 — Manim (M14A_ROOM_IN_HIGH_DIMS)**
[VISUAL] b1 2D: two random arrows, angle varies widely · b2 3D: angles cluster nearer 90° · b3 histogram of angles narrows sharply as a dimension counter climbs to 12,288 · b4 peak locks at ≈90°, label NEARLY PERPENDICULAR.
[NARRATION] "And 12,288 dimensions behave in a way our intuition does not. ‖ Pick two random arrows in that space, ‖ and they are almost always at nearly ninety degrees to each other. ‖ That means there is room for an enormous number of separate directions, ‖ one reason a single map can hold so many distinctions at once."
KEYWORDS: ROOM FOR MEANING

**Scene 35 — Remotion (R8B_TRAINED_TOGETHER)**
[VISUAL] b1 left panel 2013: MAP built → STOP · b2 right panel chatbot: MAP ⇄ MODEL loop arrows · b3 single goal label "PREDICT THE NEXT TOKEN" (lime) · b4 both panels collapse into the right one.
[NARRATION] "One more change from 2013. ‖ Word2vec built the map first, and then stopped. ‖ In a chatbot, the dictionary is trained together with the rest of the model, ‖ on the same text, ‖ toward one goal: predict the next token."
KEYWORDS: TRAINED TOGETHER | NEXT TOKEN

**Scene 36 — Manim (M14_BANK_SPLIT)**
[VISUAL] b1 BANK point appears · b2 money cluster (RATES, LOAN) lights lime on one side · b3 river cluster (WATER, SHORE) lights Pumpkin on the other · b4 BANK slides to the midpoint, dashed "?" ring.
[NARRATION] "But one point per word has a flaw. ‖ Think of bank. ‖ A river bank and a savings bank get the same coordinates. ‖ The map has to park the word somewhere in between, ‖ and it is wrong for both."
KEYWORDS: ONE POINT, TWO MEANINGS

**Scene 37 — Manim (M15_CONTEXT_SHIFT)**
[VISUAL] b1 sentence "the bank raised rates" above the map · b2 layer 1: arrows from RAISED and RATES nudge BANK · b3 layer 2: another nudge · b4 BANK arrives inside the money cluster · b5 split: "we sat on the bank" moves a copy toward the river cluster.
[NARRATION] "Modern language models fix this inside the model. ‖ Bank starts from the same point every time. ‖ Then each layer moves it, using the words around it. ‖ By the end, bank in 'the bank raised rates' sits near money, ‖ not near water. ‖ GPT-3 does this through 96 layers, ‖ each one adjusting every token's position a little."
KEYWORDS: CONTEXT MOVES THE POINT

**Scene 38 — Flow (F4_SEARCH_HANDS, 8 s)**
[VISUAL] b1 night, hands typing on a phone, screen glow only · b2 macro on the search bar cursor.
[NARRATION] "And this is not only inside chatbots. ‖ When you type a messy question into a search box, geometry does the matching."
KEYWORDS: SEARCH = GEOMETRY

**Scene 39 — Remotion (R9_BERT_SEARCH)**
[VISUAL] b1 card "2019 · GOOGLE SEARCH" · b2 ten search-bar icons, one turns lime: "≈1 IN 10 US ENGLISH QUERIES" · b3 query card "2019 brazil traveler to usa need a visa", the word TO glows lime · b4 arrow direction BR → US flips correct · b5 query becomes a point · b6 nearest pages light up around it.
[NARRATION] "In 2019, Google said it was using BERT ‖ on about one in ten English searches in the United States. ‖ Google's own example was a search ‖ for a Brazil traveler to the USA needing a visa. ‖ Older systems ignored the little word "to". ‖ BERT caught that the traveler was going to the U.S., not coming from it. ‖ Your query becomes a point. ‖ The pages nearest to it come back first."
KEYWORDS: 1 IN 10 SEARCHES | QUERY → POINT

**Scene 40 — html_motion (HM4_VECTOR_SEARCH, 8 s)**
[VISUAL] b1 `query: "can i bring medicine for a friend"` · b2 vector strip `[0.12, -0.48, 0.91 …]` · b3 top-3 results with cosine scores 0.87 / 0.84 / 0.79 (ILLUSTRATIVE) · b4 `RETRIEVED: nearest 3`; hold.
[NARRATION] "The same move sits behind recommendations, ‖ and behind the document search many AI assistants use. ‖ Turn the question into coordinates. ‖ Return the nearest neighbors."
KEYWORDS: NEAREST NEIGHBORS

### CHAPTER 5 — THE ANSWER

**Scene 41 — Manim (M16_FULL_MAP_PULLBACK)**
[VISUAL] b1 KING→QUEEN arrow from Scene 1 reappears · b2 camera pulls back through clusters · b3 entire cloud in frame · b4 label POSITION = MEANING · b5 DIRECTION = RELATIONSHIP · b6 slow orbit.
[NARRATION] "So how does a machine that only does arithmetic know that king relates to queen? ‖ It does not know it the way you do. ‖ It measures it. ‖ For these systems, meaning is position. ‖ Similar words sit close together. ‖ Relationships are directions."
KEYWORDS: MEANING = POSITION | RELATIONSHIP = DIRECTION

**Scene 42 — Manim (M16B_CLOSE_NOT_TRUE)**
[VISUAL] b1 SYDNEY and CANBERRA points side by side, lime link "CLOSE" · b2 label "CAPITAL OF AUSTRALIA?" hovers between them · b3 the map highlights both equally · b4 only CANBERRA gets a lime check, outside the map: "NEEDS MORE THAN GEOMETRY".
[NARRATION] "That also explains one of their strangest habits. ‖ Close in the map means used in similar ways. ‖ It does not mean true. ‖ Sydney and Canberra sit side by side, ‖ and only one of them is Australia's capital. ‖ The map knows they are related. ‖ Picking the right one takes more than geometry."
KEYWORDS: CLOSE ≠ TRUE

**Scene 43 — Manim (M16C_YOUR_PROMPT)**
[VISUAL] b1 a prompt box types "plan a trip to lisbon" · b2 each token lifts off as a point into the map · b3 points land near TRAVEL and PORTUGAL clusters · b4 arrows begin to move them (context), fade to next scene.
[NARRATION] "So the next time you type a question into an AI, ‖ picture what happens first. ‖ Before any answer, before anything you could call reasoning, ‖ every word you wrote becomes a point on this map."
KEYWORDS: EVERY WORD → A POINT

**Scene 44 — Manim (M17_TEXT_TO_POINTS)**
[VISUAL] b1 human sentences scroll in from all sides · b2 they condense into points · b3 the capitals arrow glows lime · b4 the stereotype arrow glows Pumpkin beside it · b5 both arrows in one frame; push-in.
[NARRATION] "And every coordinate came from us, ‖ from billions of sentences people wrote. ‖ That is why the map is so good at capitals and grammar, ‖ and why it also absorbed our stereotypes. ‖ It is a mirror with a ruler attached."
KEYWORDS: FROM US | A MIRROR WITH A RULER

**Scene 45 — Remotion (R10_RECAP_STACK)**
[VISUAL] b1 card 1954 "250 WORDS, 6 RULES" · b2 card 1957 "THE COMPANY IT KEEPS" · b3 card 2013 "300 NUMBERS" · b4 card 2020 "12,288 NUMBERS" · b5 cards align: RULES FAILED, NEIGHBORS WON.
[NARRATION] "Six grammar rules in 1954. ‖ One sentence about neighbors in 1957. ‖ Three hundred numbers in 2013. ‖ More than twelve thousand in 2020. ‖ The rules failed. ‖ The neighbors won."
KEYWORDS: RULES FAILED | NEIGHBORS WON

### CLOSE

**Scene 46 — Manim (M18_CTA_SPLIT)** (T-45 → T-20, ≤25 s)
[VISUAL] b1 the word cloud shrinks to the left half · b2 a price chart draws on the right half (lime/Pumpkin) · b3 dashed bridge between the two · b4 frame clears toward the end-screen layout.
[NARRATION] "If you want to see what this kind of machine does with real market data, ‖ watch {EP04_TITLE}. ‖ It shows where the patterns hold, ‖ and where they break. ‖ It's on screen now."
KEYWORDS: none (CTA)

**Scene 47 — Manim (M19_END_SCREEN_BG, 20 s)**
[VISUAL] Slow-drifting point cloud and grid at 20% opacity. **No text**; YouTube end-screen cards only.
[NARRATION] none. [AUDIO] Bed swell, dip to black over the last 1 s.

## 5. Asset specs (agent builds after Gate 1; 1920x1080, 60 fps, palette lock)
**Manim (MovingCameraScene/ThreeDScene, ambient drifting #233D4C grid 15-25%, push ≤1.08 per beat)**
| Asset | Content / numbers |
|---|---|
| M01/M02 | Sentence → points; 3D cloud; KING − MAN + WOMAN ≈ QUEEN; coordinate bracket "(0.21, −0.64, 0.33, …)" ILLUSTRATIVE |
| M03/M03B | Unit vectors HOTEL/MOTEL/BANANA; every pairwise distance = √2 (exact); dot product of any two = 0 |
| M04 | Rule-card stack topples |
| M06/M06B/M06D | Pull (positive pairs) / push (negative samples) springs; context window ±5 words drawn; update ticker without an exact-count claim |
| M06C | "Guessing machine" removed; vector table kept |
| M07/M07B | PCA-style 3D projection "300D → 3D · ILLUSTRATIVE"; no named axis; diagonal direction arrow |
| M08 | cos θ = a·b / (‖a‖‖b‖); COFFEE–TEA ≈ 0.8, COFFEE–TAX ≈ 0.1 (ILLUSTRATIVE) |
| M09-M11 | Parallel offset vectors; note "input words excluded from nearest-neighbor search" |
| M12/M13 | Bolukbasi et al. (2016) analogy; neutralize = v − (v·g)g; residue tag "Gonen & Goldberg (2019)" |
| M14A | Angle histogram of random vector pairs for d = 2, 3, 100, 12,288 (computed with numpy, seed 7; real distribution, not illustrative) |
| M14/M15 | BANK midpoint; contextual shift over 2 illustrative layers; tag "GPT-3: 96 LAYERS" |
| M16/M16B/M16C/M17 | Pull-back; SYDNEY/CANBERRA close-not-true; prompt → points; mirror frame |
| M18/M19 | CTA split; end-screen background (20 s, no text) |

**Remotion (first 16:9 compositions; `spring()` damping 200; tokens from `brandTokens.ts`; one `<Sequence>` per beat)**
R1 Georgetown card (250 words, 6 rules, "3–5 years") · R2 ALPAC 1966 bars · R3 1957 timeline · R4 word2vec counters · R5 analogy bars 55/59 · R6 GloVe co-occurrence grid · R6B 2020 exclusion-rule toggle · R7 log-scale dims 300/768/12,288 · R8 embedding matrix 617,558,016 · R8B trained-together diagram · R9 2019 BERT 1-in-10 + Brazil visa example · R10 recap cards.

**HyperFrames html_motion (local render, deterministic, hold final frame ≥0.5 s)**: HM1 one-hot scroll · HM2 fill-the-blank bars · HM3 tokenizer chips · HM4 vector search top-3. No narration keywords on screen (V2 overlay owns them).

**Flow prompts (Sahand generates in labs.google/flow; 8 s, 16:9, no text, no faces, no logos)**
- F1_MAINFRAME_1954: "Slow dolly past a 1950s mainframe computer, tape reels turning, cold blue-grey light, dust in the air, rack focus to punched cards in a tray, cinematic, 35mm film grain, no people, no readable text."
- F2_PAPER_ARCHIVE: "Endless aisles of stacked newspapers in a dark warehouse, cool overhead light, slow push-in toward one stack, cinematic, shallow depth of field, no people, no readable text."
- F3_PRINTING_PRESS: "Night shift newspaper printing press, macro of ink rollers and pages rushing past, warm sparse light on a dark background, cinematic, no readable text, no people."
- F4_SEARCH_HANDS: "Close-up of two hands typing on a smartphone in a dark room, screen glow only lighting the fingers, macro on a blinking search bar cursor, cinematic, no readable text, no face."

## 6. Sources (real; cite in description)
- Hutchins, W.J. (2004). *The Georgetown-IBM experiment demonstrated in January 1954*. AMTA.
- ALPAC (1966). *Language and Machines: Computers in Translation and Linguistics*. National Academy of Sciences / NRC.
- Firth, J.R. (1957). *A Synopsis of Linguistic Theory 1930-1955*.
- Mikolov, T. et al. (2013a). *Efficient Estimation of Word Representations in Vector Space*, arXiv:1301.3781 (analogy set 19,544; Skip-gram 640-dim, 6B words: 55% semantic / 59% syntactic).
- Mikolov, T. et al. (2013b). *Distributed Representations of Words and Phrases and their Compositionality*, NeurIPS (negative sampling; Google News vectors ≈100B words, 3M words/phrases, 300 dims).
- Pennington, J., Socher, R., Manning, C. (2014). *GloVe: Global Vectors for Word Representation*, EMNLP.
- Bolukbasi, T. et al. (2016). *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings*, NeurIPS.
- Gonen, H. & Goldberg, Y. (2019). *Lipstick on a Pig*, NAACL.
- Nissim, M., van Noord, R., van der Goot, R. (2020). *Fair is Better than Sensational: Man is to Doctor as Woman is to Doctor*, Computational Linguistics 46(2).
- Devlin, J. et al. (2018). *BERT*, arXiv:1810.04805 (BERT-base hidden size 768).
- Brown, T. et al. (2020). *Language Models are Few-Shot Learners* (GPT-3: d_model 12,288; 96 layers; BPE vocab 50,257).
- Nayak, P. (Google, 25 Oct 2019). *Understanding searches better than ever before* (1 in 10 US English searches; "2019 brazil traveler to usa need a visa").

## 7. VERIFY BEFORE PUBLISH
1. Georgetown-IBM: "more than sixty sentences", 250 words, 6 rules, "3-5 years" claim (Hutchins 2004).
2. ALPAC 1966 "slower, less accurate, about twice as expensive" wording.
3. Google News vectors: ≈100B words, 3M words/phrases (word2vec project page).
4. Analogy figures (S25): confirm the 55% / 59% row in arXiv:1301.3781; use the exact numbers if different.
5. Word2vec window "a handful of words" (S15): deliberately unquantified; do not add a number unless sourced.
6. Nissim et al. (2020): confirm the doctor example matches the paper (S30).
7. GPT-3: vocab 50,257, d_model 12,288, 96 layers (Brown et al. 2020, Table 2.1).
8. Google 2019 "one in ten" + Brazil example wording (S39).
9. `{EP04_TITLE}` = exact published title of EP04 (`jwPcJSfDQPg`).

## 8. ElevenLabs pronunciation hints
word2vec = "word-to-vec" · Mikolov = MEE-ko-lov · Firth = "Furth" · ALPAC = AL-pack · GloVe = "glove" · Bolukbasi = boh-look-BAH-shee · Nissim = NISS-im · GPT = "G-P-T" · BERT = "Bert" · cosine = KO-sign · Canberra = CAN-bruh.

## 9. Chapters (timestamps from final timeline)
0:00 Words as coordinates · S3 The Word a Computer Cannot See · S11 The Company a Word Keeps · S23 The Directions Nobody Programmed · S31 From 300 Numbers to 12,288 · S41 The Answer

## 10. Humanization self-audit
- Banned clichés: 0. Chapter Quad mapped (Question → Mystery → Data Reveal → Consequence) in Ch1-Ch4; Ch5 = primary payoff.
- Curiosity pivots: S8 "Here is the problem", S18 "Here is the strange part", S22 "something they had not asked for", S30 "There is a twist", S36 "one point per word has a flaw", S42 "one of their strangest habits".
- Investigator voice; no definition-first openings (one-hot is introduced through the failure, cosine through the measurement need).
- Quantitative fidelity: every figure is sourced (§6) or tagged ILLUSTRATIVE on screen. The analogy nuance (input words excluded) is stated, not hidden.
- Zero fabrication: no invented anecdotes or quotes beyond Firth's published line.
