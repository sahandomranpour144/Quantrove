"""EP08 chapters 4-5: Scenes 30 (M15), 33 (M15B), 34 (M16)."""
from ep08_common import *


class M15_DECODER_ONLY(QScene):
    ASSET = "M15_DECODER_ONLY"

    def construct(self):
        self.setup_q()
        enc = tower(3, w=2.8, h=0.62, gap=0.1).move_to(LEFT * 2.6 + UP * 0.3)
        dec = tower(3, w=2.8, h=0.62, gap=0.1).move_to(RIGHT * 2.6 + UP * 0.3)
        el = chip("ENCODER", 22).next_to(enc, DOWN, buff=0.3)
        dl = chip("DECODER", 22, LIME, LIME).next_to(dec, DOWN, buff=0.3)
        link = Arrow(enc.get_right() + RIGHT * 0.1, dec.get_left() + LEFT * 0.1, buff=0, stroke_width=4, color=OFFWHITE)
        dd, ee = VGroup(dec, dl), VGroup(enc, el, link)
        # b1: the original two-part design
        self.beat(FadeIn(enc, shift=RIGHT * 0.3), FadeIn(dd, shift=LEFT * 0.3), FadeIn(el), GrowArrow(link), run=1.8)
        # b2: encoder half fades, decoder stays
        self.beat(FadeOut(ee, shift=LEFT * 0.8), dd.animate.move_to(LEFT * 4.6 + DOWN * 0.1), run=2.0)
        # b3: attention grid, each word may look back
        words = ["the", "bank", "raised", "rates", "on", "loans"]
        g = pair_grid(6, 0.64, 0.05).move_to(RIGHT * 1.7 + DOWN * 0.1)
        cols = VGroup(*[txt(w, 14, bold=False).next_to(g[c], UP, buff=0.12) for c, w in enumerate(words)])
        rows = VGroup(*[txt(w, 14, bold=False).next_to(g[6 * r], LEFT, buff=0.14) for r, w in enumerate(words)])
        low = [g[6 * r + c] for r in range(6) for c in range(6) if c <= r]
        up = [g[6 * r + c] for r in range(6) for c in range(6) if c > r]
        self.beat(FadeIn(g), FadeIn(cols), FadeIn(rows),
                  LaggedStart(*[c.animate.set_fill(LIME, 0.75).set_stroke(LIME, 1.4) for c in low], lag_ratio=0.04), run=1.4)
        # b4: but never ahead: the upper triangle is masked
        mk = txt("MASKED", 22, PUMPKIN).next_to(g, RIGHT, buff=0.35).shift(UP * 0.9)
        self.beat(LaggedStart(*[c.animate.set_fill(PUMPKIN, 0.85).set_stroke(PUMPKIN, 1.4) for c in up], lag_ratio=0.04),
                  FadeIn(mk, shift=LEFT * 0.2), run=1.4)
        # b5: next-token prediction
        full = Sentence(["the", "bank", "raised", "rates"], 34, gap=0.2, center=UP * 0.3)
        full.box(3).set_stroke(LIME, 3).set_fill(LIME, 0.14)
        full.word(3).set_color(LIME)
        slot = DashedVMobject(full.box(3).copy().set_stroke(PUMPKIN, 3).set_fill(opacity=0), num_dashes=24)
        first = VGroup(*full[:3])
        self.beat(FadeOut(VGroup(dd, g, cols, rows, mk)),
                  Succession(FadeIn(first, lag_ratio=0.25, run_time=1.0), FadeIn(slot, run_time=0.5),
                             ReplacementTransform(slot, full[3], run_time=0.9)), run=2.8)
        # b6: that one rule, repeated, is the chatbot
        chat = Sentence(["the", "bank", "raised", "rates", "on", "new", "home", "loans"], 26, gap=0.14, center=UP * 0.3)
        bub = RoundedRectangle(corner_radius=0.35, width=chat.width + 0.9, height=1.5).set_stroke(SLATE, 3.5)
        bub.set_fill(BACKGROUND, 0.9).move_to(chat)
        tail = Polygon(bub.get_corner(DL) + RIGHT * 0.6 + UP * 0.02, bub.get_corner(DL) + RIGHT * 1.2 + UP * 0.02,
                       bub.get_corner(DL) + RIGHT * 0.5 + DOWN * 0.4).set_stroke(SLATE, 3.5).set_fill(BACKGROUND, 0.9)
        self.beat(*[ReplacementTransform(full[k], chat[k]) for k in range(4)], FadeIn(VGroup(bub, tail)),
                  LaggedStart(*[AnimationGroup(FadeIn(chat[k], shift=RIGHT * 0.2), chat.mark(k)) for k in range(4, 8)],
                              lag_ratio=0.45), run=2.5)
        self.finish()


