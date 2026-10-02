"""
Quantrove EP05 Short: PFOF Kickback (Revised Visual Architecture)
Format: 9:16 Vertical (1080x1920 @ 60fps)
Target Duration: Exactly 35.25s
Narration: Approved EP05 Master Stem (131.80s - 167.04s)
Visual Logic: Market Maker Desire -> 50 Shares Apple Order -> Broker Node -> PFOF Reverse Money Flow -> $200M Revenue Bar
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

class PfofKickbackVertical(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # ----------------------------------------------------
        # BEAT 1: [0.0s - 7.0s] "Why do market makers want your retail trades so badly? Because retail trades are safe."
        # ----------------------------------------------------
        mm_box = RoundedRectangle(corner_radius=0.25, width=7.2, height=2.4, stroke_color=SUCCESS, stroke_width=3, fill_color="#182319", fill_opacity=0.96).move_to(UP * 4.6)
        mm_title = CleanText("WHOLESALE MARKET MAKERS", font_size=16, color=SUCCESS, weight="BOLD").move_to(mm_box.get_top() + DOWN * 0.45)
        mm_names = CleanText("CITADEL SECURITIES // VIRTU FINANCIAL", font_size=13, color=TEXT, weight="BOLD").next_to(mm_title, DOWN, buff=0.18)
        mm_target = CleanText("TARGET: RETAIL ORDER FLOW", font_size=13, color=SUCCESS).next_to(mm_names, DOWN, buff=0.15)
        mm_group = VGroup(mm_box, mm_title, mm_names, mm_target)

        safe_box = RoundedRectangle(corner_radius=0.2, width=6.2, height=1.6, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#1F2E14", fill_opacity=0.95).move_to(UP * 1.5)
        safe_txt = CleanText("RETAIL ORDERS = SAFE PROFIT", font_size=17, color=SUCCESS, weight="BOLD").move_to(safe_box.get_top() + DOWN * 0.45)
        safe_sub = CleanText("Zero Market Prediction Edge", font_size=13, color=TEXT).next_to(safe_txt, DOWN, buff=0.15)
        safe_group = VGroup(safe_box, safe_txt, safe_sub)

        self.play(FadeIn(mm_group, shift=DOWN * 0.4), run_time=1.2)
        self.play(FadeIn(safe_group, scale=1.1), run_time=1.2)
        self.wait(4.6)

        # ----------------------------------------------------
        # BEAT 2: [7.0s - 15.0s] "You aren't a hedge fund... you're an individual buying 50 shares of Apple"
        # ----------------------------------------------------
        self.play(FadeOut(safe_group), run_time=0.6)

        # Prominent Apple stock order card
        apple_card = RoundedRectangle(corner_radius=0.3, width=7.2, height=3.6, stroke_color=TEXT, stroke_width=3, fill_color="#181C24", fill_opacity=0.98).move_to(UP * 1.0)
        a_tag = CleanText("LUNCH-BREAK ORDER // MOBILE", font_size=13, color=TEXT, fill_opacity=0.7).move_to(apple_card.get_top() + DOWN * 0.45)
        a_ticker = CleanText("AAPL  (APPLE INC.)", font_size=24, color=TEXT, weight="BOLD").next_to(a_tag, DOWN, buff=0.25)
        a_shares = CleanText("50 SHARES @ $150.00", font_size=20, color=SUCCESS, weight="BOLD").next_to(a_ticker, DOWN, buff=0.25)
        a_cost = CleanText("TOTAL VALUE: $7,500.00", font_size=13, color=TEXT, fill_opacity=0.8).next_to(a_shares, DOWN, buff=0.2)
        apple_group = VGroup(apple_card, a_tag, a_ticker, a_shares, a_cost)

        self.play(FadeIn(apple_group, shift=UP * 0.4), run_time=1.2)
        self.wait(6.2)

        # ----------------------------------------------------
        # BEAT 3: [15.0s - 23.5s] "Pay your broker for the privilege of filling it... PFOF"
        # ----------------------------------------------------
        self.play(
            apple_group.animate.scale(0.65).move_to(DOWN * 5.2),
            mm_group.animate.scale(0.85).move_to(UP * 5.2),
            run_time=1.0
        )

        broker_card = RoundedRectangle(corner_radius=0.2, width=5.8, height=2.2, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#1E232F", fill_opacity=0.96).move_to(UP * 0.5)
        b_hdr = CleanText("RETAIL BROKER NODE", font_size=15, color=TEXT, weight="BOLD").move_to(broker_card.get_top() + DOWN * 0.4)
        b_rev = CleanText("ORDER DESTINATION: CITADEL", font_size=12, color=SUCCESS).next_to(b_hdr, DOWN, buff=0.15)
        b_stat = CleanText("STATUS: KICKBACK COLLECTED", font_size=13, color=RISK, weight="BOLD").next_to(b_rev, DOWN, buff=0.15)
        broker_group = VGroup(broker_card, b_hdr, b_rev, b_stat)

        # Upward order pipe
        up_pipe = Arrow(start=DOWN * 3.5, end=broker_card.get_bottom(), stroke_color=SUCCESS, stroke_width=3.5, buff=0.1)
        up_lbl = CleanText("APPLE ORDER", font_size=12, color=SUCCESS, weight="BOLD").next_to(up_pipe, LEFT, buff=0.1)

        # Downward Kickback Arrow
        down_pipe = Arrow(start=mm_box.get_bottom() + RIGHT * 1.5, end=broker_card.get_top() + RIGHT * 1.5, stroke_color=RISK, stroke_width=4, buff=0.1)
        down_lbl = CleanText("CASH PAYMENT (PFOF)", font_size=12, color=RISK, weight="BOLD").next_to(down_pipe, RIGHT, buff=0.15)

        self.play(FadeIn(broker_group), Create(up_pipe), FadeIn(up_lbl), run_time=1.2)
        self.play(Create(down_pipe), FadeIn(down_lbl), run_time=1.2)
        self.wait(5.1)

        # ----------------------------------------------------
        # BEAT 4: [23.5s - 35.25s] "Robinhood generating over $200M every single quarter selling order flow"
        # ----------------------------------------------------
        self.play(
            FadeOut(apple_group), FadeOut(broker_group), FadeOut(up_pipe), FadeOut(up_lbl),
            FadeOut(down_pipe), FadeOut(down_lbl), FadeOut(mm_group),
            run_time=0.8
        )

        rev_title = CleanText("QUARTERLY ORDER FLOW REVENUE", font_size=16, color=TEXT, weight="BOLD").move_to(UP * 5.4)

        # Large Bar Chart Eruption
        chart_base = Line(start=LEFT * 3.2 + DOWN * 1.8, end=RIGHT * 3.2 + DOWN * 1.8, stroke_color=UI_STRUCTURE, stroke_width=2.5)

        # Quarter bars
        b1 = Rectangle(width=1.2, height=1.5, stroke_color=UI_STRUCTURE, stroke_width=1.5, fill_color="#1E232F", fill_opacity=0.8).move_to(LEFT * 2.0 + DOWN * 1.05)
        b1_lbl = CleanText("Q1", font_size=12, color=TEXT, fill_opacity=0.6).next_to(b1, DOWN, buff=0.15)

        b2 = Rectangle(width=1.2, height=2.6, stroke_color=UI_STRUCTURE, stroke_width=1.5, fill_color="#1E232F", fill_opacity=0.8).move_to(LEFT * 0.4 + DOWN * 0.5)
        b2_lbl = CleanText("Q2", font_size=12, color=TEXT, fill_opacity=0.6).next_to(b2, DOWN, buff=0.15)

        # Massive Peak Bar (Pumpkin)
        b3 = Rectangle(width=1.6, height=5.2, stroke_color=RISK, stroke_width=3, fill_color=RISK, fill_opacity=0.9).move_to(RIGHT * 1.8 + UP * 0.8)
        b3_lbl = CleanText("PEAK", font_size=13, color=RISK, weight="BOLD").next_to(b3, DOWN, buff=0.15)

        bar_val = CleanText("$200,000,000+", font_size=24, color=TEXT, weight="BOLD").next_to(b3, UP, buff=0.2)
        bar_sub = CleanText("PER QUARTER // PFOF ONLY", font_size=12, color=RISK, weight="BOLD").next_to(bar_val, UP, buff=0.15)

        badge = RoundedRectangle(corner_radius=0.15, width=5.2, height=1.1, stroke_color=TEXT, stroke_width=2, fill_color=TEXT, fill_opacity=0.95).move_to(DOWN * 4.5)
        badge_txt = CleanText("PFOF KICKBACK", font_size=16, color=BACKGROUND, weight="BOLD").move_to(badge.get_center())
        badge_group = VGroup(badge, badge_txt)

        self.play(FadeIn(rev_title), Create(chart_base), run_time=0.6)
        self.play(FadeIn(b1), FadeIn(b1_lbl), FadeIn(b2), FadeIn(b2_lbl), run_time=1.0)
        self.play(GrowFromEdge(b3, DOWN), FadeIn(b3_lbl), run_time=1.2)
        self.play(FadeIn(bar_val, scale=1.15), FadeIn(bar_sub), run_time=1.0)
        self.play(FadeIn(badge_group, scale=1.1), run_time=0.8)
        self.wait(6.35)
