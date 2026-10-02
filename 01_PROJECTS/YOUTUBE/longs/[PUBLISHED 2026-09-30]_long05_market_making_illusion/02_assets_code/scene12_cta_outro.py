"""
EP05 Scene 12: CTA & Outro End-Screen (05:20.50 - 05:37.12, TARGET: EXACTLY 16.62s)
Official Quantrove brandmark, designated clear zones for YouTube interactive cards,
and bottom teaser banner for Episode 06 with microsecond telemetry wave.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene12CtaOutro(Scene):
    def construct(self):
        TARGET_DURATION = 16.62

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Quantrove Official Brand Wordmark & Channel Header
        brand = CleanText("QUANTROVE", font_size=38, color=TEXT, weight="BOLD")
        brand.shift(UP * 2.5)
        tagline = CleanText("INSTITUTIONAL DATA INTELLIGENCE // AI & FINANCE", font_size=15, color=TEXT, fill_opacity=0.60)
        tagline.next_to(brand, DOWN, buff=0.15)

        # 3. Designated Interactive YouTube End-Screen Zones
        video_zone = RoundedRectangle(
            corner_radius=0.2, width=5.4, height=3.0,
            stroke_color=UI_STRUCTURE, stroke_width=2, stroke_opacity=0.6, fill_color="#141E22", fill_opacity=0.3
        ).shift(LEFT * 3.8 + DOWN * 0.1)
        vz_lbl = CleanText("NEXT EPISODE // RECOMMENDED", font_size=13, color=TEXT, fill_opacity=0.60).move_to(video_zone.get_center())

        sub_zone = Circle(
            radius=1.2, stroke_color=SUCCESS, stroke_width=2, stroke_opacity=0.8, fill_color="#182A1C", fill_opacity=0.3
        ).shift(RIGHT * 3.8 + DOWN * 0.1)
        sz_lbl = CleanText("SUBSCRIBE", font_size=14, color=SUCCESS, weight="BOLD").move_to(sub_zone.get_center())

        # 4. Episode 06 Teaser Banner
        teaser_box = RoundedRectangle(
            corner_radius=0.15, width=9.2, height=0.9,
            stroke_color=SUCCESS, stroke_width=2, fill_color="#161B22", fill_opacity=0.96
        ).shift(DOWN * 2.3)

        t_lbl = CleanText("NEXT: EPISODE 06 // HFT MICROSECOND MATH & MACHINE LEARNING", font_size=15, color=SUCCESS, weight="BOLD")
        t_lbl.move_to(teaser_box)

        all_content = VGroup(brand, tagline, video_zone, vz_lbl, sub_zone, sz_lbl, teaser_box, t_lbl)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 16.62s) -----------------
        # Beat 1: Brand & Tagline appear (2.0s) + hold (1.0s) = 3.0s
        self.play(FadeIn(brand, shift=DOWN * 0.3 * s_factor), FadeIn(tagline, shift=DOWN * 0.2 * s_factor), run_time=2.0)
        self.wait(1.0)

        # Beat 2: End-screen zones illuminate (2.5s) + subscribe zone pulse (2.0s) = 4.5s -> cumulative 7.5s
        self.play(FadeIn(video_zone), FadeIn(vz_lbl), FadeIn(sub_zone), FadeIn(sz_lbl), run_time=2.5)
        self.play(sub_zone.animate.scale(1.10), sz_lbl.animate.scale(1.10), run_time=1.0)
        self.play(sub_zone.animate.scale(1.0 / 1.10), sz_lbl.animate.scale(1.0 / 1.10), run_time=1.0)

        # Beat 3: Episode 06 Teaser Box enters (3.0s) + banner pulse (3.0s) = 6.0s -> cumulative 13.5s
        self.play(FadeIn(teaser_box, shift=UP * 0.2 * s_factor), FadeIn(t_lbl), run_time=3.0)
        self.play(teaser_box.animate.set_stroke(color=SUCCESS, width=4.0), run_time=1.5)
        self.play(teaser_box.animate.set_stroke(color=SUCCESS, width=2.0), run_time=1.5)

        # Beat 4: Final highlight pulse on brandmark to exact duration (3.12s) -> cumulative 16.62s
        self.play(
            brand.animate.set_color(SUCCESS),
            run_time=1.56
        )
        self.play(
            brand.animate.set_color(TEXT),
            run_time=1.56
        )
