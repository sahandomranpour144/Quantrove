"""
EP05 Scene 06: Payment for Order Flow Kickback (02:11.80 - 02:47.04, TARGET: EXACTLY 35.24s)
Dual pipeline routing retail order right and PFOF kickback cash left,
dissolving into Robinhood's quarterly revenue bar chart where PFOF towers over other streams.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene06PfofKickback(Scene):
    def construct(self):
        TARGET_DURATION = 35.24

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Left: Retail Flow Box vs Institutional Flow Box
        retail_box = RoundedRectangle(corner_radius=0.2, width=4.2, height=2.6, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.95).shift(LEFT * 4.0 + UP * 0.2)
        ret_title = CleanText("RETAIL INVESTOR FLOW", font_size=16, color=SUCCESS, weight="BOLD").move_to(retail_box.get_top() + DOWN * 0.35)
        ret_ex = CleanText("50 SHARES OF APPLE", font_size=15, color=TEXT).next_to(ret_title, DOWN, buff=0.18)
        ret_tag = CleanText("Uninformed // Non-Toxic Flow", font_size=13, color=SUCCESS).next_to(ret_ex, DOWN, buff=0.12)
        ret_eval = CleanText("SAFE SPREAD HARVESTING", font_size=13, color=TEXT, fill_opacity=0.60).next_to(ret_tag, DOWN, buff=0.12)
        ret_grp = VGroup(retail_box, ret_title, ret_ex, ret_tag, ret_eval)

        mm_box = RoundedRectangle(corner_radius=0.2, width=4.2, height=2.6, stroke_color=RISK, stroke_width=2.5, fill_color="#201510", fill_opacity=0.95).shift(RIGHT * 4.0 + UP * 0.2)
        mm_title = CleanText("WHOLESALE MARKET MAKER", font_size=16, color=RISK, weight="BOLD").move_to(mm_box.get_top() + DOWN * 0.35)
        mm_firm = CleanText("CITADEL / VIRTU / SIG", font_size=15, color=TEXT).next_to(mm_title, DOWN, buff=0.18)
        mm_stat = CleanText("Eager to Buy Your Trades", font_size=13, color=RISK).next_to(mm_firm, DOWN, buff=0.12)
        mm_vol = CleanText("Zero Toxic Information Risk", font_size=13, color=TEXT, fill_opacity=0.60).next_to(mm_stat, DOWN, buff=0.12)
        mm_grp = VGroup(mm_box, mm_title, mm_firm, mm_stat, mm_vol)

        part1_group = VGroup(ret_grp, mm_grp)
        part1_group, s1 = stage_fit(part1_group, max_w=12.2, max_h=4.5)

        # 3. Dual Pipeline
        order_pipe = Arrow(start=retail_box.get_right() + UP * 0.35 * s1, end=mm_box.get_left() + UP * 0.35 * s1, stroke_color=TEXT, stroke_width=4, buff=0.1)
        order_lbl = CleanText("ORDERS: 50 SHARES AAPL", font_size=12, color=TEXT).next_to(order_pipe, UP, buff=0.1)

        pfof_pipe = Arrow(start=mm_box.get_left() + DOWN * 0.35 * s1, end=retail_box.get_right() + DOWN * 0.35 * s1, stroke_color=RISK, stroke_width=4, buff=0.1)
        pfof_lbl = CleanText("PFOF CASH KICKBACK TO BROKER", font_size=12, color=RISK, weight="BOLD").next_to(pfof_pipe, DOWN, buff=0.1)

        # 4. Robinhood Quarterly Revenue Surge
        chart_card = RoundedRectangle(corner_radius=0.25, width=8.5, height=4.2, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#161B22", fill_opacity=0.95).move_to(ORIGIN)
        ch_title = CleanText("ROBINHOOD REVENUE BY SOURCE // PEAK PFOF ERA", font_size=18, color=SUCCESS, weight="BOLD").move_to(chart_card.get_top() + DOWN * 0.45)

        b1_bg = Rectangle(width=1.5, height=1.0, fill_color=UI_STRUCTURE, fill_opacity=0.8, stroke_color=UI_STRUCTURE).move_to(LEFT * 2.6 + DOWN * 0.7)
        b1_lbl = CleanText("INTEREST\n$40M", font_size=12, color=TEXT, fill_opacity=0.60).next_to(b1_bg, DOWN, buff=0.12)

        b2_bg = Rectangle(width=1.5, height=1.4, fill_color=UI_STRUCTURE, fill_opacity=0.8, stroke_color=UI_STRUCTURE).move_to(LEFT * 0.0 + DOWN * 0.5)
        b2_lbl = CleanText("CRYPTO\n$60M", font_size=12, color=TEXT, fill_opacity=0.60).next_to(b2_bg, DOWN, buff=0.12)

        b3_bg = Rectangle(width=1.8, height=3.0, fill_color=RISK, fill_opacity=0.95, stroke_color=TEXT, stroke_width=2).move_to(RIGHT * 2.6 + UP * 0.3)
        b3_val = CleanText("$200M+", font_size=24, color=TEXT, weight="BOLD").move_to(b3_bg.get_top() + DOWN * 0.35)
        b3_lbl = CleanText("PFOF REVENUE\nPER QUARTER", font_size=13, color=RISK, weight="BOLD").next_to(b3_bg, DOWN, buff=0.12)

        pct_tag = CleanText("75%+ OF TOTAL REVENUE", font_size=14, color=RISK, weight="BOLD").next_to(b3_val, UP, buff=0.15)

        chart_grp = VGroup(chart_card, ch_title, b1_bg, b1_lbl, b2_bg, b2_lbl, b3_bg, b3_val, b3_lbl, pct_tag)
        chart_grp, s2 = stage_fit(chart_grp, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 35.24s) -----------------
        # Beat 1: Retail & MM profiles enter (2.0s) + inspection (3.0s) = 5.0s
        self.play(FadeIn(ret_grp, shift=RIGHT * 0.3 * s1), FadeIn(mm_grp, shift=LEFT * 0.3 * s1), run_time=2.0)
        self.wait(3.0)

        # Beat 2: Dual Pipeline draws (order forward, kickback reverse) (2.0s + 2.5s) = 4.5s -> cumulative 9.5s
        self.play(Create(order_pipe), FadeIn(order_lbl), run_time=1.2)
        self.play(Create(pfof_pipe), FadeIn(pfof_lbl), run_time=1.3)
        self.wait(2.0)

        # Beat 3: Packets cycling through dual pipe (order right, cash left) (4.5s) -> cumulative 14.0s
        order_dot = Dot(color=SUCCESS, radius=0.10 * s1).move_to(retail_box.get_right() + UP * 0.35 * s1)
        cash_dot = Dot(color=RISK, radius=0.10 * s1).move_to(mm_box.get_left() + DOWN * 0.35 * s1)
        self.play(
            FadeIn(order_dot), FadeIn(cash_dot),
            order_dot.animate.move_to(mm_box.get_left() + UP * 0.35 * s1),
            cash_dot.animate.move_to(retail_box.get_right() + DOWN * 0.35 * s1),
            run_time=2.25, rate_func=linear
        )
        self.play(
            FadeOut(order_dot), FadeOut(cash_dot),
            retail_box.animate.set_stroke(color=SUCCESS, width=4.0),
            mm_box.animate.set_stroke(color=RISK, width=4.0),
            run_time=2.25
        )

        # Beat 4: Transition to Robinhood revenue chart card (2.5s) -> cumulative 16.5s
        self.play(FadeOut(ret_grp, mm_grp, order_pipe, order_lbl, pfof_pipe, pfof_lbl), run_time=1.2)
        self.play(FadeIn(chart_card), FadeIn(ch_title), run_time=1.3)

        # Beat 5: Secondary revenue bars grow (Interest $40M, Crypto $60M) (2.5s) -> cumulative 19.0s
        self.play(
            GrowFromEdge(b1_bg, DOWN), FadeIn(b1_lbl),
            GrowFromEdge(b2_bg, DOWN), FadeIn(b2_lbl),
            run_time=2.5
        )

        # Beat 6: PFOF Tower Bar erupts upwards crossing $200M+ (3.5s + 3.0s count) = 6.5s -> cumulative 25.5s
        self.play(
            GrowFromEdge(b3_bg, DOWN), FadeIn(b3_lbl),
            run_time=3.5
        )
        self.play(FadeIn(b3_val, scale=1.3), run_time=3.0)

        # Beat 7: Milestone line and 75%+ dominance tag illuminate (5.0s) -> cumulative 30.5s
        milestone_line = DashedLine(
            start=chart_card.get_left() + RIGHT * 0.5 + UP * 0.8 * s2,
            end=chart_card.get_right() + LEFT * 0.5 + UP * 0.8 * s2,
            stroke_color=RISK, stroke_width=2
        )
        self.play(Create(milestone_line), FadeIn(pct_tag), run_time=2.5)
        self.wait(2.5)

        # Beat 8: Final pulse on PFOF tower bar to exact duration (4.74s) -> cumulative 35.24s
        self.play(
            b3_bg.animate.set_stroke(color=RISK, width=5.0),
            pct_tag.animate.scale(1.10),
            run_time=2.37
        )
        self.play(
            b3_bg.animate.set_stroke(color=TEXT, width=2.0),
            pct_tag.animate.scale(1.0 / 1.10),
            run_time=2.37
        )
