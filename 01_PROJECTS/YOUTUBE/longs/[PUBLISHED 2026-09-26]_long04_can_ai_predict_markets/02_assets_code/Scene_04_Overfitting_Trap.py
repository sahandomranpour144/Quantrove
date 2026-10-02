from manim import *
import numpy as np

# Quantrove Theme Colors
COLOR_BG = "#0B0F19"
COLOR_CYAN = "#00F0FF"
COLOR_MINT = "#00FFA3"
COLOR_GOLD = "#FFD700"
COLOR_CRIMSON = "#FF3366"
COLOR_WHITE = "#F8FAFC"
COLOR_MUTED = "#94A3B8"
COLOR_CARD_BG = "#131B2E"

# High-resolution CleanText to eliminate Pango sub-pixel advance quantization / character scattering
def CleanText(text, font="Segoe UI", font_size=24, **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    return Text(text, font=font, font_size=ref_size, **kwargs).scale(scale_factor)

# Render targets:
#   OverfittingTrapPart1 -> TIMELINE_MEDIA/04_T03-21_to_03-50_manim_overfitting_trap_part1.mp4
#     Timeline window 03:21-03:50 -> EXACT duration 29.0s (1080p60).
#     Visual: scattered historical points + hyper-wiggly polynomial curve
#     achieving 99.8% backtest accuracy. (Scene 4, Part 1)
#   OverfittingTrapPart2 -> TIMELINE_MEDIA/04_T04-00_to_04-33_manim_overfitting_trap_part2.mp4
#     Timeline window 04:00-04:33 -> EXACT duration 33.0s (1080p60).
#     Visual: crossing the dashed LIVE DATA boundary into a catastrophic red
#     crash. Red stamp: OVERFITTED TO NOISE. (Scene 4, Part 2)

# Deterministic dataset (shared by both parts so the curves match)
np_seed = 42
x_hist = np.array([0.5, 1.0, 1.6, 2.2, 2.8, 3.4, 4.0, 4.6, 4.9])
y_hist = np.array([4.2, 5.8, 3.9, 6.4, 4.1, 7.2, 5.0, 6.8, 5.5])


class OverfittingTrapPart1(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ---- Definition badge (t 0.0 - 3.0) ----
        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.6, height=1.1,
                                    fill_color=COLOR_CARD_BG, fill_opacity=0.9,
                                    stroke_color=COLOR_CRIMSON, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("PATTERN #2: THE OVERFITTING TRAP", weight="BOLD",
                                font_size=24, color=COLOR_CRIMSON).next_to(badge_bg.get_top(), DOWN, buff=0.15)
        badge_sub = CleanText("Overfitting = Learning historical noise instead of real, repeatable patterns",
                              font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        # ---- Axes + backtest/live divider (t 3.0 - 6.0) ----
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 10, 2],
            x_length=8.8, y_length=4.2,
            axis_config={"color": COLOR_MUTED, "stroke_width": 2},
            tips=True,
        ).shift(DOWN * 0.7)
        divider = DashedLine(axes.c2p(5.0, 0), axes.c2p(5.0, 9.5),
                             color=COLOR_GOLD, stroke_width=2.5)
        hist_label = CleanText("HISTORICAL BACKTEST", weight="BOLD",
                               font_size=16, color=COLOR_MINT).next_to(axes.c2p(2.5, 9.5), DOWN, buff=0.1)
        live_label = CleanText("LIVE UNSEEN DATA", weight="BOLD",
                               font_size=16, color=COLOR_CRIMSON).next_to(axes.c2p(7.5, 9.5), DOWN, buff=0.1)
        self.play(Create(axes), Create(divider), FadeIn(hist_label), FadeIn(live_label), run_time=2.5)
        self.wait(0.5)

        # ---- Historical data points (t 6.0 - 9.0) ----
        hist_dots = VGroup(*[Dot(axes.c2p(x, y), color=COLOR_CYAN, radius=0.08)
                             for x, y in zip(x_hist, y_hist)])
        self.play(LaggedStartMap(FadeIn, hist_dots, lag_ratio=0.15), run_time=2.0)
        self.wait(1.0)

        # ---- Hyper-wiggly polynomial through every point (t 9.0 - 13.0) ----
        poly_coefs = np.polyfit(x_hist, y_hist, deg=6)
        t_dense = np.linspace(0.4, 5.0, 200)
        curve_overfit = axes.plot(
            lambda x: np.clip(np.interp(x, t_dense, np.polyval(poly_coefs, t_dense)), 0.4, 9.2),
            x_range=[0.4, 5.0], color=COLOR_MINT, stroke_width=3.5)
        self.play(Create(curve_overfit), run_time=3.0)
        self.wait(1.0)

        # ---- 99.8% backtest accuracy badge (t 13.0 - 16.5) ----
        badge_train = RoundedRectangle(corner_radius=0.1, width=4.4, height=0.8,
                                       fill_color=COLOR_CARD_BG, fill_opacity=0.95,
                                       stroke_color=COLOR_MINT, stroke_width=2
                                       ).move_to(axes.c2p(7.5, 1.6))
        text_train = CleanText("BACKTEST ACCURACY: 99.8%", weight="BOLD",
                               font_size=16, color=COLOR_MINT).move_to(badge_train)
        self.play(FadeIn(badge_train), Write(text_train), run_time=2.0)
        self.wait(1.5)

        # ---- Emphasize the wiggle (t 16.5 - 19.0) ----
        self.play(Indicate(curve_overfit, color=COLOR_MINT, scale_factor=1.03), run_time=1.5)
        self.wait(1.0)

        # ---- Checkmarks: fits EVERY point (t 19.0 - 22.0) ----
        def make_tick(color):
            a, b, c = LEFT * 0.1 + DOWN * 0.02, ORIGIN + DOWN * 0.12, RIGHT * 0.14 + UP * 0.09
            return VGroup(Line(a, b, color=color, stroke_width=3.5),
                          Line(b, c, color=color, stroke_width=3.5))

        ticks = VGroup(*[make_tick(COLOR_MINT).next_to(dot, UP, buff=0.12) for dot in hist_dots])
        self.play(LaggedStartMap(FadeIn, ticks, lag_ratio=0.15), run_time=2.0)
        self.wait(1.0)

        # ---- Caption (t 22.0 - 25.5) ----
        caption = CleanText("IT MEMORIZED THE NOISE — NOT THE MARKET", weight="BOLD",
                            font_size=19, color=COLOR_WHITE).to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=1.5)
        self.wait(2.0)

        # ---- Final pulse on the badge (t 25.5 - 29.0) ----
        self.play(Circumscribe(badge_train, color=COLOR_MINT, time_width=1.0), run_time=1.5)
        self.wait(2.0)


