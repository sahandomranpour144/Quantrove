"""
Quantrove Native Short: The 2-Cent Drag (Completely Rebuilt)
Format: 9:16 Vertical (1080x1920 @ 60fps)
Target Duration: Exactly 34.00s (Calibrated to 33.45s Gemini Voiceover)
Visual Architecture: $150.00 vs $150.02 -> 100 Shares Bracket -> $2.00 Drag -> Calendar Accumulation -> 500-Trade Grid -> Illustrative $1,000 Loss Meter
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

class TwoCentDragRebuilt(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # ----------------------------------------------------
        # BEAT 1: [0.0s - 6.5s] $150.00 vs $150.02 Price Split
        # ----------------------------------------------------
        hdr = CleanText("EXECUTION BENCHMARK", font_size=15, color=TEXT, fill_opacity=0.7).move_to(UP * 6.0)

        card_nbbo = RoundedRectangle(corner_radius=0.25, width=3.8, height=2.4, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.96).move_to(UP * 4.2 + LEFT * 2.1)
        t_nbbo = CleanText("PUBLIC BEST BID", font_size=12, color=SUCCESS).move_to(card_nbbo.get_top() + DOWN * 0.4)
        p_nbbo = CleanText("$150.00", font_size=30, color=TEXT, weight="BOLD").move_to(card_nbbo.get_center() + DOWN * 0.2)
        group_nbbo = VGroup(card_nbbo, t_nbbo, p_nbbo)

        card_app = RoundedRectangle(corner_radius=0.25, width=3.8, height=2.4, stroke_color=RISK, stroke_width=2.5, fill_color="#24140E", fill_opacity=0.96).move_to(UP * 4.2 + RIGHT * 2.1)
        t_app = CleanText("YOUR APP FILL", font_size=12, color=RISK).move_to(card_app.get_top() + DOWN * 0.4)
        p_app = CleanText("$150.02", font_size=30, color=TEXT, weight="BOLD").move_to(card_app.get_center() + DOWN * 0.2)
        group_app = VGroup(card_app, t_app, p_app)

        delta_card = RoundedRectangle(corner_radius=0.2, width=6.2, height=1.3, stroke_color=RISK, stroke_width=3, fill_color="#2A1408", fill_opacity=0.98).move_to(UP * 2.2)
        delta_txt = CleanText("DELTA: -$0.02 / SHARE WORSE", font_size=16, color=RISK, weight="BOLD").move_to(delta_card)
        delta_group = VGroup(delta_card, delta_txt)

        self.play(FadeIn(hdr), FadeIn(group_nbbo, shift=RIGHT * 0.3), FadeIn(group_app, shift=LEFT * 0.3), run_time=1.2)
        self.play(FadeIn(delta_group, scale=1.12), run_time=1.0)
        self.wait(4.3)

        # ----------------------------------------------------
        # BEAT 2: [6.5s - 14.5s] 100 Shares -> $2.00 Drag
        # ----------------------------------------------------
        math_card = RoundedRectangle(corner_radius=0.25, width=7.2, height=2.8, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.98).move_to(DOWN * 0.2)
        m_step1 = CleanText("-$0.02  x  100 SHARES", font_size=20, color=TEXT, weight="BOLD").move_to(math_card.get_top() + DOWN * 0.55)
        m_step2 = CleanText("= -$2.00 LOSS PER ORDER", font_size=24, color=RISK, weight="BOLD").next_to(m_step1, DOWN, buff=0.3)
        m_dismiss = CleanText("\"Basically completely free...\"", font_size=13, color=TEXT, fill_opacity=0.6).next_to(m_step2, DOWN, buff=0.25)
        math_group = VGroup(math_card, m_step1, m_step2, m_dismiss)

        self.play(FadeIn(math_group, shift=UP * 0.4), run_time=1.2)
        self.wait(6.8)

        # ----------------------------------------------------
        # BEAT 3: [14.5s - 21.5s] The Illusion vs Repeated Trades
        # ----------------------------------------------------
        old_card = RoundedRectangle(corner_radius=0.2, width=6.8, height=2.0, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#1E232F", fill_opacity=0.95).move_to(DOWN * 3.4)
        old_t = CleanText("1999 TICKET COMMISSION: $19.95", font_size=13, color=TEXT, fill_opacity=0.7).move_to(old_card.get_top() + DOWN * 0.4)
        old_comp = CleanText("Old Fee: Obvious | New Drag: Invisible", font_size=14, color=RISK, weight="BOLD").next_to(old_t, DOWN, buff=0.2)
        old_group = VGroup(old_card, old_t, old_comp)

        self.play(FadeIn(old_group, shift=UP * 0.3), run_time=1.0)
        self.wait(6.0)

        # ----------------------------------------------------
        # BEAT 4: [21.5s - 34.0s] Illustrative Model: 500 Trades -> $1,000 Drag
        # ----------------------------------------------------
        self.play(
            FadeOut(hdr), FadeOut(group_nbbo), FadeOut(group_app), FadeOut(delta_group),
            FadeOut(math_group), FadeOut(old_group),
            run_time=0.8
        )

        model_hdr = CleanText("ILLUSTRATIVE SCENARIO: 500 TRADES", font_size=15, color=TEXT, weight="BOLD").move_to(UP * 5.6)
        model_sub = CleanText("2 Orders Per Week Over 5 Years", font_size=12, color=TEXT, fill_opacity=0.7).next_to(model_hdr, DOWN, buff=0.15)

        # 10x10 Trade Accumulation Grid
        dots_grid = VGroup()
        for r in range(8):
            for c in range(8):
                sq = Square(side_length=0.40, stroke_color=UI_STRUCTURE, stroke_width=1, fill_color=RISK, fill_opacity=0.9).move_to(
                    LEFT * 2.8 + RIGHT * (c * 0.46) + UP * 3.6 + DOWN * (r * 0.46)
                )
                dots_grid.add(sq)

        tally_box = RoundedRectangle(corner_radius=0.25, width=7.2, height=3.0, stroke_color=RISK, stroke_width=3.5, fill_color="#181210", fill_opacity=0.98).move_to(DOWN * 2.8)
        t_label = CleanText("CUMULATIVE EXECUTION DRAG:", font_size=13, color=RISK).move_to(tally_box.get_top() + DOWN * 0.4)
        t_amount = CleanText("-$1,000.00", font_size=36, color=RISK, weight="BOLD").next_to(t_label, DOWN, buff=0.25)
        t_disclaimer = CleanText("*Hypothetical model based on $2.00 drag / 100-share trade", font_size=10, color=TEXT, fill_opacity=0.6).next_to(t_amount, DOWN, buff=0.2)
        tally_group = VGroup(tally_box, t_label, t_amount, t_disclaimer)

        badge = RoundedRectangle(corner_radius=0.15, width=5.4, height=1.0, stroke_color=TEXT, stroke_width=2, fill_color=TEXT, fill_opacity=0.95).move_to(DOWN * 5.2)
        badge_txt = CleanText("COMPOUNDING DRAG", font_size=15, color=BACKGROUND, weight="BOLD").move_to(badge.get_center())
        badge_group = VGroup(badge, badge_txt)

        self.play(FadeIn(model_hdr), FadeIn(model_sub), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(s, scale=0.8) for s in dots_grid], lag_ratio=0.015), run_time=2.2)
        self.play(FadeIn(tally_group, scale=1.08), run_time=1.2)
        self.play(FadeIn(badge_group, scale=1.1), run_time=0.8)
        self.wait(6.9)
