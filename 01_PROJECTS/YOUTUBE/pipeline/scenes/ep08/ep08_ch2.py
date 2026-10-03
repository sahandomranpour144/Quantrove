"""EP08 chapter 2: ATTENTION IS ALL YOU NEED (Scenes 14-20)."""
from ep08_common import *

# Dot-product scores consistent with W_IT: softmax(SCORES) == W_IT exactly (scores = ln(w / 0.01)), ILLUSTRATIVE
SCORES = [float(np.log(w / 0.01)) for w in W_IT]
QUERY_ANG = 45 * DEGREES
QK_NORM = 4.6     # |q||k|, so cos(angle) = score / QK_NORM


def bars(sent, values, k, base_y, color=LIME, width=0.34, min_h=0.03):
    g = VGroup()
    for i, v in enumerate(values):
        h = max(v * k, min_h)
        g.add(Rectangle(width=width, height=h).set_stroke(color, 1.5).set_fill(color, 0.75)
              .move_to([sent[i].get_center()[0], base_y + h / 2, 0]))
    return g


class M06_ALL_AT_ONCE(QScene):
    ASSET = "M06_ALL_AT_ONCE"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(DOWN * 0.3)
        hp = hops(s)
        # b1: sentence words in a row, still joined by the old chain
        self.beat(FadeIn(s, lag_ratio=0.06), Create(hp, lag_ratio=0.1), run=1.6)
        # b2: the old way: one step after another, left to right
        path = VMobject().set_points(np.concatenate([h.points for h in hp]))
        pulse = glow_dot(path.get_start(), OFFWHITE, 0.08)
        self.add(pulse)
        self.beat(MoveAlongPath(pulse, path), LaggedStart(*[s.box(i).animate(rate_func=there_and_back)
                                                            .set_stroke(OFFWHITE, 3) for i in range(12)], lag_ratio=0.4),
                  run=2.0)
        # b3: every word looks at every other word, all at once
        web = all_arcs(s, LIME, 1.5, 0.42)
        self.beat(AnimationGroup(*[Create(a) for a in web]), FadeOut(pulse), run=1.4, focus=UP * 0.3)
        # b4: no chain, no fading memory
        self.beat(FadeOut(hp, shift=DOWN * 0.3), run=1.2)
        # b5: any word reaches any other in one step
        key = arc(s[TROPHY].get_top(), s[IT].get_top(), LIME, 6, 1)
        label = chip("ONE STEP, ANY DISTANCE", 26, LIME, LIME).move_to(DOWN * 1.5)
        self.beat(web.animate.set_stroke(opacity=0.12), Create(key), s.mark(TROPHY), s.mark(IT),
                  FadeIn(label, shift=UP * 0.15), run=1.6, focus=UP * 0.2)
        # b6: self-attention: each word also attends to itself
        loops = VGroup(*[Circle(radius=0.12).set_stroke(LIME, 2.2, 0.85).next_to(c, UP, buff=0) for c in s])
        self.beat(web.animate.set_stroke(opacity=0.42), key.animate.set_stroke(width=3, opacity=0.8), FadeOut(label),
                  LaggedStart(*[Create(l) for l in loops], lag_ratio=0.08), run=1.6)
        # b7: the sentence attending to itself: a wave of attention runs through the web
        self.beat(LaggedStart(*[a.animate(rate_func=there_and_back).set_stroke(width=3.2, opacity=1) for a in web],
                              lag_ratio=0.015),
                  LaggedStart(*[l.animate(rate_func=there_and_back).scale(1.35) for l in loops], lag_ratio=0.1), run=2.2)
        self.finish()


