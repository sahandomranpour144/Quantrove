"""
Quantrove EP06 Manim Scenes — Part 1 (S02, S04, S05, S08, S09)
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


class Scene02Grid1238(Scene):
    """
    S02: 1,238-day grid from Virtu Financial S-1.
    Target Duration: 15.00s
    """
    def construct(self):
        # 1. Title and metadata header
        header = CleanText("1,238 TRADING DAYS // VIRTU FINANCIAL S-1", font_size=24, color=TEXT, weight="BOLD")
        header.move_to(STAGE_CENTER + UP * 2.1)

        subhead = CleanText("JAN 2009 – DEC 2013 · REAL-TIME RISK RECORD", font_size=15, color=TEXT)
        subhead.next_to(header, DOWN, buff=0.15)

        self.play(FadeIn(header), FadeIn(subhead), run_time=1.2)

        # 2. Build 62-column grid of dots/cells (62 cols x 20 rows = 1240, 1238 active)
        cols = 62
        rows = 20
        total_cells = 1238

        grid_group = VGroup()
        dot_radius = 0.04
        x_spacing = 0.16
        y_spacing = 0.12

        x_start = - (cols * x_spacing) / 2.0 + 0.08
        y_start = 0.90

        dots = []
        for i in range(total_cells):
            r = i // cols
            c = i % cols
            x = x_start + c * x_spacing
            y = y_start - r * y_spacing
            dot = Dot(point=np.array([x, y, 0.0]), radius=dot_radius, color=UI_STRUCTURE)
            dots.append(dot)
            grid_group.add(dot)

        self.add(grid_group)
        self.wait(0.8)

        # Turn dots into lime in sweeps
        # Orange outlier cell at index 734 (arbitrary illustrative position)
        orange_idx = 734

        # Batch animate filling lime
        batch_size = 62
        anim_time_per_batch = 0.25
        num_batches = (total_cells + batch_size - 1) // batch_size

        for b in range(min(num_batches, 16)):
            idx_start = b * batch_size
            idx_end = min((b + 1) * batch_size, total_cells)
            batch_dots = dots[idx_start:idx_end]
            self.play(
                *[d.animate.set_color(SUCCESS) for d in batch_dots if d != dots[orange_idx]],
                run_time=anim_time_per_batch,
                rate_func=linear
            )

        # Complete remaining dots quickly
        remaining = [d for d in dots[16 * batch_size:] if d != dots[orange_idx]]
        if remaining:
            self.play(*[d.animate.set_color(SUCCESS) for d in remaining], run_time=0.8)

        # Highlight single orange losing day with opaque callout badge
        orange_dot = dots[orange_idx]
        circle_hl = Circle(radius=0.20, stroke_color=RISK, stroke_width=2.5).move_to(orange_dot.get_center())

        callout_box = RoundedRectangle(corner_radius=0.15, width=3.4, height=0.65, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=1.0)
        callout_box.move_to(orange_dot.get_center() + UP * 0.75 + LEFT * 0.2)
        callout = CleanText("ONE LOSING DAY", font_size=17, color=RISK, weight="BOLD")
        callout.move_to(callout_box)
        callout_arrow = Line(start=callout_box.get_bottom(), end=circle_hl.get_top(), stroke_color=RISK, stroke_width=2)

        tag = CleanText("POSITION ILLUSTRATIVE  |  SOURCE: VIRTU FORM S-1 (2014)", font_size=13, color=TEXT)
        tag.move_to(STAGE_CENTER + DOWN * 1.85)

        self.play(
            orange_dot.animate.set_color(RISK),
            Create(circle_hl),
            Create(callout_box),
            Create(callout_arrow),
            FadeIn(callout),
            FadeIn(tag),
            run_time=1.4
        )

        # Final hold to match 15.00s exactly
        self.wait(6.80)


class Scene04ZeroCost(Scene):
    """
    S04: Glosten & Milgrom (1985) Zero Cost Stack
    Target Duration: 18.90s
    """
    def construct(self):
        title = CleanText("GLOSTEN & MILGROM (1985) // ZERO COST EXPERIMENT", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("CAN A SPREAD EXIST WHEN EVERY FRICTION IS ELIMINATED?", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.15)

        self.play(FadeIn(title), FadeIn(sub), run_time=1.5)

        # 3 Stacked Bars
        box_w = 7.5
        box_h = 0.75

        b1 = RoundedRectangle(corner_radius=0.15, width=box_w, height=box_h, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        b1.move_to(STAGE_CENTER + UP * 0.9)
        t1_lbl = CleanText("EXCHANGE & ROUTING FEES", font_size=17, color=TEXT)
        t1_lbl.move_to(b1.get_left() + RIGHT * 2.2)
        t1_val = CleanText("= $0.00", font_size=20, color=SUCCESS, weight="BOLD")
        t1_val.move_to(b1.get_right() + LEFT * 1.2)

        b2 = RoundedRectangle(corner_radius=0.15, width=box_w, height=box_h, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        b2.next_to(b1, DOWN, buff=0.25)
        t2_lbl = CleanText("OVERHEAD & INFRASTRUCTURE", font_size=17, color=TEXT)
        t2_lbl.move_to(b2.get_left() + RIGHT * 2.2)
        t2_val = CleanText("= $0.00", font_size=20, color=SUCCESS, weight="BOLD")
        t2_val.move_to(b2.get_right() + LEFT * 1.2)

        b3 = RoundedRectangle(corner_radius=0.15, width=box_w, height=box_h, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        b3.next_to(b2, DOWN, buff=0.25)
        t3_lbl = CleanText("MARKET MAKER EXPECTED PROFIT", font_size=17, color=TEXT)
        t3_lbl.move_to(b3.get_left() + RIGHT * 2.2)
        t3_val = CleanText("= $0.00", font_size=20, color=SUCCESS, weight="BOLD")
        t3_val.move_to(b3.get_right() + LEFT * 1.2)

        self.play(Create(b1), FadeIn(t1_lbl), FadeIn(t1_val), run_time=2.2)
        self.wait(0.5)
        self.play(Create(b2), FadeIn(t2_lbl), FadeIn(t2_val), run_time=2.2)
        self.wait(0.5)
        self.play(Create(b3), FadeIn(t3_lbl), FadeIn(t3_val), run_time=2.2)
        self.wait(0.8)

        # Result Divider & Spread Question
        res_line = Line(start=np.array([-4.0, -1.2, 0.0]), end=np.array([4.0, -1.2, 0.0]), stroke_color=UI_STRUCTURE, stroke_width=2)

        res_box = RoundedRectangle(corner_radius=0.2, width=8.2, height=1.0, stroke_color=RISK, stroke_width=3, fill_color=BACKGROUND, fill_opacity=1.0)
        res_box.next_to(res_line, DOWN, buff=0.25)

        spread_lbl = CleanText("EQUILIBRIUM SPREAD :", font_size=20, color=TEXT, weight="BOLD")
        spread_lbl.move_to(res_box.get_left() + RIGHT * 2.0)

        spread_q = CleanText("STILL EXISTS  ( > 0 )", font_size=22, color=RISK, weight="BOLD")
        spread_q.move_to(res_box.get_right() + LEFT * 2.3)

        self.play(Create(res_line), run_time=1.0)
        self.play(Create(res_box), FadeIn(spread_lbl), FadeIn(spread_q), run_time=2.0)

        # Hold to match 18.90s
        self.wait(6.0)


class Scene05AdverseSelection(Scene):
    """
    S05: Adverse Selection Mechanism (Informed vs Uninformed)
    Target Duration: 22.78s
    """
    def construct(self):
        title = CleanText("THE MECHANISM // ADVERSE SELECTION", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("WHY THE SPREAD CANNOT COLLAPSE TO ZERO", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.5)

        # Center Node: Market Maker Machine
        mm_box = RoundedRectangle(corner_radius=0.2, width=3.8, height=2.0, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        mm_box.move_to(STAGE_CENTER + DOWN * 0.1)
        mm_lbl = CleanText("MARKET MAKER", font_size=18, color=TEXT, weight="BOLD")
        mm_lbl.move_to(mm_box.get_top() + DOWN * 0.45)
        mm_quote = CleanText("ASK: $100.01  |  BID: $100.00", font_size=14, color=SUCCESS)
        mm_quote.next_to(mm_lbl, DOWN, buff=0.25)

        self.play(Create(mm_box), FadeIn(mm_lbl), FadeIn(mm_quote), run_time=1.8)
        self.wait(0.5)

        # Trader 1: Uninformed Trader (Lime, Left)
        t1_box = RoundedRectangle(corner_radius=0.15, width=3.4, height=1.5, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        t1_box.shift(LEFT * 4.6 + UP * 0.6)
        t1_title = CleanText("UNINFORMED TRADER", font_size=15, color=SUCCESS, weight="BOLD")
        t1_title.move_to(t1_box.get_top() + DOWN * 0.35)
        t1_desc = CleanText("Random liquidity need\nNo private price signal", font_size=12, color=TEXT)
        t1_desc.next_to(t1_title, DOWN, buff=0.15)

        arrow1 = Arrow(start=t1_box.get_right(), end=mm_box.get_left() + UP * 0.4, stroke_color=SUCCESS, stroke_width=2, buff=0.1)

        self.play(Create(t1_box), FadeIn(t1_title), FadeIn(t1_desc), Create(arrow1), run_time=2.2)
        self.wait(1.5)

        # Trader 2: Informed Trader (Orange / Risk, Left Lower)
        t2_box = RoundedRectangle(corner_radius=0.15, width=3.4, height=1.5, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        t2_box.shift(LEFT * 4.6 + DOWN * 1.3)
        t2_title = CleanText("INFORMED TRADER", font_size=15, color=RISK, weight="BOLD")
        t2_title.move_to(t2_box.get_top() + DOWN * 0.35)
        t2_desc = CleanText("Knows news / fast signal\nBuys right before price jumps", font_size=12, color=TEXT)
        t2_desc.next_to(t2_title, DOWN, buff=0.15)

        arrow2 = Arrow(start=t2_box.get_right(), end=mm_box.get_left() + DOWN * 0.4, stroke_color=RISK, stroke_width=2, buff=0.1)

        self.play(Create(t2_box), FadeIn(t2_title), FadeIn(t2_desc), Create(arrow2), run_time=2.5)
        self.wait(1.5)

        # Right Outcome Panel: Expected Post-Trade Jump
        res_card = RoundedRectangle(corner_radius=0.2, width=3.8, height=3.0, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        res_card.shift(RIGHT * 4.6 + DOWN * 0.3)

        c_title = CleanText("CONSEQUENCE", font_size=16, color=RISK, weight="BOLD")
        c_title.move_to(res_card.get_top() + DOWN * 0.4)

        c_line1 = CleanText("Sells to informed @ $100.01", font_size=13, color=TEXT)
        c_line1.next_to(c_title, DOWN, buff=0.3)

        c_line2 = CleanText("Fair price jumps to $100.11", font_size=13, color=RISK, weight="BOLD")
        c_line2.next_to(c_line1, DOWN, buff=0.2)

        c_line3 = CleanText("Spread must cover this loss\nfrom informed order flow", font_size=12, color=TEXT)
        c_line3.next_to(c_line2, DOWN, buff=0.25)

        arrow_out = Arrow(start=mm_box.get_right(), end=res_card.get_left(), stroke_color=RISK, stroke_width=2, buff=0.1)

        self.play(Create(res_card), FadeIn(c_title), FadeIn(c_line1), FadeIn(c_line2), FadeIn(c_line3), Create(arrow_out), run_time=2.8)

        # Hold to match 22.78s
        self.wait(8.48)


class Scene08TickHistory(Scene):
    """
    S08: Minimum Tick Step Chart (NYSE Decimals)
    Target Duration: 29.52s
    """
    def construct(self):
        title = CleanText("TICK SIZE EVOLUTION // NEW YORK STOCK EXCHANGE", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("HOW THE RULEBOOK NARROWED THE MINIMUM SPREAD", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.8)

        # 3 Step Timeline Cards
        w = 3.6
        h = 2.4

        # Step 1: Pre-1997 (12.5 cents)
        c1 = RoundedRectangle(corner_radius=0.2, width=w, height=h, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        c1.shift(LEFT * 4.2 + DOWN * 0.2)
        c1_date = CleanText("PRE-JUNE 1997", font_size=14, color=TEXT)
        c1_date.move_to(c1.get_top() + DOWN * 0.35)
        c1_val = CleanText("12.5¢", font_size=36, color=TEXT, weight="BOLD")
        c1_val.next_to(c1_date, DOWN, buff=0.15)
        c1_frac = CleanText("1/8th of a dollar", font_size=13, color=UI_STRUCTURE)
        c1_frac.next_to(c1_val, DOWN, buff=0.1)

        # Step 2: 1997 - 2001 (6.25 cents)
        c2 = RoundedRectangle(corner_radius=0.2, width=w, height=h, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        c2.shift(DOWN * 0.2)
        c2_date = CleanText("JUNE 1997 – JAN 2001", font_size=14, color=TEXT)
        c2_date.move_to(c2.get_top() + DOWN * 0.35)
        c2_val = CleanText("6.25¢", font_size=36, color=TEXT, weight="BOLD")
        c2_val.next_to(c2_date, DOWN, buff=0.15)
        c2_frac = CleanText("1/16th of a dollar", font_size=13, color=UI_STRUCTURE)
        c2_frac.next_to(c2_val, DOWN, buff=0.1)

        # Step 3: Jan 29, 2001 (1 cent)
        c3 = RoundedRectangle(corner_radius=0.2, width=w, height=h, stroke_color=SUCCESS, stroke_width=3, fill_color=BACKGROUND, fill_opacity=1.0)
        c3.shift(RIGHT * 4.2 + DOWN * 0.2)
        c3_date = CleanText("JANUARY 29, 2001", font_size=14, color=SUCCESS)
        c3_date.move_to(c3.get_top() + DOWN * 0.35)
        c3_val = CleanText("1.0¢", font_size=38, color=SUCCESS, weight="BOLD")
        c3_val.next_to(c3_date, DOWN, buff=0.15)
        c3_frac = CleanText("Decimalization", font_size=13, color=SUCCESS)
        c3_frac.next_to(c3_val, DOWN, buff=0.1)

        self.play(Create(c1), FadeIn(c1_date), FadeIn(c1_val), FadeIn(c1_frac), run_time=2.2)
        self.wait(1.5)
        self.play(Create(c2), FadeIn(c2_date), FadeIn(c2_val), FadeIn(c2_frac), run_time=2.2)
        self.wait(1.5)
        self.play(Create(c3), FadeIn(c3_date), FadeIn(c3_val), FadeIn(c3_frac), run_time=2.2)
        self.wait(2.0)

        # Impact bar at bottom: Example on $50 stock
        impact_box = RoundedRectangle(corner_radius=0.15, width=12.0, height=0.9, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        impact_box.move_to(STAGE_CENTER + DOWN * 1.95)

        t_comp = CleanText("ON A $50 STOCK:  Floor falls from 0.125% (6.25¢)  -->  0.020% (1.0¢) of share price", font_size=16, color=TEXT, weight="BOLD")
        t_comp.move_to(impact_box)

        self.play(Create(impact_box), FadeIn(t_comp), run_time=2.5)

        # Hold to match 29.52s
        self.wait(13.62)


class Scene09SecSpreadDrop(Scene):
    """
    S09: SEC Spread Drop Bars (-37% NYSE, -50% Nasdaq)
    Target Duration: 17.28s
    """
    def construct(self):
        title = CleanText("DECIMALIZATION IMPACT // SEC STAFF REPORT (2001)", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("AVERAGE QUOTED SPREAD REDUCTION ACROSS EXCHANGES", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.4)

        # 2 Comparison Bars
        # NYSE Bar
        nyse_box = RoundedRectangle(corner_radius=0.2, width=4.5, height=2.8, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        nyse_box.shift(LEFT * 2.8 + DOWN * 0.1)
        nyse_lbl = CleanText("NYSE QUOTED SPREADS", font_size=17, color=TEXT, weight="BOLD")
        nyse_lbl.move_to(nyse_box.get_top() + DOWN * 0.45)
        nyse_val = CleanText("-37%", font_size=54, color=SUCCESS, weight="BOLD")
        nyse_val.next_to(nyse_lbl, DOWN, buff=0.25)
        nyse_sub = CleanText("Average narrowing", font_size=13, color=TEXT)
        nyse_sub.next_to(nyse_val, DOWN, buff=0.15)

        # Nasdaq Bar
        nasdaq_box = RoundedRectangle(corner_radius=0.2, width=4.5, height=2.8, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
        nasdaq_box.shift(RIGHT * 2.8 + DOWN * 0.1)
        nasdaq_lbl = CleanText("NASDAQ QUOTED SPREADS", font_size=17, color=TEXT, weight="BOLD")
        nasdaq_lbl.move_to(nasdaq_box.get_top() + DOWN * 0.45)
        nasdaq_val = CleanText("-50%", font_size=54, color=SUCCESS, weight="BOLD")
        nasdaq_val.next_to(nasdaq_lbl, DOWN, buff=0.25)
        nasdaq_sub = CleanText("Average narrowing", font_size=13, color=TEXT)
        nasdaq_sub.next_to(nasdaq_val, DOWN, buff=0.15)

        self.play(Create(nyse_box), FadeIn(nyse_lbl), FadeIn(nyse_val), FadeIn(nyse_sub), run_time=2.2)
        self.wait(0.5)
        self.play(Create(nasdaq_box), FadeIn(nasdaq_lbl), FadeIn(nasdaq_val), FadeIn(nasdaq_sub), run_time=2.2)
        self.wait(0.8)

        # Footnote Card
        foot_box = RoundedRectangle(corner_radius=0.15, width=10.2, height=0.8, stroke_color=UI_STRUCTURE, stroke_width=1, fill_color=BACKGROUND, fill_opacity=0.8)
        foot_box.move_to(STAGE_CENTER + DOWN * 2.05)
        foot_txt = CleanText("Effective spreads fell ~15% · Market maker trading revenues dropped significantly", font_size=14, color=RISK)
        foot_txt.move_to(foot_box)

        self.play(Create(foot_box), FadeIn(foot_txt), run_time=1.6)

        # Hold to match 17.28s
        self.wait(8.58)
