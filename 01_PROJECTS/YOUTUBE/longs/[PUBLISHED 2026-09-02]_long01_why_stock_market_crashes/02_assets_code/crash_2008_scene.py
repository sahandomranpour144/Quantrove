from manim import *
import numpy as np

config.background_color = "#121212"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class Crash2008Scene(Scene):
    def construct(self):
        # Target total duration: Exactly 31.0 seconds

        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        PURPLE = "#8B5CF6"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#1A1F2C"

        # ---------------------------------------------------------
        # 1. Title & Header (0.0s - 3.0s) -> 3.0s
        # ---------------------------------------------------------
        title = Text("2008: THE FINANCIAL CRISIS", font_size=38, font="Segoe UI", weight=BOLD, color=CYAN)
        subtitle = Text("FIRE #2: OPAQUE SUBPRIME MORTGAGES & HIDDEN RISK", font_size=20, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.5)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # ---------------------------------------------------------
        # 2. Subprime Mortgage & CDO Pipeline (3.0s - 9.0s) -> 6.0s
        # ---------------------------------------------------------
        stages_text = [
            ("Risky Subprime\nMortgages", RED),
            ("Packaged into\nOpaque CDOs", GOLD),
            ("AAA Rating\nRubber-Stamped", CYAN),
            ("Lehman Brothers\n$600B+ Exposure", RED)
        ]
        boxes = []
        for i, (st, col) in enumerate(stages_text):
            b = RoundedRectangle(corner_radius=0.15, height=1.6, width=2.4, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=col, stroke_width=2.5)
            t = Text(st, font_size=13, font="Segoe UI", weight=BOLD, color=WHITE).move_to(b.get_center())
            boxes.append(VGroup(b, t))

        pipe_group = VGroup(*boxes).arrange(RIGHT, buff=0.4).shift(DOWN * 0.2)
        arrows = []
        for i in range(len(boxes) - 1):
            ar = Arrow(start=boxes[i].get_right(), end=boxes[i+1].get_left(), color=MUTED, buff=0.1, stroke_width=3)
            arrows.append(ar)
        arrow_group = VGroup(*arrows)

        pipe_title = Text("The Hidden Subprime Contagion Pipeline", font_size=22, font="Segoe UI", weight=BOLD, color=GOLD).next_to(pipe_group, UP, buff=0.5)

        self.play(
            FadeIn(pipe_title),
            FadeIn(pipe_group, lag_ratio=0.2),
            Create(arrow_group, lag_ratio=0.2),
            run_time=2.2
        )
        self.wait(3.0)

        # ---------------------------------------------------------
        # 3. Lehman Brothers Bankruptcy ($639B) (9.0s - 15.5s) -> 6.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(pipe_title), FadeOut(pipe_group), FadeOut(arrow_group),
            run_time=0.8
        )

        bar_title = Text("Largest Corporate Bankruptcies in U.S. History", font_size=22, font="Segoe UI", weight=BOLD, color=WHITE).shift(UP * 1.8)

        # Horizontal Bar Chart
        bar_data = [
            ("Lehman Brothers (2008)", 6.39, "$639B", RED),
            ("Washington Mutual (2008)", 3.28, "$328B", GOLD),
            ("WorldCom (2002)", 1.07, "$107B", CYAN),
            ("Enron (2001)", 0.65, "$65B", PURPLE)
        ]
        bar_mobs = []
        for i, (name, width_val, val_str, col) in enumerate(bar_data):
            y_pos = 0.8 - i * 0.9
            bar = Rectangle(width=width_val, height=0.5, fill_color=col, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1).move_to(LEFT * 1.5 + RIGHT * (width_val / 2) + UP * y_pos)
            label = Text(name, font_size=13, font="Segoe UI", color=WHITE).next_to(bar, LEFT, buff=0.2)
            val_text = Text(val_str, font_size=14, font="Segoe UI", weight=BOLD, color=WHITE).next_to(bar, RIGHT, buff=0.15)
            bar_mobs.extend([bar, label, val_text])

        bars_vgroup = VGroup(*bar_mobs)

        self.play(
            FadeIn(bar_title),
            FadeIn(bars_vgroup, lag_ratio=0.15),
            run_time=2.2
        )
        self.wait(3.5)

        # ---------------------------------------------------------
        # 4. September 15, 2008: Dow Intraday Drop (-504 pts) (15.5s - 21.0s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(bar_title), FadeOut(bars_vgroup),
            run_time=0.8
        )

        axes_intraday = Axes(
            x_range=[0, 4, 1],
            y_range=[10800, 11600, 200],
            x_length=8.5,
            y_length=3.8,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        hours_lbls = ["9:30 AM", "11:30 AM", "1:30 PM", "3:00 PM", "4:00 PM"]
        hours_group = VGroup(*[
            Text(hours_lbls[i], font_size=13, color=MUTED).next_to(axes_intraday.c2p(i, 10800), DOWN, buff=0.15)
            for i in range(5)
        ])

        pts_intra = [axes_intraday.c2p(i, val) for i, val in enumerate([11421, 11210, 11140, 11010, 10917])]
        curve_intra = VMobject(color=RED, stroke_width=4.5)
        curve_intra.set_points_as_corners(pts_intra)

        badge_drop = RoundedRectangle(corner_radius=0.15, height=0.9, width=4.8, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=RED, stroke_width=2).to_corner(UR, buff=1.2)
        text_drop = VGroup(
            Text("SEPT 15, 2008 CRASH", font_size=15, font="Segoe UI", weight=BOLD, color=RED),
            Text("Dow Dropped -504 pts (-4.4%)", font_size=14, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(badge_drop.get_center())

        self.play(
            FadeIn(axes_intraday), FadeIn(hours_group),
            Create(curve_intra), FadeIn(badge_drop), FadeIn(text_drop),
            run_time=2.2
        )
        self.wait(2.5)

        # ---------------------------------------------------------
        # 5. The Domino Cascade: Lehman to AIG Bailout (21.0s - 26.5s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(axes_intraday), FadeOut(hours_group), FadeOut(curve_intra), FadeOut(badge_drop), FadeOut(text_drop),
            run_time=0.8
        )

        domino_title = Text("The Contagion Chain: Lehman Was Just The First Visible Domino", font_size=20, font="Segoe UI", weight=BOLD, color=GOLD).shift(UP * 1.8)

        dominos = [
            ("1. Subprime Mortgages Default", GOLD),
            ("2. Bear Stearns Sold (Mar 2008)", GOLD),
            ("3. Lehman Files Bankruptcy (Sept 15)", RED),
            ("4. AIG $85B Emergency Bailout (Sept 17)", RED),
            ("5. Global Interbank Lending Freezes", PURPLE)
        ]
        d_boxes = []
        for i, (text_d, col_d) in enumerate(dominos):
            y_d = 0.9 - i * 0.7
            box_d = RoundedRectangle(corner_radius=0.1, height=0.55, width=7.2, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=col_d, stroke_width=2).shift(UP * y_d)
            txt_d = Text(text_d, font_size=14, font="Segoe UI", weight=BOLD, color=col_d).move_to(box_d.get_center())
            d_boxes.extend([box_d, txt_d])

        domino_group = VGroup(*d_boxes)

        self.play(
            FadeIn(domino_title),
            FadeIn(domino_group, lag_ratio=0.15),
            run_time=2.2
        )
        self.wait(2.5)

        # ---------------------------------------------------------
        # 6. Conclusion Summary Card & Pad to 31.0s (26.5s - 31.0s) -> 4.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(domino_title), FadeOut(domino_group), FadeOut(header_group),
            run_time=0.8
        )

        summary_card = RoundedRectangle(corner_radius=0.25, height=4.2, width=9.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=CYAN, stroke_width=3)
        summary_content = VGroup(
            Text("2008'S LESSON", font_size=28, font="Segoe UI", weight=BOLD, color=CYAN),
            Text("Hidden Risk Nobody Could See Until Too Late", font_size=20, font="Segoe UI", weight=BOLD, color=WHITE),
            Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=MUTED, stroke_width=1),
            Text("• Trigger: Subprime Mortgages & Interconnected Derivatives\n• Max Drawdown: -56.8% in S&P 500 (Oct 2007 - Mar 2009)\n• Recovery Timeline: ~5.5 Years to Regain Previous Peak", font_size=16, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.2).move_to(summary_card.get_center())

        self.play(FadeIn(summary_card, scale=0.95), FadeIn(summary_content), run_time=1.0)
        self.wait(3.5)