class M06B_144_LINKS(QScene):
    ASSET = "M06B_144_LINKS"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(UP * 1.95)
        nums = VGroup(*[txt(str(i + 1), 18, bold=False).next_to(s[i], DOWN, buff=0.14) for i in range(12)])
        # b1: the 12-word trophy sentence, counted
        self.beat(FadeIn(s, lag_ratio=0.06), LaggedStart(*[FadeIn(n, shift=UP * 0.1) for n in nums], lag_ratio=0.15),
                  run=2.2)
        g = pair_grid(12, 0.27, 0.035).move_to([-1.4, -0.4, 0])
        cols = [g[j].get_top() for j in range(12)]
        funnel = VGroup(*[Line(s[j].get_bottom() + DOWN * 0.05, cols[j] + UP * 0.05) for j in range(12)])
        funnel.set_stroke(LIME, 1.2, 0.35)
        vt, cnt = counter(0, 144, size=84)
        cnt.add_updater(lambda m: m.move_to([3.7, -0.05, 0]))
        cap = txt("COMPARISONS", 22, bold=False).move_to([3.7, -0.85, 0])
        # b2: every word against every word: a 12x12 grid, 144 comparisons
        self.add(cnt)
        self.beat(FadeOut(nums), Create(funnel, lag_ratio=0.05),
                  LaggedStart(*[FadeIn(c, scale=0.5) for c in g], lag_ratio=0.008), vt.animate.set_value(144),
                  FadeIn(cap), run=3.4)
        # b3: the old reader: one comparison per step
        k = ValueTracker(0)
        hi = always_redraw(lambda: Square(0.33).set_stroke(PUMPKIN, 3).move_to(g[min(int(k.get_value()), 143)]))

        def done(m):
            for i, c in enumerate(m):
                if i < int(k.get_value()):
                    c.set_fill(OFFWHITE, 0.3)
        g.add_updater(done)
        self.add(hi)
        self.beat(k.animate(rate_func=linear).set_value(26), run=2.7, focus=[-1.4, 0.4, 0])   # ticker: linear ok
        g.clear_updaters()
        self.remove(hi)
        # b4: all 144 at the same moment
        tag = chip("AT THE SAME TIME", 26, LIME, LIME).move_to([3.7, -1.75, 0])
        flash = AnimationGroup(g.animate.set_fill(LIME, 0.8).set_stroke(LIME, 1.6), FadeIn(tag, scale=0.9),
                               funnel.animate.set_stroke(opacity=0.8), run_time=0.5)
        order = sorted(range(144), key=lambda i: i // 12 + i % 12)
        shimmer = LaggedStart(*[g[i].animate(rate_func=there_and_back).set_fill(LIME, 0.35) for i in order],
                              lag_ratio=0.01, run_time=3.0)
        self.beat(Succession(flash, shimmer), run=3.9)
        self.finish()


class M07_QKV(QScene):
    ASSET = "M07_QKV"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(UP * 1.6)
        others = VGroup(*[s[i] for i in range(12) if i != IT])
        # b1: the word IT
        self.beat(FadeIn(s, lag_ratio=0.05), s.mark(IT), others.animate.set_opacity(0.45), run=1.4,
                  focus=s[IT].get_center() * 0.4)
        xs, vy = [-3.6, 0, 3.6], -0.55
        vq, vk, vv = mem_column(4, 0.26, LIME, 0.85), mem_column(4, 0.26, OFFWHITE, 0.75), mem_column(4, 0.26, LIME, 0)
        vv.set_stroke(OFFWHITE, 2.4)
        vecs = VGroup(vq, vk, vv)
        for v, x in zip(vecs, xs):
            v.move_to([x, vy, 0])
        start = s[IT].get_bottom() + DOWN * 0.05
        arrs = VGroup(*[Arrow(start, v.get_top() + UP * 0.08, buff=0, stroke_width=4, color=c,
                              max_tip_length_to_length_ratio=0.08) for v, c in zip(vecs, [LIME, OFFWHITE, OFFWHITE])])
        arrs[2].set_opacity(0.7)
        # b2: IT produces three lists of numbers
        self.beat(LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.25),
                  LaggedStart(*[FadeIn(v, shift=DOWN * 0.2, lag_ratio=0.2) for v in vecs], lag_ratio=0.25), run=2.0)
        names = [("QUERY", LIME, "WHAT AM I LOOKING FOR?"), ("KEY", OFFWHITE, "WHAT DO I CONTAIN?"),
                 ("VALUE", OFFWHITE, "WHAT I PASS ALONG")]
        labels = []
        for (n, c, q), x in zip(names, xs):
            labels.append(VGroup(txt(n, 28, c), txt(q, 19, OFFWHITE, bold=False)).arrange(DOWN, buff=0.14)
                          .next_to(vecs[0], DOWN, buff=0.3).set_x(x))
        # b3-b5: query, key, value, each with its question
        for i in range(3):
            anims = [FadeIn(labels[i], shift=UP * 0.15), vecs[i].animate(rate_func=there_and_back).scale(1.15)]
            if i == 2:
                ticks = VGroup()
                for c in s:
                    t = VGroup(Rectangle(width=0.08, height=0.2).set_fill(LIME, 0.9).set_stroke(width=0),
                               Rectangle(width=0.08, height=0.2).set_fill(OFFWHITE, 0.8).set_stroke(width=0),
                               Rectangle(width=0.08, height=0.2).set_stroke(OFFWHITE, 1.5).set_fill(opacity=0))
                    ticks.add(t.arrange(RIGHT, buff=0.05).next_to(c, UP, buff=0.1))
                anims += [others.animate.set_opacity(1), LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in ticks],
                                                                     lag_ratio=0.1)]
            self.beat(*anims, run=1.2 if i < 2 else 2.6, focus=[xs[i] * 0.3, 0, 0] if i < 2 else None)
        self.finish()


