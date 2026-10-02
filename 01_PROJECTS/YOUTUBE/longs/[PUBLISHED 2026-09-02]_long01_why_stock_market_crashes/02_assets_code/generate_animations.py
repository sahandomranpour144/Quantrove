"""
Script & Visual Asset Generator: generate_animations.py
Generates 1920x1080 (1080p, 30fps) MP4 animations for dynamic scenes:
1. Scene 01: S&P 500 2020 22-Day Collapse & Counter
2. Scene 07/08: Crowded Theater / "Fire" Bottleneck Simulation
3. Scene 09: Order Book Liquidity Evaporation Cascade
4. Scene 13: Margin Call 10:1 Leverage Wipeout
5. Scene 14: Dow Jones 1929 4-Day Collapse
6. Scene 19: 2008 Systemic Domino Contagion
7. Scene 23: NYSE Emergency Circuit Breaker Trigger
8. Scene 24: 2020 S&P 500 V-Shaped Liquidity Recovery
9. Scene 27: Universal Crash Mechanism Sequential Pipeline
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
    "grid.color": "#1E293B",
    "grid.linestyle": "--",
    "grid.alpha": 0.6,
    "figure.dpi": 120,
})

def render_frames_to_mp4(frame_generator, output_filename, fps=30, total_frames=90):
    if os.path.exists(TEMP_FRAMES_DIR):
        shutil.rmtree(TEMP_FRAMES_DIR)
    os.makedirs(TEMP_FRAMES_DIR, exist_ok=True)

    print(f"Generating frames for {output_filename} ({total_frames} frames)...")
    for i, fig in enumerate(frame_generator(total_frames)):
        frame_path = os.path.join(TEMP_FRAMES_DIR, f"frame_{i:04d}.png")
        fig.savefig(frame_path, dpi=120, bbox_inches="tight", facecolor=DARK_BG)
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
    print(f"Rendered Animation: {output_filename} -> {out_mp4}")

# ==========================================================
# ANIMATION 1: Scene 01 - S&P 500 2020 22-Day Plunge
# ==========================================================
def anim_scene_01(total_frames=60):
    peak = 3386.15
    trough = 2237.40
    days = np.arange(1, 23)
    decay = (1 - np.cos(np.linspace(0, np.pi, 22))) / 2
    full_prices = peak - (peak - trough) * (decay ** 1.1)
    full_prices[0] = peak
    full_prices[-1] = trough

    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)

        progress = min(1.0, f / (total_frames - 12))
        current_day_idx = int(progress * 21)
        cur_days = days[:current_day_idx + 1]
        cur_prices = full_prices[:current_day_idx + 1]

        ax.plot(days, full_prices, color="#334155", lw=2, linestyle=":")
        ax.plot(cur_days, cur_prices, color=ACCENT_RED, lw=4.5)
        ax.fill_between(cur_days, cur_prices, peak, color=ACCENT_RED, alpha=0.2)

        if len(cur_days) > 0:
            ax.scatter([cur_days[-1]], [cur_prices[-1]], color=ACCENT_RED, s=200, edgecolor="white", lw=2)

        c_day = cur_days[-1] if len(cur_days) > 0 else 1
        c_price = cur_prices[-1] if len(cur_prices) > 0 else peak
        c_loss = ((c_price - peak) / peak) * 100

        badge = patches.FancyBboxPatch((1.5, 2300), 8.5, 450, boxstyle="round,pad=0.3",
                                      facecolor=PANEL_BG, edgecolor=ACCENT_RED, linewidth=2)
        ax.add_patch(badge)
        ax.text(2, 2620, f"DAY {c_day} OF 22", fontsize=26, fontweight="bold", color=ACCENT_RED)
        ax.text(2, 2500, f"S&P 500: {c_price:,.1f} pts ({c_loss:.1f}%)", fontsize=16, fontweight="bold", color=TEXT_MAIN)
        ax.text(2, 2400, "Fastest -30%+ Bear Market in History", fontsize=13, color=TEXT_MUTED)

        ax.set_title("Animation: S&P 500 Pandemic Collapse (-34% in 22 Days)", fontsize=22, fontweight="bold", pad=20)
        ax.set_xlabel("Trading Days (Feb 19 – Mar 23, 2020)", fontsize=14)
        ax.set_ylabel("S&P 500 Index Level", fontsize=14)
        ax.set_xlim(0.5, 22.5)
        ax.set_ylim(2100, 3550)
        ax.grid(True)
        yield fig

# ==========================================================
# ANIMATION 2: Scene 07/08 - Crowded Theater / "Fire" Bottleneck
# ==========================================================
def anim_scene_07_08(total_frames=60):
    np.random.seed(101)
    num_particles = 35
    px = np.random.uniform(-3.5, 1.5, num_particles)
    py = np.random.uniform(-1.8, 1.8, num_particles)

    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)
        ax.axis("off")

        is_fire = f >= 25

        bg_col = "#201215" if is_fire else PANEL_BG
        room = patches.Rectangle((-4, -2.2), 6.5, 4.4, facecolor=bg_col, edgecolor=ACCENT_RED if is_fire else TEXT_MUTED, lw=3)
        ax.add_patch(room)
        door = patches.Rectangle((2.5, -0.6), 0.3, 1.2, facecolor=ACCENT_RED if is_fire else ACCENT_GREEN, edgecolor="white", lw=2)
        ax.add_patch(door)
        ax.text(3.5, 0, "EXIT /\nMARKET DEPTH", ha="center", va="center",
                color=ACCENT_RED if is_fire else ACCENT_GREEN, fontsize=14, fontweight="bold")

        if not is_fire:
            px += np.random.uniform(-0.02, 0.05, num_particles)
            py += np.random.uniform(-0.02, 0.02, num_particles)
            px = np.clip(px, -3.8, 2.0)
            py = np.clip(py, -1.9, 1.9)
            cols = [ACCENT_GREEN] * num_particles
            status_title = "Normal Market: Orderly Liquidity Flow"
            status_col = ACCENT_GREEN
        else:
            target_x = 2.5
            target_y = 0.0
            dx = target_x - px
            dy = target_y - py
            dist = np.sqrt(dx**2 + dy**2) + 0.1
            px += (dx / dist) * 0.14 + np.random.uniform(-0.03, 0.03, num_particles)
            py += (dy / dist) * 0.14 + np.random.uniform(-0.03, 0.03, num_particles)
            px = np.clip(px, -3.8, 2.45)
            py = np.clip(py, -1.9, 1.9)
            cols = [ACCENT_RED] * num_particles
            status_title = 'ALARM TRIGGERED: "FIRE!" — Rush Creates the Jam'
            status_col = ACCENT_RED

            fire_badge = patches.FancyBboxPatch((-3.5, 1.2), 2.5, 0.8, boxstyle="round,pad=0.2",
                                                facecolor=ACCENT_RED, edgecolor="white", lw=2)
            ax.add_patch(fire_badge)
            ax.text(-2.25, 1.6, 'SHOUT OF "FIRE!"', ha="center", va="center", color="white", fontsize=14, fontweight="bold")

        ax.scatter(px, py, color=cols, s=170, edgecolor="white", lw=1.5, zorder=5)

        ax.text(-0.7, 2.6, status_title, ha="center", va="center", fontsize=20, fontweight="bold", color=status_col)
        ax.text(-0.7, -2.7, "Destruction occurs because the exit capacity cannot absorb aggregate liquidation volume.",
                ha="center", va="center", fontsize=14, color=TEXT_MAIN)

        ax.set_xlim(-4.5, 4.8)
        ax.set_ylim(-3.2, 3.2)
        yield fig

# ==========================================================
# ANIMATION 3: Scene 09 - Order Book Liquidity Evaporation
# ==========================================================
def anim_scene_09(total_frames=50):
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)

        prog = f / total_frames
        bid_multiplier = max(0.05, 1.0 - prog * 1.2)
        ask_multiplier = 1.0 + prog * 3.0

        prices_bids = np.array([98, 97, 96, 95, 94])
        qty_bids = np.array([400, 600, 900, 1200, 1500]) * bid_multiplier

        prices_asks = np.array([100, 101, 102, 103, 104, 105])
        qty_asks = np.array([500, 800, 1200, 1800, 2500, 3500]) * ask_multiplier

        ax.barh(prices_bids, qty_bids, color=ACCENT_GREEN, height=0.6, alpha=0.85, label="Buy Orders (Bids Draining)")
        ax.barh(prices_asks, qty_asks, color=ACCENT_RED, height=0.6, alpha=0.85, label="Sell Orders (Ask Wall Surge)")

        current_exec_price = 100 - prog * 8.5
        ax.axhline(current_exec_price, color=ACCENT_GOLD, lw=3, linestyle="--", label=f"Market Execution: ${current_exec_price:.2f}")

        ax.set_title("Animation: Real-Time Order Book Liquidity Evaporation", fontsize=20, fontweight="bold", pad=15)
        ax.set_xlabel("Depth / Number of Contracts Available", fontsize=13)
        ax.set_ylabel("Share Price ($)", fontsize=13)
        ax.set_xlim(0, 12000)
        ax.set_ylim(93, 106)
        ax.legend(loc="upper right", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=12)
        ax.grid(True, axis="x")
        yield fig

# ==========================================================
# ANIMATION 4: Scene 13 - Margin Call Wipeout
# ==========================================================
def anim_scene_13(total_frames=50):
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)

        prog = f / total_frames
        stock_price = 100 - prog * 12.0
        equity_val = max(0, stock_price - 90)
        debt_val = 90

        ax.bar(["10:1 Leveraged Asset"], [equity_val], color=ACCENT_GREEN if equity_val > 2 else ACCENT_RED,
               width=0.4, label=f"Investor Equity (${equity_val:.1f})")
        ax.bar(["10:1 Leveraged Asset"], [debt_val], bottom=[equity_val], color=ACCENT_GOLD,
               width=0.4, label="Broker Loan ($90 Debt)")

        if equity_val <= 0:
            badge = patches.FancyBboxPatch((-0.35, 95), 0.7, 18, boxstyle="round,pad=0.2",
                                          facecolor=ACCENT_RED, edgecolor="white", lw=2)
            ax.add_patch(badge)
            ax.text(0, 104, "MARGIN CALL TRIGGERED!", ha="center", va="center", color="white", fontweight="bold", fontsize=14)

        ax.set_ylim(0, 125)
        ax.set_ylabel("Dollar Value ($)", fontsize=13)
        ax.set_title(f"Animation: 10% Drop Wipes 100% Equity (Stock Price: ${stock_price:.1f})", fontsize=20, fontweight="bold", pad=15)
        ax.legend(loc="upper right", facecolor=PANEL_BG, edgecolor=PANEL_BORDER, fontsize=12)
        ax.grid(True, axis="y")
        yield fig

# ==========================================================
# ANIMATION 5: Scene 19 - Domino Chain 2008
# ==========================================================
def anim_scene_19(total_frames=60):
    dominos = [
        "1. Subprime Mortgages Default",
        "2. Bear Stearns Fails (Mar 2008)",
        "3. Lehman Brothers Files Bankruptcy (Sept 15)",
        "4. AIG $85B Emergency Bailout (Sept 17)",
        "5. Global Money Markets & Liquidity Freeze"
    ]
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)
        ax.axis("off")

        active_count = min(len(dominos), int((f / total_frames) * (len(dominos) + 1)))

        for i, text in enumerate(dominos):
            y = 2.0 - i * 0.95
            if i < active_count:
                col = ACCENT_RED if i >= 2 else ACCENT_GOLD
                bg = PANEL_BG
                border = col
                lw = 2.5
            else:
                col = TEXT_MUTED
                bg = "#111620"
                border = "#1E293B"
                lw = 1

            b = patches.FancyBboxPatch((-3.0, y-0.3), 6.0, 0.65, boxstyle="round,pad=0.2",
                                       facecolor=bg, edgecolor=border, lw=lw)
            ax.add_patch(b)
            ax.text(0, y, text, ha="center", va="center", color=col, fontweight="bold", fontsize=13)

        ax.text(0, 2.7, "Animation: The 2008 Domino Cascade", ha="center", va="center", fontsize=22, fontweight="bold", color=TEXT_MAIN)
        ax.set_xlim(-4, 4)
        ax.set_ylim(-2.6, 3.2)
        yield fig

# ==========================================================
# ANIMATION 6: Scene 23 - Circuit Breakers Siren & Halts
# ==========================================================
def anim_scene_23(total_frames=50):
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)
        ax.axis("off")

        flash = (f // 5) % 2 == 0
        border_col = ACCENT_RED if flash else "#7F1D1D"

        frame = patches.FancyBboxPatch((-4.5, -2.4), 9.0, 4.8, boxstyle="round,pad=0.3",
                                       facecolor="#1A0D0E" if flash else PANEL_BG,
                                       edgecolor=border_col, lw=4)
        ax.add_patch(frame)

        ax.text(0, 1.6, "NYSE EMERGENCY CIRCUIT BREAKER", ha="center", va="center",
                fontsize=24, fontweight="bold", color=ACCENT_RED)
        ax.text(0, 0.7, "LEVEL 1 HALT ACTIVATED (-7.0% IN S&P 500)", ha="center", va="center",
                fontsize=18, fontweight="bold", color="white")
        ax.text(0, -0.2, "ALL EQUITIES & DERIVATIVES TRADING SUSPENDED FOR 15 MINUTES", ha="center", va="center",
                fontsize=14, color=TEXT_MAIN)

        dates = "Triggered: March 9, March 12, March 16, March 18 (2020)"
        ax.text(0, -1.2, dates, ha="center", va="center", fontsize=14, fontweight="bold", color=ACCENT_GOLD)

        ax.set_xlim(-5, 5)
        ax.set_ylim(-2.8, 2.8)
        yield fig

# ==========================================================
# ANIMATION 7: Scene 24 - 2020 V-Shaped Recovery
# ==========================================================
def anim_scene_24(total_frames=60):
    t = np.linspace(0, 148, 150)
    v_curve = np.piecewise(t, [t <= 22, t > 22],
                           [lambda x: 3386.15 - (3386.15 - 2237.40) * (x/22)**1.2,
                            lambda x: 2237.40 + (3389.78 - 2237.40) * ((x-22)/(148-22))**0.85])
    v_curve[0] = 3386.15
    v_curve[22] = 2237.40
    v_curve[-1] = 3389.78

    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)

        prog = min(1.0, f / (total_frames - 8))
        cur_idx = int(prog * (len(t) - 1))
        cur_t = t[:cur_idx + 1]
        cur_v = v_curve[:cur_idx + 1]

        ax.plot(t, v_curve, color="#334155", lw=2, linestyle=":")
        ax.plot(cur_t, cur_v, color=ACCENT_GREEN if cur_idx > 22 else ACCENT_RED, lw=4)
        ax.axhline(3386.15, color=TEXT_MUTED, linestyle=":", alpha=0.7)

        if len(cur_t) > 0:
            ax.scatter([cur_t[-1]], [cur_v[-1]], color=ACCENT_GREEN if cur_idx > 22 else ACCENT_RED, s=180, edgecolor="white", lw=2)

        if cur_idx >= 22:
            stim = patches.FancyBboxPatch((28, 2550), 65, 400, boxstyle="round,pad=0.2",
                                          facecolor=PANEL_BG, edgecolor=ACCENT_GREEN, lw=2)
            ax.add_patch(stim)
            ax.text(60, 2800, "CENTRAL BANK LIQUIDITY INJECTION", ha="center", color=ACCENT_GREEN, fontweight="bold", fontsize=12)
            ax.text(60, 2680, "$3T+ Fed QE  •  $2.2T CARES Act", ha="center", color=TEXT_MAIN, fontsize=11)

        ax.set_title("Animation: S&P 500 V-Shaped Velocity Recovery", fontsize=20, fontweight="bold", pad=15)
        ax.set_xlabel("Trading Days from Peak (Feb 19 – Aug 18, 2020)", fontsize=13)
        ax.set_ylabel("S&P 500 Level", fontsize=13)
        ax.set_xlim(0, 150)
        ax.set_ylim(2100, 3650)
        ax.grid(True)
        yield fig

# ==========================================================
# ANIMATION 8: Scene 27 - Universal Mechanism Pipeline
# ==========================================================
def anim_scene_27(total_frames=60):
    stages = [
        ("1. ANY TRIGGER\n(Debt/CDO/Pandemic)", -3.6, ACCENT_RED),
        ("2. CONFIDENCE BREAK\n(Safety Shatters)", -1.2, ACCENT_GOLD),
        ("3. EXIT STAMPEDE\n(Liquidity Evaporation)", 1.2, ACCENT_CYAN),
        ("4. CASCADE CRASH\n(Forced Liquidations)", 3.6, ACCENT_PURPLE),
    ]
    for f in range(total_frames):
        fig = plt.figure(figsize=(16, 9), dpi=120)
        ax = fig.add_subplot(111)
        ax.axis("off")

        active_count = min(4, int((f / total_frames) * 5))

        for i, (title, x, col) in enumerate(stages):
            is_act = i < active_count
            box = patches.FancyBboxPatch((x-1.1, -1.0), 2.2, 2.0, boxstyle="round,pad=0.2",
                                         facecolor=PANEL_BG if is_act else "#111620",
                                         edgecolor=col if is_act else "#1E293B",
                                         lw=3 if is_act else 1)
            ax.add_patch(box)
            lines = title.split("\n")
            ax.text(x, 0.3, lines[0], ha="center", va="center", fontsize=12, fontweight="bold",
                    color=col if is_act else TEXT_MUTED)
            ax.text(x, -0.4, lines[1], ha="center", va="center", fontsize=10.5,
                    color=TEXT_MAIN if is_act else "#475569")

        for i in range(len(stages)-1):
            if i < active_count - 1:
                x_start = stages[i][1] + 1.15
                x_end = stages[i+1][1] - 1.15
                ax.annotate("", xy=(x_end, 0), xytext=(x_start, 0),
                            arrowprops=dict(arrowstyle="->", color=ACCENT_GOLD, lw=3))

        ax.text(0, 2.2, "Animation: The Universal Crash Mechanism", ha="center", va="center",
                fontsize=22, fontweight="bold", color=TEXT_MAIN)
        ax.set_xlim(-5, 5)
        ax.set_ylim(-3, 3)
        yield fig

def main():
    print("Starting video animation rendering pipeline...")
    render_frames_to_mp4(anim_scene_01, "Scene_01_sp500_crash_animation.mp4", fps=30, total_frames=60)
    render_frames_to_mp4(anim_scene_07_08, "Scene_07_08_crowded_room_metaphor.mp4", fps=30, total_frames=60)
    render_frames_to_mp4(anim_scene_09, "Scene_09_order_book_liquidity_drain.mp4", fps=30, total_frames=50)
    render_frames_to_mp4(anim_scene_13, "Scene_13_margin_call_wipeout.mp4", fps=30, total_frames=50)
    render_frames_to_mp4(anim_scene_19, "Scene_19_domino_cascade_2008.mp4", fps=30, total_frames=60)
    render_frames_to_mp4(anim_scene_23, "Scene_23_circuit_breakers_halt.mp4", fps=30, total_frames=50)
    render_frames_to_mp4(anim_scene_24, "Scene_24_v_shaped_recovery.mp4", fps=30, total_frames=60)
    render_frames_to_mp4(anim_scene_27, "Scene_27_universal_mechanism.mp4", fps=30, total_frames=60)
    print("All MP4 animations rendered successfully!")

if __name__ == "__main__":
    main()
