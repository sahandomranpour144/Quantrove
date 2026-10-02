"""
EP05 Scene 05: The Bid-Ask Spread Mechanism (01:36.84 - 02:11.80, TARGET: EXACTLY 34.96s)
Airport currency exchange booth analogy seamlessly morphs into
institutional Level 2 order book, ending with rapid microsecond profit accumulation ramp.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene05BidAskMechanism(Scene):
    def construct(self):
        TARGET_DURATION = 34.96

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Part 1: Airport Currency Booth Analogy
        booth_card = RoundedRectangle(
            corner_radius=0.25, width=8.5, height=3.8,
            stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#161B22", fill_opacity=0.95
        ).shift(UP * 0.5)

        b_title = CleanText("THE CURRENCY BOOTH ANALOGY", font_size=20, color=SUCCESS, weight="BOLD")
        b_title.move_to(booth_card.get_top() + DOWN * 0.45)

        buy_panel = RoundedRectangle(corner_radius=0.15, width=3.4, height=1.6, stroke_color=SUCCESS, stroke_width=2, fill_color="#18241D", fill_opacity=0.9).move_to(booth_card.get_center() + LEFT * 2.0 + DOWN * 0.2)
        b_lbl = CleanText("THEY SELL EUROS TO YOU:", font_size=12, color=TEXT, fill_opacity=0.60).move_to(buy_panel.get_top() + DOWN * 0.3)
        b_val = CleanText("$1.10 / €", font_size=28, color=SUCCESS, weight="BOLD").next_to(b_lbl, DOWN, buff=0.12)
        b_group = VGroup(buy_panel, b_lbl, b_val)

        sell_panel = RoundedRectangle(corner_radius=0.15, width=3.4, height=1.6, stroke_color=TEXT, stroke_width=2, fill_color="#1E232B", fill_opacity=0.9).move_to(booth_card.get_center() + RIGHT * 2.0 + DOWN * 0.2)
        s_lbl = CleanText("THEY BUY EUROS FROM YOU:", font_size=12, color=TEXT, fill_opacity=0.60).move_to(sell_panel.get_top() + DOWN * 0.3)
        s_val = CleanText("$1.06 / €", font_size=28, color=TEXT, weight="BOLD").next_to(s_lbl, DOWN, buff=0.12)
        s_group = VGroup(sell_panel, s_lbl, s_val)

        spread_arrow = DoubleArrow(start=buy_panel.get_right() + RIGHT * 0.1, end=sell_panel.get_left() + LEFT * 0.1, stroke_color=RISK, stroke_width=3, buff=0)
        spread_lbl = CleanText("SPREAD: $0.04", font_size=14, color=RISK, weight="BOLD").next_to(spread_arrow, UP, buff=0.1)

        # 3. Transition into Level 2 Stock Order Book Ladder
        ladder_title = CleanText("STOCK MARKET LEVEL 2 ORDER BOOK", font_size=20, color=SUCCESS, weight="BOLD").move_to(booth_card.get_top() + DOWN * 0.45)

        ask_bar = RoundedRectangle(corner_radius=0.15, width=7.0, height=0.9, stroke_color=SUCCESS, stroke_width=2, fill_color="#19281E", fill_opacity=0.95).move_to(booth_card.get_center() + UP * 0.5)
        ask_l = CleanText("MARKET MAKER SELLS (ASK):", font_size=14, color=SUCCESS).move_to(ask_bar.get_left() + RIGHT * 1.8)
        ask_v = CleanText("$100.01", font_size=26, color=TEXT, weight="BOLD").move_to(ask_bar.get_right() + LEFT * 1.0)
        ask_grp = VGroup(ask_bar, ask_l, ask_v)

        bid_bar = RoundedRectangle(corner_radius=0.15, width=7.0, height=0.9, stroke_color=TEXT, stroke_width=2, fill_color="#1E232B", fill_opacity=0.95).move_to(booth_card.get_center() + DOWN * 0.5)
        bid_l = CleanText("MARKET MAKER BUYS (BID):", font_size=14, color=TEXT).move_to(bid_bar.get_left() + RIGHT * 1.8)
        bid_v = CleanText("$99.99", font_size=26, color=TEXT, weight="BOLD").move_to(bid_bar.get_right() + LEFT * 1.0)
        bid_grp = VGroup(bid_bar, bid_l, bid_v)

        stock_spread_bracket = Brace(VGroup(ask_bar, bid_bar), direction=RIGHT, color=RISK)
        stock_spread_txt = CleanText("THE SPREAD: $0.02", font_size=15, color=RISK, weight="BOLD").next_to(stock_spread_bracket, RIGHT, buff=0.2)

        # 4. Volume Ramp & Cumulative Profit Acceleration
        vol_box = RoundedRectangle(
            corner_radius=0.2, width=8.5, height=1.2,
            stroke_color=SUCCESS, stroke_width=2.5, fill_color="#161B22", fill_opacity=0.95
        ).shift(DOWN * 2.6)

        vol_lbl = CleanText("MICROSECOND VOLUME // RISK-FREE SPREAD CAPTURE:", font_size=13, color=TEXT, fill_opacity=0.60).move_to(vol_box.get_top() + DOWN * 0.3)
        vol_txt = CleanText("$200 / SEC PROFIT ACCUMULATION", font_size=24, color=SUCCESS, weight="BOLD").next_to(vol_lbl, DOWN, buff=0.12)

        all_content = VGroup(
            booth_card, b_title, b_group, s_group, spread_arrow, spread_lbl,
            ladder_title, ask_grp, bid_grp, stock_spread_bracket, stock_spread_txt,
            vol_box, vol_lbl, vol_txt
        )
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 34.96s) -----------------
        # Beat 1: Booth card enters (1.5s) + buy/sell panels enter (1.5s) = 3.0s
        self.play(FadeIn(booth_card, shift=DOWN * 0.3 * s_factor), FadeIn(b_title), run_time=1.5)
        self.play(FadeIn(b_group, shift=RIGHT * 0.3 * s_factor), FadeIn(s_group, shift=LEFT * 0.3 * s_factor), run_time=1.5)

        # Beat 2: Spread arrow & gap callout (1.5s + 2.0s hold) = 3.5s -> cumulative 6.5s
        self.play(Create(spread_arrow), FadeIn(spread_lbl), run_time=1.5)
        self.wait(2.0)

        # Beat 3: Morph transition from Currency Booth to Level 2 Order Book (2.0s) -> cumulative 8.5s
        self.play(FadeOut(b_group, s_group, spread_arrow, spread_lbl, b_title), run_time=2.0)

        # Beat 4: Level 2 Order Book draws with Ask and Bid bars (2.0s + 1.5s bracket = 3.5s) -> cumulative 12.0s
        self.play(FadeIn(ladder_title), FadeIn(ask_grp, shift=DOWN * 0.2 * s_factor), FadeIn(bid_grp, shift=UP * 0.2 * s_factor), run_time=2.0)
        self.play(Create(stock_spread_bracket), FadeIn(stock_spread_txt), run_time=1.5)

        # Beat 5: Simulated retail orders arriving at the book (4.0s) -> cumulative 16.0s
        buy_order_dot = Dot(color=SUCCESS, radius=0.12 * s_factor).move_to(ask_bar.get_left() + LEFT * 2.0)
        sell_order_dot = Dot(color=TEXT, radius=0.12 * s_factor).move_to(bid_bar.get_left() + LEFT * 2.0)
        self.play(
            FadeIn(buy_order_dot), FadeIn(sell_order_dot),
            buy_order_dot.animate.move_to(ask_bar.get_center()),
            sell_order_dot.animate.move_to(bid_bar.get_center()),
            run_time=2.0
        )
        self.play(
            ask_bar.animate.set_stroke(color=SUCCESS, width=4.0),
            bid_bar.animate.set_stroke(color=TEXT, width=4.0),
            FadeOut(buy_order_dot), FadeOut(sell_order_dot),
            run_time=2.0
        )

        # Beat 6: Net inventory risk = $0 tag appears (3.5s) -> cumulative 19.5s
        risk_tag = CleanText("INVENTORY MATCHED // ZERO NET POSITION RISK", font_size=int(14 * s_factor), color=SUCCESS, weight="BOLD")
        risk_tag.move_to(booth_card.get_bottom() + UP * 0.4 * s_factor)
        self.play(FadeIn(risk_tag, scale=1.1), run_time=1.5)
        self.wait(2.0)

        # Beat 7: Volume Multiplier Box appears (1.5s) -> cumulative 21.0s
        self.play(FadeIn(vol_box), FadeIn(vol_lbl), FadeIn(vol_txt), run_time=1.5)

        # Beat 8: Rapid Profit Multiplier Acceleration across 4 steps (8.0s) -> cumulative 29.0s
        step1 = CleanText("$5,400 / SEC PROFIT ACCUMULATION", font_size=int(24 * s_factor), color=SUCCESS, weight="BOLD").next_to(vol_lbl, DOWN, buff=0.12 * s_factor)
        step2 = CleanText("$32,000 / SEC PROFIT ACCUMULATION", font_size=int(24 * s_factor), color=SUCCESS, weight="BOLD").next_to(vol_lbl, DOWN, buff=0.12 * s_factor)
        step3 = CleanText("$145,000 / SEC PROFIT ACCUMULATION", font_size=int(24 * s_factor), color=SUCCESS, weight="BOLD").next_to(vol_lbl, DOWN, buff=0.12 * s_factor)
        step4 = CleanText("$1,200,000,000+ ANNUAL SPREAD HARVEST", font_size=int(24 * s_factor), color=SUCCESS, weight="BOLD").next_to(vol_lbl, DOWN, buff=0.12 * s_factor)

        self.play(Transform(vol_txt, step1), run_time=2.0)
        self.play(Transform(vol_txt, step2), run_time=2.0)
        self.play(Transform(vol_txt, step3), run_time=2.0)
        self.play(Transform(vol_txt, step4), run_time=2.0)

        # Beat 9: Final highlight pulse on high-frequency spread harvest to exact duration (5.96s) -> cumulative 34.96s
        self.play(
            vol_box.animate.set_stroke(color=SUCCESS, width=4.5),
            stock_spread_bracket.animate.set_color(RISK),
            run_time=2.98
        )
        self.play(
            vol_box.animate.set_stroke(color=SUCCESS, width=2.5),
            run_time=2.98
        )