class OverfittingTrapPart2(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ---- Small badge (t 0.0 - 2.0) ----
        badge_bg = RoundedRectangle(corner_radius=0.15, width=8.0, height=0.95,
                                     fill_color=COLOR_CARD_BG, fill_opacity=0.9,
                                     stroke_color=COLOR_CRIMSON, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("THE LIVE TEST", weight="BOLD",
                                font_size=24, color=COLOR_CRIMSON).move_to(badge_bg)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), run_time=1.5)
        self.wait(0.5)

        # ---- Axes + boundary (t 2.0 - 5.5) ----
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 10, 2],
            x_length=8.8, y_length=4.2,
            axis_config={"color": COLOR_MUTED, "stroke_width": 2},
            tips=True,
        ).shift(DOWN * 0.7)
        divider = DashedLine(axes.c2p(5.0, 0), axes.c2p(5.0, 9.5),
                             color=COLOR_GOLD, stroke_width=2.5)
        hist_label = CleanText("HISTORICAL BACKTEST", weight="BOLD",
                               font_size=15, color=COLOR_MUTED).next_to(axes.c2p(2.2, 9.5), DOWN, buff=0.1)
        live_label = CleanText("LIVE UNSEEN DATA", weight="BOLD",
                               font_size=16, color=COLOR_CRIMSON).next_to(axes.c2p(7.3, 9.5), DOWN, buff=0.1)
        self.play(Create(axes), Create(divider), FadeIn(hist_label), FadeIn(live_label), run_time=2.5)
        self.wait(1.0)

        # ---- Ghost of the overfit curve re-enters (t 5.5 - 8.5) ----
        poly_coefs = np.polyfit(x_hist, y_hist, deg=6)
        t_dense = np.linspace(0.4, 5.0, 200)
        ghost_curve = axes.plot(
            lambda x: np.clip(np.interp(x, t_dense, np.polyval(poly_coefs, t_dense)), 0.4, 9.2),
            x_range=[0.4, 5.0], color=COLOR_MINT, stroke_width=3).set_stroke(opacity=0.55)
        # Position ghost_label below hist_label so there is zero collision
        ghost_label = CleanText("THE 'PERFECT' MODEL", font_size=13,
                                color=COLOR_MINT).next_to(hist_label, DOWN, buff=0.22)
        self.play(Create(ghost_curve), FadeIn(ghost_label), run_time=2.0)
        self.wait(1.0)

        # ---- Actual market path (t 8.5 - 12.0) ----
        rng = np.random.default_rng(np_seed)
        x_live = np.linspace(5.0, 9.5, 60)
        y_live = 5.5 + 1.2 * np.sin(x_live * 1.5) + rng.normal(0, 0.3, len(x_live))
        y_live = np.clip(y_live, 1.0, 8.5)
        curve_live = axes.plot(lambda x: np.interp(x, x_live, y_live),
                               x_range=[5.0, 9.5], color=COLOR_MUTED, stroke_width=2.5)
        real_label = CleanText("ACTUAL MARKET", font_size=13,
                               color=COLOR_MUTED).next_to(axes.c2p(8.6, 6.6), UP, buff=0.12)
        self.play(Create(curve_live), FadeIn(real_label), run_time=2.5)
        self.wait(1.0)

        # ---- Model extrapolation crosses the boundary (t 12.0 - 16.0) ----
        x_pred = np.linspace(5.0, 9.2, 60)
        y_pred = np.clip(np.polyval(poly_coefs, x_pred) - (x_pred - 5.0) ** 2.2 * 1.8, 0.4, 9.5)
        curve_pred = axes.plot(lambda x: np.interp(x, x_pred, y_pred),
                               x_range=[5.0, 9.2], color=COLOR_CRIMSON, stroke_width=4)
        self.play(Create(curve_pred), run_time=3.0)
        self.wait(1.0)

        # ---- Catastrophic divergence crash (t 16.0 - 19.5) ----
        crash_dot = Dot(axes.c2p(9.0, y_pred[-1] + 0.4), color=COLOR_CRIMSON, radius=0.13)
        self.play(Create(crash_dot), Flash(axes.c2p(8.8, 0.8), color=COLOR_CRIMSON,
                                            flash_radius=0.7, line_length=0.35, num_lines=14),
                  run_time=2.5)
        self.wait(1.0)

        # ---- OVERFITTED TO NOISE stamp (t 19.5 - 23.5) ----
        stamp_text = CleanText("OVERFITTED TO NOISE", weight="BOLD",
                               font_size=30, color=COLOR_CRIMSON)
        stamp = VGroup(stamp_text, SurroundingRectangle(
            stamp_text, corner_radius=0.08, color=COLOR_CRIMSON, stroke_width=4, buff=0.18))
        stamp.rotate(-0.12).move_to(axes.c2p(7.3, 5.2))
        self.play(FadeIn(stamp, scale=1.6), run_time=2.0)
        self.wait(2.0)

        # ---- Live loss card (t 23.5 - 27.5) ----
        badge_fail = RoundedRectangle(corner_radius=0.1, width=4.6, height=0.8,
                                      fill_color=COLOR_CARD_BG, fill_opacity=0.95,
                                      stroke_color=COLOR_CRIMSON, stroke_width=2
                                      ).move_to(axes.c2p(2.5, 1.6))
        text_fail = CleanText("LIVE RESULT: CATASTROPHIC LOSS", weight="BOLD",
                              font_size=16, color=COLOR_CRIMSON).move_to(badge_fail)
        self.play(FadeIn(badge_fail), Write(text_fail), run_time=2.0)
        self.wait(2.0)

        # ---- Verdict caption (t 27.5 - 33.0) ----
        caption = CleanText("PERFECT ON PAPER. BROKEN IN REALITY.", weight="BOLD",
                            font_size=20, color=COLOR_WHITE).to_edge(DOWN, buff=0.3)
        self.play(Write(caption), run_time=1.5)
        self.wait(4.0)
