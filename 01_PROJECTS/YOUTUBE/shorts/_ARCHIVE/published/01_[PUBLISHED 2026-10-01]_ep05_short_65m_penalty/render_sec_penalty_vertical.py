"""
Quantrove EP05 Short: The $65 Million SEC Penalty
Format: 9:16 Vertical (1080x1920 @ 60fps)
Target Duration: Exactly 33.67s
Narration: Approved EP05 Master Stem (166.50s - 200.16s)
Visual Architecture: Customer Order -> Broker -> Routing -> Worse Execution -> SEC -> $65M Penalty -> Hidden Invoice
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

class SecPenaltyVertical(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # ----------------------------------------------------
        # BEAT 1: [0.0s - 5.0s] "If market makers are paying brokers, who ends up paying the bill?"
        # ----------------------------------------------------
        phone_box = RoundedRectangle(corner_radius=0.25, width=4.8, height=2.0, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 4.8)
        phone_title = CleanText("CUSTOMER ORDER FLOW", font_size=15, color=TEXT, weight="BOLD").move_to(phone_box.get_top() + DOWN * 0.4)
        phone_sub = CleanText("100 Shares // $0 Commission App", font_size=12, color=TEXT, fill_opacity=0.7).next_to(phone_title, DOWN, buff=0.15)
        phone_group = VGroup(phone_box, phone_title, phone_sub)

        broker_box = RoundedRectangle(corner_radius=0.2, width=4.8, height=1.8, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#1E232F", fill_opacity=0.95).move_to(UP * 1.5)
        b_name = CleanText("RETAIL BROKER", font_size=16, color=TEXT, weight="BOLD").move_to(broker_box.get_top() + DOWN * 0.4)
        b_status = CleanText("Collecting Order Kickbacks", font_size=12, color=RISK).next_to(b_name, DOWN, buff=0.15)
        broker_group = VGroup(broker_box, b_name, b_status)

        order_arrow = Arrow(start=phone_box.get_bottom(), end=broker_box.get_top(), stroke_color=SUCCESS, stroke_width=3, buff=0.1)

        question_card = RoundedRectangle(corner_radius=0.2, width=5.6, height=1.4, stroke_color=RISK, stroke_width=3, fill_color="#2A1408", fill_opacity=0.95).move_to(DOWN * 1.5)
        q_txt = CleanText("WHO PAYS THE BILL?", font_size=20, color=RISK, weight="BOLD").move_to(question_card)
        q_group = VGroup(question_card, q_txt)

        self.play(FadeIn(phone_group, shift=DOWN * 0.3), run_time=1.0)
        self.play(Create(order_arrow), FadeIn(broker_group, shift=UP * 0.2), run_time=1.2)
        self.play(FadeIn(q_group, scale=1.15), run_time=1.0)
        self.wait(1.8)

        # ----------------------------------------------------
        # BEAT 2: [5.0s - 12.0s] "In 2020, the SEC answered with a $65M enforcement settlement against Robinhood"
        # ----------------------------------------------------
        self.play(FadeOut(q_group), run_time=0.5)

        # Official SEC Seal Drops
        sec_badge = Circle(radius=1.3, stroke_color=RISK, stroke_width=4, fill_color="#24130C", fill_opacity=0.96).move_to(UP * 2.8)
        sec_title = CleanText("U.S. SEC", font_size=18, color=RISK, weight="BOLD").move_to(sec_badge.get_center() + UP * 0.45)
        sec_sub = CleanText("ENFORCEMENT", font_size=13, color=TEXT, weight="BOLD").next_to(sec_title, DOWN, buff=0.15)
        sec_group = VGroup(sec_badge, sec_title, sec_sub)

        # Massive $65,000,000 Penalty Payoff Card
        penalty_box = RoundedRectangle(corner_radius=0.25, width=7.2, height=3.2, stroke_color=RISK, stroke_width=3.5, fill_color="#181210", fill_opacity=0.98).move_to(DOWN * 1.0)
        p_label = CleanText("REGULATORY PENALTY (2020)", font_size=13, color=RISK).move_to(penalty_box.get_top() + DOWN * 0.4)
        p_amount = CleanText("$65,000,000", font_size=38, color=RISK, weight="BOLD").next_to(p_label, DOWN, buff=0.25)
        p_target = CleanText("SETTLEMENT: ROBINHOOD FINANCIAL", font_size=14, color=TEXT, weight="BOLD").next_to(p_amount, DOWN, buff=0.25)
        penalty_group = VGroup(penalty_box, p_label, p_amount, p_target)

        self.play(
            FadeOut(phone_group), FadeOut(broker_group), FadeOut(order_arrow),
            FadeIn(sec_group, scale=1.3),
            run_time=1.2
        )
        self.play(FadeIn(penalty_group, shift=UP * 0.5), run_time=1.3)
        self.wait(4.0)

        # ----------------------------------------------------
        # BEAT 3: [12.0s - 23.0s] "Routing orders to market makers paying the highest fees... worse execution prices"
        # ----------------------------------------------------
        self.play(FadeOut(sec_group), FadeOut(penalty_group), run_time=0.8)

        mech_title = CleanText("THE ORDER ROUTING MECHANISM", font_size=16, color=TEXT, weight="BOLD").move_to(UP * 5.6)

        # Left: Public Exchange Route (Closed)
        ex_card = RoundedRectangle(corner_radius=0.15, width=3.8, height=2.2, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.9).move_to(UP * 3.0 + LEFT * 2.1)
        ex_t = CleanText("PUBLIC EXCHANGES", font_size=12, color=TEXT, fill_opacity=0.7).move_to(ex_card.get_top() + DOWN * 0.35)
        ex_status = CleanText("NYSE // NASDAQ", font_size=14, color=TEXT, weight="BOLD").next_to(ex_t, DOWN, buff=0.15)
        ex_gate = CleanText("BYPASSED", font_size=12, color=RISK, weight="BOLD").next_to(ex_status, DOWN, buff=0.15)
        ex_group = VGroup(ex_card, ex_t, ex_status, ex_gate)

        # Right: Highest Fee PFOF Internalizer (Selected)
        pfof_card = RoundedRectangle(corner_radius=0.15, width=3.8, height=2.2, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.95).move_to(UP * 3.0 + RIGHT * 2.1)
        pfof_t = CleanText("WHOLESALE ROUTE", font_size=12, color=SUCCESS).move_to(pfof_card.get_top() + DOWN * 0.35)
        pfof_name = CleanText("HIGHEST BIDDER", font_size=14, color=TEXT, weight="BOLD").next_to(pfof_t, DOWN, buff=0.15)
        pfof_kick = CleanText("MAX PFOF PAYMENT", font_size=12, color=RISK, weight="BOLD").next_to(pfof_name, DOWN, buff=0.15)
        pfof_group = VGroup(pfof_card, pfof_t, pfof_name, pfof_kick)

        # Consequence Box: Worse Execution
        worse_box = RoundedRectangle(corner_radius=0.2, width=6.8, height=2.4, stroke_color=RISK, stroke_width=3, fill_color="#24140E", fill_opacity=0.96).move_to(DOWN * 0.8)
        w_hdr = CleanText("SEC OFFICIAL FINDING:", font_size=14, color=RISK, weight="BOLD").move_to(worse_box.get_top() + DOWN * 0.4)
        w_main = CleanText("INFERIOR TRADE EXECUTION", font_size=18, color=TEXT, weight="BOLD").next_to(w_hdr, DOWN, buff=0.2)
        w_sub = CleanText("Customer Orders Paid Higher Fill Prices", font_size=12, color=RISK).next_to(w_main, DOWN, buff=0.15)
        worse_group = VGroup(worse_box, w_hdr, w_main, w_sub)

        self.play(FadeIn(mech_title), run_time=0.6)
        self.play(FadeIn(ex_group, shift=RIGHT * 0.2), FadeIn(pfof_group, shift=LEFT * 0.2), run_time=1.2)
        self.play(FadeIn(worse_group, scale=1.08), run_time=1.2)
        self.wait(7.2)

        # ----------------------------------------------------
        # BEAT 4: [23.0s - 33.67s] "Free trading had a hidden invoice. Subtracted from your fill price..."
        # ----------------------------------------------------
        self.play(
            FadeOut(mech_title), FadeOut(ex_group), FadeOut(pfof_group), FadeOut(worse_group),
            run_time=0.8
        )

        invoice_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=4.2, stroke_color=RISK, stroke_width=3.5, fill_color="#181210", fill_opacity=0.98).move_to(UP * 1.5)
        inv_title = CleanText("RETAIL TRADER INVOICE", font_size=18, color=RISK, weight="BOLD").move_to(invoice_card.get_top() + DOWN * 0.45)
        inv_item1 = CleanText("STATED COMMISSION:   $0.00", font_size=14, color=SUCCESS).next_to(inv_title, DOWN, buff=0.4)
        inv_item2 = CleanText("HIDDEN FILL DRAG:   -$2.00 / 100 SHARES", font_size=15, color=RISK, weight="BOLD").next_to(inv_item1, DOWN, buff=0.3)
        inv_divider = Line(start=invoice_card.get_left() + RIGHT * 0.5, end=invoice_card.get_right() + LEFT * 0.5, stroke_color=UI_STRUCTURE, stroke_width=1.5).next_to(inv_item2, DOWN, buff=0.25)
        inv_total = CleanText("NET RESULT:  NOT FREE", font_size=18, color=TEXT, weight="BOLD").next_to(inv_divider, DOWN, buff=0.3)
        invoice_group = VGroup(invoice_card, inv_title, inv_item1, inv_item2, inv_divider, inv_total)

        badge = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.1, stroke_color=TEXT, stroke_width=2, fill_color=TEXT, fill_opacity=0.95).move_to(DOWN * 3.5)
        badge_txt = CleanText("$65M SEC PENALTY", font_size=16, color=BACKGROUND, weight="BOLD").move_to(badge.get_center())
        badge_group = VGroup(badge, badge_txt)

        self.play(FadeIn(invoice_group, shift=UP * 0.4), run_time=1.2)
        self.play(FadeIn(badge_group, scale=1.1), run_time=0.8)
        self.wait(7.87)
