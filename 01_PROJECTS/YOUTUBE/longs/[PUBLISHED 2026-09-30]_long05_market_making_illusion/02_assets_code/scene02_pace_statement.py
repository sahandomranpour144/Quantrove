"""
EP05 Scene 02: Pace Statement & Open Loop Progress Dossier (00:20.00 - 00:38.24, TARGET: EXACTLY 18.24s)
3-part illuminated dossier progress bar with live millisecond clock countdown (05:00.00)
and open-loop chapter anchors.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene02PaceStatement(Scene):
    def construct(self):
        TARGET_DURATION = 18.24

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Header: Quantrove Research Dossier #05
        header = CleanText("QUANTROVE RESEARCH // DOSSIER #05", font_size=20, color=TEXT)
        header.shift(UP * 2.8)
        headline = CleanText("THE ORDER FLOW INVESTIGATION", font_size=36, color=TEXT, weight="BOLD")
        headline.next_to(header, DOWN, buff=0.25)

        # 3. Three Chapter Dossier Cards
        def make_card(num, title, subtitle, color, x_pos):
            card = RoundedRectangle(
                corner_radius=0.2, width=4.2, height=3.2,
                stroke_color=color, stroke_width=2.5, fill_color="#161B22", fill_opacity=0.95
            ).move_to(np.array([x_pos, -0.1, 0]))

            badge = RoundedRectangle(
                corner_radius=0.1, width=1.0, height=0.5,
                stroke_color=color, stroke_width=1.5, fill_color=UI_STRUCTURE, fill_opacity=1.0
            ).move_to(card.get_top() + DOWN * 0.45 + LEFT * 1.2)
            b_txt = CleanText(num, font_size=16, color=color, weight="BOLD").move_to(badge)

            t = CleanText(title, font_size=19, color=TEXT, weight="BOLD").next_to(badge, RIGHT, buff=0.2)
            t.shift(UP * 0.02)

            line = Line(start=card.get_left() + RIGHT * 0.3, end=card.get_right() + LEFT * 0.3, stroke_color=UI_STRUCTURE, stroke_width=1.5)
            line.next_to(badge, DOWN, buff=0.25)

            s1 = CleanText(subtitle[0], font_size=15, color=color).next_to(line, DOWN, buff=0.3)
            s2 = CleanText(subtitle[1], font_size=13, color=TEXT, fill_opacity=0.60).next_to(s1, DOWN, buff=0.18)

            return VGroup(card, badge, b_txt, t, line, s1, s2)

        c1 = make_card("01", "THE ROUTER", ["Citadel & Virtu", "Wholesale internalizers"], SUCCESS, -4.5)
        c2 = make_card("02", "THE SEC CASE", ["$65M Settlement", "Best execution deception"], RISK, 0.0)
        c3 = make_card("03", "THE DEFENSE", ["Limit Orders & NBBO", "3 rules to take control"], SUCCESS, 4.5)

        # 4. Live Countdown Clock at Bottom
        clock_box = RoundedRectangle(
            corner_radius=0.15, width=6.0, height=1.0,
            stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#18202A", fill_opacity=0.9
        ).shift(DOWN * 2.6)

        clock_lbl = CleanText("FAST-PACED AUDIT // TIME REMAINING:", font_size=15, color=TEXT, fill_opacity=0.60)
        clock_lbl.next_to(clock_box, UP, buff=0.15)

        tracker = ValueTracker(300.0)
        clock_txt = CleanText("05:00.00", font_size=30, color=SUCCESS, weight="BOLD").move_to(clock_box)

        # Stage fit all content
        all_content = VGroup(header, headline, c1, c2, c3, clock_box, clock_lbl, clock_txt)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 18.24s) -----------------
        # Beat 1: Header & Headline appear (1.5s)
        self.play(FadeIn(header, shift=DOWN * 0.2 * s_factor), FadeIn(headline, shift=DOWN * 0.2 * s_factor), run_time=1.5)

        # Beat 2, 3, 4: Three chapter dossier cards enter sequentially (1.2s each = 3.6s) -> cumulative 5.1s
        self.play(FadeIn(c1, shift=UP * 0.3 * s_factor), run_time=1.2)
        self.play(FadeIn(c2, shift=UP * 0.3 * s_factor), run_time=1.2)
        self.play(FadeIn(c3, shift=UP * 0.3 * s_factor), run_time=1.2)

        # Beat 5: Clock reveals (1.0s) -> cumulative 6.1s
        def update_clock(mob):
            val = tracker.get_value()
            m = int(val // 60)
            s = int(val % 60)
            ms = int((val % 1) * 100)
            mob.become(CleanText(f"{m:02d}:{s:02d}.{ms:02d}", font_size=int(30 * s_factor), color=SUCCESS, weight="BOLD").move_to(clock_box))

        clock_txt.add_updater(update_clock)
        self.play(FadeIn(clock_box), FadeIn(clock_lbl), FadeIn(clock_txt), run_time=1.0)

        # Beat 6: Live clock countdown with active milliseconds (11.0s) -> cumulative 17.1s
        self.play(tracker.animate.set_value(289.0), run_time=11.0, rate_func=linear)
        clock_txt.remove_updater(update_clock)

        # Beat 7: Electrical dossier pulse to exact duration (1.14s) -> cumulative 18.24s
        self.play(
            c1[0].animate.set_stroke(color=SUCCESS, width=4.0),
            c2[0].animate.set_stroke(color=RISK, width=4.0),
            c3[0].animate.set_stroke(color=SUCCESS, width=4.0),
            run_time=0.57
        )
        self.play(
            c1[0].animate.set_stroke(color=SUCCESS, width=2.5),
            c2[0].animate.set_stroke(color=RISK, width=2.5),
            c3[0].animate.set_stroke(color=SUCCESS, width=2.5),
            run_time=0.57
        )
