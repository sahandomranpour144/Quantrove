"""
Quantrove Standalone Short: Why Wall Street Loves "Dumb Money" (Completely Rebuilt)
Format: 9:16 Vertical (1080x1920 @ 60fps)
Target Duration: Exactly 43.00s (Calibrated to 42.49s Gemini Voiceover)
Visual Architecture: HFT vs Beginner Paradox -> Debunking Front-Running & Directional Bets -> Adverse Selection Model (Informed Asymmetric Risk vs Uninformed Random Flow) -> Spread Capture
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

class WhyDumbMoneyRebuilt(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # ----------------------------------------------------
        # BEAT 1: [0.0s - 9.0s] The Paradox: HFTs Paying for Retail
        # ----------------------------------------------------
        hft_card = RoundedRectangle(corner_radius=0.25, width=6.8, height=2.4, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.96).move_to(UP * 4.8)
        hft_t = CleanText("QUANT / HFT MARKET MAKER", font_size=15, color=SUCCESS, weight="BOLD").move_to(hft_card.get_top() + DOWN * 0.45)
        hft_sub = CleanText("Microsecond Speed // Multi-Billion Balance Sheet", font_size=12, color=TEXT, fill_opacity=0.7).next_to(hft_t, DOWN, buff=0.18)
        hft_group = VGroup(hft_card, hft_t, hft_sub)

        retail_card = RoundedRectangle(corner_radius=0.25, width=6.8, height=2.2, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.96).move_to(UP * 1.0)
        ret_t = CleanText("RETAIL BEGINNER TRADER", font_size=15, color=TEXT, weight="BOLD").move_to(retail_card.get_top() + DOWN * 0.4)
        ret_sub = CleanText("Buying 50 Shares on Smartphone App", font_size=12, color=TEXT, fill_opacity=0.7).next_to(ret_t, DOWN, buff=0.18)
        retail_group = VGroup(retail_card, ret_t, ret_sub)

        flow_pipe = Arrow(start=hft_card.get_bottom(), end=retail_card.get_top(), stroke_color=RISK, stroke_width=3.5, buff=0.1)
        flow_lbl = CleanText("PAYS BROKER FOR YOUR FLOW", font_size=13, color=RISK, weight="BOLD").next_to(flow_pipe, RIGHT, buff=0.15)

        self.play(FadeIn(hft_group, shift=DOWN * 0.4), FadeIn(retail_group, shift=UP * 0.4), run_time=1.2)
        self.play(Create(flow_pipe), FadeIn(flow_lbl), run_time=1.2)
        self.wait(6.6)

        # ----------------------------------------------------
        # BEAT 2: [9.0s - 18.0s] Myth #1: Front-Running Predictions
        # ----------------------------------------------------
        self.play(FadeOut(flow_pipe), FadeOut(flow_lbl), run_time=0.6)

        myth1 = RoundedRectangle(corner_radius=0.2, width=7.0, height=2.6, stroke_color=RISK, stroke_width=2.5, fill_color="#24140E", fill_opacity=0.96).move_to(DOWN * 2.8)
        m1_hdr = CleanText("MYTH #1: FRONT-RUNNING IDEAS", font_size=14, color=RISK, weight="BOLD").move_to(myth1.get_top() + DOWN * 0.4)
        m1_desc = CleanText("Assumption: HFTs steal retail stock picks", font_size=12, color=TEXT).next_to(m1_hdr, DOWN, buff=0.2)
        m1_verdict = CleanText("FALSE: Retail has zero market prediction edge", font_size=12, color=RISK, weight="BOLD").next_to(m1_desc, DOWN, buff=0.2)
        m1_group = VGroup(myth1, m1_hdr, m1_desc, m1_verdict)

        self.play(FadeIn(m1_group, shift=UP * 0.3), run_time=1.2)
        self.wait(7.2)

        # ----------------------------------------------------
        # BEAT 3: [18.0s - 25.5s] Myth #2: Directional Bets
        # ----------------------------------------------------
        self.play(FadeOut(m1_group), run_time=0.6)

        myth2 = RoundedRectangle(corner_radius=0.2, width=7.0, height=2.6, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.96).move_to(DOWN * 2.8)
        m2_hdr = CleanText("MYTH #2: DIRECTIONAL BETS", font_size=14, color=TEXT, weight="BOLD").move_to(myth2.get_top() + DOWN * 0.4)
        m2_desc = CleanText("Assumption: Market makers gamble on market direction", font_size=12, color=TEXT).next_to(m2_hdr, DOWN, buff=0.2)
        m2_verdict = CleanText("FALSE: Goal is strictly ZERO inventory risk", font_size=13, color=SUCCESS, weight="BOLD").next_to(m2_desc, DOWN, buff=0.2)
        m2_group = VGroup(myth2, m2_hdr, m2_desc, m2_verdict)

        self.play(FadeIn(m2_group, shift=UP * 0.3), run_time=1.2)
        self.wait(5.7)

        # ----------------------------------------------------
        # BEAT 4: [25.5s - 43.0s] The Adverse Selection Model
        # ----------------------------------------------------
        self.play(
            FadeOut(hft_group), FadeOut(retail_group), FadeOut(m2_group),
            run_time=0.8
        )

        title_adv = CleanText("THE ADVERSE SELECTION MODEL", font_size=16, color=TEXT, weight="BOLD").move_to(UP * 5.6)

        # Top Card: Informed Institutional Flow (Hazardous)
        inst_card = RoundedRectangle(corner_radius=0.2, width=7.2, height=3.0, stroke_color=RISK, stroke_width=2.5, fill_color="#24140E", fill_opacity=0.98).move_to(UP * 2.8)
        i_hdr = CleanText("INSTITUTIONAL ORDER FLOW", font_size=14, color=RISK, weight="BOLD").move_to(inst_card.get_top() + DOWN * 0.4)
        i_feat = CleanText("Faster Private Research // Directional Capital", font_size=12, color=TEXT).next_to(i_hdr, DOWN, buff=0.2)
        i_risk = CleanText("SEVERE INFORMATION RISK (Adverse Selection)", font_size=13, color=RISK, weight="BOLD").next_to(i_feat, DOWN, buff=0.2)
        inst_group = VGroup(inst_card, i_hdr, i_feat, i_risk)

        # Bottom Card: Uninformed Retail Flow (Safe Spread Capture)
        ret_card = RoundedRectangle(corner_radius=0.2, width=7.2, height=3.0, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.98).move_to(DOWN * 0.8)
        r_hdr = CleanText("RETAIL ORDER FLOW", font_size=14, color=SUCCESS, weight="BOLD").move_to(ret_card.get_top() + DOWN * 0.4)
        r_feat = CleanText("Small, Random & Uncoordinated Orders", font_size=12, color=TEXT).next_to(r_hdr, DOWN, buff=0.2)
        r_risk = CleanText("ZERO ADVERSE RISK: 100% SPREAD CAPTURE", font_size=13, color=SUCCESS, weight="BOLD").next_to(r_feat, DOWN, buff=0.2)
        ret_group = VGroup(ret_card, r_hdr, r_feat, r_risk)

        badge = RoundedRectangle(corner_radius=0.15, width=5.6, height=1.1, stroke_color=TEXT, stroke_width=2, fill_color=TEXT, fill_opacity=0.95).move_to(DOWN * 4.2)
        badge_txt = CleanText("ADVERSE SELECTION", font_size=15, color=BACKGROUND, weight="BOLD").move_to(badge.get_center())
        badge_group = VGroup(badge, badge_txt)

        self.play(FadeIn(title_adv), run_time=0.6)
        self.play(FadeIn(inst_group, shift=DOWN * 0.3), run_time=1.2)
        self.play(FadeIn(ret_group, shift=UP * 0.3), run_time=1.2)
        self.play(FadeIn(badge_group, scale=1.1), run_time=0.8)
        self.wait(12.9)
