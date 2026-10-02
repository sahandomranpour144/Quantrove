from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class LeadLagParadoxScene(Scene):
    def construct(self):
        # Target total duration: Exactly 30.0 seconds
        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"

        # 1. Header (0.0s - 3.0s) -> 3.0s
        title = Text("PATTERN #1: THE LEAD-LAG PARADOX", font_size=36, font="Segoe UI", weight=BOLD, color=CYAN)
        subtitle = Text("MARKETS ARE FORWARD-LOOKING (6–9 MONTHS AHEAD)", font_size=19, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.45)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # 2. Axes & Recession Shading (3.0s - 9.0s) -> 6.0s
        axes = Axes(
            x_range=[-12, 14, 2],
            y_range=[40, 130, 20],
            x_length=11.0,
            y_length=4.5,
            axis_config={"color": MUTED, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.4)

        x_lbl = Text("Months Relative to Official Recession End (0 = Recovery Date)", font_size=13, font="Segoe UI", color=MUTED).next_to(axes, DOWN, buff=0.3)
        y_lbl = Text("S&P 500 Normalized Level", font_size=13, font="Segoe UI", color=MUTED).next_to(axes, LEFT, buff=0.3).rotate(PI/2)

        p_start = axes.c2p(-12, 40)
        p_end = axes.c2p(0, 130)
        w = p_end[0] - p_start[0]
        h = p_end[1] - p_start[1]
        rec_band = Rectangle(width=w, height=h, fill_color="#334155", fill_opacity=0.45, stroke_color=PANEL_BORDER, stroke_width=1)
        rec_band.move_to([(p_start[0] + p_end[0])/2, (p_start[1] + p_end[1])/2, 0])

        rec_tag = Text("Recession Window", font_size=13, font="Segoe UI", color=MUTED).next_to(rec_band.get_top(), DOWN, buff=0.2)

        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), FadeIn(rec_band), FadeIn(rec_tag), run_time=2.2)
        self.wait(3.8)

        # 3. Stock Price Curve Draw & Generational Bottom (9.0s - 19.0s) -> 10.0s
        def price_func(t):
            if t < -4:
                return 100 - 45 * np.exp(-((t + 4)/5.0)**2)
            else:
                return 55 + 3.8 * (t + 4)

        curve = axes.plot(price_func, x_range=[-12, 12], color=CYAN, stroke_width=3.5)

        self.play(Create(curve), run_time=3.5)

        pt_bottom = axes.c2p(-4, 55)
        d_bottom = Dot(pt_bottom, color=GREEN, radius=0.18)
        ring_bottom = Circle(radius=0.4, color=GREEN, stroke_width=2.5).move_to(pt_bottom)
        lbl_bottom = Text("MARKET BOTTOMS HERE\n(3–5 Months Before Economy Ends!)", font_size=13, font="Segoe UI", weight=BOLD, color=GREEN, line_spacing=1.2).next_to(d_bottom, UP, buff=0.4)

        self.play(FadeIn(d_bottom), Create(ring_bottom), FadeIn(lbl_bottom, shift=UP), run_time=1.5)
        self.play(ring_bottom.animate.scale(1.8).set_stroke_opacity(0), run_time=1.5)
        self.wait(3.5)

        # 4. March 2009 Deep-Dive Case Study (19.0s - 30.0s) -> 11.0s
        case_card = RoundedRectangle(corner_radius=0.15, height=1.4, width=10.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=GOLD, stroke_width=2).shift(DOWN * 1.8)
        case_title = Text("CASE STUDY: MARCH 9, 2009 GENERATIONAL BOTTOM", font_size=15, font="Segoe UI", weight=BOLD, color=GOLD).next_to(case_card.get_top(), DOWN, buff=0.25)
        case_desc = Text(
            "• Market bottomed on March 9, 2009 while unemployment was still skyrocketing to 10%.\n• Next 12 Months: S&P 500 surged +68% while news headlines were pure panic.",
            font_size=12, font="Segoe UI", color=WHITE, line_spacing=1.3
        ).next_to(case_title, DOWN, buff=0.18)

        self.play(FadeIn(case_card, shift=UP), FadeIn(case_title, shift=UP), FadeIn(case_desc, shift=UP), run_time=1.8)
        self.wait(9.2)
