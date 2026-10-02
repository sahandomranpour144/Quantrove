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

# Render target: TIMELINE_MEDIA/02_T02-00_to_02-29_manim_reflexivity.mp4
# Timeline window 02:00-02:29 -> EXACT duration 29.0s (1080p60).
# Visual: Split comparison. Left: invariant 4x4 pixel grid (stationary data).
# Right: stock curve that reflexively DODGES the AI prediction as capital
# orders flow in. (Scene 2, Part 2)


class ReflexivityScene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ---- Definition badge (t 0.0 - 3.0) ----
        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.5, height=1.1,
                                    fill_color=COLOR_CARD_BG, fill_opacity=0.9,
                                    stroke_color=COLOR_GOLD, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("REFLEXIVITY IN FINANCIAL MARKETS", weight="BOLD",
                                font_size=24, color=COLOR_GOLD).next_to(badge_bg.get_top(), DOWN, buff=0.15)
        badge_sub = CleanText("When a market's price changes because people & algorithms act on predictions",
                              font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        # ---- Left column: stationary problem (t 3.0 - 6.0) ----
        left_box = RoundedRectangle(corner_radius=0.2, width=5.6, height=4.6,
                                    fill_color=COLOR_CARD_BG, fill_opacity=0.6,
                                    stroke_color=COLOR_CYAN, stroke_width=1.5).shift(LEFT * 3.3 + DOWN * 0.7)
        left_header = CleanText("1. STATIONARY DATA (IMAGES/CHESS)", weight="BOLD",
                                font_size=18, color=COLOR_CYAN).next_to(left_box.get_top(), DOWN, buff=0.25)

        grid_vg = VGroup()
        for r in range(4):
            for c in range(4):
                sq = Square(side_length=0.42, stroke_color=COLOR_CYAN, stroke_width=1,
                            fill_color=COLOR_CYAN, fill_opacity=0.15 if (r + c) % 2 == 0 else 0.4)
                sq.move_to(left_box.get_center() + RIGHT * (c - 1.5) * 0.48
                           + DOWN * (r - 1.5) * 0.48 + UP * 0.1)
                grid_vg.add(sq)

        left_status = CleanText("PHYSICAL RULES NEVER MUTATE", font_size=16,
                                color=COLOR_MINT).next_to(grid_vg, DOWN, buff=0.35)

        self.play(Create(left_box), Write(left_header),
                  FadeIn(grid_vg, lag_ratio=0.05), FadeIn(left_status), run_time=2.0)
        self.wait(1.0)

        # ---- Right column: reflexive system (t 6.0 - 11.0) ----
        right_box = RoundedRectangle(corner_radius=0.2, width=5.6, height=4.6,
                                     fill_color=COLOR_CARD_BG, fill_opacity=0.6,
                                     stroke_color=COLOR_CRIMSON, stroke_width=1.5).shift(RIGHT * 3.3 + DOWN * 0.7)
        right_header = CleanText("2. REFLEXIVE SYSTEM (STOCK PRICES)", weight="BOLD",
                                 font_size=18, color=COLOR_CRIMSON).next_to(right_box.get_top(), DOWN, buff=0.25)

        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 10, 2],
            x_length=4.2, y_length=2.5,
            axis_config={"color": COLOR_MUTED, "stroke_width": 1.5},
            tips=False,
        ).move_to(right_box.get_center() + UP * 0.1)

        t_vals = np.linspace(0, 10, 100)
        p_vals = 4.5 + 1.8 * np.sin(t_vals * 0.7)
        curve_orig = axes.plot(lambda x: np.interp(x, t_vals, p_vals),
                               color=COLOR_CYAN, stroke_width=3)

        pred_line = DashedLine(axes.c2p(2, 5.5), axes.c2p(7, 8.2),
                               color=COLOR_GOLD, stroke_width=3)
        pred_label = CleanText("AI PREDICTION VECTOR", font_size=13,
                               color=COLOR_GOLD).next_to(pred_line, UP, buff=0.1)

        self.play(Create(right_box), Write(right_header), Create(axes), Create(curve_orig), run_time=2.5)
        self.wait(0.5)
        self.play(Create(pred_line), FadeIn(pred_label), run_time=1.5)
        self.wait(0.5)

        # ---- Capital orders flow in (t 11.0 - 14.0) ----
        inflow_vg = VGroup()
        for (tx, ty) in [(5.2, 9.0), (6.0, 8.6), (6.8, 9.0), (7.6, 8.4), (8.4, 8.8)]:
            d = Dot(axes.c2p(tx, ty), color=COLOR_CRIMSON, radius=0.09)
            inflow_vg.add(d)
        inflow_label = CleanText("CAPITAL ORDERS FLOW IN", font_size=12,
                                 color=COLOR_CRIMSON).next_to(inflow_vg, UP, buff=0.12)
        self.play(LaggedStartMap(FadeIn, inflow_vg, lag_ratio=0.25),
                  FadeIn(inflow_label), run_time=2.5)
        self.wait(0.5)

        # ---- Market dodges the prediction (t 14.0 - 17.0) ----
        p_mutated = 4.5 + 1.8 * np.sin(t_vals * 0.7) - 2.5 * np.exp(-((t_vals - 6) ** 2) / 3.0)
        curve_mutated = axes.plot(lambda x: np.interp(x, t_vals, p_mutated),
                                  color=COLOR_CRIMSON, stroke_width=3.5)
        right_status = CleanText("SIGNAL ERASED BY CAPITAL FLOW", font_size=15,
                                 color=COLOR_CRIMSON).next_to(axes, DOWN, buff=0.25)
        self.play(Transform(curve_orig, curve_mutated),
                  FadeOut(pred_line), FadeOut(pred_label),
                  FadeOut(inflow_vg), FadeOut(inflow_label),
                  FadeIn(right_status), run_time=2.5)
        self.wait(0.5)

        # ---- Verdict badges (t 17.0 - 20.0) ----
        def make_tick(color):
            a, b, c = LEFT * 0.12 + DOWN * 0.02, ORIGIN + DOWN * 0.14, RIGHT * 0.16 + UP * 0.10
            g = VGroup(Line(a, b, color=color, stroke_width=4),
                       Line(b, c, color=color, stroke_width=4))
            return g

        def make_cross(color):
            g = VGroup(Line(LEFT * 0.14 + UP * 0.14, RIGHT * 0.14 + DOWN * 0.14,
                            color=color, stroke_width=4),
                       Line(LEFT * 0.14 + DOWN * 0.14, RIGHT * 0.14 + UP * 0.14,
                            color=color, stroke_width=4))
            return g

        left_verdict = VGroup(CleanText("RULES STAY FIXED", font_size=15, color=COLOR_MINT),
                              make_tick(COLOR_MINT)
                              ).arrange(RIGHT, buff=0.2).next_to(left_status, DOWN, buff=0.25)
        right_verdict = VGroup(CleanText("MARKET MUTATES", font_size=15, color=COLOR_CRIMSON),
                               make_cross(COLOR_CRIMSON)
                               ).arrange(RIGHT, buff=0.2).next_to(right_status, DOWN, buff=0.18)
        self.play(FadeIn(left_verdict, shift=UP * 0.2), FadeIn(right_verdict, shift=UP * 0.2), run_time=2.0)
        self.wait(1.0)

        # ---- Second capital wave: market dodges again (t 20.0 - 23.5) ----
        wave2 = VGroup(*[Dot(axes.c2p(tx, 8.7), color=COLOR_CRIMSON, radius=0.07, fill_opacity=0.75)
                         for tx in [4.4, 5.6, 6.9, 8.1]])
        p_mut2 = (4.5 + 1.8 * np.sin(t_vals * 0.7)
                  - 2.5 * np.exp(-((t_vals - 6) ** 2) / 3.0)
                  - 2.0 * np.exp(-((t_vals - 2.8) ** 2) / 2.2))
        curve_mut2 = axes.plot(lambda x: np.interp(x, t_vals, p_mut2),
                              color=COLOR_CRIMSON, stroke_width=4)
        self.play(LaggedStartMap(FadeIn, wave2, lag_ratio=0.2), run_time=2.5)
        self.play(Transform(curve_orig, curve_mut2), FadeOut(wave2), run_time=1.0)
        self.wait(1.0)

        # ---- Emphasis + final caption (t 23.5 - 29.0) ----
        self.play(Indicate(left_header, color=COLOR_CYAN, scale_factor=1.05),
                  Indicate(right_header, color=COLOR_CRIMSON, scale_factor=1.05), run_time=1.5)
        self.wait(1.0)
        caption = CleanText("PREDICTING THE PRICE  CHANGES  THE PRICE", weight="BOLD",
                            font_size=20, color=COLOR_GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(caption), run_time=1.5)
        self.wait(0.5)
