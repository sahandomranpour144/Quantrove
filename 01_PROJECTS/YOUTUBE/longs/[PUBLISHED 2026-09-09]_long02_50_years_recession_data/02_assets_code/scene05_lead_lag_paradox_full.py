"""
Continuous Manim Animation: ep02_scene05_lead_lag_paradox.py
Covers the entire Scene 5 narration passage (73.16 seconds):
Phase 1: Abstract / General Lead-Lag Pattern with 3-5 Months Lead Time Bracket
Phase 2: Real 2008-2010 S&P 500 Case Study (March 9, 2009 Bottom & +68% 12-Month Surge)
"""

from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class LeadLagParadoxFullScene(Scene):
    def construct(self):
        # Color Palette - Quantrove Dark Institutional Standard
        BG_COLOR = "#0B0E14"
        CYAN = "#06B6D4"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        RED = "#EF4444"
        WHITE = "#F8FAFC"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"
        REC_GRAY = "#334155"

        # =========================================================================
        # SECTION 1: HEADER & PHASE 1 SETUP (0.0s - 13.0s) [13.0s]
        # =========================================================================
        title = Text("PATTERN #1: THE LEAD-LAG PARADOX", font="Segoe UI", font_size=32, weight=BOLD, color=CYAN)
        phase_sub = Text("PHASE 1: THE HISTORICAL PATTERN (AVERAGE CYCLE)", font="Segoe UI", font_size=16, weight=BOLD, color=MUTED)
        header = VGroup(title, phase_sub).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)

        self.play(FadeIn(header, shift=DOWN), run_time=2.0)
        self.wait(2.0)

        # Axes for Phase 1
        # X: Months relative to recession end (-16 to +10, 0 = Official End)
        # Y: Normalized Price (40 to 140)
        axes1 = Axes(
            x_range=[-16, 12, 2],
            y_range=[40, 140, 20],
            x_length=11.2,
            y_length=4.6,
            axis_config={"color": MUTED, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.45)

        x_lbl1 = Text("Months Relative to Official Recession End (Month 0 = Economic Recovery)", font="Segoe UI", font_size=13, color=MUTED).next_to(axes1, DOWN, buff=0.25)
        y_lbl1 = Text("S&P 500 Normalized Level", font="Segoe UI", font_size=13, color=MUTED).next_to(axes1, LEFT, buff=0.25).rotate(PI/2)

        # Shaded Recession Window: from -12 to 0 (12-Month Average Recession)
        p1_start = axes1.c2p(-12, 40)
        p1_end = axes1.c2p(0, 140)
        rec_width1 = p1_end[0] - p1_start[0]
        rec_height1 = p1_end[1] - p1_start[1]
        rec_band1 = Rectangle(
            width=rec_width1, height=rec_height1,
            fill_color=REC_GRAY, fill_opacity=0.45,
            stroke_color=PANEL_BORDER, stroke_width=1.5
        ).move_to([(p1_start[0] + p1_end[0])/2, (p1_start[1] + p1_end[1])/2, 0])

        rec_label1 = Text("OFFICIAL RECESSION (12 Months)", font="Segoe UI", font_size=13, weight=BOLD, color=WHITE).next_to(rec_band1.get_top(), DOWN, buff=0.2)
        rec_end_line1 = DashedLine(axes1.c2p(0, 40), axes1.c2p(0, 140), color=GOLD, stroke_width=2.5, dash_length=0.1)
        rec_end_tag1 = Text("Month 0: Recession Ends", font="Segoe UI", font_size=12, weight=BOLD, color=GOLD).next_to(axes1.c2p(0, 140), UP, buff=0.1)

        phase1_setup = VGroup(axes1, x_lbl1, y_lbl1, rec_band1, rec_label1, rec_end_line1, rec_end_tag1)
        self.play(FadeIn(phase1_setup), run_time=3.0)
        self.wait(6.0)

        # =========================================================================
        # SECTION 2: S&P 500 LEADING DECLINE & EARLY PEAK (13.0s - 34.0s) [21.0s]
        # =========================================================================
        # S&P 500 curve:
        # Peaks at t = -14 (before recession starts at -12)
        # Troughs at t = -4 (4 months before recession ends)
        # Surges through t = 0 to t = 10
        def p1_curve_down(t):
            # from -16 to -4
            if t <= -14:
                return 110 + (t + 16) * 5.0  # rises from 110 to 120
            elif t <= -12:
                return 120 - 4.0 * (t + 14)**1.5 # starts turning down before -12
            else:
                # plunges to 60 at t = -4
                prog = (t + 12) / 8.0 # 0 at -12, 1 at -4
                return 112 - 52.0 * np.sin(prog * (PI / 2))

        curve_p1_down = axes1.plot(p1_curve_down, x_range=[-16, -4], color=CYAN, stroke_width=3.8)

        # Peak indicator at t = -14
        pt_peak1 = axes1.c2p(-14, 120)
        dot_peak1 = Dot(pt_peak1, color=GOLD, radius=0.12)
        lbl_peak1 = Text("Market Peaks Early\n(2 Months Before Recession)", font="Segoe UI", font_size=12, weight=BOLD, color=GOLD, line_spacing=1.2).next_to(dot_peak1, UP, buff=0.25)
        arrow_peak1 = Arrow(lbl_peak1.get_bottom(), dot_peak1.get_top(), buff=0.08, stroke_width=2, color=GOLD, max_tip_length_to_length_ratio=0.3)

        # Animate descent down to lowest point
        self.play(Create(curve_p1_down), run_time=8.0)
        self.play(FadeIn(dot_peak1), FadeIn(lbl_peak1), FadeIn(arrow_peak1), run_time=2.0)
        self.wait(11.0)

        # =========================================================================
        # SECTION 3: GENERATIONAL BOTTOM & 3-5 MONTH LEAD TIME (34.0s - 45.0s) [11.0s]
        # =========================================================================
        # Lowest node at Month -4
        pt_bot1 = axes1.c2p(-4, 60)
        dot_bot1 = Dot(pt_bot1, color=GREEN, radius=0.16)
        pulse_ring1 = Circle(radius=0.35, color=GREEN, stroke_width=3).move_to(pt_bot1)
        
        lbl_bot1_txt = Text("MARKET BOTTOMS HERE\n(Inside the Recession)", font="Segoe UI", font_size=12, weight=BOLD, color=GREEN, line_spacing=1.1)
        lbl_bot1_box = SurroundingRectangle(lbl_bot1_txt, color=GREEN, fill_color=PANEL_BG, fill_opacity=0.92, corner_radius=0.08, buff=0.12)
        lbl_bot1 = VGroup(lbl_bot1_box, lbl_bot1_txt).next_to(dot_bot1, UP, buff=0.35)

        # Upward surge curve from -4 to 10
        def p1_curve_up(t):
            # rises from 60 at -4 to 115 at 10
            return 60 + 55.0 * ((t + 4) / 14.0)**0.85

        curve_p1_up = axes1.plot(p1_curve_up, x_range=[-4, 10], color=GREEN, stroke_width=4.0)

        # Bracket showing 3-5 months lead time
        # Between Month -4 and Month 0 at y = 44
        b_left = axes1.c2p(-4, 44)
        b_right = axes1.c2p(0, 44)
        bracket_line = DoubleArrow(b_left, b_right, buff=0, color=GOLD, stroke_width=3, tip_length=0.18)
        bracket_lbl = Text("Average Lead Time: 3–5 Months Before Recovery", font="Segoe UI", font_size=12, weight=BOLD, color=GOLD).next_to(bracket_line, DOWN, buff=0.12)
        bracket_box = SurroundingRectangle(bracket_lbl, color=PANEL_BORDER, fill_color=PANEL_BG, fill_opacity=0.92, corner_radius=0.08, buff=0.1)
        bracket_group = VGroup(bracket_line, bracket_box, bracket_lbl)

        self.play(
            FadeIn(dot_bot1), Create(pulse_ring1), FadeIn(lbl_bot1),
            Create(curve_p1_up),
            run_time=4.5
        )
        self.play(
            pulse_ring1.animate.scale(2.0).set_stroke_opacity(0),
            FadeIn(bracket_group, shift=UP),
            run_time=2.0
        )
        self.wait(4.5)

        # =========================================================================
        # SECTION 4: TRANSITION TO PHASE 2 (REAL 2008-2010 CASE STUDY) (45.0s - 59.0s) [14.0s]
        # =========================================================================
        # Fade out Phase 1 elements
        phase1_elements = VGroup(
            axes1, x_lbl1, y_lbl1, rec_band1, rec_label1, rec_end_line1, rec_end_tag1,
            curve_p1_down, curve_p1_up, dot_peak1, lbl_peak1, arrow_peak1,
            dot_bot1, lbl_bot1, bracket_group
        )

        phase2_sub = Text("PHASE 2: REAL CASE STUDY — 2008–2009 GREAT RECESSION", font="Segoe UI", font_size=16, weight=BOLD, color=GOLD)
        phase2_sub.move_to(phase_sub.get_center())

        # Phase 2 Real Data Setup
        # Months from Oct 2007 (Month 0) to March 2010 (Month 29)
        # 0: Oct 2007 (Peak: 1,565)
        # 2: Dec 2007 (Recession Begins)
        # 11: Sept 2008 (Lehman Brothers: 1,215)
        # 17: March 9, 2009 (Bottom: 676)
        # 20: June 2009 (Recession Officially Ends)
        # 29: March 2010 (12M Rally: 1,140)
        axes2 = Axes(
            x_range=[0, 30, 3],
            y_range=[500, 1700, 200],
            x_length=11.2,
            y_length=4.6,
            axis_config={"color": MUTED, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.45)

        x_lbl2 = Text("Timeline: Oct 2007 ➔ Dec 2007 (Start) ➔ Mar 9, 2009 (Bottom) ➔ Jun 2009 (End) ➔ Mar 2010", font="Segoe UI", font_size=13, color=MUTED).next_to(axes2, DOWN, buff=0.25)
        y_lbl2 = Text("S&P 500 Index (Real Level)", font="Segoe UI", font_size=13, color=MUTED).next_to(axes2, LEFT, buff=0.25).rotate(PI/2)

        # Real Great Recession Shading: Dec 2007 (x=2) to June 2009 (x=20) (18 Months)
        p2_start = axes2.c2p(2, 500)
        p2_end = axes2.c2p(20, 1700)
        rec_width2 = p2_end[0] - p2_start[0]
        rec_height2 = p2_end[1] - p2_start[1]
        rec_band2 = Rectangle(
            width=rec_width2, height=rec_height2,
            fill_color=REC_GRAY, fill_opacity=0.45,
            stroke_color=PANEL_BORDER, stroke_width=1.5
        ).move_to([(p2_start[0] + p2_end[0])/2, (p2_start[1] + p2_end[1])/2, 0])

        rec_label2 = Text("GREAT RECESSION (Dec 2007 – June 2009)", font="Segoe UI", font_size=13, weight=BOLD, color=WHITE).next_to(rec_band2.get_top(), DOWN, buff=0.2)
        rec_end_line2 = DashedLine(axes2.c2p(20, 500), axes2.c2p(20, 1700), color=GOLD, stroke_width=2.5, dash_length=0.1)
        rec_end_tag2 = Text("June 2009: Recession Ends", font="Segoe UI", font_size=11, weight=BOLD, color=GOLD).next_to(axes2.c2p(20, 1700), UP, buff=0.15).shift(LEFT * 1.5)

        phase2_setup = VGroup(axes2, x_lbl2, y_lbl2, rec_band2, rec_label2, rec_end_line2, rec_end_tag2)

        self.play(
            FadeOut(phase1_elements),
            Transform(phase_sub, phase2_sub),
            FadeIn(phase2_setup),
            run_time=2.5
        )

        # Real S&P 500 crash curve: Oct 2007 (1565) -> Mar 2009 (676)
        x_crash = np.array([0, 2, 5, 8, 11, 13, 15, 17], dtype=float)
        y_crash = np.array([1565, 1470, 1330, 1280, 1215, 890, 825, 676], dtype=float)
        pts_crash = [axes2.c2p(x, y) for x, y in zip(x_crash, y_crash)]
        curve_real_crash = VMobject(color=CYAN, stroke_width=3.8).set_points_smoothly(pts_crash)

        # March 9, 2009 Bottom Indicator
        pt_bottom_2009 = axes2.c2p(17, 676)
        dot_2009 = Dot(pt_bottom_2009, color=GREEN, radius=0.18)
        ring_2009 = Circle(radius=0.4, color=GREEN, stroke_width=3.5).move_to(pt_bottom_2009)
        
        lbl_box_2009 = RoundedRectangle(corner_radius=0.1, height=1.1, width=4.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=GREEN, stroke_width=2)
        lbl_txt_2009_a = Text("GENERATIONAL BOTTOM: MARCH 9, 2009", font="Segoe UI", font_size=13, weight=BOLD, color=GREEN)
        lbl_txt_2009_b = Text("S&P 500: 676.53  |  Unemployment at 10%\n3 Full Months BEFORE Recession Ended!", font="Segoe UI", font_size=11, color=WHITE, line_spacing=1.2)
        lbl_group_2009 = VGroup(lbl_txt_2009_a, lbl_txt_2009_b).arrange(DOWN, buff=0.1)
        lbl_box_2009.surround(lbl_group_2009, buff=0.18)
        tag_bottom_2009 = VGroup(lbl_box_2009, lbl_group_2009).next_to(dot_2009, UP + LEFT, buff=0.25)

        self.play(Create(curve_real_crash), run_time=5.5)
        self.play(
            FadeIn(dot_2009), Create(ring_2009), FadeIn(tag_bottom_2009),
            run_time=2.0
        )
        self.wait(4.0)

        # =========================================================================
        # SECTION 5: THE 12-MONTH HISTORIC RALLY (+68% SURGE) (59.0s - 73.16s) [14.16s]
        # =========================================================================
        # Real S&P 500 rally: March 2009 (676) -> March 2010 (1140)
        x_rally = np.array([17, 18.5, 20, 23, 26, 29], dtype=float)
        y_rally = np.array([676, 850, 920, 1040, 1115, 1140], dtype=float)
        pts_rally = [axes2.c2p(x, y) for x, y in zip(x_rally, y_rally)]
        curve_real_rally = VMobject(color=GREEN, stroke_width=4.5).set_points_smoothly(pts_rally)

        # March 2010 Top Target
        pt_target_2010 = axes2.c2p(29, 1140)
        dot_2010 = Dot(pt_target_2010, color=GOLD, radius=0.18)

        # Gain Measurement Bracket / Banner
        gain_arrow = Arrow(axes2.c2p(17, 720), axes2.c2p(29, 1100), color=GOLD, stroke_width=4, buff=0.2)
        gain_card = RoundedRectangle(corner_radius=0.12, height=1.35, width=4.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=GOLD, stroke_width=2.5).shift(RIGHT * 3.85 + UP * 1.35)
        gain_title = Text("12-MONTH SURGE: +68.4%", font="Segoe UI", font_size=16, weight=BOLD, color=GOLD).next_to(gain_card.get_top(), DOWN, buff=0.2)
        gain_desc = Text("676 ➔ 1,140 pts (+464 Index Points)\nRallied while unemployment was at a 26-year high!", font="Segoe UI", font_size=11, color=WHITE, line_spacing=1.2).next_to(gain_title, DOWN, buff=0.12)
        gain_banner = VGroup(gain_card, gain_title, gain_desc)

        # Bottom Takeaway Ribbon (66.0s - 73.16s)
        takeaway_card = RoundedRectangle(corner_radius=0.12, height=0.9, width=12.2, fill_color="#0F172A", fill_opacity=0.95, stroke_color=CYAN, stroke_width=1.5).to_edge(DOWN, buff=0.15)
        takeaway_txt = Text(
            "CORE LESSON: The market bottoms in peak despair. Waiting for the news to report 'safe' misses the biggest gains.",
            font="Segoe UI", font_size=12, weight=BOLD, color=CYAN
        ).move_to(takeaway_card.get_center())
        takeaway_bar = VGroup(takeaway_card, takeaway_txt)

        self.play(
            Create(curve_real_rally),
            ring_2009.animate.scale(2.2).set_stroke_opacity(0),
            run_time=4.5
        )
        self.play(
            FadeIn(dot_2010),
            FadeIn(gain_arrow),
            FadeIn(gain_banner, shift=LEFT),
            FadeOut(x_lbl2),
            FadeIn(takeaway_bar, shift=UP),
            run_time=2.5
        )
        # Final hold to exactly 73.16s
        self.wait(7.16)
