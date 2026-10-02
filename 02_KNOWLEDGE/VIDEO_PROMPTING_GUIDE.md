# 🎬 Video Production Prompting Guide (Shorts & Long-Form)

This is the exact prompt structure to use when instructing agents to produce YouTube Shorts or Long-form episodes in Sahand's AI Company.

---

## 🧭 Which Role to Invoke

- **`/content`**: Media & Channel Director — use this directly for video scripting, shot lists, asset generation, and publishing metadata.
- **`/orchestrator`**: Use this if you only have a rough raw idea and want the team to research demand and propose formats first.

---

## 📱 1. Prompt Structure for YouTube Shorts (Vertical 9:16)

Shorts run on a fast-paced, high-retention formula:
- **Hook (0–1.5s)**: Immediate visual payoff / shock number (e.g., *"$4.5 Trillion"*, *"80% Monopoly"*).
- **Cuts (Every 2–4s)**: 6–8 distinct visual beats.
- **Captions**: Kinetic, word-by-word bold text.
- **Outro (Last 2.5s)**: Direct Call to Action.

### 📋 Copy-Paste Prompt Template for Shorts:

```markdown
/content

I want to create a YouTube Short.

Topic / Idea:
[Describe topic, e.g., "The 1929 Margin Debt Trap" or "Fastest Market Crash in History"]

Source Context:
[Paste excerpt from a long video, an article, or a key statistic]

Target Audience:
[e.g., Curious beginners / finance enthusiasts / tech]

Requirements:
1. Hard Hook (0-1.5s): Show the biggest number/shock payoff first.
2. Fast Pacing: 6 to 8 visual beats, cutting every 2-4 seconds.
3. Script: Punchy narration (< 15 words/sentence, total 45-55 seconds).
4. Shot List: Visual asset plan for each beat (Manim chart vs. cinematic prompt).
5. Metadata: Title with #shorts, tags, description, and pinned comment.
```

---

## 🎥 2. Prompt Structure for Long-Form Episodes (Horizontal 16:9)

Long-form follows a hybrid director workflow:
1. **Claude / `/content` Agent**: Writes the initial script, runs `quantrove-script-humanizer` (4-pass documentary transformation), and creates the scene-by-scene shot list.
2. **Data / Numbers Scenes**: Built mathematically with Python/Manim.
3. **Atmospheric / Story Scenes**: Cinematic AI video prompts for Google Flow (`labs.google/flow`).
4. **Assembly**: Manual assembly and pacing sync in CapCut.

### 📋 Copy-Paste Prompt Template for Long-Form Kickoff:

```markdown
/content Plan long-form episode

Topic:
[Topic name / core question, e.g., "Why Stock Market Crashes Actually Happen"]

Target Length:
[e.g., 8–12 minutes / 12–15 minutes]

Target Angle / Thesis:
[e.g., "Compare 1929, 2008, and 2020 through liquidity cascades, not just panic selling"]

Deliverables Needed:
1. Narrative Architecture: Hook, 3-act story arc, curiosity loops, and "aha" climax.
2. Director Script: [VISUAL], [NARRATION], [AUDIO CUE] with scene pacing.
3. Documentary Humanization: Apply quantrove-script-humanizer (0 AI tropes, Chapter Quad: Human Question -> Mystery -> Data Reveal -> Consequence, anti-textbook framing, investigative observer tone).
4. 4-Engine Scene Classification:
   - Numerical/Data scenes -> Specify exact Manim chart requirements.
   - Reusable Data Graphics -> Specify Remotion components.
   - Mood/Story scenes -> Write exact Google Flow / Gemini video prompts.
   - Terminal/UI Metaphors -> Write exact html_motion prompts (see [HTML_MOTION_STANDARD.md](../01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md)).
5. Packaging: 3 High-CTR title options, thumbnail concept & text, YouTube chapters, and SEO description.

Note: Stop at Gate 1 (Humanized Script & Shot List approval) before generating any code or final assets.
```

---

## 🛑 Review Gates (Mandatory Checkpoints)

