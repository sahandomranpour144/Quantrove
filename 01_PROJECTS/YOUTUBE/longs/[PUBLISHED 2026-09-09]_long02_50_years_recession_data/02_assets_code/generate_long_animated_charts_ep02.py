"""
Script: generate_long_animated_charts_ep02.py
EP02: "What Does 50 Years of Data Say About Recessions?"
Generates 7 dedicated, long-duration, high-retention 1080p 30fps animated MP4 charts:
1. anim01_sp500_50yr_recession_reveal.mp4 (~18s, 540 frames)
2. anim02_nber_vs_gdp_metrics.mp4 (~20s, 600 frames)
3. anim03_referee_lag_progress.mp4 (~22s, 660 frames)
4. anim04_50yr_autopsy_timeline.mp4 (~25s, 750 frames)
5. anim05_lead_lag_surge.mp4 (~22s, 660 frames)
6. anim06_time_and_jobs_asymmetry.mp4 (~24s, 720 frames)
7. anim07_macro_rules_summary.mp4 (~20s, 600 frames)
"""

import os
import shutil
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
TEMP_FRAMES_DIR = os.path.join(RENDERS_DIR, "temp_frames_long")
os.makedirs(RENDERS_DIR, exist_ok=True)

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
    "grid.alpha": 0.35,
    "figure.dpi": 100,
})

def render_frames_to_mp4(frame_generator, output_filename, fps=30, total_frames=300):
    if os.path.exists(TEMP_FRAMES_DIR):
        shutil.rmtree(TEMP_FRAMES_DIR)
    os.makedirs(TEMP_FRAMES_DIR, exist_ok=True)

    print(f"\n🎬 Rendering {output_filename} ({total_frames} frames @ {fps}fps = {total_frames/fps:.1f}s)...")
    for i, fig in enumerate(frame_generator(total_frames)):
        frame_path = os.path.join(TEMP_FRAMES_DIR, f"frame_{i:04d}.png")
        fig.savefig(frame_path, dpi=100, bbox_inches="tight", facecolor=DARK_BG)
        plt.close(fig)
        if (i + 1) % 100 == 0 or (i + 1) == total_frames:
            print(f"   Frame {i+1}/{total_frames} ({(i+1)/total_frames*100:.0f}%) rendered...")

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
    print(f"✅ Finished: {output_filename} -> {out_mp4}")

