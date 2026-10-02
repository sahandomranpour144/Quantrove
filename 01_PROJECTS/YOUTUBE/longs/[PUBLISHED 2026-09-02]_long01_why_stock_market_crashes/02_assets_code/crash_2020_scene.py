from manim import *
import numpy as np

config.background_color = "#121212"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class Crash2020Scene(Scene):
    def construct(self):
        # Target total duration: Exactly 29.0 seconds

        RED = "#EF4444"
        GREEN = "#10B981"
        GOLD = "#F59E0B"
        CYAN = "#06B6D4"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#1A1F2C"

        # ---------------------------------------------------------
        # 1. Title & Header (0.0s - 3.0s) -> 3.0s
        # ---------------------------------------------------------
        title = Text("2020: THE COVID SHOCK", font_size=38, font="Segoe UI", weight=BOLD, color=RED)
        subtitle = Text("FIRE #3: EXOGENOUS BIOLOGICAL SHOCK & THE FASTEST BEAR MARKET", font_size=20, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.5)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # ---------------------------------------------------------
        # 2. 22-Day Crash Curve (-34%) (3.0s - 9.0s) -> 6.0s
        # ---------------------------------------------------------
        axes_2020 = Axes(
            x_range=[1, 22, 3],
            y_range=[2000, 3600, 400],
            x_length=9,
            y_length=4.0,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        labels_2020 = VGroup(
            Text("Day 1 (Feb 19): 3,386 pts", font_size=14, color=GREEN).next_to(axes_2020.c2p(1, 3386), UP, buff=0.15),
            Text("Day 22 (Mar 23): 2,237 pts (-34%)", font_size=14, color=RED).next_to(axes_2020.c2p(22, 2237), DOWN, buff=0.15),
        )

        curve_2020 = axes_2020.plot(
            lambda x: 3386.15 - (3386.15 - 2237.40) * (((x - 1) / 21)**1.1),
            x_range=[1, 22],
            color=RED,
            stroke_width=4.5
        )

        badge_22days = RoundedRectangle(corner_radius=0.15, height=1.0, width=4.8, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=RED, stroke_width=2).to_corner(UL, buff=1.2)
        text_22days = VGroup(
            Text("22 TRADING DAYS", font_size=16, font="Segoe UI", weight=BOLD, color=RED),
            Text("Fastest Bear Market in History", font_size=14, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(badge_22days.get_center())

        self.play(
            FadeIn(axes_2020), FadeIn(labels_2020),
            Create(curve_2020), FadeIn(badge_22days), FadeIn(text_22days),
            run_time=2.2
        )
        self.wait(3.0)

        # ---------------------------------------------------------
        # 3. Worst 1-Day Point Drops (9.0s - 14.5s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(axes_2020), FadeOut(labels_2020), FadeOut(curve_2020), FadeOut(badge_22days), FadeOut(text_22days),
            run_time=0.8
        )

        drop_title = Text("Worst Single-Day Point Drops in Dow Jones History", font_size=22, font="Segoe UI", weight=BOLD, color=WHITE).shift(UP * 1.8)

        drop_data = [
            ("March 16, 2020", 2.997, "-2,997 pts (-12.9%)", RED),
            ("March 12, 2020", 2.352, "-2,352 pts (-10.0%)", RED),
            ("March 9, 2020", 2.013, "-2,013 pts (-7.8%)", GOLD),
            ("Sept 29, 2008", 0.777, "-777 pts (-7.0%)", CYAN)
        ]
        drop_mobs = []
        for i, (date_str, width_val, val_str, col) in enumerate(drop_data):
            y_pos = 0.8 - i * 0.9
            bar = Rectangle(width=width_val * 1.5, height=0.5, fill_color=col, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1).move_to(LEFT * 1.5 + RIGHT * (width_val * 1.5 / 2) + UP * y_pos)
            label = Text(date_str, font_size=14, font="Segoe UI", color=WHITE).next_to(bar, LEFT, buff=0.2)
            val_text = Text(val_str, font_size=14, font="Segoe UI", weight=BOLD, color=WHITE).next_to(bar, RIGHT, buff=0.15)
            drop_mobs.extend([bar, label, val_text])

        drop_vgroup = VGroup(*drop_mobs)

        self.play(
            FadeIn(drop_title),
            FadeIn(drop_vgroup, lag_ratio=0.15),
            run_time=2.2
        )
        self.wait(2.5)

        # ---------------------------------------------------------
        # 4. NYSE Emergency Circuit Breakers (14.5s - 20.0s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(drop_title), FadeOut(drop_vgroup),
            run_time=0.8
        )

        cb_title = Text("NYSE Market-Wide Circuit Breakers Triggered 4 Times", font_size=20, font="Segoe UI", weight=BOLD, color=RED).shift(UP * 1.8)

        levels = [
            ("LEVEL 1: -7% DROP", "15-Minute Market Halt", "Triggered: March 9, 12, 16, 18 (2020)", RED),
            ("LEVEL 2: -13% DROP", "15-Minute Market Halt", "Secondary circuit breaker barrier", GOLD),
            ("LEVEL 3: -20% DROP", "Full-Day Trading Closure", "Emergency shutdown threshold", PURPLE)
        ]
        cb_boxes = []
        for i, (l_title, l_sub, l_desc, col_l) in enumerate(levels):
            x_l = -3.8 + i * 3.8
            box_l = RoundedRectangle(corner_radius=0.15, height=3.0, width=3.4, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=col_l, stroke_width=2.5).shift(RIGHT * x_l + DOWN * 0.2)
            t_main = Text(l_title, font_size=14, font="Segoe UI", weight=BOLD, color=col_l).move_to(box_l.get_top() + DOWN * 0.4)
            t_sub = Text(l_sub, font_size=12, font="Segoe UI", weight=BOLD, color=WHITE).next_to(t_main, DOWN, buff=0.2)
            t_desc = Text(l_desc, font_size=11, font="Segoe UI", color=MUTED).next_to(t_sub, DOWN, buff=0.3)
            cb_boxes.extend([box_l, t_main, t_sub, t_desc])

        cb_group = VGroup(*cb_boxes)

        self.play(
            FadeIn(cb_title),
            FadeIn(cb_group, lag_ratio=0.15),
            run_time=2.2
        )
        self.wait(2.5)

        # ---------------------------------------------------------
        # 5. V-Shaped Liquidity Flood Recovery (20.0s - 25.5s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(cb_title), FadeOut(cb_group),
            run_time=0.8
        )

        axes_v = Axes(
            x_range=[0, 150, 30],
            y_range=[2000, 3600, 400],
            x_length=9,
            y_length=4.0,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        labels_v = VGroup(
            Text("Feb 2020 (ATH)", font_size=13, color=MUTED).next_to(axes_v.c2p(0, 3386), UP, buff=0.1),
            Text("Mar 23 (Bottom)", font_size=13, color=RED).next_to(axes_v.c2p(22, 2237), DOWN, buff=0.1),
            Text("Aug 2020 (New ATH)", font_size=13, color=GREEN).next_to(axes_v.c2p(148, 3389), UP, buff=0.1),
        )

        curve_v = axes_v.plot(
            lambda x: 3386.15 - (3386.15 - 2237.40) * (x / 22)**1.2 if x <= 22 else 2237.40 + (3389.78 - 2237.40) * ((x - 22) / 126)**0.85,
            x_range=[0, 148],
            color=GREEN,
            stroke_width=4.5
        )

        stim_box = RoundedRectangle(corner_radius=0.15, height=1.0, width=5.0, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=GREEN, stroke_width=2).to_corner(UL, buff=1.2)
        stim_text = VGroup(
            Text("CENTRAL BANK FLOOD", font_size=15, font="Segoe UI", weight=BOLD, color=GREEN),
            Text("$3T+ Fed QE + $2.2T CARES Act", font_size=13, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(stim_box.get_center())

        self.play(
            FadeIn(axes_v), Create(curve_v), FadeIn(labels_v),
            FadeIn(stim_box), FadeIn(stim_text),
            run_time=2.2
        )
        self.wait(2.5)

        # ---------------------------------------------------------
        # 6. Conclusion Summary Card & Pad to 29.0s (25.5s - 29.0s) -> 3.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(axes_v), FadeOut(curve_v), FadeOut(labels_v),
            FadeOut(stim_box), FadeOut(stim_text), FadeOut(header_group),
            run_time=0.8
        )

        summary_card = RoundedRectangle(corner_radius=0.25, height=4.2, width=9.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=RED, stroke_width=3)
        summary_content = VGroup(
            Text("2020'S LESSON", font_size=28, font="Segoe UI", weight=BOLD, color=RED),
            Text("Exogenous Shock & Unprecedented Liquidity Rescue", font_size=20, font="Segoe UI", weight=BOLD, color=WHITE),
            Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=MUTED, stroke_width=1),
            Text("• Trigger: Global Pandemic & Mandated Lockdowns\n• Max Drawdown: -33.9% in 22 Trading Days (Fastest in history)\n• Recovery Timeline: ~5 Months (New All-Time Highs in August 2020)", font_size=16, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.2).move_to(summary_card.get_center())

        self.play(FadeIn(summary_card, scale=0.95), FadeIn(summary_content), run_time=1.0)
        self.wait(2.5)
