import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.patches import Rectangle, FancyBboxPatch

# 1. Setup fonts
font_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
bold_path = os.path.join(font_dir, "Nohemi-Bold.ttf")
med_path = os.path.join(font_dir, "Nohemi-Medium.ttf")

bold_font = fm.FontProperties(fname=bold_path)
med_font = fm.FontProperties(fname=med_path)

# 2. Exact Brand Tokens
BG_COLOR = "#202322"       # Raisin Black
UI_STRUCTURE = "#233D4C"   # Charcoal Slate
SUCCESS = "#C3D809"        # Power Lime
RISK = "#FD802E"           # Pumpkin
TEXT = "#E6EDF3"           # Off-White

# 3. Create High-Res Institutional Chart
fig = plt.figure(figsize=(16, 9), dpi=150, facecolor=BG_COLOR)
gs = fig.add_gridspec(nrows=3, ncols=3, height_ratios=[0.18, 0.72, 0.10], width_ratios=[1, 1, 1],
                      left=0.07, right=0.93, top=0.92, bottom=0.06, hspace=0.35, wspace=0.25)

# --- Top Header & Telemetry Cards ---
ax_header = fig.add_subplot(gs[0, :])
ax_header.set_facecolor(BG_COLOR)
ax_header.axis("off")

# Title & Subtitle
ax_header.text(0.0, 0.75, "INSTITUTIONAL DATA INTELLIGENCE", fontproperties=bold_font,
               fontsize=22, color=TEXT, va="center", ha="left")
ax_header.text(0.0, 0.25, "Bloomberg-Terminal Precision | Predictive Order Flow & Tail Risk Telemetry",
               fontproperties=med_font, fontsize=12, color=TEXT, alpha=0.75, va="center", ha="left")

# Metric Badges on the right
badges = [
    ("CONVERGENCE", "+42.8%", SUCCESS),
    ("ANOMALY RISK", "9.4%", RISK),
    ("CHROME [SYSTEM]", "ACTIVE", UI_STRUCTURE)
]

for idx, (label, val, col) in enumerate(badges):
    bx = 0.52 + idx * 0.165
    rect = FancyBboxPatch((bx, 0.05), 0.15, 0.85, boxstyle="round,pad=0.02,rounding_size=0.04",
                          facecolor=BG_COLOR, edgecolor=UI_STRUCTURE, linewidth=1.5)
    ax_header.add_patch(rect)
    ax_header.text(bx + 0.075, 0.65, label, fontproperties=med_font, fontsize=8.5,
                   color=TEXT, alpha=0.6, ha="center", va="center")
    val_color = col if col != UI_STRUCTURE else SUCCESS
    ax_header.text(bx + 0.075, 0.28, val, fontproperties=bold_font, fontsize=13,
                   color=val_color, ha="center", va="center")

# --- Main Subplot 1: Convergence Curves (2 cols wide) ---
ax_main = fig.add_subplot(gs[1, :2])
ax_main.set_facecolor(BG_COLOR)

# Generate synthetic quantitative data
np.random.seed(42)
x = np.linspace(0, 100, 250)
trend = 100 + 0.55 * x + 4.5 * np.sin(x / 7.0)
upper_bound = trend + 8 + 1.5 * np.cos(x / 5.0)
lower_bound = trend - 8 - 1.5 * np.cos(x / 5.0)

# Outlier anomaly trigger window (x between 62 and 78)
anomaly_mask = (x >= 60) & (x <= 80)
risk_series = trend.copy()
risk_series[anomaly_mask] -= 16.5 + 4 * np.sin((x[anomaly_mask] - 60) * np.pi / 20)

# Plot main series
ax_main.plot(x, trend, color=SUCCESS, linewidth=2.8, label="Active Model Alpha (Validated Upward)")
ax_main.plot(x[anomaly_mask], risk_series[anomaly_mask], color=RISK, linewidth=2.8,
             linestyle="--", label="Liquidity Outlier / Cascade Risk (Down Move)")
ax_main.fill_between(x, lower_bound, upper_bound, color=UI_STRUCTURE, alpha=0.25, label="Calibrated Confidence Band (+/-2 SD)")

# Grid & Spines
ax_main.grid(True, linestyle="--", linewidth=0.7, color=UI_STRUCTURE, alpha=0.8)
for spine in ax_main.spines.values():
    spine.set_color(UI_STRUCTURE)
    spine.set_linewidth(1.5)

# Ticks and Labels
ax_main.tick_params(colors=TEXT, labelsize=10, width=1.2, length=5)
for label in ax_main.get_xticklabels() + ax_main.get_yticklabels():
    label.set_fontproperties(med_font)

ax_main.set_xlabel("Time Horizon [t+ms]", fontproperties=med_font, fontsize=11, color=TEXT, labelpad=8)
ax_main.set_ylabel("Order Flow Liquidity Index", fontproperties=med_font, fontsize=11, color=TEXT, labelpad=8)
ax_main.set_title("ALPHA CONVERGENCE & TAIL RISK DETECTION", fontproperties=bold_font,
                  fontsize=13, color=TEXT, pad=12, loc="left")

