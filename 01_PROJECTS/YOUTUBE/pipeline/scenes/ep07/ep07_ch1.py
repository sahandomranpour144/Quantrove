"""EP07 chapter 1 Manim scenes (S6 M04, S8 M03, S9 M03B). Render: see PRODUCTION_BRIEF.md."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ep07_intro import *


def card(head, body, w=3.7, h=0.5):
    box = RoundedRectangle(corner_radius=0.08, width=w, height=h, stroke_color=SLATE, stroke_width=2.5,
                           fill_color=BACKGROUND, fill_opacity=0.96)
    t = VGroup(txt(head, 22, LIME), txt(body, 22, bold=False)).arrange(RIGHT, buff=0.18)
    return VGroup(box, t.move_to(box))


def chip(s, color=OFFWHITE, size=28):
    t = txt(s, size, bold=False)
    box = SurroundingRectangle(t, buff=0.18, corner_radius=0.1, stroke_color=color, stroke_width=2.5,
                               fill_color=BACKGROUND, fill_opacity=0.96)
    return VGroup(box, t)


class M04_RULES_PILE(QScene):
    ASSET = "M04_RULES_PILE"

    def construct(self):
        self.setup_q()
        rules = [("IF", "noun + adjective"), ("THEN", "swap the order"), ("EXCEPT", "proper names"),
                 ("IF", "verb ends in -ed"), ("THEN", "mark past tense"), ("EXCEPT", "irregular verbs"),
                 ("IF", "word is bank"), ("THEN", "check the subject"), ("EXCEPT", "idioms"),
                 ("IF", "two nouns in a row")]
        r = np.random.default_rng(4)
        cards = VGroup(*[card(h, b).move_to([2.3 + r.uniform(-0.15, 0.15), -2.0 + 0.47 * i, 0])
                         .rotate(r.uniform(-0.035, 0.035)) for i, (h, b) in enumerate(rules)])
        # b1: rule cards stack up fast, camera tilts up the pile
        self.beat(LaggedStart(*[FadeIn(c, shift=DOWN * 0.7) for c in cards], lag_ratio=0.3), run=3.2,
                  focus=UP * 0.5 + RIGHT * 0.8)
        # b2: a demo sentence passes cleanly
        demo = chip("the cat sat", LIME).move_to([-6.0, 0.9, 0])
        check = txt("✓", 40, LIME).next_to(demo, RIGHT, buff=0.25)
        demo_to = [-2.2, 0.9, 0]
        self.beat(demo.animate.move_to(demo_to), FadeIn(check.move_to(np.array(demo_to) + RIGHT * 1.6), scale=1.6), run=0.8)
        # b3: a real sentence hits the stack; it topples and the cards scatter
        real = chip("the old man the boats", PUMPKIN).move_to([-6.2, -0.4, 0])
        falls = []
        for i, c in enumerate(cards):
            dx, ang = 0.9 + 0.35 * i + r.uniform(-0.3, 0.3), r.uniform(-0.9, 0.9)
            tgt = [min(2.0 + dx, 5.6), -2.0 + r.uniform(0, 0.5) + 0.05 * (i % 3), 0]
            falls.append(c.animate.rotate(ang).move_to(tgt).set_stroke(PUMPKIN, opacity=0.8))
        self.beat(Succession(real.animate(run_time=0.8).move_to([-0.4, -0.4, 0]),
                             AnimationGroup(LaggedStart(*reversed(falls), lag_ratio=0.06, run_time=1.6),
                                            real.animate(run_time=1.6).move_to([0.3, -0.4, 0]),
                                            VGroup(demo, check).animate(run_time=1.6).set_opacity(0.35))),
                  run=2.7, focus=RIGHT * 1.2 + DOWN * 0.4)
        self.finish()


# One-hot space: HOTEL, MOTEL, BANANA on the three unit axes (oblique projection of 3D)
O3 = np.array([0.0, -0.45, 0])
EX, EY, EZ = np.array([2.5, -1.05, 0]), np.array([0, 2.6, 0]), np.array([-2.5, -1.05, 0])
H3, M3, B3 = O3 + EX, O3 + EY, O3 + EZ
CENT = (H3 + M3 + B3) / 3


def onehot_space():
    axes = VGroup(*[Line(O3 - 0.25 * e, O3 + 1.18 * e, stroke_color=SLATE, stroke_width=3) for e in (EX, EY, EZ)])
    origin = Dot(O3, radius=0.05, color=OFFWHITE).set_opacity(0.6)
    pts = {}
    for w, p, vec, side in [("HOTEL", H3, "[1, 0, 0]", RIGHT), ("MOTEL", M3, "[0, 1, 0]", RIGHT),
                            ("BANANA", B3, "[0, 0, 1]", LEFT)]:
        d = glow_dot(p, LIME, 0.075)
        lab = VGroup(txt(w, 30), txt(vec, 22, bold=False).set_opacity(0.85)).arrange(DOWN, buff=0.1,
                                                                                      aligned_edge=-side)
        lab.next_to(d, side, buff=0.2)
        pts[w] = VGroup(d, lab)
    return axes, origin, pts


def edge(a, b, color=LIME):
    e = Line(a, b, stroke_color=color, stroke_width=6)
    mid = (a + b) / 2
    n = mid - CENT
    lab = txt("√2", 32).move_to(mid + n / np.linalg.norm(n) * 0.42)
    return e, lab


class M03_EQUAL_DISTANCE(QScene):
    ASSET = "M03_EQUAL_DISTANCE"

    def construct(self):
        self.setup_q()
        axes, origin, pts = onehot_space()
        # b1: three axes, words on the unit points
        self.beat(LaggedStart(*[Create(a) for a in axes], lag_ratio=0.2), FadeIn(origin),
                  LaggedStart(*[FadeIn(p, scale=0.6) for p in pts.values()], lag_ratio=0.25), run=1.6)
        hm, hb, mb = edge(H3, M3), edge(H3, B3), edge(M3, B3)
        # b2: lime edge HOTEL-MOTEL, label sqrt2
        self.beat(Succession(Create(hm[0], run_time=1.2), Write(hm[1], run_time=0.8),
                             Indicate(pts["MOTEL"][0], color=LIME, scale_factor=1.4, run_time=1.0)),
                  run=3.6, focus=(H3 + M3) / 2 * 0.4)
        # b3: identical edge HOTEL-BANANA, same label
        self.beat(Create(hb[0]), Write(hb[1]), run=1.5, focus=(H3 + B3) / 2 * 0.4)
        # b4: all three edges equal; triangle pulses Pumpkin
        tri = Polygon(H3, M3, B3, stroke_width=0, fill_color=PUMPKIN, fill_opacity=0)
        self.add(tri)
        edges = VGroup(hm[0], hb[0], mb[0])
        self.beat(Succession(AnimationGroup(Create(mb[0]), Write(mb[1]), run_time=1.2),
                             AnimationGroup(edges.animate.set_color(PUMPKIN),
                                            tri.animate(rate_func=there_and_back).set_fill(opacity=0.22),
                                            run_time=1.4),
                             tri.animate(run_time=0.8).set_fill(opacity=0.08)),
                  run=3.4, focus=CENT * 0.3)
        self.finish()


class M03B_NO_SIMILARITY(QScene):
    ASSET = "M03B_NO_SIMILARITY"

    def construct(self):
        self.setup_q()
        axes, origin, pts = onehot_space()
        hm, hb, mb = edge(H3, M3, PUMPKIN), edge(H3, B3, PUMPKIN), edge(M3, B3, PUMPKIN)
        tri = Polygon(H3, M3, B3, stroke_width=0, fill_color=PUMPKIN, fill_opacity=0.08)
        roots = VGroup(hm[1], hb[1], mb[1])
        self.add(tri, axes, origin, hm[0], hb[0], mb[0], roots, *pts.values())
        # b1: lime SIMILAR? probe touches HOTEL and MOTEL
        probe = chip("SIMILAR?", LIME, 30).move_to([4.6, 0.9, 0])
        def wires(a, b):
            return VGroup(*[DashedLine(probe.get_left() + DOWN * 0.1, p, stroke_color=LIME, stroke_width=3,
                                       dash_length=0.12) for p in (a, b)])
        w = wires(H3, M3)
        self.beat(FadeIn(probe, shift=LEFT * 0.4), roots.animate.set_opacity(0.3),
                  LaggedStart(*[Create(x) for x in w], lag_ratio=0.3), run=2.0)
        # b2: readout returns 0
        def readout(a, b):
            g = VGroup(txt(f"{a} · {b} =", 26, bold=False), txt("0", 34, PUMPKIN)).arrange(RIGHT, buff=0.18)
            return g.next_to(probe, DOWN, buff=0.35)
        ro = readout("[1,0,0]", "[0,1,0]")
        zeros = VGroup(*[txt("0", 30, PUMPKIN).move_to((a + b) / 2 * 0.72 + CENT * 0.28)
                         for a, b in ((H3, M3), (H3, B3), (M3, B3))])
        self.beat(Write(ro), run=1.3)
        # b3: probe tries every pair, all 0
        w2, w3 = wires(H3, B3), wires(M3, B3)
        ro2, ro3 = readout("[1,0,0]", "[0,0,1]"), readout("[0,1,0]", "[0,0,1]")
        self.beat(Succession(AnimationGroup(FadeIn(zeros[0], scale=1.5), run_time=0.5),
                             AnimationGroup(Transform(w, w2), Transform(ro, ro2), run_time=0.9),
                             FadeIn(zeros[1], scale=1.5, run_time=0.4),
                             AnimationGroup(Transform(w, w3), Transform(ro, ro3), run_time=0.9),
                             FadeIn(zeros[2], scale=1.5, run_time=0.4)), run=3.5)
        # b4: the triangle dims; caption NO MEANING INSIDE
        cap = txt("NO MEANING INSIDE", 40).move_to([3.9, -0.3, 0])
        under = Line(cap.get_corner(DL) + DOWN * 0.15, cap.get_corner(DR) + DOWN * 0.15, stroke_color=PUMPKIN,
                     stroke_width=4)
        everything = VGroup(tri, axes, origin, hm[0], hb[0], mb[0], roots, *pts.values(), zeros)
        self.beat(Succession(AnimationGroup(everything.animate.set_opacity(0.3), FadeOut(probe), FadeOut(ro), FadeOut(w),
                                            run_time=1.4),
                             AnimationGroup(FadeIn(cap, shift=UP * 0.2), Create(under), run_time=1.2)),
                  run=3.3, focus=RIGHT * 1.2)
        self.finish()
