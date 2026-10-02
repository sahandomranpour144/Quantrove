"""
Quantrove Standalone Short 2: The Airport Currency Booth Trap
Format: 9:16 Vertical (1080x1920 @ 60fps)
Target Duration: Exactly 35.00s (Calibrated to 34.83s Voiceover)
Palette: Raisin Black #202322, Charcoal Slate #233D4C, Power Lime #C3D809, Pumpkin #FD802E, Off-White #E6EDF3
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

class AirportCurrencyTrap(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # BEAT 1: IDEA (0.0s - 7.5s) - Airport Currency Booth
        booth_box = RoundedRectangle(corner_radius=0.25, width=6.8, height=2.8, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.96).move_to(UP * 4.4)
        b_hdr = CleanText("AIRPORT MONEY EXCHANGE", font_size=15, color=SUCCESS, weight="BOLD").move_to(booth_box.get_top() + DOWN * 0.45)
        b_claim = CleanText("0% COMMISSION // ZERO FEES", font_size=18, color=TEXT, weight="BOLD").next_to(b_hdr, DOWN, buff=0.25)
        b_sub = CleanText("Exchange Any Global Currency Here", font_size=12, color=TEXT, fill_opacity=0.7).next_to(b_claim, DOWN, buff=0.18)
        booth_group = VGroup(booth_box, b_hdr, b_claim, b_sub)

        bill_box = RoundedRectangle(corner_radius=0.2, width=5.0, height=1.5, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#1A202C", fill_opacity=0.95).move_to(UP * 1.5)
        bill_txt = CleanText("HANDING OVER $100 USD", font_size=15, color=TEXT, weight="BOLD").move_to(bill_box)
        bill_group = VGroup(bill_box, bill_txt)

        self.play(FadeIn(booth_group, shift=DOWN * 0.3), run_time=1.2)
        self.play(FadeIn(bill_group, shift=UP * 0.3), run_time=1.0)
        self.wait(5.3)

        # BEAT 2: SIMPLE_WRONG (7.5s - 15.5s) - Google Market Rate
        google_box = RoundedRectangle(corner_radius=0.2, width=6.8, height=2.2, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(DOWN * 1.0)
        g_title = CleanText("GOOGLE REAL MARKET RATE", font_size=13, color=TEXT, fill_opacity=0.7).move_to(google_box.get_top() + DOWN * 0.4)
        g_rate = CleanText("1 USD = 0.90 EUR  (Expected: 90 EUR)", font_size=15, color=SUCCESS, weight="BOLD").next_to(g_title, DOWN, buff=0.2)
        google_group = VGroup(google_box, g_title, g_rate)

        self.play(FadeIn(google_group, shift=UP * 0.3), run_time=1.2)
        self.wait(6.8)

        # BEAT 3: COMPLEX_WRONG (15.5s - 23.5s) - The Shortfall Receipt
        receipt_box = RoundedRectangle(corner_radius=0.2, width=6.8, height=2.6, stroke_color=RISK, stroke_width=2.5, fill_color="#24140E", fill_opacity=0.96).move_to(DOWN * 4.0)
        r_hdr = CleanText("ACTUAL CASH RECEIVED: 82 EUR", font_size=15, color=RISK, weight="BOLD").move_to(receipt_box.get_top() + DOWN * 0.45)
        r_loss = CleanText("MISSING: -8 EUR // \"IS IT A TAX?\"", font_size=13, color=TEXT).next_to(r_hdr, DOWN, buff=0.2)
        r_note = CleanText("No fee on the receipt... where did it go?", font_size=12, color=TEXT, fill_opacity=0.7).next_to(r_loss, DOWN, buff=0.18)
        receipt_group = VGroup(receipt_box, r_hdr, r_loss, r_note)

        self.play(FadeIn(receipt_group, shift=UP * 0.3), run_time=1.2)
        self.wait(6.8)

        # BEAT 4: INSIGHT (23.5s - 35.0s) - Bid/Ask Spread Revealed
        self.play(
            FadeOut(booth_group), FadeOut(bill_group),
            FadeOut(google_group), FadeOut(receipt_group),
            run_time=1.0
        )

        spread_title = CleanText("THE SPREAD: WALL STREET'S INVISIBLE FEE", font_size=15, color=TEXT, weight="BOLD").move_to(UP * 5.4)

        # Ask Card
        ask_card = RoundedRectangle(corner_radius=0.2, width=7.0, height=2.0, stroke_color=RISK, stroke_width=2.5, fill_color="#24140E", fill_opacity=0.96).move_to(UP * 3.4)
        ask_hdr = CleanText("ASK PRICE // THEY SELL TO YOU", font_size=13, color=RISK).move_to(ask_card.get_top() + DOWN * 0.35)
        ask_val = CleanText("$0.95 PER EURO", font_size=22, color=TEXT, weight="BOLD").next_to(ask_hdr, DOWN, buff=0.15)
        ask_group = VGroup(ask_card, ask_hdr, ask_val)

        # Bid Card
        bid_card = RoundedRectangle(corner_radius=0.2, width=7.0, height=2.0, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.96).move_to(UP * 0.8)
        bid_hdr = CleanText("BID PRICE // THEY BUY FROM YOU", font_size=13, color=SUCCESS).move_to(bid_card.get_top() + DOWN * 0.35)
        bid_val = CleanText("$0.85 PER EURO", font_size=22, color=TEXT, weight="BOLD").next_to(bid_hdr, DOWN, buff=0.15)
        bid_group = VGroup(bid_card, bid_hdr, bid_val)

        # Gap Bracket
        gap_card = RoundedRectangle(corner_radius=0.2, width=7.0, height=1.8, stroke_color=RISK, stroke_width=3, fill_color="#2A1408", fill_opacity=0.98).move_to(DOWN * 1.8)
        gap_txt = CleanText("SPREAD GAP: $0.10 PROFIT PER EURO", font_size=15, color=RISK, weight="BOLD").move_to(gap_card.get_top() + DOWN * 0.45)
        gap_sub = CleanText("The Exact Same Math Governs Every Stock Trade", font_size=12, color=TEXT).next_to(gap_txt, DOWN, buff=0.2)
        gap_group = VGroup(gap_card, gap_txt, gap_sub)

        badge = RoundedRectangle(corner_radius=0.15, width=5.2, height=1.1, stroke_color=TEXT, stroke_width=2, fill_color=TEXT, fill_opacity=0.95).move_to(DOWN * 4.4)
        badge_txt = CleanText("SPREAD GAP", font_size=16, color=BACKGROUND, weight="BOLD").move_to(badge.get_center())
        badge_group = VGroup(badge, badge_txt)

        self.play(FadeIn(spread_title), run_time=0.6)
        self.play(FadeIn(ask_group, shift=DOWN * 0.3), FadeIn(bid_group, shift=UP * 0.3), run_time=1.2)
        self.play(FadeIn(gap_group, scale=1.05), run_time=1.0)
        self.play(FadeIn(badge_group, scale=1.1), run_time=0.8)
        self.wait(6.9)