# ==========================================================
# 1. ANIMATION 1: S&P 500 50-Year Trajectory & Recession Illumination (18s)
# ==========================================================
def anim01_sp500_frames(total_frames=540):
    years = np.linspace(1970, 2025, 600)
    trend = 90 * np.exp(0.073 * (years - 1970))
    sp500 = trend.copy()
    dips = [
        (1973.8, 1975.2, 0.45, "1973 Oil Shock"),
        (1980.0, 1980.6, 0.15, "1980 Energy"),
        (1981.5, 1982.9, 0.25, "1981 Volcker"),
        (1990.5, 1991.2, 0.18, "1990 Gulf War"),
        (2001.2, 2002.8, 0.45, "2001 Dot-Com"),
        (2007.9, 2009.2, 0.52, "2008 GFC"),
        (2020.1, 2020.3, 0.34, "2020 COVID"),
    ]
    for start_yr, end_yr, dip, _ in dips:
        mask = (years >= start_yr) & (years <= end_yr + 1.2)
        sp500[mask] *= (1.0 - dip * np.exp(-((years[mask] - start_yr) / 0.85)**2))

    recession_bands = [
        (1973.9, 1975.2, "1973-75"), (1980.0, 1980.6, "1980"), (1981.5, 1982.9, "1981-82"),
        (1990.5, 1991.2, "1990-91"), (2001.2, 2001.9, "2001"), (2007.9, 2009.5, "2007-09"),
        (2020.1, 2020.3, "2020")
    ]

    for f in range(total_frames):
        p1 = min(1.0, f / (total_frames * 0.55))
        curr_idx = int(len(years) * p1)
        curr_year = years[min(curr_idx, len(years) - 1)]

        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)

        # Plot all recession bands up to current year
        for start, end, label in recession_bands:
            if curr_year >= start:
                band_end = min(curr_year, end)
                ax.axvspan(start, band_end, color="#334155", alpha=0.45)
                if curr_year >= end:
                    ax.text((start + end) / 2, 70, label, color=TEXT_MUTED, fontsize=10, ha="center", va="bottom", rotation=90)

        # Plot curve
        if curr_idx > 1:
            ax.plot(years[:curr_idx], sp500[:curr_idx], color=ACCENT_CYAN, lw=3.2)
            ax.scatter([years[curr_idx-1]], [sp500[curr_idx-1]], color=ACCENT_CYAN, s=140, edgecolors=TEXT_MAIN, lw=2.5, zorder=5)

        # Pulse bottom nodes in later phase
        if f >= total_frames * 0.55:
            pulse = 1.0 + 0.25 * np.sin((f - total_frames * 0.55) * 0.2)
            # 2008 & 2020 beacons
            ax.scatter([2009.2], [750], color=ACCENT_GREEN, s=250 * pulse, edgecolors=TEXT_MAIN, lw=2, zorder=6)
            ax.text(2009.2, 520, "2009 Generational Bottom\n(+68% Surge)", color=ACCENT_GREEN, fontsize=11, fontweight="bold", ha="center")
            
            ax.scatter([2020.25], [2300], color=ACCENT_GREEN, s=250 * pulse, edgecolors=TEXT_MAIN, lw=2, zorder=6)
            ax.text(2020.25, 1700, "2020 2-Month Rebound", color=ACCENT_GREEN, fontsize=11, fontweight="bold", ha="center")

        ax.set_xlim(1968, 2027)
        ax.set_ylim(40, 8500)
        ax.set_yscale("log")
        ax.set_title("50 YEARS OF DATA: S&P 500 TRAJECTORY & U.S. RECESSIONS (1970–2025)", fontsize=18, fontweight="bold", pad=20, color=TEXT_MAIN)
        ax.set_xlabel("Year", fontsize=13)
        ax.set_ylabel("S&P 500 Index (Log Scale)", fontsize=13)
        ax.grid(True, alpha=0.35)

        yield fig

# ==========================================================
# 2. ANIMATION 2: The Two-Quarter Myth vs NBER 4 Pillars (20s)
# ==========================================================
def anim02_nber_vs_gdp_frames(total_frames=600):
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)
        ax.axis("off")

        ax.text(0.5, 0.92, "HOW A RECESSION IS ACTUALLY DEFINED", ha="center", va="center", color=TEXT_MAIN, fontsize=22, fontweight="bold")
        ax.text(0.5, 0.85, "The Financial News Myth vs. The Official NBER Standard", ha="center", va="center", color=TEXT_MUTED, fontsize=14)

        # Left Box: The Myth
        p_left = min(1.0, f / 80)
        card1 = patches.FancyBboxPatch((0.08, 0.20), 0.38, 0.58, boxstyle="round,pad=0.03", ec=ACCENT_RED if f > 60 else PANEL_BORDER, fc=PANEL_BG, lw=2)
        ax.add_patch(card1)
        ax.text(0.27, 0.72, "THE POPULAR MYTH", ha="center", color=ACCENT_RED if f > 60 else TEXT_MUTED, fontsize=16, fontweight="bold")
        ax.text(0.27, 0.62, "Rule of Thumb:", ha="center", color=TEXT_MUTED, fontsize=13)
        ax.text(0.27, 0.52, "2 Consecutive Quarters\nof Negative GDP Growth", ha="center", color=TEXT_MAIN, fontsize=15, fontweight="bold")

        if f > 70:
            # Stamp Red X
            stamp_scale = min(1.0, (f - 70) / 20)
            ax.text(0.27, 0.35, "❌ NOT OFFICIAL", ha="center", va="center", color=ACCENT_RED, fontsize=20 * stamp_scale, fontweight="heavy",
                    bbox=dict(boxstyle="round,pad=0.4", fc="#450A0A", ec=ACCENT_RED, lw=2))

        # Right Box: NBER Real Standard
        p_right = min(1.0, max(0.0, (f - 120) / 100))
        card2 = patches.FancyBboxPatch((0.54, 0.20), 0.38, 0.58, boxstyle="round,pad=0.03", ec=ACCENT_CYAN, fc=PANEL_BG, lw=2)
        ax.add_patch(card2)
        ax.text(0.73, 0.72, "OFFICIAL ARBITER: NBER", ha="center", color=ACCENT_CYAN, fontsize=16, fontweight="bold")
        ax.text(0.73, 0.65, "National Bureau of Economic Research (8 Economists)", ha="center", color=TEXT_MUTED, fontsize=11)

        indicators = [
            ("1. Payroll Employment", 0.55),
            ("2. Real Personal Income", 0.47),
            ("3. Wholesale & Retail Sales", 0.39),
            ("4. Industrial Production", 0.31)
        ]
        for i, (name, y_pos) in enumerate(indicators):
            item_delay = 180 + i * 60
            if f >= item_delay:
                alpha_val = min(1.0, (f - item_delay) / 30)
                box_w = 0.30 * alpha_val
                bar = patches.Rectangle((0.58, y_pos - 0.025), box_w, 0.05, color="#1E293B", zorder=2)
                ax.add_patch(bar)
                ax.text(0.60, y_pos, name, color=TEXT_MAIN, fontsize=13, fontweight="bold", va="center", zorder=3)
                ax.text(0.88, y_pos, "✔", color=ACCENT_GREEN, fontsize=14, fontweight="bold", va="center", zorder=3)

        if f > 450:
            ax.text(0.5, 0.10, "📢 'A significant decline in economic activity spread across the economy, lasting more than a few months.'",
                    ha="center", color=ACCENT_GOLD, fontsize=13, fontweight="bold")

        yield fig