class M15B_BEYOND_TEXT(QScene):
    ASSET = "M15B_BEYOND_TEXT"

    def construct(self):
        self.setup_q()
        ops = [[.1, .1, .55, .9], [.1, .5, .9, .55], [.35, .8, .45, .2], [.9, .5, .15, .1]]
        S = 0.85
        patches = VGroup(*[Square(S).set_stroke(LIME, 1, 0.5).set_fill(LIME, ops[r][c]) for r in range(4) for c in range(4)])
        patches.arrange_in_grid(4, 4, buff=0).move_to(UP * 0.2)
        # b1: an image
        self.beat(FadeIn(patches, scale=0.9), run=1.4)
        # b2: cut into 16x16-pixel patches and line them up like words
        ptag = txt("16×16 PX", 22).next_to(patches, RIGHT, buff=0.5).shift(UP * 1.2)
        c0 = patches.get_center()
        spread = [p.animate.shift((p.get_center() - c0) * 0.18) for p in patches]
        row_pos = [np.array([-5.6 + 0.75 * k, -0.3, 0]) for k in range(16)]
        line_up = [p.animate.scale(0.65).move_to(pos) for p, pos in zip(patches, row_pos)]
        self.beat(Succession(AnimationGroup(*spread, FadeIn(ptag), run_time=1.2),
                             AnimationGroup(*line_up, FadeOut(ptag), run_time=1.6)), run=3.2)
        # b3: attention lines web between them; Vision Transformer card
        row = VGroup(*[Square(0.55).move_to(pos) for pos in row_pos])
        arcs = all_arcs(row, LIME, 1.2, 0.4)
        card = chip("2020 · VISION TRANSFORMER", 26, OFFWHITE, LIME).move_to(DOWN * 1.9)
        self.beat(LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.012), FadeIn(card, shift=UP * 0.2), run=2.6)
        # b4: it worked
        self.beat(arcs.animate.set_stroke(LIME, 2.2, 0.85), card[0].animate.set_stroke(LIME, 4), run=0.8)
        # b5: protein chain
        s = np.linspace(0, 7.4, 22)
        pts = [np.array([4.9 * np.sin(0.85 * v + 0.2), 0.3 + 1.5 * np.sin(1.55 * v + 0.9), 0]) for v in s]
        back = VMobject().set_points_smoothly(pts).set_stroke(OFFWHITE, 3, 0.4)
        beads = VGroup(*[Dot(p, radius=0.1, color=OFFWHITE) for p in pts])
        card2 = chip("2021 · ALPHAFOLD 2 · ATTENTION-BASED", 26, OFFWHITE, LIME).move_to(DOWN * 1.95)
        row_all = VGroup(patches, arcs)
        self.beat(FadeOut(VGroup(row_all, card), shift=UP * 0.3), Create(back), FadeIn(beads, lag_ratio=0.06),
                  FadeIn(card2, shift=UP * 0.2), run=2.6)
        # b6: attention between distant residues
        pairs = sorted([(i, j) for i in range(22) for j in range(i + 6, 22)],
                       key=lambda ij: np.linalg.norm(pts[ij[0]] - pts[ij[1]]))[:8]
        lr = VGroup(*[Line(pts[i], pts[j]).set_stroke(LIME, 3.2, 0.9) for i, j in pairs])
        hot = VGroup(*[beads[k] for k in sorted({k for p in pairs for k in p})])
        self.beat(Succession(LaggedStart(*[Create(l) for l in lr], lag_ratio=0.25, run_time=2.0),
                             hot.animate(run_time=1.2).set_color(LIME)), run=3.6)
        # b7: same idea: every piece looks at every other piece
        allw = VGroup(*[Line(pts[i], pts[j]) for i in range(22) for j in range(i + 1, 22)]).set_stroke(LIME, 1.1, 0.3)
        prot = VGroup(back, beads, lr, allw)
        pr2 = VGroup(*[Square(0.55).set_stroke(LIME, 1, 0.5).set_fill(LIME, ops[r][c]) for r in range(4) for c in range(4)])
        pr2.arrange(RIGHT, buff=0.2).move_to(ORIGIN)
        pa2 = all_arcs(pr2, LIME, 1.2, 0.6)
        right = VGroup(pr2, pa2).scale(0.42).move_to(RIGHT * 3.5 + UP * 0.2)
        self.beat(Succession(LaggedStart(*[Create(l) for l in allw], lag_ratio=0.004, run_time=1.6),
                             AnimationGroup(prot.animate.scale(0.55).move_to(LEFT * 3.4 + UP * 0.2),
                                            FadeIn(right), FadeOut(card2), run_time=1.4)), run=3.4)
        self.finish()


