"""EP08 chapter 3: EIGHT HEADS, TWELVE HOURS (Scenes 21, 23, 24)."""
from ep08_common import *


def link_tag(a, b, size=18, color=OFFWHITE):
    ta, tb = txt(a, size, color), txt(b, size, color)
    arr = DoubleArrow(LEFT * 0.22, RIGHT * 0.22, buff=0, stroke_width=2.5, tip_length=0.1, color=color)
    return VGroup(ta, arr, tb).arrange(RIGHT, buff=0.12)


def heat(m, cell, gap, color=LIME):
    n = m.shape[0]
    g = VGroup(*[Square(cell).set_stroke(SLATE, 1).set_fill(color, 0) for _ in range(n * n)]).arrange_in_grid(n, n, buff=gap)
    return g


def heat_ops(m):
    m = m / m.max(axis=1, keepdims=True)
    return [0.06 + 0.88 * float(v) for v in m.flatten()]


def head_patterns():
    r = np.random.default_rng(12)
    P = []
    base = np.eye(12) * 0.4 + r.uniform(0, 0.08, (12, 12))
    base[IT] = np.array(W_IT)
    P.append(base)
    h1 = np.eye(12) * 0.15 + r.uniform(0, 0.05, (12, 12))         # subject <-> verb
    for a, b in [(1, 3), (1, 2), (8, 9), (6, 3)]:
        h1[a, b] = h1[b, a] = 1
    h2 = np.eye(12) * 0.15 + r.uniform(0, 0.05, (12, 12))         # pronoun -> noun
    h2[IT, TROPHY], h2[IT, SUITCASE], h2[TROPHY, TROPHY], h2[SUITCASE, SUITCASE] = 1, 0.35, 0.6, 0.6
    h3 = r.uniform(0, 0.05, (12, 12))                              # neighbours
    for i in range(12):
        for j in (i - 1, i + 1):
            if 0 <= j < 12:
                h3[i, j] = 1
    P += [h1, h2, h3]
    for _ in range(4):                                             # other heads: sparse, ILLUSTRATIVE
        h = r.uniform(0, 0.05, (12, 12))
        for i in range(12):
            h[i, r.integers(0, 12)] = 1
        P.append(h)
    return P


class M12_MULTI_HEAD(QScene):
    ASSET = "M12_MULTI_HEAD"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(UP * 1.05)
        P = head_patterns()
        big = heat(P[0], 0.19, 0.025).move_to(DOWN * 0.9)
        att = weighted_arcs(s, IT, W_IT)
        # b1: one attention pattern over the sentence
        self.beat(FadeIn(s, lag_ratio=0.05), s.mark(IT), LaggedStart(*[Create(a) for a in att], lag_ratio=0.06),
                  LaggedStart(*[c.animate.set_fill(LIME, o) for c, o in zip(big, heat_ops(P[0]))], lag_ratio=0.004),
                  FadeIn(big), FadeIn(illustrative(self)), run=1.8)
        # b2: it splits into 8 side-by-side heads
        panels = VGroup(*[heat(P[0], 0.088, 0.012) for _ in range(8)]).arrange(RIGHT, buff=0.24).move_to(DOWN * 0.75)
        for p in panels:
            for c, o in zip(p, heat_ops(P[0])):
                c.set_fill(LIME, o)
        heads = VGroup(*[txt(f"HEAD {k + 1}", 15, bold=False).next_to(p, DOWN, buff=0.14) for k, p in enumerate(panels)])
        self.beat(ReplacementTransform(big, panels[0]), *[TransformFromCopy(big, p) for p in panels[1:]],
                  LaggedStart(*[FadeIn(h) for h in heads], lag_ratio=0.1), run=2.2)
        # b3: each head learns its own kind of relationship
        self.beat(LaggedStart(*[AnimationGroup(*[c.animate.set_fill(LIME, o) for c, o in zip(p, heat_ops(P[k]))])
                                for k, p in enumerate(panels)], lag_ratio=0.12), att.animate.set_stroke(opacity=0.15),
                  run=2.6)
        # b4-b6: head 1 subject<->verb, head 2 pronoun<->noun, head 3 neighbours
        pairs = [[(1, 3), (1, 2), (8, 9)], [(IT, TROPHY), (IT, SUITCASE)], [(i, i + 1) for i in range(11)]]
        tags = [link_tag("SUBJECT", "VERB"), link_tag("PRONOUN", "NOUN"), txt("NEIGHBOURS", 18)]
        box_prev, arcs_prev, tag_prev = None, att, None
        for k in range(3):
            frame = SurroundingRectangle(panels[k], buff=0.07, corner_radius=0.05).set_stroke(LIME, 3)
            arcs = VGroup(*[arc(s[a].get_top(), s[b].get_top(), LIME, 4 if k < 2 else 3, 0.95) for a, b in pairs[k]])
            tg = tags[k].next_to(heads[k], DOWN, buff=0.1)
            anims = [Create(frame), FadeOut(arcs_prev), Create(arcs), FadeIn(tg, shift=UP * 0.1),
                     panels[k].animate.scale(1.12)]
            if box_prev:
                anims += [FadeOut(box_prev), panels[k - 1].animate.scale(1 / 1.12), FadeOut(tag_prev)]
            self.beat(*anims, run=0.8 if k == 0 else 1.0, focus=[panels[k].get_x() * 0.35, 0, 0])
            box_prev, arcs_prev, tag_prev = frame, arcs, tg
        self.finish()


