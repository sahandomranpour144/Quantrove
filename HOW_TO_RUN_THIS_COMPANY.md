# 🏢 AI Company Operating Manual & Agent Playbook

**Owner & CEO**: Sahand  
**Structure**: One-Person AI-Powered Enterprise  
**Core Objective**: Leverage specialized AI agents as a coordinated executive team to research opportunities, build high-leverage products, and create data-driven educational media.

---

## 🧭 Executive Summary: How Your Company Works

You run this company as the **CEO and sole decision-maker**. The AI agents do **not** act as disconnected chatbots; they function as specialized departments that take an idea from initial spark to final published product or deployed codebase.

```
       [ Sahand (CEO / Decision Maker) ]
                       │
             ┌─────────▼─────────┐
             │   /orchestrator   │ (Chief of Staff)
             └─────────┬─────────┘
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 🔍 /research     💡 /product      🎬 /content
(Market Intel)   (Spec & Scope)   (YouTube/Media)
      │                │                │
      └────────────────┼────────────────┘
                       ▼
                 🛠️ /builder
            (Engineering & Code)
```

---

## 🎬 1. First Video Post-Mortem & Production Workflow

For **Episode 01: "Why Stock Market Crashes Actually Happen"**, here is the exact lifecycle and standard workflow that was established:

### The 6-Phase Video Production Lifecycle

```
Phase 1: Topic & Research
   └─ Investigate 1929, 2008, 2020 crash dynamics, margin debt, liquidity cascades.
Phase 2: Strategy & Narrative Architecture
   └─ Craft the high-retention hook ("22-day collapse"), 3 case studies, core thesis.
Phase 3: Director Script & Shot List
   └─ Detailed script with word-anchored audio cues & 6-8 visual beats every 2-4s.
Phase 4: Hybrid Asset Production
   ├─ Data & Charts: Mathematically accurate animations (Manim / Python).
   ├─ Story / Atmosphere: AI cinematic b-roll via Google Flow (labs.google/flow with Gemini/Veo).
   └─ Voiceover: Clear, pacing-matched voice track.
Phase 5: Timeline Assembly & Polish (CapCut)
   └─ Sync voiceover, apply ambient audio bed, transition whooshes, kinetic captions.
Phase 6: Publishing Package & Archiving
   ├─ READY_TO_PUBLISH.md (Title, SEO Description, Timestamps, Tags, Pinned Comment, Thumbnail).
   └─ Run: python pipeline/mark_uploaded.py <slug>
```

---

## 🤖 2. The Agent Fleet & Workflow Roster

Whenever you start a task in the chat, invoke the corresponding role:

| Agent / Workflow | Department / Role | When to Use It | Primary Output |
| :--- | :--- | :--- | :--- |
| **`/orchestrator`** | **Chief of Staff** | Starting any new idea, routing multi-step tasks, coordinating teams. | Master Execution Plan & Task Delegation |
| **`/research`** | **Market Intelligence** | Investigating user demand, competitors, market data, and validating assumptions. | `RESEARCH_REPORT.md` |
| **`/product`** | **Product / Creative Strategy** | Defining feature scope, MVPs, video narratives, and what *NOT* to build. | `PRODUCT_REQUIREMENTS.md` / `STRATEGY.md` |
| **`/builder`** | **Lead Software Architect** | Designing system architecture, writing code, debugging, and deploying web apps. | Codebase, Tests, `EXECUTION_PLAN.md` |
| **`/content`** | **Media & Channel Director** | End-to-end YouTube production (Shorts & Long-form), scripts, visual briefs, metadata. | `READY_TO_PUBLISH.md`, Shot lists, Assets |

---

## 🛠️ 3. Specialized Skills Library

Agents automatically load and adhere to these specialized knowledge modules:

