# EP08 — The 2017 Paper That Rebuilt Modern AI
Slug: `long08_attention_transformer` | Pillar: AI & ML in the Real World | Season 1
Status: **GATE 1 — AWAITING CEO APPROVAL** (no asset generation before approval)

## 0. Production parameters
- **Title (recommended, 7 words, 37 chars): The 2017 Paper That Rebuilt Modern AI**
- Pace mode: **A (Relaxed)**. The template line is in Scene 2. No runtime number is spoken.
- Narration **1,638 words, 219 beats (median 2.9 s)**. At EP06's measured 157 WPM: **≈10:45** incl. 20 s end screen (inside 10-15 min). Check: `python pipeline/qa/ep_beatcheck.py <this file> 157`.
- Voiceover: Sahand supplies it. Paste **`VO_SCRIPT_CLEAN.txt`** (beat marks removed).
- **Visual Density v1**: `‖` = beat (visual change), 3-6 s, anchored to its first word via faster-whisper after VO.
- Engines: Manim (attention mechanics, math), Remotion (timelines, counters, charts), HyperFrames html_motion (terminal metaphors), Flow (atmosphere ≤8 s, never stretched).
- Kinetic keywords: existing CleanText V2 overlay. Palette lock `#202322 #233D4C #C3D809 #FD802E #E6EDF3`, Nohemi/Inter.
- Music: `assets/audio/BGM.mp3` (CC BY-ND 3.0). Credit from `assets/audio/CREDITS.md` goes in the description.
- **Publish order: EP07 before EP08** (CTA points to EP07). The outro does not tease a next topic.

## 1. Packaging (L1, locked at Gate 1)
| # | Title (6-7 words, <60 chars) | Chars | Note |
|---|---|---|---|
| **1 (rec.)** | The 2017 Paper That Rebuilt Modern AI | 37 | Story + stakes; a date makes it concrete |
| 2 | How AI Decides Which Words Matter | 33 | Mechanism-first; "attention mechanism" search |
| 3 | The Simple Idea Behind Every Chatbot | 36 | Broadest appeal, weakest specificity |

Description and tags lead with **"transformer architecture explained"** (41k/mo, +145%) and **"how llms work"**; "attention mechanism" (comp 35) in the second sentence.

| # | Thumbnail concept (1280x720, palette lock, ≤3 words) |
|---|---|
| **A (rec.)** | A blank paper-page silhouette (no real logos or text) on Raisin Black. From one highlighted word, thin lime attention lines fan out to every other word. Huge lime **"2017"**. |
| B | The letters G P T in Off-White; the **T** glows lime and expands into a stacked-block silhouette. Text: **"THE T"**. |
| C | Left: a chain of links in Pumpkin, cracking. Right: a lime web where every node touches every node. Text: **"ALL AT ONCE"**. |

## 2. Loop ledger (5 open loops)
| ID | Question planted | Planted | Paid |
|---|---|---|---|
| L1 (central) | What did the 2017 paper see that decades of language research missed? | S1-S2 | S39-S40 (82-84% of runtime) |
| L2 | Why did the best models of 2016 struggle with long sentences? | S3-S4 | S5 (first payoff ≈ 0:44) |
| L3 | In the trophy sentence, how does a model know what "it" means? | S7 | S18-S20 |
| L4 | If looking back is what works, can you delete the step-by-step reader? | S11 | S14, S25 |
| L5 | Where did the eight authors end up? | S2 | S43 (≈90%) |

## 3. Shot list (auto-built from §4 by ep_beatcheck.py --sync)
| Scene | Engine | Asset ID | Chapter |
|---|---|---|---|
| 1 | Remotion | R1_PAPER_COUNTER | Intro |
| 2 | Manim | M01_T_IN_GPT | Intro |
| 3 | Flow | F1_INTERPRETER_BOOTH | One Word At A Time |
| 4 | Manim | M02_RNN_CHAIN | One Word At A Time |
| 5 | Manim | M03_MEMORY_SQUEEZE | One Word At A Time |
| 6 | Remotion | R1B_LSTM_GNMT | One Word At A Time |
| 7 | html_motion | HM1_WINOGRAD | One Word At A Time |
| 8 | Manim | M04_DISTANT_LINK | One Word At A Time |
| 9 | Remotion | R2_SEQUENTIAL_GPU | One Word At A Time |
| 10 | Remotion | R3_BAHDANAU_2014 | One Word At A Time |
| 11 | Manim | M05_DELETE_QUESTION | One Word At A Time |
| 12 | Flow | F2_NIGHT_OFFICE | Attention Is All You Need |
| 13 | Remotion | R4_PAPER_CARD | Attention Is All You Need |
| 14 | Manim | M06_ALL_AT_ONCE | Attention Is All You Need |
| 15 | Manim | M06B_144_LINKS | Attention Is All You Need |
| 16 | Manim | M07_QKV | Attention Is All You Need |
| 17 | Manim | M08_DOT_SCORES | Attention Is All You Need |
| 18 | Manim | M09_SOFTMAX | Attention Is All You Need |
| 19 | Manim | M10_FORMULA | Attention Is All You Need |
| 20 | Manim | M11_IT_RESOLVES | Attention Is All You Need |
| 21 | Manim | M12_MULTI_HEAD | Eight Heads, Twelve Hours |
| 22 | Remotion | R4B_WHAT_HEADS_LEARN | Eight Heads, Twelve Hours |
| 23 | Manim | M13_STACK_LAYERS | Eight Heads, Twelve Hours |
| 24 | Manim | M14_POSITION_WAVES | Eight Heads, Twelve Hours |
| 25 | Remotion | R5_TRAINING_COST | Eight Heads, Twelve Hours |
| 26 | Remotion | R6_BLEU | Eight Heads, Twelve Hours |
| 27 | Flow | F3_DATA_CENTER_DAWN | Eight Heads, Twelve Hours |
| 28 | Remotion | R7_TIMELINE_2018_2022 | From Translation To Chatgpt |
| 29 | Remotion | R8_PARAM_GROWTH | From Translation To Chatgpt |
| 30 | Manim | M15_DECODER_ONLY | From Translation To Chatgpt |
| 31 | Remotion | R8B_SCALING_LAWS | From Translation To Chatgpt |
| 32 | Remotion | R9_CHATGPT_USERS | From Translation To Chatgpt |
| 33 | Manim | M15B_BEYOND_TEXT | From Translation To Chatgpt |
| 34 | Manim | M16_N_SQUARED | The Price Of Looking At Everything |
| 35 | Remotion | R10_QUADRATIC_TABLE | The Price Of Looking At Everything |
| 36 | Remotion | R11_CONTEXT_WINDOWS | The Price Of Looking At Everything |
| 37 | html_motion | HM2_TOKEN_METER | The Price Of Looking At Everything |
| 38 | Remotion | R11B_TRANSFORMER_ENGINE | The Price Of Looking At Everything |
| 39 | Manim | M17_CHAIN_VS_WEB | The Answer |
| 40 | Manim | M18_T_RETURNS | The Answer |
| 41 | Manim | M18B_WHAT_IT_DID_NOT_SOLVE | The Answer |
| 42 | Remotion | R13_RECAP | The Answer |
| 43 | Remotion | R12_AUTHORS_GRID | The Answer |
| 44 | Manim | M19_SINGLE_LINE | The Answer |
| 45 | Manim | M20_CTA_SPLIT | Close |
| 46 | Manim | M21_END_SCREEN_BG | Close |