# ==========================================================
# 3. ANIMATION 3: The 7-Month Referee Lag Timeline (22s)
# ==========================================================
def anim03_referee_lag_frames(total_frames=660):
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)
        ax.axis("off")

        ax.text(0.5, 0.90, "THE 7-MONTH REFEREE LAG", ha="center", va="center", color=TEXT_MAIN, fontsize=24, fontweight="bold")
        ax.text(0.5, 0.82, "Why Official Macro Announcements Always Report on the Past", ha="center", va="center", color=TEXT_MUTED, fontsize=14)

        pct = min(1.0, f / (total_frames * 0.70))
        elapsed_months = pct * 10.4
        progress_ratio = min(1.0, elapsed_months / 10.4)

        y = 0.52
        ax.plot([0.15, 0.85], [y, y], color=PANEL_BORDER, lw=10, zorder=1)
        current_x = 0.15 + 0.70 * progress_ratio
        bar_color = ACCENT_CYAN if elapsed_months < 7.0 else ACCENT_RED
        ax.plot([0.15, current_x], [y, y], color=bar_color, lw=10, zorder=2)

        # Month 0 Node
        ax.scatter([0.15], [y], s=400, color=ACCENT_CYAN, zorder=4, edgecolors=TEXT_MAIN, lw=2)
        ax.text(0.15, y - 0.12, "Month 0\nRecession Begins\n(Quiet Peak)", ha="center", va="top", color=TEXT_MAIN, fontsize=12, fontweight="bold")

        # Month 7 Node
        nber_x = 0.15 + 0.70 * (7.0 / 10.4)
        if elapsed_months >= 7.0:
            pulse = 1.0 + 0.15 * np.sin((f - total_frames * 0.45) * 0.3)
            ax.scatter([nber_x], [y], s=500 * pulse, color=ACCENT_RED, zorder=4, edgecolors=TEXT_MAIN, lw=2.5)
            ax.text(nber_x, y + 0.13, "Month 7 (Average)\n📢 NBER DECLARES RECESSION!", ha="center", va="bottom", color=ACCENT_RED, fontsize=14, fontweight="heavy")
        else:
            ax.scatter([nber_x], [y], s=250, color=PANEL_BORDER, zorder=3)
            ax.text(nber_x, y + 0.12, "Month 7 (Average Announcement)", ha="center", va="bottom", color=TEXT_MUTED, fontsize=12)

        # Month 10.4 Node
        ax.scatter([0.85], [y], s=400, color=ACCENT_GREEN, zorder=4, edgecolors=TEXT_MAIN, lw=2)
        ax.text(0.85, y - 0.12, "Month 10.4\nAverage Recession Ends\n(New Expansion)", ha="center", va="top", color=ACCENT_GREEN, fontsize=12, fontweight="bold")

        # Bottom Insight Box
        box = patches.FancyBboxPatch((0.20, 0.12), 0.60, 0.20, boxstyle="round,pad=0.03", ec=ACCENT_GOLD if elapsed_months >= 7.0 else PANEL_BORDER, fc=PANEL_BG, lw=2)
        ax.add_patch(box)
        ax.text(0.5, 0.25, f"Elapsed Downtime: {elapsed_months:.1f} Months", ha="center", va="center", color=TEXT_MAIN, fontsize=16, fontweight="bold")
        if elapsed_months >= 7.0:
            ax.text(0.5, 0.17, "💥 ~70% OF THE ENTIRE RECESSION IS ALREADY IN THE REARVIEW MIRROR!", ha="center", va="center", color=ACCENT_GOLD, fontsize=14, fontweight="bold")

        yield fig

