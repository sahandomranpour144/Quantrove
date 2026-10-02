"""
EP05 Scene 10: 3 Actionable Defense Steps (04:23.00 - 04:59.88, TARGET: EXACTLY 36.88s)
3 interactive defense cards:
1. Limit Orders Only (Price locked with padlock icon and slippage barrier)
2. Audit Trade Confirmations (Order history execution tape check against NBBO)
3. Direct Routing Brokers (PFOF broker vs Direct Market Access comparison)
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene10DefenseSteps(Scene):
    def construct(self):
        TARGET_DURATION = 36.88

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Main Title
        main_hdr = CleanText("EXECUTION DEFENSE // TAKE CONTROL", font_size=17, color=TEXT)
        main_hdr.shift(UP * 2.6)
        main_title = CleanText("3 RULES TO PROTECT YOUR MONEY", font_size=30, color=TEXT, weight="BOLD")
        main_title.next_to(main_hdr, DOWN, buff=0.15)

        # 3. Step 1: Limit Orders Only
        card1 = RoundedRectangle(corner_radius=0.2, width=4.1, height=3.6, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.96).move_to(LEFT * 4.4 + DOWN * 0.4)
        c1_badge = CleanText("RULE 01", font_size=15, color=SUCCESS, weight="BOLD").move_to(card1.get_top() + DOWN * 0.35)
        c1_t = CleanText("LIMIT ORDERS ONLY", font_size=18, color=TEXT, weight="BOLD").next_to(c1_badge, DOWN, buff=0.18)
        c1_sub1 = CleanText("Never hit Market Order", font_size=13, color=RISK).next_to(c1_t, DOWN, buff=0.2)
        c1_sub2 = CleanText("You set your exact price,", font_size=13, color=TEXT).next_to(c1_sub1, DOWN, buff=0.12)
        c1_sub3 = CleanText("not the market maker.", font_size=13, color=TEXT).next_to(c1_sub2, DOWN, buff=0.08)

        lock_box = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.6, stroke_color=SUCCESS, stroke_width=2, fill_color="#1D2A20", fill_opacity=1.0).next_to(c1_sub3, DOWN, buff=0.25)
        lock_txt = CleanText("🔒 PRICE LOCKED", font_size=12, color=SUCCESS, weight="BOLD").move_to(lock_box)
        c1_grp = VGroup(card1, c1_badge, c1_t, c1_sub1, c1_sub2, c1_sub3, lock_box, lock_txt)

        # 4. Step 2: Audit Confirmations
        card2 = RoundedRectangle(corner_radius=0.2, width=4.1, height=3.6, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.96).move_to(DOWN * 0.4)
        c2_badge = CleanText("RULE 02", font_size=15, color=SUCCESS, weight="BOLD").move_to(card2.get_top() + DOWN * 0.35)
        c2_t = CleanText("AUDIT YOUR NBBO", font_size=18, color=TEXT, weight="BOLD").next_to(c2_badge, DOWN, buff=0.18)
        c2_sub1 = CleanText("Open trade confirmations", font_size=13, color=TEXT, fill_opacity=0.60).next_to(c2_t, DOWN, buff=0.2)
        c2_sub2 = CleanText("under your app's history.", font_size=13, color=TEXT).next_to(c2_sub1, DOWN, buff=0.12)
        c2_sub3 = CleanText("Compare fill vs market bid/ask.", font_size=13, color=SUCCESS).next_to(c2_sub2, DOWN, buff=0.12)

        stmt_box = RoundedRectangle(corner_radius=0.1, width=2.5, height=0.6, stroke_color=SUCCESS, stroke_width=2, fill_color="#1D2A20", fill_opacity=1.0).next_to(c2_sub3, DOWN, buff=0.25)
        stmt_txt = CleanText("📄 VERIFY FILL", font_size=12, color=SUCCESS, weight="BOLD").move_to(stmt_box)
        c2_grp = VGroup(card2, c2_badge, c2_t, c2_sub1, c2_sub2, c2_sub3, stmt_box, stmt_txt)

        # 5. Step 3: Direct Routing Brokers
        card3 = RoundedRectangle(corner_radius=0.2, width=4.1, height=3.6, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.96).move_to(RIGHT * 4.4 + DOWN * 0.4)
        c3_badge = CleanText("RULE 03", font_size=15, color=SUCCESS, weight="BOLD").move_to(card3.get_top() + DOWN * 0.35)
        c3_t = CleanText("DIRECT ROUTING", font_size=18, color=TEXT, weight="BOLD").next_to(c3_badge, DOWN, buff=0.18)
        c3_sub1 = CleanText("For active traders:", font_size=13, color=TEXT, fill_opacity=0.60).next_to(c3_t, DOWN, buff=0.2)
        c3_sub2 = CleanText("Use direct access brokers", font_size=13, color=TEXT).next_to(c3_sub1, DOWN, buff=0.12)
        c3_sub3 = CleanText("that reject PFOF revenue.", font_size=13, color=SUCCESS).next_to(c3_sub2, DOWN, buff=0.12)

        dir_box = RoundedRectangle(corner_radius=0.1, width=2.6, height=0.6, stroke_color=SUCCESS, stroke_width=2, fill_color="#1D2A20", fill_opacity=1.0).next_to(c3_sub3, DOWN, buff=0.25)
        dir_txt = CleanText("⚡ DIRECT MARKET", font_size=12, color=SUCCESS, weight="BOLD").move_to(dir_box)
        c3_grp = VGroup(card3, c3_badge, c3_t, c3_sub1, c3_sub2, c3_sub3, dir_box, dir_txt)

        all_content = VGroup(main_hdr, main_title, c1_grp, c2_grp, c3_grp)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.2)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 36.88s) -----------------
        # Beat 1: Main Header & Title (1.5s) + hold (1.0s) = 2.5s
        self.play(FadeIn(main_hdr), FadeIn(main_title), run_time=1.5)
        self.wait(1.0)

        # Beat 2: RULE 01 - Limit Orders Only (9.0s) -> cumulative 11.5s
        self.play(FadeIn(c1_grp, shift=UP * 0.2 * s_factor), run_time=2.0)
        self.play(lock_box.animate.scale(1.15), run_time=1.5)
        self.play(lock_box.animate.scale(1.0 / 1.15), run_time=1.5)
        self.play(card1.animate.set_stroke(color=SUCCESS, width=4.0), run_time=2.0)
        self.play(card1.animate.set_stroke(color=SUCCESS, width=2.5), run_time=2.0)

        # Beat 3: RULE 02 - Audit Your NBBO (10.0s) -> cumulative 21.5s
        self.play(FadeIn(c2_grp, shift=UP * 0.2 * s_factor), run_time=2.0)
        self.play(stmt_box.animate.scale(1.15), run_time=1.5)
        self.play(stmt_box.animate.scale(1.0 / 1.15), run_time=1.5)
        self.play(card2.animate.set_stroke(color=SUCCESS, width=4.0), run_time=2.5)
        self.play(card2.animate.set_stroke(color=SUCCESS, width=2.5), run_time=2.5)

        # Beat 4: RULE 03 - Direct Routing (10.5s) -> cumulative 32.0s
        self.play(FadeIn(c3_grp, shift=UP * 0.2 * s_factor), run_time=2.0)
        self.play(dir_box.animate.scale(1.15), run_time=1.5)
        self.play(dir_box.animate.scale(1.0 / 1.15), run_time=1.5)
        self.play(card3.animate.set_stroke(color=SUCCESS, width=4.0), run_time=2.75)
        self.play(card3.animate.set_stroke(color=SUCCESS, width=2.5), run_time=2.75)

        # Beat 5: All 3 cards resonate simultaneously with glowing Power Lime (4.88s) -> cumulative 36.88s
        self.play(
            card1.animate.set_stroke(color=SUCCESS, width=4.5),
            card2.animate.set_stroke(color=SUCCESS, width=4.5),
            card3.animate.set_stroke(color=SUCCESS, width=4.5),
            run_time=2.44
        )
        self.play(
            card1.animate.set_stroke(color=SUCCESS, width=2.5),
            card2.animate.set_stroke(color=SUCCESS, width=2.5),
            card3.animate.set_stroke(color=SUCCESS, width=2.5),
            run_time=2.44
        )