1. **`youtube-production`** ([Skill File](file:///e:/AI_COMPANY/.agents/skills/youtube-production/SKILL.md)):
   - Retention engineering, pacing rules, 1.5s visual hook directives, metadata SEO, CTR optimization.
2. **`storytelling`** ([Skill File](file:///e:/AI_COMPANY/.agents/skills/storytelling/SKILL.md)):
   - Three-act structures, curiosity loops, emotional hooks, simplifying dense concepts.
3. **`finance-analysis`** ([Skill File](file:///e:/AI_COMPANY/.agents/skills/finance-analysis/SKILL.md)):
   - Quantitative accuracy, market mechanics, risk disclosures, economic data validation.
4. **`software-architecture`** ([Skill File](file:///e:/AI_COMPANY/.agents/skills/software-architecture/SKILL.md)):
   - Scalable local-first & web systems, state management, API design, security.
5. **`ml-explainer`** ([Skill File](file:///e:/AI_COMPANY/.agents/skills/ml-explainer/SKILL.md)):
   - Intuitive mental models for AI/ML concepts without dumbing down technical facts.
6. **`quantrove-script-humanizer`** ([Skill File](.claude/skills/quantrove-script-humanizer/SKILL.md)):
   - 4-pass documentary script transformation: purge generic AI clichés, apply the Chapter Quad (Human Question -> Mystery/Problem -> Data Reveal -> Consequence), anti-textbook pacing, and investigative observer voice while preserving 100% quantitative accuracy before Gate 1 CEO review.

---

## 🔄 4. Standard Operating Procedures (SOPs)

### SOP A: Producing a YouTube Episode (Long-Form)
1. **Kickoff**: `/content Plan long-form episode on [Topic]`.
2. **Review Strategy**: Agent provides title hooks, target audience, and research angles. You approve the best angle.
3. **Generate & Humanize Script & Shot List**: Agent produces initial script draft, executes mandatory 4-pass `quantrove-script-humanizer` workflow (purging AI tropes, enforcing Problem -> Pattern -> Data Reveal -> Meaning), and presents humanized script + 4-engine scene classification (Manim/Remotion/Flow/html_motion) for Gate 1 CEO approval.
4. **Generate Assets**:
   - Agent generates accurate Manim chart code or Remotion components.
   - You prompt Google Flow (`labs.google/flow`) using prompts provided by the agent.
   - Agent supplies `html_motion` prompts (terminal/UI metaphors, 2–8s, holding final frame; see [HTML_MOTION_STANDARD.md](01_PROJECTS/YOUTUBE/pipeline/motion/HTML_MOTION_STANDARD.md)) for manual export to MP4 (Path A).
5. **Assemble & Finalize**: Assemble in CapCut with audio bed and captions.
6. **Publish**: Copy metadata from `READY_TO_PUBLISH.md` (Titles, Chapters, Tags, Thumbnail).
7. **Mark Done**: Run `python pipeline/mark_uploaded.py <episode_slug>`.

### SOP B: Launching a New Software Project / Feature
1. **Kickoff**: `/orchestrator I want to build [Software Idea]`.
2. **Market Validation**: `/research Find competitors, user pain points, and technical feasibility`.
3. **Product Definition**: `/product Define MVP features, UI layout, and what NOT to build`.
4. **Build & Test**: `/builder Generate architecture and implement codebase`.
5. **Log Strategic Decision**: Agent writes decision to [`00_CORE/decisions/DECISION_LOG.md`](file:///e:/AI_COMPANY/00_CORE/decisions/DECISION_LOG.md).

---

## 📜 5. Golden Rules for Running the Company

1. **Chat is Temporary, Files are Forever**: Never leave important specs or decisions in chat history. Always require the agent to write to `00_CORE/` or the project folder.
2. **Evidence Before Assumptions**: Agents must validate data before recommending strategic pivots.
3. **Quality Over Speed**: Better to produce 1 world-class piece of content or software than 10 mediocre generic outputs.
4. **CEO Approval Gate**: Agents propose and execute tasks, but Sahand signs off on strategic decisions, money spending, and public releases.
