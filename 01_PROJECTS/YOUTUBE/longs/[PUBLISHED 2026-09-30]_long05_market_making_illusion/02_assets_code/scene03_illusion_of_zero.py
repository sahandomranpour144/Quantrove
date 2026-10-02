"""
EP05 Scene 03: The Illusion of Zero (00:38.24 - 01:03.40, TARGET: EXACTLY 25.16s)
1999 $19.95 commission ticket stub dissolves into modern $0.00 app,
Pumpkin magnifying loupe zooms into fine print unscrambling Rule 606 disclosure.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene03IllusionOfZero(Scene):
    def construct(self):
        TARGET_DURATION = 25.16

        # 1. Subtle Background Grid inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. 1999 Vintage Ticket Stub
        ticket = RoundedRectangle(
            corner_radius=0.1, width=5.6, height=4.0,
            stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95
        ).shift(LEFT * 3.2 + UP * 0.4)

        t_head = CleanText("BROKERAGE TRADE CONFIRMATION // 1999", font_size=15, color=TEXT)
        t_head.move_to(ticket.get_top() + DOWN * 0.4)

        t_stock = CleanText("BUY 100 SHARES // MARKET", font_size=20, color=TEXT, weight="BOLD")
        t_stock.next_to(t_head, DOWN, buff=0.35)

        t_fee = CleanText("$19.95 COMMISSION", font_size=34, color=RISK, weight="BOLD")
        t_fee.next_to(t_stock, DOWN, buff=0.45)

        t_note = CleanText("Explicit transparent fee paid per trade", font_size=13, color=TEXT, fill_opacity=0.60)
        t_note.next_to(t_fee, DOWN, buff=0.25)

        ticket_group = VGroup(ticket, t_head, t_stock, t_fee, t_note)

        # 3. Modern 2026 Zero-Fee App Card
        modern_card = RoundedRectangle(
            corner_radius=0.25, width=5.6, height=4.0,
            stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.95
        ).shift(RIGHT * 3.2 + UP * 0.4)

        m_head = CleanText("ZERO-COMMISSION APP // 2026", font_size=15, color=SUCCESS)
        m_head.move_to(modern_card.get_top() + DOWN * 0.4)

        m_stock = CleanText("BUY 100 SHARES // INSTANT", font_size=20, color=TEXT, weight="BOLD")
        m_stock.next_to(m_head, DOWN, buff=0.35)

        m_fee = CleanText("$0.00 COMMISSION", font_size=38, color=SUCCESS, weight="BOLD")
        m_fee.next_to(m_stock, DOWN, buff=0.45)

        m_note = CleanText("Sounds generous. Where did the fee go?", font_size=13, color=TEXT)
        m_note.next_to(m_fee, DOWN, buff=0.25)

        modern_group = VGroup(modern_card, m_head, m_stock, m_fee, m_note)

        # 4. Pumpkin Magnifying Loupe Zoom into Fine Print
        loupe = Circle(radius=1.2, stroke_color=RISK, stroke_width=3.5, fill_color="#261810", fill_opacity=0.92)
        loupe.move_to(modern_card.get_bottom() + UP * 0.6)

        handle = Line(start=loupe.get_corner(DR), end=loupe.get_corner(DR) + DR * 0.7, stroke_color=RISK, stroke_width=4)
        loupe_group = VGroup(loupe, handle)

        fine_txt1 = CleanText("SEC RULE 606 DISCLOSURE:", font_size=14, color=RISK, weight="BOLD").move_to(loupe.get_center() + UP * 0.3)
        fine_txt2 = CleanText("ORDER ROUTED TO HIGHEST", font_size=12, color=TEXT).next_to(fine_txt1, DOWN, buff=0.1)
        fine_txt3 = CleanText("REVENUE-SHARING BIDDER", font_size=12, color=RISK, weight="BOLD").next_to(fine_txt2, DOWN, buff=0.1)
        revealed_fine = VGroup(fine_txt1, fine_txt2, fine_txt3)

        # 5. Equation Badge: $0 != FREE
        badge = RoundedRectangle(
            corner_radius=0.15, width=5.6, height=1.1,
            stroke_color=RISK, stroke_width=3, fill_color="#1E120A", fill_opacity=0.95
        ).shift(DOWN * 2.6)
        b_txt = CleanText("$0.00 DOES NOT MEAN FREE", font_size=22, color=RISK, weight="BOLD").move_to(badge)

        # Group and stage_fit
        all_content = VGroup(ticket_group, modern_group, loupe_group, revealed_fine, badge, b_txt)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 25.16s) -----------------
        # Beat 1: Vintage Ticket enters (1.8s) + inspect hold (1.5s) = 3.3s
        self.play(FadeIn(ticket_group, shift=RIGHT * 0.4 * s_factor), run_time=1.8)
        self.wait(1.5)

        # Beat 2: Barcode scanline sweeps down ticket (2.0s) -> cumulative 5.3s
        scanline = Line(ticket.get_left() + RIGHT * 0.3, ticket.get_right() + LEFT * 0.3, stroke_color=RISK, stroke_width=2.5)
        scanline.move_to(ticket.get_top() + DOWN * 0.6)
        self.play(FadeIn(scanline), run_time=0.4)
        self.play(scanline.animate.move_to(ticket.get_bottom() + UP * 0.4), run_time=1.2)
        self.play(FadeOut(scanline), run_time=0.4)

        # Beat 3: Modern Card enters (1.8s) + comparison hold (1.5s) = 3.3s -> cumulative 8.6s
        self.play(FadeIn(modern_group, shift=LEFT * 0.4 * s_factor), run_time=1.8)
        self.wait(1.5)

        # Beat 4: Contrast Pulse on fees ($19.95 vs $0.00) (2.2s) -> cumulative 10.8s
        self.play(
            t_fee.animate.scale(1.08),
            m_fee.animate.scale(1.08),
            run_time=1.1
        )
        self.play(
            t_fee.animate.scale(1.0 / 1.08),
            m_fee.animate.scale(1.0 / 1.08),
            run_time=1.1
        )

        # Beat 5: Loupe appears (1.2s) -> cumulative 12.0s
        self.play(FadeIn(loupe_group, scale=0.6), run_time=1.2)

        # Beat 6: Fine print reveals (3.5s) -> cumulative 15.5s
        self.play(FadeIn(revealed_fine, shift=UP * 0.1), run_time=1.5)
        self.wait(2.0)

        # Beat 7: Loupe micro-pan across the fine print (3.5s) -> cumulative 19.0s
        self.play(
            loupe_group.animate.shift(RIGHT * 0.3 * s_factor),
            revealed_fine.animate.shift(RIGHT * 0.3 * s_factor),
            run_time=1.75
        )
        self.play(
            loupe_group.animate.shift(LEFT * 0.3 * s_factor),
            revealed_fine.animate.shift(LEFT * 0.3 * s_factor),
            run_time=1.75
        )

        # Beat 8: Insight badge slams down (1.8s) -> cumulative 20.8s
        self.play(FadeIn(badge, scale=1.1), FadeIn(b_txt, scale=1.1), run_time=1.8)

        # Beat 9: Final highlight pulse on badge (4.36s) -> cumulative 25.16s
        self.play(
            badge.animate.set_stroke(color=RISK, width=5.0),
            m_fee.animate.set_color(SUCCESS),
            run_time=2.18
        )
        self.play(
            badge.animate.set_stroke(color=RISK, width=3.0),
            run_time=2.18
        )
