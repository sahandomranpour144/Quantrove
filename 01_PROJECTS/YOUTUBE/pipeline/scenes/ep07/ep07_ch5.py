"""EP07 chapter 5 + close Manim scenes (S41 M16, S42 M16B, S43 M16C, S44 M17, S46 M18, S47 M19)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ep07_ch4 import *


def bottom_chip(scene, s, color=LIME, size=38):
    return scene.hud(chip(s, color, size), corner=DOWN, buff=1.85)


class M16_FULL_MAP_PULLBACK(QScene):
    ASSET = "M16_FULL_MAP_PULLBACK"

    def construct(self):
        self.setup_q()
        k0, mid = 2.4, (KING + QUEEN) / 2
        pj = Proj(self, spin=0.05, k=k0, off=(-k0 * mid[0], -k0 * mid[1]))
        cloud = pj.cloud(MAP_PTS, dim=0.45, lime_z=MAP_LIME_Z)
        halos = {n: pj.cloud(cluster_pts(n), r=0.1, color=LIME, opacity=0.3, dim=0)
                 for n in ["COUNTRIES", "FOODS", "MOTION", "MONEY", "RIVER", "TRAVEL"]}
        self.add(cloud, *halos.values())
        named = VGroup(*[pj.pin(label_dot(w, p), p) for w, p in
                         [("KING", KING), ("QUEEN", QUEEN), ("MAN", MAN), ("WOMAN", WOMAN)]])
        kq, mw = pj.link(KING, QUEEN, g=0), pj.link(MAN, WOMAN, g=0)
        self.add(kq, mw)
        # b1: the KING -> QUEEN arrow from the opening
        self.beat(FadeIn(named, scale=0.6), Succession(mw.g.animate(run_time=1.4).set_value(1),
                                                       kq.g.animate(run_time=1.6).set_value(1)), run=3.2)
        # b2: the camera pulls back through the clusters
        self.beat(pj.k.animate.set_value(MAP_K), pj.ox.animate.set_value(0), pj.oy.animate.set_value(0),
                  LaggedStart(*[h.dim.animate.set_value(0.8) for h in halos.values()], lag_ratio=0.15),
                  named.animate.set_opacity(0.4), run=2.0)
        # b3: the whole cloud is in frame
        self.beat(cloud.dim.animate.set_value(0.7), *[h.dim.animate.set_value(0.35) for h in halos.values()],
                  kq.o.animate.set_value(0.4), mw.o.animate.set_value(0.4), run=1.3)
        # b4: POSITION = MEANING
        c1 = bottom_chip(self, "POSITION = MEANING")
        self.beat(FadeIn(c1, shift=UP * 0.2), *[h.dim.animate(rate_func=there_and_back).set_value(1) for h in halos.values()],
                  run=1.5)
        # b5: similar words sit close together (clusters tighten visually)
        self.beat(*[h.dim.animate(rate_func=there_and_back).set_value(0.9) for h in halos.values()], run=2.2)
        # b6: DIRECTION = RELATIONSHIP
        c2 = bottom_chip(self, "DIRECTION = RELATIONSHIP")
        self.beat(FadeOut(c1), FadeIn(c2, shift=UP * 0.2), kq.o.animate.set_value(1), mw.o.animate.set_value(1),
                  named.animate.set_opacity(1), run=1.2)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M16B_CLOSE_NOT_TRUE(QScene):
    ASSET = "M16B_CLOSE_NOT_TRUE"

    def construct(self):
        self.setup_q()
        PC = np.array([-1.5, 0.2, 0])
        panel = RoundedRectangle(corner_radius=0.2, width=7.8, height=4.4, stroke_color=SLATE, stroke_width=3,
                                 fill_color=BACKGROUND, fill_opacity=0.5).move_to(PC)
        pts = np.c_[CLOUD[:, 0] * 0.55, CLOUD[:, 1] * 0.95, np.zeros(len(CLOUD))]
        pts = pts[(np.abs(pts[:, 0]) < 3.5) & (np.abs(pts[:, 1]) < 1.95)]
        bg = cloud_dots(pts + PC).set_opacity(0.3)
        bg.add_updater(lambda m, dt: m.shift(0.04 * dt * LEFT))
        ps, pc = np.array([-2.6, 0.45, 0]), np.array([-0.7, -0.05, 0])
        syd = VGroup(glow_dot(ps, LIME, 0.085), txt("SYDNEY", 32).next_to(ps, UP, buff=0.2))
        can = VGroup(glow_dot(pc, LIME, 0.085), txt("CANBERRA", 32).next_to(pc, DOWN, buff=0.2))
        link = Line(ps, pc, stroke_color=LIME, stroke_width=5)
        close = chip("CLOSE", LIME, 28).move_to([-0.45, 0.8, 0])
        q = txt("CAPITAL OF AUSTRALIA?", 30, OFFWHITE).move_to(PC + UP * 1.55)
        # b1: the map; two nearby points
        self.add(bg)
        self.beat(FadeIn(panel), FadeIn(syd, scale=0.5), FadeIn(can, scale=0.5), run=1.6)
        # b2: close in the map: a lime link
        self.beat(Create(link), FadeIn(close, scale=0.7), run=1.5)
        # b3: not the same as true: the question hovers between them
        self.beat(FadeIn(q, shift=DOWN * 0.3), close.animate.set_opacity(0.6),
                  Succession(Wait(1.2), Indicate(q, color=PUMPKIN, scale_factor=1.08)), run=1.4)
        # b4: side by side
        self.beat(Indicate(syd[0], color=LIME, scale_factor=1.8), Indicate(can[0], color=LIME, scale_factor=1.8), run=0.5)
        # b5: the map highlights both equally
        hs = Circle(radius=0.55, stroke_color=LIME, stroke_width=3).move_to(ps)
        hc = Circle(radius=0.55, stroke_color=LIME, stroke_width=3).move_to(pc)
        self.beat(Create(hs), Create(hc), run=1.2)
        # b6: related
        self.beat(link.animate.set_stroke(width=9), hs.animate.set_stroke(opacity=0.5), hc.animate.set_stroke(opacity=0.5),
                  run=1.2)
        # b7: only CANBERRA earns the check, outside the map
        chk = VGroup(txt("✓", 64, LIME), txt("CANBERRA", 32)).arrange(RIGHT, buff=0.3).move_to([4.25, 0.9, 0])
        need = VGroup(txt("NEEDS MORE", 32, LIME), txt("THAN GEOMETRY", 32, LIME)).arrange(DOWN, buff=0.15).move_to([4.25, -0.35, 0])
        self.beat(syd.animate.set_opacity(0.35), FadeIn(chk, shift=LEFT * 0.4), FadeIn(need, shift=LEFT * 0.4),
                  hs.animate.set_stroke(opacity=0.0), Succession(Wait(1.4), Indicate(chk[0], color=LIME, scale_factor=1.25)),
                  run=1.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M16C_YOUR_PROMPT(QScene):
    ASSET = "M16C_YOUR_PROMPT"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.05, k=MAP_K)
        cloud = pj.cloud(MAP_PTS, dim=0.3, lime_z=MAP_LIME_Z)
        self.add(cloud)
        words = ["plan", "a", "trip", "to", "lisbon"]
        box = RoundedRectangle(corner_radius=0.14, width=8.6, height=0.8, stroke_color=SLATE, stroke_width=3,
                               fill_color=BACKGROUND, fill_opacity=0.97).move_to(UP * 2.2)
        chips = VGroup(*[txt(w, 38) for w in words]).arrange(RIGHT, buff=0.32).move_to(box)
        cur = Rectangle(width=0.05, height=0.55, stroke_width=0, fill_color=LIME, fill_opacity=1)
        cur.next_to(chips[0], LEFT, buff=0.12)
        cur.add_updater(lambda m, dt: m.set_opacity(1 if int(self.renderer.time * 2.4) % 2 == 0 else 0.1))
        # b1: the prompt box types the sentence
        self.add(box)
        steps = [AnimationGroup(FadeIn(w, shift=RIGHT * 0.15), cur.animate.next_to(w, RIGHT, buff=0.12), run_time=0.4)
                 for w in chips]
        self.beat(FadeIn(cur), Succession(*steps), run=1.9)
        # b2: picture what happens first: the map brightens, the box glows
        glow = box.copy().set_fill(opacity=0).set_stroke(LIME, width=4)
        self.beat(cloud.dim.animate.set_value(0.6), FadeIn(glow), run=1.2)
        tgt = {"plan": CLUSTERS["TRAVEL"] + np.array([0.8, 0.2, 0.0]), "a": np.array([0.0, 0.15, 0.4]),
               "trip": CLUSTERS["TRAVEL"] + np.array([-0.2, -0.65, 0.2]), "to": np.array([-1.9, 0.3, 0.0]),
               "lisbon": CLUSTERS["COUNTRIES"] + np.array([-0.4, -0.55, 0.25])}
        dots = {w: pj.pin(label_dot(w.upper(), p, LIME, r=0.07, size=24), p) for w, p in tgt.items()}
        tag(self, "ILLUSTRATIVE")
        # b3: each token lifts off the box and flies into the map as a point
        flights = []
        for c, w in zip(chips, words):
            flights.append(Succession(c.animate(run_time=0.9).move_to(pj.P(tgt[w]) + UP * 0.1).scale(0.35).set_opacity(0),
                                      FadeIn(dots[w], scale=0.4, run_time=0.5)))
        self.beat(LaggedStart(*flights, lag_ratio=0.22), FadeOut(cur), FadeOut(glow), run=3.0)
        # b4: they land near TRAVEL and COUNTRIES; arrows begin to move them
        halo_t = pj.cloud(cluster_pts("TRAVEL"), r=0.1, color=LIME, opacity=0.3, dim=0)
        halo_c = pj.cloud(cluster_pts("COUNTRIES"), r=0.1, color=LIME, opacity=0.3, dim=0)
        self.add(halo_t, halo_c)
        nudges = [pj.link(tgt[a], tgt[b], LIME, 4, g=0, trim=0.22) for a, b in [("plan", "trip"), ("trip", "lisbon"),
                                                                              ("to", "lisbon")]]
        self.add(*nudges)
        self.beat(halo_t.dim.animate.set_value(1), halo_c.dim.animate.set_value(1),
                  LaggedStart(*[n.g.animate.set_value(1) for n in nudges], lag_ratio=0.25),
                  Succession(Wait(2.0), AnimationGroup(*[n.o.animate.set_value(0) for n in nudges], run_time=1.0)),
                  FadeOut(box), run=3.1)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M17_TEXT_TO_POINTS(QScene):
    ASSET = "M17_TEXT_TO_POINTS"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.05, k=MAP_K)
        cloud = pj.cloud(MAP_PTS, dim=0.5, reveal=0, lime_z=MAP_LIME_Z)
        self.add(cloud)
        lines = ["i miss my grandmother's soup", "the market closed lower today", "she is a brilliant surgeon",
                 "he stayed home with the kids", "paris is lovely in spring", "the train was late again"]
        starts = [LEFT * 3.4 + UP * 2.1, RIGHT * 3.4 + DOWN * 2.0, LEFT * 3.4 + DOWN * 1.9,
                  RIGHT * 3.4 + UP * 2.1, LEFT * 3.6 + UP * 0.1, RIGHT * 3.6 + DOWN * 0.1]
        ends = ["FOODS", "MONEY", "BIAS", "BIAS", "COUNTRIES", "MOTION"]
        sents = VGroup(*[txt(s, 28, bold=False).set_opacity(0.85).move_to(p) for s, p in zip(lines, starts)])
        # b1: human sentences scroll in from every side
        self.beat(LaggedStart(*[FadeIn(s, shift=-p * 0.06) for s, p in zip(sents, starts)], lag_ratio=0.2),
                  cloud.reveal.animate.set_value(0.2), run=2.2)
        # b2: they condense into points of the map
        self.beat(LaggedStart(*[s.animate.move_to(pj.P(CLUSTERS[e]) * 0.9).scale(0.12).set_opacity(0)
                                for s, e in zip(sents, ends)], lag_ratio=0.12),
                  cloud.reveal.animate.set_value(1.0), run=2.2)
        FR, IT = np.array([3.0, 2.0, 0.3]), np.array([3.2, 0.7, -0.3])
        VC = np.array([1.5, 0.4, 0.0])
        VS = np.array([1.8, 0.4, 0.2])
        mk = lambda w, p, c=OFFWHITE, s=22: pj.pin(label_dot(w, p, c, r=0.06, size=s), p)
        caps = VGroup(mk("FRANCE", FR, LIME), mk("PARIS", FR + VC, LIME), mk("ITALY", IT, LIME), mk("ROME", IT + VC, LIME))
        ster = VGroup(mk("MAN", MAN, PUMPKIN), mk("PROGRAMMER", MAN + VS, PUMPKIN), mk("WOMAN", WOMAN, PUMPKIN),
                      mk("HOMEMAKER", WOMAN + VS, PUMPKIN))
        lc = [pj.link(FR, FR + VC, LIME, 6), pj.link(IT, IT + VC, LIME, 6)]
        ls = [pj.link(MAN, MAN + VS, PUMPKIN, 6), pj.link(WOMAN, WOMAN + VS, PUMPKIN, 6)]
        self.add(*lc, *ls)
        # b3: the capitals arrow glows lime
        self.beat(FadeIn(caps, scale=0.6), *[a.g.animate.set_value(1) for a in lc], cloud.dim.animate.set_value(0.35),
                  run=2.2, focus=pj.P(FR) * 0.3)
        # b4: the stereotype arrow glows Pumpkin beside it
        self.beat(FadeIn(ster, scale=0.6), *[a.g.animate.set_value(1) for a in ls], run=1.8,
                  focus=pj.P(MAN) * 0.25)
        # b5: both in one frame; mirror frame with a ruler attached; push in
        mirror = RoundedRectangle(corner_radius=0.2, width=11.6, height=4.9, stroke_color=OFFWHITE, stroke_width=3,
                                  stroke_opacity=0.55, fill_opacity=0).move_to(UP * 0.0)
        ruler = VGroup(Line(mirror.get_corner(DR) + LEFT * 8 + UP * 0.0, mirror.get_corner(DR), stroke_color=LIME, stroke_width=4),
                       *[Line(mirror.get_corner(DR) + LEFT * (0.4 * i), mirror.get_corner(DR) + LEFT * (0.4 * i) + UP * (0.22 if i % 5 == 0 else 0.12),
                              stroke_color=LIME, stroke_width=3) for i in range(0, 21)])
        self.beat(Create(mirror), LaggedStart(*[FadeIn(t) for t in ruler], lag_ratio=0.03), run=2.0,
                  focus=pj.P((MAN + FR) / 2) * 0.2)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M18_CTA_SPLIT(QScene):
    ASSET = "M18_CTA_SPLIT"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.06, k=1.0)
        cloud = pj.cloud(MAP_CORE, dim=0.7, lime_z=MAP_CORE_LIME)
        self.add(cloud)
        # chart on the right half
        W, Hc, X0, YB = 5.2, 2.7, 0.9, -1.55
        r = np.random.default_rng(46)
        n = 70
        y = np.cumsum(r.normal(0.05, 0.12, n)); y[int(n * 0.72):] -= np.linspace(0, 1.6, n - int(n * 0.72)) * 1.0
        y = (y - y.min()) / (y.max() - y.min())
        P = [np.array([X0 + W * i / (n - 1), YB + Hc * (0.1 + 0.85 * v), 0]) for i, v in enumerate(y)]
        k = int(n * 0.72)
        line_ok = VMobject(stroke_color=LIME, stroke_width=5).set_points_as_corners(P[:k + 1])
        line_bad = VMobject(stroke_color=PUMPKIN, stroke_width=5).set_points_as_corners(P[k:])
        axes = VGroup(Line([X0, YB, 0], [X0 + W, YB, 0], stroke_color=SLATE, stroke_width=3),
                      Line([X0, YB, 0], [X0, YB + Hc + 0.2, 0], stroke_color=SLATE, stroke_width=3),
                      *[Line([X0, YB + Hc * f, 0], [X0 + W, YB + Hc * f, 0], stroke_color=SLATE, stroke_width=1.5)
                        .set_opacity(0.5) for f in (0.33, 0.66, 1.0)])
        head = Dot(P[0], radius=0.08, color=LIME)
        tag(self, "ILLUSTRATIVE")
        # b1: the word cloud shrinks to the left half
        self.beat(pj.k.animate.set_value(0.52), pj.ox.animate.set_value(-3.3), pj.oy.animate.set_value(0.0),
                  FadeIn(axes), run=3.0)
        # b2: a price chart draws on the right half
        self.add(head)
        self.beat(Create(line_ok, run_time=3.2), MoveAlongPath(head, line_ok, run_time=3.2),
                  Succession(Wait(3.2), AnimationGroup(Create(line_bad, run_time=1.4),
                                                       head.animate(run_time=1.4).set_color(PUMPKIN).move_to(P[-1]))),
                  run=4.8)
        # b3: dashed bridge between the two halves
        a, b = np.array([-1.4, 0.2, 0]), np.array([X0 - 0.15, YB + Hc * 0.6, 0])
        bridge = ArcBetweenPoints(a, b, angle=-0.7, stroke_color=LIME, stroke_width=4)
        dashes = DashedVMobject(bridge, num_dashes=22).set_stroke(LIME, 4)
        self.beat(Create(dashes), run=1.2)
        # b4: signal flows across the bridge
        pulses = [Dot(a, radius=0.09, color=LIME) for _ in range(3)]
        self.beat(LaggedStart(*[MoveAlongPath(p, bridge, run_time=0.9) for p in pulses], lag_ratio=0.3),
                  Indicate(dashes, color=LIME, scale_factor=1.02), run=1.7)
        # b5: the frame clears toward the end-screen layout
        self.beat(FadeOut(axes), FadeOut(line_ok), FadeOut(line_bad), FadeOut(head), FadeOut(dashes),
                  *[FadeOut(p) for p in pulses], pj.k.animate.set_value(0.8), pj.ox.animate.set_value(0),
                  cloud.dim.animate.set_value(0.3), run=1.2)
        self.finish()


class M19_END_SCREEN_BG(QScene):
    ASSET = "M19_END_SCREEN_BG"

    def construct(self):
        self.setup_q(grid=False)
        self.add(ambient_grid(opacity=0.2))
        pj = Proj(self, spin=0.04, k=0.8)
        cloud = pj.cloud(MAP_PTS, dim=0.3, reveal=0, lime_z=MAP_LIME_Z)
        self.add(cloud)
        veil = Rectangle(width=30, height=18, stroke_width=0, fill_color=BACKGROUND, fill_opacity=1)
        # one 20 s beat: the cloud drifts, then dips to the background colour in the last second
        self.beat(cloud.reveal.animate.set_value(1), pj.k.animate.set_value(0.72),
                  Succession(Wait(18.8), FadeIn(veil, run_time=1.1)), run=20.0, cam=False)
        self.finish()
