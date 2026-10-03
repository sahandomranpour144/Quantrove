"""EP08 chapter 6 + close: Scenes 39 (M17), 40 (M18), 41 (M18B), 44 (M19), 45 (M20), 46 (M21)."""
from ep08_common import *
from ep08_intro import tower_web


class M17_CHAIN_VS_WEB(QScene):
    ASSET = "M17_CHAIN_VS_WEB"

    def construct(self):
        self.setup_q()
        boxes, arrows = chain(5, w=0.62, gap=0.36)
        ch = VGroup(boxes, arrows).move_to(LEFT * 3.7 + DOWN * 0.1)
        wb = web(9, 2.1, 1.45, opacity=0.6, center=RIGHT * 3.7 + DOWN * 0.1)
        divider = Line([0, -2.1, 0], [0, 2.1, 0]).set_stroke(SLATE, 2.5)
        y16, y17 = chip("2016", 26).move_to([-3.7, 1.95, 0]), chip("2017", 26, LIME, LIME).move_to([3.7, 1.95, 0])
        xs = [b.get_center()[0] for b in boxes]
        t = ValueTracker(0)
        hop = Dot(radius=0.1, color=LIME)
        hop.add_updater(lambda m, dt: (t.increment_value(dt / 3.0),
                                       m.move_to([np.interp((t.get_value() % 1) * (len(xs) - 1), range(len(xs)), xs),
                                                  boxes.get_center()[1], 0])))
        self.add(t)
        # b1: split screen, chain left (2016), web right (2017)
        self.beat(FadeIn(ch, lag_ratio=0.1), FadeIn(wb[1], lag_ratio=0.1), LaggedStart(*[Create(l) for l in wb[0]], lag_ratio=0.02),
                  Create(divider), FadeIn(y16), FadeIn(y17), FadeIn(hop), run=2.4)
        # b2: the chain is the bottleneck
        bt = txt("BOTTLENECK", 26, PUMPKIN).next_to(ch, DOWN, buff=0.5)
        hop.set_color(PUMPKIN)
        self.beat(Succession(AnimationGroup(*[b.animate.set_stroke(PUMPKIN, 3.5) for b in boxes],
                                            *[a.animate.set_color(PUMPKIN).set_opacity(0.9) for a in arrows], FadeIn(bt, shift=UP * 0.15),
                                            run_time=1.2),
                             AnimationGroup(*[b.animate(rate_func=there_and_back).scale(1.12) for b in boxes], run_time=2.0)),
                  run=3.2)
        # b3: the chain dissolves
        self.beat(FadeOut(VGroup(ch, bt, hop, divider, y16), scale=0.8), run=0.7)
        hop.clear_updaters()
        # b4: the web fills the frame
        self.beat(wb.animate.scale(1.55).move_to(ORIGIN), FadeOut(y17), run=2.0)
        # b5: a GPU grid lights behind the web
        cells = VGroup(*[Square(0.5).set_stroke(SLATE, 1.2).set_fill(LIME, 0) for _ in range(18 * 8)]).arrange_in_grid(8, 18, buff=0.03)
        cells.move_to(ORIGIN)
        ph = np.random.default_rng(5).uniform(0, TAU, len(cells))
        sp = np.random.default_rng(6).uniform(1.2, 3.0, len(cells))
        lvl = ValueTracker(0)
        clock = ValueTracker(0)
        clock.add_updater(lambda m, dt: m.increment_value(dt))

        def glow(g):
            tt, L = clock.get_value(), lvl.get_value()
            for c, p, s_ in zip(g, ph, sp):
                c.set_fill(LIME, L * (0.07 + 0.2 * (0.5 + 0.5 * np.sin(tt * s_ + p))))
        cells.add_updater(glow)
        self.add(clock)
        cells.set_z_index(1)
        wb.set_z_index(3)
        self.beat(FadeIn(cells), lvl.animate.set_value(1), wb[0].animate.set_stroke(LIME, 2.0, 0.85), run=2.0)
        self.finish()


class M18_T_RETURNS(QScene):
    ASSET = "M18_T_RETURNS"

    def construct(self):
        self.setup_q()
        gpt = gpt_letters(150).move_to(UP * 0.1)
        tw = tower(6, w=4.0, h=0.56, gap=0.12).move_to(UP * 0.1)
        lines, dots = tower_web(tw)
        # b1: G P T return
        self.beat(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in gpt], lag_ratio=0.2), run=1.6)
        # b2: T glows, expands into the stacked blocks
        self.beat(FadeOut(gpt[0], shift=LEFT * 0.5), FadeOut(gpt[1], shift=LEFT * 0.3),
                  Succession(gpt[2].animate(run_time=0.6).set_color(LIME), ReplacementTransform(gpt[2], tw, run_time=1.2)), run=1.9)
        # b3: a new way to route information
        self.beat(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.006), FadeIn(dots, lag_ratio=0.02), run=1.8)
        # b4: the whole thing fits on one line
        body = VGroup(tw, lines, dots)
        f = Formula(34).move_to(ORIGIN)
        plate = RoundedRectangle(corner_radius=0.2, width=f.width + 0.8, height=f.height + 0.7).set_stroke(LIME, 2.5)
        plate.set_fill(BACKGROUND, 1).move_to(f)
        plate.set_z_index(20)
        f.set_z_index(21)                 # tower_web lines carry their own z_index
        self.beat(LaggedStart(FadeIn(plate, scale=0.95), FadeIn(f, lag_ratio=0.08), lag_ratio=0.4), run=1.5)
        # b5: and grows 800-fold
        n = ValueTracker(1)
        X0, X1, YR = -5.4, 5.4, -1.8
        ruler = Line([X0, YR, 0], [X1, YR, 0]).set_stroke(OFFWHITE, 3, 0.7)
        ticks = VGroup()
        for v in (1, 10, 100, 800):
            x = X0 + (X1 - X0) * np.log10(v) / np.log10(800)
            ticks.add(Line([x, YR - 0.12, 0], [x, YR + 0.12, 0]).set_stroke(OFFWHITE, 3, 0.7),
                      txt(f"{v}", 18, bold=False).move_to([x, YR - 0.4, 0]))
        bar = always_redraw(lambda: Line([X0, YR, 0], [X0 + (X1 - X0) * np.log10(max(n.get_value(), 1)) / np.log10(800), YR, 0])
                            .set_stroke(LIME, 9))
        big = live_txt(lambda: (f"× {n.get_value():,.0f}", LIME), 72, [3.4, 0.5, 0])
        self.add(bar, big)
        self.beat(body.animate.scale(0.72).move_to(LEFT * 2.4 + UP * 0.5), FadeOut(VGroup(plate, f), shift=DOWN * 0.2),
                  FadeIn(ruler), FadeIn(ticks), n.animate.set_value(800), run=3.0)
        self.finish()


