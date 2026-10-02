from manim import *
import numpy as np

# Quantrove Theme Colors
COLOR_BG = "#0B0F19"
COLOR_CYAN = "#00F0FF"
COLOR_MINT = "#00FFA3"
COLOR_GOLD = "#FFD700"
COLOR_CRIMSON = "#FF3366"
COLOR_WHITE = "#F8FAFC"
COLOR_MUTED = "#94A3B8"
COLOR_CARD_BG = "#131B2E"

# High-resolution CleanText to eliminate Pango sub-pixel advance quantization / character scattering
def CleanText(text, font="Segoe UI", font_size=24, **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    return Text(text, font=font, font_size=ref_size, **kwargs).scale(scale_factor)

# Render target: TIMELINE_MEDIA/03_T02-29_to_03-00_manim_alpha_decay.mp4
# Timeline window 02:29-03:00 -> EXACT duration 31.0s (1080p60).
# Visual: Excess return decaying from +12% to flatline equilibrium as
# competing algorithmic capital swarms the trade. (Scene 3)


class AlphaDecayScene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ---- Definition badge (t 0.0 - 3.0) ----
        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.2, height=1.1,
                                     fill_color=COLOR_CARD_BG, fill_opacity=0.9,
                                     stroke_color=COLOR_CYAN, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("PATTERN #1: ALPHA DECAY", weight="BOLD",
                                font_size=24, color=COLOR_CYAN).next_to(badge_bg.get_top(), DOWN, buff=0.15)
        badge_sub = CleanText("Alpha = The excess return a strategy generates above the market",
                              font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        # ---- Axes (t 3.0 - 5.5) ----
        def alpha_f(t):
            return 12.0 * np.exp(-0.45 * t) + 0.3

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 14, 2],
            x_length=8.8, y_length=4.2,
            axis_config={"color": COLOR_MUTED, "stroke_width": 2},
            tips=True,
        ).shift(DOWN * 0.9)
        x_label = CleanText("TIME  →  COMPETITORS DISCOVER THE TRADE", font_size=15,
                            color=COLOR_MUTED).next_to(axes.x_axis, DOWN, buff=0.22)
        y_label = CleanText("EXCESS RETURN (%)", font_size=15,
                            color=COLOR_MUTED).next_to(axes.y_axis, UP, buff=0.15)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=2.0)
        self.wait(0.5)

        # ---- Decay curve + discovery label (t 5.5 - 10.0) ----
        alpha_graph = axes.plot(alpha_f, color=COLOR_MINT, stroke_width=4)
        start_dot = Dot(axes.c2p(0.25, alpha_f(0.25)), color=COLOR_GOLD, radius=0.12)
        start_label = CleanText("+12.0% AT DISCOVERY", weight="BOLD",
                                font_size=16, color=COLOR_GOLD).next_to(start_dot, RIGHT, buff=0.25)
        self.play(Create(alpha_graph), run_time=2.5)
        self.play(Create(start_dot), FadeIn(start_label), run_time=1.5)
        self.wait(0.5)

        # ---- Competing capital wave 1 (t 10.0 - 13.0) ----
        wave1 = VGroup(*[Dot(axes.c2p(t, alpha_f(t)), color=COLOR_CRIMSON, radius=0.09)
                         for t in [2.0, 3.5, 5.0, 6.8]])
        wave1_label = CleanText("COMPETING CAPITAL", font_size=13,
                                color=COLOR_CRIMSON).next_to(wave1[0], UP, buff=0.18)
        self.play(LaggedStartMap(FadeIn, wave1, lag_ratio=0.35), FadeIn(wave1_label), run_time=2.5)
        self.wait(0.5)

        # ---- Wave 2: swarm intensifies (t 13.0 - 16.5) ----
        wave2 = VGroup(*[Dot(axes.c2p(t, alpha_f(t)), color=COLOR_CRIMSON,
                             radius=0.07, fill_opacity=0.7)
                         for t in [1.0, 2.7, 4.2, 5.7, 7.5]])
        self.play(LaggedStartMap(FadeIn, wave2, lag_ratio=0.2),
                  Indicate(alpha_graph, color=COLOR_CRIMSON, scale_factor=1.02), run_time=2.5)
        self.wait(1.0)

        # ---- Edge counter card: +12.0% -> 0.0% (t 16.5 - 21.0) ----
        card = RoundedRectangle(corner_radius=0.15, width=4.6, height=1.0,
                                fill_color=COLOR_CARD_BG, fill_opacity=0.95,
                                stroke_color=COLOR_MUTED, stroke_width=1.5
                                ).to_edge(DOWN, buff=0.4).shift(LEFT * 3.4)
        card_label = CleanText("STRATEGY EDGE", font_size=13,
                               color=COLOR_MUTED).move_to(card.get_top() + DOWN * 0.18)
        step1 = CleanText("+12.0%", weight="BOLD", font_size=30, color=COLOR_WHITE)
        step2 = CleanText("+2.1%", weight="BOLD", font_size=30, color=COLOR_WHITE)
        step3 = CleanText("+0.0%", weight="BOLD", font_size=30, color=COLOR_CRIMSON)
        step1.next_to(card_label, DOWN, buff=0.08)
        step2.move_to(step1)
        step3.move_to(step1)
        self.play(FadeIn(card), FadeIn(card_label), FadeIn(step1), run_time=1.0)
        self.wait(0.5)
        self.play(Transform(step1, step2), run_time=1.0)
        self.wait(0.5)
        self.play(Transform(step1, step3), run_time=1.0)
        self.wait(0.5)

        # ---- Equilibrium (t 21.0 - 24.0) ----
        end_dot = Dot(axes.c2p(9.0, alpha_f(9.0)), color=COLOR_CRIMSON, radius=0.14)
        end_box = RoundedRectangle(corner_radius=0.1, width=3.8, height=0.85,
                                   fill_color=COLOR_CARD_BG, fill_opacity=0.95,
                                   stroke_color=COLOR_CRIMSON, stroke_width=2
                                   ).move_to(axes.c2p(7.6, 4.6))
        end_text = CleanText("EQUILIBRIUM — EDGE = 0.0%", weight="BOLD",
                             font_size=15, color=COLOR_CRIMSON).move_to(end_box)
        self.play(Create(end_dot), FadeIn(end_box), Write(end_text), run_time=2.0)
        self.wait(1.0)

        # ---- Flatline flash (t 24.0 - 26.0) ----
        self.play(Flash(end_dot, color=COLOR_CRIMSON, flash_radius=0.6,
                        line_length=0.3, num_lines=12), run_time=1.0)
        self.wait(1.0)

        # ---- Final emphasis (t 26.0 - 31.0) ----
        self.play(Circumscribe(end_box, color=COLOR_CRIMSON, time_width=1.0), run_time=1.5)
        self.wait(3.5)