class M08_DOT_SCORES(QScene):
    ASSET = "M08_DOT_SCORES"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(UP * 1.9)
        L, by = 0.55, 0.15
        bases = [np.array([c.get_center()[0], by, 0]) for c in s]
        deltas = [np.arccos(np.clip(sc / QK_NORM, -1, 1)) for sc in SCORES]
        sign = [1 if i % 2 else -1 for i in range(12)]
        kangs = [QUERY_ANG + sg * d for sg, d in zip(sign, deltas)]
        keys = VGroup(*[Arrow(b, b + L * np.array([np.cos(a), np.sin(a), 0]), buff=0, stroke_width=4, color=OFFWHITE,
                              max_tip_length_to_length_ratio=0.3) for b, a in zip(bases, kangs)])
        qd = L * np.array([np.cos(QUERY_ANG), np.sin(QUERY_ANG), 0])
        q0 = Arrow(s[IT].get_bottom() + DOWN * 0.1, s[IT].get_bottom() + DOWN * 0.1 + qd, buff=0, stroke_width=5,
                   color=LIME, max_tip_length_to_length_ratio=0.3)
        qs = VGroup(*[Arrow(b, b + qd, buff=0, stroke_width=4, color=LIME, max_tip_length_to_length_ratio=0.3) for b in bases])
        # b1: IT's query against every word's key
        self.beat(FadeIn(s, lag_ratio=0.05), s.mark(IT), LaggedStart(*[GrowArrow(k) for k in keys], lag_ratio=0.06),
                  GrowArrow(q0), run=2.2)
        angs = VGroup(*[Arc(radius=0.24, start_angle=min(QUERY_ANG, a), angle=abs(a - QUERY_ANG), arc_center=b)
                        .set_stroke(LIME if d < 1.0 else OFFWHITE, 2.5, 0.9) for b, a, d in zip(bases, kangs, deltas)])
        glows = VGroup(*[glow_dot(b, LIME, 0.06) for b, d in zip(bases, deltas) if d < 1.0])
        tag = chip("DOT PRODUCT", 20).move_to([-4.9, -1.85, 0])
        # b2: the query is laid on every key; angle arcs; aligned pairs glow
        self.beat(LaggedStart(*[TransformFromCopy(q0, q) for q in qs], lag_ratio=0.06), FadeOut(q0),
                  LaggedStart(Wait(), LaggedStart(*[Create(a) for a in angs], lag_ratio=0.05),
                              AnimationGroup(FadeIn(glows, scale=0.5), FadeIn(tag)), lag_ratio=0.5), run=3.6)
        # b3: score readouts: aligned arrows score high
        t = ValueTracker(0)
        scores = VGroup(*[live_txt(lambda i=i: (f"{abs(SCORES[i] * t.get_value()):.1f}", LIME if SCORES[i] > 1 else OFFWHITE),
                                   22, [bases[i][0], -0.85, 0]) for i in range(12)])
        self.add(scores)
        self.beat(t.animate.set_value(1), FadeIn(illustrative(self)), run=1.8)
        # b4: right angles score near zero; TROPHY scores highest
        low = [i for i in range(12) if SCORES[i] < 1]
        marks = VGroup(*[Square(0.1).set_stroke(OFFWHITE, 1.6).rotate(QUERY_ANG).move_to(
            bases[i] + 0.1 * np.array([np.cos(QUERY_ANG + sign[i] * PI / 4), np.sin(QUERY_ANG + sign[i] * PI / 4), 0]) * 1.41)
            for i in low])
        ring = Circle(radius=0.36).set_stroke(LIME, 3).move_to([bases[TROPHY][0], -0.85, 0])
        self.beat(VGroup(*[keys[i] for i in low], *[qs[i] for i in low], *[angs[i] for i in low]).animate.set_opacity(0.3),
                  Create(marks), s.mark(TROPHY), Create(ring), run=1.4, focus=[bases[TROPHY][0] * 0.4, 0, 0])
        self.finish()


