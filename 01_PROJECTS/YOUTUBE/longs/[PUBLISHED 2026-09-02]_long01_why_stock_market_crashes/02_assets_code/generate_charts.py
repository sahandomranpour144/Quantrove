"""
Script & Visual Asset Generator: generate_charts.py
Generates high-resolution (1920x1080, 16:9) dark-themed financial charts, 
infographics, stat cards, and matrix visuals for Scenes 01 through 30.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.gridspec import GridSpec

# Set output directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
os.makedirs(RENDERS_DIR, exist_ok=True)

# Global Dark Theme Styling Configuration
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
    "grid.alpha": 0.6,
    "figure.dpi": 120,
})

def create_figure():
    fig = plt.figure(figsize=(16, 9), dpi=120)  # 1920x1080 at dpi=120
    return fig

def save_scene_render(fig, filename):
    out_path = os.path.join(RENDERS_DIR, filename)
    fig.savefig(out_path, dpi=120, bbox_inches="tight", facecolor=DARK_BG)
    plt.close(fig)
    print(f"Rendered: {filename} -> {out_path}")

# ==========================================================
# SCENE 01: S&P 500 2020 Crash (-34% in 22 Trading Days)
# ==========================================================
def render_scene_01():
    fig = create_figure()
    ax = fig.add_subplot(111)
    
    days = np.arange(1, 23)
    peak = 3386.15
    trough = 2237.40
    decay = (1 - np.cos(np.linspace(0, np.pi, 22))) / 2
    prices = peak - (peak - trough) * (decay ** 1.1) + np.random.RandomState(42).normal(0, 20, 22)
    prices[0] = peak
    prices[-1] = trough

    ax.plot(days, prices, color=ACCENT_RED, linewidth=4, label="S&P 500 Index (2020)", zorder=4)
    ax.fill_between(days, prices, peak, color=ACCENT_RED, alpha=0.15, zorder=2)
    ax.axhline(peak, color=TEXT_MUTED, linestyle=":", alpha=0.7, zorder=1)

    ax.scatter([1, 22], [peak, trough], color=[ACCENT_GREEN, ACCENT_RED], s=180, zorder=5, edgecolor="white", linewidth=2)
    ax.annotate("Peak: Feb 19, 2020\n3,386.15 pts", xy=(1, peak), xytext=(2.5, peak - 80),
                color=TEXT_MAIN, fontsize=14, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ACCENT_GREEN, lw=2))
    ax.annotate("Trough: Mar 23, 2020\n2,237.40 pts (-33.9%)", xy=(22, trough), xytext=(15, trough + 150),
                color=ACCENT_RED, fontsize=14, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=ACCENT_RED, lw=2))

    badge = patches.FancyBboxPatch((1.5, 2350), 8.5, 380, boxstyle="round,pad=0.3",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_RED, linewidth=2, zorder=6)
    ax.add_patch(badge)
    ax.text(2, 2600, "22 TRADING DAYS", fontsize=22, fontweight="bold", color=ACCENT_RED, zorder=7)
    ax.text(2, 2480, "Fastest -30%+ Bear Market in History\nOver 1/3 of Market Cap Erased", fontsize=13, color=TEXT_MAIN, zorder=7)

    ax.set_title("Line Chart: S&P 500 Pandemic Collapse (-34% in 22 Days)", fontsize=22, fontweight="bold", pad=20, color=TEXT_MAIN)
    ax.set_xlabel("Trading Days (Feb 19 – Mar 23, 2020)", fontsize=14, labelpad=10)
    ax.set_ylabel("S&P 500 Index Level", fontsize=14, labelpad=10)
    ax.set_xlim(0.5, 22.5)
    ax.set_ylim(2100, 3550)
    ax.grid(True)
    save_scene_render(fig, "Scene_01_sp500_2020_crash.png")

# ==========================================================
# SCENE 02: Split Screen: 1929 (3 Years -89%) vs 2008 Lehman ($639B)
# ==========================================================
def render_scene_02():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, wspace=0.25)

    ax1 = fig.add_subplot(gs[0, 0])
    months = np.linspace(0, 34, 100)
    dow_1929 = 381.17 * np.exp(-0.065 * months) + np.sin(months * 1.5) * 8
    dow_1929[-1] = 41.22
    ax1.plot(months, dow_1929, color=ACCENT_GOLD, linewidth=3.5)
    ax1.fill_between(months, dow_1929, 381.17, color=ACCENT_GOLD, alpha=0.15)
    ax1.scatter([0, 34], [381.17, 41.22], color=[ACCENT_GREEN, ACCENT_RED], s=140, zorder=5)
    ax1.text(2, 395, "Sept 1929: 381.2", color=ACCENT_GREEN, fontsize=12, fontweight="bold")
    ax1.text(20, 70, "July 1932: 41.2 (-89.2%)\n3 Years Duration", color=ACCENT_RED, fontsize=12, fontweight="bold")
    ax1.set_title("Line Chart: Dow Jones 1929–1932\n(-89% Multi-Year Grind)", fontsize=16, fontweight="bold", color=TEXT_MAIN)
    ax1.set_xlabel("Months from Peak (Sept 1929 – July 1932)", fontsize=12)
    ax1.set_ylabel("Dow Jones Industrial Average", fontsize=12)
    ax1.grid(True)

    ax2 = fig.add_subplot(gs[0, 1])
    entities = ["Lehman Brothers\n(Sept 2008 Assets)", "Switzerland\n(2008 GDP)", "Argentina\n(2008 GDP)", "South Africa\n(2008 GDP)"]
    values = [639, 554, 361, 297]
    bar_colors = [ACCENT_RED, "#38BDF8", "#38BDF8", "#38BDF8"]
    bars = ax2.barh(entities, values, color=bar_colors, height=0.55, edgecolor="white", linewidth=1.2)
    for bar, val in zip(bars, values):
        ax2.text(val + 15, bar.get_y() + bar.get_height()/2, f"${val} Billion", va="center", color=TEXT_MAIN, fontweight="bold", fontsize=12)
    ax2.set_title("Bar Chart: Lehman Bankruptcy Assets ($639B)\nvs National Annual GDPs (2008)", fontsize=16, fontweight="bold", color=TEXT_MAIN)
    ax2.set_xlabel("Billions of USD ($)", fontsize=12)
    ax2.set_xlim(0, 780)
    ax2.grid(True, axis="x")

    save_scene_render(fig, "Scene_02_1929_vs_2008_comparison.png")

# ==========================================================
# SCENE 03: Kinetic Typography & Title Card
# ==========================================================
def render_scene_03():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    x = np.linspace(-5, 5, 200)
    for offset, col in zip([-2, 0, 2], [ACCENT_GOLD, ACCENT_CYAN, ACCENT_RED]):
        ax.plot(x, np.sin(x + offset) * 1.5 + offset * 0.8, color=col, alpha=0.25, lw=3)

    t_box = patches.FancyBboxPatch((-4, -2.5), 8, 5, boxstyle="round,pad=0.5",
                                   facecolor=PANEL_BG, edgecolor=ACCENT_CYAN, linewidth=3)
    ax.add_patch(t_box)

    ax.text(0, 1.4, "T H E   A N A T O M Y   O F   A", ha="center", va="center", fontsize=20, fontweight="bold", color=TEXT_MUTED)
    ax.text(0, 0.4, "MARKET CRASH", ha="center", va="center", fontsize=48, fontweight="bold", color=ACCENT_RED)
    ax.text(0, -0.6, "1929  •  2008  •  2020", ha="center", va="center", fontsize=24, fontweight="bold", color=ACCENT_GOLD)
    ax.text(0, -1.6, "What Triggers the Panic — and Why Every Crash Shares One Pattern", ha="center", va="center", fontsize=15, color=TEXT_MAIN)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.5, 3.5)
    save_scene_render(fig, "Scene_03_title_card.png")

# ==========================================================
# SCENE 04: Media Montage & Symptom vs Cause
# ==========================================================
def render_scene_04():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    headlines = [
        ("WALL STREET IN MASS PANIC", -2.8, 1.8, 14, ACCENT_RED),
        ("BILLIONS WIPED OUT AS INVESTORS FLEE", 2.0, 2.2, 13, TEXT_MUTED),
        ("RECORD SELL-OFF GRIPS GLOBAL EXCHANGES", -1.5, -2.0, 13, TEXT_MUTED),
        ("MARKETS IN FREEFALL AMID UNCERTAINTY", 2.2, -1.6, 14, ACCENT_RED),
    ]
    for text, x, y, size, col in headlines:
        bbox = patches.FancyBboxPatch((x-2.5, y-0.35), 5.0, 0.7, boxstyle="round,pad=0.2",
                                      facecolor=PANEL_BG, edgecolor=col, alpha=0.7, lw=1.5)
        ax.add_patch(bbox)
        ax.text(x, y, text, ha="center", va="center", fontsize=size, color=col, fontweight="bold")

    ax.text(0, 0.3, "PANIC", ha="center", va="center", fontsize=80, fontweight="bold", color=ACCENT_RED, alpha=0.9)
    
    stamp = patches.FancyBboxPatch((-3.2, -0.6), 6.4, 0.9, boxstyle="round,pad=0.2",
                                  facecolor=ACCENT_GOLD, edgecolor="white", lw=2, zorder=5)
    ax.add_patch(stamp)
    ax.text(0, -0.15, "SYMPTOM, NOT THE ROOT CAUSE", ha="center", va="center",
            fontsize=20, fontweight="bold", color="#000000", zorder=6)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_04_panic_symptom_concept.png")

# ==========================================================
# SCENE 05: Concept Architecture Diagram
# ==========================================================
def render_scene_05():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    root = patches.FancyBboxPatch((-1.8, 1.8), 3.6, 1.0, boxstyle="round,pad=0.2",
                                  facecolor=ACCENT_PURPLE, edgecolor="white", lw=2)
    ax.add_patch(root)
    ax.text(0, 2.3, "Market Crash Event", ha="center", va="center", fontsize=18, fontweight="bold", color="white")

    branches = [
        ("External Trigger\n(Spark: War, Disease, Rates)", -3.3, -0.8, ACCENT_RED),
        ("Structural Fragility\n(Fuel: Debt, Hidden Leverage)", 0, -0.8, ACCENT_GOLD),
        ("Liquidity Stampede\n(Mechanism: Exit Bottleneck)", 3.3, -0.8, ACCENT_CYAN)
    ]
    for text, x, y, col in branches:
        box = patches.FancyBboxPatch((x-1.5, y-0.6), 3.0, 1.2, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col, lw=2.5)
        ax.add_patch(box)
        ax.text(x, y, text, ha="center", va="center", fontsize=13, fontweight="bold", color=col)
        ax.annotate("", xy=(x, y+0.7), xytext=(0, 1.7),
                    arrowprops=dict(arrowstyle="->", color=TEXT_MUTED, lw=2.5, connectionstyle="arc3,rad=0.1"))

    ax.text(0, -2.5, "Is every crash triggered by the same spark, or is the underlying fuel identical?",
            ha="center", va="center", fontsize=16, fontstyle="italic", color=TEXT_MAIN)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.2, 3.2)
    save_scene_render(fig, "Scene_05_crash_architecture_diagram.png")

# ==========================================================
# SCENE 06: 3-Card Interactive Dashboard Layout
# ==========================================================
def render_scene_06():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    cards = [
        ("1929 GREAT CRASH", "Trigger: Margin Debt & Hubris\n\nDrawdown: -89%\nDuration: 34 Months\nRecovery: ~25 Years", -3.2, ACCENT_GOLD),
        ("2008 FINANCIAL CRISIS", "Trigger: Subprime Mortgages\n\nDrawdown: -57%\nDuration: 17 Months\nRecovery: 5.5 Years", 0.0, ACCENT_CYAN),
        ("2020 COVID SHOCK", "Trigger: Global Pandemic Lockdowns\n\nDrawdown: -34%\nDuration: 22 Days\nRecovery: ~5 Months", 3.2, ACCENT_RED),
    ]

    for title, desc, x, col in cards:
        card = patches.FancyBboxPatch((x-1.45, -1.8), 2.9, 3.8, boxstyle="round,pad=0.2",
                                      facecolor=PANEL_BG, edgecolor=col, lw=3)
        ax.add_patch(card)
        ax.text(x, 1.6, title, ha="center", va="center", fontsize=15, fontweight="bold", color=col)
        ax.text(x, -0.2, desc, ha="center", va="center", fontsize=13, color=TEXT_MAIN, linespacing=1.6)

    banner = patches.FancyBboxPatch((-4.5, -2.8), 9.0, 0.7, boxstyle="round,pad=0.2",
                                    facecolor="#1E293B", edgecolor=ACCENT_PURPLE, lw=2)
    ax.add_patch(banner)
    ax.text(0, -2.45, "TRIGGERS: Completely Different   |   UNDERLYING MECHANISM: Exactly The Same",
            ha="center", va="center", fontsize=15, fontweight="bold", color=TEXT_MAIN)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.2, 2.5)
    save_scene_render(fig, "Scene_06_three_crashes_overview.png")

# ==========================================================
# SCENE 07: Crowded Room Metaphor - Calm State
# ==========================================================
def render_scene_07():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    room = patches.Rectangle((-4, -2.2), 6.5, 4.4, facecolor=PANEL_BG, edgecolor=TEXT_MUTED, lw=3)
    ax.add_patch(room)
    door = patches.Rectangle((2.5, -0.6), 0.3, 1.2, facecolor=ACCENT_GREEN, edgecolor="white", lw=2)
    ax.add_patch(door)
    ax.text(3.4, 0, "EXIT / MARKET\nLIQUIDITY", ha="center", va="center", color=ACCENT_GREEN, fontsize=14, fontweight="bold")

    np.random.seed(42)
    x_dots = np.random.uniform(-3.5, 1.8, 35)
    y_dots = np.random.uniform(-1.8, 1.8, 35)
    ax.scatter(x_dots, y_dots, color=ACCENT_GREEN, s=160, edgecolor="white", lw=1.5, zorder=5)

    ax.annotate("", xy=(3.8, 0), xytext=(2.0, 0),
                arrowprops=dict(arrowstyle="->", color=ACCENT_GREEN, lw=4))

    ax.text(-0.7, 2.6, "Normal Market Conditions: Orderly Order Flow & Ample Liquidity",
            ha="center", va="center", fontsize=18, fontweight="bold", color=TEXT_MAIN)
    ax.text(-0.7, -2.7, "As long as investors remain confident, buying and selling occurs smoothly.",
            ha="center", va="center", fontsize=14, color=TEXT_MUTED)

    ax.set_xlim(-4.5, 4.8)
    ax.set_ylim(-3.2, 3.2)
    save_scene_render(fig, "Scene_07_crowded_room_calm.png")

# ==========================================================
# SCENE 08: Crowded Room Metaphor - Panic Stampede
# ==========================================================
def render_scene_08():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    room = patches.Rectangle((-4, -2.2), 6.5, 4.4, facecolor="#1F1315", edgecolor=ACCENT_RED, lw=3)
    ax.add_patch(room)
    door = patches.Rectangle((2.5, -0.6), 0.3, 1.2, facecolor=ACCENT_RED, edgecolor="white", lw=2)
    ax.add_patch(door)
    ax.text(3.4, 0, "NARROW\nBOTTLENECK", ha="center", va="center", color=ACCENT_RED, fontsize=14, fontweight="bold")

    np.random.seed(42)
    x_rush = np.random.normal(2.0, 0.4, 30)
    y_rush = np.random.normal(0.0, 0.4, 30)
    ax.scatter(x_rush, y_rush, color=ACCENT_RED, s=180, edgecolor="white", lw=1.5, zorder=5)

    fire_badge = patches.FancyBboxPatch((-3.5, 1.2), 2.5, 0.8, boxstyle="round,pad=0.2",
                                        facecolor=ACCENT_RED, edgecolor="white", lw=2)
    ax.add_patch(fire_badge)
    ax.text(-2.25, 1.6, 'SHOUT OF "FIRE!"', ha="center", va="center", color="white", fontsize=15, fontweight="bold")

    ax.text(-0.7, 2.6, "Panic Dynamics: The Stampede Creates the Destruction",
            ha="center", va="center", fontsize=18, fontweight="bold", color=ACCENT_RED)
    ax.text(-0.7, -2.7, "People get crushed not by the fire itself, but by everyone rushing the single exit at once.",
            ha="center", va="center", fontsize=14, color=TEXT_MAIN)

    ax.set_xlim(-4.5, 4.8)
    ax.set_ylim(-3.2, 3.2)
    save_scene_render(fig, "Scene_08_crowded_room_panic.png")

# ==========================================================
# SCENE 09: Order Book Liquidity Evaporation
# ==========================================================
def render_scene_09():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1.2, 1])

    ax1 = fig.add_subplot(gs[0, 0])
    prices_bids = np.array([98, 97, 96, 95])
    qty_bids = np.array([50, 80, 110, 150])
    prices_asks = np.array([101, 102, 103, 104, 105, 106, 107])
    qty_asks = np.array([800, 1500, 2400, 3200, 4100, 5300, 6800])

    ax1.barh(prices_bids, qty_bids, color=ACCENT_GREEN, height=0.7, alpha=0.8, label="Buy Orders (Drained Liquidity)")
    ax1.barh(prices_asks, qty_asks, color=ACCENT_RED, height=0.7, alpha=0.8, label="Sell Orders (Massive Sell Wall)")
    ax1.set_title("Diagram: Exchange Order Book Liquidity Collapse", fontsize=15, fontweight="bold", color=TEXT_MAIN)
    ax1.set_xlabel("Share Quantity Depth", fontsize=12)
    ax1.set_ylabel("Stock Price ($)", fontsize=12)
    ax1.legend(loc="lower right", facecolor=PANEL_BG, edgecolor=PANEL_BORDER)
    ax1.grid(True, axis="x")

    ax2 = fig.add_subplot(gs[0, 1])
    time_steps = np.arange(10)
    crash_path = [100, 99.5, 98, 95, 91, 84, 76, 68, 62, 55]
    ax2.plot(time_steps, crash_path, color=ACCENT_RED, lw=4, marker="o")
    ax2.set_title("Result: Free-Falling Asset Price", fontsize=15, fontweight="bold", color=ACCENT_RED)
    ax2.set_xlabel("Time (Minutes into Cascade)", fontsize=12)
    ax2.set_ylabel("Execution Price ($)", fontsize=12)
    ax2.grid(True)
    ax2.annotate("Bid Gap:\nNo buyers below", xy=(5, 84), xytext=(6, 92),
                 arrowprops=dict(arrowstyle="->", color=ACCENT_GOLD, lw=2),
                 color=ACCENT_GOLD, fontweight="bold")

    save_scene_render(fig, "Scene_09_order_book_liquidity_drain.png")

# ==========================================================
# SCENE 10: Definition Gauge (Correction vs Bear vs Crash)
# ==========================================================
def render_scene_10():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    categories = [
        ("Pullback\n(0% to -5%)", -3.6, ACCENT_GREEN, "Healthy market oscillation"),
        ("Correction\n(-10% to -19%)", -1.2, ACCENT_GOLD, "Standard valuation reset"),
        ("Bear Market\n(-20% or deeper)", 1.2, "#F97316", "Prolonged macro downtrend"),
        ("CRASH\n(Sudden Fast Drop)", 3.6, ACCENT_RED, "High velocity cascade in days/weeks")
    ]

    for title, x, col, desc in categories:
        box = patches.FancyBboxPatch((x-1.1, -1.2), 2.2, 2.4, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col, lw=3)
        ax.add_patch(box)
        ax.text(x, 0.6, title, ha="center", va="center", fontsize=15, fontweight="bold", color=col)
        ax.text(x, -0.4, desc, ha="center", va="center", fontsize=12, color=TEXT_MAIN, wrap=True)

    ax.text(0, 2.2, "MARKET DECLINE TAXONOMY", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)
    ax.text(0, -2.2, "A crash is not just about the depth (-20%+) — it is defined by the sheer VELOCITY of the decline.",
            ha="center", va="center", fontsize=15, fontstyle="italic", color=TEXT_MUTED)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_10_market_decline_taxonomy.png")

# ==========================================================
# SCENE 11: Chapter Breakdown (3 Fires)
# ==========================================================
def render_scene_11():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    fires = [
        ("FIRE 1: 1929", "EXCESSIVE MARGIN DEBT", "Too much confidence, speculative borrowing at 10:1 leverage.", -3.2, ACCENT_GOLD),
        ("FIRE 2: 2008", "OPAQUE SUBPRIME RISK", "Hidden derivative exposure buried deep inside the banking core.", 0.0, ACCENT_CYAN),
        ("FIRE 3: 2020", "EXOGENOUS BIOLOGICAL SHOCK", "Unprecedented global pandemic shutting down real-world economies.", 3.2, ACCENT_RED),
    ]

    for header, sub, body, x, col in fires:
        box = patches.FancyBboxPatch((x-1.45, -1.8), 2.9, 3.6, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col, lw=3)
        ax.add_patch(box)
        ax.text(x, 1.3, header, ha="center", va="center", fontsize=16, fontweight="bold", color=col)
        ax.text(x, 0.5, sub, ha="center", va="center", fontsize=13, fontweight="bold", color="white")
        ax.text(x, -0.6, body, ha="center", va="center", fontsize=12, color=TEXT_MUTED)

    ax.text(0, 2.4, "THREE HISTORIC FIRES: WHAT STARTED THE STAMPEDE?", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_11_three_fires_chapters.png")

# ==========================================================
# SCENE 12: Roaring Twenties Bull Run (1921–1929)
# ==========================================================
def render_scene_12():
    fig = create_figure()
    ax = fig.add_subplot(111)

    years = np.linspace(1921, 1929.7, 100)
    dow_20s = 75 * np.exp(0.185 * (years - 1921)) + np.sin(years * 4) * 6

    ax.plot(years, dow_20s, color=ACCENT_GOLD, lw=4, label="Dow Jones Industrial Average")
    ax.fill_between(years, dow_20s, 60, color=ACCENT_GOLD, alpha=0.15)

    ax.scatter([1921, 1929.68], [75, 381.17], color=[ACCENT_GREEN, ACCENT_RED], s=160, zorder=5)
    ax.annotate("1921 Start:\n~75 pts", xy=(1921, 75), xytext=(1922, 120),
                arrowprops=dict(arrowstyle="->", color=ACCENT_GREEN, lw=2),
                color=TEXT_MAIN, fontweight="bold")
    ax.annotate("Sept 1929 Peak:\n381.17 pts (+400%+)", xy=(1929.68, 381.17), xytext=(1926.5, 350),
                arrowprops=dict(arrowstyle="->", color=ACCENT_GOLD, lw=2),
                color=ACCENT_GOLD, fontsize=14, fontweight="bold")

    sbox = patches.FancyBboxPatch((1922, 220), 3.8, 90, boxstyle="round,pad=0.2",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_GOLD, lw=2)
    ax.add_patch(sbox)
    ax.text(1923.9, 285, "THE ROARING TWENTIES", ha="center", fontsize=14, fontweight="bold", color=ACCENT_GOLD)
    ax.text(1923.9, 245, "~20% Annualized Gains\nUnchecked Speculation & Retail Frenzy", ha="center", fontsize=11, color=TEXT_MAIN)

    ax.set_title("Line Chart: Dow Jones 1920s Bull Market (+400% in 8 Years)", fontsize=20, fontweight="bold", pad=15)
    ax.set_xlabel("Year (1921 – 1929)", fontsize=13)
    ax.set_ylabel("Dow Jones Index Level", fontsize=13)
    ax.set_xlim(1920.5, 1930.2)
    ax.set_ylim(50, 420)
    ax.grid(True)
    save_scene_render(fig, "Scene_12_roaring_twenties_bull_run.png")

# ==========================================================
# SCENE 13: Margin Buying & 10:1 Leverage Liquidation Model
# ==========================================================
def render_scene_13():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, wspace=0.25)

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.bar(["$100 Stock\nPurchase"], [10], color=ACCENT_GREEN, width=0.45, label="Investor Cash ($10 Equity)")
    ax1.bar(["$100 Stock\nPurchase"], [90], bottom=[10], color=ACCENT_GOLD, width=0.45, label="Broker Loan ($90 Debt)")
    ax1.set_ylim(0, 120)
    ax1.set_title("Margin Structure (10:1 Leverage)\nInvestor Puts Down Only 10%", fontsize=15, fontweight="bold")
    ax1.legend(loc="upper left", facecolor=PANEL_BG, edgecolor=PANEL_BORDER)
    ax1.text(0, 5, "$10 (Equity)", ha="center", color="white", fontweight="bold")
    ax1.text(0, 55, "$90 (Borrowed Debt)", ha="center", color="black", fontweight="bold")
    ax1.grid(True, axis="y")

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.bar(["Stock Drops 10%\nValue = $90"], [0], color=ACCENT_RED, width=0.45)
    ax2.bar(["Stock Drops 10%\nValue = $90"], [90], bottom=[0], color=ACCENT_GOLD, width=0.45)
    ax2.set_ylim(0, 120)
    ax2.set_title("10% Price Drop Wipeout\n100% Equity Lost Instantly", fontsize=15, fontweight="bold", color=ACCENT_RED)
    ax2.text(0, 45, "$90 Debt Owed to Broker", ha="center", color="black", fontweight="bold")
    
    m_badge = patches.FancyBboxPatch((-0.4, 98), 0.8, 18, boxstyle="round,pad=0.2",
                                     facecolor=ACCENT_RED, edgecolor="white", lw=2)
    ax2.add_patch(m_badge)
    ax2.text(0, 107, "MARGIN CALL: FORCED LIQUIDATION", ha="center", va="center", color="white", fontweight="bold", fontsize=11)
    ax2.grid(True, axis="y")

    save_scene_render(fig, "Scene_13_margin_call_wipeout.png")

# ==========================================================
# SCENE 14: Dow Jones Black Thursday - Black Tuesday (Oct 1929)
# ==========================================================
def render_scene_14():
    fig = create_figure()
    ax = fig.add_subplot(111)

    days_oct = ["Oct 23\n(Wed)", "Oct 24\n(Black Thu)", "Oct 25\n(Fri)", "Oct 28\n(Black Mon)", "Oct 29\n(Black Tue)"]
    dow_oct = [305.85, 299.42, 301.22, 260.64, 230.07]

    ax.plot(days_oct, dow_oct, color=ACCENT_RED, lw=4, marker="o", markersize=10, zorder=4)
    ax.fill_between(range(len(days_oct)), dow_oct, 310, color=ACCENT_RED, alpha=0.15)

    ax.annotate("Black Monday:\n-12.8% Drop", xy=(3, 260.64), xytext=(2.2, 275),
                arrowprops=dict(arrowstyle="->", color=ACCENT_RED, lw=2),
                color=ACCENT_RED, fontweight="bold")
    ax.annotate("Black Tuesday:\n-11.7% Drop\n16.4M Shares Dumped", xy=(4, 230.07), xytext=(3.3, 220),
                arrowprops=dict(arrowstyle="->", color=ACCENT_RED, lw=2),
                color=ACCENT_RED, fontweight="bold")

    banner = patches.FancyBboxPatch((0.2, 235), 1.8, 30, boxstyle="round,pad=0.2",
                                    facecolor=PANEL_BG, edgecolor=ACCENT_GOLD, lw=2)
    ax.add_patch(banner)
    ax.text(1.1, 250, "4-Day Total Plunge: -25%", ha="center", va="center", color=ACCENT_GOLD, fontsize=14, fontweight="bold")

    ax.set_title("Line Chart: Dow Jones 4-Day Collapse (October 24–29, 1929)", fontsize=20, fontweight="bold", pad=15)
    ax.set_ylabel("Dow Jones Index Level", fontsize=13)
    ax.set_ylim(200, 320)
    ax.grid(True)
    save_scene_render(fig, "Scene_14_black_thursday_tuesday_crash.png")

# ==========================================================
# SCENE 15: 1929-1932 Full Collapse (-89%) & Bank Run Loop
# ==========================================================
def render_scene_15():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1.3, 1])

    ax1 = fig.add_subplot(gs[0, 0])
    timeline = np.linspace(1929.7, 1932.6, 100)
    dow_long = 381.17 * (1 - 0.892 * ((timeline - 1929.7) / (1932.6 - 1929.7))**0.8) + np.sin(timeline * 15) * 5
    dow_long[-1] = 41.22

    ax1.plot(timeline, dow_long, color=ACCENT_RED, lw=4)
    ax1.fill_between(timeline, dow_long, 381.17, color=ACCENT_RED, alpha=0.15)
    ax1.scatter([1929.7, 1932.6], [381.17, 41.22], color=[ACCENT_GREEN, ACCENT_RED], s=140, zorder=5)
    ax1.text(1929.8, 360, "Sept 1929: 381.2", color=ACCENT_GREEN, fontweight="bold")
    ax1.text(1931.8, 70, "July 1932: 41.2\n(-89.2% Drawdown)", color=ACCENT_RED, fontweight="bold", fontsize=13)
    ax1.set_title("Line Chart: Dow Jones 1929–1932 (-89% Collapse)", fontsize=16, fontweight="bold")
    ax1.set_xlabel("Year", fontsize=12)
    ax1.set_ylabel("Dow Jones Industrial Average", fontsize=12)
    ax1.grid(True)

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis("off")
    steps = [
        ("1. Stock Prices Plunge", 0, 2.2, ACCENT_RED),
        ("2. Margin Debt Defaults", 0, 1.1, ACCENT_GOLD),
        ("3. Bank Runs & Failures", 0, 0.0, ACCENT_RED),
        ("4. Credit & Savings Frozen", 0, -1.1, ACCENT_PURPLE),
        ("5. Forced Fire Sales Deepen", 0, -2.2, ACCENT_RED),
    ]
    for text, x, y, col in steps:
        box = patches.FancyBboxPatch((x-1.8, y-0.35), 3.6, 0.7, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col, lw=2)
        ax2.add_patch(box)
        ax2.text(x, y, text, ha="center", va="center", color=col, fontweight="bold", fontsize=12)
        if y > -2.0:
            ax2.annotate("", xy=(x, y-0.45), xytext=(x, y-0.35),
                         arrowprops=dict(arrowstyle="->", color=TEXT_MUTED, lw=2))

    ax2.set_xlim(-2.2, 2.2)
    ax2.set_ylim(-2.8, 2.8)
    ax2.set_title("Feedback Loop: Banking Contagion", fontsize=15, fontweight="bold", color=TEXT_MAIN)

    save_scene_render(fig, "Scene_15_1929_1932_full_collapse.png")

# ==========================================================
# SCENE 16: Summary Card: 1929 Crash
# ==========================================================
def render_scene_16():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    card = patches.FancyBboxPatch((-4.0, -2.6), 8.0, 5.2, boxstyle="round,pad=0.3",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_GOLD, lw=3)
    ax.add_patch(card)

    ax.text(0, 1.8, "FIRE #1 SUMMARY (1929)", ha="center", fontsize=24, fontweight="bold", color=ACCENT_GOLD)
    ax.text(0, 1.0, "TOO MUCH CONFIDENCE  •  TOO MUCH BORROWED MONEY", ha="center", fontsize=15, fontweight="bold", color=TEXT_MAIN)

    metrics = [
        ("Trigger:", "10:1 Margin Lending Speculation & Euphoric Valuations"),
        ("Max Drawdown:", "-89.2% (Dow fell from 381 to 41)"),
        ("Bottom Timeline:", "34 Months (Sept 1929 to July 1932)"),
        ("Systemic Flaw:", "Banks invested customer deposits directly into the equity market"),
        ("Recovery Time:", "25 Years (Full nominal breakeven in 1954)")
    ]
    y_pos = 0.2
    for label, val in metrics:
        ax.text(-3.2, y_pos, label, fontsize=13, fontweight="bold", color=ACCENT_GOLD)
        ax.text(-1.0, y_pos, val, fontsize=13, color=TEXT_MAIN)
        y_pos -= 0.55

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.2, 3.2)
    save_scene_render(fig, "Scene_16_1929_summary_card.png")

# ==========================================================
# SCENE 17: Subprime Mortgage Pipeline (2008)
# ==========================================================
def render_scene_17():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    stages = [
        ("Predatory Mortgages\n(NINJA loans, No Income)", -3.6, ACCENT_RED),
        ("Packaged into CDOs\n(Tranches sliced)", -1.2, ACCENT_GOLD),
        ("AAA Ratings Rubber-Stamped\n(Deceptive Security)", 1.2, ACCENT_CYAN),
        ("Lehman Balance Sheet\n(Over $600B+ Toxic Exposure)", 3.6, ACCENT_RED),
    ]

    for title, x, col in stages:
        box = patches.FancyBboxPatch((x-1.1, -1.2), 2.2, 2.4, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col, lw=2.5)
        ax.add_patch(box)
        ax.text(x, 0.4, title.split("\n")[0], ha="center", va="center", fontsize=13, fontweight="bold", color=col)
        ax.text(x, -0.4, title.split("\n")[1], ha="center", va="center", fontsize=11, color=TEXT_MAIN)

    for i in range(len(stages)-1):
        x_start = stages[i][1] + 1.15
        x_end = stages[i+1][1] - 1.15
        ax.annotate("", xy=(x_end, 0), xytext=(x_start, 0),
                    arrowprops=dict(arrowstyle="->", color=TEXT_MUTED, lw=3))

    ax.text(0, 2.2, "THE 2008 SUBPRIME CONTAGION PIPELINE", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)
    ax.text(0, -2.3, "Risky loans were repackaged as 'safe' assets and levered 30:1 by major investment banks.",
            ha="center", va="center", fontsize=14, color=TEXT_MUTED)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_17_subprime_pipeline.png")

# ==========================================================
# SCENE 18: Largest US Bankruptcies in History (2008)
# ==========================================================
def render_scene_18():
    fig = create_figure()
    ax = fig.add_subplot(111)

    bankruptcies = [
        "Lehman Brothers (2008)",
        "Washington Mutual (2008)",
        "WorldCom (2002)",
        "General Motors (2009)",
        "CIT Group (2009)",
        "Enron (2001)"
    ]
    assets = [639.1, 327.9, 107.0, 82.3, 71.0, 65.5]
    colors = [ACCENT_RED, "#F97316", "#38BDF8", "#38BDF8", "#38BDF8", "#38BDF8"]

    bars = ax.barh(bankruptcies[::-1], assets[::-1], color=colors[::-1], height=0.6, edgecolor="white", lw=1.2)
    for bar, val in zip(bars, assets[::-1]):
        ax.text(val + 12, bar.get_y() + bar.get_height()/2, f"${val} Billion", va="center", color=TEXT_MAIN, fontweight="bold", fontsize=12)

    ax.set_title("Bar Chart: Largest Corporate Bankruptcies in U.S. History", fontsize=20, fontweight="bold", pad=15)
    ax.set_xlabel("Asset Value at Time of Filing (Billions USD)", fontsize=13)
    ax.set_xlim(0, 750)
    ax.grid(True, axis="x")

    save_scene_render(fig, "Scene_18_largest_bankruptcies.png")

# ==========================================================
# SCENE 19: Sept 15, 2008 Dow Drop (-504 pts) & Domino Cascade
# ==========================================================
def render_scene_19():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, width_ratios=[1.2, 1])

    ax1 = fig.add_subplot(gs[0, 0])
    hours = ["9:30 AM", "11:00 AM", "1:00 PM", "3:00 PM", "4:00 PM (Close)"]
    dow_intraday = [11421, 11210, 11140, 11010, 10917]
    ax1.plot(hours, dow_intraday, color=ACCENT_RED, lw=4, marker="s", markersize=8)
    ax1.fill_between(range(5), dow_intraday, 11500, color=ACCENT_RED, alpha=0.15)
    ax1.set_title("Line Chart: Dow Jones Intraday\nSeptember 15, 2008 (-504 pts / -4.4%)", fontsize=15, fontweight="bold")
    ax1.set_ylabel("Dow Jones Level", fontsize=12)
    ax1.annotate("Worst 1-day drop\nsince 9/11", xy=(4, 10917), xytext=(2.5, 11050),
                 arrowprops=dict(arrowstyle="->", color=ACCENT_RED, lw=2),
                 color=ACCENT_RED, fontweight="bold")
    ax1.grid(True)

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.axis("off")
    dominos = [
        ("1. Subprime Mortgages Default", ACCENT_GOLD),
        ("2. Bear Stearns Fails (Mar 2008)", ACCENT_GOLD),
        ("3. Lehman Brothers Collapse (Sept 15)", ACCENT_RED),
        ("4. AIG $85B Emergency Bailout (Sept 17)", ACCENT_RED),
        ("5. Global Interbank Lending Freezes", ACCENT_PURPLE)
    ]
    for i, (text, col) in enumerate(dominos):
        y = 2.0 - i * 0.95
        b = patches.FancyBboxPatch((-2.0, y-0.3), 4.0, 0.65, boxstyle="round,pad=0.2",
                                   facecolor=PANEL_BG, edgecolor=col, lw=2)
        ax2.add_patch(b)
        ax2.text(0, y, text, ha="center", va="center", color=col, fontweight="bold", fontsize=11)

    ax2.set_xlim(-2.3, 2.3)
    ax2.set_ylim(-2.5, 2.5)
    ax2.set_title("The Domino Sequence", fontsize=15, fontweight="bold", color=TEXT_MAIN)

    save_scene_render(fig, "Scene_19_sept_15_2008_dominos.png")

# ==========================================================
# SCENE 20: Summary Card: 2008 Crash
# ==========================================================
def render_scene_20():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    card = patches.FancyBboxPatch((-4.0, -2.6), 8.0, 5.2, boxstyle="round,pad=0.3",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_CYAN, lw=3)
    ax.add_patch(card)

    ax.text(0, 1.8, "FIRE #2 SUMMARY (2008)", ha="center", fontsize=24, fontweight="bold", color=ACCENT_CYAN)
    ax.text(0, 1.0, "HIDDEN RISK NOBODY COULD SEE UNTIL TOO LATE", ha="center", fontsize=15, fontweight="bold", color=TEXT_MAIN)

    metrics = [
        ("Trigger:", "Subprime mortgage collapse & opaque CDO derivative leverage"),
        ("Max Drawdown:", "-56.8% (S&P 500 fell from 1,565 to 666)"),
        ("Bottom Timeline:", "17 Months (October 2007 to March 2009)"),
        ("Systemic Flaw:", "Interconnected balance sheets with extreme 30:1 hidden leverage"),
        ("Recovery Time:", "5.5 Years (New S&P 500 ATH in March 2013)")
    ]
    y_pos = 0.2
    for label, val in metrics:
        ax.text(-3.2, y_pos, label, fontsize=13, fontweight="bold", color=ACCENT_CYAN)
        ax.text(-1.0, y_pos, val, fontsize=13, color=TEXT_MAIN)
        y_pos -= 0.55

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.2, 3.2)
    save_scene_render(fig, "Scene_20_2008_summary_card.png")

# ==========================================================
# SCENE 21: World Map / Pandemic Shock Backdrop (Feb 2020)
# ==========================================================
def render_scene_21():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    box1 = patches.FancyBboxPatch((-4.2, -1.5), 2.6, 3.2, boxstyle="round,pad=0.2",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_RED, lw=2.5)
    ax.add_patch(box1)
    ax.text(-2.9, 1.2, "GLOBAL LOCKDOWNS", ha="center", color=ACCENT_RED, fontweight="bold", fontsize=14)
    ax.text(-2.9, -0.2, "International travel halted\nSupply chains broken\nService economies frozen", ha="center", color=TEXT_MAIN, fontsize=12)

    box2 = patches.FancyBboxPatch((-1.3, -1.5), 2.6, 3.2, boxstyle="round,pad=0.2",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_GOLD, lw=2.5)
    ax.add_patch(box2)
    ax.text(0, 1.2, "OIL PRICE SHOCK", ha="center", color=ACCENT_GOLD, fontweight="bold", fontsize=14)
    ax.text(0, -0.2, "Crude futures briefly\nturned negative (-$37/bbl)\nExtreme demand collapse", ha="center", color=TEXT_MAIN, fontsize=12)

    box3 = patches.FancyBboxPatch((1.6, -1.5), 2.6, 3.2, boxstyle="round,pad=0.2",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_CYAN, lw=2.5)
    ax.add_patch(box3)
    ax.text(2.9, 1.2, "LIQUIDITY FREEZE", ha="center", color=ACCENT_CYAN, fontweight="bold", fontsize=14)
    ax.text(2.9, -0.2, "Dash for cash into USD\nTreasury market strained\nExtreme volatility spikes", ha="center", color=TEXT_MAIN, fontsize=12)

    ax.text(0, 2.4, "FEBRUARY 2020: THE EXOGENOUS PANDEMIC SHOCK", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)
    ax.text(0, -2.4, "The stock market had just closed at an all-time high on Feb 19 (3,386 pts) before reality struck.",
            ha="center", va="center", fontsize=14, color=TEXT_MUTED)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_21_pandemic_shock_backdrop.png")

# ==========================================================
# SCENE 22: Dual Velocity Charts: 2020 S&P 500 Drop + Record Point Drop
# ==========================================================
def render_scene_22():
    fig = create_figure()
    gs = GridSpec(1, 2, figure=fig, wspace=0.25)

    ax1 = fig.add_subplot(gs[0, 0])
    days = np.arange(1, 23)
    p = 3386.15 - (3386.15 - 2237.40) * ((1 - np.cos(np.linspace(0, np.pi, 22))) / 2)**1.1
    ax1.plot(days, p, color=ACCENT_RED, lw=4)
    ax1.fill_between(days, p, 3386.15, color=ACCENT_RED, alpha=0.15)
    ax1.set_title("Line Chart: S&P 500 Peak-to-Trough\n(-34% in 22 Trading Days)", fontsize=15, fontweight="bold")
    ax1.set_xlabel("Trading Days (Feb 19 – Mar 23, 2020)", fontsize=12)
    ax1.set_ylabel("S&P 500 Index Level", fontsize=12)
    ax1.grid(True)

    ax2 = fig.add_subplot(gs[0, 1])
    dates = [
        "March 16, 2020",
        "March 12, 2020",
        "March 9, 2020",
        "June 11, 2020",
        "Sept 29, 2008"
    ]
    drops = [2997.10, 2352.60, 2013.76, 1861.82, 777.68]
    b_cols = [ACCENT_RED, "#F97316", "#F97316", "#F59E0B", ACCENT_CYAN]

    b = ax2.barh(dates[::-1], drops[::-1], color=b_cols[::-1], height=0.6, edgecolor="white", lw=1.2)
    for bar, val in zip(b, drops[::-1]):
        ax2.text(val + 50, bar.get_y() + bar.get_height()/2, f"-{val:,.0f} pts", va="center", color=TEXT_MAIN, fontweight="bold", fontsize=11)

    ax2.set_title("Bar Chart: Worst 1-Day Point Drops in Dow History", fontsize=15, fontweight="bold")
    ax2.set_xlabel("Points Dropped in Single Session", fontsize=12)
    ax2.set_xlim(0, 3600)
    ax2.grid(True, axis="x")

    save_scene_render(fig, "Scene_22_worst_one_day_point_drops.png")

# ==========================================================
# SCENE 23: Circuit Breakers Graphic & Trading Halts
# ==========================================================
def render_scene_23():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    levels = [
        ("LEVEL 1: -7% DROP", "15-Minute Market-Wide Halt", "TRIGGERED 4 TIMES IN MARCH 2020:\n• March 9\n• March 12\n• March 16\n• March 18", ACCENT_RED),
        ("LEVEL 2: -13% DROP", "15-Minute Market-Wide Halt", "Secondary emergency pause\nif selloff continues below -13%", ACCENT_GOLD),
        ("LEVEL 3: -20% DROP", "Trading Closed for Full Day", "Complete market shutdown\nto prevent systemic collapse", ACCENT_PURPLE),
    ]

    for title, x, col in zip(levels, [-3.2, 0.0, 3.2], [ACCENT_RED, ACCENT_GOLD, ACCENT_PURPLE]):
        title_t, sub_t, dates_t, col_t = title
        box = patches.FancyBboxPatch((x-1.45, -1.8), 2.9, 3.6, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col_t, lw=3)
        ax.add_patch(box)
        ax.text(x, 1.3, title_t, ha="center", va="center", fontsize=15, fontweight="bold", color=col_t)
        ax.text(x, 0.6, sub_t, ha="center", va="center", fontsize=12, fontweight="bold", color="white")
        ax.text(x, -0.6, dates_t, ha="center", va="center", fontsize=11, color=TEXT_MAIN)

    ax.text(0, 2.4, "NYSE MARKET-WIDE CIRCUIT BREAKER SYSTEM", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)
    ax.text(0, -2.4, "Automatic emergency circuit breakers fired 4 times in 10 days — unprecedented in modern market history.",
            ha="center", va="center", fontsize=14, color=TEXT_MUTED)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_23_circuit_breakers_halt.png")

# ==========================================================
# SCENE 24: S&P 500 V-Shaped Recovery + Stimulus (2020)
# ==========================================================
def render_scene_24():
    fig = create_figure()
    ax = fig.add_subplot(111)

    t = np.linspace(0, 148, 150)
    v_curve = np.piecewise(t, [t <= 22, t > 22],
                           [lambda x: 3386.15 - (3386.15 - 2237.40) * (x/22)**1.2,
                            lambda x: 2237.40 + (3389.78 - 2237.40) * ((x-22)/(148-22))**0.85])
    v_curve += np.random.RandomState(42).normal(0, 15, 150)
    v_curve[0] = 3386.15
    v_curve[22] = 2237.40
    v_curve[-1] = 3389.78

    ax.plot(t, v_curve, color=ACCENT_GREEN, lw=4, label="S&P 500 (Feb - Aug 2020)")
    ax.axhline(3386.15, color=TEXT_MUTED, linestyle=":", alpha=0.7)

    ax.scatter([0, 22, 148], [3386.15, 2237.40, 3389.78], color=[ACCENT_CYAN, ACCENT_RED, ACCENT_GREEN], s=160, zorder=5)

    ax.annotate("Peak: Feb 19, 2020\n3,386 pts", xy=(0, 3386.15), xytext=(5, 3150),
                arrowprops=dict(arrowstyle="->", color=ACCENT_CYAN, lw=2),
                color=TEXT_MAIN, fontweight="bold")
    ax.annotate("Trough: Mar 23, 2020\n2,237 pts (-34%)", xy=(22, 2237.40), xytext=(35, 2400),
                arrowprops=dict(arrowstyle="->", color=ACCENT_RED, lw=2),
                color=ACCENT_RED, fontweight="bold")
    ax.annotate("New All-Time High: Aug 18, 2020\n3,389.78 pts (~5 Months)", xy=(148, 3389.78), xytext=(90, 3500),
                arrowprops=dict(arrowstyle="->", color=ACCENT_GREEN, lw=2),
                color=ACCENT_GREEN, fontsize=13, fontweight="bold")

    stim_box = patches.FancyBboxPatch((28, 2650), 65, 380, boxstyle="round,pad=0.2",
                                      facecolor=PANEL_BG, edgecolor=ACCENT_GREEN, lw=2)
    ax.add_patch(stim_box)
    ax.text(60, 2900, "HISTORIC LIQUIDITY FLOOD", ha="center", color=ACCENT_GREEN, fontweight="bold", fontsize=13)
    ax.text(60, 2750, "• Fed QE: $3+ Trillion injected\n• CARES Act: $2.2 Trillion fiscal relief\n• Zero interest rate policy (ZIRP)", ha="center", color=TEXT_MAIN, fontsize=11)

    ax.set_title("Line Chart: S&P 500 V-Shaped Recovery (Fastest in Market History)", fontsize=20, fontweight="bold", pad=15)
    ax.set_xlabel("Trading Days from Peak (Feb 19 – Aug 18, 2020)", fontsize=13)
    ax.set_ylabel("S&P 500 Index Level", fontsize=13)
    ax.set_ylim(2100, 3700)
    ax.grid(True)

    save_scene_render(fig, "Scene_24_v_shaped_recovery.png")

# ==========================================================
# SCENE 25: Summary Card: 2020 Crash
# ==========================================================
def render_scene_25():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    card = patches.FancyBboxPatch((-4.0, -2.6), 8.0, 5.2, boxstyle="round,pad=0.3",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_RED, lw=3)
    ax.add_patch(card)

    ax.text(0, 1.8, "FIRE #3 SUMMARY (2020)", ha="center", fontsize=24, fontweight="bold", color=ACCENT_RED)
    ax.text(0, 1.0, "EXOGENOUS BIOLOGICAL SHOCK & HISTORIC LIQUIDITY RESCUE", ha="center", fontsize=15, fontweight="bold", color=TEXT_MAIN)

    metrics = [
        ("Trigger:", "Global COVID-19 pandemic and mandatory economic shutdowns"),
        ("Max Drawdown:", "-33.9% (S&P 500 fell from 3,386 to 2,237)"),
        ("Bottom Timeline:", "22 Trading Days (Feb 19 to Mar 23, 2020 - Fastest in history)"),
        ("Systemic Response:", "Immediate $5T+ fiscal & monetary liquidity backstop"),
        ("Recovery Time:", "~5 Months (New S&P 500 ATH reached August 18, 2020)")
    ]
    y_pos = 0.2
    for label, val in metrics:
        ax.text(-3.2, y_pos, label, fontsize=13, fontweight="bold", color=ACCENT_RED)
        ax.text(-1.0, y_pos, val, fontsize=13, color=TEXT_MAIN)
        y_pos -= 0.55

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.2, 3.2)
    save_scene_render(fig, "Scene_25_2020_summary_card.png")

# ==========================================================
# SCENE 26: Master Comparison Matrix (1929 vs 2008 vs 2020)
# ==========================================================
def render_scene_26():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    headers = ["Metric / Dimension", "1929 Crash", "2008 Crisis", "2020 Pandemic"]
    rows = [
        ["Root Trigger", "10:1 Margin Speculation", "Subprime Mortgages & CDOs", "COVID-19 Lockdowns"],
        ["Peak-to-Trough Drop", "-89.2% (Dow)", "-56.8% (S&P 500)", "-33.9% (S&P 500)"],
        ["Duration to Bottom", "34 Months (3 Years)", "17 Months (1.5 Years)", "22 Days (1 Month)"],
        ["Recovery to ATH", "~25 Years (1954)", "~5.5 Years (2013)", "~5 Months (Aug 2020)"],
        ["Core Vulnerability", "Banking / Margin Loans", "Interconnected Derivatives", "Exogenous Biological Shock"],
        ["Policy Intervention", "Severe Contraction / Tariffs", "TARP & Initial QE", "Unprecedented Flood ($5T+)"]
    ]

    col_x = [-3.5, -1.2, 1.2, 3.5]
    
    hbar = patches.FancyBboxPatch((-4.6, 1.8), 9.2, 0.7, boxstyle="round,pad=0.1",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_PURPLE, lw=2)
    ax.add_patch(hbar)
    for title, x in zip(headers, col_x):
        ax.text(x, 2.15, title, ha="center", va="center", fontsize=13, fontweight="bold", color=TEXT_MAIN)

    y = 1.2
    for r_idx, row in enumerate(rows):
        bg_col = "#131924" if r_idx % 2 == 0 else PANEL_BG
        rbar = patches.FancyBboxPatch((-4.6, y-0.25), 9.2, 0.5, boxstyle="round,pad=0.05",
                                      facecolor=bg_col, edgecolor="#232F42", lw=1)
        ax.add_patch(rbar)
        ax.text(col_x[0], y, row[0], ha="center", va="center", fontsize=11, fontweight="bold", color=ACCENT_GOLD)
        ax.text(col_x[1], y, row[1], ha="center", va="center", fontsize=10.5, color=TEXT_MAIN)
        ax.text(col_x[2], y, row[2], ha="center", va="center", fontsize=10.5, color=TEXT_MAIN)
        ax.text(col_x[3], y, row[3], ha="center", va="center", fontsize=10.5, color=TEXT_MAIN)
        y -= 0.55

    ax.text(0, 2.7, "MASTER COMPARISON MATRIX: 1929 vs 2008 vs 2020", ha="center", va="center", fontsize=20, fontweight="bold", color=TEXT_MAIN)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-2.5, 3.2)
    save_scene_render(fig, "Scene_26_master_comparison_matrix.png")

# ==========================================================
# SCENE 27: Unified Theoretical Mechanism Framework
# ==========================================================
def render_scene_27():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    stages = [
        ("1. ANY CATALYST TRIGGER\n(Debt / Derivatives / Pandemic)", -3.6, ACCENT_RED),
        ("2. CONFIDENCE RUPTURE\n(Perception of Safety Shatters)", -1.2, ACCENT_GOLD),
        ("3. LIQUIDITY EVAPORATION\n(Everyone Hits the Exit At Once)", 1.2, ACCENT_CYAN),
        ("4. SYSTEMIC CRASH\n(Self-Reinforcing Selling Cascade)", 3.6, ACCENT_PURPLE),
    ]

    for title, x, col in stages:
        box = patches.FancyBboxPatch((x-1.1, -1.0), 2.2, 2.0, boxstyle="round,pad=0.2",
                                     facecolor=PANEL_BG, edgecolor=col, lw=2.5)
        ax.add_patch(box)
        lines = title.split("\n")
        ax.text(x, 0.3, lines[0], ha="center", va="center", fontsize=12, fontweight="bold", color=col)
        ax.text(x, -0.4, lines[1], ha="center", va="center", fontsize=10.5, color=TEXT_MAIN)

    for i in range(len(stages)-1):
        x_start = stages[i][1] + 1.15
        x_end = stages[i+1][1] - 1.15
        ax.annotate("", xy=(x_end, 0), xytext=(x_start, 0),
                    arrowprops=dict(arrowstyle="->", color=TEXT_MUTED, lw=3))

    banner = patches.FancyBboxPatch((-4.2, -2.4), 8.4, 0.8, boxstyle="round,pad=0.2",
                                    facecolor="#1E293B", edgecolor=ACCENT_RED, lw=2.5)
    ax.add_patch(banner)
    ax.text(0, -2.0, "THE TRIGGER CHANGES. THE PANIC DOESN'T.", ha="center", va="center",
            fontsize=18, fontweight="bold", color=ACCENT_RED)

    ax.text(0, 2.2, "THE UNIVERSAL CRASH PATTERN", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_27_universal_mechanism_framework.png")

# ==========================================================
# SCENE 28: Philosophy / Investor Lens Graphic
# ==========================================================
def render_scene_28():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    card = patches.FancyBboxPatch((-3.8, -2.2), 7.6, 4.4, boxstyle="round,pad=0.3",
                                  facecolor=PANEL_BG, edgecolor=ACCENT_GREEN, lw=3)
    ax.add_patch(card)

    ax.text(0, 1.4, "WHAT THIS MEANS FOR INVESTORS", ha="center", fontsize=22, fontweight="bold", color=ACCENT_GREEN)

    points = [
        ("1. Triggers are inherently unpredictable:", "War, novel diseases, or hidden balance sheet fraud cannot be timed."),
        ("2. Structural leverage is the true hazard:", "Crashes only turn catastrophic when excessive debt forces liquidations."),
        ("3. Liquidity dries up when you need it most:", "In a panic, the bid-ask spread widens and buyers disappear."),
        ("4. Every historical crash resolved:", "Markets with resilient institutions eventually found price discovery and recovered.")
    ]
    y_pos = 0.5
    for p_title, p_desc in points:
        ax.text(-3.2, y_pos, p_title, fontsize=12, fontweight="bold", color=ACCENT_GOLD)
        ax.text(-3.2, y_pos - 0.28, p_desc, fontsize=11, color=TEXT_MAIN)
        y_pos -= 0.7

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_28_investor_takeaways.png")

# ==========================================================
# SCENE 29: Teaser: 50 Years of Post-Crash Macro Recoveries
# ==========================================================
def render_scene_29():
    fig = create_figure()
    ax = fig.add_subplot(111)

    years = np.linspace(1974, 2024, 200)
    sp500_trend = 100 * np.exp(0.075 * (years - 1974))
    for drop_yr, depth in [(1987, 0.78), (2000, 0.60), (2008, 0.45), (2020, 0.68)]:
        mask = (years >= drop_yr) & (years <= drop_yr + 2)
        sp500_trend[mask] *= depth

    ax.plot(years, sp500_trend, color=ACCENT_CYAN, lw=3.5, label="S&P 500 Real Total Return (Log Scale)")
    ax.set_yscale("log")

    for yr, label in [(1987, "1987 Black Monday"), (2000, "2000 Dot-Com"), (2008, "2008 GFC"), (2020, "2020 COVID")]:
        ax.axvline(yr, color=ACCENT_RED, linestyle="--", alpha=0.7)
        ax.text(yr + 0.5, 200, label, rotation=90, color=ACCENT_GOLD, fontsize=10, fontweight="bold")

    banner = patches.FancyBboxPatch((1980, 2000), 30, 2500, boxstyle="round,pad=0.2",
                                    facecolor=PANEL_BG, edgecolor=ACCENT_PURPLE, lw=2.5)
    ax.add_patch(banner)
    ax.text(1995, 3200, "NEXT EPISODE: THE AFTERMATH", ha="center", fontsize=15, fontweight="bold", color=ACCENT_PURPLE)
    ax.text(1995, 2300, "What happens to jobs, real GDP, and wages in the 5 years following a crash?\n50 Years of Macroeconomic Data Analyzed.", ha="center", fontsize=11, color=TEXT_MAIN)

    ax.set_title("Multi-Line Macro Chart: 50 Years of Market Cycles & Recoveries (1974–2024)", fontsize=18, fontweight="bold", pad=15)
    ax.set_xlabel("Year", fontsize=13)
    ax.set_ylabel("Index Level (Log Scale)", fontsize=13)
    ax.grid(True, which="both")
    ax.legend(loc="lower right", facecolor=PANEL_BG, edgecolor=PANEL_BORDER)

    save_scene_render(fig, "Scene_29_fifty_years_macro_teaser.png")

# ==========================================================
# SCENE 30: Outro & Channel End Screen
# ==========================================================
def render_scene_30():
    fig = create_figure()
    ax = fig.add_subplot(111)
    ax.axis("off")

    frame = patches.FancyBboxPatch((-4.5, -2.5), 9.0, 5.0, boxstyle="round,pad=0.3",
                                   facecolor=PANEL_BG, edgecolor=ACCENT_CYAN, lw=2)
    ax.add_patch(frame)

    vid1 = patches.FancyBboxPatch((-4.0, -1.2), 3.6, 2.2, boxstyle="round,pad=0.1",
                                  facecolor="#0B0E14", edgecolor=TEXT_MUTED, lw=2)
    ax.add_patch(vid1)
    ax.text(-2.2, 0, "NEXT EPISODE\n\n50 Years of Crash Recovery Data", ha="center", va="center", color=TEXT_MAIN, fontweight="bold", fontsize=12)

    vid2 = patches.FancyBboxPatch((0.4, -1.2), 3.6, 2.2, boxstyle="round,pad=0.1",
                                  facecolor="#0B0E14", edgecolor=TEXT_MUTED, lw=2)
    ax.add_patch(vid2)
    ax.text(2.2, 0, "SUBSCRIBE & SERIES PLAYLIST\n\nThe Anatomy of Modern Finance", ha="center", va="center", color=TEXT_MAIN, fontweight="bold", fontsize=12)

    sub_circ = patches.Circle((0, 1.4), 0.5, facecolor=ACCENT_RED, edgecolor="white", lw=2)
    ax.add_patch(sub_circ)
    ax.text(0, 1.4, "SUB", ha="center", va="center", color="white", fontweight="bold", fontsize=13)

    ax.text(0, -1.8, "Subscribe for deep-dive visual finance and data-driven market documentaries.",
            ha="center", va="center", color=TEXT_MUTED, fontsize=13)

    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 3)
    save_scene_render(fig, "Scene_30_outro_end_screen.png")

def main():
    print("Starting rendering of all static graphics & charts for Scene 01 to Scene 30...")
    render_scene_01()
    render_scene_02()
    render_scene_03()
    render_scene_04()
    render_scene_05()
    render_scene_06()
    render_scene_07()
    render_scene_08()
    render_scene_09()
    render_scene_10()
    render_scene_11()
    render_scene_12()
    render_scene_13()
    render_scene_14()
    render_scene_15()
    render_scene_16()
    render_scene_17()
    render_scene_18()
    render_scene_19()
    render_scene_20()
    render_scene_21()
    render_scene_22()
    render_scene_23()
    render_scene_24()
    render_scene_25()
    render_scene_26()
    render_scene_27()
    render_scene_28()
    render_scene_29()
    render_scene_30()
    print("All 30 static scenes rendered successfully!")

if __name__ == "__main__":
    main()
