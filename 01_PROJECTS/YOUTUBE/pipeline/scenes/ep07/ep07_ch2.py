"""EP07 chapter 2 Manim scenes (S11 M05, S13 M06, S14 M06B, S15 M06D, S18 M06C, S19 M07, S20 M07B,
S21 M08, S22 M09). Render: see PRODUCTION_BRIEF.md."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ep07_intro import *
from ep07_ch1 import chip


def spring(a_mob, b_mob, color=LIME, n=12, amp=0.11, op=None):
    """Zig-zag spring redrawn every frame between the centers of two mobjects."""
    def draw():
        a, b = a_mob.get_center(), b_mob.get_center()
        u = b - a
        L = np.linalg.norm(u) + 1e-6
        nrm = np.array([-u[1], u[0], 0]) / L
        pts = [a + u * t + nrm * (amp * (1 if i % 2 else -1) if 0 < i < n else 0)
               for i, t in enumerate(np.linspace(0, 1, n + 1))]
        m = VMobject(stroke_color=color, stroke_width=3.5).set_points_as_corners(pts)
        return m.set_stroke(opacity=op.get_value() if op else 1)
    return always_redraw(draw)


# ---------------------------------------------------------------------------------------------
class M05_FIRTH_QUOTE(QScene):
    ASSET = "M05_FIRTH_QUOTE"

    def construct(self):
        self.setup_q()
        l1 = VGroup(*[txt(w, 52) for w in "You shall know a word".split()]).arrange(RIGHT, buff=0.26)
        l2 = VGroup(*[txt(w, 52) for w in "by the company it keeps.".split()]).arrange(RIGHT, buff=0.26)
        quote = VGroup(l1, l2).arrange(DOWN, buff=0.4).move_to(UP * 0.45)
        words = [*l1, *l2]
        attr = txt("J.R. FIRTH · 1957", 24, bold=False).set_opacity(0.8).next_to(quote, DOWN, buff=0.5)
        r = np.random.default_rng(5)
        seeds = VGroup(*[Dot([r.uniform(-5.8, 5.8), r.uniform(-2.0, 2.3), 0], radius=0.05, color=LIME)
                         for _ in words])
        seeds.add_updater(lambda m, dt: [d.shift(0.12 * dt * np.array([np.sin(i), np.cos(i * 1.7), 0]))
                                         for i, d in enumerate(m)])
        self.add(seeds)
        # b1: quote assembles word by word from drifting points
        seeds.clear_updaters()
        self.beat(LaggedStart(*[ReplacementTransform(d, w) for d, w in zip(seeds, words)], lag_ratio=0.12),
                  Succession(Wait(2.2), FadeIn(attr, shift=UP * 0.15)), run=3.1)
        # b2: COMPANY IT KEEPS turns lime; the word itself is boxed and dims (meaning is not inside it)
        keep = VGroup(*l2[2:])
        under = Line(keep.get_corner(DL) + DOWN * 0.14, keep.get_corner(DR) + DOWN * 0.14, stroke_color=LIME,
                     stroke_width=5)
        box = DashedVMobject(SurroundingRectangle(l1[4], buff=0.14, corner_radius=0.08), num_dashes=28)
        box.set_stroke(OFFWHITE, 2.5, opacity=0.8)
        self.beat(Succession(AnimationGroup(keep.animate.set_color(LIME), Create(under), run_time=1.6),
                             Wait(0.6),
                             AnimationGroup(Create(box), l1[4].animate.set_opacity(0.35), run_time=1.4)), run=4.0)
        # b3: quote dissolves into one word surrounded by neighbour words
        center = label_dot("COFFEE", ORIGIN + DOWN * 0.1, LIME, size=34)
        nb = ["cup", "morning", "espresso", "milk", "hot", "brew"]
        ang = np.linspace(0, TAU, len(nb), endpoint=False) + 0.4
        npos = [np.array([3.3 * np.cos(a), 1.75 * np.sin(a) - 0.1, 0]) for a in ang]
        ndots = VGroup(*[glow_dot(p, OFFWHITE, 0.06) for p in npos])
        nlabs = VGroup(*[txt(w, 30, bold=False).next_to(p, UP if p[1] > 0 else DOWN, buff=0.15)
                         for w, p in zip(nb, npos)])
        spokes = VGroup(*[Line(center[0].get_center(), p, stroke_color=SLATE, stroke_width=3) for p in npos])
        others = [w for w in words if w not in words[:len(nb)]]
        self.beat(*[ReplacementTransform(w, l) for w, l in zip(words[:len(nb)], nlabs)],
                  *[FadeOut(w) for w in others], FadeOut(attr), FadeOut(under), FadeOut(box),
                  GrowFromCenter(center), LaggedStart(*[Create(s) for s in spokes], lag_ratio=0.1),
                  LaggedStart(*[FadeIn(d, scale=0.5) for d in ndots], lag_ratio=0.1), run=1.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
def sentence_pair():
    a = ["I", "drank", "hot", "coffee", "this", "morning"]
    b = ["I", "drank", "hot", "tea", "this", "morning"]
    ra = VGroup(*[txt(w, 32, bold=False) for w in a]).arrange(RIGHT, buff=0.22)
    rb = VGroup(*[txt(w, 32, bold=False) for w in b])
    for wa, wb in zip(ra, rb):
        wb.move_to(wa).shift(DOWN * 0.62)
    g = VGroup(ra, rb).move_to(UP * 1.95)
    return ra, rb, g


def number_col(vals, side, anchor):
    col = VGroup(*[txt(f"{v:+.2f}", 22, bold=False) for v in vals]).arrange(DOWN, buff=0.12)
    box = SurroundingRectangle(col, buff=0.12, corner_radius=0.06, stroke_color=SLATE, stroke_width=2)
    g = VGroup(box, col)
    return g.next_to(anchor, side, buff=0.3)


class M06_CONTEXT_PULL(QScene):
    ASSET = "M06_CONTEXT_PULL"

    def construct(self):
        self.setup_q()
        ra, rb, sents = sentence_pair()
        ctx = VGroup(*[w for i, w in enumerate([*ra, *rb]) if i % 6 != 3])
        win = SurroundingRectangle(sents, buff=0.2, corner_radius=0.12, stroke_color=SLATE, stroke_width=2.5)
        # b1: two sentences, the shared context highlighted
        self.beat(Succession(LaggedStart(FadeIn(ra, shift=UP * 0.2), FadeIn(rb, shift=UP * 0.2), lag_ratio=0.4,
                                         run_time=1.4),
                             AnimationGroup(ctx.animate.set_color(LIME), Create(win), run_time=1.4)), run=3.2)
        Y = 0.05
        cof = label_dot("COFFEE", [-4.4, Y, 0], OFFWHITE, size=28)
        tea = label_dot("TEA", [4.4, Y, 0], OFFWHITE, size=28)
        # b2: COFFEE and TEA start far apart
        self.beat(GrowFromCenter(cof), GrowFromCenter(tea), ra[3].animate.set_color(OFFWHITE), run=1.3)
        steps = [[0.82, -0.41, 0.07, -0.93, 0.56], [-0.35, 0.66, -0.88, 0.12, -0.29]]
        targ = [[0.61, -0.22, 0.38, -0.47, 0.15], [0.58, -0.19, 0.41, -0.52, 0.11]]
        def cols(t, xc, xt):
            vc = [a + (b - a) * t for a, b in zip(steps[0], targ[0])]
            vt = [a + (b - a) * t for a, b in zip(steps[1], targ[1])]
            return (number_col(vc, DOWN, Dot([xc, Y, 0])).shift(DOWN * 0.1),
                    number_col(vt, DOWN, Dot([xt, Y, 0])).shift(DOWN * 0.1))
        cc, ct = cols(0, -4.4, 4.4)
        cc.shift(RIGHT * (cc.width + 0.5)).shift(DOWN * 0.0)   # first appearance: under/next to the dot
        ct.shift(LEFT * (ct.width + 0.5))
        cc.next_to(cof[0], DOWN, buff=0.35)
        ct.next_to(tea[0], DOWN, buff=0.35)
        tag(self, "ILLUSTRATIVE")
        # b3: a list of numbers under each point, random values
        self.beat(Write(cc[1]), Create(cc[0]), Write(ct[1]), Create(ct[0]), run=1.6)
        op = ValueTracker(0)
        spr = spring(cof[0], tea[0], LIME, n=22, op=op)
        self.add(spr)
        def move(xc, t, rt=None):
            a, b = cols(t, -xc, xc)
            kw = {} if rt is None else {"run_time": rt}
            return AnimationGroup(cof.animate.shift(RIGHT * 0).move_to([-xc, Y, 0]).shift(cof.get_center() - cof[0].get_center()),
                                  tea.animate.move_to([xc, Y, 0]).shift(tea.get_center() - tea[0].get_center()),
                                  Transform(cc, a), Transform(ct, b), **kw)
        # b4: a context match, a lime spring pulls them closer
        self.beat(op.animate.set_value(1), Indicate(ctx, color=LIME, scale_factor=1.06), move(3.0, 0.3), run=1.8)
        # b5: many pulls in sequence, UPDATES ticker climbing
        vt, num = counter(0, 0, size=34, color=LIME)
        tick = VGroup(txt("UPDATES", 22, bold=False), num)
        num.add_updater(lambda m: m.next_to(tick[0], RIGHT, buff=0.2))
        tick[0].move_to([-5.0, 0.85, 0])
        self.add(tick)
        self.beat(vt.animate(rate_func=linear).set_value(48210), FadeIn(tick[0]),
                  Succession(move(2.3, 0.55, 0.9), move(1.75, 0.75, 0.9), move(1.45, 0.88, 0.9)), run=2.9)
        # b6: coffee and tea settle side by side
        self.beat(vt.animate(rate_func=linear).set_value(91574), move(1.2, 1.0),
                  op.animate.set_value(0.6), run=2.0)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M06B_PUSH_APART(QScene):
    ASSET = "M06B_PUSH_APART"

    def construct(self):
        self.setup_q()
        r = np.random.default_rng(8)
        homes = {"drink": [-3.0, 0.9], "fruit": [3.2, 1.3], "geo": [2.6, -1.4], "animal": [-3.2, -1.3],
                 "city": [0.1, 1.8]}
        pts, home = [], []
        for c, h in homes.items():
            for _ in range(8):
                home.append(np.array([*h, 0]) + np.array([*r.normal(0, 0.38, 2), 0]))
        home = np.array(home)
        start = np.c_[r.uniform(-5.6, 5.6, len(home)), r.uniform(-2.0, 2.2, len(home)), np.zeros(len(home))]
        blob = np.c_[r.normal(0, 0.22, len(home)), r.normal(0.1, 0.22, len(home)), np.zeros(len(home))]
        dots = VGroup(*[glow_dot(p, OFFWHITE, 0.055) for p in start]).set_opacity(0.75)
        iC, iT, iB, iV = 0, 1, 8, 16          # coffee, tea (drink); banana (fruit); volcano (geo)
        self.add(dots)
        # b1: pull-only training: everything slides to the center (collapse)
        pulls = VGroup(*[Line(start[i], start[j], stroke_color=LIME, stroke_width=2.5)
                         for i, j in r.integers(0, len(home), (14, 2)) if i != j])
        self.beat(Succession(LaggedStart(*[ShowPassingFlash(l, time_width=0.6) for l in pulls], lag_ratio=0.12,
                                         run_time=1.6),
                             AnimationGroup(*[d.animate.move_to(p) for d, p in zip(dots, blob)], run_time=2.6)),
                  run=4.5)
        # b2: freeze; Pumpkin warning ring
        ring = Circle(radius=0.95, stroke_color=PUMPKIN, stroke_width=5).move_to(UP * 0.1)
        self.beat(Create(ring), ring.animate(rate_func=flicker(3)).set_stroke(opacity=1), run=1.6)
        # b3: random words sampled: BANANA, VOLCANO; COFFEE marked
        lab = lambda s, i, c, d: txt(s, 26, c).next_to(dots[i], d, buff=0.1)
        cofL = lab("COFFEE", iC, LIME, LEFT)
        out = {iB: np.array([1.7, 1.1, 0]), iV: np.array([1.5, -1.0, 0])}
        rings = VGroup(*[Circle(radius=0.2, stroke_color=PUMPKIN, stroke_width=3).move_to(p) for p in out.values()])
        bL = txt("BANANA", 26, PUMPKIN).next_to(out[iB], UR, buff=0.1)
        vL = txt("VOLCANO", 26, PUMPKIN).next_to(out[iV], DR, buff=0.1)
        self.beat(dots[iC].animate.set_color(LIME), FadeIn(cofL), dots[iB].animate.move_to(out[iB]).set_color(PUMPKIN),
                  dots[iV].animate.move_to(out[iV]).set_color(PUMPKIN), Create(rings), FadeIn(bL), FadeIn(vL),
                  ring.animate.set_stroke(opacity=0.4), run=1.8)
        # b4: Pumpkin springs push them away from COFFEE
        op = ValueTracker(1)
        sB, sV = spring(dots[iC], dots[iB], PUMPKIN, op=op), spring(dots[iC], dots[iV], PUMPKIN, op=op)
        far = {iB: np.array([3.9, 1.7, 0]), iV: np.array([3.6, -1.9, 0])}
        for m in (cofL, bL, vL, rings[0], rings[1]):
            pass
        bL.add_updater(lambda m: m.next_to(dots[iB], UR, buff=0.1))
        vL.add_updater(lambda m: m.next_to(dots[iV], DR, buff=0.1))
        rings[0].add_updater(lambda m: m.move_to(dots[iB]))
        rings[1].add_updater(lambda m: m.move_to(dots[iV]))
        self.add(sB, sV)
        self.beat(dots[iB].animate.move_to(far[iB]), dots[iV].animate.move_to(far[iV]), run=1.5)
        # b5: pull the real neighbours in, push the random ones out: clean clusters
        homes_final = home.copy()
        homes_final[iB], homes_final[iV] = far[iB], far[iV]
        homes_final[iT] = homes_final[iC] + np.array([0.45, 0.12, 0])
        cofL.add_updater(lambda m: m.next_to(dots[iC], LEFT, buff=0.1))
        teaL = txt("TEA", 26, LIME)
        teaL.add_updater(lambda m: m.next_to(dots[iT], RIGHT, buff=0.1))
        sCT = spring(dots[iC], dots[iT], LIME, n=8, amp=0.07)
        self.add(sCT)
        self.beat(*[d.animate.move_to(p) for d, p in zip(dots, homes_final)], dots[iT].animate.set_color(LIME),
                  FadeIn(teaL), FadeOut(ring), op.animate.set_value(0.35), run=2.6)
        # b6: millions of times: rapid pull/push flashes everywhere
        flashes = []
        for k in range(18):
            i, j = r.integers(0, len(home), 2)
            same = (i // 8) == (j // 8)
            flashes.append(ShowPassingFlash(Line(homes_final[i], homes_final[j],
                                                 stroke_color=LIME if same else PUMPKIN, stroke_width=3),
                                            time_width=0.5))
        self.beat(LaggedStart(*flashes, lag_ratio=0.08), run=1.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M06D_CONTEXT_WINDOW(QScene):
    ASSET = "M06D_CONTEXT_WINDOW"

    def construct(self):
        self.setup_q()
        ws = "every morning she orders a large cup of hot coffee with milk before the train to work".split()
        words = VGroup(*[txt(w, 32, bold=False) for w in ws]).arrange(RIGHT, buff=0.3)
        C = 9                                              # coffee
        words.shift(UP * 0.7 - RIGHT * words[C].get_x())
        x0 = np.array([w.get_x() for w in words])
        base = words.copy()                                # sentence at rest, for window geometry
        sh = ValueTracker(7.0)                             # scroll offset (updater-driven: no animation fights)
        words.add_updater(lambda m: [w.set_x(x0[i] + sh.get_value()) for i, w in enumerate(m)])
        def window(c):
            g = VGroup(*base[c - 5:c + 6]).copy().shift(LEFT * (x0[c] - x0[C]))
            return SurroundingRectangle(g, buff=0.2, corner_radius=0.12, stroke_color=LIME, stroke_width=4)
        # b1: a long sentence scrolls in
        self.beat(sh.animate.set_value(0.0), run=1.9)
        # b2: lime window frames a handful of words either side of COFFEE (no count shown, see VERIFY #5)
        win = window(C)
        arcs = VGroup(*[ArcBetweenPoints(words[C].get_top() + UP * 0.08, words[j].get_top() + UP * 0.08,
                                         angle=-0.9 if j > C else 0.9, stroke_color=LIME, stroke_width=2.5)
                        for j in range(C - 5, C + 6) if j != C]).set_fill(opacity=0).set_stroke(opacity=0.7)
        self.beat(Succession(AnimationGroup(words[C].animate.set_color(LIME), Create(win), run_time=1.4),
                             LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.08, run_time=2.0)), run=3.7)
        # b3: the window slides one word at a time
        def step(c, prev):
            return AnimationGroup(sh.animate.set_value(-(x0[c] - x0[C])), Transform(win, window(c)),
                                  words[c].animate.set_color(LIME), words[prev].animate.set_color(OFFWHITE))
        self.beat(FadeOut(arcs), Succession(step(C + 1, C), step(C + 2, C + 1)), run=2.4)
        # b4: one more step; words outside the window fade to grey
        outside = VGroup(*[w for i, w in enumerate(words) if abs(i - (C + 3)) > 5])
        self.beat(step(C + 3, C + 2), outside.animate.set_opacity(0.25), run=1.0)
        # b5: every (centre, neighbour) pair becomes free training data
        c = C + 3
        pairs = [ws[j] for j in (c - 1, c + 1, c - 3, c + 2, c - 5, c + 4)]
        chips = VGroup(*[chip(f"{ws[c]} → {p}", LIME, 24) for p in pairs]).arrange_in_grid(2, 3, buff=(0.4, 0.3))
        chips.move_to(DOWN * 1.35)
        self.beat(LaggedStart(*[FadeIn(ch, shift=DOWN * 0.4) for ch in chips], lag_ratio=0.18), run=2.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M06C_SIDE_EFFECT(QScene):
    ASSET = "M06C_SIDE_EFFECT"

    def construct(self):
        self.setup_q()
        r = np.random.default_rng(12)
        names = ["CAT", "COFFEE", "KING", "PARIS", "RIVER", "TEA"]
        def cells(vals):
            return VGroup(*[Square(0.4, stroke_color=SLATE, stroke_width=2, fill_color=LIME,
                                   fill_opacity=0.12 + 0.75 * abs(v)) for v in vals]).arrange(RIGHT, buff=0.06)
        V = r.uniform(-1, 1, (6, 6))
        rows = VGroup(*[VGroup(txt(n, 24).set_width(min(1.4, txt(n, 24).width)), cells(v)).arrange(RIGHT, buff=0.3)
                        for n, v in zip(names, V)])
        for row in rows:
            row[0].align_to(rows[0][0], LEFT) if False else None
        rows.arrange(DOWN, buff=0.14, aligned_edge=RIGHT).move_to([-3.3, 0.2, 0])
        # b1: the word table
        self.beat(LaggedStart(*[FadeIn(row, shift=RIGHT * 0.3) for row in rows], lag_ratio=0.15), run=1.2)
        # b2: a guessing machine predicts neighbour words around COFFEE
        box = RoundedRectangle(corner_radius=0.15, width=4.0, height=2.6, stroke_color=SLATE, stroke_width=3,
                               fill_color=BACKGROUND, fill_opacity=0.95).move_to([3.3, 0.35, 0])
        title = txt("GUESSING MACHINE", 22, bold=False).next_to(box.get_top(), DOWN, buff=0.22)
        feed = Arrow(rows[1][1].get_right(), box.get_left() + DOWN * 0.1, buff=0.15, stroke_width=4, color=LIME)
        guesses = ["cup", "hot", "tax"]
        probs = [0.62, 0.48, 0.06]
        glabs = VGroup(*[txt(g, 24, bold=False) for g in guesses]).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        glabs.move_to(box.get_center() + LEFT * 1.25 + DOWN * 0.25)
        tracks = VGroup(*[Rectangle(width=2.2, height=0.2, stroke_color=SLATE, stroke_width=2).next_to(g, RIGHT, buff=0.3)
                          .align_to(glabs, LEFT).shift(RIGHT * 0.9) for g in glabs])
        bars = VGroup(*[Rectangle(width=2.2 * p, height=0.2, stroke_width=0, fill_color=LIME if p > 0.2 else OFFWHITE,
                                  fill_opacity=0.9).align_to(t, LEFT).align_to(t, UP) for p, t in zip(probs, tracks)])
        machine = VGroup(box, title, glabs, tracks)
        self.beat(Succession(AnimationGroup(FadeIn(machine, shift=LEFT * 0.3), GrowArrow(feed),
                                            rows[1][0].animate.set_color(LIME), run_time=1.6),
                             LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.3, run_time=1.3)),
                  run=3.0, focus=RIGHT * 0.6)
        tag(self, "ILLUSTRATIVE")
        # b3: training bar fills while the table numbers keep changing
        prog_t = Rectangle(width=4.0, height=0.16, stroke_color=SLATE, stroke_width=2).next_to(box, DOWN, buff=0.3)
        prog = Rectangle(width=4.0, height=0.16, stroke_width=0, fill_color=LIME, fill_opacity=0.9).move_to(prog_t)
        ptxt = txt("TRAINING", 18, bold=False).next_to(prog_t, DOWN, buff=0.12)
        V2 = r.uniform(-1, 1, (6, 6))
        self.beat(FadeIn(prog_t), FadeIn(ptxt), GrowFromEdge(prog, LEFT),
                  *[Transform(row[1], cells(v).move_to(row[1])) for row, v in zip(rows, V2)], run=2.2)
        # b4: the guessing part is thrown away: lifts out of frame and dissolves
        gone = VGroup(machine, bars, prog_t, prog, ptxt)
        self.beat(gone.animate.shift(UP * 4.2).set_opacity(0), FadeOut(feed), run=2.4)
        # b5: what they kept: the table glows lime, KEPT
        self.beat(rows.animate.move_to(UP * 0.1).scale(1.12), run=1.6)
        frame = SurroundingRectangle(rows, buff=0.25, corner_radius=0.12, stroke_color=LIME, stroke_width=4)
        kept = txt("KEPT", 40, LIME).next_to(frame, RIGHT, buff=0.35).rotate(-0.12)
        # (b5 continues) -> b6: the numbers for each word: lime sweep row by row
        self.beat(Create(frame), FadeIn(kept, scale=1.5), rows[1][0].animate.set_color(OFFWHITE),
                  LaggedStart(*[Indicate(row[1], color=LIME, scale_factor=1.04) for row in rows], lag_ratio=0.15),
                  run=1.9)
        # b7: like walking a city to run errands: table becomes a street map, a walker runs errands
        streets = VGroup(*[Line([x, -2.1, 0], [x + r.uniform(-0.3, 0.3), 2.3, 0]) for x in np.linspace(-5, 5, 9)],
                         *[Line([-5.6, y, 0], [5.6, y + r.uniform(-0.2, 0.2), 0]) for y in np.linspace(-1.8, 2.0, 6)])
        streets.set_stroke(SLATE, 4, opacity=1)
        stops = [np.array(p) for p in ([-3.75, -1.05, 0], [-1.25, 1.2, 0], [1.25, -0.3, 0], [3.75, 1.2, 0])]
        pins = VGroup(*[glow_dot(p, PUMPKIN, 0.08) for p in stops])
        path = VMobject().set_points_as_corners([[-5, -1.8, 0], [-3.75, -1.8, 0], [-3.75, 1.2, 0], [1.25, 1.2, 0],
                                                 [1.25, -0.3, 0], [3.75, -0.3, 0], [3.75, 1.2, 0]])
        walker = glow_dot(path.get_start(), LIME, 0.09)
        trail = TracedPath(walker[2].get_center, stroke_color=LIME, stroke_width=4, stroke_opacity=0.6)
        self.add(trail)
        self.beat(FadeOut(rows), FadeOut(frame), FadeOut(kept), Create(streets),
                  Succession(AnimationGroup(FadeIn(pins), FadeIn(walker), run_time=0.7),
                             MoveAlongPath(walker, path, run_time=2.1)), run=2.8)
        # b8: the errands end
        self.beat(FadeOut(pins, scale=0.4), FadeOut(walker), run=1.1)
        # b9: the map in your head stays: the streets turn into the word map
        pj = Proj(self, spin=0.05, k=0.85)
        cloud = pj.cloud(CLOUD, reveal=0)
        self.add(cloud)
        self.beat(streets.animate.set_stroke(LIME, opacity=0.25), FadeOut(trail),
                  cloud.reveal.animate.set_value(1), run=2.0)
        self.finish()


# ---------------------------------------------------------------------------------------------
def strip300(vals, y=0.0, w=10.2, h=0.55):
    cw = w / len(vals)
    return VGroup(*[Rectangle(width=cw * 0.82, height=h, stroke_width=0, fill_color=LIME,
                              fill_opacity=0.1 + 0.8 * min(1, abs(v) / 2.2)).move_to([-w / 2 + cw * (i + 0.5), y, 0])
                    for i, v in enumerate(vals)])


MAP_CORE = np.vstack([CLOUD, CLUSTER_PTS])
MAP_CORE_LIME = np.r_[np.full(len(CLOUD), 0.8), np.full(len(CLUSTER_PTS), 9.0)]
CLUSTER_WORDS = {"COUNTRIES": ["FRANCE", "JAPAN", "BRAZIL"], "FOODS": ["BREAD", "RICE", "APPLE"],
                 "MOTION": ["RUN", "WALK", "SWIM"]}


def word_pts(name, words):
    """3D points for named words inside a cluster (spread so labels do not collide)."""
    offs = [np.array([-0.35, 0.3, 0.1]), np.array([0.3, -0.05, -0.2]), np.array([-0.2, -0.4, 0.2])]
    return [CLUSTERS[name] + o for o in offs[:len(words)]]


class M07_300D_TO_3D(QScene):
    ASSET = "M07_300D_TO_3D"

    def construct(self):
        self.setup_q()
        vals = np.random.default_rng(17).normal(0, 1, 300)
        strip = strip300(vals)
        lab = txt("300 NUMBERS", 24, bold=False).next_to(strip, UP, buff=0.3).align_to(strip, LEFT)
        dot = glow_dot(ORIGIN, LIME, 0.09)
        # b1: a 300-cell strip folds into a single point
        self.beat(Succession(AnimationGroup(LaggedStart(*[FadeIn(c) for c in strip], lag_ratio=0.004),
                                            FadeIn(lab), run_time=1.3),
                             AnimationGroup(strip.animate.scale(0.0).move_to(ORIGIN), FadeOut(lab),
                                            FadeIn(dot, scale=0.2), run_time=1.2)), run=2.6)
        self.remove(strip)
        # b2: the 3D projection appears around it
        pj = Proj(self, spin=0.07, k=1.0)
        cloud = pj.cloud(MAP_CORE, reveal=0, lime_z=MAP_CORE_LIME)
        self.add(cloud)
        tag(self, "300D → 3D PROJECTION · ILLUSTRATIVE")
        self.beat(cloud.reveal.animate.set_value(1), FadeOut(dot, scale=3), run=2.6)
        halos, labels = {}, {}
        for n, ws in CLUSTER_WORDS.items():
            halos[n] = pj.cloud(cluster_pts(n), r=0.1, color=LIME, opacity=0.32, dim=0)
            self.add(halos[n])
            labels[n] = VGroup(*[pj.pin(VGroup(glow_dot(ORIGIN, LIME, 0.06), txt(w, 24).next_to(ORIGIN, UR, buff=0.08)), p)
                                 for w, p in zip(ws, word_pts(n, ws))])
        prev = None
        # b3-b5: countries, foods, verbs of motion light one by one
        for n in CLUSTER_WORDS:
            anims = [halos[n].dim.animate.set_value(1), LaggedStart(*[FadeIn(l, scale=0.6) for l in labels[n]],
                                                                    lag_ratio=0.25)]
            if prev:
                anims += [halos[prev].dim.animate.set_value(0.45), labels[prev].animate.set_opacity(0.45)]
            self.beat(*anims, run=min(1.2, 0.8 * self.beat_len()))
            prev = n
        self.finish()


class M07B_NO_NAMED_AXIS(QScene):
    ASSET = "M07B_NO_NAMED_AXIS"

    def construct(self):
        self.setup_q()
        r = np.random.default_rng(23)
        vals = r.normal(0, 1, 300)
        Y = -0.2
        strip = strip300(vals, Y)
        c17 = strip[16]
        hi = SurroundingRectangle(c17, buff=0.05, stroke_color=LIME, stroke_width=3)
        q = VGroup(txt("#17", 30, LIME), txt("= ANIMAL?", 30)).arrange(RIGHT, buff=0.18)
        q.next_to(c17, UP, buff=0.9).align_to(c17, LEFT).shift(LEFT * 0.2)
        stem = Line(hi.get_top(), q.get_bottom() + DOWN * 0.08, stroke_color=LIME, stroke_width=2.5)
        # b1: the 300-cell strip; cell 17 highlighted with = ANIMAL?
        self.beat(Succession(LaggedStart(*[FadeIn(c) for c in strip], lag_ratio=0.003, run_time=1.2),
                             AnimationGroup(Create(hi), Create(stem), FadeIn(q, shift=UP * 0.2), run_time=1.2)),
                  run=2.6, focus=c17.get_center() * 0.4)
        # b2: No. Pumpkin cross over the label
        cross = VGroup(Line(q.get_corner(UL), q.get_corner(DR)), Line(q.get_corner(DL), q.get_corner(UR)))
        cross.set_stroke(PUMPKIN, 6)
        self.beat(Create(cross), q.animate.set_opacity(0.4), run=0.5)
        # b3: cells light for CAT: bars of similar size everywhere, no single cell dominates
        cat = txt("CAT", 34).next_to(strip, LEFT, buff=0.3)
        def bars(v):
            cw = 10.2 / 300
            return VGroup(*[Rectangle(width=cw * 0.8, height=max(0.02, abs(x) * 0.55), stroke_width=0, fill_color=LIME,
                                      fill_opacity=0.35 + 0.4 * min(1, abs(x) / 2))
                            .move_to([-5.1 + cw * (i + 0.5), Y + np.sign(x) * abs(x) * 0.275, 0])
                            for i, x in enumerate(v)])
        v1, v2 = r.normal(0, 1, 300), r.normal(0, 1, 300)
        self.beat(FadeOut(VGroup(hi, stem, q, cross)), FadeIn(cat, shift=RIGHT * 0.2),
                  Succession(Transform(strip, bars(v1), run_time=1.4), Transform(strip, bars(v2), run_time=1.4)),
                  run=2.9, focus=ORIGIN)
        # b4: meaning is spread across all 300 at once: a lime sweep lights every bar
        sweep = Line([-5.2, Y - 1.3, 0], [-5.2, Y + 1.3, 0], stroke_color=LIME, stroke_width=4)
        self.beat(Succession(FadeIn(sweep, run_time=0.2), sweep.animate(run_time=2.4).move_to([5.2, Y, 0]),
                             FadeOut(sweep, run_time=0.3)),
                  LaggedStart(*[b.animate.set_fill(LIME, opacity=0.95) for b in strip], lag_ratio=0.01), run=3.0)
        # b5: it shows up as directions through the space, not as axes
        O = np.array([-0.6, -0.5, 0])
        dirs = [np.array([np.cos(a), np.sin(a) * 0.62, 0]) for a in np.linspace(0, PI, 7)[:-1] + 0.2]
        axes = VGroup(*[Line(O - 2.4 * d, O + 2.4 * d, stroke_color=SLATE, stroke_width=3) for d in dirs])
        arrow = Arrow(O, O + np.array([3.3, 1.9, 0]), buff=0, stroke_width=7, color=LIME, tip_length=0.3)
        mlab = txt("MEANING LIVES HERE", 30, LIME).next_to(arrow.get_end(), RIGHT, buff=0.2).shift(DOWN * 0.15)
        self.beat(Succession(AnimationGroup(FadeOut(strip), FadeOut(cat),
                                            LaggedStart(*[Create(a) for a in axes], lag_ratio=0.1), run_time=1.4),
                             GrowArrow(arrow, run_time=1.2), Write(mlab, run_time=1.0)), run=3.8,
                  focus=O * 0.3 + RIGHT * 0.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
class M08_COSINE_ANGLE(QScene):
    ASSET = "M08_COSINE_ANGLE"

    def construct(self):
        self.setup_q()
        O = np.array([-3.6, -2.0, 0])
        a_c, a_t, a_x = 10 * DEGREES, (10 + np.degrees(np.arccos(0.8))) * DEGREES, (10 + np.degrees(np.arccos(0.1))) * DEGREES
        P = lambda a, L: O + L * np.array([np.cos(a), np.sin(a), 0])
        pc, pt, px = P(a_c, 4.8), P(a_t, 4.3), P(a_x, 3.9)
        cof, tea, tax = label_dot("COFFEE", pc, LIME, size=28), label_dot("TEA", pt, LIME, size=28), \
            label_dot("TAX", px, OFFWHITE, size=28)
        ruler = DashedLine(pc, pt, stroke_color=OFFWHITE, stroke_width=3, dash_length=0.1)
        ticks = VGroup(*[Line(ORIGIN, UP * 0.12, stroke_color=OFFWHITE, stroke_width=2)
                         .rotate(np.arctan2(*(pt - pc)[[1, 0]]) + PI / 2).move_to(pc + (pt - pc) * t)
                         for t in np.linspace(0.1, 0.9, 9)])
        origin = glow_dot(O, OFFWHITE, 0.07)
        # b1: three words; a ruler is drawn, then set aside; the origin appears
        self.beat(Succession(LaggedStart(*[FadeIn(m, scale=0.6) for m in (cof, tea, tax)], lag_ratio=0.25,
                                         run_time=1.4),
                             AnimationGroup(Create(ruler), FadeIn(ticks), run_time=1.0),
                             AnimationGroup(VGroup(ruler, ticks).animate.set_opacity(0.15), FadeIn(origin, scale=0.4),
                                            run_time=1.2)), run=4.3)
        arr = lambda p, c, o=1: Arrow(O, p, buff=0.1, stroke_width=5, color=c, tip_length=0.24).set_opacity(o)
        ac, at, ax = arr(pc, LIME), arr(pt, LIME), arr(px, OFFWHITE, 0.4)
        # b2: an arrow from the center to each word
        self.beat(FadeOut(ruler), FadeOut(ticks), LaggedStart(GrowArrow(ac), GrowArrow(at), GrowArrow(ax), lag_ratio=0.3),
                  run=2.0)
        tag(self, "ILLUSTRATIVE")
        arc1 = Arc(radius=1.6, start_angle=a_c, angle=a_t - a_c, arc_center=O, stroke_color=LIME, stroke_width=6)
        c1 = txt("cos ≈ 0.8", 30, LIME).move_to(O + 2.45 * np.array([np.cos(a_c + 0.32), np.sin(a_c + 0.32), 0]))
        # b3: small angle means similar
        self.beat(Create(arc1), Write(c1), run=1.3)
        arc2 = Arc(radius=0.95, start_angle=a_c, angle=a_x - a_c, arc_center=O, stroke_color=OFFWHITE, stroke_width=5)
        c2 = txt("cos ≈ 0.1", 30).move_to(O + np.array([-1.5, 1.35, 0]))
        # b4: wide angle means unrelated
        self.beat(ax.animate.set_opacity(1), Create(arc2), Write(c2), VGroup(arc1, c1).animate.set_opacity(0.55),
                  run=1.5)
        f = txt("cos θ = a·b / (‖a‖‖b‖)", 40).move_to([3.2, 1.0, 0])
        name = txt("COSINE SIMILARITY", 30, LIME).next_to(f, DOWN, buff=0.4)
        # b5: the formula writes on; COSINE SIMILARITY
        self.beat(Succession(Write(f, run_time=1.3), FadeIn(name, shift=UP * 0.2, run_time=0.8)), run=2.2,
                  focus=RIGHT * 1.0)
        self.finish()


class M09_DIRECTION_TEASE(QScene):
    ASSET = "M09_DIRECTION_TEASE"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.07, k=1.0, th=0.6)
        cloud = pj.cloud(MAP_CORE, lime_z=MAP_CORE_LIME)
        halos = [pj.cloud(cluster_pts(n), r=0.1, color=LIME, opacity=0.32, dim=0.6) for n in CLUSTER_WORDS]
        self.add(cloud, *halos)
        # b1: clusters dim
        self.beat(cloud.dim.animate.set_value(0.4), *[h.dim.animate.set_value(0.15) for h in halos], run=2.2)
        # b2: the positions mattered: rings mark where each cluster sits
        names = ["COUNTRIES", "FOODS", "MOTION", "MONEY", "RIVER", "TRAVEL"]
        rings = VGroup(*[pj.pin(Circle(radius=0.5, stroke_color=OFFWHITE, stroke_width=2.5, stroke_opacity=0.7, fill_opacity=0),
                                CLUSTERS[n], idx=None) for n in names])
        self.beat(LaggedStart(*[Create(c) for c in rings], lag_ratio=0.15), run=1.3)
        # b3: faint arrows between them appear, one brightens (the MAN -> WOMAN direction); push in
        faint = [pj.link(CLUSTERS[a], CLUSTERS[b], OFFWHITE, 3, o=0.35) for a, b in
                 [("COUNTRIES", "TRAVEL"), ("RIVER", "MOTION"), ("FOODS", "MONEY"), ("MOTION", "FOODS")]]
        hero = pj.link(MAN, WOMAN, LIME, 6)
        ends = VGroup(*[pj.pin(glow_dot(ORIGIN, LIME, 0.06), p) for p in (MAN, WOMAN)]).set_opacity(0)
        self.beat(Succession(LaggedStart(*[a.g.animate.set_value(1) for a in faint], lag_ratio=0.2, run_time=1.1),
                             AnimationGroup(hero.g.animate.set_value(1), ends.animate.set_opacity(1),
                                            rings.animate.set_stroke(opacity=0.25), run_time=1.0)),
                  run=2.2, focus=pj.P(MAN) * 0.5)
        self.finish()
