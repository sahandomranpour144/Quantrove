from manim import *
import numpy as np

config.background_color = "#121212"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class Crash1929Scene(Scene):
    def construct(self):
        # Target total duration: Exactly 29.0 seconds

        # Colors
        GOLD = "#F59E0B"
        RED = "#EF4444"
        GREEN = "#10B981"
        CYAN = "#06B6D4"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#1A1F2C"

        # ---------------------------------------------------------
        # 1. Title & Header (0.0s - 3.0s) -> 3.0s
        # ---------------------------------------------------------
        title = Text("1929: THE GREAT CRASH", font_size=38, font="Segoe UI", weight=BOLD, color=GOLD)
        subtitle = Text("FIRE #1: UNCHECKED MARGIN DEBT & THE 3-YEAR COLLAPSE", font_size=20, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.5)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(2.0)

        # ---------------------------------------------------------
        # 2. The Roaring 20s Bull Market (3.0s - 7.5s) -> 4.5s
        # ---------------------------------------------------------
        axes_20s = Axes(
            x_range=[1921, 1930, 1],
            y_range=[0, 420, 100],
            x_length=9,
            y_length=4.2,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        x_labels_20s = VGroup(
            Text("1921", font_size=16, color=MUTED).next_to(axes_20s.c2p(1921, 0), DOWN, buff=0.15),
            Text("1925", font_size=16, color=MUTED).next_to(axes_20s.c2p(1925, 0), DOWN, buff=0.15),
            Text("1929", font_size=16, color=MUTED).next_to(axes_20s.c2p(1929, 0), DOWN, buff=0.15),
        )

        # Roaring 20s curve
        curve_20s = axes_20s.plot(
            lambda x: 75 * np.exp(0.185 * (x - 1921)),
            x_range=[1921, 1929.7],
            color=GOLD,
            stroke_width=4
        )

        stat_badge_20s = RoundedRectangle(corner_radius=0.15, height=1.0, width=4.0, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=GOLD, stroke_width=1.5).to_corner(UL, buff=1.2)
        stat_text_20s = VGroup(
            Text("THE ROARING TWENTIES", font_size=16, font="Segoe UI", weight=BOLD, color=GOLD),
            Text("+20% Annual Gains (75 -> 381 pts)", font_size=14, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(stat_badge_20s.get_center())

        self.play(
            FadeIn(axes_20s),
            FadeIn(x_labels_20s),
            FadeIn(stat_badge_20s),
            FadeIn(stat_text_20s),
            Create(curve_20s),
            run_time=2.5
        )
        self.wait(2.0)

        # ---------------------------------------------------------
        # 3. Margin Buying Structure & Liquidation (7.5s - 13.0s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(axes_20s),
            FadeOut(x_labels_20s),
            FadeOut(curve_20s),
            FadeOut(stat_badge_20s),
            FadeOut(stat_text_20s),
            run_time=0.8
        )

        margin_title = Text("Margin Buying Structure (10:1 Leverage)", font_size=24, font="Segoe UI", weight=BOLD, color=CYAN).shift(UP * 1.8)

        # Bar 1: Normal
        box_equity = Rectangle(width=2.4, height=0.4, fill_color=GREEN, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1).shift(LEFT * 2.5 + DOWN * 1.2)
        box_debt = Rectangle(width=2.4, height=3.6, fill_color=GOLD, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1).next_to(box_equity, UP, buff=0)
        lbl_eq = Text("$10 Cash (Equity)", font_size=14, font="Segoe UI", color=WHITE).move_to(box_equity.get_center())
        lbl_db = Text("$90 Loan (Debt)", font_size=16, font="Segoe UI", weight=BOLD, color="#121212").move_to(box_debt.get_center())
        lbl_bar1 = Text("Normal: $100 Stock", font_size=16, font="Segoe UI", color=WHITE).next_to(box_equity, DOWN, buff=0.2)

        # Bar 2: 10% Drop Wipeout
        box_debt_wipe = Rectangle(width=2.4, height=3.6, fill_color=GOLD, fill_opacity=0.9, stroke_color=WHITE, stroke_width=1).shift(RIGHT * 2.5 + DOWN * 0.8)
        lbl_db_wipe = Text("$90 Debt Owed", font_size=16, font="Segoe UI", weight=BOLD, color="#121212").move_to(box_debt_wipe.get_center())
        lbl_bar2 = Text("10% Drop = 100% Wipeout", font_size=16, font="Segoe UI", color=RED).next_to(box_debt_wipe, DOWN, buff=0.6)

        alert_badge = RoundedRectangle(corner_radius=0.15, height=0.7, width=4.5, fill_color=RED, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2).next_to(box_debt_wipe, UP, buff=0.3)
        alert_text = Text("MARGIN CALL TRIGGERED", font_size=16, font="Segoe UI", weight=BOLD, color=WHITE).move_to(alert_badge.get_center())

        self.play(
            FadeIn(margin_title),
            Create(box_equity), Create(box_debt), FadeIn(lbl_eq), FadeIn(lbl_db), FadeIn(lbl_bar1),
            run_time=1.5
        )
        self.play(
            Create(box_debt_wipe), FadeIn(lbl_db_wipe), FadeIn(lbl_bar2),
            FadeIn(alert_badge, shift=UP), FadeIn(alert_text, shift=UP),
            run_time=1.5
        )
        self.wait(1.7)

        # ---------------------------------------------------------
        # 4. October 1929 4-Day Collapse (-25%) (13.0s - 18.5s) -> 5.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(margin_title), FadeOut(box_equity), FadeOut(box_debt), FadeOut(lbl_eq), FadeOut(lbl_db), FadeOut(lbl_bar1),
            FadeOut(box_debt_wipe), FadeOut(lbl_db_wipe), FadeOut(lbl_bar2), FadeOut(alert_badge), FadeOut(alert_text),
            run_time=0.8
        )

        axes_oct = Axes(
            x_range=[0, 4, 1],
            y_range=[200, 320, 40],
            x_length=8.5,
            y_length=3.8,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        oct_labels = ["Oct 23", "Oct 24 (Thu)", "Oct 25", "Oct 28 (Mon)", "Oct 29 (Tue)"]
        oct_lbl_group = VGroup(*[
            Text(oct_labels[i], font_size=14, color=MUTED).next_to(axes_oct.c2p(i, 200), DOWN, buff=0.15)
            for i in range(5)
        ])

        oct_pts = [axes_oct.c2p(i, val) for i, val in enumerate([305.8, 299.4, 301.2, 260.6, 230.1])]
        oct_curve = VMobject(color=RED, stroke_width=4.5)
        oct_curve.set_points_as_corners(oct_pts)

        badge_4day = RoundedRectangle(corner_radius=0.15, height=0.9, width=4.5, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=RED, stroke_width=2).to_corner(UR, buff=1.2)
        text_4day = VGroup(
            Text("BLACK THURSDAY - TUESDAY", font_size=15, font="Segoe UI", weight=BOLD, color=RED),
            Text("4-Day Panic Drop: -25%", font_size=14, color=WHITE)
        ).arrange(DOWN, buff=0.1).move_to(badge_4day.get_center())

        self.play(
            FadeIn(axes_oct), FadeIn(oct_lbl_group),
            Create(oct_curve), FadeIn(badge_4day), FadeIn(text_4day),
            run_time=2.2
        )
        self.wait(2.5)

        # ---------------------------------------------------------
        # 5. 1929 - 1932 Full 3-Year Collapse (-89%) & Bank Runs (18.5s - 24.5s) -> 6.0s
        # ---------------------------------------------------------
        self.play(
            FadeOut(axes_oct), FadeOut(oct_lbl_group), FadeOut(oct_curve), FadeOut(badge_4day), FadeOut(text_4day),
            run_time=0.8
        )

        axes_3yr = Axes(
            x_range=[1929, 1933, 1],
            y_range=[0, 400, 100],
            x_length=9,
            y_length=4.0,
            axis_config={"color": MUTED, "stroke_width": 2},
        ).shift(DOWN * 0.4)

        labels_3yr = VGroup(
            Text("1929 (Peak)", font_size=15, color=GREEN).next_to(axes_3yr.c2p(1929, 381), UP, buff=0.1),
            Text("1932 (Trough)", font_size=15, color=RED).next_to(axes_3yr.c2p(1932.5, 41), DOWN, buff=0.1),
        )

        curve_3yr = axes_3yr.plot(
            lambda x: 381.17 * (1 - 0.892 * ((x - 1929) / 3.5)**0.85),
            x_range=[1929, 1932.5],
            color=RED,
            stroke_width=4.5
        )

        bank_run_box = RoundedRectangle(corner_radius=0.15, height=1.2, width=5.2, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=GOLD, stroke_width=2).to_corner(UL, buff=1.2)
        bank_run_text = VGroup(
            Text("THE REAL DISASTER: 1929 - 1932", font_size=15, font="Segoe UI", weight=BOLD, color=GOLD),
            Text("Dow Dropped -89% Over 3 Years", font_size=14, color=WHITE),
            Text("Panic Selling Triggered Systemic Bank Runs", font_size=12, color=MUTED)
        ).arrange(DOWN, buff=0.08).move_to(bank_run_box.get_center())

        self.play(
            FadeIn(axes_3yr), Create(curve_3yr), FadeIn(labels_3yr),
            FadeIn(bank_run_box), FadeIn(bank_run_text),
            run_time=2.5
        )
        self.wait(2.7)

        # ---------------------------------------------------------
        # 6. Conclusion Summary Card & Pad to 29.0s (24.5s - 29.0s) -> 4.5s
        # ---------------------------------------------------------
        self.play(
            FadeOut(axes_3yr), FadeOut(curve_3yr), FadeOut(labels_3yr),
            FadeOut(bank_run_box), FadeOut(bank_run_text), FadeOut(header_group),
            run_time=0.8
        )

        summary_card = RoundedRectangle(corner_radius=0.25, height=4.2, width=9.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=GOLD, stroke_width=3)
        summary_content = VGroup(
            Text("1929'S LESSON", font_size=28, font="Segoe UI", weight=BOLD, color=GOLD),
            Text("Excessive Confidence + 10:1 Borrowed Money", font_size=20, font="Segoe UI", weight=BOLD, color=WHITE),
            Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=MUTED, stroke_width=1),
            Text("• 4-Day Panic: -25% Drop in Dow Jones\n• 3-Year Total Drawdown: -89.2% (1929 - 1932)\n• Recovery Timeline: ~25 Years to Reach Previous Highs", font_size=16, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.2).move_to(summary_card.get_center())

        self.play(FadeIn(summary_card, scale=0.95), FadeIn(summary_content), run_time=1.0)
        # Pad remaining time to hit exactly 29.0s
        self.wait(2.7)
