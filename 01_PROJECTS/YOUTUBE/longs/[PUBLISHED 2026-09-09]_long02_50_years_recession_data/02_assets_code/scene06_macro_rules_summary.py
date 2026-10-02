from manim import *

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class MacroRulesSummaryScene(Scene):
    def construct(self):
        # Target total duration: Exactly 25.0 seconds
        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"

        # 1. Header (0.0s - 3.0s) -> 3.0s
        title = Text("WHAT 50 YEARS OF DATA ACTUALLY TEACHES US", font_size=34, font="Segoe UI", weight=BOLD, color=CYAN)
        subtitle = Text("THE THREE IMMUTABLE RULES OF ECONOMIC CYCLES", font_size=18, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.45)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # 2. Three Rule Cards (3.0s - 16.0s) -> 13.0s
        rules = [
            ("RULE #1", "Recessions are brief resets in an ongoing long-term growth curve.", CYAN),
            ("RULE #2", "Official news is always late; waiting for certainty guarantees missing the bottom.", GOLD),
            ("RULE #3", "Panic selling is historically the most expensive trade an investor can make.", RED),
        ]

        card_mobs = []
        for i, (r_title, r_desc, col) in enumerate(rules):
            c_box = RoundedRectangle(corner_radius=0.12, height=1.15, width=11.2, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=col, stroke_width=2)
            t1 = Text(r_title, font_size=14, font="Segoe UI", weight=HEAVY, color=col).next_to(c_box.get_left(), RIGHT, buff=0.4).shift(UP * 0.18)
            t2 = Text(r_desc, font_size=13, font="Segoe UI", color=WHITE).next_to(c_box.get_left(), RIGHT, buff=0.4).shift(DOWN * 0.18)
            chk = Text("✔", font_size=18, font="Segoe UI", weight=BOLD, color=GREEN).next_to(c_box.get_right(), LEFT, buff=0.4)
            card_mobs.append(VGroup(c_box, t1, t2, chk))

        cards_group = VGroup(*card_mobs).arrange(DOWN, buff=0.25).shift(DOWN * 0.2)

        self.play(FadeIn(cards_group, lag_ratio=0.3), run_time=3.0)
        self.wait(10.0)

        # 3. Next Episode Teaser Bridge (16.0s - 25.0s) -> 9.0s
        teaser_box = RoundedRectangle(corner_radius=0.15, height=1.3, width=11.2, fill_color="#0F172A", fill_opacity=0.95, stroke_color=CYAN, stroke_width=2.5).to_edge(DOWN, buff=0.45)
        teaser_tag = Text("NEXT BREAKDOWN (WEEK 3 — AI & ML EXPLAINED):", font_size=13, font="Segoe UI", weight=HEAVY, color=CYAN).next_to(teaser_box.get_top(), DOWN, buff=0.25)
        teaser_title = Text("How Recommendation Algorithms Actually Decide What You Watch", font_size=15, font="Segoe UI", weight=BOLD, color=WHITE).next_to(teaser_tag, DOWN, buff=0.18)

        self.play(
            FadeIn(teaser_box, shift=UP),
            FadeIn(teaser_tag, shift=UP),
            FadeIn(teaser_title, shift=UP),
            run_time=1.5
        )
        self.wait(7.5)