def mini_net():
    a = [UP * 0.16 * (k - 1) + LEFT * 0.14 for k in range(3)]
    b = [UP * 0.16 * (k - 1) + RIGHT * 0.14 for k in range(3)]
    lines = VGroup(*[Line(p, q) for p in a for q in b]).set_stroke(OFFWHITE, 1.2, 0.5)
    dots = VGroup(*[Dot(p, radius=0.035, color=OFFWHITE) for p in a + b])
    box = RoundedRectangle(corner_radius=0.07, width=0.56, height=0.56).set_stroke(OFFWHITE, 2).set_fill(BACKGROUND, 0.95)
    return VGroup(box, lines, dots)


class M13_STACK_LAYERS(QScene):
    ASSET = "M13_STACK_LAYERS"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(DOWN * 1.55)
        web = all_arcs(s, LIME, 1.3, 0.38)
        nets = VGroup(*[mini_net().move_to([c.get_x(), 0.55, 0]) for c in s])
        # b1: attention lines gather into each word, then each word gets its own small network
        gather = AnimationGroup(web.animate.set_stroke(opacity=0.05),
                                *[s.box(i).animate(rate_func=there_and_back).set_fill(LIME, 0.5) for i in range(12)],
                                run_time=1.0)
        self.beat(Succession(AnimationGroup(FadeIn(s, lag_ratio=0.05), AnimationGroup(*[Create(a) for a in web]),
                                            run_time=1.4), gather,
                             LaggedStart(*[FadeIn(n, shift=UP * 0.15) for n in nets], lag_ratio=0.08, run_time=1.3)),
                  run=3.7)
        # b2: each word carries what it gathered up into its own network
        dots = VGroup(*[glow_dot(c.get_top(), LIME, 0.05) for c in s])
        self.beat(LaggedStart(*[d.animate.move_to(n.get_center()) for d, n in zip(dots, nets)], lag_ratio=0.06),
                  LaggedStart(*[n[1].animate.set_stroke(LIME, 1.4, 0.9) for n in nets], lag_ratio=0.06),
                  FadeIn(dots), run=1.9, focus=UP * 0.2)
        # b3: attention, then processing
        lab = VGroup(txt("ATTENTION", 24, LIME), Arrow(LEFT * 0.35, RIGHT * 0.35, buff=0, stroke_width=3, color=OFFWHITE,
                                                       max_tip_length_to_length_ratio=0.3),
                     txt("PROCESSING", 24)).arrange(RIGHT, buff=0.2).move_to(UP * 1.75)
        self.beat(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.15) for m in lab], lag_ratio=0.3),
                  web.animate.set_stroke(opacity=0.3), run=1.4)
        # b4: that pair is one block
        pair = VGroup(s, web, nets, dots)
        outline = SurroundingRectangle(pair, buff=0.18, corner_radius=0.15).set_stroke(LIME, 3)
        btag = chip("1 BLOCK", 22, LIME, LIME).next_to(outline, UP, buff=0.12).align_to(outline, LEFT)
        self.beat(Create(outline), FadeOut(lab, shift=UP * 0.2), FadeIn(btag, shift=DOWN * 0.1), run=1.2)
        # b5: stack the block six times
        tw = tower(6, w=3.6, h=0.56, gap=0.12).move_to(UP * 0.35)
        vt, cnt = counter(1, 6, fmt="× {:.0f}", size=64, color=LIME)
        cnt.add_updater(lambda m: m.next_to(tw, RIGHT, buff=0.6))
        self.add(cnt)
        self.beat(ReplacementTransform(VGroup(pair, outline), tw[0]), FadeOut(btag),
                  LaggedStart(Wait(), *[FadeIn(b, shift=DOWN * 0.5) for b in tw[1:]], lag_ratio=0.25),
                  vt.animate.set_value(6), run=2.2, focus=UP * 0.3)
        # b6: a token's vector rises through the stack and sharpens
        vec = mem_column(4, 0.2, OFFWHITE, 0.2).move_to(tw[0].get_center())
        self.add(vec)
        self.beat(vec.animate.move_to(tw[5].get_center()).set_fill(LIME, 0.95).set_stroke(LIME, 2),
                  LaggedStart(*[b[0].animate(rate_func=there_and_back).set_stroke(LIME, 4) for b in tw], lag_ratio=0.3),
                  run=2.6)
        self.finish()


