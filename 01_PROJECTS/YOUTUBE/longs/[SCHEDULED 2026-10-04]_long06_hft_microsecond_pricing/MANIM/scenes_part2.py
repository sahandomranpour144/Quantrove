"""
Quantrove EP06 Manim Scenes — Part 2 (S10, S12, S13, S15, S16)
Palette: #202322 (Canvas), #233D4C (Chrome/Grid), #C3D809 (Lime), #FD802E (Pumpkin Risk), #E6EDF3 (Text)
Strictly adheres to CleanText, stage_fit, and exact calibrated durations.
"""

from manim import *
import numpy as np
import sys, os

# Setup paths for Quantrove pipeline theme
MANIM_DIR = os.path.dirname(os.path.abspath(__file__))
EPISODE_DIR = os.path.abspath(os.path.join(MANIM_DIR, ".."))
YOUTUBE_DIR = os.path.abspath(os.path.join(EPISODE_DIR, "..", ".."))
if YOUTUBE_DIR not in sys.path:
    sys.path.insert(0, YOUTUBE_DIR)

from pipeline.manim_theme import (
    apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT,
    STAGE_CENTER, stage_fit
)

apply_manim_theme(config, is_vertical=False, fps=60)


class Scene10PinnedSpread(Scene):
    """
    S10: Tick-Constrained Pinned Spread & 2024 Half-Cent Rule
    Target Duration: 18.02s
    """
    def construct(self):
        title = CleanText("THE PINNED SPREAD // TICK CONSTRAINT", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("WHEN THE 1¢ FLOOR PREVENTS NATURAL MARKET CLEARING", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.4)

        # Quotes ladder
        ladder_box = RoundedRectangle(corner_radius=0.2, width=8.5, height=2.8, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        ladder_box.move_to(STAGE_CENTER + DOWN * 0.1)

        ask_line = Line(start=np.array([-3.2, 0.7, 0.0]), end=np.array([3.2, 0.7, 0.0]), stroke_color=SUCCESS, stroke_width=3)
        ask_lbl = CleanText("ASK: $100.01", font_size=18, color=SUCCESS, weight="BOLD")
        ask_lbl.next_to(ask_line, UP, buff=0.15)

        bid_line = Line(start=np.array([-3.2, -0.7, 0.0]), end=np.array([3.2, -0.7, 0.0]), stroke_color=SUCCESS, stroke_width=3)
        bid_lbl = CleanText("BID: $100.00", font_size=18, color=SUCCESS, weight="BOLD")
        bid_lbl.next_to(bid_line, DOWN, buff=0.15)

        self.play(Create(ladder_box), Create(ask_line), FadeIn(ask_lbl), Create(bid_line), FadeIn(bid_lbl), run_time=2.2)
        self.wait(1.0)

        # Dashed half-cent gap (TICK-CONSTRAINED)
        half_cent_line = DashedLine(start=np.array([-3.2, 0.0, 0.0]), end=np.array([3.2, 0.0, 0.0]), stroke_color=RISK, stroke_width=2, dash_length=0.12)
        constraint_tag = CleanText("TICK-CONSTRAINED (0.5¢ NOT PERMITTED)", font_size=15, color=RISK, weight="BOLD")
        constraint_tag.move_to(np.array([0.0, 0.0, 0.0]))

        self.play(Create(half_cent_line), FadeIn(constraint_tag), run_time=2.0)
        self.wait(1.5)

        # SEC 2024 Rule update card
        rule_box = RoundedRectangle(corner_radius=0.15, width=10.5, height=0.9, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        rule_box.move_to(STAGE_CENTER + DOWN * 2.05)
        rule_txt = CleanText("SEC ADOPTED HALF-CENT TICK (2024) · COMPLIANCE DATE DELAYED", font_size=15, color=TEXT, weight="BOLD")
        rule_txt.move_to(rule_box)

        self.play(Create(rule_box), FadeIn(rule_txt), run_time=2.0)

        # Hold to match 18.02s
        self.wait(7.92)


class Scene12InventoryRisk(Scene):
    """
    S12: Avellaneda & Stoikov (2008) Inventory Risk
    Target Duration: 17.72s
    """
    def construct(self):
        title = CleanText("INVENTORY RISK // AVELLANEDA & STOIKOV (2008)", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("WHY A MARKET MAKER HATES HOLDING POSITIONS", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.5)

        # Left Container: Inventory Box q = 0 -> 3
        inv_box = RoundedRectangle(corner_radius=0.2, width=3.8, height=3.2, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        inv_box.shift(LEFT * 3.8 + DOWN * 0.2)

        inv_header = CleanText("INVENTORY HELD (q)", font_size=16, color=TEXT, weight="BOLD")
        inv_header.move_to(inv_box.get_top() + DOWN * 0.4)

        u1 = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.5, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9).move_to(inv_box.get_bottom() + UP * 0.6)
        t_u1 = CleanText("UNIT 1: RISK EXPOSURE", font_size=12, color=RISK)
        t_u1.move_to(u1)

        u2 = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.5, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9).next_to(u1, UP, buff=0.15)
        t_u2 = CleanText("UNIT 2: VOLATILITY DRAG", font_size=12, color=RISK)
        t_u2.move_to(u2)

        u3 = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.5, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9).next_to(u2, UP, buff=0.15)
        t_u3 = CleanText("UNIT 3: CAPITAL LOCKUP", font_size=12, color=RISK)
        t_u3.move_to(u3)

        self.play(Create(inv_box), FadeIn(inv_header), run_time=1.8)
        self.wait(0.5)

        # Stack units one by one
        self.play(Create(u1), FadeIn(t_u1), run_time=1.5)
        self.wait(0.4)
        self.play(Create(u2), FadeIn(t_u2), run_time=1.5)
        self.wait(0.4)
        self.play(Create(u3), FadeIn(t_u3), run_time=1.5)
        self.wait(0.8)

        # Right Card: Theoretical Insight
        r_card = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.2, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        r_card.shift(RIGHT * 3.2 + DOWN * 0.2)

        r_title = CleanText("THE CORE PRINCIPLE", font_size=17, color=RISK, weight="BOLD")
        r_title.move_to(r_card.get_top() + DOWN * 0.45)

        r_l1 = CleanText("Buying inventory = owning price risk", font_size=14, color=TEXT)
        r_l1.next_to(r_title, DOWN, buff=0.35)

        r_l2 = CleanText("Market makers want ZERO inventory", font_size=14, color=SUCCESS, weight="BOLD")
        r_l2.next_to(r_l1, DOWN, buff=0.25)

        r_l3 = CleanText("Quotes must skew to offload units fast", font_size=14, color=TEXT)
        r_l3.next_to(r_l2, DOWN, buff=0.25)

        self.play(Create(r_card), FadeIn(r_title), FadeIn(r_l1), FadeIn(r_l2), FadeIn(r_l3), run_time=2.5)

        # Hold to match 17.72s
        self.wait(5.32)


class Scene13ReservationPrice(Scene):
    """
    S13: Reservation Price Equation Breakdown
    Target Duration: 22.60s
    """
    def construct(self):
        title = CleanText("THE RESERVATION PRICE // MATH BREAKDOWN", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("HOW INVENTORY AND VOLATILITY PENALIZE THE QUOTE", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.5)

        # Main Equation Box
        eq_box = RoundedRectangle(corner_radius=0.2, width=10.5, height=1.3, stroke_color=SUCCESS, stroke_width=3, fill_color=BACKGROUND, fill_opacity=1.0)
        eq_box.move_to(STAGE_CENTER + UP * 0.8)

        eq_text = CleanText("r  =  s  -  q · γ · σ² · (T - t)", font_size=32, color=TEXT, weight="BOLD")
        eq_text.move_to(eq_box)

        self.play(Create(eq_box), FadeIn(eq_text), run_time=2.0)
        self.wait(1.0)

        # Term explanation grid below
        grid_w = 11.2
        grid_h = 2.4
        t_grid = RoundedRectangle(corner_radius=0.2, width=grid_w, height=grid_h, stroke_color=UI_STRUCTURE, stroke_width=1, fill_color=BACKGROUND, fill_opacity=0.95)
        t_grid.move_to(STAGE_CENTER + DOWN * 1.3)

        t_lbl1 = CleanText("r = Reservation Price (where machine feels neutral)", font_size=14, color=SUCCESS)
        t_lbl1.move_to(t_grid.get_top() + DOWN * 0.4)

        t_lbl2 = CleanText("s = Mid Price ($100.00)     |     q = Inventory Units Held", font_size=14, color=TEXT)
        t_lbl2.next_to(t_lbl1, DOWN, buff=0.2)

        t_lbl3 = CleanText("γ (Risk Aversion Factor)     |     σ² (Price Volatility Variance)", font_size=14, color=TEXT)
        t_lbl3.next_to(t_lbl2, DOWN, buff=0.2)

        t_lbl4 = CleanText("(T - t) = Trading Time Left Until Market Close", font_size=14, color=TEXT)
        t_lbl4.next_to(t_lbl3, DOWN, buff=0.2)

        self.play(Create(t_grid), FadeIn(t_lbl1), FadeIn(t_lbl2), FadeIn(t_lbl3), FadeIn(t_lbl4), run_time=3.0)

        # Hold to match 22.60s
        self.wait(15.10)


class Scene15SpreadFormula(Scene):
    """
    S15: Avellaneda-Stoikov Spread Decomposition
    Target Duration: 14.68s
    """
    def construct(self):
        title = CleanText("SPREAD DECOMPOSITION // THE TWO FORCES", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("RISK ABSORPTION PLUS ORDER BOOK COMPETITION", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.4)

        # Two Terms formula cards
        box_w = 5.2
        box_h = 2.5

        # Term 1: Risk Premium
        b1 = RoundedRectangle(corner_radius=0.2, width=box_w, height=box_h, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        b1.shift(LEFT * 3.0 + DOWN * 0.1)
        b1_title = CleanText("1. RISK PENALTY TERM", font_size=16, color=RISK, weight="BOLD")
        b1_title.move_to(b1.get_top() + DOWN * 0.4)
        b1_formula = CleanText("γ · σ² · (T - t)", font_size=20, color=TEXT, weight="BOLD")
        b1_formula.next_to(b1_title, DOWN, buff=0.25)
        b1_val = CleanText("~ $0.40", font_size=28, color=RISK, weight="BOLD")
        b1_val.next_to(b1_formula, DOWN, buff=0.2)

        # Term 2: Competition / Elasticity
        b2 = RoundedRectangle(corner_radius=0.2, width=box_w, height=box_h, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        b2.shift(RIGHT * 3.0 + DOWN * 0.1)
        b2_title = CleanText("2. COMPETITION TERM", font_size=16, color=SUCCESS, weight="BOLD")
        b2_title.move_to(b2.get_top() + DOWN * 0.4)
        b2_formula = CleanText("(2 / γ) · ln(1 + γ / k)", font_size=20, color=TEXT, weight="BOLD")
        b2_formula.next_to(b2_title, DOWN, buff=0.25)
        b2_val = CleanText("~ $1.29", font_size=28, color=SUCCESS, weight="BOLD")
        b2_val.next_to(b2_formula, DOWN, buff=0.2)

        self.play(Create(b1), FadeIn(b1_title), FadeIn(b1_formula), FadeIn(b1_val), run_time=2.2)
        self.wait(0.5)
        self.play(Create(b2), FadeIn(b2_title), FadeIn(b2_formula), FadeIn(b2_val), run_time=2.2)
        self.wait(0.8)

        # Sum Card at Bottom
        sum_box = RoundedRectangle(corner_radius=0.15, width=10.8, height=0.85, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        sum_box.move_to(STAGE_CENTER + DOWN * 2.05)
        sum_txt = CleanText("TOTAL SPREAD: $0.40 + $1.29 = $1.69  (TEXTBOOK PARAMETERS - NOT A REAL QUOTE)", font_size=14, color=TEXT, weight="BOLD")
        sum_txt.move_to(sum_box)

        self.play(Create(sum_box), FadeIn(sum_txt), run_time=1.8)

        # Hold to match 14.68s
        self.wait(5.78)


class Scene16RepriceShape(Scene):
    """
    S16: Dynamic Reprice Curve & Next Buyer Uncertainty
    Target Duration: 23.54s
    """
    def construct(self):
        title = CleanText("DYNAMIC REPRICING // CONSTANT SHIFTING", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("THE MACHINE NEVER HOLDS A STATIC PRICE", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.5)

        # Dynamic Repricing Ladder Table
        table_box = RoundedRectangle(corner_radius=0.2, width=6.2, height=3.2, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        table_box.shift(LEFT * 3.4 + DOWN * 0.15)

        r_hdr = CleanText("INVENTORY (q)   RESERVATION   BID / ASK", font_size=13, color=UI_STRUCTURE)
        r_hdr.move_to(table_box.get_top() + DOWN * 0.35)

        row0 = CleanText("q = 0             $100.00        99.16 / 100.85", font_size=13, color=TEXT)
        row0.next_to(r_hdr, DOWN, buff=0.25)

        row1 = CleanText("q = 1 (Buy)       $99.60         98.76 / 100.45", font_size=13, color=SUCCESS)
        row1.next_to(row0, DOWN, buff=0.2)

        row2 = CleanText("q = 2 (Buy)       $99.20         98.36 / 100.05", font_size=13, color=SUCCESS)
        row2.next_to(row1, DOWN, buff=0.2)

        row3 = CleanText("q = 3 (Buy)       $98.80         97.96 / 99.65", font_size=13, color=RISK)
        row3.next_to(row2, DOWN, buff=0.2)

        self.play(Create(table_box), FadeIn(r_hdr), FadeIn(row0), FadeIn(row1), FadeIn(row2), FadeIn(row3), run_time=3.2)
        self.wait(1.5)

        # Right Insight Card: The Unknown Input
        unk_card = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.2, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        unk_card.shift(RIGHT * 3.4 + DOWN * 0.15)

        unk_title = CleanText("THE MISSING INPUT", font_size=17, color=RISK, weight="BOLD")
        unk_title.move_to(unk_card.get_top() + DOWN * 0.45)

        unk_l1 = CleanText("The model prices risk,\nvolatility, and time.", font_size=13, color=TEXT)
        unk_l1.next_to(unk_title, DOWN, buff=0.3)

        unk_q = CleanText("WHO IS BUYING NEXT?", font_size=18, color=RISK, weight="BOLD")
        unk_q.next_to(unk_l1, DOWN, buff=0.35)

        unk_l2 = CleanText("Does the incoming trader\nknow more than the machine?", font_size=12, color=TEXT)
        unk_l2.next_to(unk_q, DOWN, buff=0.25)

        self.play(Create(unk_card), FadeIn(unk_title), FadeIn(unk_l1), FadeIn(unk_q), FadeIn(unk_l2), run_time=3.0)

        # Hold to match 23.54s
        self.wait(14.34)
