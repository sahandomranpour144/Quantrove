"""EP08 close: Scenes 45 (M20_CTA_SPLIT), 46 (M21_END_SCREEN_BG)."""
from ep08_common import *
from ep07_intro import CLOUD, cloud_dots


class M20_CTA_SPLIT(QScene):
    ASSET = "M20_CTA_SPLIT"

    def construct(self):
        self.setup_q()
        wb = web(11, 3.0, 1.9, opacity=0.6)
        # b1: the attention web builds, then shrinks to the left
        self.beat(Succession(AnimationGroup(FadeIn(wb[1], lag_ratio=0.05),
                                            LaggedStart(*[Create(l) for l in wb[0]], lag_ratio=0.008), run_time=1.5),
                             wb.animate(run_time=1.8).scale(0.62).move_to(LEFT * 3.7)), run=3.3)
        # b2: EP07's word cloud appears on the right and slowly turns
        cloud = cloud_dots(CLOUD).scale(0.5).move_to(RIGHT * 3.8)
        cloud.add_updater(lambda m, dt: m.rotate(0.15 * dt, axis=UP, about_point=m.get_center()))
        self.beat(LaggedStart(*[FadeIn(d, scale=0.3) for d in cloud], lag_ratio=0.004), run=2.6)
        # b3: dashed bridge QUERY / KEY -> POINTS IN SPACE
        a, b = LEFT * 1.3, RIGHT * 1.6
        bridge = DashedLine(a, b, dash_length=0.18).set_stroke(LIME, 4)
        head = Triangle().scale(0.12).rotate(-PI / 2).set_fill(LIME, 1).set_stroke(LIME, 1).move_to(b)
        l1 = chip("QUERY / KEY", 22, OFFWHITE, LIME).move_to([-3.7, -2.0, 0])
        l2 = chip("POINTS IN SPACE", 22, OFFWHITE, LIME).move_to([3.8, -2.0, 0])
        pulse = Dot(radius=0.09, color=LIME)
        tt = ValueTracker(0)
        pulse.add_updater(lambda m, dt: (tt.increment_value(dt / 1.2), m.move_to(a + (b - a) * (tt.get_value() % 1))))
        self.add(tt)
        self.beat(Create(bridge), FadeIn(head), FadeIn(pulse), FadeIn(l1, shift=UP * 0.15), FadeIn(l2, shift=UP * 0.15), run=1.6)
        # b4: frame clears toward the end-screen layout
        pulse.clear_updaters()
        self.beat(FadeOut(VGroup(wb, cloud, bridge, head, pulse, l1, l2), scale=0.9), run=1.1)
        self.finish()


class M21_END_SCREEN_BG(QScene):
    ASSET = "M21_END_SCREEN_BG"

    def construct(self):
        self.setup_q(grid=False)
        self.add(ambient_grid(opacity=0.2, drift=0.04))
        rng = np.random.default_rng(21)
        n = 16
        base = np.stack([rng.uniform(-6.2, 6.2, n), rng.uniform(-2.5, 2.5, n)], 1)
        w = rng.uniform(0.15, 0.4, (n, 2))
        ph = rng.uniform(0, TAU, (n, 2))
        clock = ValueTracker(0)
        clock.add_updater(lambda m, dt: m.increment_value(dt))
        pos = lambda t: [np.array([base[i, 0] + 0.7 * np.sin(w[i, 0] * t + ph[i, 0]),
                                   base[i, 1] + 0.5 * np.cos(w[i, 1] * t + ph[i, 1]), 0]) for i in range(n)]
        idx = [(i, j) for i in range(n) for j in range(i + 1, n)]
        lines = VGroup(*[Line(ORIGIN, RIGHT) for _ in idx]).set_stroke(LIME, 1.6, 0.2)
        dots = VGroup(*[Dot(radius=0.05, color=LIME).set_opacity(0.3) for _ in range(n)])

        def upd(_):
            P = pos(clock.get_value())
            for l, (i, j) in zip(lines, idx):
                d = np.linalg.norm(P[i] - P[j])
                l.put_start_and_end_on(P[i], P[j]).set_stroke(LIME, 1.6, 0.2 * float(np.clip(1.6 - d / 5.0, 0, 1)))
            for dd, p in zip(dots, P):
                dd.move_to(p)
        web_ = VGroup(lines, dots)
        web_.add_updater(upd)
        self.add(clock, web_)
        self.beat(run=20)
        self.finish()
