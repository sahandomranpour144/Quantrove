"""EP08 chapter 1: ONE WORD AT A TIME (Scenes 4, 5, 8, 11)."""
from ep08_common import *

rng8 = np.random.default_rng(8)


class M02_RNN_CHAIN(QScene):
    ASSET = "M02_RNN_CHAIN"

    def construct(self):
        self.setup_q()
        xs = [-5.1 + 1.7 * i for i in range(7)]
        words = WORDS[:7]
        boxes = VGroup(*[RoundedRectangle(corner_radius=0.1, width=0.9, height=0.9).set_stroke(OFFWHITE, 2.5)
                         .set_fill(BACKGROUND, 0.95).move_to([x, -0.3, 0]) for x in xs])
        chips = VGroup(*[tok(w).move_to([x, -1.5, 0]) for w, x in zip(words, xs)])
        ups = VGroup(*[Arrow(c.get_top(), b.get_bottom(), buff=0.06, stroke_width=3, color=OFFWHITE,
                             max_tip_length_to_length_ratio=0.3).set_opacity(0.6) for c, b in zip(chips, boxes)])
        cols = VGroup(*[mem_column(4, 0.24).move_to([x, 1.0, 0]) for x in xs])
        for c in cols:
            for cell in c:
                cell.set_fill(LIME, float(rng8.uniform(0.15, 0.85)))
        feeds = VGroup(*[Arrow(b.get_top(), c.get_bottom(), buff=0.05, stroke_width=2.5, color=LIME,
                               max_tip_length_to_length_ratio=0.3).set_opacity(0.7) for b, c in zip(boxes, cols)])
        links = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.06, stroke_width=3.5, color=LIME,
                               max_tip_length_to_length_ratio=0.25) for i in range(6)])
        # b1: words enter their boxes one by one from the left
        self.beat(LaggedStart(*[AnimationGroup(FadeIn(chips[i], shift=RIGHT * 0.6), FadeIn(boxes[i], scale=0.8),
                                               GrowArrow(ups[i])) for i in range(5)], lag_ratio=0.35), run=2.4)
        # b2: after each word, the memory column updates
        self.beat(LaggedStart(*[AnimationGroup(GrowArrow(feeds[i]), FadeIn(cols[i], shift=UP * 0.2, lag_ratio=0.15))
                                for i in range(5)], lag_ratio=0.45), run=4.0, focus=UP * 0.3)
        # b3: the memory is handed to the next step
        hand = VGroup(*[cols[i].copy() for i in range(4)])
        self.beat(LaggedStart(*[GrowArrow(l) for l in links[:4]], lag_ratio=0.25),
                  LaggedStart(*[h.animate.move_to(cols[i + 1]).set_opacity(0) for i, h in enumerate(hand)], lag_ratio=0.25),
                  run=1.8)
        self.remove(hand)
        # b4: the chain extends; label
        extra = VGroup(boxes[5:], chips[5:], ups[5:], feeds[5:], cols[5:], links[4:])
        label = chip("RECURRENT NEURAL NETWORK", 22).move_to([-3.2, 2.05, 0])
        self.beat(FadeIn(extra, shift=LEFT * 0.4), FadeIn(label, shift=DOWN * 0.15),
                  run=1.8)
        self.finish()


class M03_MEMORY_SQUEEZE(QScene):
    ASSET = "M03_MEMORY_SQUEEZE"

    def construct(self):
        self.setup_q()
        r = np.random.default_rng(30)
        para = VGroup()
        for line in range(3):
            x = -6.0
            for k in range(10):
                w = float(r.uniform(0.24, 0.5))
                c = RoundedRectangle(corner_radius=0.06, width=w, height=0.3).set_stroke(SLATE, 2).set_fill(OFFWHITE, 0.16)
                c.move_to([x + w / 2, 0.9 - 0.6 * line, 0])
                para.add(c)
                x += w + 0.1
        para.move_to([-2.9, 0.3, 0])
        H, W, cx, cy = 3.4, 1.0, 3.3, 0.1
        frame = RoundedRectangle(corner_radius=0.08, width=W + 0.2, height=H + 0.2).set_stroke(OFFWHITE, 2.2).move_to([cx, cy, 0])
        feed = Arrow([0.0, 0.3, 0], [cx - 0.75, 0.3, 0], buff=0, stroke_width=4, color=OFFWHITE).set_opacity(0.6)
        n, tau, tint = ValueTracker(0), ValueTracker(100), ValueTracker(0)

        def col():
            m = n.get_value()
            g = VGroup()
            if m <= 0.01:
                return g
            k_n = int(np.ceil(m))
            h = H / max(m, 1)
            for k in range(k_n):
                age = m - 1 - k
                op = max(0.3, float(np.exp(-max(age, 0) / tau.get_value())))
                if k == k_n - 1:
                    op *= min(1, m - k)
                c = LIME
                if age > 4:
                    t = tint.get_value()
                    c = interpolate_color(ManimColor(LIME), ManimColor(PUMPKIN), min(t, 1)) if t <= 1 else \
                        interpolate_color(ManimColor(PUMPKIN), ManimColor(OFFWHITE), min(t - 1, 1))
                if age > 4 and tint.get_value() > 1:
                    op *= 1 - 0.6 * min(tint.get_value() - 1, 1)     # overwritten -> faint grey
                g.add(Rectangle(width=W, height=max(h - 0.015, 0.02)).set_stroke(width=0).set_fill(c, op)
                      .move_to([cx, cy - H / 2 + h * (k + 0.5), 0]))
            return g

        stripes = always_redraw(col)

        def para_upd(m):
            cur = int(n.get_value())
            for k, c in enumerate(m):
                c.set_fill(LIME if k == cur else OFFWHITE, 0.85 if k == cur else (0.05 if k < cur else 0.16))
        # b1: a 30-word sentence lines up against the memory column
        self.beat(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in para], lag_ratio=0.03), Create(frame),
                  GrowArrow(feed), run=1.0)
        para.add_updater(para_upd)
        self.add(stripes)
        # b2: words start flowing into the one column
        self.beat(n.animate.set_value(10), run=1.8)
        # b3: everything squeezed through the same list
        self.beat(n.animate.set_value(30), run=3.4)
        para.clear_updaters()
        para_upd(para)
        w1 = txt("WORD 1", 18, bold=False).next_to(frame, DOWN, buff=0.12)
        w30 = txt("WORD 30", 18, bold=False).next_to(frame, UP, buff=0.12)
        # b4: early words fade
        self.beat(tau.animate.set_value(3.5), tint.animate.set_value(1), FadeIn(w1), FadeIn(w30), run=1.4,
                  focus=[cx * 0.5, 0, 0])
        # b5: details get overwritten
        self.beat(tint.animate.set_value(2), tau.animate.set_value(2.2), frame.animate.set_stroke(PUMPKIN, 2.5), run=1.6)
        self.finish()