# ==========================================================
# 4. ANIMATION 4: The 50-Year Historical Autopsy Carousel (25s)
# ==========================================================
def anim04_50yr_autopsy_frames(total_frames=750):
    eras = [
        {"title": "1. 1973–1975: THE STAGFLATION SHOCK", "trigger": "OPEC Oil Embargo + Inflation", "dur": "16 Months", "sp_drop": "-48.2%", "cpi": "12.3% Inflation Peak", "color": "#F59E0B"},
        {"title": "2. 1981–1982: THE VOLCKER HAMMER", "trigger": "Fed Raised Rates to 20%", "dur": "16 Months", "sp_drop": "-27.1%", "cpi": "Rates: 20% Peak", "color": "#EF4444"},
        {"title": "3. 2001: THE DOT-COM VALUATION HANGOVER", "trigger": "Speculative Tech Bubble Burst", "dur": "8 Months", "sp_drop": "-49.1% (Nasdaq -78%)", "cpi": "Tech Sector Wipeout", "color": "#8B5CF6"},
        {"title": "4. 2008: THE GREAT FINANCIAL CRISIS", "trigger": "Global Banking & Subprime Freeze", "dur": "18 Months", "sp_drop": "-56.8% Drawdown", "cpi": "Longest Modern Downturn", "color": "#EF4444"},
        {"title": "5. 2020: THE COVID FLASH FREEZE", "trigger": "Global Lockdowns / Artificial Halt", "dur": "2 Months (Shortest in History)", "sp_drop": "-33.9% Flash Crash", "cpi": "Rapid Vertical V-Rebound", "color": "#10B981"},
    ]

    frames_per_era = total_frames // len(eras)

    for f in range(total_frames):
        era_idx = min(len(eras) - 1, f // frames_per_era)
        era = eras[era_idx]
        local_f = f % frames_per_era

        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)
        ax.axis("off")

        ax.text(0.5, 0.92, "50 YEARS OF RECESSIONS: THE HISTORICAL AUTOPSY", ha="center", va="center", color=TEXT_MAIN, fontsize=22, fontweight="bold")
        ax.text(0.5, 0.85, f"Analyzing 5 Distinct Economic Eras (Era {era_idx+1} of 5)", ha="center", va="center", color=TEXT_MUTED, fontsize=14)

        # Indicator Carousel dots
        for d in range(5):
            dot_color = ACCENT_CYAN if d == era_idx else "#334155"
            ax.scatter([0.42 + d * 0.04], [0.80], color=dot_color, s=120)

        # Center Main Era Card
        card = patches.FancyBboxPatch((0.15, 0.18), 0.70, 0.56, boxstyle="round,pad=0.04", ec=era["color"], fc=PANEL_BG, lw=2.5)
        ax.add_patch(card)

        ax.text(0.5, 0.67, era["title"], ha="center", va="center", color=era["color"], fontsize=20, fontweight="heavy")
        ax.plot([0.22, 0.78], [0.62, 0.62], color=PANEL_BORDER, lw=1.5)

        # Grid of metrics inside card
        ax.text(0.25, 0.52, "Economic Trigger:", color=TEXT_MUTED, fontsize=14)
        ax.text(0.25, 0.46, era["trigger"], color=TEXT_MAIN, fontsize=16, fontweight="bold")

        ax.text(0.60, 0.52, "Recession Duration:", color=TEXT_MUTED, fontsize=14)
        ax.text(0.60, 0.46, era["dur"], color=ACCENT_GOLD, fontsize=16, fontweight="bold")

        ax.text(0.25, 0.35, "S&P 500 Market Impact:", color=TEXT_MUTED, fontsize=14)
        ax.text(0.25, 0.29, era["sp_drop"], color=ACCENT_RED if "-" in era["sp_drop"] else TEXT_MAIN, fontsize=16, fontweight="bold")

        ax.text(0.60, 0.35, "Key Data Signature:", color=TEXT_MUTED, fontsize=14)
        ax.text(0.60, 0.29, era["cpi"], color=ACCENT_CYAN, fontsize=16, fontweight="bold")

        yield fig