## 4. Script

### INTRO

**Scene 1 — Remotion (R1_PAPER_COUNTER)**
[VISUAL] b1 date card "JUNE 2017" · b2 a blank paper silhouette slides in, 8 author dots, a faint vinyl-record ring behind it · b3 citation counter rolls to "250,000+" · b4 the letters G P T fade in, T pulses lime · b5 T label "TRANSFORMER".
[NARRATION] "In June 2017, eight researchers at Google posted a paper ‖ with a title borrowed from a Beatles song. ‖ It has since been cited more than 250,000 times. ‖ And its key idea became the T in ChatGPT. ‖ T, ‖ for Transformer."
[AUDIO] No logo. Low pulse under the first word; tick with the counter.
KEYWORDS: 2017 | 250,000+ CITATIONS | THE T IN GPT

**Scene 2 — Manim (M01_T_IN_GPT)**
[VISUAL] b1 the T expands into a stacked-block silhouette · b2 thin attention lines web across the blocks · b3 8 author dots orbit, one by one drift off-frame · b4 calm hold, slow drift.
[NARRATION] "So what did this paper see ‖ that decades of language research had missed? ‖ And where did its eight authors end up? ‖ Get comfortable, this one is worth going slowly."
KEYWORDS: WHAT DID THEY SEE?

### CHAPTER 1 — ONE WORD AT A TIME

**Scene 3 — Flow (F1_INTERPRETER_BOOTH, 8 s)**
[VISUAL] b1 empty interpreter booth, headset on the desk, dim conference hall beyond the glass · b2 slow push toward the microphone.
[NARRATION] "Before 2017, the best translation systems worked like a careful reader ‖ with a bad memory."
KEYWORDS: A BAD MEMORY

**Scene 4 — Manim (M02_RNN_CHAIN)**
[VISUAL] b1 words enter a box one by one from the left · b2 a memory vector (column of cells) updates after each word · b3 the vector is handed to the next box · b4 chain of boxes extends; label RECURRENT NEURAL NETWORK.
[NARRATION] "They read a sentence one word at a time. ‖ After each word, they updated a single list of numbers, a running memory, ‖ and passed it to the next step. ‖ These were recurrent neural networks."
KEYWORDS: ONE WORD AT A TIME | RUNNING MEMORY

**Scene 5 — Manim (M03_MEMORY_SQUEEZE)**
[VISUAL] b1 a 30-word sentence feeds the chain · b2 early words' colors fade inside the memory column · b3 the column overwrites, early cells Pumpkin then grey · b4 final memory shows only the last few words clearly.
[NARRATION] "Here is the problem. ‖ By the end of a long sentence, ‖ everything has been squeezed through that one list of numbers. ‖ Early words fade. ‖ Details get overwritten."
KEYWORDS: SQUEEZED | EARLY WORDS FADE

**Scene 6 — Remotion (R1B_LSTM_GNMT)**
[VISUAL] b1 card "1997 · LSTM · Hochreiter & Schmidhuber" · b2 gate icons KEEP / FORGET open and close on the memory column · b3 card "2016 · GOOGLE TRANSLATE → LSTM" · b4 bar "TRANSLATION ERRORS −60% (avg.)" in lime · b5 grey chain still underneath: "STILL ONE WORD AT A TIME".
[NARRATION] "Engineers had fought this for years. ‖ In 1997, a design called the LSTM added gates ‖ that decide what to keep and what to forget. ‖ In 2016, Google Translate switched to a large LSTM system ‖ and reported cutting translation errors by about 60 percent on average. ‖ A huge step. ‖ But it still read one word at a time."
KEYWORDS: 1997 LSTM | 2016 | −60% ERRORS

