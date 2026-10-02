#!/usr/bin/env python3
"""
Unit and integration test suite for the Quantrove Script Humanizer workflow.
Verifies:
1. Banned AI cliché detection logic.
2. Textbook pedagogical pattern detection vs. documentary storytelling pattern.
3. Preservation of quantitative claims, numbers, and dates.
4. Completeness of skill documentation and integration touchpoints across workspace configs.
"""

import os
import re
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

BANNED_AI_PATTERNS = [
    r"\bin today'?s world\b",
    r"\bin our modern world\b",
    r"\bin a world where\b",
    r"\brapidly evolving\b",
    r"\bever-changing\b",
    r"\blandscape\b",
    r"\brevolutionary\b",
    r"\bgame-?changing\b",
    r"\bit is important to understand\b",
    r"\bit'?s crucial to note\b",
    r"\bvital to remember\b",
    r"\bdelve into\b",
    r"\bdive into\b",
    r"\btestament to\b",
    r"\btapestry\b",
    r"\bpivotal role\b",
]

TEXTBOOK_PATTERNS = [
    r"\bdefinition\s*:",
    r"\bexplanation\s*:",
    r"\bfor example\s*:",
    r"\bis defined as\b",
]

CURIOSITY_PATERNS = [
    r"something strange appears",
    r"what happens when",
    r"to see why",
    r"look closely at",
    r"a bizarre pattern emerges",
    r"the moment",
    r"inside the",
]

class TestScriptHumanizer(unittest.TestCase):

    def setUp(self):
        self.raw_ai_sample = (
            "In today's world, algorithmic trading plays a pivotal role in the rapidly evolving financial landscape. "
            "It is important to understand that the stock market crash happened because of portfolio insurance algorithms. "
            "Reflexivity is defined as when an asset's price changes because traders act on predictions. "
            "This revolutionary technology allows firms to make millions. "
            "For example, when Apple stock was traded in 1987, algorithms executed sell orders."
        )

        self.humanized_sample = (
            "On October 19, 1987, fifty-four automated trading systems at the New York Stock Exchange began selling "
            "S&P 500 futures at the exact same millisecond. "
            "Why would the world's largest investment banks trust billions to an equation that broke within minutes? "
            "Standard financial theory assumed market swings followed a Gaussian distribution. "
            "But something strange appears when we look at every crash together: the selling didn't start with human panic. "
            "It started with a mathematical rule specifically designed to prevent it. "
            "When researchers plotted the 1987 order flow, the tails were fat, stubborn, and mathematically volatile. "
            "The consequence was structural: the algorithms didn't buffer market shock—they magnified it by 10,000x."
        )

    def test_banned_ai_tropes_flagged(self):
        detected = []
        for pattern in BANNED_AI_PATTERNS:
            if re.search(pattern, self.raw_ai_sample, re.IGNORECASE):
                detected.append(pattern)
        self.assertGreaterEqual(len(detected), 4, f"Expected multiple AI clichés flagged, found: {detected}")

    def test_humanized_script_zero_banned_tropes(self):
        detected = []
        for pattern in BANNED_AI_PATTERNS:
            match = re.search(pattern, self.humanized_sample, re.IGNORECASE)
            if match:
                detected.append(match.group(0))
        self.assertEqual(len(detected), 0, f"Humanized script contains banned AI clichés: {detected}")

    def test_textbook_pattern_eliminated(self):
        # Raw sample has textbook patterns
        raw_textbook = [p for p in TEXTBOOK_PATTERNS if re.search(p, self.raw_ai_sample, re.IGNORECASE)]
        self.assertGreaterEqual(len(raw_textbook), 1)

        # Humanized sample has 0 textbook patterns
        humanized_textbook = [p for p in TEXTBOOK_PATTERNS if re.search(p, self.humanized_sample, re.IGNORECASE)]
        self.assertEqual(len(humanized_textbook), 0)

    def test_curiosity_markers_present_in_humanized(self):
        curiosity_hits = [p for p in CURIOSITY_PATERNS if re.search(p, self.humanized_sample, re.IGNORECASE)]
        self.assertGreaterEqual(len(curiosity_hits), 1)

    def test_chapter_quad_components(self):
        # 1. Human Question
        self.assertIn("Why would the world's largest investment banks", self.humanized_sample)
        # 2. Mystery / Problem
        self.assertIn("Standard financial theory assumed", self.humanized_sample)
        # 3. Data Reveal
        self.assertIn("When researchers plotted the 1987 order flow", self.humanized_sample)
        # 4. Consequence
        self.assertIn("The consequence was structural", self.humanized_sample)

    def test_quantitative_preservation(self):
        # Test that exact metrics, dates, and numbers remain intact
        raw_with_numbers = "In 1988, Jim Simons achieved a 66% return, executing with a 50.75% statistical edge."
        humanized_with_numbers = (
            "In 1988, Jim Simons took a mathematical approach that generated a 66% return. "
            "The mystery was his edge: Renaissance Technologies wasn't right 90% of the time, but exactly 50.75%."
        )
        raw_numbers = re.findall(r"\b\d+(?:\.\d+)?%?\b", raw_with_numbers)
        humanized_numbers = re.findall(r"\b\d+(?:\.\d+)?%?\b", humanized_with_numbers)
        for num in raw_numbers:
            self.assertIn(num, humanized_numbers, f"Quantitative data point {num} lost during humanization")

    def test_skill_file_exists_and_complete(self):
        skill_path = os.path.join(WORKSPACE_ROOT, ".claude", "skills", "quantrove-script-humanizer", "SKILL.md")
        self.assertTrue(os.path.exists(skill_path), "SKILL.md does not exist")
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("name: quantrove-script-humanizer", content)
        self.assertIn("Rule 1: Banish Generic AI Language", content)
        self.assertIn("Rule 2: Documentary Storytelling Chapter Quad", content)
        self.assertIn("Rule 3: Increase Curiosity & Tension", content)
        self.assertIn("Rule 4: Human Investigative Observer Voice", content)
        self.assertIn("Rule 5: Anti-Textbook Architecture", content)
        self.assertIn("Rule 6: Preserve Quantitative Rigor & Neutrality", content)
        self.assertIn("Rule 7: Zero Fabrication", content)
        self.assertIn("Pass 1: AI Cliché & Pattern Detection", content)
        self.assertIn("Pass 2: Documentary Section-by-Section Rewrite", content)
        self.assertIn("Pass 3: The Believability & Quality Audit", content)
        self.assertIn("Pass 4: Final Output Package Delivery", content)

    def test_rule_file_exists(self):
        rule_path = os.path.join(WORKSPACE_ROOT, ".claude", "rules", "script-humanization.md")
        self.assertTrue(os.path.exists(rule_path), "script-humanization.md does not exist")

    def test_workflow_integrations(self):
        claude_md = os.path.join(WORKSPACE_ROOT, "CLAUDE.md")
        with open(claude_md, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("quantrove-script-humanizer", c)
        self.assertIn("Script humanization", c)  # CLAUDE.md trimmed 2026-10-02; heading numbers removed

        content_agent = os.path.join(WORKSPACE_ROOT, ".claude", "agents", "content.md")
        with open(content_agent, "r", encoding="utf-8") as f:
            ca = f.read()
        self.assertIn("quantrove-script-humanizer", ca)
        self.assertIn("Phase 3.5 — Script humanization pass", ca)

if __name__ == "__main__":
    unittest.main()