class M18B_WHAT_IT_DID_NOT_SOLVE(QScene):
    ASSET = "M18B_WHAT_IT_DID_NOT_SOLVE"

    def construct(self):
        self.setup_q()
        f = Formula(34).move_to(UP * 1.6)
        A = chip("ATTENTION", 24, LIME, LIME).move_to([-4.6, -0.35, 0])
        N = chip("NEXT TOKEN", 24, OFFWHITE, SLATE).move_to([4.6, -0.35, 0])
        box = DashedVMobject(RoundedRectangle(corner_radius=0.15, width=3.2, height=1.0).set_stroke(PUMPKIN, 3.5)
                             .set_fill(opacity=0).move_to([0, -0.35, 0]), num_dashes=40)
        lab = txt("FACT CHECK", 22, PUMPKIN).move_to(box)
        bypass = arc(A.get_top(), N.get_top(), LIME, 4, 1, h=0.75).add_tip(tip_length=0.2)
        stream = Sentence(["the", "bank", "raised", "rates", "again"], 24, gap=0.16, center=DOWN * 1.35)
        # b1: the formula
        self.beat(LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in f.parts()], lag_ratio=0.08), FadeIn(A, shift=RIGHT * 0.2),
                  run=2.0)
        # b2: an empty FACT CHECK box
        self.beat(FadeIn(box, scale=0.9), FadeIn(lab), FadeIn(N, shift=LEFT * 0.2), run=1.4)
        # b3: the arrow skips it
        self.beat(Create(bypass), box.animate(rate_func=flicker(3)).set_stroke(PUMPKIN, 5), run=2.0)
        # b4: next-token arrow continues regardless
        self.beat(LaggedStart(*[FadeIn(stream[k], shift=RIGHT * 0.2) for k in range(3)], lag_ratio=0.3),
                  N.animate.set_stroke(LIME, 3), run=1.4)
        # b5: fluent and fast
        self.beat(LaggedStart(*[FadeIn(stream[k], shift=RIGHT * 0.2) for k in (3, 4)], lag_ratio=0.3),
                  *[stream.mark(k) for k in (3, 4)], run=1.2)
        # b6: routing is not checking
        cap = txt("ROUTING ≠ CHECKING", 44, OFFWHITE).move_to(DOWN * 2.05)
        self.beat(Write(cap), box.animate(rate_func=flicker(2)).set_stroke(PUMPKIN, 5), run=1.8)
        self.finish()


class M19_SINGLE_LINE(QScene):
    ASSET = "M19_SINGLE_LINE"

    def construct(self):
        self.setup_q()
        f = Formula(42).move_to(ORIGIN)
        rng = np.random.default_rng(19)
        bubbles = VGroup()
        for i in range(10):
            w = rng.uniform(1.4, 2.2)
            b = RoundedRectangle(corner_radius=0.2, width=w, height=0.62).set_stroke(OFFWHITE, 2, 0.28).set_fill(BACKGROUND, 0.5)
            bars_ = VGroup(*[Line(LEFT * w * 0.32, RIGHT * w * (0.18 + 0.14 * k)).set_stroke(OFFWHITE, 3, 0.25)
                             for k in range(2)]).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
            bars_.move_to(b).align_to(b, LEFT).shift(RIGHT * 0.25)
            g = VGroup(b, bars_).move_to([rng.uniform(-9, 9), rng.uniform(-2.0, 2.0), 0])
            g.speed = rng.uniform(0.8, 1.6)
            bubbles.add(g)

        def flow(m, dt):
            for g in m:
                g.shift(RIGHT * g.speed * dt)
                if g.get_left()[0] > 8.2:
                    g.shift(LEFT * 17.5)
        bubbles.add_updater(flow)
        f.set_z_index(5)
        self.add(bubbles)
        # b1: the formula alone on the grid
        self.beat(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in f.parts()], lag_ratio=0.1), run=1.6)
        # b2: faint chat bubbles flow through it
        self.beat(f.animate.set_opacity(1), run=2.0)
        # b3: slow push-in on softmax
        self.beat(f.softmax.animate.set_color(LIME), run=1.6, focus=f.softmax.get_center() * 0.6)
        self.finish()