**Scene 7 — html_motion (HM1_WINOGRAD, 8 s)**
[VISUAL] b1 terminal prints `The trophy didn't fit in the suitcase because it was too big.` · b2 `it → ?` cursor blinks · b3 `it → trophy` in lime · b4 `big` swaps to `small`; `it → suitcase`; hold.
[NARRATION] "Try this sentence. ‖ The trophy didn't fit in the suitcase because it was too big. ‖ What was too big? The trophy. ‖ Change big to small, and it now means the suitcase."
KEYWORDS: WHAT IS "IT"?

**Scene 8 — Manim (M04_DISTANT_LINK)**
[VISUAL] b1 the sentence laid out as chain boxes · b2 a long arc needed from IT back to TROPHY · b3 the arc must travel through every box; memory fades along it (Pumpkin gradient).
[NARRATION] "To get that right, a model must connect it to a word several steps back, ‖ through a memory that has been fading the whole way."
KEYWORDS: SEVERAL STEPS BACK

**Scene 9 — Remotion (R2_SEQUENTIAL_GPU)**
[VISUAL] b1 a grid of 1,000+ GPU cores (small squares) · b2 one core lights lime, the rest dark · b3 the next lights only after the first finishes · b4 label "STEP 1 → STEP 2 → STEP 3 …" · b5 idle-core counter in Pumpkin.
[NARRATION] "There was a second problem, a hardware one. ‖ Because each step needs the step before it, ‖ the words must be processed in order. ‖ A graphics chip with thousands of cores ‖ sits mostly idle, waiting."
KEYWORDS: IN ORDER | IDLE CORES

**Scene 10 — Remotion (R3_BAHDANAU_2014)**
[VISUAL] b1 card "2014 · MONTREAL · Bahdanau, Cho, Bengio" · b2 an output word sends lime lines back to every input word · b3 line thickness = importance · b4 label ATTENTION · b5 the lines are bolted onto a grey chain: "STILL SEQUENTIAL".
[NARRATION] "A partial fix had appeared in 2014. ‖ A team in Montreal let the translator look back at every input word ‖ while writing each output word, ‖ and decide which ones mattered most. ‖ They called it attention. ‖ But it was still bolted onto the slow, step-by-step reader."
KEYWORDS: 2014 | ATTENTION | STILL STEP BY STEP

**Scene 11 — Manim (M05_DELETE_QUESTION)**
[VISUAL] b1 chain + attention lines · b2 the chain highlights Pumpkin · b3 a cursor hovers a "DELETE?" over the chain.
[NARRATION] "So a question sat in plain sight. ‖ If looking back is the part that works, ‖ why keep the step-by-step reader at all?"
KEYWORDS: DELETE THE CHAIN?

### CHAPTER 2 — ATTENTION IS ALL YOU NEED

**Scene 12 — Flow (F2_NIGHT_OFFICE, 8 s)**
[VISUAL] b1 empty open-plan tech office at night, whiteboard with erased equations · b2 slow drift past monitors in standby.
[NARRATION] "In 2017, a group at Google Brain and Google Research tried exactly that. ‖ They deleted the recurrence completely."
KEYWORDS: DELETED THE CHAIN

**Scene 13 — Remotion (R4_PAPER_CARD)**
[VISUAL] b1 title types on: ATTENTION IS ALL YOU NEED · b2 8 author dots appear, shuffle randomly · b3 footnote card "EQUAL CONTRIBUTION · LISTING ORDER IS RANDOM" · b4 card "NeurIPS 2017".
[NARRATION] "The title said it plainly: ‖ Attention Is All You Need. ‖ Eight authors, ‖ with a footnote saying they contributed equally ‖ and were listed in random order."
KEYWORDS: ATTENTION IS ALL YOU NEED

**Scene 14 — Manim (M06_ALL_AT_ONCE)**
[VISUAL] b1 sentence words in a row · b2 every word draws lines to every other word simultaneously (complete graph) · b3 the old chain fades out below · b4 one long-range link (IT↔TROPHY) is now one hop, lime · b5 label "ONE STEP, ANY DISTANCE".
[NARRATION] "Here is the core idea. ‖ Instead of reading left to right, ‖ every word looks at every other word, all at once. ‖ No chain. No fading memory. ‖ Any word can reach any other word in a single step. ‖ The technical name is self-attention: ‖ the sentence attending to itself."
KEYWORDS: ALL AT ONCE | ONE STEP

**Scene 15 — Manim (M06B_144_LINKS)**
[VISUAL] b1 the 12-word trophy sentence · b2 a 12×12 grid assembles beside it, one cell per word pair · b3 counter "144 COMPARISONS" · b4 all 144 light in a single frame: "AT THE SAME TIME".
[NARRATION] "Our trophy sentence has twelve words. ‖ Every word against every word is 144 comparisons. ‖ The old reader made them one step at a time. ‖ This design makes all 144 at the same moment."
KEYWORDS: 144 COMPARISONS | SAME MOMENT

**Scene 16 — Manim (M07_QKV)**
[VISUAL] b1 the word IT emits three arrows · b2 QUERY (lime) labeled "WHAT AM I LOOKING FOR?" · b3 KEY (Off-White) "WHAT DO I CONTAIN?" · b4 VALUE (outline) "WHAT I PASS ALONG" · b5 every word now carries its own Q, K, V.
[NARRATION] "How does a word decide what to look at? ‖ Each word produces three lists of numbers. ‖ A query: what am I looking for? ‖ A key: what do I contain? ‖ And a value: what I will pass along if I am chosen."
KEYWORDS: QUERY | KEY | VALUE

