from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class TimeJobsAsymmetryScene(Scene):
    def construct(self):
        # Target total duration: Exactly 30.0 seconds
        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"

        # 1. Header (0.0s - 3.0s) -> 3.0s
        title = Text("PATTERN #2: THE ASYMMETRY OF TIME & JOBS", font_size=34, font="Segoe UI", weight=BOLD, color=GOLD)
        subtitle = Text("RECESSIONS ARE BRIEF RESETS; EXPANSIONS ARE LONG AND DOMINANT", font_size=18, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.45)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # 2. Duration Asymmetry Bar Chart (3.0s - 14.0s) -> 11.0s
        bar_title = Text("1. DURATION COMPARISON (1950–2025)", font_size=16, font="Segoe UI", weight=BOLD, color=WHITE).shift(UP * 1.8 + LEFT * 2.5)

        # Recession Bar (10.4 Months)
        rec_bar = RoundedRectangle(corner_radius=0.1, height=0.6, width=1.5, fill_color=RED, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1.5).shift(UP * 0.9 + LEFT * 3.8)
        rec_lbl = Text("Recession: 10.4 Months", font_size=13, font="Segoe UI", weight=BOLD, color=RED).next_to(rec_bar, RIGHT, buff=0.3)

        # Expansion Bar (64 Months / 5.3 Years)
        exp_bar = RoundedRectangle(corner_radius=0.1, height=0.6, width=9.2, fill_color=GREEN, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1.5).shift(UP * 0.1 + LEFT * 0.0)
        exp_lbl = Text("Expansion: 64 Months (5.3 Years / 6x Longer!)", font_size=13, font="Segoe UI", weight=BOLD, color=GREEN).next_to(exp_bar, UP, buff=0.15).align_to(exp_bar, LEFT)

        self.play(FadeIn(bar_title), run_time=0.8)
        self.play(GrowFromEdge(rec_bar, LEFT), FadeIn(rec_lbl), run_time=1.5)
        self.play(GrowFromEdge(exp_bar, LEFT), FadeIn(exp_lbl), run_time=2.5)
        self.wait(6.2)

        # 3. Jobs Recovery Curve: Elevator Down, Stairs Up (14.0s - 30.0s) -> 16.0s
        self.play(
            FadeOut(bar_title), FadeOut(rec_bar), FadeOut(rec_lbl),
            FadeOut(exp_bar), FadeOut(exp_lbl),
            run_time=0.8
        )

        jobs_title = Text("2. THE JOBS RECOVERY LAG: ELEVATOR DOWN, STAIRS UP", font_size=18, font="Segoe UI", weight=BOLD, color=CYAN).shift(UP * 1.8)

        axes = Axes(
            x_range=[0, 48, 6],
            y_range=[3, 11, 2],
            x_length=10.5,
            y_length=3.6,
            axis_config={"color": MUTED, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.6)

        x_lbl = Text("Months from Recession Start", font_size=12, font="Segoe UI", color=MUTED).next_to(axes, DOWN, buff=0.25)
        y_lbl = Text("Unemployment Rate (%)", font_size=12, font="Segoe UI", color=MUTED).next_to(axes, LEFT, buff=0.25).rotate(PI/2)

        def unemp_func(t):
            if t <= 4:
                return 4.0 + 6.0 * (t / 4.0)**0.8
            else:
                return 10.0 - 5.5 * ((t - 4) / 44.0)**0.65

        curve_unemp = axes.plot(unemp_func, x_range=[0, 48], color=GOLD, stroke_width=3.5)

        self.play(FadeIn(jobs_title), Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.5)
        self.play(Create(curve_unemp), run_time=3.5)

        # Callouts
        d_peak = Dot(axes.c2p(4, 10.0), color=RED, radius=0.14)
        lbl_elevator = Text("ELEVATOR DOWN\n(Layoffs in Weeks)", font_size=12, font="Segoe UI", weight=BOLD, color=RED, line_spacing=1.2).next_to(d_peak, UP, buff=0.2)

        lbl_stairs = Text("STAIRS UP\n(3–5 Years to Rehire)", font_size=12, font="Segoe UI", weight=BOLD, color=GREEN, line_spacing=1.2).next_to(axes.c2p(28, 6.2), UP, buff=0.3)

        self.play(FadeIn(d_peak), FadeIn(lbl_elevator), FadeIn(lbl_stairs), run_time=1.5)
        self.wait(8.7)
