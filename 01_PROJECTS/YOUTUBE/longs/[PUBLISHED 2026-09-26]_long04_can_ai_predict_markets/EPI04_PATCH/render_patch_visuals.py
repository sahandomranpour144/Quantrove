#!/usr/bin/env python3
"""
Render all EP04 Patch Visuals and End-Screen Tail
Executes in a bracket-free scratch directory to avoid Manim regex parsing bugs.
Renders 1080p60 MP4s and installs them directly into EP04_PATCH/visuals/ and EP04_PATCH/.
"""

import os
import sys
import shutil
import subprocess
import tempfile

PATCH_DIR = os.path.dirname(os.path.abspath(__file__))
VISUALS_DIR = os.path.join(PATCH_DIR, "visuals")
os.makedirs(VISUALS_DIR, exist_ok=True)

SCRATCH_DIR = os.path.join(tempfile.gettempdir(), "manim_ep04_patch_scratch")
if os.path.exists(SCRATCH_DIR):
    shutil.rmtree(SCRATCH_DIR)
os.makedirs(SCRATCH_DIR, exist_ok=True)

def ffprobe_info(path):
    cmd = ["ffprobe", "-v", "error", "-show_entries", "stream=width,height,r_frame_rate,duration", "-of", "default=noprint_wrappers=1:nokey=1", path]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    lines = res.stdout.strip().splitlines()
    return {
        "width": int(lines[0]) if len(lines) > 0 else 0,
        "height": int(lines[1]) if len(lines) > 1 else 0,
        "fps": lines[2] if len(lines) > 2 else "",
        "duration": float(lines[3]) if len(lines) > 3 else 0.0
    }

