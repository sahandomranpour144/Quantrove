"""
EP05 Scene 04: Who Actually Fills Your Order (01:07.00 - 01:36.84, TARGET: EXACTLY 29.84s)
Retail broker routing split: public exchange route drops blocked,
diverting flow into high-speed internalizer nodes (Citadel, Virtu, Susquehanna)
with active packet streams and microsecond latency telemetry.
Fitted strictly within manim_stage (x: 96-1824, y: 190-856).
"""
from manim import *
import numpy as np
import sys, os

YOUTUBE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, YOUTUBE_DIR)
from pipeline.manim_theme import apply_manim_theme, CleanText, BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, stage_fit, STAGE_CENTER

apply_manim_theme(config, is_vertical=False, fps=60)

class Scene04WhoFillsOrders(Scene):
    def construct(self):
        TARGET_DURATION = 29.84

        # 1. Background Grid inside stage
        grid = NumberPlane(
            x_range=[-6.4, 6.4, 1], y_range=[-2.34, 2.59, 1],
            background_line_style={"stroke_color": UI_STRUCTURE, "stroke_width": 1, "stroke_opacity": 0.35}
        ).move_to(STAGE_CENTER)
        self.add(grid)

        # 2. Left: Retail Investor Node
        retail_box = RoundedRectangle(
            corner_radius=0.25, width=3.8, height=2.2,
            stroke_color=SUCCESS, stroke_width=2.5, fill_color="#141E22", fill_opacity=0.95
        ).shift(LEFT * 5.0 + UP * 1.6)

        r_title = CleanText("RETAIL INVESTOR", font_size=17, color=SUCCESS, weight="BOLD").move_to(retail_box.get_top() + DOWN * 0.35)
        r_action = CleanText("TAP: BUY 100 SHARES", font_size=15, color=TEXT).next_to(r_title, DOWN, buff=0.18)
        r_sub = CleanText("Zero Commission App", font_size=13, color=TEXT, fill_opacity=0.60).next_to(r_action, DOWN, buff=0.12)
        retail_group = VGroup(retail_box, r_title, r_action, r_sub)

        # 3. Top Right: Public Exchange Node
        exchange_box = RoundedRectangle(
            corner_radius=0.25, width=4.6, height=2.2,
            stroke_color=UI_STRUCTURE, stroke_width=2, fill_color="#181C24", fill_opacity=0.95
        ).shift(RIGHT * 4.6 + UP * 1.6)

        e_title = CleanText("PUBLIC EXCHANGES", font_size=17, color=TEXT, weight="BOLD").move_to(exchange_box.get_top() + DOWN * 0.35)
        e_sub = CleanText("NYSE // NASDAQ", font_size=15, color=TEXT, fill_opacity=0.60).next_to(e_title, DOWN, buff=0.18)
        e_stat = CleanText("Public Order Book Match", font_size=13, color=TEXT, fill_opacity=0.60).next_to(e_sub, DOWN, buff=0.12)
        exchange_group = VGroup(exchange_box, e_title, e_sub, e_stat)

        # Connecting Pipeline
        expected_route = Line(start=retail_box.get_right(), end=exchange_box.get_left(), stroke_color=SUCCESS, stroke_width=4)
        route_lbl = CleanText("EXPECTED ROUTE", font_size=14, color=SUCCESS).next_to(expected_route, UP, buff=0.15)

        # 4. Gate Barrier
        gate_pos = expected_route.point_from_proportion(0.55)
        barrier = Rectangle(width=0.4, height=1.3, fill_color=RISK, fill_opacity=1.0, stroke_color=TEXT, stroke_width=2).move_to(gate_pos)
        barrier_lbl = CleanText("BLOCKED", font_size=13, color=TEXT, weight="BOLD").next_to(barrier, UP, buff=0.15)

        # 5. Route Diverts to Wholesale Internalizers
        diverted_start = retail_box.get_right() + RIGHT * 1.3
        diverted_line = Arrow(start=diverted_start, end=diverted_start + DOWN * 2.4, stroke_color=RISK, stroke_width=4, buff=0)
        diverted_lbl = CleanText("ACTUAL ROUTE // PFOF", font_size=13, color=RISK, weight="BOLD").next_to(diverted_line, LEFT, buff=0.2)

        # 3 Server Nodes: Citadel, Virtu, Susquehanna
        def make_server(name, share, lat_text, pos):
            box = RoundedRectangle(
                corner_radius=0.2, width=3.6, height=1.6,
                stroke_color=RISK, stroke_width=2, fill_color="#1F1612", fill_opacity=0.95
            ).move_to(pos)
            n = CleanText(name, font_size=16, color=TEXT, weight="BOLD").move_to(box.get_top() + DOWN * 0.35)
            s = CleanText(share, font_size=13, color=RISK).next_to(n, DOWN, buff=0.1)
            lat = CleanText(lat_text, font_size=11, color=SUCCESS).next_to(s, DOWN, buff=0.08)
            return VGroup(box, n, s, lat)

        s1 = make_server("CITADEL SECURITIES", "40%+ Retail Flow", "LATENCY: < 12 μs", np.array([-4.0, -1.8, 0]))
        s2 = make_server("VIRTU FINANCIAL", "High-Frequency Internalizer", "LATENCY: < 15 μs", np.array([0.0, -1.8, 0]))
        s3 = make_server("SUSQUEHANNA (SIG)", "Options & Equity Wholesaler", "LATENCY: < 18 μs", np.array([4.0, -1.8, 0]))
        servers = VGroup(s1, s2, s3)

        # 6. Summary Badge
        badge = RoundedRectangle(
            corner_radius=0.15, width=8.5, height=1.0,
            stroke_color=RISK, stroke_width=2.5, fill_color="#181310", fill_opacity=0.95
        ).shift(DOWN * 2.9)
        b_txt = CleanText("YOUR TRADES ARE INTERNALIZED BEFORE REACHING PUBLIC EXCHANGES", font_size=16, color=RISK, weight="BOLD").move_to(badge)

        # Stage fit
        all_content = VGroup(retail_group, exchange_group, expected_route, route_lbl, barrier, barrier_lbl, diverted_line, diverted_lbl, servers, badge, b_txt)
        all_content, s_factor = stage_fit(all_content, max_w=12.2, max_h=4.5)

        # ----------------- ANIMATION SEQUENCE (EXACTLY 29.84s) -----------------
        # Beat 1: Retail & Exchange nodes appear (1.8s) + hold (1.2s) = 3.0s
        self.play(FadeIn(retail_group, shift=RIGHT * 0.4 * s_factor), FadeIn(exchange_group, shift=LEFT * 0.4 * s_factor), run_time=1.8)
        self.wait(1.2)

        # Beat 2: Expected Route creates and packet travels across (1.2s + 1.8s) = 3.0s -> cumulative 6.0s
        self.play(Create(expected_route), FadeIn(route_lbl), run_time=1.2)
        packet = Dot(color=SUCCESS, radius=0.12 * s_factor).move_to(retail_box.get_right())
        self.play(MoveAlongPath(packet, expected_route), run_time=1.8, rate_func=linear)

        # Beat 3: Mechanical Gate Drops Shut with impact (1.2s + 1.0s + 1.8s) = 4.0s -> cumulative 10.0s
        self.play(FadeIn(barrier, scale=1.5), FadeIn(barrier_lbl), expected_route.animate.set_stroke(color=RISK), run_time=1.2)
        self.play(exchange_group.animate.set_opacity(0.20), run_time=1.0)
        self.wait(1.8)

        # Beat 4: Diverted Route arrow draws (1.5s) + servers emerge sequentially (2.0s) = 3.5s -> cumulative 13.5s
        self.play(Create(diverted_line), FadeIn(diverted_lbl), run_time=1.5)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.4 * s_factor) for s in servers], lag_ratio=0.25), run_time=2.0)

        # Beat 5: Secondary routing lines branch to each server (3.0s) -> cumulative 16.5s
        branch_lines = VGroup(*[
            Line(start=diverted_line.get_end(), end=s.get_top(), stroke_color=RISK, stroke_width=2.5)
            for s in servers
        ])
        self.play(Create(branch_lines), run_time=2.0)
        self.wait(1.0)

        # Beat 6: Microsecond Latency Telemetry Pulses across servers (4.5s) -> cumulative 21.0s
        for s in servers:
            self.play(
                s[0].animate.set_stroke(color=SUCCESS, width=3.5),
                s[3].animate.scale(1.15),
                run_time=0.75
            )
            self.play(
                s[0].animate.set_stroke(color=RISK, width=2.0),
                s[3].animate.scale(1.0 / 1.15),
                run_time=0.75
            )

        # Beat 7: Continuous Stream of Diverted Packets into wholesalers (5.0s) -> cumulative 26.0s
        p_stream = VGroup(*[
            Dot(color=SUCCESS if i % 2 == 0 else RISK, radius=0.08 * s_factor).move_to(retail_box.get_right())
            for i in range(9)
        ])
        def animate_packet(dot, delay, target_server):
            return Succession(
                Wait(delay),
                dot.animate(rate_func=linear).move_to(diverted_start),
                dot.animate(rate_func=linear).move_to(diverted_line.get_end()),
                dot.animate(rate_func=linear).move_to(target_server.get_top())
            )
        self.play(
            LaggedStart(*[
                animate_packet(p_stream[i], i * 0.25, servers[i % 3])
                for i in range(9)
            ], lag_ratio=0.15),
            run_time=5.0
        )

        # Beat 8: Summary Badge and pulse to exact end (1.8s + 2.04s) = 3.84s -> cumulative 29.84s
        self.play(FadeIn(badge, scale=1.05), FadeIn(b_txt, scale=1.05), run_time=1.8)
        self.play(
            badge.animate.set_stroke(color=RISK, width=4.5),
            b_txt.animate.set_color(TEXT),
            run_time=1.02
        )
        self.play(
            badge.animate.set_stroke(color=RISK, width=2.5),
            b_txt.animate.set_color(RISK),
            run_time=1.02
        )