class M04_DISTANT_LINK(QScene):
    ASSET = "M04_DISTANT_LINK"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(DOWN * 0.2)
        hp = hops(s)
        a0 = arc(s[IT].get_top(), s[TROPHY].get_top(), LIME, 3.5, 1, h=1.9)
        link = DashedVMobject(a0, num_dashes=40)
        q = chip("?", 26, LIME, LIME).move_to(a0.point_from_proportion(0.5) + UP * 0.05)
        # b1: sentence as a chain; a long arc is needed from IT back to TROPHY
        self.beat(LaggedStart(FadeIn(s, lag_ratio=0.08), Create(hp, lag_ratio=0.1),
                              AnimationGroup(s.mark(IT), s.mark(TROPHY), Create(link), FadeIn(q, scale=0.6)),
                              lag_ratio=0.45), run=3.6)
        # b2: the information has to travel through every box; memory fades along the way
        path = VMobject()
        path.set_points(np.concatenate([hp[i].points for i in range(TROPHY, IT)]))
        x0, x1 = s[TROPHY].get_center()[0], s[IT].get_center()[0]
        pulse = glow_dot(path.get_start(), PUMPKIN, 0.09)
        pulse.add_updater(lambda m: m.set_opacity(float(np.clip(1 - 0.8 * (m.get_center()[0] - x0) / (x1 - x0), 0.2, 1))))
        steps = [hp[i] for i in range(TROPHY, IT)]
        self.add(pulse)
        self.beat(MoveAlongPath(pulse, path),
                  LaggedStart(*[h.animate.set_color(PUMPKIN).set_opacity(1 - 0.11 * j) for j, h in enumerate(steps)],
                              lag_ratio=0.5),
                  LaggedStart(*[s.box(i).animate.set_stroke(PUMPKIN, 2.5, opacity=1 - 0.1 * (i - TROPHY - 1))
                                for i in range(TROPHY + 1, IT)], lag_ratio=0.5), run=2.9)
        self.finish()


def cursor_icon():
    p = Polygon([0, 0, 0], [0, -0.62, 0], [0.16, -0.47, 0], [0.29, -0.74, 0], [0.38, -0.69, 0], [0.26, -0.43, 0],
                [0.46, -0.42, 0])
    return p.set_fill(OFFWHITE, 1).set_stroke(BACKGROUND, 2)


class M05_DELETE_QUESTION(QScene):
    ASSET = "M05_DELETE_QUESTION"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(DOWN * 0.1)
        hp = hops(s)
        att = weighted_arcs(s, IT, W_IT)
        # b1: chain + attention lines
        self.beat(FadeIn(s, lag_ratio=0.05), Create(hp, lag_ratio=0.08), s.mark(IT),
                  LaggedStart(*[Create(a) for a in att], lag_ratio=0.08), run=2.0)
        # b2: the step-by-step chain highlights in Pumpkin
        self.beat(hp.animate.set_color(PUMPKIN).set_opacity(1), run=1.0, focus=DOWN * 0.5)
        # b3: a cursor hovers DELETE? over the chain
        sel = DashedVMobject(SurroundingRectangle(hp, buff=0.14, corner_radius=0.08), num_dashes=70).set_stroke(PUMPKIN, 2.5)
        cur = cursor_icon().move_to([4.6, -2.4, 0])
        tag = chip("DELETE?", 26, PUMPKIN, PUMPKIN).next_to(sel, DOWN, buff=0.18).shift(RIGHT * 1.6)
        self.beat(cur.animate.move_to(tag.get_left() + LEFT * 0.35 + UP * 0.15), Create(sel),
                  LaggedStart(Wait(), FadeIn(tag, scale=0.8), lag_ratio=0.6),
                  hp.animate(rate_func=there_and_back).set_opacity(0.35), run=2.2)
        self.finish()
