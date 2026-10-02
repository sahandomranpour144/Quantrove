"""
EP05 Scene 01: The Hook (00:00.00 - 00:20.00, TARGET: EXACTLY 20.00s)
Smartphone wireframe, $0 Commission Buy button, tap shatter animation,
encrypted hexadecimal particle stream routing to unseen buyer node,
and running micro-cents counter.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene01Hook(Scene):
    def construct(self):
        TARGET_DURATION = 20.00

        # 1. Background Grid strictly inside stage bounds
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.30}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Smartphone Outline & Retail App Header
        phone = RoundedRectangle(
            corner_radius=0.4, width=5.0, height=7.0,
            stroke_color=UI_STRUCTURE, stroke_width=3, fill_color="#161B22", fill_opacity=0.95
        ).shift(LEFT * 3.2)

        app_title = CleanText("ZERO-FEE BROKER // MOBILE", font_size=18, color=TEXT)
        app_title.move_to(phone.get_top() + DOWN * 0.5)

        stock_ticker = CleanText("AAPL  $150.00", font_size=36, color=TEXT, weight="BOLD")
        stock_ticker.next_to(app_title, DOWN, buff=0.4)

        buy_btn = RoundedRectangle(
            corner_radius=0.25, width=4.0, height=1.1,
            stroke_color=SUCCESS, stroke_width=3, fill_color=UI_STRUCTURE, fill_opacity=1.0
        ).next_to(stock_ticker, DOWN, buff=0.6)

        buy_txt = CleanText("BUY: $0 COMMISSION", font_size=24, color=SUCCESS, weight="BOLD")
        buy_txt.move_to(buy_btn)

        phone_group = VGroup(phone, app_title, stock_ticker, buy_btn, buy_txt)

        # 3. "UNSEEN BUYER" Node on the Right
        buyer_node = RoundedRectangle(
            corner_radius=0.3, width=4.4, height=3.2,
            stroke_color=RISK, stroke_width=3, fill_color="#181310", fill_opacity=0.95
        ).shift(RIGHT * 3.8 + UP * 0.8)

        buyer_title = CleanText("INTERNALIZER // HFT", font_size=18, color=RISK)
        buyer_title.move_to(buyer_node.get_top() + DOWN * 0.4)
        buyer_sub = CleanText("OFF-EXCHANGE LIQUIDITY", font_size=14, color=TEXT, fill_opacity=0.60)
        buyer_sub.next_to(buyer_title, DOWN, buff=0.15)
        buyer_status = CleanText("PURCHASING ORDER FLOW", font_size=20, color=TEXT, weight="BOLD")
        buyer_status.next_to(buyer_sub, DOWN, buff=0.4)

        buyer_group = VGroup(buyer_node, buyer_title, buyer_sub, buyer_status)

        # 4. Live Spread Tally & Compounding Ticker
        tally_box = RoundedRectangle(
            corner_radius=0.2, width=4.4, height=1.6,
            stroke_color=RISK, stroke_width=2, fill_color="#161B22", fill_opacity=0.9
        ).next_to(buyer_node, DOWN, buff=0.35)

        tally_lbl = CleanText("HIDDEN EXECUTION DRAG:", font_size=16, color=RISK)
        tally_lbl.move_to(tally_box.get_top() + DOWN * 0.35)

        tracker = ValueTracker(0.00)
        tally_num = CleanText("-$0.0000 / share", font_size=28, color=RISK, weight="BOLD")
        tally_num.next_to(tally_lbl, DOWN, buff=0.2)

        # 5. Punchy Hook Insight Stamp
        stamp_box = RoundedRectangle(
            corner_radius=0.15, width=6.8, height=1.1,
            stroke_color=RISK, stroke_width=3, fill_color="#2A1408", fill_opacity=0.95
        ).shift(DOWN * 2.8)
        stamp_txt = CleanText("YOU ARE NOT THE CUSTOMER. YOU ARE THE PRODUCT.", font_size=18, color=RISK, weight="BOLD")
        stamp_txt.move_to(stamp_box)

        all_content = VGroup(phone_group, buyer_group, tally_box, tally_lbl, tally_num, stamp_box, stamp_txt)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 20.00s) -----------------
        # Beat 1: Phone enters (1.8s) + brief hold (1.0s) = 2.8s
        self.play(FadeIn(phone_group, shift=RIGHT * 0.5 * s_factor), run_time=1.8)
        self.wait(1.0)

        # Beat 2: Tap Reticle & Press (0.4s + 0.3s + 0.5s = 1.2s) -> cumulative 4.0s
        tap_circle = Circle(radius=0.35 * s_factor, stroke_color=SUCCESS, stroke_width=3, color=SUCCESS, fill_opacity=0.3)
        tap_circle.move_to(buy_btn.get_center())
        self.play(FadeIn(tap_circle, scale=1.5), run_time=0.4)
        self.play(FadeOut(tap_circle, scale=0.5), buy_btn.animate.scale(0.96), run_time=0.3)
        self.play(buy_btn.animate.scale(1.0 / 0.96), run_time=0.5)

        # Beat 3: Buyer node appears (1.5s) -> cumulative 5.5s
        self.play(FadeIn(buyer_group, shift=LEFT * 0.5 * s_factor), run_time=1.5)

        # Beat 4: High-density particle stream from buy button to buyer node (3.5s) -> cumulative 9.0s
        particles = VGroup()
        for i in range(16):
            dot = Dot(radius=0.07 * s_factor, color=SUCCESS if i % 2 == 0 else TEXT)
            p_start = buy_btn.get_center()
            dot.move_to(p_start + np.array([np.random.uniform(-0.5, 0.5) * s_factor, np.random.uniform(-0.2, 0.2) * s_factor, 0]))
            particles.add(dot)

        self.play(
            LaggedStart(*[
                p.animate.move_to(buyer_node.get_center() + np.array([np.random.uniform(-0.8, 0.8) * s_factor, np.random.uniform(-0.5, 0.5) * s_factor, 0]))
                for p in particles
            ], lag_ratio=0.06),
            run_time=3.5
        )

        # Beat 5: Live spread tally activates and counts up (0.8s in + 5.5s count = 6.3s) -> cumulative 15.3s
        def update_tally(mob):
            v = tracker.get_value()
            mob.become(CleanText(f"-${v:.4f} / share", font_size=int(28 * s_factor), color=RISK, weight="BOLD").next_to(tally_lbl, DOWN, buff=0.2 * s_factor))

        tally_num.add_updater(update_tally)
        self.play(FadeIn(tally_box), FadeIn(tally_num), run_time=0.8)
        self.play(tracker.animate.set_value(0.0240), run_time=5.5, rate_func=linear)
        tally_num.remove_updater(update_tally)

        # Beat 6: Insight stamp slams down (1.5s) -> cumulative 16.8s
        self.play(FadeIn(stamp_box, scale=1.15), FadeIn(stamp_txt, scale=1.15), run_time=1.5)

        # Beat 7: Pulsing electrical highlight filling to exactly 20.00s (3.2s) -> cumulative 20.00s
        self.play(
            stamp_box.animate.set_stroke(color=RISK, width=5),
            buyer_node.animate.set_stroke(color=RISK, width=4.5),
            run_time=1.6
        )
        self.play(
            stamp_box.animate.set_stroke(color=RISK, width=3),
            buyer_node.animate.set_stroke(color=RISK, width=3),
            run_time=1.6
        )
