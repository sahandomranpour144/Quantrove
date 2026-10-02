import os
import sys
import numpy as np
from manim import *
import matplotlib.font_manager as fm

# Add Nohemi fonts
for f in ["assets/fonts/Nohemi-Bold.ttf", "assets/fonts/Nohemi-Medium.ttf", "assets/fonts/Nohemi-Regular.ttf"]:
    if os.path.exists(f):
        fm.fontManager.addfont(f)

# Brand Tokens (Institutional Data Intelligence)
COLOR_BG = "#202322"         # Raisin Black
COLOR_SURFACE = "#191C1B"    # Dark surface
COLOR_CHROME = "#233D4C"     # Charcoal Slate (lines & borders only)
COLOR_TEXT = "#E6EDF3"       # Off-White
COLOR_LIME = "#C3D809"       # Power Lime
COLOR_PUMPKIN = "#FD802E"    # Pumpkin
COLOR_MUTED = "#8B9A98"      # Mid-tone gray for secondary axes

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60

def CleanText(text, font="Nohemi", font_size=24, **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    return Text(text, font=font, font_size=ref_size, **kwargs).scale(scale_factor)

class WallStreetAIEnginesShort(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Background grid (Charcoal Slate)
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": COLOR_CHROME, "stroke_width": 1, "stroke_opacity": 0.4}
        )
        self.add(grid)

        # =========================================================================
        # BEAT 1: HOOK (0.0s - 6.5s, 6.5s)
        # "Wall Street spends billions on AI. But zero dollars trying to predict stock prices."
        # =========================================================================
        top_badge = RoundedRectangle(
            corner_radius=0.15, width=7.8, height=1.1,
            fill_color=COLOR_SURFACE, fill_opacity=0.95,
            stroke_color=COLOR_LIME, stroke_width=2.5
        ).to_edge(UP, buff=1.0)
        top_title = CleanText("THE WALL STREET AI PARADOX", font_size=24, weight="BOLD", color=COLOR_LIME).move_to(top_badge)

        hook_box = RoundedRectangle(
            corner_radius=0.2, width=8.0, height=3.4,
            fill_color=COLOR_SURFACE, fill_opacity=0.9,
            stroke_color=COLOR_PUMPKIN, stroke_width=2.0
        ).shift(UP * 3.8)

        txt_billions = CleanText("BILLIONS SPENT ON AI", font_size=28, weight="BOLD", color=COLOR_TEXT).next_to(hook_box.get_top(), DOWN, buff=0.4)
        txt_zero = CleanText("$0 ON PREDICTING PRICES", font_size=32, weight="BOLD", color=COLOR_PUMPKIN).next_to(txt_billions, DOWN, buff=0.35)

        # Graph with erratic stock curve and crossed out crystal ball
        axes_hook = Axes(
            x_range=[0, 6, 1], y_range=[0, 10, 2],
            x_length=7.4, y_length=3.8,
            axis_config={"color": COLOR_CHROME, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 1.5)

        np.random.seed(42)
        x_pts = np.linspace(0, 6, 50)
        y_pts = 4.0 + np.sin(x_pts * 2.5) * 1.8 + np.cos(x_pts * 4.0) * 0.8
        price_curve = axes_hook.plot_line_graph(x_pts, y_pts, add_vertex_dots=False, line_color=COLOR_LIME, stroke_width=3.5)

        prediction_line = DashedLine(axes_hook.c2p(3.5, 4.0), axes_hook.c2p(5.8, 8.5), color=COLOR_PUMPKIN, stroke_width=3.0)
        cross_out = VGroup(
            Line(axes_hook.c2p(4.0, 5.0), axes_hook.c2p(5.2, 7.5), color=COLOR_PUMPKIN, stroke_width=4.5),
            Line(axes_hook.c2p(4.0, 7.5), axes_hook.c2p(5.2, 5.0), color=COLOR_PUMPKIN, stroke_width=4.5)
        )
        lbl_failed_pred = CleanText("PRICE PREDICTION: IMPOSSIBLE", font_size=18, weight="BOLD", color=COLOR_PUMPKIN).next_to(cross_out, UP, buff=0.2)

        self.play(FadeIn(top_badge), FadeIn(top_title), run_time=1.0)
        self.play(FadeIn(hook_box), Write(txt_billions), Write(txt_zero), run_time=1.8)
        self.play(Create(axes_hook), Create(price_curve), run_time=2.0)
        self.play(Create(prediction_line), Create(cross_out), FadeIn(lbl_failed_pred), run_time=1.7)

        # =========================================================================
        # BEAT 2: RETAIL MYTH VS REFLEXIVITY (6.5s - 14.0s, 7.5s)
        # "Retail traders think AI is a crystal ball... but markets are reflexive."
        # =========================================================================
        self.play(
            FadeOut(hook_box), FadeOut(txt_billions), FadeOut(txt_zero),
            FadeOut(axes_hook), FadeOut(price_curve), FadeOut(prediction_line),
            FadeOut(cross_out), FadeOut(lbl_failed_pred),
            run_time=1.0
        )

        # Split comparison cards
        card_retail = RoundedRectangle(
            corner_radius=0.18, width=7.8, height=3.2,
            fill_color=COLOR_SURFACE, fill_opacity=0.9,
            stroke_color=COLOR_CHROME, stroke_width=2.0
        ).shift(UP * 3.4)
        lbl_retail_title = CleanText("1. RETAIL TRADER ILLUSION", font_size=22, weight="BOLD", color=COLOR_PUMPKIN).next_to(card_retail.get_top(), DOWN, buff=0.35)
        lbl_retail_desc = CleanText("\"AI will predict if Tesla goes up tomorrow\"", font_size=18, color=COLOR_TEXT).next_to(lbl_retail_title, DOWN, buff=0.25)
        lbl_retail_sub = CleanText("Belief: Market is a passive puzzle (like chess)", font_size=16, color=COLOR_MUTED).next_to(lbl_retail_desc, DOWN, buff=0.25)

        card_reflex = RoundedRectangle(
            corner_radius=0.18, width=7.8, height=3.6,
            fill_color=COLOR_SURFACE, fill_opacity=0.9,
            stroke_color=COLOR_LIME, stroke_width=2.5
        ).shift(DOWN * 0.8)
        lbl_reflex_title = CleanText("2. THE REFLEXIVITY REALITY", font_size=22, weight="BOLD", color=COLOR_LIME).next_to(card_reflex.get_top(), DOWN, buff=0.35)
        lbl_reflex_desc = CleanText("The prediction itself destroys the pattern.", font_size=19, weight="BOLD", color=COLOR_TEXT).next_to(lbl_reflex_title, DOWN, buff=0.25)
        lbl_reflex_sub = CleanText("If AI discovers an edge, capital rushing in\nerases the profit spread instantly.", font_size=16, color=COLOR_MUTED).next_to(lbl_reflex_desc, DOWN, buff=0.2)

        self.play(FadeIn(card_retail), Write(lbl_retail_title), FadeIn(lbl_retail_desc), FadeIn(lbl_retail_sub), run_time=2.2)
        self.play(FadeIn(card_reflex), Write(lbl_reflex_title), FadeIn(lbl_reflex_desc), FadeIn(lbl_reflex_sub), run_time=2.5)
        self.wait(1.8)

        # =========================================================================
        # BEAT 3: THE 4 INVISIBLE ENGINES (14.0s - 40.0s, 26.0s)
        # "So where do institutional quants actually use machine learning? Across four invisible engines..."
        # =========================================================================
        self.play(
            FadeOut(card_retail), FadeOut(lbl_retail_title), FadeOut(lbl_retail_desc), FadeOut(lbl_retail_sub),
            FadeOut(card_reflex), FadeOut(lbl_reflex_title), FadeOut(lbl_reflex_desc), FadeOut(lbl_reflex_sub),
            run_time=1.0
        )

        top_title_new = CleanText("WHERE WALL STREET ACTUALLY USES AI", font_size=21, weight="BOLD", color=COLOR_LIME).move_to(top_badge)
        self.play(Transform(top_title, top_title_new), run_time=0.8)

        # 4 Vertical Engine Cards
        engine_cards = []
        engine_y = [4.2, 1.8, -0.6, -3.0]
        engine_data = [
            ("1. EXTREME RISK MODELING", "Simulating 100,000 catastrophic crash scenarios", COLOR_LIME),
            ("2. ORDER MICRO-SLICING", "Hiding $5B trades across thousands of micro-slices", COLOR_LIME),
            ("3. ANOMALY & FRAUD RADAR", "Detecting spoofing & wash trades in microseconds", COLOR_LIME),
            ("4. PORTFOLIO COVARIANCE", "Calculating optimal 500-asset risk weighting", COLOR_LIME)
        ]

        card_groups = []
        for i, (title, sub, col) in enumerate(engine_data):
            c_box = RoundedRectangle(
                corner_radius=0.16, width=8.0, height=2.0,
                fill_color=COLOR_SURFACE, fill_opacity=0.9,
                stroke_color=COLOR_CHROME, stroke_width=2.0
            ).shift(UP * engine_y[i])
            c_title = CleanText(title, font_size=20, weight="BOLD", color=COLOR_TEXT).next_to(c_box.get_top(), DOWN, buff=0.3)
            c_sub = CleanText(sub, font_size=15, color=COLOR_MUTED).next_to(c_title, DOWN, buff=0.2)
            c_grp = VGroup(c_box, c_title, c_sub)
            card_groups.append(c_grp)

        # Introduce all 4 cards dimmed (2.0s)
        self.play(*[FadeIn(cg) for cg in card_groups], run_time=2.0)

        # Engine 1 activates (23s - 27.5s, 4.5s)
        highlight_1 = card_groups[0][0].animate.set_stroke(COLOR_LIME, width=3.5)
        title_1 = card_groups[0][1].animate.set_color(COLOR_LIME)
        desc_1 = card_groups[0][2].animate.set_color(COLOR_TEXT)
        self.play(highlight_1, title_1, desc_1, run_time=1.2)
        # Small pulsing metric inside Card 1
        metric_1 = CleanText("MONTE CARLO: 100,000 LIQUIDITY PATHS", font_size=13, weight="BOLD", color=COLOR_LIME).next_to(card_groups[0][2], DOWN, buff=0.12)
        self.play(FadeIn(metric_1), run_time=1.0)
        self.wait(2.3)

        # Engine 2 activates (27.5s - 32.0s, 4.5s)
        highlight_2 = card_groups[1][0].animate.set_stroke(COLOR_LIME, width=3.5)
        title_2 = card_groups[1][1].animate.set_color(COLOR_LIME)
        desc_2 = card_groups[1][2].animate.set_color(COLOR_TEXT)
        metric_2 = CleanText("SLIPPAGE SAVED: $14.2M PER BLOCK", font_size=13, weight="BOLD", color=COLOR_LIME).next_to(card_groups[1][2], DOWN, buff=0.12)
        self.play(highlight_2, title_2, desc_2, FadeIn(metric_2), run_time=1.5)
        self.wait(3.0)

        # Engine 3 activates (32.0s - 36.0s, 4.0s)
        highlight_3 = card_groups[2][0].animate.set_stroke(COLOR_LIME, width=3.5)
        title_3 = card_groups[2][1].animate.set_color(COLOR_LIME)
        desc_3 = card_groups[2][2].animate.set_color(COLOR_TEXT)
        metric_3 = CleanText("LATENCY: < 42 MICROSECONDS", font_size=13, weight="BOLD", color=COLOR_LIME).next_to(card_groups[2][2], DOWN, buff=0.12)
        self.play(highlight_3, title_3, desc_3, FadeIn(metric_3), run_time=1.5)
        self.wait(2.5)

        # Engine 4 activates (36.0s - 40.0s, 4.0s)
        highlight_4 = card_groups[3][0].animate.set_stroke(COLOR_LIME, width=3.5)
        title_4 = card_groups[3][1].animate.set_color(COLOR_LIME)
        desc_4 = card_groups[3][2].animate.set_color(COLOR_TEXT)
        metric_4 = CleanText("OPTIMIZED: MAX SHARPE RATIO", font_size=13, weight="BOLD", color=COLOR_LIME).next_to(card_groups[3][2], DOWN, buff=0.12)
        self.play(highlight_4, title_4, desc_4, FadeIn(metric_4), run_time=1.5)
        self.wait(2.5)

        # =========================================================================
        # BEAT 4: THE VERDICT (40.0s - 48.05s, 8.05s)
        # "Notice what none of them do: they never predict the future. Real AI in finance is an optimization engine, not a fortune teller."
        # =========================================================================
        self.play(
            *[FadeOut(cg) for cg in card_groups],
            FadeOut(metric_1), FadeOut(metric_2), FadeOut(metric_3), FadeOut(metric_4),
            FadeOut(top_badge), FadeOut(top_title),
            run_time=1.2
        )

        verdict_card = RoundedRectangle(
            corner_radius=0.25, width=8.2, height=6.5,
            fill_color=COLOR_SURFACE, fill_opacity=0.95,
            stroke_color=COLOR_LIME, stroke_width=3.0
        ).shift(UP * 0.5)

        v_head = CleanText("THE QUANTITATIVE TRUTH", font_size=24, weight="BOLD", color=COLOR_LIME).next_to(verdict_card.get_top(), DOWN, buff=0.6)
        v_sub = CleanText("None of these engines predict price.", font_size=20, weight="BOLD", color=COLOR_TEXT).next_to(v_head, DOWN, buff=0.45)

        box_opt = RoundedRectangle(corner_radius=0.15, width=7.2, height=1.4, fill_color=COLOR_BG, fill_opacity=0.9, stroke_color=COLOR_LIME, stroke_width=2).next_to(v_sub, DOWN, buff=0.5)
        txt_opt = CleanText("AI = OPTIMIZATION ENGINE", font_size=22, weight="BOLD", color=COLOR_LIME).move_to(box_opt)

        box_pred = RoundedRectangle(corner_radius=0.15, width=7.2, height=1.4, fill_color=COLOR_BG, fill_opacity=0.9, stroke_color=COLOR_PUMPKIN, stroke_width=2).next_to(box_opt, DOWN, buff=0.35)
        txt_pred = CleanText("NOT A FORTUNE TELLER", font_size=22, weight="BOLD", color=COLOR_PUMPKIN).move_to(box_pred)

        logo_sub = CleanText("QUANTROVE", font_size=18, weight="BOLD", color=COLOR_TEXT).to_edge(DOWN, buff=1.2)

        self.play(FadeIn(verdict_card), Write(v_head), FadeIn(v_sub), run_time=1.8)
        self.play(FadeIn(box_opt), Write(txt_opt), run_time=1.5)
        self.play(FadeIn(box_pred), Write(txt_pred), FadeIn(logo_sub), run_time=1.5)
        self.wait(3.25)
