from manim import *

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class RefereeLagScene(Scene):
    def construct(self):
        # Target total duration: Exactly 28.0 seconds
        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"

        # 1. Header (0.0s - 3.0s) -> 3.0s
        title = Text("THE 7-MONTH REFEREE LAG", font_size=36, font="Segoe UI", weight=BOLD, color=GOLD)
        subtitle = Text("WHY OFFICIAL ANNOUNCEMENTS ALWAYS ARRIVE TOO LATE", font_size=19, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.45)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # 2. Horizontal Timeline Track (3.0s - 10.0s) -> 7.0s
        track_bg = Line(start=LEFT * 5.5, end=RIGHT * 5.5, color=PANEL_BORDER, stroke_width=10).shift(UP * 0.5)

        p_start = LEFT * 5.5 + UP * 0.5
        p_nber = LEFT * 5.5 + RIGHT * (11.0 * (7.0 / 10.4)) + UP * 0.5
        p_end = RIGHT * 5.5 + UP * 0.5

        d_start = Dot(p_start, color=CYAN, radius=0.16)
        lbl_start = Text("Month 0\nRecession Begins", font_size=13, font="Segoe UI", color=WHITE, line_spacing=1.2).next_to(d_start, DOWN, buff=0.3)

        d_end = Dot(p_end, color=GREEN, radius=0.16)
        lbl_end = Text("Month 10.4\nAverage End Date", font_size=13, font="Segoe UI", color=GREEN, line_spacing=1.2).next_to(d_end, DOWN, buff=0.3)

        self.play(
            Create(track_bg),
            FadeIn(d_start), FadeIn(lbl_start),
            FadeIn(d_end), FadeIn(lbl_end),
            run_time=2.0
        )
        self.wait(5.0)

        # 3. Active Progress Bar & Month 7 Declaration Alarm (10.0s - 18.0s) -> 8.0s
        track_active = Line(start=p_start, end=p_nber, color=RED, stroke_width=10)
        d_nber = Dot(p_nber, color=RED, radius=0.20)
        lbl_nber = Text("Month 7 (Average)\nNBER DECLARES RECESSION!", font_size=14, font="Segoe UI", weight=BOLD, color=RED, line_spacing=1.2).next_to(d_nber, UP, buff=0.3)

        alarm_ring = Circle(radius=0.4, color=RED, stroke_width=2.5).move_to(p_nber)

        self.play(Create(track_active), run_time=2.5)
        self.play(FadeIn(d_nber), FadeIn(lbl_nber), Create(alarm_ring), run_time=1.5)
        self.play(alarm_ring.animate.scale(1.8).set_stroke_opacity(0), run_time=1.5)
        self.wait(2.5)

        # 4. Bracket: 70% Elapsed Callout (18.0s - 28.0s) -> 10.0s
        elapsed_box = RoundedRectangle(corner_radius=0.15, height=1.6, width=10.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=GOLD, stroke_width=2).shift(DOWN * 1.8)
        elapsed_title = Text("DATA TRAP: ~70% OF THE RECESSION IS ALREADY OVER", font_size=17, font="Segoe UI", weight=BOLD, color=GOLD).next_to(elapsed_box.get_top(), DOWN, buff=0.3)
        elapsed_desc = Text(
            "• 1980 Recession: NBER announced it after it was literally already over.\n• 2020 Recession: Declared in June after market hit bottom in March and economy bottomed in April.",
            font_size=12, font="Segoe UI", color=WHITE, line_spacing=1.3
        ).next_to(elapsed_title, DOWN, buff=0.2)

        self.play(FadeIn(elapsed_box, shift=UP), FadeIn(elapsed_title, shift=UP), FadeIn(elapsed_desc, shift=UP), run_time=1.8)
        self.wait(8.2)
