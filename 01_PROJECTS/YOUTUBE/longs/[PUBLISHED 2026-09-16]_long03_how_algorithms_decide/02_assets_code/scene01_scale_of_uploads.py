from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class ScaleOfUploadsScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG, RED = "#94A3B8", "#151B26", "#EF4444"

        # 1. Header (0.0 - 2.5s)
        title = Text(
            "THE SCALE OF THE PROBLEM",
            font="Segoe UI", weight=BOLD, font_size=40, color=CYAN
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1.0)
        self.wait(1.5)

        # 2. Dual stat panels (2.5 - 6.5s)
        def panel(val, lbl, sub, col, pos):
            box = RoundedRectangle(
                corner_radius=0.2, width=5.2, height=2.5,
                fill_color=PANEL_BG, fill_opacity=1,
                stroke_color=col, stroke_width=2
            ).move_to(pos)
            v = Text(val, font="Segoe UI", weight=BOLD, font_size=52,
                     color=col).move_to(box).shift(UP * 0.35)
            l = Text(lbl, font="Segoe UI", font_size=15,
                     color=WHITE).next_to(v, DOWN, buff=0.12)
            s = Text(sub, font="Segoe UI", font_size=12,
                     color=MUTED).next_to(l, DOWN, buff=0.08)
            return VGroup(box, v, l, s)

        p1 = panel("500 / min", "hours of video uploaded every minute",
                   "nonstop, every platform, right now", GOLD, LEFT * 3 + DOWN * 0.5)
        p2 = panel("700,000", "hours in a human lifetime (80 yrs)",
                   "sleeping 8 hours every night", CYAN, RIGHT * 3 + DOWN * 0.5)
        self.play(FadeIn(p1, shift=RIGHT * 0.4), FadeIn(p2, shift=LEFT * 0.4), run_time=1.5)
        self.wait(2.5)

        # 3. Live counter (6.5 - 12.5s)
        lbl = Text("Hours uploaded while you have been watching:",
                   font="Segoe UI", font_size=17, color=MUTED).to_edge(DOWN, buff=1.9)
        tracker = ValueTracker(0.0)
        num = Text("0.0", font="Segoe UI", weight=BOLD, font_size=68,
                   color=GOLD).next_to(lbl, DOWN, buff=0.3)
        unit = Text("hours", font="Segoe UI", font_size=24,
                    color=MUTED).next_to(num, RIGHT, buff=0.22)

        def update_num(mob):
            val = tracker.get_value()
            new_mob = Text(f"{val:.1f}", font="Segoe UI", weight=BOLD,
                          font_size=68, color=GOLD).next_to(lbl, DOWN, buff=0.3)
            mob.become(new_mob)
        num.add_updater(update_num)

        def update_unit(mob):
            mob.next_to(num, RIGHT, buff=0.22)
        unit.add_updater(update_unit)

        self.play(FadeIn(lbl), FadeIn(num), FadeIn(unit), run_time=0.8)
        self.play(tracker.animate.set_value(50.0), run_time=5.0, rate_func=linear)
        num.remove_updater(update_num)
        unit.remove_updater(update_unit)
        self.wait(0.2)

        # 4. Insight callout (12.5 - 18.0s)
        insight_line1 = Text("The algorithm decides what YOU see", font="Segoe UI",
                            font_size=22, color=WHITE, t2c={"YOU": CYAN})
        insight_line2 = Text("among billions of candidates in under 50ms.",
                            font="Segoe UI", font_size=22, color=WHITE, t2c={"50ms": RED})
        insight = VGroup(insight_line1, insight_line2).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.45)
        self.play(FadeOut(lbl, num, unit), FadeIn(insight, shift=UP * 0.3), run_time=1.2)
        self.wait(4.3)