**Scene 17 — Manim (M08_DOT_SCORES)**
[VISUAL] b1 IT's query arrow vs each word's key arrow · b2 angle arcs; aligned pairs glow · b3 score readouts appear beside each word (ILLUSTRATIVE) · b4 TROPHY's score highest.
[NARRATION] "Then every query is compared with every key. ‖ The comparison is the same closeness measure that turns words into maps: ‖ arrows that point the same way score high. ‖ Arrows at right angles score near zero."
KEYWORDS: QUERY · KEY = SCORE

**Scene 18 — Manim (M09_SOFTMAX)**
[VISUAL] b1 raw scores as bars · b2 softmax squashes them into weights summing to 1.00 · b3 TROPHY 0.71, SUITCASE 0.18, others small (ILLUSTRATIVE) · b4 values blend by weight into IT's new vector.
[NARRATION] "The scores are turned into weights that add up to one. ‖ For the word it, in our trophy sentence, ‖ most of the weight can land on trophy. ‖ The new meaning of it becomes a weighted blend of the values."
KEYWORDS: WEIGHTS SUM TO 1 | A WEIGHTED BLEND

**Scene 19 — Manim (M10_FORMULA)**
[VISUAL] b1 Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V assembles · b2 QKᵀ highlights · b3 √dₖ highlights · b4 without it: one weight spikes to 0.99 (Pumpkin), gradient arrow flattens · b5 with it: weights spread · b6 softmax highlights · b7 V highlights; whole line glows lime.
[NARRATION] "Written down, the whole mechanism fits on one line. ‖ Multiply queries by keys. ‖ Scale them down so the numbers stay stable. ‖ Without that step, the scores grow so large ‖ that almost all the weight lands on one word, ‖ and learning stalls. ‖ Turn them into weights. ‖ Mix the values."
KEYWORDS: ONE LINE

**Scene 20 — Manim (M11_IT_RESOLVES)**
[VISUAL] b1 the sentence with weights from IT · b2 BIG flips to SMALL · b3 weight bars slide from TROPHY to SUITCASE (ILLUSTRATIVE) · b4 caption "LEARNED, NOT WRITTEN".
[NARRATION] "Change big to small, ‖ and in a well-trained model the weight can shift toward suitcase. ‖ Nobody wrote a rule about trophies or suitcases. ‖ The queries and keys are learned from data."
KEYWORDS: LEARNED, NOT WRITTEN

### CHAPTER 3 — EIGHT HEADS, TWELVE HOURS

**Scene 21 — Manim (M12_MULTI_HEAD)**
[VISUAL] b1 one attention pattern over the sentence · b2 it splits into 8 side-by-side panels · b3 panel 1 links subject↔verb · b4 panel 2 links pronoun↔noun · b5 panel 3 links neighbors; patterns ILLUSTRATIVE.
[NARRATION] "One attention pattern is not enough. ‖ So the paper ran eight of them side by side, called heads. ‖ Each head can learn to track a different kind of relationship: ‖ who did what, ‖ what refers to what, ‖ which words sit next to each other."
KEYWORDS: 8 HEADS

**Scene 22 — Remotion (R4B_WHAT_HEADS_LEARN)**
[VISUAL] b1 card "2019 · Clark, Khandelwal, Levy, Manning · Stanford" · b2 head panel: verb → its direct object (lime link) · b3 head panel: noun → its determiner · b4 head panel: pronoun → the noun it refers to · b5 caption "FOUND, NOT PROGRAMMED".
[NARRATION] "And they do. ‖ In 2019, a Stanford team opened up a trained Transformer model, BERT, ‖ and looked at its heads one by one. ‖ Some heads had learned to link verbs to their objects. ‖ Others linked nouns to their articles, ‖ or a pronoun to the thing it refers to. ‖ Nobody programmed any of it."
KEYWORDS: FOUND, NOT PROGRAMMED

**Scene 23 — Manim (M13_STACK_LAYERS)**
[VISUAL] b1 attention lines gather into each word · b2 each word enters its own small network box · b3 label ATTENTION → PROCESSING · b4 the pair outlines as one BLOCK · b5 block stacks ×6, camera tilts up · b6 a token's vector refines as it rises, color sharpening.
[NARRATION] "After attention, each word passes through a small network of its own, ‖ a place to process what it just gathered. ‖ Attention, then processing. ‖ That pair is one block. ‖ Then they stacked the block six times, ‖ each layer refining what the one below produced."
KEYWORDS: × 6 LAYERS

**Scene 24 — Manim (M14_POSITION_WAVES)**
[VISUAL] b1 DOG BIT MAN and MAN BIT DOG as identical word sets · b2 attention alone sees the same set: "=" in Pumpkin · b3 sine waves of different speeds draw under each position · b4 each word gets a unique wave signature; "≠" in lime.
[NARRATION] "One catch. ‖ If every word looks at every word at once, ‖ the model has no sense of word order. ‖ The dog bit the man would look the same as the man bit the dog. ‖ So they stamped each position with a signature, ‖ built from sine waves of different speeds."
KEYWORDS: WORD ORDER | SINE WAVES

**Scene 25 — Remotion (R5_TRAINING_COST)**
[VISUAL] b1 GPU core grid from Scene 8 returns; now all cores light at once (lime) · b2 card "8 × NVIDIA P100" · b3 timer "BASE MODEL: 12 HOURS" · b4 timer "BIG MODEL: 3.5 DAYS".
[NARRATION] "Now the real payoff of deleting the chain. ‖ With no step-by-step dependency, ‖ the whole sentence can be processed in parallel. ‖ Their base model trained in twelve hours on eight graphics chips. ‖ The big one took three and a half days."
KEYWORDS: PARALLEL | 12 HOURS | 3.5 DAYS

