"""
Quantrove Manim Theme: Institutional Data Intelligence
Reads single source of truth from brand/brand_tokens.json.
Provides:
  - Theme colors and palettes (Raisin Black, Charcoal Slate, Power Lime, Pumpkin, Off-White)
  - apply_manim_theme() for global config
  - CleanText() using Nohemi vector scaling (ref_size=72) with Inter fallback
  - Institutional UI components: axes, grids, candlestick vectors, telemetry cards
"""

import os
import json
from typing import Optional, Any

# Locate brand/brand_tokens.json
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_CURRENT_DIR)))
_BRAND_TOKENS_PATH = os.path.join(_WORKSPACE_ROOT, "brand", "brand_tokens.json")

# Fallback path relative to pipeline
if not os.path.exists(_BRAND_TOKENS_PATH):
    _BRAND_TOKENS_PATH = os.path.join(os.path.dirname(_CURRENT_DIR), "brand", "brand_tokens.json")

def load_brand_tokens() -> dict:
    if os.path.exists(_BRAND_TOKENS_PATH):
        with open(_BRAND_TOKENS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    # Hardcoded safety fallback strictly adhering to Quantrove brand tokens
    return {
        "palette": {
            "BACKGROUND": "#202322",
            "UI_STRUCTURE": "#233D4C",
            "SUCCESS": "#C3D809",
            "RISK": "#FD802E",
            "TEXT": "#E6EDF3"
        },
        "typography": {
            "primary_font": "Nohemi",
            "fallback_font": "Inter",
            "weights": {"bold": 700, "medium": 500}
        }
    }

TOKENS = load_brand_tokens()

# Palette Constants
BACKGROUND = TOKENS["palette"]["BACKGROUND"]        # #202322 Raisin Black: canvases & card fills
UI_STRUCTURE = TOKENS["palette"]["UI_STRUCTURE"]    # #233D4C Charcoal Slate: grids, axes, chrome (lines ONLY)
SUCCESS = TOKENS["palette"]["SUCCESS"]              # #C3D809 Power Lime: primary accent / upward moves
RISK = TOKENS["palette"]["RISK"]                    # #FD802E Pumpkin: secondary accent / risk / down moves
TEXT = TOKENS["palette"]["TEXT"]                    # #E6EDF3 Off-White: all text, numbers, headings

# Semantic Aliases
BG_DARK = BACKGROUND
GRID_COLOR = UI_STRUCTURE
AXES_COLOR = UI_STRUCTURE
ACCENT_UP = SUCCESS
ACCENT_DOWN = RISK
ACCENT_LIME = SUCCESS
ACCENT_PUMPKIN = RISK
TEXT_PRIMARY = TEXT

# Typography Constants
FONT_PRIMARY = TOKENS["typography"]["primary_font"]      # "Nohemi"
FONT_FALLBACK = TOKENS["typography"]["fallback_font"]    # "Inter"

WEIGHT_BOLD = TOKENS["typography"]["weights"].get("bold", 700)
WEIGHT_MEDIUM = TOKENS["typography"]["weights"].get("medium", 500)


def apply_manim_theme(manim_config: Any, is_vertical: bool = False, fps: int = 60) -> None:
    """
    Applies the Quantrove Institutional Data Intelligence theme to Manim config.
    """
    manim_config.background_color = BACKGROUND
    manim_config.frame_rate = fps
    if is_vertical:
        manim_config.pixel_width = 1080
        manim_config.pixel_height = 1920
        manim_config.frame_width = 4.5
        manim_config.frame_height = 8.0
    else:
        manim_config.pixel_width = 1920
        manim_config.pixel_height = 1080
        manim_config.frame_width = 14.222222222222221
        manim_config.frame_height = 8.0

# Stage Constants (1920x1080 @ 135 px/unit = 14.2222 x 8.0 units)
# manim_stage: x [96, 1824], y [190, 856] (px from top-left)
STAGE_X_MIN = -6.4
STAGE_X_MAX = 6.4
STAGE_Y_TOP = 2.5925925925925926       # (540 - 190) / 135
STAGE_Y_BOTTOM = -2.3407407407407408    # (540 - 856) / 135
STAGE_WIDTH = 12.8
STAGE_HEIGHT = 4.933333333333334
import numpy as np
STAGE_CENTER = np.array([0.0, 0.1259259259259259, 0.0])

def stage_fit(mobject_or_group, max_w: float = 12.2, max_h: float = 4.5, center: np.ndarray = STAGE_CENTER):
    """
    Wrap scene content in a stage_fit helper:
    Scales to fit within manim_stage, preserves aspect ratio, and centers at STAGE_CENTER.
    Guarantees nothing draws in the forbidden caption lane (y 864-1080) or top popup band (y 56-176).
    """
    w = mobject_or_group.width
    h = mobject_or_group.height
    scale_factor = 1.0
    if w > max_w:
        scale_factor = min(scale_factor, max_w / max(w, 0.001))
    if h > max_h:
        scale_factor = min(scale_factor, max_h / max(h, 0.001))
    if scale_factor < 1.0:
        mobject_or_group.scale(scale_factor)
    mobject_or_group.move_to(center)
    return mobject_or_group, scale_factor


_NOHEMI_FONT_FILE = os.path.join(_WORKSPACE_ROOT, "01_PROJECTS", "YOUTUBE", "pipeline", "remotion_engine", "public", "fonts", "Nohemi-Bold.ttf")
_NOHEMI_CMAP = set()
if os.path.exists(_NOHEMI_FONT_FILE):
    try:
        from fontTools.ttLib import TTFont
        _NOHEMI_CMAP = set(TTFont(_NOHEMI_FONT_FILE).getBestCmap().keys())
    except Exception:
        pass

def CleanText(
    text: str,
    font_size: int = 24,
    color: str = TEXT,
    font: Optional[str] = None,
    weight: Optional[str] = None,
    **kwargs
):
    """
    Render native Manim Text() objects with CleanText vector scaling.
    Uses Nohemi font with intelligent fallback to Segoe UI when text contains
    characters not supported in Nohemi (Greek letters, math symbols, arrows).
    Renders at ref_size=72 and scales down to target_size / 72 to eliminate
    Pango glyph advance quantization scattering ('m ar ket' bug).
    """
    try:
        from manim import Text
    except ImportError:
        raise RuntimeError("CleanText requires manim to be installed in the active python environment.")

    if font is None:
        target_font = FONT_PRIMARY
        if _NOHEMI_CMAP and any(ord(c) not in _NOHEMI_CMAP for c in text):
            target_font = "Segoe UI"
    else:
        target_font = font

    ref_size = 72
    scale_factor = font_size / ref_size

    # Defensive guard: UI_STRUCTURE (#233D4C) is forbidden for text per layout contract
    if color == UI_STRUCTURE or str(color).upper() == "#233D4C":
        color = TEXT
        if "fill_opacity" not in kwargs and "opacity" not in kwargs:
            kwargs["fill_opacity"] = 0.60

    # Pop opacity if present
    fill_op = kwargs.pop("fill_opacity", kwargs.pop("opacity", None))

    # Try primary font first, fall back to fallback font if requested or failed
    try:
        t = Text(text, font=target_font, font_size=ref_size, color=color, weight=weight or "NORMAL", **kwargs)
    except Exception:
        t = Text(text, font=FONT_FALLBACK, font_size=ref_size, color=color, weight=weight or "NORMAL", **kwargs)

    if fill_op is not None:
        t.set_opacity(fill_op)

    t.scale(scale_factor)
    return t


def create_candle(center_pt, height: float, is_up: bool, width: float = 0.22):
    """
    Institutional Candlestick Vector:
    Upward = Power Lime (#C3D809)
    Downward = Pumpkin (#FD802E)
    Strictly zero generic red/green.
    """
    from manim import Rectangle, Line, UP, DOWN

    col = SUCCESS if is_up else RISK
    body = Rectangle(
        width=width,
        height=max(0.04, abs(height)),
        color=col,
        fill_color=col,
        fill_opacity=0.92,
        stroke_width=1.5
    ).move_to(center_pt)

    wick_len = max(0.12, abs(height) * 0.4)
    wick = Line(
        center_pt + UP * (abs(height) / 2.0 + wick_len),
        center_pt + DOWN * (abs(height) / 2.0 + wick_len),
        color=col,
        stroke_width=1.5
    )
    return body, wick


def create_telemetry_card(width: float = 6.0, height: float = 4.0, border_color: str = UI_STRUCTURE):
    """
    Institutional Telemetry Card Wireframe.
    Background: Raisin Black (#202322)
    Border: Charcoal Slate (#233D4C)
    """
    from manim import RoundedRectangle
    return RoundedRectangle(
        corner_radius=0.15,
        width=width,
        height=height,
        color=border_color,
        fill_color=BACKGROUND,
        fill_opacity=0.95,
        stroke_width=2.0
    )
