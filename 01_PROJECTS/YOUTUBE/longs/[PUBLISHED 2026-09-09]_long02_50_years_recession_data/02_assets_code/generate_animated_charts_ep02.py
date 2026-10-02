"""
Script: generate_animated_charts_ep02.py
EP02: "What Does 50 Years of Data Say About Recessions?"
Generates high-retention, 1920x1080 (1080p, 30fps) animated MP4 charts for:
1. anim01_sp500_50yr_recession_reveal.mp4 (50-Year S&P 500 dynamic line draw with illuminating recession bands)
2. anim02_referee_lag_progress.mp4 (7-Month NBER Announcement lag with ticking percentage counter)
3. anim05_lead_lag_surge.mp4 (The Lead-Lag Paradox: Market bottoming and surging while recession is active)
"""

import os
import shutil
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
TEMP_FRAMES_DIR = os.path.join(RENDERS_DIR, "temp_frames")
os.makedirs(RENDERS_DIR, exist_ok=True)

# Quantrove Brand Palette
DARK_BG = "#0B0E14"
PANEL_BG = "#151B26"
PANEL_BORDER = "#2A364F"
TEXT_MAIN = "#F8FAFC"
TEXT_MUTED = "#94A3B8"
ACCENT_RED = "#EF4444"
ACCENT_GREEN = "#10B981"
ACCENT_CYAN = "#06B6D4"
ACCENT_GOLD = "#F59E0B"
GRID_COLOR = "#1E293B"

plt.rcParams.update({
    "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Helvetica", "Arial"],
    "font.family": "sans-serif",
    "figure.facecolor": DARK_BG,
    "axes.facecolor": DARK_BG,
    "savefig.facecolor": DARK_BG,
    "text.color": TEXT_MAIN,
    "axes.labelcolor": TEXT_MUTED,
    "xtick.color": TEXT_MUTED,
    "ytick.color": TEXT_MUTED,
    "grid.color": GRID_COLOR,
    "grid.linestyle": "--",
    "grid.alpha": 0.4,
    "figure.dpi": 100,
})