**Scene 26 — Remotion (R6_BLEU)**
[VISUAL] b1 chart "ENGLISH → GERMAN · BLEU" · b2 previous best bar, then TRANSFORMER 28.4 bar overtakes by 2+ (lime) · b3 chart "ENGLISH → FRENCH": 41.8 · b4 cost bar: "A SMALL FRACTION OF THE TRAINING COST".
[NARRATION] "And it beat the best translation systems of the time. ‖ English to German: 28.4 on the standard BLEU score, ‖ more than two points above the previous best. ‖ English to French: 41.8, ‖ at a small fraction of the training cost of earlier top models."
KEYWORDS: 28.4 | 41.8 | FRACTION OF THE COST

**Scene 27 — Flow (F3_DATA_CENTER_DAWN, 8 s)**
[VISUAL] b1 vast data-center hall, rows of racks, first light through high windows · b2 slow crane up revealing scale.
[NARRATION] "Speed was the real gift. ‖ A model that runs in parallel can grow as fast as hardware can."
KEYWORDS: GROWS WITH HARDWARE

### CHAPTER 4 — FROM TRANSLATION TO CHATGPT

**Scene 28 — Remotion (R7_TIMELINE_2018_2022)**
[VISUAL] b1 timeline 2017 → 2023 · b2 2018: GPT card "GENERATIVE PRE-TRAINED TRANSFORMER" · b3 2018: BERT card · b4 2020: GPT-3 card "96 LAYERS" · b5 "175 BILLION PARAMETERS" · b6 Nov 2022: ChatGPT card.
[NARRATION] "Within a year, others took the design and ran with it. ‖ In 2018, OpenAI released GPT, the Generative Pre-trained Transformer. ‖ Google released BERT, which reads in both directions at once. ‖ In 2020, GPT-3 used 96 layers ‖ and 175 billion parameters. ‖ In November 2022, ChatGPT launched."
KEYWORDS: GPT | BERT | 175 BILLION | CHATGPT

**Scene 29 — Remotion (R8_PARAM_GROWTH)**
[VISUAL] b1 bar "TRANSFORMER (BIG), 2017: 213 MILLION" · b2 bar "GPT-3, 2020: 175 BILLION" shoots past frame, camera tilts up · b3 multiplier "≈ 820×" · b4 the same block icon on both bars: "SAME CORE BLOCK".
[NARRATION] "The big 2017 model had about 213 million parameters. ‖ GPT-3 had 175 billion, ‖ roughly 800 times more. ‖ Same core block, ‖ stacked deeper, ‖ trained on far more text."
KEYWORDS: 213 MILLION → 175 BILLION | ≈ 800×

**Scene 30 — Manim (M15_DECODER_ONLY)**
[VISUAL] b1 the original two-part design (encoder | decoder) · b2 encoder half fades, decoder half stays · b3 attention grid with the upper triangle masked (Pumpkin) · b4 next-token prediction: "the bank raised ___" → "rates" (lime).
[NARRATION] "GPT kept only one half of the original design, ‖ and gave it a single job: predict the next token. ‖ Each word may look back, ‖ but never ahead. ‖ That one rule, repeated at enormous scale, ‖ became the chatbot on your phone."
KEYWORDS: PREDICT THE NEXT TOKEN | LOOK BACK, NEVER AHEAD

**Scene 31 — Remotion (R8B_SCALING_LAWS)**
[VISUAL] b1 log-log chart frame "MODEL SIZE vs ERROR" · b2 points fall on a straight line (lime) · b3 card "2020 · Kaplan et al. · SCALING LAWS" · b4 the line extends forward, dashed: "BIGGER → PREDICTABLY BETTER".
[NARRATION] "Why did everyone keep making them bigger? ‖ In 2020, researchers at OpenAI measured it. ‖ As these models grew, and got more data and compute, ‖ their error fell along a smooth, predictable curve. ‖ That turned scaling from a gamble into a plan."
KEYWORDS: SCALING LAWS | PREDICTABLE

**Scene 32 — Remotion (R9_CHATGPT_USERS)**
[VISUAL] b1 counter "MONTHLY USERS" climbing · b2 hits "100,000,000" at "≈2 MONTHS" · b3 source tag "UBS estimate, Feb 2023 (Reuters)".
[NARRATION] "Analysts at UBS estimated that ChatGPT reached 100 million monthly users ‖ about two months after launch, ‖ the fastest growth they had seen for a consumer app."
KEYWORDS: 100 MILLION | 2 MONTHS


**Scene 33 — Manim (M15B_BEYOND_TEXT)**
[VISUAL] b1 an image cut into a grid of 16×16-pixel patches · b2 patches line up like words; attention lines web between them · b3 card "2020 · VISION TRANSFORMER" · b4 a protein chain (beads) with attention lines between distant residues · b5 card "2021 · ALPHAFOLD 2 · ATTENTION-BASED".
[NARRATION] "And it did not stay with language. ‖ In 2020, Google researchers cut images into small patches ‖ and fed them to a Transformer as if they were words. ‖ It worked. ‖ In 2021, DeepMind's AlphaFold 2, built around attention, ‖ predicted protein structures with accuracy close to lab experiments. ‖ Same core idea: let every piece look at every other piece."
KEYWORDS: IMAGES | PROTEINS | EVERY PIECE

### CHAPTER 5 — THE PRICE OF LOOKING AT EVERYTHING

