"""EP08 shared visual objects: one trophy sentence, chain, attention arcs, formula, blocks, grids.
Every scene that shows the sentence/formula builds it here so it looks identical everywhere."""
import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", ".."))
sys.path.insert(0, os.path.join(_HERE, "..", "ep07"))
from qvis import *

WORDS = ["The", "trophy", "didn't", "fit", "in", "the", "suitcase", "because", "it", "was", "too", "big."]
TROPHY, SUITCASE, IT, BIG = 1, 6, 8, 11
TOK_H = 0.62          # chip height at size 28 (scales with size)
W_IT = [0.01, 0.71, 0.01, 0.01, 0.01, 0.01, 0.18, 0.01, 0.01, 0.01, 0.01, 0.02]   # IT -> words, ILLUSTRATIVE
assert abs(sum(W_IT) - 1) < 1e-9
ILLU_BUFF = np.array([0.75, 1.7, 0])   # keeps the ILLUSTRATIVE tag inside the safe area


def illustrative(scene):
    return scene.hud(txt("ILLUSTRATIVE", 16, OFFWHITE, bold=False).set_opacity(0.6), DR, buff=ILLU_BUFF)


class Sentence(VGroup):
    """The trophy sentence as 12 token chips (typeset as one line so baselines match).
    self[i] = VGroup(box, word). Same look in every scene."""

    def __init__(self, words=WORDS, size=21, gap=0.13, center=ORIGIN):
        super().__init__()
        line = CleanText(" ".join(words), font_size=size, color=OFFWHITE, weight=BOLD, disable_ligatures=True)
        k, pad, h = 0, 0.16 * size / 28, TOK_H * size / 28
        x = 0.0
        for w in words:
            g = VGroup(*line[k:k + len(w)])
            k += len(w) + 1          # ligatures disabled -> spaces are (empty) glyphs too
            g.shift(RIGHT * (x + pad - g.get_left()[0]))
            box = RoundedRectangle(corner_radius=0.09 * size / 28, width=g.width + 2 * pad, height=h)
            box.set_stroke(SLATE, 2.2).set_fill(BACKGROUND, 0.92)
            box.move_to([g.get_center()[0], line.get_center()[1], 0])
            self.add(VGroup(box, g))
            x += box.width + gap
        self.move_to(center)

    def box(self, i):
        return self[i][0]

    def word(self, i):
        return self[i][1]

    def mark(self, i, color=LIME, fill=0.14):
        """Animation: chip i turns accent color."""
        return AnimationGroup(self.box(i).animate.set_stroke(color, 3).set_fill(color, fill),
                              self.word(i).animate.set_color(color))


def arc(a, b, color=LIME, width=2.5, opacity=0.8, up=True, h=None):
    """Attention arc between two points on a row; bulges above (up) by height h (default grows with span, capped)."""
    c = abs(b[0] - a[0])
    h = min(0.32 * c, 1.0) + 0.08 if h is None else h
    ang = 4 * np.arctan(2 * h / max(c, 1e-3))
    ang = -ang if (b[0] > a[0]) == up else ang
    return ArcBetweenPoints(a, b, angle=ang).set_stroke(color, width, opacity)


def all_arcs(sent, color=LIME, width=1.6, opacity=0.45, up=True):
    pts = [(s.get_top() if up else s.get_bottom()) for s in sent]
    return VGroup(*[arc(pts[i], pts[j], color, width, opacity, up)
                    for i in range(len(pts)) for j in range(i + 1, len(pts))])


def hops(sent, color=OFFWHITE, opacity=0.55):
    """Old recurrent chain drawn under the sentence: one curved hop arrow per step."""
    g = VGroup()
    for i in range(len(sent) - 1):
        a, b = sent[i].get_bottom() + DOWN * 0.05, sent[i + 1].get_bottom() + DOWN * 0.05
        g.add(CurvedArrow(a, b, angle=0.9, stroke_width=2.5, tip_length=0.12, color=color).set_opacity(opacity))
    return g


