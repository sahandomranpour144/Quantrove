"""
EP05 Scene 08: The Real Cost to You (03:20.16 - 03:53.48, TARGET: EXACTLY 33.32s)
A single trade's -$2.00 sliver pulls back into a 500-trade lifetime grid,
cascading into Pumpkin orange and totaling over -$1,000 in compounding losses.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene08RealCostToYou(Scene):
    def construct(self):
        TARGET_DURATION = 33.32

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Single Trade Tile: -$2.00 on 100 Shares
        single_card = RoundedRectangle(
            corner_radius=0.25, width=6.0, height=3.2,
            stroke_color=RISK, stroke_width=2.5, fill_color="#181310", fill_opacity=0.96
        ).move_to(STAGE_CENTER)

        sc_title = CleanText("A SINGLE 100-SHARE TRADE", font_size=18, color=TEXT, weight="BOLD")
        sc_title.move_to(single_card.get_top() + DOWN * 0.4)

        sc_calc1 = CleanText("SPREAD SLIPPAGE: 2 CENTS / SHARE", font_size=14, color=TEXT, fill_opacity=0.60)
        sc_calc1.next_to(sc_title, DOWN, buff=0.22)

        sc_val = CleanText("-$2.00 PER ORDER", font_size=34, color=RISK, weight="BOLD")
        sc_val.next_to(sc_calc1, DOWN, buff=0.22)

        sc_sub = CleanText("Feels trivial. Barely noticed on one trade.", font_size=13, color=TEXT)
        sc_sub.next_to(sc_val, DOWN, buff=0.22)

        single_group = VGroup(single_card, sc_title, sc_calc1, sc_val, sc_sub)
        single_group, s1 = stage_fit(single_group, max_w=11.2, max_h=3.8)

        # 3. 500-Trade Lifetime Grid Matrix
        grid_title = CleanText("THE COMPOUNDING MATH // 500 LIFETIME TRADES", font_size=17, color=RISK, weight="BOLD")
        grid_title.shift(UP * 1.8)

        tiles = VGroup()
        rows, cols = 7, 16
        for r in range(rows):
            for c in range(cols):
                sq = Rectangle(
                    width=0.40, height=0.26,
                    stroke_color=UI_STRUCTURE, stroke_width=1, fill_color="#1E232B", fill_opacity=0.8
                )
                x = (c - cols / 2 + 0.5) * 0.48
                y = (r - rows / 2 + 0.5) * 0.32 + 0.1
                sq.move_to(np.array([x, y, 0]))
                tiles.add(sq)

        summary_box = RoundedRectangle(
            corner_radius=0.15, width=8.0, height=1.1,
            stroke_color=RISK, stroke_width=2.5, fill_color="#20120A", fill_opacity=0.96
        ).shift(DOWN * 1.6)

        sum_val = CleanText("-$1,000.00+ CUMULATIVE SPREAD DRAG", font_size=22, color=RISK, weight="BOLD")
        sum_val.move_to(summary_box.get_top() + DOWN * 0.35)

        sum_sub = CleanText("2 trades per week = hundreds siphoned out of your portfolio silently", font_size=12, color=TEXT)
        sum_sub.next_to(sum_val, DOWN, buff=0.1)

        sum_grp = VGroup(summary_box, sum_val, sum_sub)

        # Fit tightly inside stage bounds with ample margin
        part2 = VGroup(grid_title, tiles, sum_grp)
        part2, s2 = stage_fit(part2, max_w=11.0, max_h=3.8)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 33.32s) -----------------
        # Beat 1: Single Trade Tile appears in macro focus (2.0s) + inspection (2.0s) = 4.0s
        self.play(FadeIn(single_group, scale=0.85), run_time=2.0)
        self.wait(2.0)

        # Beat 2: Slippage drag callout pulse (3.0s) -> cumulative 7.0s
        self.play(sc_val.animate.scale(1.10), single_card.animate.set_stroke(color=RISK, width=4.0), run_time=1.5)
        self.play(sc_val.animate.scale(1.0 / 1.10), single_card.animate.set_stroke(color=RISK, width=2.5), run_time=1.5)

        # Beat 3: Pull back transition from single card to grid view (2.5s + 2.0s hold) = 4.5s -> cumulative 11.5s
        self.play(FadeOut(single_group), run_time=1.2)
        freq_card = RoundedRectangle(corner_radius=0.15, width=6.2, height=1.1, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#141E22", fill_opacity=0.95).shift(UP * 0.1)
        freq_txt = CleanText("2 TRADES / WEEK = 104 TRADES / YEAR", font_size=17, color=SUCCESS, weight="BOLD").move_to(freq_card)
        self.play(FadeIn(freq_card), FadeIn(freq_txt), run_time=1.3)
        self.wait(2.0)

        # Beat 4: Transition to 500-Trade Matrix Grid (4.0s) -> cumulative 15.5s
        self.play(FadeOut(freq_card, freq_txt), FadeIn(grid_title), run_time=1.5)
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.008), run_time=2.5)

        # Beat 5: Domino cascade: all 500 cells illuminate turning Pumpkin #FD802E (6.5s) -> cumulative 22.0s
        self.play(
            LaggedStart(*[t.animate.set_fill(color=RISK, opacity=0.95).set_stroke(color=RISK, width=1.5) for t in tiles], lag_ratio=0.012),
            run_time=6.5
        )

        # Beat 6: Cumulative spread drag summary card materializes (3.5s) -> cumulative 25.5s
        self.play(FadeIn(sum_grp, scale=0.95), run_time=1.5)
        self.wait(2.0)

        # Beat 7: Shaded loss drag delta pulse (4.5s) -> cumulative 30.0s
        self.play(
            sum_val.animate.scale(1.08),
            summary_box.animate.set_stroke(color=RISK, width=4.0),
            run_time=2.25
        )
        self.play(
            sum_val.animate.scale(1.0 / 1.08),
            summary_box.animate.set_stroke(color=RISK, width=2.5),
            run_time=2.25
        )

        # Beat 8: Final highlight pulse to exact duration (3.32s) -> cumulative 33.32s
        self.play(
            summary_box.animate.set_fill(color="#2D160C"),
            grid_title.animate.set_color(TEXT),
            run_time=1.66
        )
        self.play(
            summary_box.animate.set_fill(color="#20120A"),
            grid_title.animate.set_color(RISK),
            run_time=1.66
        )
