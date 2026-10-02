"""
EP05 Scene 09: The NBBO Benchmark (03:53.48 - 04:23.00, TARGET: EXACTLY 29.52s)
Side-by-side terminal execution comparison: Public NBBO ($150.00) vs Internalized PFOF ($150.02),
highlighting the $2 lost price improvement delta and regulatory audit citations.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene09NbboBenchmark(Scene):
    def construct(self):
        TARGET_DURATION = 29.52

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Section Header
        hdr = CleanText("THE LEGAL STANDARD // BEST EXECUTION", font_size=16, color=TEXT)
        hdr.shift(UP * 2.4)
        sub = CleanText("NBBO BENCHMARK vs INTERNALIZED FILL", font_size=28, color=TEXT, weight="BOLD")
        sub.next_to(hdr, DOWN, buff=0.15)

        # 3. Side-by-Side Comparison Columns
        nbbo_col = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.3, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.96).shift(LEFT * 3.2 + DOWN * 0.1)
        n_head = CleanText("PUBLIC NBBO (TRUE BEST)", font_size=16, color=SUCCESS, weight="BOLD").move_to(nbbo_col.get_top() + DOWN * 0.35)
        n_desc = CleanText("National Best Bid & Offer", font_size=12, color=TEXT, fill_opacity=0.60).next_to(n_head, DOWN, buff=0.1)
        n_share = CleanText("100 SHARES @ $150.00", font_size=17, color=TEXT).next_to(n_desc, DOWN, buff=0.22)
        n_total = CleanText("$15,000.00", font_size=26, color=SUCCESS, weight="BOLD").next_to(n_share, DOWN, buff=0.18)
        n_status = CleanText("✓ Best Available Market Price", font_size=12, color=SUCCESS).next_to(n_total, DOWN, buff=0.2)
        nbbo_grp = VGroup(nbbo_col, n_head, n_desc, n_share, n_total, n_status)

        pfof_col = RoundedRectangle(corner_radius=0.2, width=4.6, height=3.3, stroke_color=RISK, stroke_width=2.5, fill_color="#1E1410", fill_opacity=0.96).shift(RIGHT * 3.2 + DOWN * 0.1)
        p_head = CleanText("INTERNALIZED (PFOF)", font_size=16, color=RISK, weight="BOLD").move_to(pfof_col.get_top() + DOWN * 0.35)
        p_desc = CleanText("Wholesaler Execution Fill", font_size=12, color=TEXT, fill_opacity=0.60).next_to(p_head, DOWN, buff=0.1)
        p_share = CleanText("100 SHARES @ $150.02", font_size=17, color=TEXT).next_to(p_desc, DOWN, buff=0.22)
        p_total = CleanText("$15,002.00", font_size=26, color=RISK, weight="BOLD").next_to(p_share, DOWN, buff=0.18)
        p_status = CleanText("✕ Missed Price Improvement", font_size=12, color=RISK).next_to(p_total, DOWN, buff=0.2)
        pfof_grp = VGroup(pfof_col, p_head, p_desc, p_share, p_total, p_status)

        # 4. Center Delta Bracket: -$2.00 Difference
        delta_box = RoundedRectangle(corner_radius=0.15, width=3.4, height=1.1, stroke_color=RISK, stroke_width=2.5, fill_color="#2A1408", fill_opacity=0.98).move_to(DOWN * 0.1)
        d_val = CleanText("-$2.00 DELTA", font_size=22, color=RISK, weight="BOLD").move_to(delta_box.get_top() + DOWN * 0.32)
        d_lbl = CleanText("Per 100 Shares", font_size=12, color=TEXT).next_to(d_val, DOWN, buff=0.08)
        delta_grp = VGroup(delta_box, d_val, d_lbl)

        # 5. Regulatory Citation Stamp
        cit_box = RoundedRectangle(corner_radius=0.15, width=8.2, height=0.75, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#18202A", fill_opacity=0.95).shift(DOWN * 2.3)
        cit_txt = CleanText("AUDIT VERIFIED: SEC RULE 605/606 & FINRA RULE 5310 BEST EXECUTION", font_size=12, color=TEXT, fill_opacity=0.60).move_to(cit_box)
        cit_grp = VGroup(cit_box, cit_txt)

        all_content = VGroup(hdr, sub, nbbo_grp, pfof_grp, delta_grp, cit_grp)
        all_content, s_factor = stage_fit(all_content, max_w=11.2, max_h=3.8)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 29.52s) -----------------
        # Beat 1: Header & Subtitle draw (1.5s) + reading hold (1.5s) = 3.0s
        self.play(FadeIn(hdr), FadeIn(sub), run_time=1.5)
        self.wait(1.5)

        # Beat 2: Public NBBO column enters (2.5s) + inspect hold (1.5s) = 4.0s -> cumulative 7.0s
        self.play(FadeIn(nbbo_grp, shift=RIGHT * 0.3 * s_factor), run_time=2.5)
        self.wait(1.5)

        # Beat 3: Internalized PFOF column enters (2.5s) + inspect hold (1.5s) = 4.0s -> cumulative 11.0s
        self.play(FadeIn(pfof_grp, shift=LEFT * 0.3 * s_factor), run_time=2.5)
        self.wait(1.5)

        # Beat 4: Simulated execution comparison pulse (4.5s) -> cumulative 15.5s
        self.play(
            n_total.animate.scale(1.10),
            p_total.animate.scale(1.10),
            run_time=1.5
        )
        self.play(
            n_total.animate.scale(1.0 / 1.10),
            p_total.animate.scale(1.0 / 1.10),
            run_time=1.5
        )
        self.wait(1.5)

        # Beat 5: Center Delta Callout Box emerges with bracket (4.5s) -> cumulative 20.0s
        self.play(FadeIn(delta_grp, scale=1.2), run_time=2.0)
        self.play(delta_box.animate.set_stroke(color=RISK, width=4.5), run_time=1.2)
        self.play(delta_box.animate.set_stroke(color=RISK, width=2.5), run_time=1.3)

        # Beat 6: Regulatory citation badge stamps down (4.5s) -> cumulative 24.5s
        self.play(FadeIn(cit_box), FadeIn(cit_txt), run_time=2.0)
        self.wait(2.5)

        # Beat 7: Side-by-side verification highlight pulse strictly inside stage (5.02s) -> cumulative 29.52s
        self.play(
            nbbo_col.animate.set_stroke(color=SUCCESS, width=4.5),
            pfof_col.animate.set_stroke(color=RISK, width=4.5),
            run_time=2.51
        )
        self.play(
            nbbo_col.animate.set_stroke(color=SUCCESS, width=2.5),
            pfof_col.animate.set_stroke(color=RISK, width=2.5),
            run_time=2.51
        )
