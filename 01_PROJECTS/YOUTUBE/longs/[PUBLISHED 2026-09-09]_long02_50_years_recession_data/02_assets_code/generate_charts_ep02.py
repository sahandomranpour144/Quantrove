"""
Script & Visual Asset Generator: generate_charts_ep02.py
EP02: "What Does 50 Years of Data Say About Recessions?"
Generates high-resolution (1920x1080, 16:9) dark-themed financial charts,
infographics, stat cards, and timeline visuals for Scenes 01 through 07.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec

# Directory Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
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
ACCENT_PURPLE = "#8B5CF6"
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
    "grid.alpha": 0.5,
    "figure.dpi": 120,
})

def create_figure():
    return plt.figure(figsize=(16, 9), dpi=120)

def save_render(fig, filename):
    out_path = os.path.join(RENDERS_DIR, filename)
    fig.savefig(out_path, dpi=120, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print(f"✅ Rendered: {filename}")

# NBER Recession Dates (1970 - 2025)
RECESSIONS = [
    ("1973-11", "1975-03", "1973 Oil Shock (16m)"),
    ("1980-01", "1980-07", "1980 Energy (6m)"),
    ("1981-07", "1982-11", "1981 Volcker (16m)"),
    ("1990-07", "1991-03", "1990 Gulf War (8m)"),
    ("2001-03", "2001-11", "2001 Dot-Com (8m)"),
    ("2007-12", "2009-06", "2008 Financial Crisis (18m)"),
    ("2020-02", "2020-04", "2020 COVID (2m)"),
]

# ==========================================================
# SCENE 01: S&P 500 50-Year Trajectory with Shaded Recessions
# ==========================================================
def render_scene01():
    fig = create_figure()
    ax = fig.add_subplot(111)

    years = np.linspace(1970, 2025, 550)
    # Synthetic empirical S&P 500 curve on log-scale progression
    trend = 90 * np.exp(0.073 * (years - 1970))
    # Add cyclical dips matching recessions
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

    # Shaded Recession Bands
    recession_bands = [
        (1973.9, 1975.2), (1980.0, 1980.6), (1981.5, 1982.9),
        (1990.5, 1991.2), (2001.2, 2001.9), (2007.9, 2009.5),
        (2020.1, 2020.3)
    ]
    for start, end in recession_bands:
        ax.axvspan(start, end, color="#475569", alpha=0.35, label="NBER Recession" if start == 1973.9 else "")

    ax.plot(years, sp500, color=ACCENT_CYAN, linewidth=2.8, label="S&P 500 Index (50-Year Trajectory)")
    ax.set_yscale("log")
    ax.set_title("50 YEARS OF S&P 500 DATA & U.S. RECESSIONS (1970 – 2025)", fontsize=18, fontweight="bold", pad=20, color=TEXT_MAIN)
    ax.set_xlabel("Year", fontsize=13)
    ax.set_ylabel("S&P 500 Index (Log Scale)", fontsize=13)
    ax.grid(True, alpha=0.4)
    ax.legend(loc="upper left", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=12)

    # Callout text
    ax.text(2009.5, 750, "← 2008 Great Recession", color=ACCENT_GOLD, fontsize=11, fontweight="bold")
    ax.text(2020.4, 2500, "← 2020 COVID (2 Months)", color=ACCENT_GREEN, fontsize=11, fontweight="bold")

    save_render(fig, "scene01_sp500_50yr_recessions.png")

# ==========================================================
# SCENE 02: Split Screen — Two-Quarter Myth vs NBER Reality
# ==========================================================
def render_scene02():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, wspace=0.15)

    # Left: The Myth
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor(PANEL_BG)
    ax1.axis("off")
    rect1 = patches.FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.03", ec=ACCENT_RED, fc=PANEL_BG, lw=2.5)
    ax1.add_patch(rect1)
    ax1.text(0.5, 0.85, "THE HEADLINE MYTH", ha="center", va="center", color=ACCENT_RED, fontsize=18, fontweight="bold")
    ax1.text(0.5, 0.73, '"2 Consecutive Quarters of Negative GDP"', ha="center", va="center", color=TEXT_MAIN, fontsize=14, fontstyle="italic")
    
    # Red Cross mark
    ax1.text(0.5, 0.52, "✖", ha="center", va="center", color=ACCENT_RED, fontsize=70, fontweight="bold")
    ax1.text(0.5, 0.32, "• Not the official U.S. definition\n• Ignores employment & wages\n• Grossly oversimplifies complex cycles", ha="center", va="center", color=TEXT_MUTED, fontsize=13, linespacing=1.6)

    # Right: NBER Reality
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor(PANEL_BG)
    ax2.axis("off")
    rect2 = patches.FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.03", ec=ACCENT_CYAN, fc=PANEL_BG, lw=2.5)
    ax2.add_patch(rect2)
    ax2.text(0.5, 0.85, "THE OFFICIAL ARBITER (NBER)", ha="center", va="center", color=ACCENT_CYAN, fontsize=18, fontweight="bold")
    ax2.text(0.5, 0.73, "Business Cycle Dating Committee (8 Economists)", ha="center", va="center", color=TEXT_MAIN, fontsize=14)
    
    # Checkmark
    ax2.text(0.5, 0.52, "✔", ha="center", va="center", color=ACCENT_GREEN, fontsize=70, fontweight="bold")
    ax2.text(0.5, 0.28, "Comprehensive Macro Evaluation:\n1. Nonfarm Payroll Employment\n2. Real Personal Income Less Transfers\n3. Real Consumer & Wholesale Spending\n4. Industrial Production Capacity", ha="center", va="center", color=TEXT_MAIN, fontsize=13, linespacing=1.6)

    fig.suptitle("RETHINKING RECESSIONS: MYTH VS EMPIRICAL REALITY", fontsize=20, fontweight="bold", y=0.96, color=TEXT_MAIN)
    save_render(fig, "scene02_two_quarter_myth.png")

# ==========================================================
# SCENE 03: The 7-Month Referee Announcement Lag Timeline
# ==========================================================
def render_scene03():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    # Title
    ax.text(0.5, 0.90, "THE 7-MONTH REFEREE LAG", ha="center", va="center", color=TEXT_MAIN, fontsize=22, fontweight="bold")
    ax.text(0.5, 0.82, "Why Official Recession News is Always Late to the Party", ha="center", va="center", color=TEXT_MUTED, fontsize=14)

    # Horizontal timeline bar
    y = 0.50
    ax.plot([0.1, 0.9], [y, y], color=PANEL_BORDER, lw=6, zorder=1)
    ax.plot([0.1, 0.66], [y, y], color=ACCENT_RED, lw=6, zorder=2)
    ax.plot([0.66, 0.9], [y, y], color=ACCENT_GREEN, lw=6, zorder=2)

    # Key Points
    nodes = [
        (0.10, "Month 0", "Recession Starts\n(Peak of Cycle)", ACCENT_CYAN),
        (0.66, "Month 7 (Average)", "NBER Official Declaration\n(News Headline Panic!)", ACCENT_GOLD),
        (0.90, "Month 10.4", "Recession Ends\n(Average Duration)", ACCENT_GREEN),
    ]

    for x_pos, top_txt, btm_txt, color in nodes:
        ax.scatter(x_pos, y, s=400, color=color, zorder=3, edgecolors=TEXT_MAIN, linewidths=2.5)
        ax.text(x_pos, y + 0.10, top_txt, ha="center", va="bottom", color=color, fontsize=15, fontweight="bold")
        ax.text(x_pos, y - 0.12, btm_txt, ha="center", va="top", color=TEXT_MAIN, fontsize=13, linespacing=1.3)

    # Callout Highlight
    bracket_box = patches.FancyBboxPatch((0.15, 0.12), 0.70, 0.18, boxstyle="round,pad=0.02", ec=ACCENT_GOLD, fc=PANEL_BG, lw=1.5)
    ax.add_patch(bracket_box)
    ax.text(0.5, 0.21, "💡 KEY INSIGHT: By the time the NBER declares a recession,\napproximately 70% of the entire downturn is ALREADY OVER.", ha="center", va="center", color=TEXT_MAIN, fontsize=14, fontweight="bold", linespacing=1.4)

    save_render(fig, "scene03_referee_lag_timeline.png")

# ==========================================================
# SCENE 04: The 5-Era Historical Autopsy Cards
# ==========================================================
def render_scene04_cards():
    eras = [
        ("1973–1975: THE STAGFLATION SHOCK", "16 Months", "OPEC Oil Embargo + Skyrocketing Inflation", "S&P 500 fell -48%; double hit of stagnant growth + inflation.", ACCENT_RED, "scene04_era1_1973_oil_shock.png"),
        ("1981–1982: THE VOLCKER RATE HAMMER", "16 Months", "Fed Hikes Rates to 20% to Crush Inflation", "Intentional economic shutdown; broke inflation and launched 1980s bull run.", ACCENT_PURPLE, "scene04_era2_1981_volcker.png"),
        ("2001: THE DOT-COM BUST", "8 Months", "Tech Speculation Bubble Pops", "Mild recession in GDP terms (-0.3%), but severe Nasdaq tech wipeout (-78%).", ACCENT_CYAN, "scene04_era3_2001_dotcom.png"),
        ("2007–2009: THE GREAT FINANCIAL CRISIS", "18 Months", "Subprime Mortgages & Lehman Insolvency", "Deepest post-WWII crisis; complete balance-sheet liquidity freeze.", ACCENT_RED, "scene04_era4_2008_gfc.png"),
        ("2020: THE COVID FLASH CONTRACTION", "2 Months", "Global Pandemic Lockdown", "Shortest recession in history; fastest recovery to all-time highs.", ACCENT_GREEN, "scene04_era5_2020_covid.png"),
    ]

    for title, duration, trigger, impact, color, fname in eras:
        fig = create_figure()
        ax = fig.add_subplot(111)
        ax.axis("off")

        # Card container
        card = patches.FancyBboxPatch((0.1, 0.1), 0.8, 0.8, boxstyle="round,pad=0.03", ec=color, fc=PANEL_BG, lw=3)
        ax.add_patch(card)

        ax.text(0.5, 0.78, title, ha="center", va="center", color=color, fontsize=24, fontweight="bold")
        ax.text(0.5, 0.65, f"Official Duration: {duration}", ha="center", va="center", color=TEXT_MAIN, fontsize=18, fontweight="bold")
        
        # Divider
        ax.plot([0.2, 0.8], [0.55, 0.55], color=PANEL_BORDER, lw=2)

        ax.text(0.5, 0.44, f"Primary Trigger:\n{trigger}", ha="center", va="center", color=ACCENT_GOLD, fontsize=15, linespacing=1.3)
        ax.text(0.5, 0.26, f"Data Takeaway:\n{impact}", ha="center", va="center", color=TEXT_MUTED, fontsize=14, linespacing=1.3)

        save_render(fig, fname)

# ==========================================================
# SCENE 05: Pattern #1 — The Lead-Lag Paradox
# ==========================================================
def render_scene05():
    fig = create_figure()
    ax = fig.add_subplot(111)

    t = np.linspace(-12, 18, 300)
    # Simulated stock market bottoming ahead of recession end (t=0 is recession end)
    recession_start = -14
    recession_end = 0

    # Stock market trajectory: bottoms at t = -4 (4 months before recession ends)
    stock_price = 100 - 45 * np.exp(-((t + 4) / 6)**2) + 2.5 * t
    stock_price[t < -4] = 100 - 45 * (1 - (t[t < -4] + 12) / 8)**0.5

    ax.axvspan(-14, 0, color="#475569", alpha=0.35, label="Recession Active Period (14 Months)")
    ax.plot(t, stock_price, color=ACCENT_CYAN, lw=3.5, label="Stock Market (S&P 500)")

    # Bottom marker
    ax.scatter([-4], [55], color=ACCENT_GREEN, s=350, zorder=5, edgecolors=TEXT_MAIN, lw=2.5)
    ax.annotate("MARKET BOTTOMS\n(~4 Months Before Recession Ends)", xy=(-4, 55), xytext=(-8, 80),
                arrowprops=dict(facecolor=ACCENT_GREEN, shrink=0.08, width=2, headwidth=8),
                fontsize=13, fontweight="bold", color=ACCENT_GREEN)

    # 2009 Example Callout
    box = patches.FancyBboxPatch((2, 50), 14, 35, boxstyle="round,pad=1.5", ec=ACCENT_GOLD, fc=PANEL_BG, lw=2)
    ax.add_patch(box)
    ax.text(9, 75, "CASE STUDY: MARCH 2009", ha="center", va="center", color=ACCENT_GOLD, fontsize=14, fontweight="bold")
    ax.text(9, 62, "• Market bottomed March 9, 2009\n• Unemployment was still climbing (10%)\n• Recession didn't end until June 2009\n• S&P surged +68% over next 12 months!", ha="center", va="center", color=TEXT_MAIN, fontsize=11, linespacing=1.4)

    ax.set_title("THE LEAD-LAG PARADOX: MARKETS RALLY BEFORE THE RECOVERY", fontsize=18, fontweight="bold", color=TEXT_MAIN, pad=20)
    ax.set_xlabel("Months Relative to Official Recession End (t = 0)", fontsize=13)
    ax.set_ylabel("Market Price Level", fontsize=13)
    ax.grid(True, alpha=0.4)
    ax.legend(loc="upper left", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=12)

    save_render(fig, "scene05_lead_lag_paradox.png")

# ==========================================================
# SCENE 06: Pattern #2 — Asymmetry of Time & Jobs
# ==========================================================
def render_scene06():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, wspace=0.25)

    # Left: Duration Comparison
    ax1 = fig.add_subplot(gs[0, 0])
    categories = ["Average Recession", "Average Expansion"]
    durations = [10.4, 64.0]
    colors = [ACCENT_RED, ACCENT_GREEN]
    bars = ax1.bar(categories, durations, color=colors, width=0.55, edgecolor=PANEL_BORDER, lw=2)
    
    ax1.set_ylabel("Duration in Months", fontsize=13)
    ax1.set_title("THE TIME ASYMMETRY\n(Post-1950 U.S. Business Cycles)", fontsize=16, fontweight="bold", pad=15, color=TEXT_MAIN)
    ax1.grid(axis="y", alpha=0.4)

    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 1.8, f"{yval} Months\n({yval/12:.1f} Years)", ha="center", va="bottom", fontsize=13, fontweight="bold", color=TEXT_MAIN)
    ax1.set_ylim(0, 80)

    # Right: Jobs Elevator vs Stairs
    ax2 = fig.add_subplot(gs[0, 1])
    months = np.linspace(0, 48, 200)
    # Rapid unemployment rise (elevator down) and slow crawl back (stairs up)
    unemployment = 4.0 + 6.0 / (1.0 + np.exp(-1.5 * (months - 4))) * np.exp(-0.045 * (months - 4))
    unemployment[months < 4] = 4.0 + 0.5 * months[months < 4]

    ax2.plot(months, unemployment, color=ACCENT_GOLD, lw=3.2)
    ax2.set_title("THE JOBS SCAR\n(Elevator Up, Stairs Down)", fontsize=16, fontweight="bold", pad=15, color=TEXT_MAIN)
    ax2.set_xlabel("Months Since Recession Onset", fontsize=13)
    ax2.set_ylabel("Unemployment Rate (%)", fontsize=13)
    ax2.grid(True, alpha=0.4)

    ax2.text(8, 9.2, "⚡ Rapid Job Losses\n(2 - 4 Months)", color=ACCENT_RED, fontsize=11, fontweight="bold")
    ax2.text(26, 6.2, "🐢 Painful Multi-Year Recovery\n(36 - 60 Months)", color=ACCENT_GREEN, fontsize=11, fontweight="bold")

    fig.suptitle("ASYMMETRY: TIME DURATION VS HUMAN JOB IMPACT", fontsize=20, fontweight="bold", y=0.98, color=TEXT_MAIN)
    save_render(fig, "scene06_time_and_jobs_asymmetry.png")

# ==========================================================
# SCENE 07: Takeaway Summary Card & Outro
# ==========================================================
def render_scene07():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    box = patches.FancyBboxPatch((0.1, 0.1), 0.8, 0.8, boxstyle="round,pad=0.03", ec=ACCENT_CYAN, fc=PANEL_BG, lw=3)
    ax.add_patch(box)

    ax.text(0.5, 0.82, "WHAT 50 YEARS OF DATA ACTUALLY TEACH US", ha="center", va="center", color=ACCENT_CYAN, fontsize=22, fontweight="bold")

    rules = [
        ("1. RECESSIONS ARE BRIEF RESETS", "The average downturn lasts 10 months; expansions last 5+ years. Don't extrapolate temporary pain permanently.", ACCENT_GOLD),
        ("2. OFFICIAL DATA IS ALWAYS LATE", "By the time the recession is declared, smart money has already positioned for the recovery.", ACCENT_GREEN),
        ("3. PANIC IS THE MOST EXPENSIVE TRADE", "The market bottoms months before the headlines turn positive. Waiting for certainty guarantees missing the bottom.", ACCENT_RED),
    ]

    y = 0.65
    for title, desc, col in rules:
        ax.text(0.18, y, title, color=col, fontsize=15, fontweight="bold")
        ax.text(0.18, y - 0.06, desc, color=TEXT_MAIN, fontsize=12.5)
        y -= 0.16

    ax.text(0.5, 0.16, "👉 UP NEXT: How Recommendation Algorithms Actually Decide What You Watch", ha="center", va="center", color=ACCENT_PURPLE, fontsize=14, fontweight="bold")

    save_render(fig, "scene07_takeaways_summary.png")

def main():
    print("🚀 Starting EP02 High-Resolution Chart Generation...")
    render_scene01()
    render_scene02()
    render_scene03()
    render_scene04_cards()
    render_scene05()
    render_scene06()
    render_scene07()
    print("🎉 All EP02 visual chart assets successfully generated in renders/")

if __name__ == "__main__":
    main()