class M09_SOFTMAX(QScene):
    ASSET = "M09_SOFTMAX"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(DOWN * 1.85)
        base = s.get_top()[1] + 0.35
        raw = bars(s, SCORES, 0.5, base, OFFWHITE)
        wts = bars(s, W_IT, 3.0, base, LIME)
        sm = chip("softmax", 26, LIME, LIME).move_to([-4.2, 1.9, 0])
        vt, total = counter(0, 1, fmt="SUM = {:.2f}", size=26, color=LIME)
        total.add_updater(lambda m: m.next_to(sm, RIGHT, buff=0.4))
        self.add(s)
        # b1: raw scores as bars, squashed by softmax into weights that sum to 1.00
        grow = LaggedStart(*[GrowFromEdge(b, DOWN) for b in raw], lag_ratio=0.05, run_time=1.2)
        squash = AnimationGroup(FadeIn(sm, scale=0.8), ReplacementTransform(raw, wts), vt.animate.set_value(1.0),
                                run_time=1.4)
        self.add(total)
        self.beat(Succession(grow, squash), FadeIn(illustrative(self)), run=2.8)
        # b2: for the word IT
        others = VGroup(*[s[i] for i in range(12) if i != IT])
        self.beat(s.mark(IT), others.animate.set_opacity(0.55), run=1.2, focus=s[IT].get_center() * 0.3)
        # b3: most of the weight lands on TROPHY
        labs = VGroup(*[txt(f"{w:.2f}", 20 if w > 0.1 else 16, LIME if w > 0.1 else OFFWHITE, bold=w > 0.1)
                        .next_to(wts[i], UP, buff=0.1) for i, w in enumerate(W_IT)])
        self.beat(LaggedStart(*[FadeIn(l, shift=UP * 0.1) for l in labs], lag_ratio=0.05),
                  s[TROPHY].animate.set_opacity(1), s.mark(TROPHY), wts[TROPHY].animate.set_fill(LIME, 1), run=1.4)
        # b4: IT's new meaning = weighted blend of the values
        H, x = 2.4, s[IT].get_center()[0]
        stack, y = VGroup(), base
        for i in [TROPHY, SUITCASE] + [j for j in range(12) if j not in (TROPHY, SUITCASE)]:
            h = H * W_IT[i]
            c, op = (LIME, 0.95) if i == TROPHY else ((LIME, 0.5) if i == SUITCASE else (OFFWHITE, 0.35))
            stack.add(Rectangle(width=0.62, height=h).set_stroke(BACKGROUND, 1).set_fill(c, op).move_to([x, y + h / 2, 0]))
            y += h
        order = [TROPHY, SUITCASE] + [j for j in range(12) if j not in (TROPHY, SUITCASE)]
        newit = chip("new  it", 22, LIME, LIME).next_to(stack, UP, buff=0.2)
        self.beat(*[ReplacementTransform(wts[i], stack[k]) for k, i in enumerate(order)], FadeOut(labs),
                  LaggedStart(Wait(), FadeIn(newit, shift=DOWN * 0.1), lag_ratio=0.7), run=2.4)
        self.finish()


