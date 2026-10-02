"""
Quantrove Native Short 1: Where Your $0 Trade Actually Goes
Format: 9:16 Vertical (1080x1920 @ 60fps)
Target Duration: Exactly 35.80s (Calibrated to 35.45s Voiceover)
Palette: Raisin Black #202322, Charcoal Slate #233D4C, Power Lime #C3D809, Pumpkin #FD802E, Off-White #E6EDF3
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

class WhereTradeGoes(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.25}
        )
        self.add(grid)

        # BEAT 1: IDEA (0.0s - 8.0s) - Smartphone order initiation
        phone = RoundedRectangle(corner_radius=0.3, width=3.8, height=3.0, stroke_color=UI_STRUCTURE, stroke_width=2.5, fill_color="#181C24", fill_opacity=0.95).move_to(DOWN * 4.2)
        phone_title = CleanText("RETAIL BROKER APP", font_size=15, color=TEXT, weight="BOLD").move_to(phone.get_top() + DOWN * 0.4)
        buy_btn = RoundedRectangle(corner_radius=0.15, width=3.0, height=0.9, stroke_color=SUCCESS, stroke_width=2, fill_color="#1F2E14", fill_opacity=0.9).move_to(phone.get_center() + DOWN * 0.2)
        buy_txt = CleanText("BUY 100 SHARES // $0.00", font_size=14, color=SUCCESS, weight="BOLD").move_to(buy_btn.get_center())
        phone_group = VGroup(phone, phone_title, buy_btn, buy_txt)

        self.play(FadeIn(phone_group, shift=UP * 0.5), run_time=1.2)
        self.wait(1.5)

        # Order packet launches
        packet = Dot(point=buy_btn.get_center(), radius=0.16, color=SUCCESS)
        packet_ring = Circle(radius=0.28, stroke_color=SUCCESS, stroke_width=1.5).move_to(packet)
        self.play(FadeIn(packet), FadeIn(packet_ring), run_time=0.5)
        self.play(VGroup(packet, packet_ring).animate.move_to(DOWN * 0.8), run_time=2.0, rate_func=smooth)
        self.wait(2.8)

        # BEAT 2: SIMPLE_WRONG (8.0s - 16.5s) - NYSE / Exchange Barrier
        nyse_box = RoundedRectangle(corner_radius=0.2, width=4.8, height=2.2, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.95).move_to(UP * 4.5)
        nyse_title = CleanText("PUBLIC STOCK EXCHANGE", font_size=15, color=TEXT, weight="BOLD").move_to(nyse_box.get_top() + DOWN * 0.4)
        nyse_sub = CleanText("NYSE // NASDAQ (Public Book)", font_size=13, color=TEXT, fill_opacity=0.6).next_to(nyse_title, DOWN, buff=0.15)
        nyse_group = VGroup(nyse_box, nyse_title, nyse_sub)

        self.play(FadeIn(nyse_group, shift=DOWN * 0.5), run_time=1.2)

        # Route path to NYSE
        route_nyse = DashedLine(start=DOWN * 0.8, end=UP * 3.4, stroke_color=UI_STRUCTURE, stroke_width=2)
        self.play(Create(route_nyse), run_time=0.8)
        self.play(VGroup(packet, packet_ring).animate.move_to(UP * 1.5), run_time=1.5)

        # Barrier drops: ROUTE BLOCKED
        barrier = Line(start=LEFT * 1.8 + UP * 2.5, end=RIGHT * 1.8 + UP * 2.5, stroke_color=RISK, stroke_width=4)
        blocked_lbl = CleanText("GATE CLOSED // ZERO ROUTED", font_size=12, color=RISK, weight="BOLD").next_to(barrier, UP, buff=0.15)
        self.play(Create(barrier), FadeIn(blocked_lbl), run_time=1.0)
        self.wait(4.0)

        # BEAT 3: COMPLEX_WRONG (16.5s - 25.5s) - Broker Node & Diversion
        broker_box = RoundedRectangle(corner_radius=0.15, width=4.0, height=1.4, stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#1C212B", fill_opacity=0.95).move_to(DOWN * 0.5)
        broker_txt = CleanText("ORDER ROUTER GATEWAY", font_size=14, color=TEXT, weight="BOLD").move_to(broker_box.get_top() + DOWN * 0.35)
        broker_sub = CleanText("Zero Inventory Risk Taken", font_size=12, color=RISK).next_to(broker_txt, DOWN, buff=0.1)
        broker_group = VGroup(broker_box, broker_txt, broker_sub)

        self.play(
            FadeOut(barrier), FadeOut(blocked_lbl), FadeOut(route_nyse),
            VGroup(packet, packet_ring).animate.move_to(broker_box.get_center()),
            FadeIn(broker_group),
            run_time=1.5
        )
        self.wait(7.5)

        # BEAT 4: INSIGHT (25.5s - 35.8s) - Wholesale Internalizers & Reverse PFOF Kickback
        wholesaler_box = RoundedRectangle(corner_radius=0.2, width=5.2, height=2.4, stroke_color=SUCCESS, stroke_width=2.5, fill_color="#182319", fill_opacity=0.95).move_to(UP * 2.8)
        ws_title = CleanText("WHOLESALE INTERNALIZERS", font_size=16, color=SUCCESS, weight="BOLD").move_to(wholesaler_box.get_top() + DOWN * 0.4)
        ws_names = CleanText("CITADEL SECURITIES // VIRTU FINANCIAL", font_size=12, color=TEXT, weight="BOLD").next_to(ws_title, DOWN, buff=0.15)
        ws_sub = CleanText("Fills 70%+ of All US Retail Orders", font_size=12, color=TEXT, fill_opacity=0.7).next_to(ws_names, DOWN, buff=0.12)
        wholesaler_group = VGroup(wholesaler_box, ws_title, ws_names, ws_sub)

        order_pipe = Arrow(start=broker_box.get_top(), end=wholesaler_box.get_bottom() + LEFT * 0.8, stroke_color=SUCCESS, stroke_width=3, buff=0.1)
        order_lbl = CleanText("YOUR ORDER FLOW", font_size=11, color=SUCCESS, weight="BOLD").next_to(order_pipe, LEFT, buff=0.1)

        kickback_pipe = Arrow(start=wholesaler_box.get_bottom() + RIGHT * 0.8, end=broker_box.get_top() + RIGHT * 0.8, stroke_color=RISK, stroke_width=3, buff=0.1)
        kickback_lbl = CleanText("PFOF CASH KICKBACK", font_size=11, color=RISK, weight="BOLD").next_to(kickback_pipe, RIGHT, buff=0.1)

        badge = RoundedRectangle(corner_radius=0.15, width=4.8, height=1.0, stroke_color=TEXT, stroke_width=2, fill_color=TEXT, fill_opacity=0.95).move_to(UP * 0.8)
        badge_txt = CleanText("INTERNALIZERS", font_size=14, color=BACKGROUND, weight="BOLD").move_to(badge.get_center())
        badge_group = VGroup(badge, badge_txt)

        self.play(
            FadeOut(nyse_group),
            FadeIn(wholesaler_group),
            Create(order_pipe), FadeIn(order_lbl),
            Create(kickback_pipe), FadeIn(kickback_lbl),
            VGroup(packet, packet_ring).animate.move_to(wholesaler_box.get_center()),
            run_time=2.0
        )
        self.play(FadeIn(badge_group, shift=LEFT * 0.5), run_time=1.0)
        self.wait(7.3)
