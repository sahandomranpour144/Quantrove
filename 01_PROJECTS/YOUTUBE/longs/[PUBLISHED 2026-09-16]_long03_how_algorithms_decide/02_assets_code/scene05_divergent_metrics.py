from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class DivergentMetricsScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"

        # 1. Header (0.0 - 1.5s)
        title = Text(
            "THE PERSONALIZATION PARADOX",
            font="Segoe UI", weight=BOLD, font_size=32, color=CYAN
        ).to_edge(UP, buff=0.35)
        subtitle = Text(
            "Identical Video File  *  Opposite Watch Histories  *  Two Completely Divergent Outcomes",
            font="Segoe UI", font_size=15, color=MUTED
        ).next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(subtitle), run_time=1.0)
        self.wait(0.3)

        # 2. Dual Side-by-Side Panels
        # Left Panel = Viewer A (Long Form)
        left_box = RoundedRectangle(
            corner_radius=0.2, width=6.2, height=5.2,
            fill_color=PANEL_BG, fill_opacity=0.95,
            stroke_color=GREEN, stroke_width=2.0
        ).move_to([-3.4, -0.6, 0])

        left_hdr = Text("VIEWER A: LONG-FORM HABIT", font="Segoe UI",
                        weight=BOLD, font_size=16, color=GREEN).move_to([-3.4, 1.6, 0])
        left_sub = Text("History: 45-min documentary essays", font="Segoe UI",
                        font_size=12, color=MUTED).next_to(left_hdr, DOWN, buff=0.08)

        # Right Panel = Viewer B (Short Form)
        right_box = RoundedRectangle(
            corner_radius=0.2, width=6.2, height=5.2,
            fill_color=PANEL_BG, fill_opacity=0.95,
            stroke_color=RED, stroke_width=2.0
        ).move_to([3.4, -0.6, 0])

        right_hdr = Text("VIEWER B: SHORT-FORM HABIT", font="Segoe UI",
                         weight=BOLD, font_size=16, color=RED).move_to([3.4, 1.6, 0])
        right_sub = Text("History: 15-second fast dopamine scrolls", font="Segoe UI",
                         font_size=12, color=MUTED).next_to(right_hdr, DOWN, buff=0.08)

        self.play(
            FadeIn(left_box, shift=RIGHT * 0.3), FadeIn(left_hdr), FadeIn(left_sub),
            FadeIn(right_box, shift=LEFT * 0.3), FadeIn(right_hdr), FadeIn(right_sub),
            run_time=1.0
        )
        self.wait(0.4)

        # 3. Dual Animated Counters via ValueTracker
        left_tracker = ValueTracker(0.0)
        right_tracker = ValueTracker(45.0)

        left_num = Text("0%", font="Segoe UI", weight=BOLD, font_size=58,
                       color=GREEN).move_to([-3.4, 0.7, 0])
        left_lbl = Text("Predicted Completion Rate", font="Segoe UI",
                        font_size=13, color=WHITE).next_to(left_num, DOWN, buff=0.15)

        right_num = Text("45.0s", font="Segoe UI", weight=BOLD, font_size=58,
                        color=RED).move_to([3.4, 0.7, 0])
        right_lbl = Text("Predicted Abandonment Point", font="Segoe UI",
                         font_size=13, color=WHITE).next_to(right_num, DOWN, buff=0.15)

        def update_left(mob):
            v = int(round(left_tracker.get_value()))
            new_mob = Text(f"{v}%", font="Segoe UI", weight=BOLD,
                          font_size=58, color=GREEN).move_to([-3.4, 0.7, 0])
            mob.become(new_mob)
        left_num.add_updater(update_left)

        def update_right(mob):
            v = right_tracker.get_value()
            new_mob = Text(f"{v:.1f}s", font="Segoe UI", weight=BOLD,
                          font_size=58, color=RED).move_to([3.4, 0.7, 0])
            mob.become(new_mob)
        right_num.add_updater(update_right)

        self.play(
            FadeIn(left_num), FadeIn(left_lbl),
            FadeIn(right_num), FadeIn(right_lbl),
            run_time=0.6
        )

        # 4. Graphs beneath the counters
        left_axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 100, 25],
            x_length=4.8, y_length=1.4,
            axis_config={"color": MUTED, "stroke_width": 1.0, "include_ticks": False}
        ).move_to([-3.4, -1.2, 0])

        left_curve = left_axes.plot(
            lambda x: 15 + 79 * (1 / (1 + np.exp(-0.8 * (x - 4)))),
            x_range=[0, 10], color=GREEN, stroke_width=3.5
        )

        right_axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 100, 25],
            x_length=4.8, y_length=1.4,
            axis_config={"color": MUTED, "stroke_width": 1.0, "include_ticks": False}
        ).move_to([3.4, -1.2, 0])

        right_curve = right_axes.plot(
            lambda x: 5 + 90 * np.exp(-1.2 * x),
            x_range=[0, 10], color=RED, stroke_width=3.5
        )

        self.play(Create(left_axes), Create(right_axes), run_time=0.5)

        # Simultaneous counter + curve animation
        self.play(
            left_tracker.animate.set_value(94.0),
            Create(left_curve),
            right_tracker.animate.set_value(3.0),
            Create(right_curve),
            run_time=3.5,
            rate_func=smooth
        )
        left_num.remove_updater(update_left)
        right_num.remove_updater(update_right)
        self.wait(0.4)

        # 5. Badges below curves
        left_badge = RoundedRectangle(
            corner_radius=0.1, width=5.2, height=0.5,
            fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN, stroke_width=1.5
        ).move_to([-3.4, -2.4, 0])
        left_badge_txt = Text("ALGORITHM ACTION: RECOMMEND HEAVILY", font="Segoe UI",
                              weight=BOLD, font_size=11, color=GREEN).move_to(left_badge)

        right_badge = RoundedRectangle(
            corner_radius=0.1, width=5.2, height=0.5,
            fill_color=RED, fill_opacity=0.2, stroke_color=RED, stroke_width=1.5
        ).move_to([3.4, -2.4, 0])
        right_badge_txt = Text("ALGORITHM ACTION: SUPPRESS / ZERO IMPRESSIONS", font="Segoe UI",
                               weight=BOLD, font_size=11, color=RED).move_to(right_badge)

        self.play(
            FadeIn(left_badge), FadeIn(left_badge_txt),
            FadeIn(right_badge), FadeIn(right_badge_txt),
            run_time=0.6
        )
        self.wait(0.5)

        # 6. Bottom Takeaway Callout (8.5 - 10.0s)
        callout = Text(
            "The algorithm does not judge the video. It predicts the interaction between video and viewer.",
            font="Segoe UI", weight=BOLD, font_size=15, color=GOLD
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(callout, shift=UP * 0.2), run_time=0.8)
        self.wait(2.0)