When running Long-Form video production, the agent must observe two CEO approval gates:

1. **Gate 1 — Script & Shot List Approval**:  
   The agent presents the complete humanized narrative script (audited via `quantrove-script-humanizer`) and shot-by-shot visual breakdown with 4-engine classification (Manim/Remotion/Flow/html_motion). Sahand reviews and approves before moving to asset creation.
2. **Gate 2 — Asset Approval**:  
   The agent presents the rendered Manim/Remotion charts, audio voiceover files, Google Flow clips, and html_motion exports. Sahand signs off before final CapCut timeline assembly.

---

## ⚡ 3. Quick Follow-Up & Sub-Task Prompts

### A. Generating Manim Chart Code:
```markdown
/builder

Generate the Python Manim script for Scene [X]:
- Data points to plot: [X values, Y values, timestamps]
- Style: Dark background, glowing accent lines, clean typography, 16:9 1080p.
- Animation: Smooth line draw matching [X] seconds of narration.
```

### B. Generating Google Flow / Gemini Video Prompts:
```markdown
/content

Generate prompt briefs for Google Flow (labs.google/flow) for the atmospheric scenes in Episode [X]:
- Camera motion, lighting, color grade, and subject descriptions.
- Ensure cinematic realism without text or numbers.
```

### C. Generating html_motion Prompts:
```markdown
/content

Generate the html_motion prompt for Scene [X] per pipeline/motion/HTML_MOTION_STANDARD.md:
- scene_id: [ID]
- episode: [slug]
- slot duration: [N.0s, 2.0-8.0s]
- aspect: [16:9 | 9:16]
- concept: [visual metaphor]
- focal element: [single UI element]
- data source: [REAL+cite | ILLUSTRATIVE]
Include the verbatim BASE BLOCK from 01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md.
```

### D. Humanizing a Long-Form Script Draft (Pass 1–4):
```markdown
/quantrove-script-humanizer

Humanize the draft script for Episode [X]:
- Execute Pass 1: Scan and purge generic AI clichés ("in today's world", "rapidly evolving", "landscape", "revolutionary", "it is important to understand").
- Execute Pass 2: Rewrite sections using the Chapter Quad (Human Question -> Mystery/Problem -> Data Reveal -> Consequence), curiosity pivots, and investigative observer voice.
- Execute Pass 3: Audit against documentary believability while preserving 100% of mathematical formulas and quantitative claims.
- Execute Pass 4: Provide humanized script, change manifest, and Gate 1 validation stamp.
```

### D. Extracting a Short from an Existing Long Video:
```markdown
/content

Extract a high-retention 50-second Short from Episode [X]:
- Find the single most dramatic insight or hook in the episode.
- Re-structure it for vertical 9:16 using the 1.5s hook rule.
- Provide script, visual cuts, and related-video funnel link back to Episode [X].
```

### D. Marking an Episode as Uploaded:
When an episode or short is live on YouTube, tell the agent:
```
I uploaded [episode_slug / short_slug]. Mark it as done.
```
*(The agent runs `python pipeline/mark_uploaded.py <slug>` to archive and close it).*

---

## 🔗 Related References
- [HOW_TO_RUN_THIS_COMPANY.md](file:///e:/AI_COMPANY/HOW_TO_RUN_THIS_COMPANY.md) (Full operating manual & SOP A)
- [00_CORE/CLAUDE_COLLABORATION_GUIDE.md](file:///e:/AI_COMPANY/00_CORE/CLAUDE_COLLABORATION_GUIDE.md) (Claude director standards & gates)
- [01_PROJECTS/YOUTUBE/AGENTS.md](file:///e:/AI_COMPANY/01_PROJECTS/YOUTUBE/AGENTS.md) (Pacing & visual guidelines)
- [.agents/skills/youtube-production/SKILL.md](file:///e:/AI_COMPANY/.agents/skills/youtube-production/SKILL.md) (Deep YouTube skill playbook)
- [mine.md](file:///e:/AI_COMPANY/mine.md) (Quick prompt cheat-sheet)