def cgrid(n, side=3.4, gap=0.03):
    cell = (side - gap * (n - 1)) / n
    return VGroup(*[Square(cell).set_stroke(SLATE, 1.4).set_fill(BACKGROUND, 0.9) for _ in range(n * n)]).arrange_in_grid(n, n, buff=gap)


def header(n, side=3.4, gap=0.03):
    cell = (side - gap * (n - 1)) / n
    return VGroup(*[RoundedRectangle(corner_radius=min(0.05, cell / 4), width=cell, height=0.2).set_stroke(SLATE, 1.4)
                    .set_fill(OFFWHITE, 0.3) for _ in range(n)]).arrange(RIGHT, buff=gap)


class M16_N_SQUARED(QScene):
    ASSET = "M16_N_SQUARED"

    def construct(self):
        self.setup_q()
        GC = LEFT * 3.0 + DOWN * 0.45
        wv, shown, col = ValueTracker(4), ValueTracker(0), ValueTracker(0)
        px = 3.6
        n_ = lambda: int(round(wv.get_value()))
        wlab = live_txt(lambda: (f"WORDS  {n_()}", OFFWHITE), 30, [px, 1.9, 0])
        big = live_txt(lambda: (f"{shown.get_value():,.0f}", interpolate_color(ManimColor(LIME), ManimColor(PUMPKIN), col.get_value()).to_hex()),
                       110, [px, 0.8, 0])
        sub = txt("COMPARISONS", 24, bold=False).move_to([px, -0.1, 0])
        eq = live_txt(lambda: (f"{n_()} × {n_()} = {n_() ** 2}", OFFWHITE), 30, [px, -0.75, 0])

        def grid_pair(n, color, o):
            g, h = cgrid(n), header(n)
            for c in g:
                c.set_fill(color, o).set_stroke(color, 1.4)
            g.move_to(GC)
            h.next_to(g, UP, buff=0.12)
            return g, h
        g4, h4 = grid_pair(4, LIME, 0.7)
        g10, h10 = grid_pair(10, LIME, 0.7)
        g20, h20 = grid_pair(20, LIME, 0.7)
        base = cgrid(4).move_to(GC)
        self.add(wlab, big, eq, sub)
        # b1: 4 words -> 16 comparisons
        self.beat(FadeIn(h4, lag_ratio=0.15), FadeIn(base),
                  LaggedStart(*[ReplacementTransform(b, c) for b, c in zip(base, g4)], lag_ratio=0.05),
                  shown.animate.set_value(16), run=2.6)
        # b2: 10 words -> 100
        self.beat(ReplacementTransform(g4, g10), ReplacementTransform(h4, h10), wv.animate.set_value(10),
                  shown.animate.set_value(100), run=1.8)
        # b3: double the text -> four times the work
        for c in g20:
            c.set_fill(PUMPKIN, 0.8).set_stroke(PUMPKIN, 1.2)
        x4 = txt("×4", 80, PUMPKIN).move_to([px, -1.75, 0])
        self.beat(Succession(AnimationGroup(ReplacementTransform(g10, g20), ReplacementTransform(h10, h20),
                                            wv.animate.set_value(20), shown.animate.set_value(400),
                                            col.animate.set_value(1), run_time=1.6),
                             FadeIn(x4, scale=1.6, run_time=0.8)), run=2.8)
        self.finish()
