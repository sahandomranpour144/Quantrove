"""
Quantrove EP06 Short S06-04: HFT Doesn't Predict Prices
Format: 9:16 Vertical (1080x1920 @ 60fps)
Duration: ~32.0s (within 30-45s)
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

class HftNotPredictPrices(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # BEAT 1: [0.0s - 5.5s] IDEA
        title = CleanText("THE DIRECTIONAL MYTH", font_size=18, color=TEXT, weight="BOLD").move_to(UP * 6.5)
        sub = CleanText("DOES HFT PREDICT UP OR DOWN?", font_size=13, color=RISK).next_to(title, DOWN, buff=0.15)
        head_group = VGroup(title, sub)

        chart_card = RoundedRectangle(corner_radius=0.25, width=7.0, height=3.8, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 3.2)
        c_lbl = CleanText("ILLUSTRATIVE DATA", font_size=10, color=TEXT, fill_opacity=0.6).move_to(chart_card.get_top() + DOWN * 0.3 + RIGHT * 2.2)

        axes = Axes(x_range=[0, 10, 2], y_range=[0, 5, 1], x_length=5.6, y_length=2.2, axis_config={"color": UI_STRUCTURE, "stroke_width": 2}).move_to(chart_card.get_center() + DOWN * 0.2)
        curve = axes.plot(lambda x: 2.5 + 0.8 * np.sin(x * 1.5) + 0.3 * np.cos(x * 3), color=TEXT, stroke_width=3)
        tracer = Dot(color=SUCCESS, radius=0.12).move_to(curve.get_start())

        self.play(FadeIn(head_group, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(chart_card), FadeIn(c_lbl), run_time=0.8)
        self.play(Create(axes), Create(curve), run_time=1.6)
        self.play(MoveAlongPath(tracer, curve), run_time=2.0)

        # BEAT 2: [5.5s - 14.5s] SIMPLE_WRONG
        cross_line1 = Line(start=chart_card.get_corner(UL), end=chart_card.get_corner(DR), color=RISK, stroke_width=5)
        cross_line2 = Line(start=chart_card.get_corner(UR), end=chart_card.get_corner(DL), color=RISK, stroke_width=5)
        reject_tag = CleanText("DIRECTIONAL FORECASTING: REJECTED", font_size=14, color=RISK, weight="BOLD").move_to(DOWN * 0.2)
        sub_rej = CleanText("High Variance Coin Toss in Liquid Markets", font_size=11, color=TEXT).next_to(reject_tag, DOWN, buff=0.2)

        self.play(Create(cross_line1), run_time=1.0)
        self.play(Create(cross_line2), run_time=1.0)
        self.play(FadeIn(reject_tag, shift=UP * 0.2), FadeIn(sub_rej), run_time=1.2)
        self.play(cross_line1.animate.set_stroke(width=6), cross_line2.animate.set_stroke(width=6), run_time=1.0)
        self.play(reject_tag.animate.scale(1.08), sub_rej.animate.shift(UP * 0.1), run_time=1.2)
        self.play(tracer.animate.scale(1.2), run_time=1.0)
        self.wait(1.0)

        # BEAT 3: [14.5s - 26.5s] COMPLEX_WRONG
        chart_group = VGroup(chart_card, c_lbl, axes, curve, tracer, cross_line1, cross_line2, reject_tag, sub_rej)
        self.play(FadeOut(chart_group), run_time=0.8)

        mn_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=4.4, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 3.0)
        mn_title = CleanText("MARKET NEUTRAL SPREAD CAPTURE", font_size=15, color=SUCCESS, weight="BOLD").move_to(mn_card.get_top() + DOWN * 0.45)

        bid_box = RoundedRectangle(corner_radius=0.15, width=2.8, height=1.4, stroke_color=SUCCESS, stroke_width=2, fill_color="#202322").move_to(mn_card.get_center() + LEFT * 1.8 + UP * 0.3)
        b_txt = CleanText("BUY BID\\n$100.00", font_size=12, color=SUCCESS, weight="BOLD").move_to(bid_box)

        ask_box = RoundedRectangle(corner_radius=0.15, width=2.8, height=1.4, stroke_color=RISK, stroke_width=2, fill_color="#202322").move_to(mn_card.get_center() + RIGHT * 1.8 + UP * 0.3)
        a_txt = CleanText("SELL ASK\\n$100.01", font_size=12, color=RISK, weight="BOLD").move_to(ask_box)

        hedge_arrow = DoubleArrow(start=bid_box.get_right(), end=ask_box.get_left(), color=SUCCESS, stroke_width=3)
        hedge_lbl = CleanText("IMMEDIATE INVENTORY HEDGE", font_size=11, color=TEXT, weight="BOLD").next_to(hedge_arrow, UP, buff=0.1)

        edge_txt = CleanText("SPREAD CAPTURE: +$0.01 / SHARE", font_size=13, color=TEXT, weight="BOLD").move_to(mn_card.get_bottom() + UP * 0.5)

        self.play(FadeIn(mn_card), FadeIn(mn_title), run_time=0.9)
        self.play(FadeIn(bid_box), FadeIn(b_txt), run_time=1.0)
        self.play(FadeIn(ask_box), FadeIn(a_txt), run_time=1.0)
        self.play(Create(hedge_arrow), FadeIn(hedge_lbl), run_time=1.2)
        self.play(FadeIn(edge_txt, scale=1.05), run_time=1.1)
        self.play(mn_card.animate.set_stroke(SUCCESS, width=3.5), run_time=1.0)
        self.play(edge_txt.animate.scale(1.08), run_time=1.0)
        self.wait(1.5)

        # BEAT 4: [26.5s - 39.0s] INSIGHT
        mn_group = VGroup(mn_card, mn_title, bid_box, b_txt, ask_box, a_txt, hedge_arrow, hedge_lbl, edge_txt)
        self.play(FadeOut(mn_group), run_time=0.8)

        virtu_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=4.2, stroke_color=SUCCESS, stroke_width=3, fill_color="#181C24", fill_opacity=0.96).move_to(UP * 2.8)
        v_title = CleanText("VIRTU FINANCIAL // SEC S-1 FILING", font_size=15, color=SUCCESS, weight="BOLD").move_to(virtu_card.get_top() + DOWN * 0.45)
        v_stat = CleanText("1,238 TRADING DAYS", font_size=26, color=SUCCESS, weight="BOLD").move_to(virtu_card.get_center() + UP * 0.5)
        v_loss = CleanText("EXACTLY 1 LOSING DAY", font_size=14, color=RISK, weight="BOLD").next_to(v_stat, DOWN, buff=0.2)
        v_disclaimer = CleanText("ILLUSTRATIVE DATA // SEC DISCLOSED RECORD", font_size=9, color=TEXT, fill_opacity=0.6).next_to(v_loss, DOWN, buff=0.35)

        badge_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.2, stroke_color=SUCCESS, stroke_width=3, fill_color="#181C24", fill_opacity=0.98).move_to(DOWN * 1.5)
        badge_txt = CleanText("TINY EDGE REPEATED", font_size=17, color=SUCCESS, weight="BOLD").move_to(badge_box)
        badge_group = VGroup(badge_box, badge_txt)

        self.play(FadeIn(virtu_card), FadeIn(v_title), run_time=0.9)
        self.play(FadeIn(v_stat, scale=1.15), run_time=1.2)
        self.play(FadeIn(v_loss), FadeIn(v_disclaimer), run_time=1.0)
        self.play(FadeIn(badge_group, shift=UP * 0.3), run_time=1.2)
        self.play(badge_box.animate.set_stroke(SUCCESS, width=4.5), run_time=1.0)
        self.play(badge_txt.animate.scale(1.08), run_time=1.0)
        self.wait(1.5)