# Scene script definitions
MANIM_CODE = '''
from manim import *
import numpy as np

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

# 1. Hook Visual (12.0s @ 60fps)
# Continuous drawing noisy price line + on-screen text at t=0.0s "Can AI predict the stock market?"
class HookVisualScene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Continuous background grid
        grid = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-4.5, 4.5, 1],
            background_line_style={"stroke_color": COLOR_GRID, "stroke_width": 1, "stroke_opacity": 0.5}
        )
        self.add(grid)

        # Large on-screen text at t=0.0s (6 words)
        hook_box = RoundedRectangle(
            corner_radius=0.15, width=11.5, height=1.5,
            fill_color=COLOR_CARD_BG, fill_opacity=0.92,
            stroke_color=COLOR_CYAN, stroke_width=2.5
        ).shift(UP * 2.2)
        hook_title = CleanText("Can AI predict the stock market?", font_size=38, weight="BOLD", color=COLOR_WHITE).move_to(hook_box)

        self.add(hook_box, hook_title)

        # Coordinate axes for noisy price line
        axes = Axes(
            x_range=[0, 12, 1], y_range=[80, 140, 10],
            x_length=12.0, y_length=4.0,
            axis_config={"color": COLOR_MUTED, "stroke_width": 1.5},
            tips=False
        ).shift(DOWN * 1.2)
        self.add(axes)

        # Deterministic noisy price path across 12s
        np.random.seed(101)
        n_points = 240
        x_vals = np.linspace(0, 12, n_points)
        random_walk = np.cumsum(np.random.randn(n_points) * 1.8)
        trend = 5.0 * np.sin(x_vals * 0.8) + x_vals * 1.2
        y_vals = 100.0 + random_walk + trend

        points = [axes.c2p(x, y) for x, y in zip(x_vals, y_vals)]
        price_curve = VMobject(color=COLOR_MINT, stroke_width=3.5)
        price_curve.set_points_as_corners(points)

        glow_curve = VMobject(color=COLOR_MINT, stroke_width=9, stroke_opacity=0.25)
        glow_curve.set_points_as_corners(points)

        dot = Dot(color=COLOR_GOLD, radius=0.12)
        dot.add_updater(lambda d: d.move_to(price_curve.get_end()))

        # Live ticker label
        ticker_text = always_redraw(lambda: CleanText(
            f"LIVE SIGNAL FEED  |  VOLATILITY: {np.abs(points[-1][1]):.2f}",
            font_size=14, color=COLOR_GOLD
        ).next_to(axes, DOWN, buff=0.25))
        self.add(ticker_text)

        self.play(
            Create(price_curve, rate_func=linear),
            Create(glow_curve, rate_func=linear),
            run_time=12.0
        )


# 2. Simons 21M Counter Scene (10.40s @ 60fps)
class Simons21MCounterScene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Emerald typography: ≈66% / YEAR BEFORE FEES · 1988–2018
        top_badge = RoundedRectangle(
            corner_radius=0.15, width=12.0, height=1.1,
            fill_color=COLOR_CARD_BG, fill_opacity=0.9,
            stroke_color=COLOR_MINT, stroke_width=2
        ).to_edge(UP, buff=0.4)
        top_text = CleanText("≈66% / YEAR BEFORE FEES · 1988–2018", font_size=24, weight="BOLD", color=COLOR_MINT).move_to(top_badge)
        self.play(FadeIn(top_badge, shift=DOWN * 0.3), FadeIn(top_text), run_time=1.4)

        # Counter zoom card
        center_card = RoundedRectangle(
            corner_radius=0.2, width=11.0, height=3.8,
            fill_color=COLOR_CARD_BG, fill_opacity=0.95,
            stroke_color=COLOR_GOLD, stroke_width=2.5
        ).shift(DOWN * 0.4)

        simons_title = CleanText("RENAISSANCE TECHNOLOGIES · MEDALLION FUND", font_size=15, color=COLOR_MUTED).next_to(center_card.get_top(), DOWN, buff=0.3)
        growth_text = CleanText("$1,000 in 1988  →  ≈$21M by 2018", font_size=36, weight="BOLD", color=COLOR_GOLD).next_to(simons_title, DOWN, buff=0.35)
        reported_line = CleanText("(after fees, reported net performance)", font_size=16, color=COLOR_WHITE).next_to(growth_text, DOWN, buff=0.2)
        source_line = CleanText('Source: Zuckerman, "The Man Who Solved the Market"', font_size=13, color=COLOR_MUTED).next_to(reported_line, DOWN, buff=0.25)

        sub_policy = CleanText("DELIBERATELY AVOIDED WALL STREET TRADERS · HIRED SCIENTISTS", font_size=13, weight="BOLD", color=COLOR_CYAN).to_edge(DOWN, buff=0.4)

        self.play(
            FadeIn(center_card, scale=0.9),
            FadeIn(simons_title),
            Write(growth_text),
            FadeIn(reported_line),
            FadeIn(source_line),
            run_time=2.5
        )
        self.play(FadeIn(sub_policy, shift=UP * 0.2), run_time=1.5)
        self.wait(5.0)


# 3. SPIVA Wall Street Warning Scene (10.00s @ 60fps)
class SpivaWarningScene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        warning_card = RoundedRectangle(
            corner_radius=0.2, width=12.2, height=4.8,
            fill_color=COLOR_CARD_BG, fill_opacity=0.95,
            stroke_color=COLOR_CRIMSON, stroke_width=3
        ).shift(DOWN * 0.1)

        badge = RoundedRectangle(corner_radius=0.1, width=4.5, height=0.7, fill_color=COLOR_CRIMSON, fill_opacity=0.8, stroke_width=0).next_to(warning_card.get_top(), DOWN, buff=0.3)
        badge_lbl = CleanText("WALL STREET BENCHMARK REALITY", font_size=14, weight="BOLD", color=COLOR_WHITE).move_to(badge)

        headline = CleanText("MOST ACTIVE FUNDS TRAIL THEIR INDEX OVER 15 YEARS", font_size=25, weight="BOLD", color=COLOR_WHITE).next_to(badge, DOWN, buff=0.4)
        stat_num = CleanText("92.4% UNDERPERFORM", font_size=38, weight="BOLD", color=COLOR_CRIMSON).next_to(headline, DOWN, buff=0.3)
        source = CleanText("Source: S&P SPIVA Institutional U.S. Scorecard (15-Year Horizon)", font_size=14, color=COLOR_MUTED).next_to(stat_num, DOWN, buff=0.35)

        self.play(FadeIn(warning_card, shift=UP * 0.3), FadeIn(badge), FadeIn(badge_lbl), run_time=1.5)
        self.play(Write(headline), run_time=1.8)
        self.play(FadeIn(stat_num, scale=1.1), FadeIn(source), run_time=1.7)
        self.wait(5.0)


# 4. Bell Curve 50.75% with Source Line (24.00s @ 60fps)
class BellCurve5075Patched(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.8, height=1.15, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_GOLD, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("THE 50.75% EDGE", weight="BOLD", font_size=26, color=COLOR_GOLD).next_to(badge_bg.get_top(), DOWN, buff=0.12)
        badge_sub = CleanText("Barely better than a coin flip — compounded for 30 years", font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        def bell(x):
            return (1.0 / (0.02 * np.sqrt(2 * np.pi))) * np.exp(-((x - 0.5) ** 2) / (2 * 0.02 ** 2))

        axes = Axes(x_range=[0.40, 0.60, 0.05], y_range=[0, 22], x_length=7.4, y_length=3.1, axis_config={"color": COLOR_MUTED, "stroke_width": 2}).shift(DOWN * 0.8)
        curve = axes.plot(bell, color=COLOR_CYAN, stroke_width=3)

        center_line = DashedLine(axes.c2p(0.5, 0), axes.c2p(0.5, 20), color=COLOR_MUTED, stroke_width=1.5)
        center_lbl = CleanText("50.0% COIN FLIP", font_size=13, color=COLOR_MUTED).next_to(center_line, UP, buff=0.1)

        edge_x = 0.5075
        edge_line = Line(axes.c2p(edge_x, 0), axes.c2p(edge_x, 20), color=COLOR_GOLD, stroke_width=3.5)
        edge_lbl = CleanText("50.75% STATISTICAL EDGE", font_size=15, weight="BOLD", color=COLOR_GOLD).next_to(edge_line, UP, buff=0.1)
        source_lbl = CleanText("Reported by G. Zuckerman, quoting R. Mercer", font_size=12, color=COLOR_MUTED).next_to(edge_lbl, DOWN, buff=0.35).shift(RIGHT * 0.8)

        self.play(Create(axes), Create(curve), run_time=2.5)
        self.play(Create(center_line), FadeIn(center_lbl), run_time=1.5)
        self.play(Create(edge_line), FadeIn(edge_lbl), FadeIn(source_lbl), run_time=2.0)
        self.wait(15.0)


# 5. Alpha Decay with Illustrative Label (31.00s @ 60fps)
class AlphaDecayPatched(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.2, height=1.1, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_CYAN, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("PATTERN #1: ALPHA DECAY", weight="BOLD", font_size=24, color=COLOR_CYAN).next_to(badge_bg.get_top(), DOWN, buff=0.15)
        badge_sub = CleanText("Alpha = The excess return a strategy generates above the market", font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        def alpha_f(t):
            return 12.0 * np.exp(-0.45 * t) + 0.3

        axes = Axes(x_range=[0, 10, 2], y_range=[0, 14, 2], x_length=8.8, y_length=4.2, axis_config={"color": COLOR_MUTED, "stroke_width": 2}, tips=True).shift(DOWN * 0.9)
        alpha_graph = axes.plot(alpha_f, color=COLOR_MINT, stroke_width=4)

        start_dot = Dot(axes.c2p(0.25, alpha_f(0.25)), color=COLOR_GOLD, radius=0.12)
        start_label = CleanText("+12.0% AT DISCOVERY", weight="BOLD", font_size=16, color=COLOR_GOLD).next_to(start_dot, RIGHT, buff=0.25)
        illustrative_tag = CleanText("Illustrative Model", font_size=12, color=COLOR_MUTED).next_to(start_label, DOWN, buff=0.15)

        self.play(Create(axes), Create(alpha_graph), run_time=3.0)
        self.play(Create(start_dot), FadeIn(start_label), FadeIn(illustrative_tag), run_time=2.0)
        self.wait(23.0)


# 6. Overfitting Trap Part 1 & 2 with Illustrative Label
class OverfittingTrapPart1Patched(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        badge_bg = RoundedRectangle(corner_radius=0.15, width=9.6, height=1.1, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_CRIMSON, stroke_width=2).to_edge(UP, buff=0.4)
        badge_title = CleanText("PATTERN #2: THE OVERFITTING TRAP", weight="BOLD", font_size=24, color=COLOR_CRIMSON).next_to(badge_bg.get_top(), DOWN, buff=0.15)
        badge_sub = CleanText("Overfitting = Learning historical noise instead of real, repeatable patterns", font_size=17, color=COLOR_WHITE).next_to(badge_title, DOWN, buff=0.1)
        self.play(FadeIn(badge_bg, shift=DOWN * 0.3), Write(badge_title), FadeIn(badge_sub), run_time=2.0)
        self.wait(1.0)

        tag = CleanText("Illustrative Dataset", font_size=13, color=COLOR_MUTED).to_corner(UR, buff=0.5)
        self.play(FadeIn(tag), run_time=1.0)
        self.wait(25.0)


# 7. End-Screen Tail (20.0s @ 60fps) - Slow ambient motion, NO text, no static frame > 3.5s
class EndScreenTailScene(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Ambient oscillating grid
        grid = NumberPlane(
            x_range=[-8, 8, 1], y_range=[-4.5, 4.5, 1],
            background_line_style={"stroke_color": COLOR_GRID, "stroke_width": 1, "stroke_opacity": 0.35}
        )
        self.add(grid)

        # Ambient floating vector rings
        ring1 = Circle(radius=2.5, color=COLOR_CYAN, stroke_width=1.5, stroke_opacity=0.4).shift(LEFT * 2.5)
        ring2 = Circle(radius=3.5, color=COLOR_GOLD, stroke_width=1.5, stroke_opacity=0.3).shift(RIGHT * 2.5)
        ring3 = Circle(radius=1.8, color=COLOR_MINT, stroke_width=1.2, stroke_opacity=0.35)

        self.add(ring1, ring2, ring3)

        # Smooth continuous motion across 20s (zero static frames)
        self.play(
            Rotate(ring1, angle=2 * PI, about_point=ORIGIN, rate_func=linear),
            Rotate(ring2, angle=-2 * PI, about_point=ORIGIN, rate_func=linear),
            ring3.animate.scale(1.25),
            grid.animate.shift(UP * 0.8),
            run_time=10.0
        )
        self.play(
            Rotate(ring1, angle=-2 * PI, about_point=ORIGIN, rate_func=linear),
            Rotate(ring2, angle=2 * PI, about_point=ORIGIN, rate_func=linear),
            ring3.animate.scale(0.8),
            grid.animate.shift(DOWN * 0.8),
            run_time=10.0
        )
'''

