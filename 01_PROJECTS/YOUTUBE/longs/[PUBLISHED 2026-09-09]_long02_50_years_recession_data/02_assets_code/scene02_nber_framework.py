from manim import *

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class NBERFrameworkScene(Scene):
    def construct(self):
        # Target total duration: Exactly 26.0 seconds
        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"

        # 1. Header (0.0s - 3.0s) -> 3.0s
        title = Text("THE TWO-QUARTER GDP MYTH", font_size=36, font="Segoe UI", weight=BOLD, color=RED)
        subtitle = Text("HOW RECESSIONS ARE ACTUALLY MEASURED IN REALITY", font_size=19, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.45)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # 2. The Headline Myth Card & Stamp (3.0s - 9.5s) -> 6.5s
        myth_card = RoundedRectangle(corner_radius=0.15, height=4.2, width=4.8, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=2).shift(LEFT * 3.4 + DOWN * 0.4)
        myth_title = Text("THE POPULAR RULE", font_size=18, font="Segoe UI", weight=BOLD, color=MUTED).next_to(myth_card.get_top(), DOWN, buff=0.4)
        myth_desc = Text("2 Consecutive Quarters\nof Negative Real GDP", font_size=17, font="Segoe UI", color=WHITE, line_spacing=1.3).next_to(myth_title, DOWN, buff=0.5)

        self.play(FadeIn(myth_card), FadeIn(myth_title), FadeIn(myth_desc), run_time=1.5)
        self.wait(1.5)

        stamp_box = RoundedRectangle(corner_radius=0.12, height=1.0, width=3.8, fill_color="#450A0A", fill_opacity=1.0, stroke_color=RED, stroke_width=2.5).move_to(myth_card.get_center() + DOWN * 0.8)
        stamp_txt = Text("NOT OFFICIAL", font_size=20, font="Segoe UI", weight=HEAVY, color=RED).move_to(stamp_box.get_center())

        self.play(
            FadeIn(stamp_box, scale=1.3),
            FadeIn(stamp_txt, scale=1.3),
            run_time=0.8
        )
        self.wait(2.7)

        # 3. NBER Arbiter Panel & 4 Pillars (9.5s - 19.0s) -> 9.5s
        nber_card = RoundedRectangle(corner_radius=0.15, height=4.2, width=5.6, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=CYAN, stroke_width=2.5).shift(RIGHT * 2.8 + DOWN * 0.4)
        nber_title = Text("OFFICIAL ARBITER: NBER", font_size=18, font="Segoe UI", weight=BOLD, color=CYAN).next_to(nber_card.get_top(), DOWN, buff=0.35)
        nber_sub = Text("National Bureau of Economic Research (8 Economists)", font_size=12, font="Segoe UI", color=MUTED).next_to(nber_title, DOWN, buff=0.15)

        pillars = [
            ("1. Payroll Employment", GREEN),
            ("2. Real Personal Income", GREEN),
            ("3. Wholesale & Retail Sales", GREEN),
            ("4. Industrial Production", GREEN)
        ]
        p_mobs = []
        for i, (name, col) in enumerate(pillars):
            p_box = RoundedRectangle(corner_radius=0.08, height=0.5, width=4.8, fill_color="#1E293B", fill_opacity=0.8, stroke_color=PANEL_BORDER, stroke_width=1.5)
            p_txt = Text(name, font_size=13, font="Segoe UI", weight=BOLD, color=WHITE).next_to(p_box.get_left(), RIGHT, buff=0.3)
            chk = Text("✔", font_size=14, font="Segoe UI", weight=BOLD, color=col).next_to(p_box.get_right(), LEFT, buff=0.3)
            item = VGroup(p_box, p_txt, chk)
            p_mobs.append(item)

        pillar_group = VGroup(*p_mobs).arrange(DOWN, buff=0.2).next_to(nber_sub, DOWN, buff=0.3)

        self.play(
            FadeIn(nber_card),
            FadeIn(nber_title),
            FadeIn(nber_sub),
            FadeIn(pillar_group, lag_ratio=0.2),
            run_time=2.5
        )
        self.wait(7.0)

        # 4. Official Standard Callout (19.0s - 26.0s) -> 7.0s
        callout_box = RoundedRectangle(corner_radius=0.12, height=1.1, width=11.0, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=GOLD, stroke_width=2).to_edge(DOWN, buff=0.5)
        callout_txt = Text(
            "\"A significant decline in economic activity spread across the economy,\nlasting more than a few months.\"",
            font_size=14, font="Segoe UI", weight=BOLD, color=GOLD, line_spacing=1.3
        ).move_to(callout_box.get_center())

        self.play(FadeIn(callout_box, shift=UP), FadeIn(callout_txt, shift=UP), run_time=1.5)
        self.wait(5.5)
