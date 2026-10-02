from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class TwoTowerVectorSpaceScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"

        # 1. Title (0 - 2s)
        title = Text(
            "HOW THE ALGORITHM FILTERS 100M TO 1,000 IN 50ms",
            font="Segoe UI", weight=BOLD, font_size=32, color=CYAN
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1.0)
        self.wait(1.0)

        # 2. Two tower boxes (2 - 8s)
        user_box = RoundedRectangle(
            corner_radius=0.3, width=4.2, height=4.8,
            fill_color=PANEL_BG, fill_opacity=1,
            stroke_color=CYAN, stroke_width=2.5
        ).shift(LEFT * 4.0 + DOWN * 0.5)
        item_box = RoundedRectangle(
            corner_radius=0.3, width=4.2, height=4.8,
            fill_color=PANEL_BG, fill_opacity=1,
            stroke_color=GOLD, stroke_width=2.5
        ).shift(RIGHT * 4.0 + DOWN * 0.5)

        u_lbl = Text("USER TOWER", font="Segoe UI", weight=BOLD,
                     font_size=18, color=CYAN).move_to(user_box).shift(UP * 1.8)
        i_lbl = Text("ITEM TOWER", font="Segoe UI", weight=BOLD,
                     font_size=18, color=GOLD).move_to(item_box).shift(UP * 1.8)

        u_inputs = VGroup(
            Text("Watch history",   font="Segoe UI", font_size=14, color=MUTED),
            Text("Session context", font="Segoe UI", font_size=14, color=MUTED),
            Text("Search queries",  font="Segoe UI", font_size=14, color=MUTED),
            Text("Demographics",    font="Segoe UI", font_size=14, color=MUTED),
        ).arrange(DOWN, buff=0.28).move_to(user_box).shift(DOWN * 0.2)

        i_inputs = VGroup(
            Text("Title / tags",    font="Segoe UI", font_size=14, color=MUTED),
            Text("CTR history",     font="Segoe UI", font_size=14, color=MUTED),
            Text("Avg watch time",  font="Segoe UI", font_size=14, color=MUTED),
            Text("Freshness",       font="Segoe UI", font_size=14, color=MUTED),
        ).arrange(DOWN, buff=0.28).move_to(item_box).shift(DOWN * 0.2)

        self.play(
            FadeIn(user_box), FadeIn(item_box),
            FadeIn(u_lbl), FadeIn(i_lbl),
            run_time=1.0
        )
        self.play(
            FadeIn(u_inputs, lag_ratio=0.3),
            FadeIn(i_inputs, lag_ratio=0.3),
            run_time=1.5
        )
        self.wait(0.8)

        # 3. Embedding vectors converge (8 - 14s)
        u_arrow = Arrow(user_box.get_right(), LEFT * 0.8 + DOWN * 0.5,
                        color=CYAN, stroke_width=4, max_tip_length_to_length_ratio=0.08)
        i_arrow = Arrow(item_box.get_left(), RIGHT * 0.8 + DOWN * 0.5,
                        color=GOLD, stroke_width=4, max_tip_length_to_length_ratio=0.08)
        u_v_lbl = Text("user vector", font="Segoe UI", font_size=13,
                       color=CYAN).next_to(u_arrow, UP, buff=0.1)
        i_v_lbl = Text("item vector", font="Segoe UI", font_size=13,
                       color=GOLD).next_to(i_arrow, UP, buff=0.1)
        self.play(GrowArrow(u_arrow), FadeIn(u_v_lbl), run_time=0.8)
        self.play(GrowArrow(i_arrow), FadeIn(i_v_lbl), run_time=0.8)
        self.wait(0.5)

        # 4. Similarity score (14 - 20s)
        score_bg = RoundedRectangle(
            corner_radius=0.25, width=4.8, height=1.5,
            fill_color="#1E293B", fill_opacity=1,
            stroke_color=GREEN, stroke_width=2
        ).move_to(DOWN * 0.5)
        score_eq = Text("score = u · v = ∑ (uᵢ · vᵢ)", font="Consolas",
                       weight=BOLD, font_size=24, color=GREEN).move_to(score_bg)
        self.play(FadeIn(score_bg), FadeIn(score_eq), run_time=1.5)
        self.wait(1.0)

        # 5. Result callout (20 - 28s)
        result = Text("100,000,000 videos  →  1,000 candidates  →  ~50ms",
                     font="Segoe UI", weight=BOLD, font_size=20, color=WHITE,
                     t2c={"100,000,000": RED, "1,000": GREEN, "~50ms": CYAN}
                     ).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(result, shift=UP * 0.3), run_time=0.8)
        self.wait(4.0)
