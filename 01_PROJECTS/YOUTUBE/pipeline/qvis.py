"""Quantrove Visual Density kit for Manim (visual-density.md v1).

Every scene subclasses QScene and sets ASSET = "<asset id>". Beat durations come from the
episode MASTER_TIMELINE.json (beat_align.py), so animations land on real VO word anchors.

    class M01_WORDS_TO_POINTS(QScene):
        ASSET = "M01_WORDS_TO_POINTS"
        def construct(self):
            self.setup_q()
            dot = Dot()
            self.beat(FadeIn(dot))             # beat 1: animations fill the beat, camera drifts
            self.beat(dot.animate.shift(RIGHT)) # beat 2 ...
            self.finish()                       # pads to the exact scene duration

Render: QTIMELINE=<path to MASTER_TIMELINE.json> manim -qh --fps 60 -r 1920,1080 file.py M01_WORDS_TO_POINTS
"""
import json, os, random
import numpy as np
from manim import *
from manim.animation.animation import prepare_animation
from manim_theme import (BACKGROUND, UI_STRUCTURE, SUCCESS, RISK, TEXT, CleanText, apply_manim_theme,
                         STAGE_CENTER, stage_fit)

apply_manim_theme(config, fps=60)
LIME, PUMPKIN, SLATE, OFFWHITE = SUCCESS, RISK, UI_STRUCTURE, TEXT
CAM_MAX = 1.08          # longs_style.json camera_push_max_scale


def load_beats(asset):
    """Return list of beat durations (s) for an asset from QTIMELINE, or None for preview mode."""
    path = os.environ.get("QTIMELINE")
    if not path:
        return None
    tl = json.load(open(path, encoding="utf-8"))
    for sc in tl["scenes"]:
        if sc["asset"] == asset:
            # snap boundaries to the 60 fps grid so rendered frames == timeline frames (no drift)
            f = [round(b["start"] * 60) for b in sc["beats"]] + [round(sc["beats"][-1]["end"] * 60)]
            return [(f[i + 1] - f[i]) / 60 for i in range(len(sc["beats"]))]
    raise KeyError(f"{asset} not in {path}")


def ambient_grid(spacing=0.8, opacity=0.32, drift=0.05):
    """Slow-drifting Charcoal Slate grid (never a flat background). Spans enough for 60 s of drift."""
    lines = VGroup(*[Line([x, -9, 0], [x, 9, 0]) for x in np.arange(-14, 14.01, spacing)],
                   *[Line([-14, y, 0], [14, y, 0]) for y in np.arange(-9, 9.01, spacing)])
    lines.set_stroke(SLATE, width=1.6, opacity=opacity)
    lines.add_updater(lambda m, dt: m.shift(drift * dt * np.array([1, 0.5, 0])))
    return lines


def ambient_particles(n=40, seed=7, opacity=0.35):
    """Sparse drifting particles (Off-White, tiny) for continuous motion."""
    rng = random.Random(seed)
    g = VGroup(*[Dot([rng.uniform(-7.5, 7.5), rng.uniform(-4.2, 4.2), 0], radius=rng.uniform(0.008, 0.02))
                 for _ in range(n)]).set_fill(OFFWHITE, opacity=opacity)
    vel = [np.array([rng.uniform(-0.05, 0.05), rng.uniform(0.02, 0.08), 0]) for _ in range(n)]

    def upd(m, dt):
        for d, v in zip(m, vel):
            d.shift(v * dt)
            if d.get_center()[1] > 4.3:
                d.shift(DOWN * 8.6)
    g.add_updater(upd)
    return g


class QScene(MovingCameraScene):
    ASSET = None
    PREVIEW_BEAT_S = 4.0   # used when no timeline is set (quick look renders)

    def setup_q(self, grid=True, particles=True):
        self.camera.background_color = BACKGROUND
        self.beats = load_beats(self.ASSET) or []
        self.beat_i, self._zoomed = 0, False
        if grid:
            self.add(ambient_grid())
        if particles:
            self.add(ambient_particles())

    def beat_len(self, i=None):
        i = self.beat_i if i is None else i
        return self.beats[i] if i < len(self.beats) else self.PREVIEW_BEAT_S

    def beat(self, *anims, run=None, cam=True, focus=None):
        """One beat = exactly its VO duration. Content anims take `run` s (default min(1.6, 60%)),
        the camera drifts (push-in <-> pull-back, <= CAM_MAX) across the whole beat."""
        dur = self.beat_len()
        run = min(run if run is not None else min(1.6, 0.6 * dur), dur)
        group = [prepare_animation(a).set_run_time(run) for a in anims]
        if cam:
            w = config.frame_width if self._zoomed else config.frame_width / CAM_MAX
            center = focus if focus is not None else (ORIGIN if self._zoomed else self.camera.frame.get_center())
            group.append(prepare_animation(self.camera.frame.animate.set(width=w).move_to(center)).set_run_time(dur))
            self._zoomed = not self._zoomed
        else:
            group.append(Wait(dur))
        self.play(AnimationGroup(*group, lag_ratio=0))
        self.beat_i += 1

    def hud(self, mob, corner=DR, buff=0.4):
        """Pin a label to the screen (tracks camera position and zoom), e.g. ILLUSTRATIVE / source tags."""
        frame, w0 = self.camera.frame, config.frame_width
        mob.to_corner(corner, buff=buff)
        rel, width0 = mob.get_center().copy(), mob.width
        mob.add_updater(lambda m: m.set(width=width0 * frame.width / w0)
                        .move_to(frame.get_center() + rel * frame.width / w0))
        return mob

    def finish(self):
        """Pad remaining timeline beats with moving holds so render length == timeline length."""
        if self.beats and self.beat_i > len(self.beats):
            raise RuntimeError(f"{self.ASSET}: {self.beat_i} beats played, timeline has {len(self.beats)}")
        while self.beat_i < len(self.beats):
            self.beat()


def txt(s, size=36, color=OFFWHITE, bold=True):
    return CleanText(s, font_size=size, color=color, weight=BOLD if bold else "MEDIUM")


def glow_dot(pos, color=LIME, r=0.07):
    """Dot with a soft halo (two low-opacity rings)."""
    return VGroup(Dot(pos, radius=r * 3.2, color=color).set_opacity(0.08),
                  Dot(pos, radius=r * 1.9, color=color).set_opacity(0.18),
                  Dot(pos, radius=r, color=color))


def label_dot(word, pos, color=LIME, r=0.07, size=26):
    d = glow_dot(pos, color, r)
    t = txt(word, size=size).next_to(d, UR, buff=0.08)
    return VGroup(d, t)


def counter(value_from, value_to, fmt="{:,.0f}", size=60, color=OFFWHITE):
    """ValueTracker-driven count-up (numbers never pop in)."""
    vt = ValueTracker(value_from)
    m = always_redraw(lambda: txt(fmt.format(vt.get_value()), size=size, color=color))
    return vt, m
