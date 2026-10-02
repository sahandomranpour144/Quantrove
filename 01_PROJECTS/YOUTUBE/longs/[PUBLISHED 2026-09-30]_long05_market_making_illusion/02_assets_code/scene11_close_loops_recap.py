"""
EP05 Scene 11: Closing the Loops (04:59.88 - 05:16.80, TARGET: EXACTLY 16.92s)
The 4 open-loop dossier cards return in a 2x2 grid, each snapping closed
with a Power Lime checkmark, resolving the Loop Ledger completely.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene11CloseLoopsRecap(Scene):
    def construct(self):
        TARGET_DURATION = 16.92

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Header
        hdr = CleanText("QUANTROVE DOSSIER #05 // RESOLUTION", font_size=17, color=TEXT)
        hdr.shift(UP * 2.5)
        title = CleanText("THE ORDER FLOW SUMMARY", font_size=30, color=TEXT, weight="BOLD")
        title.next_to(hdr, DOWN, buff=0.15)

        # 3. 2x2 Grid of Resolved Loops
        def make_resolved_card(num, text, pos):
            card = RoundedRectangle(
                corner_radius=0.15, width=5.6, height=1.4,
                stroke_color=SUCCESS, stroke_width=2, fill_color="#141E22", fill_opacity=0.96
            ).move_to(pos)

            chk = CleanText("✓", font_size=22, color=SUCCESS, weight="BOLD").move_to(card.get_left() + RIGHT * 0.35)
            n = CleanText(num, font_size=13, color=TEXT, fill_opacity=0.60).next_to(chk, RIGHT, buff=0.18)
            t = CleanText(text, font_size=15, color=TEXT, weight="BOLD").next_to(n, RIGHT, buff=0.2)

            return VGroup(card, chk, n, t)

        c1 = make_resolved_card("01", "Orders routed to wholesalers, not exchange", np.array([-3.2, 0.7, 0]))
        c2 = make_resolved_card("02", "Market makers profit off bid/ask spread", np.array([ 3.2, 0.7, 0]))
        c3 = make_resolved_card("03", "Brokers paid kickbacks (PFOF revenue)", np.array([-3.2, -0.9, 0]))
        c4 = make_resolved_card("04", "Limit orders & NBBO audits protect you", np.array([ 3.2, -0.9, 0]))

        # 4. Center Resolution Seal
        seal_box = RoundedRectangle(
            corner_radius=0.15, width=6.2, height=0.9,
            stroke_color=SUCCESS, stroke_width=3, fill_color="#182A1C", fill_opacity=0.98
        ).shift(DOWN * 2.3)

        seal_txt = CleanText("LOOP LEDGER: 100% RESOLVED", font_size=19, color=SUCCESS, weight="BOLD").move_to(seal_box)
        seal_grp = VGroup(seal_box, seal_txt)

        all_content = VGroup(hdr, title, c1, c2, c3, c4, seal_grp)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 16.92s) -----------------
        # Beat 1: Header & Title (1.5s)
        self.play(FadeIn(hdr), FadeIn(title), run_time=1.5)

        # Beat 2: Card 1 enters with checkmark strike (1.5s + 1.0s) = 2.5s -> cumulative 4.0s
        self.play(FadeIn(c1, shift=DOWN * 0.2 * s_factor), run_time=1.5)
        self.play(c1[1].animate.scale(1.3), run_time=0.5)
        self.play(c1[1].animate.scale(1.0 / 1.3), run_time=0.5)

        # Beat 3: Card 2 enters with checkmark strike (1.5s + 1.0s) = 2.5s -> cumulative 6.5s
        self.play(FadeIn(c2, shift=DOWN * 0.2 * s_factor), run_time=1.5)
        self.play(c2[1].animate.scale(1.3), run_time=0.5)
        self.play(c2[1].animate.scale(1.0 / 1.3), run_time=0.5)

        # Beat 4: Card 3 enters with checkmark strike (1.5s + 1.0s) = 2.5s -> cumulative 9.0s
        self.play(FadeIn(c3, shift=DOWN * 0.2 * s_factor), run_time=1.5)
        self.play(c3[1].animate.scale(1.3), run_time=0.5)
        self.play(c3[1].animate.scale(1.0 / 1.3), run_time=0.5)

        # Beat 5: Card 4 enters with checkmark strike (1.5s + 1.0s) = 2.5s -> cumulative 11.5s
        self.play(FadeIn(c4, shift=DOWN * 0.2 * s_factor), run_time=1.5)
        self.play(c4[1].animate.scale(1.3), run_time=0.5)
        self.play(c4[1].animate.scale(1.0 / 1.3), run_time=0.5)

        # Beat 6: Center resolution seal slams down (2.5s) -> cumulative 14.0s
        self.play(FadeIn(seal_box, scale=1.2), FadeIn(seal_txt, scale=1.2), run_time=1.5)
        self.play(seal_box.animate.set_stroke(color=SUCCESS, width=5.0), run_time=1.0)

        # Beat 7: Final checkmark resonance pulse to exact duration (2.92s) -> cumulative 16.92s
        self.play(
            seal_box.animate.set_stroke(color=SUCCESS, width=3.0),
            c1[0].animate.set_stroke(color=SUCCESS, width=3.5),
            c2[0].animate.set_stroke(color=SUCCESS, width=3.5),
            c3[0].animate.set_stroke(color=SUCCESS, width=3.5),
            c4[0].animate.set_stroke(color=SUCCESS, width=3.5),
            run_time=1.46
        )
        self.play(
            c1[0].animate.set_stroke(color=SUCCESS, width=2.0),
            c2[0].animate.set_stroke(color=SUCCESS, width=2.0),
            c3[0].animate.set_stroke(color=SUCCESS, width=2.0),
            c4[0].animate.set_stroke(color=SUCCESS, width=2.0),
            run_time=1.46
        )
