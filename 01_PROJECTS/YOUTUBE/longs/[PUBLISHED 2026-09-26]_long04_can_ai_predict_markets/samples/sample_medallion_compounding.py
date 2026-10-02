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
COLOR_GRID = "#1E293B"

def CleanText(text, font="Segoe UI", font_size=24, **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    return Text(text, font=font, font_size=ref_size, **kwargs).scale(scale_factor)

class MedallionCompoundingSample(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # ---- 1. Header Telemetry Card (0.0s - 1.5s) ----
        top_card = RoundedRectangle(
            corner_radius=0.12, width=13.0, height=0.9,
            fill_color=COLOR_CARD_BG, fill_opacity=0.85,
            stroke_color=COLOR_GOLD, stroke_width=1.5
        ).to_edge(UP, buff=0.3)
        
        tag = CleanText("QUANTITATIVE BENCHMARK", font_size=13, color=COLOR_GOLD).next_to(top_card.get_left(), RIGHT, buff=0.4)
        title = CleanText("THE SIMONS COMPOUNDING PARADOX (1988 – 2024)", font_size=18, color=COLOR_WHITE).next_to(tag, RIGHT, buff=0.5)
        edge_badge = CleanText("+66.1% ANNUAL RETURN", font_size=13, color=COLOR_MINT).next_to(top_card.get_right(), LEFT, buff=0.4)

        self.play(
            FadeIn(top_card, shift=DOWN * 0.2),
            FadeIn(tag), FadeIn(title), FadeIn(edge_badge),
            run_time=1.0
        )

        # ---- 2. Logarithmic Coordinate System (1.0s - 2.5s) ----
        # X: Year 1988 (0) to 2024 (36)
        # Y: Log10 Wealth: 3 ($1K) to 8 ($100M)
        axes = Axes(
            x_range=[0, 36, 6],
            y_range=[3, 8, 1],
            x_length=8.2,
            y_length=4.5,
            axis_config={"color": COLOR_MUTED, "stroke_width": 1.5},
            tips=False
        ).to_corner(DL, buff=0.7).shift(UP * 0.15 + RIGHT * 0.2)

        # X ticks labels
        x_years = [1988, 1994, 2000, 2006, 2012, 2018, 2024]
        x_labels = VGroup()
        for idx, yr in enumerate(x_years):
            lbl = CleanText(str(yr), font_size=13, color=COLOR_MUTED)
            lbl.next_to(axes.c2p(idx * 6, 3), DOWN, buff=0.15)
            x_labels.add(lbl)

        # Y ticks labels (Wealth Milestones)
        y_vals = [
            (3, "$1K"),
            (4, "$10K"),
            (5, "$100K"),
            (6, "$1M"),
            (7, "$10M"),
            (7.62, "$42M"),
        ]
        y_labels = VGroup()
        grid_lines = VGroup()
        for y_log, y_txt in y_vals:
            lbl = CleanText(y_txt, font_size=13, color=COLOR_GOLD if y_log >= 7.6 else COLOR_MUTED)
            lbl.next_to(axes.c2p(0, y_log), LEFT, buff=0.15)
            y_labels.add(lbl)
            
            # Horizontal dashed gridline
            gl = DashedLine(axes.c2p(0, y_log), axes.c2p(36, y_log), dash_length=0.08, color=COLOR_GRID, stroke_width=1)
            grid_lines.add(gl)

        self.play(
            Create(axes),
            FadeIn(grid_lines),
            FadeIn(x_labels),
            FadeIn(y_labels),
            run_time=1.2
        )

        # ---- 3. Live Metrics Sidebar Card (Right Side) ----
        side_card = RoundedRectangle(
            corner_radius=0.15, width=3.8, height=4.5,
            fill_color=COLOR_CARD_BG, fill_opacity=0.9,
            stroke_color=COLOR_CYAN, stroke_width=1.5
        ).to_corner(DR, buff=0.7).shift(UP * 0.15)

        side_title = CleanText("INITIAL CAPITAL", font_size=13, color=COLOR_MUTED).next_to(side_card.get_top(), DOWN, buff=0.25)
        init_val = CleanText("$1,000 (1988)", font_size=20, color=COLOR_WHITE).next_to(side_title, DOWN, buff=0.08)

        div1 = Line(side_card.get_left() + RIGHT * 0.3, side_card.get_right() + LEFT * 0.3, color=COLOR_GRID, stroke_width=1).next_to(init_val, DOWN, buff=0.15)

        sp_hdr = CleanText("S&P 500 BENCHMARK", font_size=12, color=COLOR_MUTED).next_to(div1, DOWN, buff=0.15)
        sp_ret = CleanText("+10.2% / YR ➔ $32,400", font_size=15, color="#94A3B8").next_to(sp_hdr, DOWN, buff=0.06)

        div2 = Line(side_card.get_left() + RIGHT * 0.3, side_card.get_right() + LEFT * 0.3, color=COLOR_GRID, stroke_width=1).next_to(sp_ret, DOWN, buff=0.15)

        med_hdr = CleanText("MEDALLION FUND (SIMONS)", font_size=12, color=COLOR_GOLD).next_to(div2, DOWN, buff=0.15)
        med_ret = CleanText("+66.1% / YR AVERAGE", font_size=15, color=COLOR_GOLD).next_to(med_hdr, DOWN, buff=0.06)
        
        mult_box = RoundedRectangle(
            corner_radius=0.08, width=3.2, height=0.65,
            fill_color="#064E3B", fill_opacity=0.6,
            stroke_color=COLOR_MINT, stroke_width=1.5
        ).next_to(med_ret, DOWN, buff=0.2)
        mult_txt = CleanText("42,000x MULTIPLIER", font_size=16, color=COLOR_MINT).move_to(mult_box.get_center())

        self.play(
            FadeIn(side_card, shift=LEFT * 0.3),
            FadeIn(side_title), FadeIn(init_val),
            Create(div1),
            FadeIn(sp_hdr), FadeIn(sp_ret),
            Create(div2),
            FadeIn(med_hdr), FadeIn(med_ret),
            FadeIn(mult_box), FadeIn(mult_txt),
            run_time=1.0
        )

        # ---- 4. Plot S&P 500 Growth (2.5s - 4.5s) ----
        # S&P grows from $1K to $32.4K (log10 goes from 3.0 to 4.51)
        def sp_func(t):
            # t in [0, 36]
            wealth = 1000.0 * ((1.0 + 0.102) ** t)
            return np.log10(wealth)

        sp_curve = axes.plot(sp_func, x_range=[0, 36], color="#64748B", stroke_width=3)
        sp_tag = CleanText("S&P 500: $32K", font_size=13, color="#94A3B8").next_to(axes.c2p(36, 4.51), UP + LEFT, buff=0.1)

        self.play(
            Create(sp_curve),
            run_time=1.8,
            rate_func=linear
        )
        self.play(FadeIn(sp_tag), run_time=0.4)

        # ---- 5. Plot Medallion Fund Astronomical Surge (4.5s - 8.5s) ----
        # Medallion compounds from $1K to $42M (log10 from 3.0 to 7.623)
        # Using a slight realistic sigmoid inflection to capture the 90s acceleration
        def med_func(t):
            ratio = t / 36.0
            log_val = 3.0 + 4.623 * (ratio ** 1.08)
            return log_val

        med_curve = axes.plot(med_func, x_range=[0, 36], color=COLOR_GOLD, stroke_width=4.5)
        
        # Glowing halo behind medallion line
        med_glow = axes.plot(med_func, x_range=[0, 36], color=COLOR_MINT, stroke_width=8, stroke_opacity=0.35)

        # Dot at the tip
        tip_dot = Dot(color=COLOR_MINT, radius=0.1).move_to(axes.c2p(0, 3))

        # Dynamic Value Tracker Label
        val_tracker = ValueTracker(1000)
        
        live_label = always_redraw(lambda: 
            CleanText(
                f"${int(val_tracker.get_value()):,}" if val_tracker.get_value() < 1000000 
                else f"${val_tracker.get_value() / 1e6:.1f}M",
                font_size=15, color=COLOR_GOLD
            ).next_to(tip_dot, UP + LEFT, buff=0.15)
        )

        self.add(tip_dot, live_label)

        def update_dot(mob, alpha):
            t = alpha * 36.0
            y = med_func(t)
            mob.move_to(axes.c2p(t, y))

        self.play(
            Create(med_glow),
            Create(med_curve),
            UpdateFromAlphaFunc(tip_dot, update_dot),
            val_tracker.animate.set_value(42000000),
            run_time=3.5,
            rate_func=smooth
        )

        # ---- 6. Final Accent Slam & Milestone Badge (8.5s - 10.0s) ----
        peak_badge = RoundedRectangle(
            corner_radius=0.1, width=3.4, height=0.75,
            fill_color=COLOR_CARD_BG, fill_opacity=0.95,
            stroke_color=COLOR_GOLD, stroke_width=2
        ).next_to(axes.c2p(36, 7.62), LEFT, buff=0.3)
        
        peak_txt = CleanText("$42,000,000+", font_size=18, color=COLOR_GOLD).next_to(peak_badge.get_top(), DOWN, buff=0.1)
        peak_sub = CleanText("BANNED FINANCE BACKGROUND", font_size=11, color=COLOR_CRIMSON).next_to(peak_txt, DOWN, buff=0.06)

        # Horizontal dashed guide to Y axis $42M
        h_line = DashedLine(axes.c2p(0, 7.62), axes.c2p(36, 7.62), dash_length=0.06, color=COLOR_GOLD, stroke_width=1.5)

        self.play(
            Create(h_line),
            FadeIn(peak_badge, scale=1.1),
            FadeIn(peak_txt),
            FadeIn(peak_sub),
            Flash(axes.c2p(36, 7.62), color=COLOR_GOLD, line_length=0.25, flash_radius=0.4),
            run_time=1.0
        )
        self.wait(0.5)

if __name__ == "__main__":
    pass
