# AI COMPANY COMMUNICATION PROTOCOL

Version:
1.0

---

# 1. Source of Truth

The AI Company does not use chat history as permanent memory.

Permanent information must exist inside project files.

Important information includes:

- Decisions
- Requirements
- Research
- Plans
- Technical designs
- Progress updates

---

# 2. Agent Workflow

Every project follows this flow:

## Phase 1 — Discovery

Research Agent investigates:

- Problem
- Users
- Market
- Competitors
- Existing solutions

Output:

RESEARCH_REPORT.md

---

## Phase 2 — Strategy

Strategy Agent evaluates:

- Opportunities
- Risks
- Possible directions
- Recommended approach

Output:

STRATEGY.md

---

## Phase 3 — Product Planning

Product Agent creates:

- User requirements
- Features
- Priorities
- MVP definition

Output:

PRODUCT_REQUIREMENTS.md

---

## Phase 4 — Execution Planning

Engineering/Content/Design agents create:

- Technical plans
- Production plans
- Implementation details

Output:

EXECUTION_PLAN.md

---

## Phase 5 — Execution

Agents perform approved tasks.

During execution they must:

- Report progress.
- Update status.
- Document important changes.

---

## Phase 6 — Review

QA/Critic Agent evaluates:

- Quality
- Problems
- Missing parts
- Risks

Output:

REVIEW_REPORT.md

---

# 3. Task Handoff Format

When one agent gives work to another:

Use:

## Task

What needs to be done?

## Context

Why is this needed?

## Previous Work

What already exists?

## Expected Output

What should be produced?

## Constraints

What limitations exist?

## Success Criteria

How do we know it is complete?

---

# 4. Status Reporting

Agents should report:

STATUS:
(Current state)

COMPLETED:
(Completed work)

WORKING ON:
(Current task)

BLOCKERS:
(Current problems)

NEXT:
(Next action)

---

# 5. Human Decision Points

The human CEO must approve:

- Project direction
- Major strategy changes
- Product scope
- Final release
- Business decisions

Agents prepare information.

Human decides.

---

# 6. Conflict Resolution

If agents disagree:

They must provide:

- Their position.
- Evidence.
- Risks.
- Recommendation.

The Orchestrator resolves operational conflicts.

The CEO resolves strategic conflicts.

---

# 7. Communication Principle

Agents should avoid:

- Long unnecessary explanations.
- Repeating information.
- Working without context.

Agents should prioritize:

- Clear information.
- Useful outputs.
- Actionable recommendations.

---

END OF PROTOCOL