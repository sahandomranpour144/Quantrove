from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class AlgorithmSummaryRulesScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN             = "#10B981"

        title = Text(
            "3 RULES TO TAKE BACK CONTROL",
            font="Segoe UI", weight=BOLD, font_size=40, color=CYAN
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1.0)
        self.wait(0.5)

        levers = [
            dict(num="01",
                 heading="Deliberately seed new topics",
                 body="Search for and watch 100% of a new-topic video."
                      " The model will start predicting new neighbors.",
                 col=GOLD, y=1.3),
            dict(num="02",
                 heading="Engagement quality over quantity",
                 body="Likes, comments, and shares outweigh passive watching."
                      " Active signals are weighted 3-5x by the ranking model.",
                 col=CYAN, y=-0.4),
            dict(num="03",
                 heading="Use 'Not interested' as a scalpel",
                 body="Each dismissal directly updates your embedding vector"
                      " -- it is the fastest feedback signal you have.",
                 col=GREEN, y=-2.1),
        ]

        for lever in levers:
            box = RoundedRectangle(
                corner_radius=0.25, width=13.0, height=1.55,
                fill_color=PANEL_BG, fill_opacity=1,
                stroke_color=lever["col"], stroke_width=2.5
            ).move_to(UP * lever["y"])
            num_lbl = Text(lever["num"], font="Segoe UI", weight=BOLD,
                          font_size=34, color=lever["col"]
                          ).move_to(box.get_left() + RIGHT * 0.95)
            check = Text("✓", font="Segoe UI", weight=BOLD, font_size=26,
                        color=lever["col"]).next_to(num_lbl, LEFT, buff=0.15)
            heading = Text(lever["heading"], font="Segoe UI", weight=BOLD,
                          font_size=17, color=WHITE
                          ).next_to(num_lbl, RIGHT, buff=0.3).shift(UP * 0.27)
            body = Text(lever["body"], font="Segoe UI", font_size=12,
                       color=MUTED).next_to(heading, DOWN, buff=0.1).align_to(heading, LEFT)
            self.play(
                FadeIn(box, shift=RIGHT * 0.3),
                FadeIn(num_lbl), FadeIn(check),
                FadeIn(heading, shift=LEFT * 0.15),
                run_time=0.65
            )
            self.play(FadeIn(body, shift=UP * 0.1), run_time=0.35)
            self.wait(0.4)

        brand = Text(
            "Quantrove -- understand the systems running your world",
            font="Segoe UI", font_size=15, color=MUTED
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(brand), run_time=0.8)
        self.wait(4.0)