def render_frames_to_mp4(frame_generator, output_filename, fps=30, total_frames=90):
    if os.path.exists(TEMP_FRAMES_DIR):
        shutil.rmtree(TEMP_FRAMES_DIR)
    os.makedirs(TEMP_FRAMES_DIR, exist_ok=True)

    print(f"Generating frames for {output_filename} ({total_frames} frames)...")
    for i, fig in enumerate(frame_generator(total_frames)):
        frame_path = os.path.join(TEMP_FRAMES_DIR, f"frame_{i:04d}.png")
        fig.savefig(frame_path, dpi=100, bbox_inches="tight", facecolor=DARK_BG)
        plt.close(fig)

    out_mp4 = os.path.join(RENDERS_DIR, output_filename)
    cmd = [
        "ffmpeg", "-y", "-r", str(fps),
        "-i", os.path.join(TEMP_FRAMES_DIR, "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-vf", "scale=1920:1080",
        "-crf", "18", out_mp4
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    shutil.rmtree(TEMP_FRAMES_DIR)
    print(f"✅ Rendered Animation: {output_filename} -> {out_mp4}")

# ==========================================================
# ANIMATION 1: S&P 500 50-Year Trajectory Draw & Recession Illumination
# ==========================================================
def anim01_sp500_frames(total_frames=120):
    years = np.linspace(1970, 2025, 400)
    trend = 90 * np.exp(0.073 * (years - 1970))
    sp500 = trend.copy()
    for start_yr, end_yr, dip in [
        (1973.8, 1975.2, 0.45),
        (1980.0, 1980.6, 0.15),
        (1981.5, 1982.9, 0.25),
        (1990.5, 1991.2, 0.18),
        (2001.2, 2002.8, 0.45),
        (2007.9, 2009.2, 0.52),
        (2020.1, 2020.3, 0.34),
        (2022.0, 2022.8, 0.22),
    ]:
        mask = (years >= start_yr) & (years <= end_yr + 1.0)
        sp500[mask] *= (1.0 - dip * np.exp(-((years[mask] - start_yr) / 0.8)**2))

    recession_bands = [
        (1973.9, 1975.2), (1980.0, 1980.6), (1981.5, 1982.9),
        (1990.5, 1991.2), (2001.2, 2001.9), (2007.9, 2009.5),
        (2020.1, 2020.3)
    ]

    for f in range(total_frames):
        progress = min(1.0, (f + 1) / (total_frames * 0.85))
        curr_idx = int(len(years) * progress)
        curr_year = years[min(curr_idx, len(years) - 1)]

        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)

        # Plot recession bands up to current year
        for start, end in recession_bands:
            if curr_year >= start:
                band_end = min(curr_year, end)
                ax.axvspan(start, band_end, color="#475569", alpha=0.35)

        # Plot drawn curve
        if curr_idx > 1:
            ax.plot(years[:curr_idx], sp500[:curr_idx], color=ACCENT_CYAN, lw=3.2)
            # Glowing current head
            ax.scatter([years[curr_idx-1]], [sp500[curr_idx-1]], color=ACCENT_CYAN, s=120, edgecolors=TEXT_MAIN, lw=2, zorder=5)

        ax.set_xlim(1968, 2027)
        ax.set_ylim(60, 7500)
        ax.set_yscale("log")
        ax.set_title("50 YEARS OF DATA: S&P 500 TRAJECTORY & U.S. RECESSIONS", fontsize=18, fontweight="bold", pad=20, color=TEXT_MAIN)
        ax.set_xlabel("Year", fontsize=13)
        ax.set_ylabel("S&P 500 Index (Log Scale)", fontsize=13)
        ax.grid(True, alpha=0.4)

        if f > total_frames * 0.7:
            ax.text(2009.5, 800, "2008 Crash", color=ACCENT_GOLD, fontsize=12, fontweight="bold")
            ax.text(2020.4, 2600, "2020 COVID", color=ACCENT_GREEN, fontsize=12, fontweight="bold")

        yield fig

# ==========================================================
# ANIMATION 2: The 7-Month Referee Lag Progress Bar & Percentage
# ==========================================================
def anim02_referee_lag_frames(total_frames=90):
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)
        ax.axis("off")

        pct = min(1.0, (f + 1) / (total_frames * 0.75))
        elapsed_months = pct * 10.4
        progress_ratio = min(1.0, elapsed_months / 10.4)

        ax.text(0.5, 0.88, "THE 7-MONTH REFEREE LAG", ha="center", va="center", color=TEXT_MAIN, fontsize=22, fontweight="bold")
        ax.text(0.5, 0.80, "Why Official News Always Reports on the Past", ha="center", va="center", color=TEXT_MUTED, fontsize=14)

        y = 0.50
        # Background bar
        ax.plot([0.15, 0.85], [y, y], color=PANEL_BORDER, lw=8, zorder=1)
        # Active progress bar
        current_x = 0.15 + 0.70 * progress_ratio
        bar_color = ACCENT_CYAN if elapsed_months < 7.0 else ACCENT_RED
        ax.plot([0.15, current_x], [y, y], color=bar_color, lw=8, zorder=2)

        # Markers
        ax.scatter([0.15], [y], s=350, color=ACCENT_CYAN, zorder=4)
        ax.text(0.15, y - 0.12, "Month 0\nRecession Begins", ha="center", va="top", color=TEXT_MAIN, fontsize=12)

        nber_x = 0.15 + 0.70 * (7.0 / 10.4)
        if elapsed_months >= 7.0:
            ax.scatter([nber_x], [y], s=400, color=ACCENT_RED, zorder=4, edgecolors=TEXT_MAIN, lw=2)
            ax.text(nber_x, y + 0.12, "Month 7\nNBER Declares Recession!", ha="center", va="bottom", color=ACCENT_RED, fontsize=13, fontweight="bold")
        else:
            ax.scatter([nber_x], [y], s=250, color=PANEL_BORDER, zorder=3)
            ax.text(nber_x, y + 0.12, "Month 7 (Declaration)", ha="center", va="bottom", color=TEXT_MUTED, fontsize=12)

        ax.scatter([0.85], [y], s=350, color=ACCENT_GREEN, zorder=4)
        ax.text(0.85, y - 0.12, "Month 10.4\nRecession Ends", ha="center", va="top", color=TEXT_MAIN, fontsize=12)

        # Large elapsed box
        calc_pct = int(min(70, (elapsed_months / 10.4) * 100)) if elapsed_months < 7.0 else 70
        box = patches.FancyBboxPatch((0.25, 0.15), 0.50, 0.18, boxstyle="round,pad=0.02", ec=ACCENT_GOLD, fc=PANEL_BG, lw=2)
        ax.add_patch(box)
        ax.text(0.5, 0.24, f"Elapsed Downtime: {elapsed_months:.1f} Months", ha="center", va="center", color=TEXT_MAIN, fontsize=15, fontweight="bold")
        if elapsed_months >= 7.0:
            ax.text(0.5, 0.18, "💥 ~70% OF THE ENTIRE RECESSION IS ALREADY OVER!", ha="center", va="center", color=ACCENT_GOLD, fontsize=14, fontweight="bold")

        yield fig

