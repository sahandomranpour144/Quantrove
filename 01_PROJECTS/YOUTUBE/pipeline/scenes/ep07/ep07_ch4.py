"""EP07 chapter 4 Manim scenes (S34 M14A, S36 M14, S37 M15). Render: see PRODUCTION_BRIEF.md."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ep07_ch3 import *

_GL = {}


def numtxt(s, size=40, color=OFFWHITE):
    """Per-frame-safe number text: cached glyphs (Pango text creation is ~1 s each; too slow inside always_redraw)."""
    gl = []
    for ch in s:
        k = (ch, size, str(color))
        if k not in _GL:
            _GL[k] = txt(ch, size, color)
        gl.append(_GL[k].copy())
    g = VGroup(*gl).arrange(RIGHT, buff=0.035 * size / 40, aligned_edge=DOWN)
    digits = [m for m, ch in zip(g, s) if ch.isdigit()]
    if digits:
        for m, ch in zip(g, s):
            if ch == "°":
                m.align_to(digits[0], UP)
    return g


HERE = os.path.dirname(os.path.abspath(__file__))
D_NODES = sorted({2, 3, 100, 12288} | {int(round(x)) for x in np.geomspace(3, 100, 14)}
                 | {int(round(x)) for x in np.geomspace(100, 12288, 26)})
N_PAIRS, BIN_DEG = 4000, 2.0
EDGES = np.arange(0, 180 + BIN_DEG, BIN_DEG)


def angle_data():
    """REAL angles between random Gaussian vector pairs (numpy seed 7), cached. Returns hists, samples."""
    cache = os.path.join(HERE, "m14a_angles_seed7.npz")
    if os.path.exists(cache):
        z = np.load(cache)
        return z["hists"], z["samples"], z["within"]
    rng = np.random.default_rng(7)
    hists, samples, within = [], [], []
    for d in D_NODES:
        ang = []
        for _ in range(0, N_PAIRS, 500):
            a = rng.standard_normal((500, d), dtype=np.float32)
            b = rng.standard_normal((500, d), dtype=np.float32)
            c = (a * b).sum(1) / (np.linalg.norm(a, axis=1) * np.linalg.norm(b, axis=1))
            ang.append(np.degrees(np.arccos(np.clip(c, -1, 1))))
        ang = np.concatenate(ang)
        hists.append(np.histogram(ang, bins=EDGES)[0].astype(float))
        s = np.full(64, np.nan); s[:64] = ang[:64]
        samples.append(s)
        within.append(float(np.mean(np.abs(ang - 90) < 1)) * 100)
    hists, samples, within = np.array(hists), np.array(samples), np.array(within)
    np.savez(cache, hists=hists, samples=samples, within=within)
    return hists, samples, within


class M14A_ROOM_IN_HIGH_DIMS(QScene):
    ASSET = "M14A_ROOM_IN_HIGH_DIMS"

    def construct(self):
        self.setup_q()
        H, S, W = angle_data()
        LD = np.log(D_NODES)
        i2, i3, i100 = D_NODES.index(2), D_NODES.index(3), D_NODES.index(100)
        iE = len(D_NODES) - 1
        u = ValueTracker(0)          # continuous node index
        grow = ValueTracker(0)       # histogram grow-in
        clock = ValueTracker(0)
        self.add(u, grow, clock)
        clock.add_updater(lambda m, dt: m.increment_value(dt))

        def dval():
            x = float(np.clip(u.get_value(), 0, iE)); i = min(int(x), iE - 1); f = x - i
            return float(np.exp(LD[i] * (1 - f) + LD[i + 1] * f))

        # ---- histogram panel (right) ----
        X0, X1, YB, HH = -0.9, 6.3, -1.75, 3.2
        axis = Line([X0, YB, 0], [X1, YB, 0], stroke_color=SLATE, stroke_width=3)
        ticks = VGroup(*[VGroup(Line([X0 + (X1 - X0) * a / 180, YB, 0], [X0 + (X1 - X0) * a / 180, YB - 0.1, 0],
                                     stroke_color=SLATE, stroke_width=3),
                                txt(f"{a}°", 22, bold=False).move_to([X0 + (X1 - X0) * a / 180, YB - 0.34, 0]))
                        for a in (0, 90, 180)])
        ylab = txt("SHARE OF PAIRS", 20, bold=False).set_opacity(0.8).move_to([(X0 + X1) / 2, YB + HH + 0.3, 0])

        def hist():
            x = float(np.clip(u.get_value(), 0, iE)); i = min(int(x), iE - 1); f = x - i
            h = H[i] * (1 - f) + H[i + 1] * f
            h = h / h.max() * HH * grow.get_value()
            xs = X0 + (X1 - X0) * EDGES / 180
            pts = [[xs[0], YB, 0]]
            for k, hk in enumerate(h):
                pts += [[xs[k], YB + hk, 0], [xs[k + 1], YB + hk, 0]]
            pts += [[xs[-1], YB, 0], [xs[0], YB, 0]]
            return VMobject(fill_color=LIME, fill_opacity=0.28, stroke_color=LIME, stroke_width=3).set_points_as_corners(pts)

        hist_m = always_redraw(hist)

        # ---- arrows panel (left) ----
        C, R = np.array([-3.9, -0.15, 0]), 1.55
        ring = Circle(radius=R, stroke_color=SLATE, stroke_width=3).move_to(C)
        rr = np.random.default_rng(3)

        def pair():
            x = float(np.clip(u.get_value(), 0, iE)); i = min(int(round(x)), iE)
            k = int(clock.get_value() / 0.55) % 64
            th = float(S[i][k]) * (1 if k % 2 else -1)
            a0 = np.radians(25 + 40 * np.sin(clock.get_value() * 0.3))
            va = np.array([np.cos(a0), np.sin(a0), 0]) * R
            vb = np.array([np.cos(a0 + np.radians(th)), np.sin(a0 + np.radians(th)), 0]) * R
            arc = Arc(radius=0.55, start_angle=a0, angle=np.radians(th), arc_center=C, stroke_color=PUMPKIN,
                      stroke_width=4)
            lab = numtxt(f"{abs(th):.0f}°", 28, PUMPKIN).move_to(C + np.array([np.cos(a0 + np.radians(th) / 2),
                                                                           np.sin(a0 + np.radians(th) / 2), 0]) * 0.98)
            return VGroup(Arrow(C, C + va, buff=0, stroke_width=6, color=LIME, tip_length=0.22),
                          Arrow(C, C + vb, buff=0, stroke_width=6, color=OFFWHITE, tip_length=0.22), arc, lab)

        pair_m = always_redraw(pair)
        dlab = txt("d =", 46, bold=False)
        dm = always_redraw(lambda: VGroup(dlab, numtxt(f"{dval():,.0f}", 56, LIME))
                           .arrange(RIGHT, buff=0.2).move_to([-3.9, 2.05, 0]))
        tag(self, "REAL ANGLES · SEED 7", corner=DL)
        # b1: 2D: the angle between two random arrows swings anywhere; flat histogram builds
        self.add(ring, pair_m)
        self.beat(FadeIn(ring), FadeIn(dm), Create(axis), FadeIn(ticks), FadeIn(ylab), grow.animate.set_value(1),
                  run=2.4)
        self.add(hist_m)
        # b2: 3D: angles start to bunch toward 90
        self.beat(u.animate.set_value(i3), run=1.6)
        # b3: dimension counter climbs: 100, then 12,288; the histogram narrows
        self.beat(Succession(u.animate(run_time=1.6).set_value(i100), Wait(0.3), u.animate(run_time=1.9).set_value(iE)),
                  run=3.8)
        # b4: the peak locks at 90 degrees
        ang = ((X0 + X1) / 2)
        line90 = DashedLine([ang, YB, 0], [ang, YB + HH + 0.1, 0], stroke_color=LIME, stroke_width=3)
        lab = txt("NEARLY PERPENDICULAR", 30, LIME).move_to([ang + 0.0, YB + HH + 0.55, 0])
        self.beat(Create(line90), FadeIn(lab, shift=DOWN * 0.2), FadeOut(ylab), run=1.8)
        # b5: how tight: share of pairs within +-1 degree of 90 (computed from the same data)
        within = float(W[iE])
        pct = ValueTracker(0)
        plab = txt("WITHIN ±1° OF 90°", 24, bold=False)
        pm = always_redraw(lambda: VGroup(numtxt(f"{pct.get_value():.0f}%", 52, LIME), plab)
                           .arrange(RIGHT, buff=0.25).move_to([ang, YB + HH + 1.05, 0]))
        self.add(pm)
        self.beat(pct.animate.set_value(within), lab.animate.shift(DOWN * 0.0), run=2.8)
        self.finish()
        print(f"M14A within +-1deg of 90 at d=12288: {within:.2f}%")


# ---------------------------------------------------------------------------------------------
BANK_MID = (CLUSTERS["MONEY"] + CLUSTERS["RIVER"]) / 2
MONEY_W = [("RATES", CLUSTERS["MONEY"] + np.array([-0.45, 0.45, 0.1])), ("LOAN", CLUSTERS["MONEY"] + np.array([0.35, -0.5, 0.1]))]
RIVER_W = [("WATER", CLUSTERS["RIVER"] + np.array([0.3, 0.5, 0.0])), ("SHORE", CLUSTERS["RIVER"] + np.array([-0.4, -0.5, 0.2]))]


class M14_BANK_SPLIT(QScene):
    ASSET = "M14_BANK_SPLIT"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.03, k=1.0)
        cloud = pj.cloud(MAP_CORE, dim=0.35, lime_z=MAP_CORE_LIME)
        hm = pj.cloud(cluster_pts("MONEY"), r=0.1, color=LIME, opacity=0.34, dim=0)
        hr = pj.cloud(cluster_pts("RIVER"), r=0.1, color=PUMPKIN, opacity=0.5, dim=0)
        self.add(cloud, hm, hr)
        s = ValueTracker(0)
        start = np.array([0.0, 1.0, 0.2])
        bpos = lambda: start + (BANK_MID - start) * s.get_value()
        bank = pj.pin(label_dot("BANK", start, OFFWHITE, size=34), bpos)
        # b1: BANK appears
        self.beat(FadeIn(bank, scale=0.4), cloud.dim.animate.set_value(0.3), run=1.4)
        mw = VGroup(*[pj.pin(label_dot(w, p, LIME, size=26), p) for w, p in MONEY_W])
        # b2: money cluster lights lime (RATES, LOAN)
        self.beat(hm.dim.animate.set_value(1), FadeIn(mw, scale=0.6), run=1.2)
        rw = VGroup(*[pj.pin(label_dot(w, p, PUMPKIN, size=26), p) for w, p in RIVER_W])
        # b3: river cluster lights pumpkin (WATER, SHORE)
        self.beat(hr.dim.animate.set_value(1), FadeIn(rw, scale=0.6), run=1.8)
        # b4: tugged both ways, BANK parks at the midpoint with a dashed ? ring
        tm = pj.link(bpos, CLUSTERS["MONEY"], LIME, 3, cls=Line, g=1, o=0, trim=0.2)
        tr = pj.link(bpos, CLUSTERS["RIVER"], PUMPKIN, 3, cls=Line, g=1, o=0, trim=0.2)
        q = VGroup(DashedVMobject(Circle(radius=0.42, stroke_color=OFFWHITE, stroke_width=3), num_dashes=16),
                   txt("?", 34, PUMPKIN))
        pj.pin(q, bpos, idx=None)
        self.add(tm, tr)
        self.beat(s.animate.set_value(1), tm.o.animate.set_value(0.8), tr.o.animate.set_value(0.8),
                  FadeIn(q, scale=0.5), run=1.8, focus=pj.P(BANK_MID) * 0.3)
        # b5: wrong for both: tension pulses
        self.beat(Indicate(q, color=PUMPKIN, scale_factor=1.2), tm.o.animate(rate_func=there_and_back).set_value(0.3),
                  tr.o.animate(rate_func=there_and_back).set_value(0.3), run=1.6)
        self.finish()


# ---------------------------------------------------------------------------------------------
def pinned_layer(scene, vt, pos=(-5.0, 2.35)):
    """'LAYER n' readout that follows the camera."""
    fr, w0 = scene.camera.frame, config.frame_width
    rel = np.array([*pos, 0.0])
    word = txt("LAYER", 28, LIME)
    return always_redraw(lambda: VGroup(word.copy(), numtxt(f"{int(round(vt.get_value()))}", 28, LIME))
                         .arrange(RIGHT, buff=0.15).scale(fr.width / w0).move_to(fr.get_center() + rel * fr.width / w0))


class M15_CONTEXT_SHIFT(QScene):
    ASSET = "M15_CONTEXT_SHIFT"

    def construct(self):
        self.setup_q()
        pj = Proj(self, spin=0.03, k=1.0)
        cloud = pj.cloud(MAP_CORE, dim=0.3, lime_z=MAP_CORE_LIME)
        hm = pj.cloud(cluster_pts("MONEY"), r=0.1, color=LIME, opacity=0.3, dim=0.8)
        hr = pj.cloud(cluster_pts("RIVER"), r=0.1, color=PUMPKIN, opacity=0.45, dim=0.8)
        self.add(cloud, hm, hr)
        M, Rv = CLUSTERS["MONEY"], CLUSTERS["RIVER"]
        mlab = VGroup(*[pj.pin(label_dot(w, p, LIME, size=22), p) for w, p in MONEY_W])
        rlab = VGroup(*[pj.pin(label_dot(w, p, PUMPKIN, size=22), p) for w, p in RIVER_W])
        s1, s2 = ValueTracker(0), ValueTracker(0)          # money-bank and river-bank progress
        goal1 = M + np.array([-0.1, 0.0, 0.0])
        goal2 = Rv + np.array([0.1, 0.0, 0.0])
        b1p = lambda: BANK_MID + (goal1 - BANK_MID) * s1.get_value()
        b2p = lambda: BANK_MID + (goal2 - BANK_MID) * s2.get_value()
        wd = lambda ws: " ".join(ws)
        sent1 = VGroup(*[txt(w, 40, LIME if w == "bank" else OFFWHITE) for w in "the bank raised rates".split()]
                       ).arrange(RIGHT, buff=0.3).move_to(UP * 2.3)
        self.add(self.make_layer_trackers())
        # b1: the sentence above the map
        self.beat(LaggedStart(*[FadeIn(w, shift=DOWN * 0.2) for w in sent1], lag_ratio=0.18),
                  cloud.dim.animate.set_value(0.4), FadeIn(mlab, scale=0.6), FadeIn(rlab, scale=0.6), run=1.8)
        # b2: BANK starts from the same point every time
        bank = pj.pin(label_dot("BANK", BANK_MID, OFFWHITE, size=30), b1p)
        raised = pj.pin(label_dot("RAISED", M + np.array([0.7, 0.9, -0.2]), LIME, size=22), M + np.array([0.7, 0.9, -0.2]))
        self.beat(FadeIn(bank, scale=0.4), FadeIn(raised, scale=0.6), run=1.5)
        # b3: layer 1 and layer 2 nudge BANK using RAISED and RATES
        layer = self.layer
        ln = pinned_layer(self, layer)
        nudge = pj.link(b1p, M + np.array([-0.45, 0.45, 0.1]), LIME, 4, g=0.0, trim=0.25)
        nudge2 = pj.link(b1p, M + np.array([0.7, 0.9, -0.2]), LIME, 4, g=0.0, trim=0.25)
        self.add(nudge, nudge2)
        self.beat(FadeIn(ln), layer.animate.set_value(1),
                  Succession(AnimationGroup(nudge.g.animate.set_value(0.5), nudge2.g.animate.set_value(0.5), run_time=0.7),
                             AnimationGroup(s1.animate.set_value(0.35), run_time=0.8),
                             AnimationGroup(layer.animate.set_value(2), nudge.g.animate.set_value(0.8),
                                            nudge2.g.animate.set_value(0.8), run_time=0.5),
                             s1.animate(run_time=0.9).set_value(0.7)), run=3.2)
        # b4: BANK arrives inside the money cluster
        self.beat(s1.animate.set_value(1), nudge.o.animate.set_value(0), nudge2.o.animate.set_value(0),
                  bank[0][2].animate.set_color(LIME), sent1[1].animate.scale(1.2), run=2.4, focus=pj.P(goal1) * 0.35)
        # b5: "not near water": a second sentence sends a copy of BANK toward the river
        sent2 = VGroup(*[txt(w, 40, PUMPKIN if w == "bank" else OFFWHITE) for w in "we sat on the bank".split()]
                       ).arrange(RIGHT, buff=0.3).move_to(UP * 1.7)
        bank2 = pj.pin(label_dot("BANK", BANK_MID, PUMPKIN, size=30), b2p)
        self.beat(sent1.animate.shift(UP * 0.1).set_opacity(0.5), FadeIn(sent2, shift=DOWN * 0.2), FadeIn(bank2, scale=0.5),
                  s2.animate.set_value(0.55), run=2.0, focus=pj.P(BANK_MID) * 0.2)
        # b6: the copy keeps moving; 96 layers
        t96 = self.hud(txt("GPT-3: 96 LAYERS", 20, bold=False).set_opacity(0.8), corner=DR,
                       buff=np.array([0.8, 1.78, 0]))
        self.beat(s2.animate.set_value(1), FadeIn(t96), layer.animate(rate_func=linear).set_value(40), run=2.1)
        # b7: each layer adjusts every token a little: counter to 96, both banks shimmer
        self.beat(layer.animate(rate_func=linear).set_value(96),
                  Succession(s1.animate(run_time=1.0, rate_func=there_and_back).set_value(0.9),
                             s2.animate(run_time=1.0, rate_func=there_and_back).set_value(0.9)), run=2.9)
        self.finish()

    def make_layer_trackers(self):
        self.layer = ValueTracker(0)
        return self.layer
