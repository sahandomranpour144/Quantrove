"""EP07 chapter 3 Manim scenes (S23 M10, S24 M11, S28 M12, S29 M13). Render: see PRODUCTION_BRIEF.md."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ep07_ch2 import *


def lab_left(s, size=34):
    return txt(s, size, bold=False)


# ---------------------------------------------------------------------------------------------
class M10_KING_QUEEN(QScene):
    ASSET = "M10_KING_QUEEN"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.05, k=1.0)  # slow orbit: MAN/WOMAN and KING/QUEEN pairs never cross on screen
        cloud = pj.cloud(MAP_CORE, dim=0.35, lime_z=MAP_CORE_LIME)
        self.add(cloud)
        def side_label(w, p, left):
            g = label_dot(w, p)
            if left:   # MAN/WOMAN labels left, KING/QUEEN right: no collisions while the map orbits
                g[1].next_to(g[0], UL, buff=0.08)
            return pj.pin(g, p)
        king, man, woman, queen = [side_label(w, p, w in ("MAN", "WOMAN")) for w, p in
                                   [("KING", KING), ("MAN", MAN), ("WOMAN", WOMAN), ("QUEEN", QUEEN)]]
        # b1: KING appears; the map orbits
        self.beat(FadeIn(king, scale=0.5), run=0.9)
        # b2: MAN -> WOMAN arrow in lime
        gender = pj.link(MAN, WOMAN, LIME, 5)
        self.add(gender)
        self.beat(FadeIn(man), FadeIn(woman), gender.g.animate.set_value(1), run=1.8)
        # b3: the arrow copies itself to KING's tip; QUEEN is where it lands
        s, off = ValueTracker(0), KING - MAN
        copy = pj.link(lambda: MAN + off * s.get_value(), lambda: WOMAN + off * s.get_value(), LIME, 5, g=1, o=0)
        ring = pj.pin(Circle(radius=0.34, stroke_color=LIME, stroke_width=4), QUEEN, idx=None)
        self.add(copy, s)
        self.beat(copy.o.animate.set_value(1), s.animate.set_value(1), gender.o.animate.set_value(0.4),
                  Succession(Wait(1.5), AnimationGroup(FadeIn(queen, scale=1.4), FadeIn(ring, scale=0.4), run_time=0.9)),
                  run=2.5, focus=pj.P((KING + QUEEN) / 2) * 0.3)
        # b4: nearest-neighbour ring pulses around QUEEN, then the honest note
        note = self.hud(chip("INPUT WORDS EXCLUDED FROM SEARCH", PUMPKIN, 22), corner=DOWN, buff=1.9)
        self.beat(Succession(Indicate(ring, color=LIME, scale_factor=1.7, run_time=0.9),
                             Indicate(ring, color=LIME, scale_factor=1.7, run_time=0.9),
                             FadeIn(note, shift=UP * 0.2, run_time=0.8)), run=2.6)
        # b5: the starting words are left out of the search (KING would often win)
        ex = VGroup(*[pj.pin(DashedVMobject(Circle(radius=0.3, stroke_color=PUMPKIN, stroke_width=3), num_dashes=14),
                             p, idx=None) for p in (KING, MAN, WOMAN)])
        self.beat(LaggedStart(*[Create(e) for e in ex], lag_ratio=0.25), run=1.7)
        # b6: but the direction is real; the arrow locks onto QUEEN
        self.beat(Indicate(ring, color=LIME, scale_factor=1.9), Indicate(queen, color=LIME, scale_factor=1.25),
                  ex.animate.set_opacity(0.35), run=1.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
def plane(title, pairs, vec_noise, w=6.6, h=4.3):
    """pairs: [(src_label, dst_label, src_pos)]; returns (group, arrows). Local coords, centered near origin."""
    frame = RoundedRectangle(corner_radius=0.15, width=w, height=h, stroke_color=SLATE, stroke_width=2.5,
                             fill_color=BACKGROUND, fill_opacity=0.55)
    head = txt(title, 26, LIME).move_to(frame.get_corner(UL) + np.array([1.3, -0.4, 0]))
    items, arrows = [], []
    for (a, b, p), v in zip(pairs, vec_noise):
        p = np.array([*p, 0.0])
        q = p + np.array([*v, 0.0])
        da, db = glow_dot(p, OFFWHITE, 0.07), glow_dot(q, LIME, 0.07)
        la = txt(a, 30).next_to(da, LEFT, buff=0.18)
        lb = txt(b, 30).next_to(db, RIGHT, buff=0.18)
        arr = Arrow(p, q, buff=0.14, stroke_width=6, color=LIME, tip_length=0.26)
        items.append(VGroup(da, la, db, lb))
        arrows.append(arr)
    return VGroup(frame, head), items, arrows


class M11_PARALLEL_ARROWS(QScene):
    ASSET = "M11_PARALLEL_ARROWS"

    def construct(self):
        self.setup_q()
        cap_base, cap_items, cap_arr = plane(
            "CAPITALS", [("FRANCE", "PARIS", (-2.1, -1.2)), ("ITALY", "ROME", (-2.0, -0.15)),
                         ("JAPAN", "TOKYO", (-2.3, 0.85))], [(3.6, 0.55), (3.7, 0.6), (3.5, 0.5)], w=9.2, h=3.7)
        gr_base, gr_items, gr_arr = plane(
            "PAST TENSE", [("WALKING", "WALKED", (-2.3, 0.5)), ("SWIMMING", "SWAM", (-2.3, -0.9))],
            [(3.5, -0.55), (3.55, -0.6)], w=9.2, h=3.7)
        cap = VGroup(cap_base, *cap_items, *cap_arr).move_to(ORIGIN + UP * 0.1)
        gram = VGroup(gr_base, *gr_items, *gr_arr).move_to(ORIGIN + UP * 0.1)
        # b1: FRANCE -> PARIS
        self.beat(FadeIn(cap_base), FadeIn(cap_items[0], scale=0.6), GrowArrow(cap_arr[0]), run=1.5)
        # b2: ITALY -> ROME, parallel
        self.beat(FadeIn(cap_items[1], scale=0.6), GrowArrow(cap_arr[1]), run=2.0)
        # b3: JAPAN -> TOKYO joins
        self.beat(FadeIn(cap_items[2], scale=0.6), GrowArrow(cap_arr[2]), run=1.0)
        # b4: cut to the grammar plane: WALKING -> WALKED
        self.beat(Succession(FadeOut(cap, run_time=0.6),
                             AnimationGroup(FadeIn(gr_base), FadeIn(gr_items[0], scale=0.6), run_time=1.2),
                             GrowArrow(gr_arr[0], run_time=1.4)), run=3.2)
        # b5: SWIMMING -> SWAM, parallel
        self.beat(FadeIn(gr_items[1], scale=0.6), GrowArrow(gr_arr[1]), run=1.6)
        # b6: both planes side by side, NO RULE WRITTEN
        k = 0.66
        self.add(cap)
        cap.set_opacity(1)
        note = chip("NO RULE WRITTEN", LIME, 30).move_to(DOWN * 2.15)
        self.beat(FadeIn(cap), cap.animate.scale(k).move_to([-3.1, 0.3, 0]),
                  gram.animate.scale(k).move_to([3.1, 0.3, 0]), FadeIn(note, shift=UP * 0.2), run=1.8)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M12_BIAS_ARROW(QScene):
    ASSET = "M12_BIAS_ARROW"

    def construct(self):
        self.setup_q()
        bg = cloud_dots(np.c_[CLOUD[:, :2] * 0.95, np.zeros(len(CLOUD))]).set_opacity(0.2)
        bg.add_updater(lambda m, dt: m.shift(0.05 * dt * LEFT))
        self.add(bg)
        head = VGroup(txt("2016", 44, LIME), txt("·  Bolukbasi et al.", 34, bold=False)).arrange(RIGHT, buff=0.25)
        head.move_to(UP * 2.3)
        V = np.array([3.9, 0.7, 0])
        pm, pw, pf = np.array([-4.5, 1.0, 0]), np.array([-4.5, -0.4, 0]), np.array([-4.5, -1.8, 0])
        mk = lambda w, p, c, d: VGroup(glow_dot(p, c, 0.075), txt(w, 30).next_to(p, d, buff=0.2))
        man, woman, france = mk("MAN", pm, OFFWHITE, LEFT), mk("WOMAN", pw, OFFWHITE, LEFT), mk("FRANCE", pf, OFFWHITE, LEFT)
        prog = mk("COMPUTER PROGRAMMER", pm + V, LIME, RIGHT)
        home = mk("HOMEMAKER", pw + V, PUMPKIN, RIGHT)
        paris = mk("PARIS", pf + V * 0.98 + np.array([0, 0.03, 0]), OFFWHITE, RIGHT)
        a1 = Arrow(pm, pm + V, buff=0.14, stroke_width=6, color=LIME, tip_length=0.26)
        a2 = Arrow(pw, pw + V, buff=0.14, stroke_width=6, color=LIME, tip_length=0.26)
        a3 = Arrow(pf, pf + V * 0.98, buff=0.14, stroke_width=5, color=OFFWHITE, tip_length=0.24).set_opacity(0.5)
        src = self.hud(txt("GOOGLE NEWS VECTORS", 18, bold=False).set_opacity(0.7), corner=DR, buff=np.array([0.8, 1.78, 0]))
        # b1: header
        self.beat(Write(head), run=1.6)
        # b2: same arithmetic on the Google News vectors; the words appear
        self.beat(FadeIn(man, scale=0.6), FadeIn(woman, scale=0.6), FadeIn(src), run=1.6)
        # b3: MAN -> COMPUTER PROGRAMMER
        self.beat(GrowArrow(a1), FadeIn(prog, scale=0.7), run=1.4)
        # b4: the same arrow from WOMAN, endpoint hidden
        q = txt("?", 56, PUMPKIN).move_to(pw + V + RIGHT * 0.35)
        a2b = a2.copy()
        self.beat(GrowArrow(a2), FadeIn(q, scale=0.6), run=1.3)
        # b5: HOMEMAKER revealed in Pumpkin
        self.beat(FadeOut(q), FadeIn(home, scale=1.4), Indicate(a2, color=PUMPKIN, scale_factor=1.04), run=1.4)
        # b6: both parallel arrows; the stereotype is as clean as the capitals
        self.beat(a2.animate.set_color(PUMPKIN), a1.animate.set_color(PUMPKIN), run=1.2)
        # b7: ghost capitals arrow with the same precision
        self.beat(FadeIn(france), FadeIn(paris), GrowArrow(a3), run=1.8)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M13_DEBIAS_PROJECTION(QScene):
    ASSET = "M13_DEBIAS_PROJECTION"

    def construct(self):
        self.setup_q()
        Y0 = -0.2
        ax = Arrow(np.array([-5.4, Y0, 0]), np.array([5.4, Y0, 0]), buff=0, stroke_width=5, color=LIME,
                   tip_length=0.28)
        axl = txt("GENDER DIRECTION", 28, LIME).move_to([-3.4, Y0 - 0.45, 0])
        g = np.array([1.0, 0.0, 0.0])
        words = {"NURSE": np.array([-3.6, 1.5, 0]), "PROGRAMMER": np.array([2.9, 1.9, 0]),
                 "ENGINEER": np.array([3.6, -1.2, 0])}
        base = np.array([0, Y0, 0])
        pts = {n: glow_dot(base + p, OFFWHITE, 0.08) for n, p in words.items()}
        labs = {n: txt(n, 28).next_to(pts[n], UP if p[1] > 0 else DOWN, buff=0.15) for n, p in words.items()}
        tag(self, "ILLUSTRATIVE")
        # b1: one axis
        self.beat(GrowArrow(ax), FadeIn(axl, shift=UP * 0.15), run=1.5)
        # b2: occupation points cast projections onto the axis
        shadows, drops = {}, {}
        for n, p in words.items():
            sx = np.array([p[0], Y0, 0])
            shadows[n] = Dot(sx, radius=0.09, color=LIME)
            drops[n] = DashedLine(base + p, sx, stroke_color=LIME, stroke_width=2.5, dash_length=0.12)
        self.beat(LaggedStart(*[FadeIn(VGroup(pts[n], labs[n]), scale=0.7) for n in words], lag_ratio=0.2),
                  Succession(Wait(0.8), LaggedStart(*[AnimationGroup(Create(drops[n]), FadeIn(shadows[n], scale=2))
                                                      for n in words], lag_ratio=0.3)), run=2.2)
        # b3: neutralize: v - (v.g)g; projections collapse to zero, points slide onto the perpendicular line
        f = txt("v′ = v − (v·g)g", 38, LIME).move_to([-3.2, -1.55, 0])
        zero = txt("0", 34, LIME).move_to([0.0, Y0 - 0.45, 0])
        newpos = {n: base + np.array([0, p[1], 0]) for n, p in words.items()}
        self.beat(FadeIn(f, shift=UP * 0.2),
                  *[AnimationGroup(pts[n].animate.move_to(newpos[n]), labs[n].animate.next_to(newpos[n], RIGHT if n != "NURSE" else LEFT, buff=0.3),
                                   shadows[n].animate.move_to(base), drops[n].animate.put_start_and_end_on(newpos[n], base))
                    for n in words], FadeIn(zero, scale=1.5), run=3.6)
        # b4: a small Pumpkin residue remains: clusters of words still lean one way
        r = np.random.default_rng(29)
        cl = [np.array([-3.4, 1.3, 0]), np.array([3.6, 1.2, 0]), np.array([3.4, -1.4, 0])]
        res = VGroup(*[Dot(c + np.array([r.normal(0, 0.28), r.normal(0, 0.2), 0]), radius=0.055, color=PUMPKIN)
                       for c in cl for _ in range(9)])
        note = txt("2019 FOLLOW-UP: BIAS PERSISTS", 30, PUMPKIN).move_to([-1.0, 2.4, 0])
        src = self.hud(txt("Gonen & Goldberg (2019)", 18, bold=False).set_opacity(0.7), corner=DL,
                       buff=np.array([0.8, 1.78, 0]))
        self.beat(FadeOut(f), FadeOut(axl), LaggedStart(*[FadeIn(d, scale=0.2) for d in res], lag_ratio=0.05),
                  FadeIn(note, shift=LEFT * 0.2), FadeIn(src), run=2.4, focus=RIGHT * 0.3)
        # b5: not solved
        self.beat(Indicate(res, color=PUMPKIN, scale_factor=1.15), run=1.6)
        self.finish()