**Scene 34 — Manim (M16_N_SQUARED)**
[VISUAL] b1 4 words → 4×4 comparison grid (16 cells) · b2 10 words → 100 cells · b3 text doubles → grid quadruples, cells flood Pumpkin.
[NARRATION] "But every word looking at every word has a price. ‖ Ten words means a hundred comparisons. ‖ Double the text, and the work goes up four times."
KEYWORDS: DOUBLE THE TEXT = 4× THE WORK

**Scene 35 — Remotion (R10_QUADRATIC_TABLE)**
[VISUAL] b1 row "1,000 TOKENS → 1,000,000 COMPARISONS" · b2 tag "PER HEAD, PER LAYER" · b3 a book icon "≈100,000 TOKENS (APPROX.)" · b4 row "100,000 TOKENS → 10,000,000,000" in Pumpkin · b5 tag repeats.
[NARRATION] "A thousand tokens means a million comparisons, ‖ for every head, in every layer. ‖ A long novel is on the order of a hundred thousand tokens. ‖ That is ten billion comparisons, ‖ again for every head, in every layer."
KEYWORDS: 10 BILLION COMPARISONS

**Scene 36 — Remotion (R11_CONTEXT_WINDOWS)**
[VISUAL] b1 bar "GPT-3 (2020): 2,048 TOKENS" · b2 bar "GEMINI 1.5 (2024): 1,000,000 TOKENS", log scale · b3 card "FLASHATTENTION · 2022 · SAME RESULT, LESS MEMORY TRAFFIC" · b4 memory-transfer arrows shrink.
[NARRATION] "That is why the amount of text a model can read at once started small. ‖ GPT-3 could take in 2,048 tokens. ‖ In 2024, Google's Gemini 1.5 offered a million. ‖ Getting there took years of engineering, ‖ like FlashAttention in 2022, ‖ which computes the exact same attention ‖ while moving far less data in and out of memory."
KEYWORDS: 2,048 → 1,000,000 TOKENS

**Scene 37 — html_motion (HM2_TOKEN_METER, 8 s)**
[VISUAL] b1 prompt box fills with a long document · b2 `tokens:` counter climbs · b3 `latency` and `cost` meters rise in Pumpkin · b4 final readout; hold.
[NARRATION] "It is also why very long prompts run slower, ‖ and why AI services charge by the token. ‖ Every extra word is one more thing every other word has to look at."
KEYWORDS: CHARGED BY THE TOKEN


**Scene 38 — Remotion (R11B_TRANSFORMER_ENGINE)**
[VISUAL] b1 chip silhouette (generic, no logo) labeled "2022 · NVIDIA H100" · b2 a block inside it lights lime: "TRANSFORMER ENGINE" · b3 arrow from the 2017 paper silhouette to the chip: "THE HARDWARE FOLLOWED".
[NARRATION] "The hardware followed the paper. ‖ In 2022, NVIDIA announced its H100 chip ‖ with a section it literally named the Transformer Engine, ‖ built to speed up exactly this kind of math."
KEYWORDS: TRANSFORMER ENGINE

### CHAPTER 6 — THE ANSWER

**Scene 39 — Manim (M17_CHAIN_VS_WEB)**
[VISUAL] b1 split: left chain (2016), right web (2017) · b2 left chain highlights as BOTTLENECK (Pumpkin) · b3 chain dissolves · b4 web fills the frame, all lines lime · b5 a GPU grid lights behind the web.
[NARRATION] "So what did the 2017 paper see that others missed? ‖ That the step-by-step reader was the bottleneck, not the helper. ‖ Remove it, ‖ let every word look at every other word at once, ‖ and language becomes a problem that hardware can scale."
KEYWORDS: THE CHAIN WAS THE BOTTLENECK

**Scene 40 — Manim (M18_T_RETURNS)**
[VISUAL] b1 G P T letters return · b2 T glows, expands into the stacked blocks · b3 the one-line formula overlays the blocks · b4 scale ruler "× 800".
[NARRATION] "That is the T in GPT. ‖ Not a new kind of mind. ‖ A new way to route information, ‖ simple enough to fit on one line, ‖ and parallel enough to grow 800-fold."
KEYWORDS: A NEW WAY TO ROUTE INFORMATION

**Scene 41 — Manim (M18B_WHAT_IT_DID_NOT_SOLVE)**
[VISUAL] b1 the formula · b2 a "FACT CHECK" box appears beside it, empty, dashed Pumpkin outline · b3 next-token arrow continues regardless · b4 caption "ROUTING ≠ CHECKING".
[NARRATION] "It is worth being clear about what it did not do. ‖ Attention decides which words to combine. ‖ It does not check whether the result is true. ‖ The model still predicts the next token, ‖ fluently and fast, ‖ whether or not the facts behind it hold."
KEYWORDS: ROUTING ≠ CHECKING

**Scene 42 — Remotion (R13_RECAP)**
[VISUAL] b1 card 1997 "GATED MEMORY" · b2 card 2014 "ATTENTION, BOLTED ON" · b3 card 2017 "CHAIN DELETED" · b4 card 2020 "≈800× BIGGER" · b5 card 2022 "100M USERS IN ≈2 MONTHS" · b6 cards align on one line.
[NARRATION] "Gated memory in 1997. ‖ Attention, bolted on, in 2014. ‖ The chain deleted in 2017. ‖ Eight hundred times bigger by 2020. ‖ A hundred million users by early 2023. ‖ One deletion, and everything after it."
KEYWORDS: ONE DELETION

