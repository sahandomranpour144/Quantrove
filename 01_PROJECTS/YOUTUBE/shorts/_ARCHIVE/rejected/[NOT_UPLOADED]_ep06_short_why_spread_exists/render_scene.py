"""
Quantrove EP06 Short S06-03: Why Does a Spread Exist?
Format: 9:16 Vertical (1080x1920 @ 60fps)
Duration: Exactly 36.8s
Visual Language: Institutional Data Intelligence
"""
from manim import *
import os, sys

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60
config.background_color = "#202322"

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT

class WhySpreadExists(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # BEAT 1: [0.0s - 4.8s] IDEA
        top_header = CleanText("THE SPREAD PARADOX", font_size=18, color=TEXT, weight="BOLD").move_to(UP * 6.5)
        sub_header = CleanText("ZERO-PROFIT MARKET MAKING", font_size=12, color=SUCCESS).next_to(top_header, DOWN, buff=0.15)
        header_group = VGroup(top_header, sub_header)

        quote_card = RoundedRectangle(corner_radius=0.2, width=6.8, height=2.4, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 3.8)
        ask_lbl = CleanText("ASK: $100.02", font_size=18, color=SUCCESS, weight="BOLD").move_to(quote_card.get_left() + RIGHT * 1.8)
        bid_lbl = CleanText("BID: $100.00", font_size=18, color=RISK, weight="BOLD").move_to(quote_card.get_right() + LEFT * 1.8)
        spread_tag = CleanText("SPREAD = $0.02", font_size=14, color=TEXT, weight="BOLD").next_to(quote_card, DOWN, buff=0.2)

        self.play(FadeIn(header_group, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(quote_card), run_time=0.8)
        self.play(FadeIn(ask_lbl, shift=LEFT * 0.2), FadeIn(bid_lbl, shift=RIGHT * 0.2), run_time=1.0)
        self.play(FadeIn(spread_tag, scale=1.1), run_time=1.0)
        self.wait(1.2)

        # BEAT 2: [4.8s - 12.8s] SIMPLE_WRONG
        deduct_box = RoundedRectangle(corner_radius=0.2, width=6.8, height=3.0, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 0.2)
        d_title = CleanText("HYPOTHETICAL DEDUCTIONS", font_size=14, color=TEXT, weight="BOLD").move_to(deduct_box.get_top() + DOWN * 0.4)
        d1 = CleanText("- Exchange Fees: $0.00", font_size=13, color=TEXT).next_to(d_title, DOWN, buff=0.25)
        d2 = CleanText("- Overhead Costs: $0.00", font_size=13, color=TEXT).next_to(d1, DOWN, buff=0.2)
        d3 = CleanText("- Expected Profit: $0.00", font_size=13, color=TEXT).next_to(d2, DOWN, buff=0.2)

        collapse_arrow = Arrow(start=UP * -1.5, end=UP * -2.4, stroke_color=RISK, stroke_width=3)
        fail_tag = CleanText("THE SPREAD REFUSES TO COLLAPSE", font_size=15, color=RISK, weight="BOLD").next_to(collapse_arrow, DOWN, buff=0.2)

        self.play(FadeIn(deduct_box), FadeIn(d_title), run_time=0.8)
        self.play(FadeIn(d1, shift=RIGHT * 0.2), run_time=1.0)
        self.play(FadeIn(d2, shift=RIGHT * 0.2), run_time=1.0)
        self.play(FadeIn(d3, shift=RIGHT * 0.2), run_time=1.0)
        self.play(Create(collapse_arrow), FadeIn(fail_tag, scale=1.08), run_time=1.4)
        self.wait(1.8)

        # BEAT 3: [12.8s - 25.3s] COMPLEX_WRONG
        deduct_group = VGroup(deduct_box, d_title, d1, d2, d3, collapse_arrow, fail_tag)
        quote_group = VGroup(quote_card, ask_lbl, bid_lbl, spread_tag)
        self.play(FadeOut(deduct_group), FadeOut(quote_group), run_time=0.8)

        gm_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=1.6, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 4.2)
        gm_title = CleanText("GLOSTEN & MILGROM (1985)", font_size=16, color=SUCCESS, weight="BOLD").move_to(gm_card.get_top() + DOWN * 0.45)
        gm_sub = CleanText("ASYMMETRIC INFORMATION MODEL", font_size=12, color=TEXT).next_to(gm_title, DOWN, buff=0.15)
        gm_group = VGroup(gm_card, gm_title, gm_sub)

        flow_box1 = RoundedRectangle(corner_radius=0.2, width=3.3, height=2.2, stroke_color=SUCCESS, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(LEFT * 1.9 + UP * 1.5)
        f1_t = CleanText("UNINFORMED", font_size=14, color=SUCCESS, weight="BOLD").move_to(flow_box1.get_top() + DOWN * 0.4)
        f1_sub = CleanText("Random liquidity\nNo private signal", font_size=11, color=TEXT).next_to(f1_t, DOWN, buff=0.15)
        f1_group = VGroup(flow_box1, f1_t, f1_sub)

        flow_box2 = RoundedRectangle(corner_radius=0.2, width=3.3, height=2.2, stroke_color=RISK, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(RIGHT * 1.9 + UP * 1.5)
        f2_t = CleanText("INFORMED", font_size=14, color=RISK, weight="BOLD").move_to(flow_box2.get_top() + DOWN * 0.4)
        f2_sub = CleanText("Superior signal\nBuys before jump", font_size=11, color=TEXT).next_to(f2_t, DOWN, buff=0.15)
        f2_group = VGroup(flow_box2, f2_t, f2_sub)

        mm_central = RoundedRectangle(corner_radius=0.2, width=7.2, height=1.8, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(DOWN * 1.2)
        mm_t = CleanText("THE MARKET MAKER IS BLIND", font_size=15, color=TEXT, weight="BOLD").move_to(mm_central.get_top() + DOWN * 0.45)
        mm_desc = CleanText("Cannot distinguish incoming order types", font_size=12, color=RISK).next_to(mm_t, DOWN, buff=0.15)
        mm_group = VGroup(mm_central, mm_t, mm_desc)

        arrow_inf = Arrow(start=flow_box2.get_bottom(), end=mm_central.get_top() + RIGHT * 1.5, stroke_color=RISK, stroke_width=3)

        self.play(FadeIn(gm_group, shift=DOWN * 0.2), run_time=1.0)
        self.play(FadeIn(f1_group, shift=RIGHT * 0.2), FadeIn(f2_group, shift=LEFT * 0.2), run_time=1.2)
        self.play(FadeIn(mm_group, shift=UP * 0.2), run_time=1.2)
        self.play(Create(arrow_inf), mm_central.animate.set_stroke(RISK, width=3.5), run_time=1.5)
        self.play(f2_group.animate.scale(1.05), run_time=1.0)
        self.wait(2.8)

        # BEAT 4: [25.3s - 36.8s] INSIGHT
        self.play(FadeOut(gm_group), FadeOut(f1_group), FadeOut(f2_group), FadeOut(mm_group), FadeOut(arrow_inf), run_time=0.8)

        cq_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=3.6, stroke_color=RISK, stroke_width=3, fill_color="#181C24", fill_opacity=0.96).move_to(UP * 2.2)
        cq_title = CleanText("THE INFORMED ORDER ARRIVES", font_size=16, color=RISK, weight="BOLD").move_to(cq_card.get_top() + DOWN * 0.5)
        cq1 = CleanText("1. Machine sells ask @ $100.01", font_size=13, color=TEXT).next_to(cq_title, DOWN, buff=0.25)
        cq2 = CleanText("2. Fair price jumps immediately to $100.11", font_size=13, color=RISK, weight="BOLD").next_to(cq1, DOWN, buff=0.2)
        cq3 = CleanText("3. Machine absorbs -$0.10 adverse selection loss", font_size=12, color=TEXT).next_to(cq2, DOWN, buff=0.2)

        badge_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.2, stroke_color=SUCCESS, stroke_width=3, fill_color="#181C24", fill_opacity=0.98).move_to(DOWN * 1.5)
        badge_txt = CleanText("ADVERSE SELECTION", font_size=17, color=SUCCESS, weight="BOLD").move_to(badge_box)
        badge_group = VGroup(badge_box, badge_txt)

        self.play(FadeIn(cq_card), FadeIn(cq_title), run_time=0.9)
        self.play(FadeIn(cq1, shift=RIGHT * 0.2), run_time=1.0)
        self.play(FadeIn(cq2, shift=RIGHT * 0.2), run_time=1.1)
        self.play(FadeIn(cq3, shift=RIGHT * 0.2), run_time=1.1)
        self.play(FadeIn(badge_group, scale=1.1), run_time=1.2)
        self.play(badge_box.animate.set_stroke(SUCCESS, width=4.5), run_time=1.0)
        self.wait(2.4)
