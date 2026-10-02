"""
Quantrove EP06 Short S06-05: One Microsecond Is 200 Meters
Format: 9:16 Vertical (1080x1920 @ 60fps)
Duration: ~32.0s (within 30-45s)
Visual Language: Institutional Data Intelligence
"""
from manim import *
import os, sys

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60
config.background_color = "#202322"

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT

class OneMicrosecondIs200Meters(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # BEAT 1: [0.0s - 5.0s] IDEA: Light travels 200m in 1 microsecond
        title = CleanText("THE SPEED OF LIGHT LIMIT", font_size=18, color=TEXT, weight="BOLD").move_to(UP * 6.5)
        sub = CleanText("PHYSICS OF LATENCY ARBITRAGE", font_size=13, color=SUCCESS).next_to(title, DOWN, buff=0.15)
        head_group = VGroup(title, sub)

        stat_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=3.0, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 3.6)
        s_val = CleanText("1 µs = 200 METERS", font_size=24, color=SUCCESS, weight="BOLD").move_to(stat_card.get_center() + UP * 0.3)
        s_sub = CleanText("SPEED OF LIGHT IN GLASS FIBER", font_size=12, color=TEXT).next_to(s_val, DOWN, buff=0.25)

        pulse_line = Line(start=LEFT * 3.0, end=RIGHT * 3.0, color=UI_STRUCTURE, stroke_width=3).move_to(UP * 1.5)
        pulse_dot = Dot(color=SUCCESS, radius=0.15).move_to(pulse_line.get_start())

        self.play(FadeIn(head_group, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(stat_card), run_time=0.7)
        self.play(FadeIn(s_val, scale=1.1), FadeIn(s_sub), run_time=1.0)
        self.play(Create(pulse_line), run_time=0.8)
        self.play(pulse_dot.animate.move_to(pulse_line.get_end()), run_time=1.5)

        # BEAT 2: [5.0s - 13.0s] SIMPLE_WRONG: Microsecond vs blink (Dynamic time bars)
        blink_card = RoundedRectangle(corner_radius=0.2, width=7.2, height=3.4, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(UP * -0.5)
        b_title = CleanText("HUMAN PERCEPTION SCALE", font_size=14, color=TEXT, weight="BOLD").move_to(blink_card.get_top() + DOWN * 0.4)

        b1 = CleanText("Human Eye Blink:", font_size=13, color=TEXT).move_to(blink_card.get_center() + UP * 0.5 + LEFT * 1.5)
        b1_val = CleanText("~350,000 µs", font_size=16, color=RISK, weight="BOLD").next_to(b1, RIGHT, buff=0.3)
        bar_blink = Rectangle(width=0.2, height=0.2, color=RISK, fill_color=RISK, fill_opacity=0.9).next_to(b1, DOWN, buff=0.15).align_to(b1, LEFT)

        b2 = CleanText("HFT Decision Window:", font_size=13, color=TEXT).move_to(blink_card.get_center() + DOWN * 0.6 + LEFT * 1.5)
        b2_val = CleanText("~1 µs", font_size=16, color=SUCCESS, weight="BOLD").next_to(b2, RIGHT, buff=0.3)
        bar_hft = Rectangle(width=0.08, height=0.2, color=SUCCESS, fill_color=SUCCESS, fill_opacity=0.9).next_to(b2, DOWN, buff=0.15).align_to(b2, LEFT)

        self.play(FadeIn(blink_card), FadeIn(b_title), run_time=0.7)
        self.play(FadeIn(b1), FadeIn(b1_val, shift=LEFT * 0.2), run_time=0.8)
        self.play(bar_blink.animate.stretch_to_fit_width(5.2), run_time=1.8)
        self.play(FadeIn(b2), FadeIn(b2_val, shift=LEFT * 0.2), run_time=0.8)
        self.play(bar_hft.animate.stretch_to_fit_width(0.1), run_time=0.8)
        self.play(b2_val.animate.scale(1.2), run_time=0.8)
        self.play(bar_blink.animate.set_stroke(RISK, width=3), run_time=0.8)
        self.wait(0.6)

        # BEAT 3: [13.0s - 23.5s] COMPLEX_WRONG: Vacuum vs fiber race
        stat_group = VGroup(stat_card, s_val, s_sub, pulse_line, pulse_dot)
        blink_group = VGroup(blink_card, b_title, b1, b1_val, bar_blink, b2, b2_val, bar_hft)
        self.play(FadeOut(stat_group), FadeOut(blink_group), run_time=0.8)

        phys_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=4.2, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 3.0)
        p_title = CleanText("OPTICAL REFRACTION SLOWDOWN", font_size=15, color=TEXT, weight="BOLD").move_to(phys_card.get_top() + DOWN * 0.45)
        row1 = CleanText("VACUUM: ~300 m / µs", font_size=14, color=TEXT).move_to(phys_card.get_center() + UP * 0.6)
        row2 = CleanText("GLASS FIBER: ~200 m / µs", font_size=15, color=RISK, weight="BOLD").next_to(row1, DOWN, buff=0.3)
        row3 = CleanText("Refractive index n ≈ 1.5 slows light by 33%", font_size=11, color=TEXT, fill_opacity=0.7).next_to(row2, DOWN, buff=0.25)

        line_v = Line(start=LEFT * 2.8, end=RIGHT * 2.8, color=TEXT, stroke_width=2.5).move_to(UP * 0.0)
        line_g = Line(start=LEFT * 2.8, end=RIGHT * 2.8, color=RISK, stroke_width=2.5).move_to(DOWN * 0.6)
        dot_v = Dot(color=SUCCESS, radius=0.12).move_to(line_v.get_start())
        dot_g = Dot(color=RISK, radius=0.12).move_to(line_g.get_start())

        self.play(FadeIn(phys_card), FadeIn(p_title), run_time=0.9)
        self.play(FadeIn(row1, shift=RIGHT * 0.2), Create(line_v), run_time=1.0)
        self.play(FadeIn(row2, shift=RIGHT * 0.2), Create(line_g), run_time=1.0)
        self.play(FadeIn(row3), run_time=0.8)
        self.play(
            dot_v.animate.move_to(line_v.get_end()),
            dot_g.animate.move_to(line_g.get_start() + RIGHT * 3.7),
            run_time=2.2
        )
        self.play(row2.animate.scale(1.08), run_time=1.0)
        self.play(dot_g.animate.scale(1.2), run_time=1.0)
        self.wait(1.0)

        # BEAT 4: [23.5s - 34.0s] INSIGHT
        phys_group = VGroup(phys_card, p_title, row1, row2, row3, line_v, line_g, dot_v, dot_g)
        self.play(FadeOut(phys_group), run_time=0.8)

        race_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=4.0, stroke_color=SUCCESS, stroke_width=3, fill_color="#181C24", fill_opacity=0.96).move_to(UP * 2.8)
        rc_title = CleanText("PHYSICAL DISTANCE = TIME DELAY", font_size=15, color=SUCCESS, weight="BOLD").move_to(race_card.get_top() + DOWN * 0.45)
        m_a = CleanText("MACHINE A: 0m  ➔ Quote at t = 0 µs", font_size=12, color=SUCCESS, weight="BOLD").move_to(race_card.get_center() + UP * 0.3)
        m_b = CleanText("MACHINE B: 200m ➔ Quote at t = 1 µs", font_size=12, color=RISK, weight="BOLD").next_to(m_a, DOWN, buff=0.3)
        rc_concl = CleanText("Machine A cancels or takes the quote first.", font_size=12, color=TEXT).next_to(m_b, DOWN, buff=0.3)

        badge_box = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.2, stroke_color=SUCCESS, stroke_width=3, fill_color="#181C24", fill_opacity=0.98).move_to(DOWN * 1.5)
        badge_txt = CleanText("SPEED OF LIGHT", font_size=17, color=SUCCESS, weight="BOLD").move_to(badge_box)
        badge_group = VGroup(badge_box, badge_txt)

        self.play(FadeIn(race_card), FadeIn(rc_title), run_time=0.9)
        self.play(FadeIn(m_a, shift=RIGHT * 0.2), FadeIn(m_b, shift=LEFT * 0.2), run_time=1.2)
        self.play(FadeIn(rc_concl), run_time=1.0)
        self.play(FadeIn(badge_group, shift=UP * 0.3), run_time=1.1)
        self.play(badge_box.animate.set_stroke(SUCCESS, width=4.5), run_time=1.0)
        self.play(badge_txt.animate.scale(1.08), run_time=1.0)
        self.wait(1.5)