**Scene 43 — Remotion (R12_AUTHORS_GRID)**
[VISUAL] b1 8 author cards (names only, no photos) · b2 "BY 2023: ALL 8 HAD LEFT GOOGLE" · b3 company tags animate in: COHERE, CHARACTER.AI, SAKANA AI, OPENAI, NEAR, INCEPTIVE, ESSENTIAL AI · b4 Shazeer's card returns to a GOOGLE tag "2024" · b5 the 8 cards regroup around the paper silhouette, counter "250,000+".
[NARRATION] "And the eight authors? ‖ By 2023, every one of them had left Google. ‖ They went on to found or join companies ‖ like Cohere, Character.AI, Sakana AI, and OpenAI. ‖ One of them, Noam Shazeer, ‖ returned to Google in 2024 as part of a deal with his startup. ‖ Their eight names sit on one of the most cited papers of the century."
KEYWORDS: ALL 8 LEFT

**Scene 44 — Manim (M19_SINGLE_LINE)**
[VISUAL] b1 the formula alone on the grid · b2 faint chat bubbles flow through it · b3 slow push-in on "softmax".
[NARRATION] "The idea they left behind is still running ‖ inside nearly every major chatbot, ‖ one weighted blend at a time."
KEYWORDS: STILL RUNNING

### CLOSE

**Scene 45 — Manim (M20_CTA_SPLIT)** (T-45 → T-20, ≤25 s)
[VISUAL] b1 attention web shrinks left · b2 EP07's 3D word cloud appears right · b3 dashed bridge: QUERY/KEY → POINTS IN SPACE · b4 frame clears toward the end-screen layout.
[NARRATION] "If you want to see what these models are actually comparing when they pay attention, ‖ watch {EP07_TITLE}. ‖ It shows how every word becomes a point in space. ‖ It's on screen now."
KEYWORDS: none (CTA)

**Scene 46 — Manim (M21_END_SCREEN_BG, 20 s)**
[VISUAL] Slow-drifting attention lines and grid at 20% opacity. **No text**; YouTube end-screen cards only.
[NARRATION] none. [AUDIO] Bed swell, dip to black over the last 1 s.

