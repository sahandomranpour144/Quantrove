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
