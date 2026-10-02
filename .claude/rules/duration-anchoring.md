# Rule: Duration Anchoring

Anchor every scene and video duration to measured file lengths via `ffprobe`; never estimate or assume durations.

**Implementation**:
- Skill: [.claude/skills/duration-check/SKILL.md](../skills/duration-check/SKILL.md)
- Hook: `.claude/hooks/verify_manifest_durations.py`
