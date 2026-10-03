"""EP07 intro scenes (S1-S2). Render: see qvis.py docstring."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from qvis import *

rng = np.random.default_rng(7)
CLOUD = rng.normal(0, 1, (320, 3)) * np.array([3.8, 1.7, 2.2])
CLOUD = CLOUD[np.abs(CLOUD[:, 1]) < 2.2]
# KING - MAN + WOMAN = QUEEN, exactly (gender offset = WOMAN - MAN)
MAN, WOMAN = np.array([-2.6, -1.1, 0.4]), np.array([-2.6, 0.9, 0.1])
KING = np.array([1.9, -1.0, -0.2])
QUEEN = KING + (WOMAN - MAN)


def cloud_dots(points, r=0.048):
    g = VGroup(*[Dot(p, radius=r) for p in points])
    for d, p in zip(g, points):
        d.set_fill(OFFWHITE if p[2] < 0.8 else LIME, opacity=float(np.clip(0.35 + 0.15 * p[2], 0.15, 0.9)))
    return g


class M01_WORDS_TO_POINTS(QScene):
    ASSET = "M01_WORDS_TO_POINTS"

    def construct(self):
        self.setup_q()
        words = ["Every", "word", "becomes", "a", "point"]
        sent = VGroup(*[txt(w, 44) for w in words]).arrange(RIGHT, buff=0.28).move_to(UP * 0.3)
        # b1: sentence appears, words lift off into points
        self.beat(LaggedStart(*[FadeIn(w, shift=UP * 0.2) for w in sent], lag_ratio=0.15), run=1.2)
        cloud = cloud_dots(CLOUD)
        targets = VGroup(*[Dot(CLOUD[i], radius=0.06, color=LIME) for i in range(len(words))])
        # b2: words collapse into points, the cloud blooms around them
        self.beat(LaggedStart(*[ReplacementTransform(w, t) for w, t in zip(sent, targets)], lag_ratio=0.1),
                  LaggedStart(*[FadeIn(d, scale=0.3) for d in cloud], lag_ratio=0.004), run=2.0)
        space = VGroup(cloud, targets)
        space.add_updater(lambda m, dt: m.rotate(0.12 * dt, axis=UP, about_point=ORIGIN))
        # b3: coordinates snap onto one point
        probe = targets[1]
        coord = txt("(0.21, −0.64, 0.33, …)", 26).next_to(probe, UR, buff=0.15)
        coord.add_updater(lambda m: m.next_to(probe, UR, buff=0.15))
        tag = self.hud(txt("ILLUSTRATIVE", 16, OFFWHITE, bold=False).set_opacity(0.6))
        self.beat(Write(coord), FadeIn(tag), run=1.0)
        space.clear_updaters()
        # b4: KING highlights
        named = {w: label_dot(w, p) for w, p in [("KING", KING), ("MAN", MAN), ("WOMAN", WOMAN)]}
        self.beat(cloud.animate.set_opacity(0.28), FadeOut(targets), FadeOut(coord), GrowFromCenter(named["KING"]), run=1.0,
                  focus=KING * 0.4)
        # b5: MAN -> WOMAN arrow, then copied onto KING
        gender = Arrow(MAN, WOMAN, buff=0.08, color=LIME, stroke_width=5)
        self.beat(FadeIn(named["MAN"]), FadeIn(named["WOMAN"]), GrowArrow(gender), run=1.2)
        moved = gender.copy()
        queen = label_dot("QUEEN", QUEEN, color=LIME)
        ring = Circle(radius=0.28, color=LIME, stroke_width=3).move_to(QUEEN)
        # b6: arrow travels to KING's tip and lands on QUEEN
        self.beat(moved.animate.shift(KING - MAN), FadeIn(queen, scale=1.4), Create(ring), run=1.4,
                  focus=(KING + QUEEN) / 2 * 0.5)
        self.finish()


# ---------------------------------------------------------------------------------------------
# Shared "map" kit for every scene that revisits the word cloud (S2, S18, S19, S22, S23, S37,
# S41-S47): same CLOUD, same cluster coordinates, same KING/QUEEN geometry everywhere.
# ---------------------------------------------------------------------------------------------
MAP_K = 0.72   # zoom at which the full map (CLOUD + MORE) fills the frame
CLUSTERS = {
    "COUNTRIES": np.array([-3.3, 1.45, -1.0]),
    "FOODS": np.array([3.2, 1.35, 1.2]),
    "MOTION": np.array([0.4, -1.75, 1.8]),
    "MONEY": np.array([3.4, -1.25, -1.3]),
    "RIVER": np.array([-3.6, -1.35, 1.0]),
    "TRAVEL": np.array([-0.5, 1.75, -1.9]),
    "BIAS": np.array([1.2, 0.35, 2.5]),
}


def cluster_pts(name, n=26, spread=0.32):
    r = np.random.default_rng(sum(map(ord, name)))
    return CLUSTERS[name] + r.normal(0, spread, (n, 3))


_r11 = np.random.default_rng(11)
MORE = _r11.normal(0, 1, (700, 3)) * np.array([4.8, 2.0, 2.6])
MORE = MORE[np.abs(MORE[:, 1]) < 3.0]
CLUSTER_PTS = np.vstack([cluster_pts(n) for n in CLUSTERS])
MAP_PTS = np.vstack([CLOUD, CLUSTER_PTS, MORE])          # the whole map, in this order
# lime tint only on the original M01 cloud's front points; the rest of the map stays Off-White
MAP_LIME_Z = np.r_[np.full(len(CLOUD), 0.8), np.full(len(CLUSTER_PTS) + len(MORE), 9.0)]


class Proj:
    """Orthographic 3D projector run as a *scene* updater (after all animations each frame):
    slow orbit about the vertical axis, zoom `k`, screen offset (ox, oy). Pinned mobjects keep
    their 3D anchor while ordinary FadeIn / set_opacity animations still run on them."""

    def __init__(self, scene, spin=0.05, k=1.0, off=(0.0, 0.0), th=0.0):
        self.th, self.spin = th, spin
        self.k, self.ox, self.oy = ValueTracker(k), ValueTracker(off[0]), ValueTracker(off[1])
        scene.add(self.k, self.ox, self.oy)
        self.pins, self.clouds, self.links = [], [], []
        scene.add_updater(self.update)

    def P(self, p):
        p = np.asarray(p() if callable(p) else p, float)
        c, s, k = np.cos(self.th), np.sin(self.th), self.k.get_value()
        return np.array([(c * p[0] + s * p[2]) * k + self.ox.get_value(), p[1] * k + self.oy.get_value(), 0])

    LEVELS = 16

    def cloud(self, pts, r=0.048, color=None, opacity=0.25, reveal=1.0, dim=1.0, seed=3, lime_z=None):
        """Dots for `pts` (same look as cloud_dots), drawn as a few multi-subpath layers bucketed by
        color and opacity so thousands of points render fast. Visibility = base * dim * staggered
        reveal; animate `g.dim` / `g.reveal` (ValueTrackers), never the layers themselves."""
        pts = np.asarray(pts, float)
        if color is None:
            lime_z = 0.8 if lime_z is None else lime_z
            palette, cols = [OFFWHITE, LIME], (pts[:, 2] >= lime_z).astype(int)
            base = np.clip(0.35 + 0.15 * pts[:, 2], 0.15, 0.9)
        else:
            palette, cols, base = [color], np.zeros(len(pts), int), np.full(len(pts), opacity)
        L = self.LEVELS
        g = VGroup(*[VMobject(fill_color=c, fill_opacity=(q + 1) / L, stroke_width=0)
                     for c in palette for q in range(L)])
        g.pts, g.cols, g.base, g.tmpl = pts, cols, base, Circle(radius=r).points
        g.order = np.random.default_rng(seed).uniform(0, 0.85, len(pts))
        g.reveal, g.dim = ValueTracker(reveal), ValueTracker(dim)
        self.clouds.append(g)
        self._draw_cloud(g)
        return g

    def pin(self, mob, p, idx=0, offset=ORIGIN):
        """Keep mob[idx] (or the whole mob if idx is None) on the projection of 3D point p."""
        self.pins.append((mob, p, idx, np.asarray(offset, float)))
        self._place(mob, p, idx, np.asarray(offset, float))
        return mob

    def link(self, a, b, color=LIME, width=5, cls=Arrow, g=0.0, o=1.0, trim=0.09, **kw):
        """Arrow/Line between two 3D points (arrays or callables). Grow via .g, fade via .o."""
        m = VMobject()
        m.a, m.b, m.cls, m.kw, m.trim = a, b, cls, dict(color=color, stroke_width=width, **kw), trim
        m.g, m.o = ValueTracker(g), ValueTracker(o)
        self.links.append(m)
        self._draw_link(m)
        return m

    def _place(self, mob, p, idx, off):
        anchor = mob.get_center() if idx is None else mob[idx].get_center()
        mob.shift(self.P(p) + off - anchor)

    def _draw_cloud(self, g):
        c, s, k = np.cos(self.th), np.sin(self.th), self.k.get_value()
        X = (c * g.pts[:, 0] + s * g.pts[:, 2]) * k + self.ox.get_value()
        Y = g.pts[:, 1] * k + self.oy.get_value()
        f = g.base * g.dim.get_value() * np.clip((g.reveal.get_value() - g.order) * 7, 0, 1)
        L = self.LEVELS
        q = np.clip(np.round(f * L).astype(int), 0, L)
        key = np.where(q > 0, g.cols * L + q - 1, -1)
        P = np.stack([X, Y, np.zeros_like(X)], axis=1)
        for j, layer in enumerate(g):
            idx = np.nonzero(key == j)[0]
            layer.points = (g.tmpl[None] + P[idx, None]).reshape(-1, 3) if len(idx) else np.zeros((0, 3))

    def _draw_link(self, m):
        A, B = self.P(m.a), self.P(m.b)
        u = B - A
        L = np.linalg.norm(u)
        g, o = m.g.get_value(), m.o.get_value()
        if L < 2 * m.trim + 0.05 or g < 0.02 or o < 0.01:
            m.become(Line(A, A + RIGHT * 1e-3).set_stroke(opacity=0))
            return
        u = u / L
        A, B = A + u * m.trim, B - u * m.trim
        E = A + (B - A) * g
        if m.cls is Arrow:
            new = Arrow(A, E, buff=0, tip_length=0.22, max_tip_length_to_length_ratio=0.35, **m.kw)
        else:
            new = m.cls(A, E, **m.kw)
        m.become(new.set_opacity(o))

    def update(self, dt):
        self.th += self.spin * dt
        for g in self.clouds:
            self._draw_cloud(g)
        for mob, p, idx, off in self.pins:
            self._place(mob, p, idx, off)
        for m in self.links:
            self._draw_link(m)


def tag(scene, s, corner=DR):
    """Pinned ILLUSTRATIVE / source tag inside the safe area (clear of the caption lane)."""
    return scene.hud(txt(s, 16, bold=False).set_opacity(0.6), corner=corner, buff=np.array([0.8, 1.78, 0]))


def flicker(n=3):
    """Rate function 0 -> 1 that flickers n times on the way (pulses / warnings)."""
    return lambda t: min(1.0, 1.25 * t) * (0.55 + 0.45 * np.cos(2 * n * PI * t))


class M02_MAP_CLUSTERS(QScene):
    ASSET = "M02_MAP_CLUSTERS"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.05, k=1.0)
        cloud = pj.cloud(MAP_PTS, dim=0.6, reveal=0, lime_z=MAP_LIME_Z)
        cloud.order[:len(CLOUD)] = -1           # the M01 cloud is already there; the rest reveals
        named = VGroup(*[pj.pin(label_dot(w, p), p) for w, p in
                         [("KING", KING), ("QUEEN", QUEEN), ("MAN", MAN), ("WOMAN", WOMAN)]])
        arrows = [pj.link(MAN, WOMAN, g=1), pj.link(KING, QUEEN, g=1)]
        self.add(cloud, named, *arrows)
        # b1: pull back, thousands of points
        self.beat(pj.k.animate.set_value(MAP_K), cloud.reveal.animate.set_value(0.45),
                  named.animate.set_opacity(0.35), *[a.o.animate.set_value(0.35) for a in arrows], run=1.9)
        # b2: sentences stream in from the edges and condense into the cloud
        lines = ["the queen opened parliament", "rates rose at the bank", "we walked along the river",
                 "paris is lovely in spring", "she ran to catch the train", "fresh bread and hot coffee"]
        starts = [LEFT * 4.6 + UP * 2.1, RIGHT * 4.4 + DOWN * 1.9, LEFT * 4.4 + DOWN * 1.8,
                  RIGHT * 4.6 + UP * 2.0, LEFT * 4.8 + UP * 0.2, RIGHT * 4.8 + DOWN * 0.1]
        ends = ["TRAVEL", "MONEY", "RIVER", "COUNTRIES", "MOTION", "FOODS"]
        sents = VGroup(*[txt(s, 28, bold=False).set_opacity(0.8).move_to(p) for s, p in zip(lines, starts)])
        flows = [Succession(FadeIn(s, shift=-p * 0.05),
                            s.animate.move_to(pj.P(CLUSTERS[e]) * 0.9).scale(0.12).set_opacity(0))
                 for s, p, e in zip(sents, starts, ends)]
        self.beat(LaggedStart(*flows, lag_ratio=0.22), cloud.reveal.animate.set_value(1.0),
                  FadeOut(named), *[a.o.animate.set_value(0) for a in arrows], run=5.0)
        # b3: clusters glow one by one
        lit = ["COUNTRIES", "FOODS", "MOTION", "MONEY", "RIVER", "TRAVEL"]
        halos = {n: pj.cloud(cluster_pts(n), r=0.1, color=LIME, opacity=0.3, dim=0) for n in lit}
        halos["BIAS"] = pj.cloud(cluster_pts("BIAS"), r=0.1, color=PUMPKIN, opacity=0.6, dim=0)
        self.add(*halos.values())
        self.beat(LaggedStart(*[halos[n].dim.animate.set_value(1) for n in lit], lag_ratio=0.3), run=1.9)
        # b4: one Pumpkin cluster flickers (foreshadow, unlabeled)
        self.beat(halos["BIAS"].dim.animate(rate_func=flicker(4)).set_value(1),
                  *[halos[n].dim.animate.set_value(0.5) for n in lit], run=1.9,
                  focus=pj.P(CLUSTERS["BIAS"]) * 0.5)
        # b5: slow drift; the pumpkin cluster pulses once more
        self.beat(pj.k.animate.set_value(MAP_K * 0.94),
                  Succession(Wait(1.6), halos["BIAS"].dim.animate(rate_func=there_and_back).set_value(0.3)),
                  run=4.2)
        self.finish()
