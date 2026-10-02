"""
EP05 Scene 07: The $65 Million Penalty (02:50.50 - 03:20.16, TARGET: EXACTLY 29.66s)
SEC administrative proceeding finding Robinhood provided inferior execution,
heavy $65,000,000 settlement seal drops with impact, flipping into the hidden customer invoice.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene07Sec65mPenalty(Scene):
    def construct(self):
        TARGET_DURATION = 29.66

        # 1. Background Grid strictly inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Official SEC Enforcement Document Vector
        doc = RoundedRectangle(
            corner_radius=0.15, width=7.8, height=3.8,
            stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.96
        ).move_to(STAGE_CENTER)

        sec_header = CleanText("UNITED STATES OF AMERICA", font_size=15, color=TEXT, weight="BOLD")
        sec_header.move_to(doc.get_top() + DOWN * 0.35)
        sec_agency = CleanText("SECURITIES AND EXCHANGE COMMISSION // ADMIN PROCEEDING", font_size=12, color=TEXT, fill_opacity=0.60)
        sec_agency.next_to(sec_header, DOWN, buff=0.1)
        sec_matter = CleanText("In the Matter of: Robinhood Financial, LLC (File No. 3-20171)", font_size=13, color=TEXT)
        sec_matter.next_to(sec_agency, DOWN, buff=0.15)

        div_line = Line(start=doc.get_left() + RIGHT * 0.4, end=doc.get_right() + LEFT * 0.4, stroke_color=UI_STRUCTURE, stroke_width=1.5)
        div_line.next_to(sec_matter, DOWN, buff=0.18)

        charge_txt1 = CleanText("FINDING: Customers received inferior trade prices due to PFOF routing.", font_size=13, color=TEXT)
        charge_txt1.next_to(div_line, DOWN, buff=0.25)
        charge_txt2 = CleanText("DEFENSE CLAIM OF 'COMMISSION FREE' OMITTED INFERIOR EXECUTION.", font_size=13, color=RISK, weight="BOLD")
        charge_txt2.next_to(charge_txt1, DOWN, buff=0.15)

        doc_group = VGroup(doc, sec_header, sec_agency, sec_matter, div_line, charge_txt1, charge_txt2)

        # 3. Heavy Seal Impact: SETTLED - $65,000,000 PENALTY (strictly contained inside doc)
        seal = Circle(radius=1.1, stroke_color=RISK, stroke_width=3.5, fill_color="#2A1408", fill_opacity=0.95).move_to(doc.get_center() + DOWN * 0.3)
        s_title = CleanText("SEC SETTLED", font_size=13, color=RISK, weight="BOLD").move_to(seal.get_center() + UP * 0.32)
        s_fine = CleanText("$65,000,000", font_size=22, color=TEXT, weight="BOLD").move_to(seal.get_center())
        s_sub = CleanText("PENALTY // 2020", font_size=11, color=RISK).move_to(seal.get_center() + DOWN * 0.32)
        seal_group = VGroup(seal, s_title, s_fine, s_sub)

        part1 = VGroup(doc_group, seal_group)
        part1, s1 = stage_fit(part1, max_w=11.2, max_h=3.8)

        # 4. Flip to Revealed Customer Invoice
        invoice_card = RoundedRectangle(
            corner_radius=0.2, width=7.4, height=3.7,
            stroke_color=RISK, stroke_width=2.5, fill_color="#1A1412", fill_opacity=0.96
        ).move_to(STAGE_CENTER)

        inv_head = CleanText("RETAIL INVESTOR INVOICE // UNNOTICED", font_size=16, color=RISK, weight="BOLD")
        inv_head.move_to(invoice_card.get_top() + DOWN * 0.4)

        inv_l1 = CleanText("BILLED TO:  Every Retail Account Using Market Orders", font_size=14, color=TEXT).next_to(inv_head, DOWN, buff=0.3)
        inv_l2 = CleanText("SERVICE:    'Free' Zero-Commission Execution", font_size=14, color=TEXT, fill_opacity=0.60).next_to(inv_l1, DOWN, buff=0.18)
        inv_l3 = CleanText("ACTUAL BILL: Inferior Execution Spread vs Best NBBO Price", font_size=14, color=RISK, weight="BOLD").next_to(inv_l2, DOWN, buff=0.18)
        inv_l4 = CleanText("COLLECTION: Silently deducted from your fill price", font_size=12, color=TEXT).next_to(inv_l3, DOWN, buff=0.18)

        calc_box = RoundedRectangle(corner_radius=0.1, width=6.5, height=0.6, stroke_color=RISK, stroke_width=1.5, fill_color="#2A160E", fill_opacity=0.9).next_to(inv_l4, DOWN, buff=0.18)
        calc_txt = CleanText("TRUE NBBO: $100.00  →  YOUR FILL: $100.02 (+$0.02 TAX)", font_size=12, color=RISK, weight="BOLD").move_to(calc_box)

        inv_group = VGroup(invoice_card, inv_head, inv_l1, inv_l2, inv_l3, inv_l4, calc_box, calc_txt)
        inv_group, s2 = stage_fit(inv_group, max_w=11.2, max_h=3.8)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 29.66s) -----------------
        # Beat 1: SEC Legal Document draws on screen (2.0s) + inspection (2.0s) = 4.0s
        self.play(FadeIn(doc_group), run_time=2.0)
        self.wait(2.0)

        # Beat 2: SEC Findings text highlights line by line (3.5s) -> cumulative 7.5s
        self.play(
            charge_txt1.animate.set_color(SUCCESS),
            charge_txt2.animate.scale(1.05),
            run_time=2.0
        )
        self.wait(1.5)

        # Beat 3: $65,000,000 Penalty Seal slams down with impact punch (4.5s) -> cumulative 12.0s
        self.play(FadeIn(seal_group, scale=1.4), run_time=1.5)
        self.play(seal_group.animate.scale(1.08), run_time=1.0)
        self.play(seal_group.animate.scale(1.0 / 1.08), run_time=1.0)
        self.wait(1.0)

        # Beat 4: Transition to Retail Customer Invoice (2.5s) -> cumulative 14.5s
        self.play(FadeOut(doc_group, seal_group), run_time=1.2)
        self.play(FadeIn(invoice_card), FadeIn(inv_head), run_time=1.3)

        # Beat 5: Invoice items illuminate line by line (5.5s) -> cumulative 20.0s
        self.play(FadeIn(inv_l1), run_time=1.3)
        self.play(FadeIn(inv_l2), run_time=1.3)
        self.play(FadeIn(inv_l3), run_time=1.4)
        self.play(FadeIn(inv_l4), run_time=1.5)

        # Beat 6: Running hidden tax calculation box reveals (5.0s) -> cumulative 25.0s
        self.play(FadeIn(calc_box), FadeIn(calc_txt), run_time=2.0)
        self.wait(3.0)

        # Beat 7: Final highlight pulse to exact duration (4.66s) -> cumulative 29.66s
        self.play(
            invoice_card.animate.set_stroke(color=RISK, width=4.5),
            calc_box.animate.set_stroke(color=RISK, width=2.5),
            run_time=2.33
        )
        self.play(
            invoice_card.animate.set_stroke(color=RISK, width=2.5),
            calc_box.animate.set_stroke(color=RISK, width=1.5),
            run_time=2.33
        )