# Institutional Callout Box on the chart
idx_70 = np.argmin(np.abs(x - 70))
ax_main.annotate(
    "STATISTICAL ANOMALY\nTarget Drawdown: -16.5%",
    xy=(x[idx_70], risk_series[idx_70]),
    xytext=(72, 85),
    arrowprops=dict(arrowstyle="->", color=RISK, lw=1.8),
    fontproperties=bold_font,
    fontsize=9.5,
    color=TEXT,
    bbox=dict(boxstyle="round,pad=0.5", facecolor=BG_COLOR, edgecolor=RISK, lw=1.5)
)

# Legend
leg = ax_main.legend(prop=med_font, loc="upper left", facecolor=BG_COLOR, edgecolor=UI_STRUCTURE, framealpha=0.95)
for text in leg.get_texts():
    text.set_color(TEXT)
    text.set_fontsize(9.5)

# --- Subplot 2: Order Book Imbalance / Candlestick Representation (1 col wide) ---
ax_side = fig.add_subplot(gs[1, 2])
ax_side.set_facecolor(BG_COLOR)

# Draw simulated candlesticks without generic red/green: Up = Power Lime, Down = Pumpkin
candle_data = [
    (1, 102, 107, 109, 100, True),
    (2, 106, 111, 113, 105, True),
    (3, 111, 104, 112, 102, False),
    (4, 104, 108, 110, 103, True),
    (5, 108, 97,  109, 95,  False),
    (6, 97,  91,  98,  89,  False),
    (7, 92,  99,  101, 90,  True),
    (8, 99,  106, 108, 98,  True),
]

for idx, op, cl, hi, lo, is_up in candle_data:
    col = SUCCESS if is_up else RISK
    # Wick
    ax_side.plot([idx, idx], [lo, hi], color=col, linewidth=1.5)
    # Body
    body_bottom = min(op, cl)
    body_height = max(1.0, abs(cl - op))
    rect = Rectangle((idx - 0.28, body_bottom), 0.56, body_height,
                     facecolor=col, edgecolor=col, alpha=0.92, linewidth=1.2)
    ax_side.add_patch(rect)

ax_side.set_xlim(0.2, 8.8)
ax_side.set_ylim(85, 118)
ax_side.grid(True, linestyle="--", linewidth=0.7, color=UI_STRUCTURE, alpha=0.8)
for spine in ax_side.spines.values():
    spine.set_color(UI_STRUCTURE)
    spine.set_linewidth(1.5)

ax_side.tick_params(colors=TEXT, labelsize=10, width=1.2, length=5)
for label in ax_side.get_xticklabels() + ax_side.get_yticklabels():
    label.set_fontproperties(med_font)

ax_side.set_xlabel("Market Session [k]", fontproperties=med_font, fontsize=11, color=TEXT, labelpad=8)
ax_side.set_ylabel("Price Level", fontproperties=med_font, fontsize=11, color=TEXT, labelpad=8)
ax_side.set_title("CANDLESTICK DISCIPLINE", fontproperties=bold_font,
                  fontsize=13, color=TEXT, pad=12, loc="left")

# Side Annotation: Up=Lime, Down=Pumpkin
ax_side.text(0.05, 0.92, "Up = Power Lime (#C3D809)\nDown/Risk = Pumpkin (#FD802E)\nZero Generic Red/Green",
             transform=ax_side.transAxes, fontproperties=med_font, fontsize=8.5,
             color=TEXT, alpha=0.9, va="top",
             bbox=dict(boxstyle="square,pad=0.4", facecolor=BG_COLOR, edgecolor=UI_STRUCTURE, lw=1.2))

# --- Bottom Bar: Brand Palette Swatch Tokens ---
ax_footer = fig.add_subplot(gs[2, :])
ax_footer.set_facecolor(BG_COLOR)
ax_footer.axis("off")

tokens = [
    ("BACKGROUND", "#202322", "Raisin Black (All Canvases & Fills)", BG_COLOR),
    ("UI_STRUCTURE", "#233D4C", "Charcoal Slate (Grids, Axes, Chrome ONLY)", UI_STRUCTURE),
    ("SUCCESS", "#C3D809", "Power Lime (Upward Moves, Validations, Emphasis)", SUCCESS),
    ("RISK", "#FD802E", "Pumpkin (Anomalies, Outliers, Downward Moves)", RISK),
    ("TEXT", "#E6EDF3", "Off-White (Headings, Numbers, All Copy)", TEXT),
]

swatch_w = 0.185
for i, (name, hex_code, desc, fill_col) in enumerate(tokens):
    sx = i * 0.203
    # Color chip
    chip = Rectangle((sx, 0.45), 0.024, 0.45, facecolor=fill_col, edgecolor=UI_STRUCTURE, linewidth=1.2)
    ax_footer.add_patch(chip)
    # Token text
    ax_footer.text(sx + 0.032, 0.80, f"{name}: {hex_code}", fontproperties=bold_font,
                   fontsize=9.5, color=TEXT, va="center")
    ax_footer.text(sx + 0.032, 0.48, desc, fontproperties=med_font,
                   fontsize=7.2, color=TEXT, alpha=0.65, va="center")

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "brand_palette_showcase.png")
plt.savefig(output_path, facecolor=BG_COLOR, edgecolor="none")
plt.close()
print(f"Chart saved to {output_path}")
