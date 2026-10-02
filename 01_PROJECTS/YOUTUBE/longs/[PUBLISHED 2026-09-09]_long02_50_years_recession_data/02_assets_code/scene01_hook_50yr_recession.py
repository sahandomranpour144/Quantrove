from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class Hook50YrRecessionScene(Scene):
    def construct(self):
        # Target total duration: Exactly 25.0 seconds
        CYAN = "#06B6D4"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#151B26"
        PANEL_BORDER = "#2A364F"

        # 1. Header & Title (0.0s - 3.5s) -> 3.5s
        title = Text("50 YEARS OF RECESSIONS & MARKETS", font_size=36, font="Segoe UI", weight=BOLD, color=CYAN)
        subtitle = Text("WHAT DOES FIVE DECADES OF ACTUAL DATA REALLY PROVE?", font_size=19, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.45)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.5)

        # 2. Coordinate Axes (3.5s - 8.0s) -> 4.5s
        axes = Axes(
            x_range=[1970, 2025, 10],
            y_range=[1, 4, 1],
            x_length=11.0,
            y_length=4.5,
            axis_config={"color": MUTED, "stroke_width": 2},
            tips=False
        ).shift(DOWN * 0.4)

        x_labels = VGroup(*[
            Text(str(yr), font_size=14, font="Segoe UI", color=MUTED).next_to(axes.c2p(yr, 1), DOWN, buff=0.2)
            for yr in range(1970, 2030, 10)
        ])

        y_labels = VGroup(
            Text("100", font_size=13, font="Segoe UI", color=MUTED).next_to(axes.c2p(1970, 2), LEFT, buff=0.2),
            Text("1,000", font_size=13, font="Segoe UI", color=MUTED).next_to(axes.c2p(1970, 3), LEFT, buff=0.2),
            Text("6,000", font_size=13, font="Segoe UI", color=MUTED).next_to(axes.c2p(1970, 4), LEFT, buff=0.2),
        )
        y_title = Text("S&P 500 (Log Scale)", font_size=14, font="Segoe UI", color=CYAN).next_to(axes.c2p(1970, 4), UP, buff=0.2).align_to(axes, LEFT)

        self.play(Create(axes), FadeIn(x_labels), FadeIn(y_labels), FadeIn(y_title), run_time=1.8)
        self.wait(2.7)

        # 3. Shaded Recession Bands (8.0s - 14.0s) -> 6.0s
        recession_ranges = [
            (1973.9, 1975.2, "1973"),
            (1980.0, 1980.6, "1980"),
            (1981.5, 1982.9, "1981"),
            (1990.5, 1991.2, "1990"),
            (2001.2, 2001.9, "2001"),
            (2007.9, 2009.5, "2008"),
            (2020.1, 2020.3, "2020"),
        ]

        band_rects = []
        for x_start, x_end, label in recession_ranges:
            p_start = axes.c2p(x_start, 1)
            p_end = axes.c2p(x_end, 4)
            w = p_end[0] - p_start[0]
            h = p_end[1] - p_start[1]
            rect = Rectangle(width=max(w, 0.12), height=h, fill_color="#334155", fill_opacity=0.5, stroke_color=PANEL_BORDER, stroke_width=1)
            rect.move_to([(p_start[0] + p_end[0])/2, (p_start[1] + p_end[1])/2, 0])
            band_rects.append(rect)

        band_group = VGroup(*band_rects)
        band_badge = RoundedRectangle(corner_radius=0.1, height=0.5, width=3.8, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=MUTED, stroke_width=1.5).to_edge(RIGHT, buff=0.8).shift(UP * 2.0)
        band_badge_txt = Text("Shaded Areas = U.S. Recessions", font_size=13, font="Segoe UI", color=WHITE).move_to(band_badge.get_center())

        self.play(FadeIn(band_group, lag_ratio=0.15), FadeIn(band_badge), FadeIn(band_badge_txt), run_time=2.2)
        self.wait(3.8)

        # 4. S&P 500 Exponential Curve Sweep (14.0s - 20.0s) -> 6.0s
        def sp_func(x):
            base = 1.0 + 0.048 * (x - 1970)
            if 1973.5 <= x <= 1975.5:
                base -= 0.35 * np.exp(-((x - 1974.5)/0.6)**2)
            elif 1981.0 <= x <= 1983.0:
                base -= 0.22 * np.exp(-((x - 1982.0)/0.6)**2)
            elif 2000.5 <= x <= 2003.0:
                base -= 0.40 * np.exp(-((x - 2002.0)/0.8)**2)
            elif 2007.5 <= x <= 2009.8:
                base -= 0.55 * np.exp(-((x - 2009.0)/0.7)**2)
            elif 2020.0 <= x <= 2020.8:
                base -= 0.30 * np.exp(-((x - 2020.3)/0.3)**2)
            return min(max(base, 1.0), 3.9)

        curve = axes.plot(sp_func, x_range=[1970, 2025], color=CYAN, stroke_width=3.5)

        self.play(Create(curve), run_time=3.5)
        self.wait(2.5)

        # 5. Generational Bottom Pulse Beacons (20.0s - 25.0s) -> 5.0s
        dot_2008 = Dot(axes.c2p(2009.2, sp_func(2009.2)), color=GREEN, radius=0.12)
        beacon_ring = Circle(radius=0.3, color=GREEN, stroke_width=2).move_to(dot_2008.get_center())
        lbl_2008 = Text("2009 Low: +68% Rally\nInside Recession!", font_size=13, font="Segoe UI", weight=BOLD, color=GREEN).next_to(dot_2008, UP, buff=0.3)

        self.play(
            FadeIn(dot_2008),
            Create(beacon_ring),
            FadeIn(lbl_2008, shift=UP),
            run_time=1.5
        )
        self.play(
            beacon_ring.animate.scale(1.8).set_stroke_opacity(0),
            run_time=1.5
        )
        self.wait(2.0)