# ==========================================================
# 5. ANIMATION 5: Pattern #1 — The Lead-Lag Paradox (22s)
# ==========================================================
def anim05_lead_lag_frames(total_frames=660):
    t = np.linspace(-14, 18, 500)
    stock_price = 100 - 45 * np.exp(-((t + 4) / 5.5)**2) + 2.2 * t
    stock_price[t < -4] = 100 - 45 * (1 - (t[t < -4] + 14) / 10)**0.5

    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)

        progress = min(1.0, f / (total_frames * 0.75))
        curr_idx = int(len(t) * progress)

        ax.axvspan(-12, 0, color="#334155", alpha=0.45, label="Recession Active Window (Gray Zone)")
        ax.axvline(0, color=ACCENT_RED, linestyle=":", lw=2, label="Recession Official End (Month 0)")

        if curr_idx > 1:
            ax.plot(t[:curr_idx], stock_price[:curr_idx], color=ACCENT_CYAN, lw=3.5, label="S&P 500 Price Trajectory")
            ax.scatter([t[curr_idx-1]], [stock_price[curr_idx-1]], color=ACCENT_CYAN, s=140, edgecolors=TEXT_MAIN, lw=2, zorder=5)

            # Lead-Lag Generational Bottom at t = -4
            if t[curr_idx-1] >= -4:
                pulse = 1.0 + 0.20 * np.sin(f * 0.25)
                ax.scatter([-4], [55], color=ACCENT_GREEN, s=380 * pulse, zorder=6, edgecolors=TEXT_MAIN, lw=2.5)
                ax.annotate("MARKET BOTTOMS HERE\n(3–5 Months Before Recession Ends!)", xy=(-4, 55), xytext=(-11, 85),
                            arrowprops=dict(facecolor=ACCENT_GREEN, shrink=0.08, width=2.5, headwidth=9),
                            fontsize=13, fontweight="heavy", color=ACCENT_GREEN,
                            bbox=dict(boxstyle="round,pad=0.3", fc=PANEL_BG, ec=ACCENT_GREEN, lw=1.5))

            if t[curr_idx-1] >= 6:
                ax.text(8, 110, "🚀 +60% Surge Into New Bull Market\nWhile News is Still Negative!", color=ACCENT_GOLD, fontsize=13, fontweight="bold")

        ax.set_xlim(-15, 19)
        ax.set_ylim(40, 135)
        ax.set_title("THE LEAD-LAG PARADOX: STOCKS RALLY WHILE ECONOMY IS STILL IN RECESSION", fontsize=17, fontweight="bold", color=TEXT_MAIN, pad=20)
        ax.set_xlabel("Months Relative to Recession End (0 = Official Recovery Date)", fontsize=13)
        ax.set_ylabel("S&P 500 Normalized Level", fontsize=13)
        ax.grid(True, alpha=0.35)
        ax.legend(loc="upper left", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=11)

        yield fig

