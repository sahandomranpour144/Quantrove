"""EP08 intro (Scene 2). Render: see PRODUCTION_BRIEF.md (Manim)."""
from ep08_common import *


def tower_web(tw, n=5, opacity=0.32):
    """Thin lime lines between token nodes of consecutive blocks (attention routing through the stack)."""
    nodes = [[b.get_left() + RIGHT * b.width * (k + 1) / (n + 1) for k in range(n)] for b in tw]
    lines = VGroup(*[Line(p, q) for a, b in zip(nodes, nodes[1:]) for p in a for q in b])
    dots = VGroup(*[Dot(p, radius=0.035, color=LIME) for row in nodes for p in row])
    return lines.set_stroke(LIME, 1.2, opacity), dots


class M01_T_IN_GPT(QScene):
    ASSET = "M01_T_IN_GPT"

    def construct(self):
        self.setup_q()
        gpt = gpt_letters(150).move_to(UP * 0.1)
        gpt[2].set_color(LIME)
        self.add(gpt)
        tw = tower(6, w=4.0, h=0.56, gap=0.12).move_to(UP * 0.1)
        # b1: G, P slide away; the T expands into a stacked-block silhouette
        self.beat(FadeOut(gpt[0], shift=LEFT * 0.6), FadeOut(gpt[1], shift=LEFT * 0.3),
                  ReplacementTransform(gpt[2], tw), run=1.1)
        # b2: thin attention lines web across the blocks
        lines, dots = tower_web(tw)
        self.beat(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.006), FadeIn(dots, lag_ratio=0.02), run=2.0)
        # b3: 8 author dots orbit the stack
        phase = ValueTracker(0)
        phase.add_updater(lambda m, dt: m.increment_value(0.55 * dt))
        rs = [ValueTracker(3.0) for _ in range(8)]
        authors = VGroup()
        for i in range(8):
            d = glow_dot(ORIGIN, LIME, 0.075)
            d.add_updater(lambda m, i=i: m.move_to(UP * 0.1 + rs[i].get_value() * np.array(
                [np.cos(phase.get_value() + i * TAU / 8), 0.42 * np.sin(phase.get_value() + i * TAU / 8), 0])))
            authors.add(d)
        self.add(phase)
        self.beat(LaggedStart(*[FadeIn(d, scale=0.3) for d in authors], lag_ratio=0.12), run=1.8)
        # b4: calm hold; one by one the authors drift off-frame
        self.beat(LaggedStart(*[r.animate.set_value(14) for r in rs], lag_ratio=0.1),
                  lines.animate.set_stroke(opacity=0.5), run=3.3)
        self.finish()