class M10_FORMULA(QScene):
    ASSET = "M10_FORMULA"

    def construct(self):
        self.setup_q()
        f = Formula(42).move_to(UP * 1.2)
        # b1: the formula assembles
        self.beat(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in f.parts()], lag_ratio=0.12), run=2.2)
        rest = VGroup(*[p for p in f.parts() if p is not f.qk])
        r = np.random.default_rng(10)
        mat = pair_grid(6, 0.3, 0.04).move_to(DOWN * 1.15)
        vals = r.uniform(0.15, 1, 36)
        # b2: multiply queries by keys -> a grid of scores
        self.beat(rest.animate.set_opacity(0.35), f.qk.animate.set_color(LIME),
                  LaggedStart(*[c.animate.set_fill(LIME, float(v)).set_stroke(LIME, 1) for c, v in zip(mat, vals)],
                              lag_ratio=0.03), FadeIn(mat), run=1.4, focus=f.qk.get_center() * 0.3)
        # b3: scale them down
        self.beat(f.qk.animate.set_color(OFFWHITE), f.qk.animate.set_opacity(0.35), f.sqrt.animate.set_opacity(1).set_color(LIME),
                  *[c.animate.set_fill(LIME, float(v) * 0.45) for c, v in zip(mat, vals)], run=1.4,
                  focus=f.sqrt.get_center() * 0.3)
        # b4: without that step the scores blow up
        strike = Line(f.sqrt.get_corner(DL) + LEFT * 0.1, f.sqrt.get_corner(UR) + RIGHT * 0.1).set_stroke(PUMPKIN, 5)
        self.beat(Create(strike), f.sqrt.animate.set_color(OFFWHITE).set_opacity(0.35),
                  *[c.animate.set_fill(PUMPKIN, 0.9).set_stroke(PUMPKIN, 1) for c in mat],
                  FadeIn(illustrative(self)), run=1.2)
        # b5: almost all the weight lands on one word (0.99)
        spike = [0.99] + [0.01 / 7] * 7
        spread = [0.30, 0.22, 0.16, 0.12, 0.09, 0.06, 0.03, 0.02]
        assert abs(sum(spread) - 1) < 1e-9
        bx = [-3.6 + 0.62 * i for i in range(8)]
        base = -2.05

        def wbars(ws, color):
            return VGroup(*[Rectangle(width=0.4, height=max(1.9 * w, 0.03)).set_stroke(color, 1.5).set_fill(color, 0.8)
                            .move_to([x, base + max(1.9 * w, 0.03) / 2, 0]) for x, w in zip(bx, ws)])
        b_sp = wbars(spike, PUMPKIN)
        vt, v99 = counter(0.12, 0.99, fmt="{:.2f}", size=26, color=PUMPKIN)
        v99.add_updater(lambda m: m.next_to(b_sp[0], UP, buff=0.1))
        grad = Arrow([3.4, -2.0, 0], [3.4, -0.35, 0], buff=0, stroke_width=6, color=LIME)
        glab = txt("GRADIENT", 18, bold=False).next_to(grad, RIGHT, buff=0.2)
        self.add(v99)
        self.beat(FadeOut(mat, scale=0.8), LaggedStart(*[GrowFromEdge(b, DOWN) for b in b_sp], lag_ratio=0.05),
                  vt.animate.set_value(0.99), GrowArrow(grad), FadeIn(glab), run=1.5)
        # b6: and learning stalls: the gradient flattens
        flat = Arrow([3.4, -2.0, 0], [3.4, -1.82, 0], buff=0, stroke_width=6, color=PUMPKIN,
                     max_tip_length_to_length_ratio=0.5)
        self.beat(Transform(grad, flat), glab.animate.next_to(flat, RIGHT, buff=0.2), run=0.8)
        # b7: with the scaling, softmax turns scores into spread-out weights
        b_ok = wbars(spread, LIME)
        v99.clear_updaters()
        self.beat(FadeOut(strike), FadeOut(v99), Transform(b_sp, b_ok), f.sqrt.animate.set_opacity(1).set_color(OFFWHITE),
                  f.softmax.animate.set_opacity(1).set_color(LIME), f.lp.animate.set_opacity(1), f.rp.animate.set_opacity(1),
                  Transform(grad, Arrow([3.4, -2.0, 0], [3.4, -0.35, 0], buff=0, stroke_width=6, color=LIME)),
                  glab.animate.next_to(Line([3.4, -2.0, 0], [3.4, -0.35, 0]), RIGHT, buff=0.2), run=1.4)
        # b8: mix the values; the whole line glows lime
        self.beat(f.animate.set_opacity(1).set_color(LIME), FadeOut(VGroup(b_sp, grad, glab), shift=DOWN * 0.2),
                  run=0.9, focus=f.get_center() * 0.4)
        self.finish()