A_WORDS = ["the", "dog", "bit", "the", "man"]
B_WORDS = ["the", "man", "bit", "the", "dog"]
SLOT = 0.86


def even_row(words, cx, y):
    r = Sentence(words)
    for k, c in enumerate(r):
        c.move_to([cx + (k - 2) * SLOT, y, 0])
    return r


def pe_wave(cx, y, fn, amp=0.22):
    return FunctionGraph(lambda x: y + amp * fn((x - cx) / SLOT + 2), x_range=[cx - 2.45 * SLOT, cx + 2.45 * SLOT, 0.02])


class M14_POSITION_WAVES(QScene):
    ASSET = "M14_POSITION_WAVES"

    def construct(self):
        self.setup_q()
        ra, rb = even_row(A_WORDS, -3.3, 1.0), even_row(B_WORDS, 3.3, 1.0)
        # b1: two sentences, same words
        self.beat(FadeIn(ra, shift=RIGHT * 0.2, lag_ratio=0.1), FadeIn(rb, shift=LEFT * 0.2, lag_ratio=0.1), run=0.8)
        wa, wb = all_arcs(ra, LIME, 1.6, 0.5), all_arcs(rb, LIME, 1.6, 0.5)
        # b2: every word looks at every word, in both
        self.beat(AnimationGroup(*[Create(a) for a in [*wa, *wb]]), run=1.4)
        # b3: attention alone sees the same set
        eq = txt("=", 72, PUMPKIN).move_to(UP * 1.0)

        def bag(row, cx):
            order = sorted(range(5), key=lambda k: row[k][1].get_left()[0] * 0 + ["bit", "dog", "man", "the", "the"].index(
                ["the", "dog", "bit", "the", "man", "man", "dog"][0]) if False else 0)
            return order
        sort_key = {"bit": 0, "dog": 1, "man": 2, "the": 3}

        def bag_moves(row, words, cx):
            order = sorted(range(5), key=lambda k: (sort_key[words[k]], k))
            return [row[k].animate.move_to([cx + (slot - 2) * SLOT, 1.0, 0]) for slot, k in enumerate(order)]
        self.beat(FadeOut(wa), FadeOut(wb), FadeIn(eq, scale=0.6), *bag_moves(ra, A_WORDS, -3.3),
                  *bag_moves(rb, B_WORDS, 3.3), run=1.6)
        # b4: "the dog bit the man" looks the same as "the man bit the dog"
        back = [c.animate.move_to([-3.3 + (k - 2) * SLOT, 1.0, 0]) for k, c in enumerate(ra)] + \
               [c.animate.move_to([3.3 + (k - 2) * SLOT, 1.0, 0]) for k, c in enumerate(rb)]
        wa2, wb2 = all_arcs(even_row(A_WORDS, -3.3, 1.0), LIME, 1.6, 0.5), all_arcs(even_row(B_WORDS, 3.3, 1.0), LIME, 1.6, 0.5)
        self.beat(Succession(AnimationGroup(*back, run_time=1.2),
                             AnimationGroup(*[Create(a) for a in [*wa2, *wb2]], eq.animate.scale(1.25), run_time=1.0),
                             eq.animate(run_time=1.0).scale(1 / 1.25)), run=3.4)
        # b5: stamp each position with a signature built from sine waves (real PE formula, d = 16)
        d = 16
        fns = [lambda p: np.sin(p / 10000 ** (0 / d)), lambda p: np.cos(p / 10000 ** (0 / d)),
               lambda p: np.sin(p / 10000 ** (2 / d))]
        ys = [-0.15, -0.75, -1.35]
        waves = VGroup(*[pe_wave(cx, y, fn).set_stroke(c, 2.5, 0.85) for cx in (-3.3, 3.3)
                         for y, fn, c in zip(ys, fns, [LIME, OFFWHITE, LIME])])
        pos = VGroup(*[txt(f"POS {k}", 14, bold=False).next_to(r[k], UP, buff=0.1)
                       for r in (ra, rb) for k in range(5)])
        f1 = VGroup(txt("PE(pos, 2i) = sin(pos / 10000", 17, bold=False), txt("2i/d", 11, bold=False), txt(")", 17, bold=False))
        f2 = VGroup(txt("PE(pos, 2i+1) = cos(pos / 10000", 17, bold=False), txt("2i/d", 11, bold=False), txt(")", 17, bold=False))
        for f in (f1, f2):
            f[1].next_to(f[0], RIGHT, buff=0.04).align_to(f[0], UP).shift(UP * 0.06)
            f[2].next_to(f[1], RIGHT, buff=0.04).align_to(f[0], DOWN)
        f1.move_to([-3.3, -1.9, 0])
        f2.move_to([3.3, -1.9, 0])
        self.beat(FadeOut(wa2), FadeOut(wb2), LaggedStart(*[Create(w) for w in waves], lag_ratio=0.1),
                  FadeIn(pos, lag_ratio=0.05), FadeIn(f1), FadeIn(f2), FadeIn(illustrative(self)), run=1.8,
                  focus=DOWN * 0.3)
        # b6: each word gets a unique signature; now the two sentences differ
        sig = VGroup()
        for cx, row in ((-3.3, ra), (3.3, rb)):
            for k in range(5):
                x = cx + (k - 2) * SLOT
                sig.add(VGroup(*[Dot([x, y + 0.22 * fn(k), 0], radius=0.065, color=LIME if j != 1 else OFFWHITE)
                                 for j, (y, fn) in enumerate(zip(ys, fns))]))
        ne = txt("≠", 72, LIME).move_to(eq)
        dogs = [ra[1], rb[4]]
        dsig = [sig[1], sig[9]]
        rings = VGroup(*[SurroundingRectangle(VGroup(c, s_), buff=0.1, corner_radius=0.08).set_stroke(LIME, 2.5)
                         for c, s_ in zip(dogs, dsig)])
        self.beat(LaggedStart(*[FadeIn(g, scale=0.5) for g in sig], lag_ratio=0.05), ReplacementTransform(eq, ne),
                  LaggedStart(Wait(), Create(rings), lag_ratio=0.5), run=2.1)
        self.finish()
