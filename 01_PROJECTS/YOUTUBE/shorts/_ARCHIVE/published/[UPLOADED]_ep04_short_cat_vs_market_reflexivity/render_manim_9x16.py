import os
import sys
import numpy as np
from manim import *
import matplotlib.font_manager as fm

# Register Nohemi fonts
for f in ["assets/fonts/Nohemi-Bold.ttf", "assets/fonts/Nohemi-Medium.ttf", "assets/fonts/Nohemi-Regular.ttf"]:
    if os.path.exists(f):
        fm.fontManager.addfont(f)

# Institutional Data Intelligence Palette
COLOR_BG = "#202322"         # Raisin Black
COLOR_SURFACE = "#191C1B"    # Dark surface
COLOR_CHROME = "#233D4C"     # Charcoal Slate (lines & borders only)
COLOR_TEXT = "#E6EDF3"       # Off-White
COLOR_LIME = "#C3D809"       # Power Lime
COLOR_PUMPKIN = "#FD802E"    # Pumpkin
COLOR_MUTED = "#8B9A98"      # Mid-tone gray

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60

def CleanText(text, font="Nohemi", font_size=24, **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    # Never pass weight="BOLD" on Nohemi to prevent Pango faux-bold glyph scattering
    kwargs.pop("weight", None)
    return Text(text, font=font, font_size=ref_size, **kwargs).scale(scale_factor)

def make_glow_box(width, height, stroke_color, fill_color=COLOR_SURFACE, fill_opacity=0.98, radius=0.18):
    box = RoundedRectangle(
        corner_radius=radius, width=width, height=height,
        fill_color=fill_color, fill_opacity=fill_opacity,
        stroke_color=stroke_color, stroke_width=3.0
    )
    # Outer soft glow layer
    glow = RoundedRectangle(
        corner_radius=radius, width=width + 0.18, height=height + 0.18,
        fill_opacity=0, stroke_color=stroke_color, stroke_width=7.5, stroke_opacity=0.4
    )
    return VGroup(glow, box)

def make_glow_badge(text, color, font_size=20, y_pos=0.0):
    txt = CleanText(text, font_size=font_size, color=color)
    box = RoundedRectangle(
        corner_radius=0.14, width=txt.width + 0.6, height=txt.height + 0.35,
        fill_color="#151817", fill_opacity=0.98,
        stroke_color=color, stroke_width=2.5
    )
    glow = RoundedRectangle(
        corner_radius=0.14, width=txt.width + 0.76, height=txt.height + 0.5,
        fill_opacity=0, stroke_color=color, stroke_width=6.5, stroke_opacity=0.5
    )
    return VGroup(glow, box, txt).shift(UP * y_pos)

class ReflexivityGlowShort(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Continuous high-tech background grid without harsh center crosshairs
        grid = NumberPlane(
            x_range=[-4.5, 4.5, 1], y_range=[-8, 8, 1],
            background_line_style={"stroke_color": COLOR_CHROME, "stroke_width": 1, "stroke_opacity": 0.3},
            axis_config={"stroke_opacity": 0}
        )
        self.add(grid)

        SHORT_DIR = r"E:\Agentic Workspaces\ClaudeCode\01_PROJECTS\YOUTUBE\shorts\[IN_PROGRESS 2026-09-23]_ep04_short_cat_vs_market_reflexivity"
        TM_DIR = os.path.join(SHORT_DIR, "TIMELINE_MEDIA")
        img1_path = os.path.join(TM_DIR, "02_00m00s_to_00m04s_image_01_computer_vision_cat_glow.png")
        img2_path = os.path.join(TM_DIR, "02_00m14s_to_00m18s_image_02_algorithmic_buying_pressure_glow.png")
        img3_path = os.path.join(TM_DIR, "02_00m26s_to_00m30s_image_03_signal_erased_self_destruct_glow.png")

        # =========================================================================
        # BEAT 1: HOOK & IMAGE 1 (0.0s - 4.8s = 4.8s)
        # "If a neural network learns to identify a cat, the cat does not change its shape..."
        # =========================================================================
        top_hook = make_glow_box(width=8.0, height=1.15, stroke_color=COLOR_LIME).to_edge(UP, buff=0.95)
        txt_hook = CleanText("THE REFLEXIVITY TRAP IN AI", font_size=23, color=COLOR_LIME).move_to(top_hook[1])

        # Image 1 (Computer vision object detection) as an animated framing
        img1 = ImageMobject(img1_path).set_height(9.5).shift(DOWN * 0.4)
        img1_frame = make_glow_box(width=img1.width + 0.1, height=img1.height + 0.1, stroke_color=COLOR_LIME).move_to(img1)

        pop1 = make_glow_badge("OBJECT: INVARIANT", COLOR_LIME, font_size=20, y_pos=1.6)

        self.play(FadeIn(top_hook), FadeIn(txt_hook), run_time=0.8)
        self.play(FadeIn(img1_frame), FadeIn(img1), run_time=1.2)
        # Continuous camera push on Image 1 with keyword pop
        self.play(
            img1.animate.scale(1.03),
            img1_frame.animate.scale(1.03),
            FadeIn(pop1, scale=0.8),
            run_time=1.4
        )
        self.play(
            img1.animate.scale(1.03),
            img1_frame.animate.scale(1.03),
            FadeOut(pop1, scale=1.1),
            run_time=1.4
        )

        # =========================================================================
        # BEAT 2: SPLIT COMPARISON (4.8s - 13.5s = 8.7s)
        # "...because the computer got good at recognizing it. But the financial market is a competitive zero-sum game..."
        # =========================================================================
        self.play(FadeOut(img1), FadeOut(img1_frame), run_time=0.8)

        # Left Card (Stationary)
        card_cat = make_glow_box(width=8.0, height=3.5, stroke_color=COLOR_LIME).shift(UP * 3.4)
        title_cat = CleanText("1. COMPUTER VISION (STATIONARY)", font_size=21, color=COLOR_LIME).next_to(card_cat[1].get_top(), DOWN, buff=0.35)
        sub_cat = CleanText("Physical objects never mutate when recognized.", font_size=16, color=COLOR_TEXT).next_to(title_cat, DOWN, buff=0.25)

        # Pixel grid inside Left Card
        grid_vg = VGroup()
        for r in range(3):
            for c in range(6):
                sq = Square(side_length=0.36, stroke_color=COLOR_LIME, stroke_width=1.5,
                            fill_color=COLOR_LIME, fill_opacity=0.2 if (r + c) % 2 == 0 else 0.5)
                sq.move_to(card_cat[1].get_center() + RIGHT * (c - 2.5) * 0.44 + DOWN * (r - 0.5) * 0.44 + DOWN * 0.35)
                grid_vg.add(sq)

        # Right Card (Reflexive)
        card_mkt = make_glow_box(width=8.0, height=4.5, stroke_color=COLOR_PUMPKIN).shift(DOWN * 1.5)
        title_mkt = CleanText("2. FINANCIAL MARKET (REFLEXIVE)", font_size=21, color=COLOR_PUMPKIN).next_to(card_mkt[1].get_top(), DOWN, buff=0.35)
        sub_mkt = CleanText("A competitive zero-sum game of algorithms.", font_size=16, color=COLOR_TEXT).next_to(title_mkt, DOWN, buff=0.2)

        # Market axes inside Right Card
        axes_mkt = Axes(
            x_range=[0, 6, 1], y_range=[0, 8, 2],
            x_length=6.4, y_length=2.2,
            axis_config={"color": COLOR_CHROME, "stroke_width": 2},
            tips=False
        ).move_to(card_mkt[1].get_center() + DOWN * 0.45)

        curve_mkt = axes_mkt.plot(lambda x: 3.5 + np.sin(x * 2.2) * 1.5, color=COLOR_PUMPKIN, stroke_width=3.5)
        pop2 = make_glow_badge("ZERO-SUM ARENA", COLOR_PUMPKIN, font_size=22, y_pos=0.1)

        self.play(FadeIn(card_cat), FadeIn(title_cat), FadeIn(sub_cat), Create(grid_vg), run_time=1.8)
        self.play(FadeIn(card_mkt), FadeIn(title_mkt), FadeIn(sub_mkt), Create(axes_mkt), Create(curve_mkt), run_time=2.2)
        # Continuous wave motion + keyword pop
        self.play(
            curve_mkt.animate.become(
                axes_mkt.plot(lambda x: 3.5 + np.sin(x * 2.2 + 1.0) * 1.6, color=COLOR_PUMPKIN, stroke_width=3.5)
            ),
            FadeIn(pop2, scale=0.8),
            run_time=1.8
        )
        self.play(
            curve_mkt.animate.become(
                axes_mkt.plot(lambda x: 3.5 + np.sin(x * 2.2 + 2.0) * 1.6, color=COLOR_PUMPKIN, stroke_width=3.5)
            ),
            FadeOut(pop2, scale=1.1),
            run_time=2.1
        )

        # =========================================================================
        # BEAT 3: BUYING PRESSURE & IMAGE 2 (13.5s - 22.0s = 8.5s)
        # "If an AI discovers a genuine profitable pattern that says Apple will rise tomorrow..."
        # =========================================================================
        self.play(
            FadeOut(card_cat), FadeOut(title_cat), FadeOut(sub_cat), FadeOut(grid_vg),
            FadeOut(card_mkt), FadeOut(title_mkt), FadeOut(sub_mkt), FadeOut(axes_mkt), FadeOut(curve_mkt),
            run_time=0.8
        )

        title_pressure = CleanText("CAPITAL FLOODING THE SIGNAL", font_size=22, color=COLOR_PUMPKIN).move_to(top_hook[1])
        self.play(Transform(txt_hook, title_pressure), top_hook[0].animate.set_stroke(COLOR_PUMPKIN), run_time=0.7)

        # Image 2 (Order book depth & buying pressure)
        img2 = ImageMobject(img2_path).set_height(9.5).shift(DOWN * 0.4)
        img2_frame = make_glow_box(width=img2.width + 0.1, height=img2.height + 0.1, stroke_color=COLOR_PUMPKIN).move_to(img2)

        pop3 = make_glow_badge("ALGORITHMIC SWARM", COLOR_LIME, font_size=21, y_pos=1.8)
        pop4 = make_glow_badge("SIGNAL EXPOSED", COLOR_PUMPKIN, font_size=21, y_pos=1.8)

        self.play(FadeIn(img2_frame), FadeIn(img2), run_time=1.2)
        # Smooth scale push with pulsing keyword pops
        self.play(
            img2.animate.scale(1.03),
            img2_frame.animate.scale(1.03),
            FadeIn(pop3, scale=0.8),
            run_time=1.5
        )
        self.play(
            FadeOut(pop3),
            FadeIn(pop4, scale=0.8),
            run_time=1.5
        )
        self.play(
            img2.animate.scale(1.03),
            img2_frame.animate.scale(1.03),
            FadeOut(pop4, scale=1.1),
            run_time=2.8
        )

        # =========================================================================
        # BEAT 4: THE ERASURE COLLISION (22.0s - 26.5s = 4.5s)
        # "...their own buying pressure instantly drives the price up today."
        # =========================================================================
        self.play(FadeOut(img2), FadeOut(img2_frame), run_time=0.7)

        collision_box = make_glow_box(width=8.0, height=7.2, stroke_color=COLOR_PUMPKIN).shift(UP * 0.2)
        axes_col = Axes(
            x_range=[0, 8, 1], y_range=[0, 10, 2],
            x_length=7.0, y_length=4.5,
            axis_config={"color": COLOR_CHROME, "stroke_width": 2},
            tips=True
        ).move_to(collision_box[1].get_center() + DOWN * 0.4)

        # Predicted path (Power Lime dashed)
        pred_line = DashedLine(axes_col.c2p(1, 3), axes_col.c2p(7, 8.5), color=COLOR_LIME, stroke_width=3.5)
        lbl_pred = CleanText("AI PREDICTION (TOMORROW)", font_size=15, color=COLOR_LIME).move_to(axes_col.c2p(5.6, 9.4))

        # Real price spikes up TODAY (Pumpkin solid)
        actual_line = axes_col.plot(lambda x: 3.0 + 4.5 / (1.0 + np.exp(-3.0 * (x - 2.5))), color=COLOR_PUMPKIN, stroke_width=4.5)
        lbl_actual = CleanText("PRICE SURGES TODAY", font_size=16, color=COLOR_PUMPKIN).move_to(axes_col.c2p(2.2, 8.5))

        stamp_erased = make_glow_box(width=7.4, height=1.3, stroke_color=COLOR_PUMPKIN, fill_color=COLOR_BG, fill_opacity=0.95).shift(DOWN * 2.8)
        txt_erased = CleanText("PREDICTION ERASES THE PATTERN", font_size=19, color=COLOR_PUMPKIN).move_to(stamp_erased[1])

        self.play(FadeIn(collision_box), Create(axes_col), Create(pred_line), FadeIn(lbl_pred), run_time=1.3)
        self.play(Create(actual_line), FadeIn(lbl_actual), FadeIn(stamp_erased), FadeIn(txt_erased), run_time=1.5)
        self.wait(1.0)

        # =========================================================================
        # BEAT 5: THE SELF-DESTRUCTION VERDICT (26.5s - 32.25s = 5.75s)
        # "The prediction itself erases the pattern. The moment an edge becomes predictable, it self-destructs."
        # =========================================================================
        self.play(
            FadeOut(collision_box), FadeOut(axes_col), FadeOut(pred_line), FadeOut(lbl_pred),
            FadeOut(actual_line), FadeOut(lbl_actual), FadeOut(stamp_erased), FadeOut(txt_erased),
            FadeOut(top_hook), FadeOut(txt_hook),
            run_time=0.8
        )

        # Image 3 (Prediction erases pattern / self-destruction)
        img3 = ImageMobject(img3_path).set_height(9.8).shift(UP * 0.2)
        img3_frame = make_glow_box(width=img3.width + 0.1, height=img3.height + 0.1, stroke_color=COLOR_PUMPKIN).move_to(img3)

        logo_outro = CleanText("QUANTROVE", font_size=20, color=COLOR_TEXT).to_edge(DOWN, buff=1.0)
        pop5 = make_glow_badge("ALPHA = 0.0%", COLOR_PUMPKIN, font_size=24, y_pos=1.4)

        self.play(FadeIn(img3_frame), FadeIn(img3), FadeIn(logo_outro), run_time=1.2)
        self.play(
            img3.animate.scale(1.03),
            img3_frame.animate.scale(1.03),
            FadeIn(pop5, scale=0.8),
            run_time=1.8
        )
        self.play(
            img3.animate.scale(1.02),
            img3_frame.animate.scale(1.02),
            FadeOut(pop5, scale=1.1),
            run_time=1.95
        )
