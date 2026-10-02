from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class TransformerAttentionScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"

        title = Text(
            "SEQUENTIAL ATTENTION: HOW THE ALGORITHM READS YOUR HISTORY",
            font="Segoe UI", weight=BOLD, font_size=26, color=CYAN
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=1.0)
        self.wait(0.5)

        actions = [
            ("3s skip",    RED,   "Bored"),
            ("100% watch", GREEN, "Loved"),
            ("Re-watch",   CYAN,  "Key"),
            ("Like",       GOLD,  "Endorsed"),
            ("3s skip",    RED,   "Bored"),
            ("Share",      GREEN, "High value"),
            ("60% watch",  MUTED, "Neutral"),
            ("Subscribe",  GOLD,  "Convert"),
            ("Comment",    CYAN,  "Engaged"),
            ("3s skip",    RED,   "Bored"),
        ]
        n = len(actions)
        xs = np.linspace(-5.8, 5.8, n)

        node_groups = []
        for (lbl, col, tip), x in zip(actions, xs):
            dot = Circle(radius=0.30, fill_color=col, fill_opacity=0.2,
                         stroke_color=col, stroke_width=2.5).move_to(RIGHT * x + UP * 1.2)
            t = Text(lbl, font="Segoe UI", weight=BOLD, font_size=9,
                    color=col).next_to(dot, DOWN, buff=0.1)
            node_groups.append(VGroup(dot, t))
        self.play(*[FadeIn(g) for g in node_groups], lag_ratio=0.12, run_time=2.0)
        self.wait(0.5)

        arc_pairs = [(1, 3), (3, 7), (1, 7), (3, 8)]
        for (i, j) in arc_pairs:
            arc = CurvedArrow(
                node_groups[i][0].get_top() + UP * 0.05,
                node_groups[j][0].get_top() + UP * 0.05,
                angle=-PI / 3, color=GOLD, stroke_width=1.8
            )
            self.play(Create(arc), run_time=0.35)
        self.wait(0.5)

        matrix_bg = RoundedRectangle(
            corner_radius=0.2, width=10.0, height=2.0,
            fill_color=PANEL_BG, fill_opacity=1,
            stroke_color=CYAN, stroke_width=1.5
        ).shift(DOWN * 1.8)
        m_title = Text("Self-Attention Weight Matrix", font="Segoe UI",
                      weight=BOLD, font_size=15, color=CYAN
                      ).move_to(matrix_bg).shift(UP * 0.6)
        m_eq = Text("Attention(Q, K, V) = softmax( (Q · Kᵀ) / √dₖ ) · V",
                   font="Consolas", weight=BOLD, font_size=20, color=WHITE
                   ).move_to(matrix_bg).shift(DOWN * 0.2)
        self.play(FadeIn(matrix_bg), FadeIn(m_title), FadeIn(m_eq), run_time=1.5)
        self.wait(4.0)