# ==========================================================
# ANIMATION 3: Pattern #1 — Lead-Lag Surge Ahead of Recovery
# ==========================================================
def anim05_lead_lag_frames(total_frames=100):
    t = np.linspace(-12, 16, 250)
    stock_price = 100 - 45 * np.exp(-((t + 4) / 6)**2) + 2.5 * t
    stock_price[t < -4] = 100 - 45 * (1 - (t[t < -4] + 12) / 8)**0.5

    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)

        progress = min(1.0, (f + 1) / (total_frames * 0.85))
        curr_idx = int(len(t) * progress)

        ax.axvspan(-12, 0, color="#475569", alpha=0.35, label="Recession Active Window (Gray Zone)")

        if curr_idx > 1:
            ax.plot(t[:curr_idx], stock_price[:curr_idx], color=ACCENT_CYAN, lw=3.5, label="S&P 500 Market Price")
            # Lead lag bottom at t = -4
            if t[curr_idx-1] >= -4:
                ax.scatter([-4], [55], color=ACCENT_GREEN, s=350, zorder=5, edgecolors=TEXT_MAIN, lw=2.5)
                ax.annotate("MARKET BOTTOMS HERE\n(4 Months Before Recession Ends!)", xy=(-4, 55), xytext=(-9, 78),
                            arrowprops=dict(facecolor=ACCENT_GREEN, shrink=0.08, width=2, headwidth=8),
                            fontsize=12, fontweight="bold", color=ACCENT_GREEN)

        ax.set_xlim(-13, 17)
        ax.set_ylim(40, 130)
        ax.set_title("THE LEAD-LAG PARADOX: STOCKS RALLY WHILE ECONOMY IS STILL IN RECESSION", fontsize=16, fontweight="bold", color=TEXT_MAIN, pad=20)
        ax.set_xlabel("Months Relative to Recession End (t = 0)", fontsize=13)
        ax.set_ylabel("S&P 500 Price", fontsize=13)
        ax.grid(True, alpha=0.4)
        ax.legend(loc="upper left", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=12)

        yield fig

def main():
    print("🎬 Starting High-Retention Animated MP4 Generation...")
    render_frames_to_mp4(anim01_sp500_frames, "anim01_sp500_50yr_recession_reveal.mp4", fps=30, total_frames=120)
    render_frames_to_mp4(anim02_referee_lag_frames, "anim02_referee_lag_progress.mp4", fps=30, total_frames=90)
    render_frames_to_mp4(anim05_lead_lag_frames, "anim05_lead_lag_surge.mp4", fps=30, total_frames=100)
    print("🎉 All 3 Animated MP4 Charts successfully rendered in renders/")

if __name__ == "__main__":
    main()
