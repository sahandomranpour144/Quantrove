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

# Render target: TIMELINE_MEDIA/02_T01-26_to_01-50_manim_bell_curve_5075.mp4
# Timeline window 01:26-01:50 -> EXACT duration 24.0s (1080p60).
# Visual: Normal-distribution bell curve, glowing gold line at 50.75% win-rate,
# tiny gold sliver of edge past the coin-flip center, compounding counter
# $1,000 (1988) -> $42,000,000 TODAY. (Scene 2, Part 1)


class BellCurve5075Scene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ---- Definition badge (t 0.0 - 3.0) ----
        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.8, height=1.15,
                                     fill_color=COLOR_CARD_BG, fill_opacity=0.9,
                                     stroke_color=COLOR_GOLD, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("THE 50.75% EDGE", weight="BOLD",
                                font_size=26, color=COLOR_GOLD).next_to(badge_bg.get_top(), DOWN, buff=0.12)
        badge_sub = CleanText("Barely better than a coin flip — compounded for 30 years",
                              font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        # ---- Axes: win-rate per trade (t 3.0 - 5.0) ----
        def bell(x):
            return (1.0 / (0.02 * np.sqrt(2 * np.pi))) * np.exp(-((x - 0.5) ** 2) / (2 * 0.02 ** 2))

        axes = Axes(
            x_range=[0.40, 0.60, 0.05],
            y_range=[0, 22],
            x_length=7.4, y_length=3.1,
            axis_config={"color": COLOR_MUTED, "stroke_width": 2},
            y_axis_config={"include_ticks": False},
            tips=False,
        ).shift(DOWN * 0.55)
        x_label = CleanText("MODEL WIN RATE PER TRADE", font_size=15,
                            color=COLOR_MUTED).next_to(axes.x_axis, DOWN, buff=0.3)
        self.play(Create(axes), FadeIn(x_label), run_time=1.5)
        self.wait(0.5)

        # ---- Bell curve (t 5.0 - 8.0) ----
        curve = axes.plot(bell, color=COLOR_CYAN, stroke_width=4)
        self.play(Create(curve), run_time=2.5)
        self.wait(0.5)

        # ---- Coin-flip center line (t 8.0 - 10.0) ----
        coin_line = DashedLine(axes.c2p(0.50, 0), axes.c2p(0.50, bell(0.50)),
                                color=COLOR_MUTED, stroke_width=2, dash_length=0.06)
        coin_label = CleanText("50% COIN FLIP", font_size=14,
                               color=COLOR_MUTED).next_to(coin_line.get_end(), LEFT, buff=0.15)
        self.play(Create(coin_line), FadeIn(coin_label), run_time=1.5)
        self.wait(0.5)

        # ---- Glowing 50.75% line (t 10.0 - 12.0) ----
        glow_wide = Line(axes.c2p(0.5075, 0), axes.c2p(0.5075, bell(0.5075)),
                         color=COLOR_GOLD, stroke_width=16).set_stroke(opacity=0.18)
        glow_mid = Line(axes.c2p(0.5075, 0), axes.c2p(0.5075, bell(0.5075)),
                        color=COLOR_GOLD, stroke_width=7).set_stroke(opacity=0.35)
        edge_line = Line(axes.c2p(0.5075, 0), axes.c2p(0.5075, bell(0.5075)),
                         color=COLOR_GOLD, stroke_width=4)
        edge_label = CleanText("50.75%", weight="BOLD", font_size=22,
                               color=COLOR_GOLD).next_to(edge_line.get_end(), RIGHT, buff=0.15)
        self.play(Create(glow_wide), Create(glow_mid), Create(edge_line), Write(edge_label), run_time=1.5)
        self.wait(0.5)

        # ---- Gold sliver of edge (t 12.0 - 14.0) ----
        region_pts = [axes.c2p(0.5075, 0)] + \
            [axes.c2p(x, bell(x)) for x in np.linspace(0.5075, 0.60, 80)] + \
            [axes.c2p(0.60, 0)]
        edge_region = Polygon(*region_pts, fill_color=COLOR_GOLD,
                               fill_opacity=0.22, stroke_width=0)
        edge_region_label = CleanText("TINY SLIVER OF EDGE", weight="BOLD", font_size=13,
                                      color=COLOR_GOLD).move_to(axes.c2p(0.556, 3.2))
        self.play(FadeIn(edge_region), FadeIn(edge_region_label), run_time=1.0)
        self.wait(1.0)

        # ---- Compounding counter card (t 14.0 - 21.0) ----
        card = RoundedRectangle(corner_radius=0.18, width=8.8, height=1.5,
                                fill_color=COLOR_CARD_BG, fill_opacity=0.95,
                                stroke_color=COLOR_MINT, stroke_width=1.5).to_edge(DOWN, buff=0.45)
        step1 = CleanText("$1,000   ·   1988", font_size=30, color=COLOR_WHITE)
        step2 = CleanText("$205,000   ·   2007", font_size=30, color=COLOR_WHITE)
        step3 = CleanText("$42,000,000   ·   TODAY", weight="BOLD",
                          font_size=34, color=COLOR_MINT)
        annual_label = CleanText("+66% AVERAGE ANNUAL RETURN — RENAISSANCE MEDALLION FUND",
                                 font_size=14, color=COLOR_MUTED)
        counter_group = VGroup(step1, annual_label).arrange(DOWN, buff=0.18).move_to(card)
        step2.move_to(step1)
        step3.move_to(step1)

        self.play(FadeIn(card), FadeIn(counter_group), run_time=1.0)
        self.wait(0.5)
        self.play(Transform(step1, step2), run_time=1.0)
        self.wait(0.5)
        self.play(Transform(step1, step3), run_time=1.0)
        self.wait(0.5)

        # ---- Final caption (t 18.5 - 24.0) ----
        caption = CleanText("MILLIONS OF MICRO-TRADES  ×  A TINY EDGE  =  BILLIONS",
                            weight="BOLD", font_size=18, color=COLOR_MINT)
        caption.move_to(annual_label)
        self.play(FadeOut(annual_label), Write(caption), run_time=1.5)
        self.wait(1.0)
        self.play(Indicate(step3, color=COLOR_MINT, scale_factor=1.08), run_time=1.0)
        self.wait(2.0)