def tok(w, size=21):
    """Single chip in the sentence style."""
    return Sentence([w], size)[0]


def weighted_arcs(sent, src, weights, color=LIME, wmax=7.0):
    """Arcs from token src to every other token, stroke width/opacity by weight."""
    p = sent[src].get_top()
    return VGroup(*[arc(p, sent[j].get_top(), color, 1 + wmax * w, 0.25 + 0.75 * min(1, w * 1.4))
                    for j, w in enumerate(weights) if j != src])


def mem_column(n=5, cell=0.28, color=LIME, fill=0.55):
    """Memory vector as a column of cells."""
    g = VGroup(*[Square(cell).set_stroke(SLATE, 2).set_fill(color, fill) for _ in range(n)])
    return g.arrange(DOWN, buff=0.04)


def chain(n, w=0.78, gap=0.42, color=SLATE):
    """Recurrent chain: n boxes joined by arrows. Returns (boxes, arrows)."""
    boxes = VGroup(*[RoundedRectangle(corner_radius=0.08, width=w, height=w).set_stroke(color, 2.5)
                     .set_fill(BACKGROUND, 0.92) for _ in range(n)]).arrange(RIGHT, buff=gap)
    arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.04, stroke_width=3,
                            max_tip_length_to_length_ratio=0.35, color=OFFWHITE).set_opacity(0.55)
                      for i in range(n - 1)])
    return boxes, arrows


class Formula(VGroup):
    """Attention(Q, K, V) = softmax( QKᵀ / √dₖ ) V, built from CleanText pieces.
    Named parts: lhs, eq, softmax, lp, qk, bar, sqrt, rp, v."""

    def __init__(self, size=46):
        super().__init__()
        s = size
        self.lhs = txt("Attention(Q, K, V)", s)
        self.eq = txt("=", s)
        self.softmax = txt("softmax", s)
        q, k = txt("Q", s), txt("K", s)
        t = txt("T", s * 0.55)
        VGroup(q, k).arrange(RIGHT, buff=0.04 * s / 46, aligned_edge=DOWN)
        t.next_to(k, UR, buff=0.02).shift(DOWN * 0.12 * s / 46)
        self.qk = VGroup(q, k, t)
        d = txt("d", s)
        kk = txt("k", s * 0.55).next_to(d, DR, buff=0.02).shift(UP * 0.1 * s / 46)
        dk = VGroup(d, kk)
        u = s / 46
        x0, x1 = dk.get_left()[0] - 0.1 * u, dk.get_right()[0] + 0.06 * u
        yt, yb = dk.get_top()[1] + 0.1 * u, dk.get_bottom()[1] - 0.04 * u
        ym = (yt + yb) / 2 - 0.05 * u
        rad = VMobject().set_points_as_corners([
            [x0 - 0.42 * u, ym, 0], [x0 - 0.32 * u, ym + 0.06 * u, 0], [x0 - 0.19 * u, yb, 0],
            [x0, yt, 0], [x1, yt, 0]])
        rad.set_stroke(OFFWHITE, 3.2 * u)
        self.sqrt = VGroup(rad, dk)
        frac_w = max(self.qk.width, self.sqrt.width) + 0.3 * u
        self.bar = Line(LEFT * frac_w / 2, RIGHT * frac_w / 2).set_stroke(OFFWHITE, 3.2 * u)
        self.qk.next_to(self.bar, UP, buff=0.14 * u)
        self.sqrt.next_to(self.bar, DOWN, buff=0.14 * u)
        frac = VGroup(self.qk, self.bar, self.sqrt)
        ph = frac.height * 1.08
        self.lp = txt("(", s).stretch_to_fit_height(ph)
        self.rp = txt(")", s).stretch_to_fit_height(ph)
        self.v = txt("V", s)
        self.lhs.next_to(self.eq, LEFT, buff=0.3 * u)
        self.softmax.next_to(self.eq, RIGHT, buff=0.3 * u)
        self.lp.next_to(self.softmax, RIGHT, buff=0.06 * u)
        frac.next_to(self.lp, RIGHT, buff=0.08 * u).match_y(self.eq)
        self.rp.next_to(frac, RIGHT, buff=0.08 * u).match_y(self.lp)
        self.lp.match_y(frac)
        self.rp.match_y(frac)
        self.v.next_to(self.rp, RIGHT, buff=0.12 * u).align_to(self.softmax, DOWN)
        self.add(self.lhs, self.eq, self.softmax, self.lp, self.qk, self.bar, self.sqrt, self.rp, self.v)
        self.move_to(ORIGIN)

    def parts(self):
        return [self.lhs, self.eq, self.softmax, self.lp, self.qk, self.bar, self.sqrt, self.rp, self.v]


