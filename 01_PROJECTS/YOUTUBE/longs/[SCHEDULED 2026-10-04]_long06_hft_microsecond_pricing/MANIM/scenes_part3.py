"""
Quantrove EP06 Manim Scenes — Part 3 (S18, S20, S21, S22, S23, S25)
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


class Scene18MicrosecondLight(Scene):
    """
    S18: Speed of Light in 1 Microsecond (Vacuum vs Fiber Glass)
    Target Duration: 17.56s
    """
    def construct(self):
        title = CleanText("THE SPEED OF LIGHT // 1 MICROSECOND (1 us)", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("DISTANCE TRAVELED IN ONE MILLIONTH OF A SECOND", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.4)

        # Distance ruler across frame
        ruler_w = 9.0
        ruler_line = Line(start=np.array([-4.5, 0.2, 0.0]), end=np.array([4.5, 0.2, 0.0]), stroke_color=UI_STRUCTURE, stroke_width=2)
        m0 = CleanText("0 m", font_size=13, color=UI_STRUCTURE).next_to(ruler_line.get_left(), DOWN, buff=0.15)
        m100 = CleanText("100 m", font_size=13, color=UI_STRUCTURE).move_to(np.array([-1.5, -0.05, 0.0]))
        m200 = CleanText("200 m (Fiber)", font_size=13, color=SUCCESS).move_to(np.array([1.5, -0.05, 0.0]))
        m300 = CleanText("300 m (Vacuum)", font_size=13, color=TEXT).next_to(ruler_line.get_right(), DOWN, buff=0.15)

        self.play(Create(ruler_line), FadeIn(m0), FadeIn(m100), FadeIn(m200), FadeIn(m300), run_time=2.0)
        self.wait(0.5)

        # Pulse 1: Vacuum Speed (c = 300 m/us)
        vac_lbl = CleanText("VACUUM: ~ 300 METERS", font_size=16, color=TEXT, weight="BOLD")
        vac_lbl.move_to(np.array([-1.0, 1.0, 0.0]))
        vac_dot = Dot(point=np.array([-4.5, 0.5, 0.0]), radius=0.09, color=TEXT)
        vac_trail = Line(start=np.array([-4.5, 0.5, 0.0]), end=np.array([4.5, 0.5, 0.0]), stroke_color=TEXT, stroke_width=3)

        # Pulse 2: Fiber Speed (v = 200 m/us)
        fib_lbl = CleanText("GLASS FIBER: ~ 200 METERS", font_size=16, color=SUCCESS, weight="BOLD")
        fib_lbl.move_to(np.array([-1.0, -0.8, 0.0]))
        fib_dot = Dot(point=np.array([-4.5, -0.3, 0.0]), radius=0.09, color=SUCCESS)
        fib_trail = Line(start=np.array([-4.5, -0.3, 0.0]), end=np.array([1.5, -0.3, 0.0]), stroke_color=SUCCESS, stroke_width=3)

        self.play(FadeIn(vac_lbl), FadeIn(fib_lbl), run_time=1.2)
        self.play(
            Create(vac_trail), vac_dot.animate.move_to(np.array([4.5, 0.5, 0.0])),
            Create(fib_trail), fib_dot.animate.move_to(np.array([1.5, -0.3, 0.0])),
            run_time=2.4, rate_func=linear
        )
        self.wait(1.0)

        # Takeaway callout box
        call_box = RoundedRectangle(corner_radius=0.15, width=10.5, height=0.85, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        call_box.move_to(STAGE_CENTER + DOWN * 1.95)
        call_txt = CleanText("A machine a few hundred meters closer hears the price move first", font_size=15, color=SUCCESS, weight="BOLD")
        call_txt.move_to(call_box)

        self.play(Create(call_box), FadeIn(call_txt), run_time=1.8)

        # Hold to match 17.56s
        self.wait(7.26)


class Scene20QueueLine(Scene):
    """
    S20: Price-Time Priority Queue Line
    Target Duration: 13.78s
    """
    def construct(self):
        title = CleanText("PRICE-TIME PRIORITY // THE ORDER BOOK QUEUE", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("AT THE SAME PRICE, ARRIVAL SPEED DETERMINES EXECUTION", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.4)

        # 6 Queue Blocks at Price $100.00
        q_label = CleanText("RESTING BIDS AT $100.00 (QUEUE ARRIVAL ORDER):", font_size=15, color=TEXT)
        q_label.move_to(STAGE_CENTER + UP * 0.9)
        self.play(FadeIn(q_label), run_time=1.0)

        blocks = VGroup()
        b_w = 1.4
        b_h = 1.1
        start_x = -4.0

        for i in range(6):
            b = RoundedRectangle(corner_radius=0.12, width=b_w, height=b_h, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.9)
            b.move_to(np.array([start_x + i * 1.6, -0.1, 0.0]))
            t_num = CleanText(f"#{i+1}", font_size=18, color=SUCCESS, weight="BOLD")
            t_num.move_to(b.get_center() + UP * 0.15)
            t_shr = CleanText("100 sh", font_size=11, color=TEXT)
            t_shr.move_to(b.get_center() + DOWN * 0.2)
            blocks.add(VGroup(b, t_num, t_shr))

        self.play(Create(blocks), run_time=2.2)
        self.wait(0.6)

        # Incoming Market Order fills #1 and #2
        order_tag = CleanText("INCOMING SELL: 200 SHARES", font_size=16, color=RISK, weight="BOLD")
        order_tag.move_to(STAGE_CENTER + DOWN * 1.3)
        self.play(FadeIn(order_tag), run_time=1.0)

        # Highlight fills
        self.play(
            blocks[0][0].animate.set_stroke(color=RISK, width=3).set_fill(color=RISK, opacity=0.3),
            blocks[1][0].animate.set_stroke(color=RISK, width=3).set_fill(color=RISK, opacity=0.3),
            run_time=1.6
        )

        fill_tag = CleanText("ORDERS #1 & #2 FILLED FIRST · #3 THROUGH #6 WAIT", font_size=14, color=TEXT)
        fill_tag.move_to(STAGE_CENTER + DOWN * 2.05)
        self.play(FadeIn(fill_tag), run_time=1.2)

        # Hold to match 13.78s
        self.wait(4.78)


class Scene21VirtuPayoff(Scene):
    """
    S21: Virtu Central Payoff — 1,238 Grid & Law of Large Numbers
    Target Duration: 27.62s
    """
    def construct(self):
        title = CleanText("THE VIRTU PAYOFF // LAW OF LARGE NUMBERS", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("WHY REPEATING A 51% EDGE MILLIONS OF TIMES ELIMINATES LUCK", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.6)

        # Left Card: Instant Hedging Mechanics
        left_card = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.2, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        left_card.shift(LEFT * 3.2 + DOWN * 0.15)

        l_title = CleanText("MARKET-NEUTRAL STRATEGY", font_size=16, color=SUCCESS, weight="BOLD")
        l_title.move_to(left_card.get_top() + DOWN * 0.4)

        l_1 = CleanText("1. Capture fraction of 1¢ spread", font_size=13, color=TEXT)
        l_1.next_to(l_title, DOWN, buff=0.3)

        l_2 = CleanText("2. Instant microsecond hedge", font_size=13, color=TEXT)
        l_2.next_to(l_1, DOWN, buff=0.22)

        l_3 = CleanText("3. Zero directional market exposure", font_size=13, color=TEXT)
        l_3.next_to(l_2, DOWN, buff=0.22)

        l_tag = CleanText("(AS REPORTED IN S-1 FILING)", font_size=11, color=UI_STRUCTURE)
        l_tag.next_to(l_3, DOWN, buff=0.25)

        self.play(Create(left_card), FadeIn(l_title), FadeIn(l_1), FadeIn(l_2), FadeIn(l_3), FadeIn(l_tag), run_time=2.8)
        self.wait(1.0)

        # Right Card: The Simons Callback
        right_card = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.2, stroke_color=SUCCESS, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        right_card.shift(RIGHT * 3.2 + DOWN * 0.15)

        r_title = CleanText("THE SIMONS PRINCIPLE (EP04)", font_size=16, color=SUCCESS, weight="BOLD")
        r_title.move_to(right_card.get_top() + DOWN * 0.4)

        r_1 = CleanText("50.75% Edge on 1 Trade = Noise", font_size=13, color=RISK)
        r_1.next_to(r_title, DOWN, buff=0.3)

        r_2 = CleanText("50.75% Edge on 10,000,000 Trades =", font_size=13, color=TEXT)
        r_2.next_to(r_1, DOWN, buff=0.22)

        r_3 = CleanText("CERTAINTY (1 LOSING DAY IN 1,238)", font_size=14, color=SUCCESS, weight="BOLD")
        r_3.next_to(r_2, DOWN, buff=0.22)

        r_sim = CleanText("ILLUSTRATIVE STATISTICAL CONVERGENCE", font_size=11, color=UI_STRUCTURE)
        r_sim.next_to(r_3, DOWN, buff=0.25)

        self.play(Create(right_card), FadeIn(r_title), FadeIn(r_1), FadeIn(r_2), FadeIn(r_3), FadeIn(r_sim), run_time=2.8)

        # Hold to match 27.62s
        self.wait(19.42)


class Scene22BothSides(Scene):
    """
    S22: Knight Capital vs Critics Debate
    Target Duration: 26.44s
    """
    def construct(self):
        title = CleanText("SPEED CUTS BOTH WAYS // RISK VS DEBATE", font_size=22, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("THE REALITY OF EXECUTION SPEED IN MODERN MARKETS", font_size=15, color=TEXT)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.6)

        # Left Box: Knight Capital Failure (August 2012)
        k_box = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.3, stroke_color=RISK, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        k_box.shift(LEFT * 3.1 + DOWN * 0.15)

        k_title = CleanText("KNIGHT CAPITAL · AUG 2012", font_size=16, color=RISK, weight="BOLD")
        k_title.move_to(k_box.get_top() + DOWN * 0.4)

        k_loss = CleanText("~ $460,000,000 LOSS", font_size=24, color=RISK, weight="BOLD")
        k_loss.next_to(k_title, DOWN, buff=0.3)

        k_desc = CleanText("In 45 minutes, a defective code\nloop flooded the market with\nerroneous buy/sell orders.", font_size=12, color=TEXT)
        k_desc.next_to(k_loss, DOWN, buff=0.25)

        k_src = CleanText("Source: SEC Administrative Proceeding (2013)", font_size=10, color=UI_STRUCTURE)
        k_src.move_to(k_box.get_bottom() + UP * 0.3)

        self.play(Create(k_box), FadeIn(k_title), FadeIn(k_loss), FadeIn(k_desc), FadeIn(k_src), run_time=2.8)
        self.wait(1.0)

        # Right Box: The Regulatory Debate
        d_box = RoundedRectangle(corner_radius=0.2, width=5.4, height=3.3, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color=BACKGROUND, fill_opacity=0.95)
        d_box.shift(RIGHT * 3.1 + DOWN * 0.15)

        d_title = CleanText("THE UNSETTLED ARGUMENT", font_size=16, color=TEXT, weight="BOLD")
        d_title.move_to(d_box.get_top() + DOWN * 0.4)

        d_l1 = CleanText("CRITICS:\nHigh-speed traders extract an unfair\ntax on ordinary investors.", font_size=12, color=RISK)
        d_l1.next_to(d_title, DOWN, buff=0.25)

        d_l2 = CleanText("MARKET MAKERS:\nSpreads narrowed 50%, saving\ninvestors billions in friction.", font_size=12, color=SUCCESS)
        d_l2.next_to(d_l1, DOWN, buff=0.25)

        d_foot = CleanText("Source: Academic Literature & Industry Comment", font_size=10, color=UI_STRUCTURE)
        d_foot.move_to(d_box.get_bottom() + UP * 0.3)

        self.play(Create(d_box), FadeIn(d_title), FadeIn(d_l1), FadeIn(d_l2), FadeIn(d_foot), run_time=2.8)

        # Hold to match 26.44s
        self.wait(18.24)


class Scene23FinalInsight(Scene):
    """
    S23: Final Insight Frame — Priced Doubt
    Target Duration: 15.48s
    """
    def construct(self):
        title = CleanText("THE SPREAD IS AN ANSWER", font_size=24, color=TEXT, weight="BOLD")
        title.move_to(STAGE_CENTER + UP * 2.2)

        sub = CleanText("NOT A FEE · AN EVALUATION OF UNCERTAINTY", font_size=15, color=SUCCESS)
        sub.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(sub), run_time=1.4)

        # Center Spread Bar 100.00 / 100.01
        bar = RoundedRectangle(corner_radius=0.2, width=8.8, height=1.3, stroke_color=SUCCESS, stroke_width=3, fill_color=BACKGROUND, fill_opacity=1.0)
        bar.move_to(STAGE_CENTER + UP * 0.5)

        t_bid = CleanText("BID $100.00", font_size=20, color=TEXT, weight="BOLD").move_to(bar.get_left() + RIGHT * 1.5)
        t_spread = CleanText("1¢ SPREAD", font_size=22, color=SUCCESS, weight="BOLD").move_to(bar.get_center())
        t_ask = CleanText("ASK $100.01", font_size=20, color=TEXT, weight="BOLD").move_to(bar.get_right() + LEFT * 1.5)

        self.play(Create(bar), FadeIn(t_bid), FadeIn(t_spread), FadeIn(t_ask), run_time=1.8)
        self.wait(0.5)

        # 3 Input Arrows feeding the spread
        in_box = RoundedRectangle(corner_radius=0.15, width=10.5, height=1.4, stroke_color=UI_STRUCTURE, stroke_width=1, fill_color=BACKGROUND, fill_opacity=0.95)
        in_box.move_to(STAGE_CENTER + DOWN * 1.1)

        f1 = CleanText("1. INVENTORY RISK", font_size=13, color=RISK).move_to(in_box.get_left() + RIGHT * 1.8)
        f2 = CleanText("2. VOLATILITY DRAG", font_size=13, color=RISK).move_to(in_box.get_center())
        f3 = CleanText("3. INFORMED TRADER ODDS", font_size=13, color=RISK).move_to(in_box.get_right() + LEFT * 2.2)

        self.play(Create(in_box), FadeIn(f1), FadeIn(f2), FadeIn(f3), run_time=2.0)
        self.wait(0.5)

        # Microsecond Ticker
        us_tag = CleanText("PRICED IN MICROSECONDS BEFORE YOU FINISH CLICKING", font_size=16, color=SUCCESS, weight="BOLD")
        us_tag.move_to(STAGE_CENTER + DOWN * 2.1)
        self.play(FadeIn(us_tag), run_time=1.2)

        # Hold to match 15.48s
        self.wait(8.08)


class Scene25EndScreenBg(Scene):
    """
    S25: End Screen Clean Slate (20.00s)
    Zero text, clean #202322 background with faint #233D4C grid for YouTube cards.
    """
    def construct(self):
        # Full frame grid line background strictly adhering to #233D4C at low opacity
        grid = NumberPlane(
            x_range=[-7.1, 7.1, 1], y_range=[-4.0, 4.0, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)
        # Exactly 20.00s wait
        self.wait(20.00)
