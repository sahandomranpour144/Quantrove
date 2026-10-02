from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class VariableRewardCurveScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"

        title = Text(
            "THE VARIABLE REWARD MECHANISM",
            font="Segoe UI", weight=BOLD, font_size=36, color=CYAN
        ).to_edge(UP, buff=0.4)
        sub = Text(
            "Why predictable content fails -- and randomized rewards hijack attention",
            font="Segoe UI", font_size=15, color=MUTED
        ).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(sub), run_time=1.0)
        self.wait(0.8)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 1.1, 0.25],
            x_length=10.5, y_length=3.8,
            axis_config={"color": MUTED, "stroke_width": 2}, tips=False
        ).shift(DOWN * 0.8)
        x_lbl = Text("Time (sessions)", font="Segoe UI", font_size=13,
                     color=MUTED).next_to(axes, DOWN, buff=0.2)
        y_lbl = Text("Engagement / Dopamine", font="Segoe UI", font_size=13,
                     color=MUTED).rotate(PI / 2).next_to(axes, LEFT, buff=0.2)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.2)

        def predictable(x):
            return max(0.85 - 0.07 * x, 0.1)

        curve_pred = axes.plot(predictable, x_range=[0, 10], color=MUTED, stroke_width=3)
        lbl_pred = Text("Predictable schedule", font="Segoe UI", font_size=14,
                       color=MUTED).next_to(axes.c2p(7.5, predictable(7.5)), UP, buff=0.2)
        self.play(Create(curve_pred), FadeIn(lbl_pred), run_time=1.5)

        spikes = [0.3, 0.7, 0.45, 0.95, 0.2, 0.85, 0.4, 0.75, 0.6, 0.9, 0.7]

        def variable(x):
            i = int(x)
            if i >= len(spikes) - 1:
                return spikes[-1]
            frac = x - i
            return spikes[i] * (1 - frac) + spikes[i + 1] * frac

        curve_var = axes.plot(variable, x_range=[0, 9.99], color=GOLD, stroke_width=3.5)
        lbl_var = Text("Variable reward (algorithm)", font="Segoe UI", font_size=14,
                      color=GOLD).next_to(axes.c2p(4.5, 0.95), UP, buff=0.2)
        self.play(Create(curve_var), FadeIn(lbl_var), run_time=2.0)
        self.wait(0.5)

        skinner_bg = RoundedRectangle(
            corner_radius=0.2, width=9.0, height=1.0,
            fill_color=PANEL_BG, fill_opacity=1,
            stroke_color=RED, stroke_width=2
        ).to_edge(DOWN, buff=0.3)
        skinner_txt = Text(
            "B.F. Skinner, 1957: Variable-ratio schedules produce the highest,"
            " most persistent response rates.",
            font="Segoe UI", font_size=13, color=WHITE
        ).move_to(skinner_bg)
        self.play(FadeIn(skinner_bg), FadeIn(skinner_txt), run_time=1.0)
        self.wait(4.0)