class M11_IT_RESOLVES(QScene):
    ASSET = "M11_IT_RESOLVES"

    def construct(self):
        self.setup_q()
        s2 = Sentence(WORDS[:-1] + ["small."]).scale(0.97).move_to(DOWN * 1.85)
        s = Sentence().scale(0.97).align_to(s2, LEFT).set_y(s2.get_y())
        base = s.get_top()[1] + 0.35
        w_small = list(W_IT)
        w_small[TROPHY], w_small[SUITCASE] = W_IT[SUITCASE], W_IT[TROPHY]      # 0.18 / 0.71, still sums to 1.00
        wb = bars(s, W_IT, 3.0, base, LIME)
        vts = [ValueTracker(w) for w in W_IT]
        labs = VGroup(*[live_txt(lambda i=i: (f"{vts[i].get_value():.2f}", LIME if vts[i].get_value() > 0.4 else OFFWHITE),
                                 20 if i in (TROPHY, SUITCASE) else 16, bold=i in (TROPHY, SUITCASE),
                                 place=lambda m, i=i: m.next_to(wb[i], UP, buff=0.1)) for i in range(12)])
        self.add(s, wb, labs)
        s.box(IT).set_stroke(LIME, 3).set_fill(LIME, 0.14)
        s.word(IT).set_color(LIME)
        s.box(TROPHY).set_stroke(LIME, 3).set_fill(LIME, 0.14)
        s.word(TROPHY).set_color(LIME)
        illustrative(self)
        s2.box(BIG).set_stroke(PUMPKIN, 3)
        s2.word(BIG).set_color(PUMPKIN)
        # b1: change big to small (one Transform owns box + word; a second box anim fought it at Gate 2)
        self.beat(Transform(s[BIG], s2[BIG]), run=0.8, focus=s[BIG].get_center() * 0.3)
        # b2: the weight shifts toward SUITCASE
        new_h = lambda w: max(w * 3.0, 0.03)
        self.beat(*[vts[i].animate.set_value(w_small[i]) for i in (TROPHY, SUITCASE)],
                  wb[TROPHY].animate.stretch_to_fit_height(new_h(w_small[TROPHY])).align_to(wb[TROPHY], DOWN),
                  wb[SUITCASE].animate.stretch_to_fit_height(new_h(w_small[SUITCASE])).align_to(wb[SUITCASE], DOWN),
                  s.box(TROPHY).animate.set_stroke(SLATE, 2.2).set_fill(BACKGROUND, 0.92), s.word(TROPHY).animate.set_color(OFFWHITE),
                  s.mark(SUITCASE), run=2.4)
        # b3: nobody wrote a rule
        rule = chip("RULE:  big → trophy", 30).move_to(UP * 2.3)
        strike = Line(rule.get_left() + RIGHT * 0.1, rule.get_right() + LEFT * 0.1).set_stroke(PUMPKIN, 5)
        self.beat(LaggedStart(FadeIn(rule, shift=DOWN * 0.15), Create(strike), lag_ratio=0.6), run=2.2,
                  focus=UP * 0.6)
        # b4: queries and keys are learned from data
        cap = chip("LEARNED, NOT WRITTEN", 30, LIME, LIME).move_to(UP * 2.3)
        self.beat(FadeOut(VGroup(rule, strike), shift=UP * 0.2), FadeIn(cap, shift=UP * 0.2),
                  wb[SUITCASE].animate(rate_func=there_and_back).set_fill(LIME, 1), run=1.4)
        self.finish()
