from ep08_common import *


class T_COMMON(QScene):
    ASSET = "T_COMMON"

    def construct(self):
        self.setup_q()
        s = Sentence().move_to(UP * 1.6)
        f = Formula().move_to(DOWN * 0.6)
        self.add(s, f, all_arcs(s).set_opacity(0.3), illustrative(self))
        print("SENT W", s.width, "FORM W", f.width)
        self.beat(s.mark(TROPHY), s.mark(IT, PUMPKIN), f.qk.animate.set_color(LIME), run=0.5)