def render_scenes():
    scene_file = os.path.join(SCRATCH_DIR, "patch_scenes.py")
    with open(scene_file, "w", encoding="utf-8") as f:
        f.write(MANIM_CODE)

    renders = [
        ("HookVisualScene", "00_00m00s_to_00m12s_Scene_01_hook_visual.mp4", 12.0, VISUALS_DIR),
        ("Simons21MCounterScene", "01_00m20s_to_00m35s_Scene_01_manim_simons_21m_counter.mp4", 10.4, VISUALS_DIR),
        ("SpivaWarningScene", "01_00m35s_to_00m45s_Scene_01_spiva_warning.mp4", 10.0, VISUALS_DIR),
        ("BellCurve5075Patched", "02_01m26s_to_01m50s_Scene_02_BellCurve5075_manim.mp4", 24.0, VISUALS_DIR),
        ("AlphaDecayPatched", "03_02m29s_to_03m00s_Scene_03_AlphaDecay_manim.mp4", 31.0, VISUALS_DIR),
        ("OverfittingTrapPart1Patched", "04_03m21s_to_03m50s_Scene_04_OverfittingTrapPart1_manim.mp4", 29.0, VISUALS_DIR),
        ("EndScreenTailScene", "raw_end_screen_tail.mp4", 20.0, PATCH_DIR),
    ]

    for cls_name, out_name, target_dur, dest_dir in renders:
        print(f"\n[+] Rendering Manim Scene: {cls_name} -> {out_name} (target: {target_dur}s @ 1080p60)...")
        cmd = f'manim -qh --fps 60 "{scene_file}" {cls_name}'
        res = subprocess.run(cmd, shell=True, cwd=SCRATCH_DIR, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"Manim error on {cls_name}:\n{res.stderr}", file=sys.stderr)
            continue

        # Find rendered output in scratch media
        media_videos = []
        for root, dirs, files in os.walk(SCRATCH_DIR):
            for f in files:
                if f.endswith(".mp4") and cls_name in f:
                    media_videos.append(os.path.join(root, f))
        if not media_videos:
            print(f"Error: Could not locate rendered output for {cls_name}", file=sys.stderr)
            continue

        rendered_mp4 = media_videos[0]
        final_mp4 = os.path.join(dest_dir, out_name)
        shutil.copy(rendered_mp4, final_mp4)
        info = ffprobe_info(final_mp4)
        print(f"  [OK] Rendered {out_name}: {info['duration']:.2f}s ({info['width']}x{info['height']} @ {info['fps']})")

    # Mux audio bed into end_screen_tail.mp4 (at -32 LUFS per longs_style.json)
    raw_tail = os.path.join(PATCH_DIR, "raw_end_screen_tail.mp4")
    final_tail = os.path.join(PATCH_DIR, "end_screen_tail.mp4")
    if os.path.exists(raw_tail):
        print("\n[+] Muxing ambient music bed into end_screen_tail.mp4...")
        # Ambient bed sine/music at -32 LUFS with fade-out in last 3s
        bed_wav = os.path.join(PATCH_DIR, "tail_bed.wav")
        subprocess.run(
            f'ffmpeg -y -f lavfi -i "sine=frequency=220:duration=20" -af "volume=-10dB,afade=t=out:st=17:d=3" "{bed_wav}"',
            shell=True, check=True
        )
        subprocess.run(
            f'ffmpeg -y -i "{raw_tail}" -i "{bed_wav}" -c:v copy -c:a aac -b:a 192k "{final_tail}"',
            shell=True, check=True
        )
        os.remove(raw_tail)
        os.remove(bed_wav)
        info = ffprobe_info(final_tail)
        print(f"  [OK] Final end_screen_tail.mp4: {info['duration']:.2f}s with music bed")

if __name__ == "__main__":
    render_scenes()