def block(w=3.2, h=1.2):
    """One Transformer block: attention band (lime) over processing band (off-white)."""
    outer = RoundedRectangle(corner_radius=0.12, width=w, height=h).set_stroke(SLATE, 3).set_fill(BACKGROUND, 0.95)
    att = RoundedRectangle(corner_radius=0.07, width=w - 0.3, height=h * 0.32).set_stroke(LIME, 2.2).set_fill(LIME, 0.12)
    ffn = RoundedRectangle(corner_radius=0.07, width=w - 0.3, height=h * 0.32).set_stroke(OFFWHITE, 2).set_fill(OFFWHITE, 0.06)
    att.move_to(outer.get_center() + UP * h * 0.2)
    ffn.move_to(outer.get_center() + DOWN * h * 0.2)
    return VGroup(outer, att, ffn)


def tower(n=6, w=3.2, h=0.62, gap=0.1):
    return VGroup(*[block(w, h) for _ in range(n)]).arrange(UP, buff=gap)


def pair_grid(n, cell=0.3, gap=0.04, color=SLATE):
    g = VGroup(*[Square(cell).set_stroke(color, 1.6).set_fill(BACKGROUND, 0.9) for _ in range(n * n)])
    return g.arrange_in_grid(n, n, buff=gap)


def gpt_letters(size=150):
    return VGroup(*[txt(c, size) for c in "GPT"]).arrange(RIGHT, buff=0.35)


def chip(s, size=22, color=OFFWHITE, stroke=SLATE):
    """Small label card."""
    t = txt(s, size, color)
    box = RoundedRectangle(corner_radius=0.08, width=t.width + 0.4, height=t.height + 0.3).set_stroke(stroke, 2.2)
    box.set_fill(BACKGROUND, 0.92).move_to(t)
    return VGroup(box, t)


def web(n=9, rx=2.2, ry=1.5, color=LIME, width=1.4, opacity=0.6, center=ORIGIN):
    """Complete attention graph on an ellipse. Returns VGroup(lines, dots)."""
    pts = [center + np.array([rx * np.cos(a), ry * np.sin(a), 0]) for a in np.linspace(0.3, 0.3 + TAU, n, endpoint=False)]
    lines = VGroup(*[Line(pts[i], pts[j]) for i in range(n) for j in range(i + 1, n)]).set_stroke(color, width, opacity)
    dots = VGroup(*[glow_dot(p, color, 0.06) for p in pts])
    return VGroup(lines, dots)


def live_txt(get, size, pos=None, bold=True, place=None):
    """Text that rebuilds only when (string, color) changes (CleanText is slow to rebuild every frame).
    place(m) re-positions it every frame (e.g. follow a moving bar); else it stays at `pos`."""
    k0 = get()
    place = place or (lambda m: m.move_to(pos))
    m = txt(k0[0], size, k0[1], bold=bold)
    place(m)
    m.key = k0

    def upd(mm):
        k = get()
        if k != mm.key:
            mm.become(txt(k[0], size, k[1], bold=bold))
            mm.key = k
        place(mm)
    m.add_updater(upd)
    return m
