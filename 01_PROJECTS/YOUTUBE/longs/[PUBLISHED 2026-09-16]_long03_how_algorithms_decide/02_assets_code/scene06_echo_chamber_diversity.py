from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class EchoChamberDiversityScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"

        title = Text(
            "EXPLORATION vs. EXPLOITATION: THE FILTER BUBBLE",
            font="Segoe UI", weight=BOLD, font_size=32, color=CYAN
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=1.0)
        self.wait(0.5)

        # Phase 1: Broad interest radar
        broad = Circle(radius=2.4, stroke_color=CYAN, stroke_width=2.5,
                       fill_color="#0F2027", fill_opacity=0.4
                       ).shift(LEFT * 3.2 + DOWN * 0.5)
        broad_lbl = Text("Broad content diet", font="Segoe UI", weight=BOLD,
                        font_size=16, color=CYAN).next_to(broad, UP, buff=0.18)
        colors = [RED, GOLD, GREEN, CYAN, MUTED, WHITE, RED, GOLD, GREEN, CYAN,
                  MUTED, WHITE, RED, GOLD, GREEN, CYAN, MUTED, WHITE, RED, GOLD]
        dots = VGroup(*[
            Dot(broad.point_at_angle(a), radius=0.09, color=colors[i])
            for i, a in enumerate(np.linspace(0, 2 * np.pi, 20, endpoint=False))
        ])
        self.play(Create(broad), FadeIn(broad_lbl),
                  FadeIn(dots, lag_ratio=0.05), run_time=1.5)
        self.wait(0.8)

        # Phase 2: Filter bubble collapse
        bubble = Circle(radius=0.55, stroke_color=RED, stroke_width=3,
                        fill_color="#1F0A0A", fill_opacity=0.7
                        ).move_to(broad.get_center())
        bubble_lbl = Text("Filter bubble", font="Segoe UI", weight=BOLD,
                         font_size=16, color=RED).next_to(bubble, DOWN, buff=0.25)
        bubble_sub = Text("(exploitation only)", font="Segoe UI", font_size=12,
                         color=MUTED).next_to(bubble_lbl, DOWN, buff=0.08)
        self.play(
            Transform(broad, bubble),
            Transform(broad_lbl, bubble_lbl),
            FadeOut(dots),
            run_time=2.0
        )
        self.play(FadeIn(bubble_sub), run_time=0.4)
        self.wait(1.0)

        # Phase 3: Epsilon-greedy exploration
        explore = Circle(radius=2.6, stroke_color=GREEN, stroke_width=2.5,
                         fill_color="#0D1F12", fill_opacity=0.35
                         ).shift(RIGHT * 3.2 + DOWN * 0.5)
        explore_lbl = Text("epsilon-greedy exploration", font="Segoe UI",
                          weight=BOLD, font_size=15, color=GREEN
                          ).next_to(explore, UP, buff=0.18)
        rays = VGroup(*[
            Arrow(explore.get_center(),
                  explore.point_at_angle(a),
                  color=GREEN, stroke_width=2,
                  max_tip_length_to_length_ratio=0.08)
            for a in np.linspace(0, 2 * np.pi, 12, endpoint=False)
        ])
        self.play(Create(explore), FadeIn(explore_lbl), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(r) for r in rays], lag_ratio=0.08), run_time=1.5)
        self.wait(0.8)

        eq_bg = RoundedRectangle(
            corner_radius=0.2, width=8.5, height=1.3,
            fill_color=PANEL_BG, fill_opacity=1,
            stroke_color=GREEN, stroke_width=1.5
        ).to_edge(DOWN, buff=0.3)
        eq = Text(
            "Policy π(a|s): (1 - ε) Exploit Best Known  |  ε Explore New Topics",
            font="Consolas", weight=BOLD, font_size=18, color=GREEN
        ).move_to(eq_bg)
        self.play(FadeIn(eq_bg), FadeIn(eq), run_time=1.5)
        self.wait(4.0)