# ==========================================================
# 6. ANIMATION 6: Pattern #2 — The Asymmetry of Time & Jobs (24s)
# ==========================================================
def anim06_time_jobs_frames(total_frames=720):
    for f in range(total_frames):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), dpi=100, gridspec_kw={'height_ratios': [1, 1.2]})

        # Top Chart: Duration Asymmetry
        ax1.set_facecolor(DARK_BG)
        ax1.set_xlim(0, 75)
        ax1.set_ylim(-0.5, 1.5)
        ax1.axis("off")

        p_bar = min(1.0, f / (total_frames * 0.40))
        rec_w = 10.4 * min(1.0, p_bar * 2.0)
        exp_w = 64.0 * p_bar

        ax1.text(0, 1.3, "1. DURATION ASYMMETRY (1950–2025)", color=TEXT_MAIN, fontsize=15, fontweight="bold")

        # Recession Bar
        ax1.barh(0.8, rec_w, height=0.35, color=ACCENT_RED, ec=TEXT_MAIN, lw=1)
        ax1.text(rec_w + 1.5, 0.8, f"Average Recession: {rec_w:.1f} Months", color=ACCENT_RED, fontsize=13, fontweight="bold", va="center")

        # Expansion Bar
        ax1.barh(0.2, exp_w, height=0.35, color=ACCENT_GREEN, ec=TEXT_MAIN, lw=1)
        ax1.text(exp_w + 1.5, 0.2, f"Average Expansion: {exp_w:.1f} Months (5.3 Years / 6x Longer!)", color=ACCENT_GREEN, fontsize=13, fontweight="bold", va="center")

        # Bottom Chart: Jobs Asymmetry (Elevator Down vs Stairs Up)
        ax2.set_facecolor(DARK_BG)
        t_jobs = np.linspace(-6, 54, 400)
        unemp = 4.0 + 6.0 / (1.0 + np.exp(-(t_jobs) / 1.2)) # fast spike
        unemp[t_jobs > 2] = 10.0 - 5.5 * ((t_jobs[t_jobs > 2] - 2) / 52)**0.65 # slow 4-year recovery

        p_jobs = min(1.0, max(0.0, (f - total_frames * 0.35) / (total_frames * 0.55)))
        curr_j = int(len(t_jobs) * p_jobs)

        ax2.axvspan(0, 10.4, color="#334155", alpha=0.45, label="Recession Active Window")

        if curr_j > 1:
            ax2.plot(t_jobs[:curr_j], unemp[:curr_j], color=ACCENT_GOLD, lw=3.2, label="Unemployment Rate (%)")
            ax2.scatter([t_jobs[curr_j-1]], [unemp[curr_j-1]], color=ACCENT_GOLD, s=120, edgecolors=TEXT_MAIN, lw=2, zorder=5)

            if t_jobs[curr_j-1] >= 2:
                ax2.annotate("ELEVATOR UP\n(Spikes in Weeks)", xy=(2, 9.8), xytext=(-5, 8.5),
                             arrowprops=dict(facecolor=ACCENT_RED, shrink=0.08, width=2, headwidth=7),
                             color=ACCENT_RED, fontsize=11, fontweight="bold")
            if t_jobs[curr_j-1] >= 30:
                ax2.annotate("STAIRS DOWN\n(3–5 Years to Recover)", xy=(35, 6.2), xytext=(25, 8.5),
                             arrowprops=dict(facecolor=ACCENT_GREEN, shrink=0.08, width=2, headwidth=7),
                             color=ACCENT_GREEN, fontsize=11, fontweight="bold")

        ax2.set_xlim(-8, 56)
        ax2.set_ylim(3, 11)
        ax2.set_title("2. THE JOBS RECOVERY LAG: ELEVATOR DOWN, STAIRS UP", fontsize=15, fontweight="bold", color=TEXT_MAIN, pad=12)
        ax2.set_xlabel("Months from Recession Start", fontsize=12)
        ax2.set_ylabel("Unemployment Rate (%)", fontsize=12)
        ax2.grid(True, alpha=0.35)
        ax2.legend(loc="upper right", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=11)

        plt.subplots_adjust(hspace=0.4)
        yield fig