## 5. Asset specs (agent builds after Gate 1; 1920x1080, 60 fps, palette lock)
**Manim (MovingCameraScene; ambient drifting #233D4C grid 15-25%; push ≤1.08 per beat)**
| Asset | Content / numbers |
|---|---|
| M01 | GPT → T → stacked blocks; 8 author dots drift off |
| M02-M04 | RNN chain with memory column; fading (opacity ∝ steps since word); long arc IT→TROPHY |
| M05 | Chain + attention lines; DELETE? cursor |
| M06 | Complete graph over ~10 words; old chain fades; "ONE STEP, ANY DISTANCE" |
| M07-M09 | Q/K/V arrows; dot-product scores; softmax weights TROPHY 0.71 / SUITCASE 0.18 / rest 0.11 (ILLUSTRATIVE, sums to 1.00) |
| M10 | Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V, term-by-term highlight |
| M11 | Weight shift TROPHY → SUITCASE on BIG→SMALL (ILLUSTRATIVE) |
| M12 | 8 head panels, patterns ILLUSTRATIVE |
| M13 | 6 stacked blocks (encoder side of base model: N = 6) |
| M14 | Sinusoidal positional encoding PE(pos,2i)=sin(pos/10000^(2i/d)), PE(pos,2i+1)=cos(…) waves |
| M06B | 12×12 comparison grid for the trophy sentence (144 cells, exact) |
| M15 | Decoder-only; causal mask (upper triangle masked) |
| M15B | Image → 16×16-pixel patches as tokens (ViT); protein bead chain with long-range attention lines (AlphaFold 2) |
| M18B | Formula + empty dashed FACT CHECK box; "ROUTING ≠ CHECKING" |
| M16 | n² grids: 4→16, 10→100, doubling → ×4 |
| M17-M21 | Chain vs web; T returns; formula alone; CTA split; end-screen BG (20 s, no text) |

**Remotion (`spring()` damping 200; brandTokens.ts; one `<Sequence>` per beat)**: R1 paper + citation counter · R2 GPU sequential cores · R3 Bahdanau 2014 · R4 paper card + random-order footnote · R5 8×P100, 12 h, 3.5 days · R6 BLEU 28.4 / 41.8 · R7 timeline 2018-2022 · R8 213M → 175B (≈820×) · R9 100M users / 2 months · R10 quadratic table · R11 context windows 2,048 → 1,000,000 + FlashAttention · R12 authors → companies · R1B LSTM 1997 + GNMT 2016 (−60% errors) · R4B Clark et al. 2019 head findings · R8B scaling-law log-log line (shape ILLUSTRATIVE, cite Kaplan 2020) · R11B H100 Transformer Engine · R13 recap 1997 → 2023.

**HyperFrames html_motion (local render; hold final frame ≥0.5 s)**: HM1 Winograd trophy/suitcase · HM2 token/latency/cost meter.

**Flow prompts (8 s, 16:9, no text, no faces, no logos)**
- F1_INTERPRETER_BOOTH: "Empty conference interpreter booth at night, headset resting on the desk, dim conference hall visible through the glass, slow push toward the microphone, cinematic, cold light, no people, no readable text."
- F2_NIGHT_OFFICE: "Empty open-plan tech office at night, whiteboard with faint erased equations, monitors in standby glow, slow lateral drift, cinematic, shallow depth of field, no people, no readable text."
- F3_DATA_CENTER_DAWN: "Vast data center hall with endless rows of server racks, first dawn light through high windows, slow crane up revealing scale, cinematic, cool tones, no people, no readable text."

## 6. Sources (real; cite in description)
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., Polosukhin, I. (2017). *Attention Is All You Need*. NeurIPS 2017, arXiv:1706.03762 (8×P100; base 12 h; big 3.5 days; EN-DE 28.4 BLEU; EN-FR 41.8; big model ≈213M params; N = 6 layers; h = 8 heads; sinusoidal positions; equal-contribution / random-order footnote).
- Bahdanau, D., Cho, K., Bengio, Y. (2014). *Neural Machine Translation by Jointly Learning to Align and Translate*, arXiv:1409.0473.
- Levesque, H. et al. (2012). *The Winograd Schema Challenge* (trophy/suitcase example).
- Radford, A. et al. (2018). *Improving Language Understanding by Generative Pre-Training* (GPT).
- Devlin, J. et al. (2018). *BERT*, arXiv:1810.04805.
- Brown, T. et al. (2020). *Language Models are Few-Shot Learners* (GPT-3: 175B params, 96 layers, 2,048-token context).
- Dao, T. et al. (2022). *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness*.
- Google (Feb 2024). Gemini 1.5 announcement (1M-token context).
- Reuters (2 Feb 2023). UBS note: ChatGPT ≈100M monthly users two months after launch.
- Hochreiter, S. & Schmidhuber, J. (1997). *Long Short-Term Memory*, Neural Computation 9(8).
- Wu, Y. et al. (2016). *Google's Neural Machine Translation System*, arXiv:1609.08144 (errors reduced by ~60% on average vs phrase-based).
- Clark, K., Khandelwal, U., Levy, O., Manning, C.D. (2019). *What Does BERT Look At? An Analysis of BERT's Attention*, BlackboxNLP.
- Kaplan, J. et al. (2020). *Scaling Laws for Neural Language Models*, arXiv:2001.08361.
- Dosovitskiy, A. et al. (2020). *An Image is Worth 16x16 Words* (Vision Transformer), arXiv:2010.11929.
- Jumper, J. et al. (2021). *Highly accurate protein structure prediction with AlphaFold*, Nature 596.
- NVIDIA (Mar 2022). H100 / Hopper announcement (Transformer Engine).
- Wikipedia, *Attention Is All You Need* (citation count >250,000; Beatles title reference; all authors left Google). Cross-check with primary press (Wired/FT) before publish.

## 7. VERIFY BEFORE PUBLISH
1. Citation count "more than 250,000" (Google Scholar on publish day).
2. Title reference to "All You Need Is Love" (primary source preferred over Wikipedia).
3. Paper footnote wording: equal contribution + random listing order.
4. Big-model parameter count ≈213M (Table 3) and the "≈820×" ratio (175B / 213M = 821.6).
5. BLEU 28.4 and "more than 2 points above previous best" (abstract wording: "improving over the existing best results, including ensembles, by over 2 BLEU").
6. UBS / Reuters 100M figure and "fastest growth" wording.
7. Authors: all eight left Google by 2023; Shazeer's 2024 return via the Character.AI deal; company tags in S35 (Gomez→Cohere, Shazeer→Character.AI, Jones→Sakana AI, Kaiser→OpenAI, Polosukhin→NEAR, Uszkoreit→Inceptive, Vaswani & Parmar→Essential AI).
8. Gemini 1.5 "a million tokens" offering date (2024).
9. GNMT "about 60 percent" error reduction wording (Wu et al. 2016 abstract).
10. Clark et al. (2019) head findings: verbs→direct objects, nouns→determiners, coreference (S22).
11. AlphaFold 2 "accuracy close to lab experiments" wording (CASP14 / Jumper 2021).
12. NVIDIA H100 "Transformer Engine" announcement date (2022).
13. "A long novel ≈ 100,000 tokens" is an order-of-magnitude estimate; it is tagged APPROX on screen.
14. `{EP07_TITLE}` = exact published EP07 title; EP07 must be public first.

## 8. ElevenLabs pronunciation hints
Vaswani = vahs-WAH-nee · Shazeer = sha-ZEER · Uszkoreit = OOSH-ko-rite · Polosukhin = po-lo-SOO-kin · Bahdanau = bah-dah-NOW · Bengio = BEN-zhee-oh · BLEU = "blue" · softmax = "soft-max" · Cohere = co-HERE · Sakana = sa-KAH-na · GPT = "G-P-T".

## 9. Chapters (timestamps from final timeline)
0:00 The T in ChatGPT · S3 One Word at a Time · S12 Attention Is All You Need · S21 Eight Heads, Twelve Hours · S28 From Translation to ChatGPT · S34 The Price of Looking at Everything · S39 The Answer

## 10. Humanization self-audit
- Banned clichés: 0. Chapter Quad: Ch1 (reader → squeeze → trophy test → GPU idle), Ch2 (deletion → Q/K/V → formula → "it" resolved), Ch3 (heads → order problem → 12 hours → BLEU), Ch4 (spread → scale → next-token rule → adoption), Ch5 (n² → numbers → context windows → cost to you).
- Curiosity pivots: S5 "Here is the problem", S11 "a question sat in plain sight", S24 "One catch", S31 "Why did everyone keep making them bigger?", S34 "has a price", S41 "what it did not do".
- Investigator voice; mechanisms introduced through the failure they fix (no definition-first openings).
- Quantitative fidelity: all figures sourced (§6) or tagged ILLUSTRATIVE on screen (attention weights, head patterns).
- Zero fabrication: no claims about the authors' motives for leaving; only where they went.

## 11. Beat check (`ep_beatcheck.py`, 157 WPM)
45 scenes · 1,638 words · 219 beats · median beat 2.9 s · est. runtime 10:45 · 0 beats > 6 s.
