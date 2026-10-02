from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class ThreeStageFunnelScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"

        title = Text(
            "THE 3-STAGE FILTERING PIPELINE",
            font="Segoe UI", weight=BOLD, font_size=36, color=CYAN
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1.0)
        self.wait(0.8)

        stages = [
            dict(label="STAGE 1", sub="Candidate Generation",
                 detail="100M  →  1,000", note="ScaNN Retrieval / Two-Tower Model",
                 col=GOLD,  y=1.6,  w=11.0),
            dict(label="STAGE 2", sub="Deep Neural Ranking",
                 detail="1,000  →  50",   note="Dense neural net -- P(watch) score",
                 col=CYAN,  y=-0.2, w=7.5),
            dict(label="STAGE 3", sub="Re-ranking & Diversity",
                 detail="50  →  Final Feed", note="Freshness + diversity injection",
                 col=GREEN, y=-2.0, w=4.5),
        ]

        prev_box = None
        for i, s in enumerate(stages):
            box = RoundedRectangle(
                corner_radius=0.2, width=s["w"], height=1.7,
                fill_color=PANEL_BG, fill_opacity=1,
                stroke_color=s["col"], stroke_width=2.5
            ).move_to(UP * s["y"])
            stg = Text(s["label"], font="Segoe UI", weight=BOLD,
                      font_size=13, color=s["col"]
                      ).move_to(box).shift(LEFT * (s["w"]/2 - 0.7) + UP * 0.35)
            sub_lbl = Text(s["sub"], font="Segoe UI", weight=BOLD,
                          font_size=19, color=WHITE
                          ).next_to(stg, RIGHT, buff=0.3).shift(UP * 0.02)
            detail = Text(s["detail"], font="Segoe UI", weight=BOLD,
                         font_size=20, color=s["col"]
                         ).move_to(box).shift(RIGHT * (s["w"]/2 - 1.4) + UP * 0.35)
            note = Text(s["note"], font="Segoe UI", font_size=12,
                       color=MUTED).move_to(box).shift(DOWN * 0.35)
            group = VGroup(box, stg, sub_lbl, detail, note)
            self.play(FadeIn(group, shift=RIGHT * 0.2), run_time=0.8)
            if i < 2:
                arr = Arrow(
                    ORIGIN + UP * (s["y"] - 0.85),
                    ORIGIN + UP * (stages[i + 1]["y"] + 0.85),
                    color=MUTED, stroke_width=2.5,
                    max_tip_length_to_length_ratio=0.1
                )
                self.play(GrowArrow(arr), run_time=0.5)

        self.wait(1.0)

        eq_bg = RoundedRectangle(
            corner_radius=0.2, width=10.2, height=1.2,
            fill_color="#1E293B", fill_opacity=1,
            stroke_color=CYAN, stroke_width=1.5
        ).to_edge(DOWN, buff=0.3)
        eq = Text(
            "Score = P(click) × w₁  +  P(watch) × w₂  +  P(like) × w₃",
            font="Consolas", weight=BOLD, font_size=20, color=CYAN
        ).move_to(eq_bg)
        self.play(FadeIn(eq_bg), FadeIn(eq), run_time=1.5)
        self.wait(4.0)