# ==========================================================
# 7. ANIMATION 7: Conclusion Macro Rules & Next Episode Teaser (20s)
# ==========================================================
def anim07_macro_rules_frames(total_frames=600):
    rules = [
        ("RULE #1", "Recessions are brief resets in an ongoing long-term growth curve.", ACCENT_CYAN),
        ("RULE #2", "Official news is always late; waiting for certainty guarantees missing the recovery.", ACCENT_GOLD),
        ("RULE #3", "Panic selling is historically the most expensive trade an investor can make.", ACCENT_RED),
    ]

    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_subplot(111)
        ax.axis("off")

        ax.text(0.5, 0.92, "WHAT 50 YEARS OF DATA ACTUALLY TEACHES US", ha="center", va="center", color=TEXT_MAIN, fontsize=22, fontweight="bold")
        ax.text(0.5, 0.85, "The Three Immutable Rules of Economic Cycles", ha="center", va="center", color=TEXT_MUTED, fontsize=14)

        for i, (title, desc, col) in enumerate(rules):
            delay = i * 110
            if f >= delay:
                alpha_val = min(1.0, (f - delay) / 40)
                y_box = 0.68 - i * 0.16
                box = patches.FancyBboxPatch((0.15, y_box - 0.05), 0.70, 0.11, boxstyle="round,pad=0.03", ec=col, fc=PANEL_BG, lw=2)
                ax.add_patch(box)
                ax.text(0.20, y_box + 0.015, title, color=col, fontsize=14, fontweight="heavy")
                ax.text(0.20, y_box - 0.025, desc, color=TEXT_MAIN, fontsize=13, fontweight="bold")
                ax.text(0.82, y_box, "✔", color=ACCENT_GREEN, fontsize=18, fontweight="bold", va="center")

        # Next Episode Teaser in final phase
        if f > 400:
            teaser_alpha = min(1.0, (f - 400) / 40)
            t_box = patches.FancyBboxPatch((0.18, 0.08), 0.64, 0.10, boxstyle="round,pad=0.02", ec=ACCENT_CYAN, fc="#0F172A", lw=2)
            ax.add_patch(t_box)
            ax.text(0.5, 0.14, "NEXT BREAKDOWN (WEEK 3):", ha="center", color=ACCENT_CYAN, fontsize=12, fontweight="heavy")
            ax.text(0.5, 0.10, "How Recommendation Algorithms Actually Decide What You Watch", ha="center", color=TEXT_MAIN, fontsize=14, fontweight="bold")

        yield fig

def main():
    print("🎬 Starting Generation of 7 Long High-Retention Animated MP4 Charts for EP02...")
    render_frames_to_mp4(anim01_sp500_frames, "anim01_sp500_50yr_recession_reveal.mp4", fps=30, total_frames=540)
    render_frames_to_mp4(anim02_nber_vs_gdp_frames, "anim02_nber_vs_gdp_metrics.mp4", fps=30, total_frames=600)
    render_frames_to_mp4(anim03_referee_lag_frames, "anim03_referee_lag_progress.mp4", fps=30, total_frames=660)
    render_frames_to_mp4(anim04_50yr_autopsy_frames, "anim04_50yr_autopsy_timeline.mp4", fps=30, total_frames=750)
    render_frames_to_mp4(anim05_lead_lag_frames, "anim05_lead_lag_surge.mp4", fps=30, total_frames=660)
    render_frames_to_mp4(anim06_time_jobs_frames, "anim06_time_and_jobs_asymmetry.mp4", fps=30, total_frames=720)
    render_frames_to_mp4(anim07_macro_rules_frames, "anim07_macro_rules_summary.mp4", fps=30, total_frames=600)
    print("\n🎉 All 7 Extended Animated MP4 Charts successfully rendered in renders/!")

if __name__ == "__main__":
    main()
