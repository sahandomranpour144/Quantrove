from manim import *
import numpy as np

config.background_color = "#121212"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class PatternRevealScene(Scene):
    def construct(self):
        # Target total duration: Exactly 57.0 seconds

        PURPLE = "#8B5CF6"
        RED = "#EF4444"
        GOLD = "#F59E0B"
        CYAN = "#06B6D4"
        GREEN = "#10B981"
        WHITE = "#FFFFFF"
        MUTED = "#94A3B8"
        PANEL_BG = "#1A1F2C"

        # ---------------------------------------------------------
        # 1. Title & Header (0.0s - 4.0s) -> 4.0s
        # ---------------------------------------------------------
        title = Text("THE ANATOMY OF A CRASH", font_size=38, font="Segoe UI", weight=BOLD, color=PURPLE)
        subtitle = Text("THE ONE UNIVERSAL PATTERN BEHIND EVERY CRISIS", font_size=20, font="Segoe UI", color=MUTED)
        header_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.5)

        self.play(FadeIn(header_group, shift=DOWN), run_time=1.0)
        self.wait(3.0)

        # ---------------------------------------------------------
        # 2. The Crowded Theater Metaphor (4.0s - 13.0s) -> 9.0s
        # ---------------------------------------------------------
        theater_title = Text("The Theater Metaphor: The Rush Causes The Destruction", font_size=22, font="Segoe UI", weight=BOLD, color=GOLD).shift(UP * 1.8)

        room = RoundedRectangle(corner_radius=0.15, height=4.0, width=6.5, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=MUTED, stroke_width=2.5).shift(DOWN * 0.4 + LEFT * 1.0)
        door = Rectangle(height=1.2, width=0.3, fill_color=GREEN, fill_opacity=1.0, stroke_color=WHITE, stroke_width=1.5).next_to(room, RIGHT, buff=-0.3).shift(UP * 0.0)
        door_lbl = Text("EXIT / LIQUIDITY", font_size=13, font="Segoe UI", weight=BOLD, color=GREEN).next_to(door, RIGHT, buff=0.2)

        # Particle dots inside room
        np.random.seed(42)
        dots = []
        for _ in range(30):
            rx = np.random.uniform(-3.5, 1.2)
            ry = np.random.uniform(-2.0, 1.2)
            d = Dot(point=[rx, ry, 0], color=GREEN, radius=0.09)
            dots.append(d)
        dot_group = VGroup(*dots)

        fire_badge = RoundedRectangle(corner_radius=0.15, height=0.7, width=3.8, fill_color=RED, fill_opacity=1.0, stroke_color=WHITE, stroke_width=2).shift(UP * 1.0 + LEFT * 1.0)
        fire_text = Text("SHOUT OF 'FIRE!'", font_size=16, font="Segoe UI", weight=BOLD, color=WHITE).move_to(fire_badge.get_center())

        self.play(
            FadeIn(theater_title),
            Create(room), Create(door), FadeIn(door_lbl),
            FadeIn(dot_group, lag_ratio=0.05),
            run_time=2.2
        )
        self.wait(1.0)

        # Surge to exit and turn red
        target_pt = door.get_left()
        surge_anims = [d.animate.move_to(target_pt + np.random.normal(0, 0.35, 3) * np.array([0.6, 0.6, 0])).set_color(RED) for d in dots]
        door_alert = door.animate.set_fill(RED)

        self.play(
            FadeIn(fire_badge, shift=UP), FadeIn(fire_text, shift=UP),
            door_alert,
            *surge_anims,
            run_time=2.0
        )
        self.wait(3.0)

        # ---------------------------------------------------------
        # 3. Order Book Liquidity Evaporation (13.0s - 21.0s) -> 8.0s
        # ---------------------------------------------------------
        self.play(
            FadeOut(theater_title), FadeOut(room), FadeOut(door), FadeOut(door_lbl),
            FadeOut(dot_group), FadeOut(fire_badge), FadeOut(fire_text),
            run_time=0.8
        )

        ob_title = Text("Exchange Order Book: Liquidity Evaporation Cascade", font_size=22, font="Segoe UI", weight=BOLD, color=CYAN).shift(UP * 1.8)

        # Bid side (Green, small/drained)
        bids = [
            Rectangle(width=0.6, height=0.4, fill_color=GREEN, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5).shift(LEFT * 1.5 + DOWN * 0.6),
            Rectangle(width=0.4, height=0.4, fill_color=GREEN, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5).shift(LEFT * 1.5 + DOWN * 1.1),
            Rectangle(width=0.2, height=0.4, fill_color=GREEN, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5).shift(LEFT * 1.5 + DOWN * 1.6),
        ]
        lbl_bid_title = Text("Buy Bids (Drained)", font_size=15, font="Segoe UI", weight=BOLD, color=GREEN).next_to(bids[0], UP, buff=0.3)

        # Ask side (Red, huge sell wall)
        asks = [
            Rectangle(width=3.2, height=0.4, fill_color=RED, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5).shift(RIGHT * 1.8 + UP * 0.6),
            Rectangle(width=4.5, height=0.4, fill_color=RED, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5).shift(RIGHT * 2.45 + UP * 1.1),
            Rectangle(width=5.8, height=0.4, fill_color=RED, fill_opacity=0.85, stroke_color=WHITE, stroke_width=0.5).shift(RIGHT * 3.1 + UP * 1.6),
        ]
        lbl_ask_title = Text("Sell Wall (Flooded)", font_size=15, font="Segoe UI", weight=BOLD, color=RED).next_to(asks[0], DOWN, buff=0.3)

        ob_vgroup = VGroup(*bids, lbl_bid_title, *asks, lbl_ask_title)

        drop_arrow = Arrow(start=UP * 0.8 + LEFT * 0.2, end=DOWN * 1.8 + LEFT * 0.2, color=RED, stroke_width=5)
        drop_lbl = Text("Price Drops\nVertically", font_size=13, font="Segoe UI", weight=BOLD, color=RED).next_to(drop_arrow, LEFT, buff=0.15)

        self.play(
            FadeIn(ob_title),
            FadeIn(ob_vgroup, lag_ratio=0.15),
            Create(drop_arrow), FadeIn(drop_lbl),
            run_time=2.2
        )
        self.wait(5.0)

        # ---------------------------------------------------------
        # 4. Master Comparison Matrix (21.0s - 32.0s) -> 11.0s
        # ---------------------------------------------------------
        self.play(
            FadeOut(ob_title), FadeOut(ob_vgroup), FadeOut(drop_arrow), FadeOut(drop_lbl),
            run_time=0.8
        )

        matrix_title = Text("Master Comparison: 1929 vs 2008 vs 2020", font_size=22, font="Segoe UI", weight=BOLD, color=WHITE).shift(UP * 1.8)

        # 3 Comparison Cards
        c1929 = RoundedRectangle(corner_radius=0.15, height=3.6, width=3.6, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=GOLD, stroke_width=2.5).shift(LEFT * 4.0 + DOWN * 0.4)
        t1929 = VGroup(
            Text("1929 CRASH", font_size=16, font="Segoe UI", weight=BOLD, color=GOLD),
            Line(start=LEFT*1.2, end=RIGHT*1.2, color=MUTED, stroke_width=1),
            Text("• Trigger: 10:1 Margin Debt\n• Drop: -89.2% in Dow\n• Speed: 34 Months\n• Recovery: ~25 Years", font_size=12, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.15).move_to(c1929.get_center())

        c2008 = RoundedRectangle(corner_radius=0.15, height=3.6, width=3.6, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=CYAN, stroke_width=2.5).shift(DOWN * 0.4)
        t2008 = VGroup(
            Text("2008 CRISIS", font_size=16, font="Segoe UI", weight=BOLD, color=CYAN),
            Line(start=LEFT*1.2, end=RIGHT*1.2, color=MUTED, stroke_width=1),
            Text("• Trigger: Subprime CDOs\n• Drop: -56.8% in S&P\n• Speed: 17 Months\n• Recovery: ~5.5 Years", font_size=12, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.15).move_to(c2008.get_center())

        c2020 = RoundedRectangle(corner_radius=0.15, height=3.6, width=3.6, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=RED, stroke_width=2.5).shift(RIGHT * 4.0 + DOWN * 0.4)
        t2020 = VGroup(
            Text("2020 PANDEMIC", font_size=16, font="Segoe UI", weight=BOLD, color=RED),
            Line(start=LEFT*1.2, end=RIGHT*1.2, color=MUTED, stroke_width=1),
            Text("• Trigger: COVID Lockdowns\n• Drop: -33.9% in S&P\n• Speed: 22 Trading Days\n• Recovery: ~5 Months", font_size=12, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.15).move_to(c2020.get_center())

        matrix_group = VGroup(c1929, t1929, c2008, t2008, c2020, t2020)

        self.play(
            FadeIn(matrix_title),
            FadeIn(matrix_group, lag_ratio=0.2),
            run_time=2.2
        )
        self.wait(8.0)

        # ---------------------------------------------------------
        # 5. The 4-Stage Universal Mechanism Pipeline (32.0s - 43.0s) -> 11.0s
        # ---------------------------------------------------------
        self.play(
            FadeOut(matrix_title), FadeOut(matrix_group),
            run_time=0.8
        )

        mech_title = Text("The 4-Stage Universal Crash Mechanism", font_size=22, font="Segoe UI", weight=BOLD, color=PURPLE).shift(UP * 1.8)

        m_stages = [
            ("1. CATALYST TRIGGER\n(Debt / CDO / Virus)", RED),
            ("2. CONFIDENCE BREAK\n(Perception Shatters)", GOLD),
            ("3. LIQUIDITY STAMPEDE\n(Everyone Hits Exit)", CYAN),
            ("4. SYSTEMIC CRASH\n(Forced Liquidations)", PURPLE)
        ]
        m_boxes = []
        for i, (m_txt, m_col) in enumerate(m_stages):
            mb = RoundedRectangle(corner_radius=0.15, height=1.6, width=2.4, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=m_col, stroke_width=2.5)
            mt = Text(m_txt, font_size=12, font="Segoe UI", weight=BOLD, color=WHITE).move_to(mb.get_center())
            m_boxes.append(VGroup(mb, mt))

        m_pipe = VGroup(*m_boxes).arrange(RIGHT, buff=0.4).shift(DOWN * 0.2)
        m_arrows = []
        for i in range(len(m_boxes) - 1):
            mar = Arrow(start=m_boxes[i].get_right(), end=m_boxes[i+1].get_left(), color=GOLD, buff=0.1, stroke_width=3)
            m_arrows.append(mar)
        m_arrow_group = VGroup(*m_arrows)

        self.play(
            FadeIn(mech_title),
            FadeIn(m_pipe, lag_ratio=0.2),
            Create(m_arrow_group, lag_ratio=0.2),
            run_time=2.2
        )
        self.wait(8.0)

        # ---------------------------------------------------------
        # 6. Big Takeaway Banner (43.0s - 50.0s) -> 7.0s
        # ---------------------------------------------------------
        self.play(
            FadeOut(mech_title), FadeOut(m_pipe), FadeOut(m_arrow_group),
            run_time=0.8
        )

        big_banner = RoundedRectangle(corner_radius=0.2, height=1.8, width=10.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=RED, stroke_width=3.5).shift(UP * 0.5)
        big_text = VGroup(
            Text("THE TRIGGER CHANGES. THE PANIC DOESN'T.", font_size=24, font="Segoe UI", weight=BOLD, color=RED),
            Text("Crashes don't have one cause — they have one universal pattern.", font_size=16, font="Segoe UI", color=WHITE)
        ).arrange(DOWN, buff=0.2).move_to(big_banner.get_center())

        quote_box = Text("Next time you hear 'the market crashed because of panic' —\nnow you understand the structural mechanism behind the exit bottleneck.", font_size=15, font="Segoe UI", color=MUTED, line_spacing=1.3).next_to(big_banner, DOWN, buff=0.5)

        self.play(
            FadeIn(big_banner, scale=0.95), FadeIn(big_text),
            FadeIn(quote_box),
            run_time=1.2
        )
        self.wait(5.0)

        # ---------------------------------------------------------
        # 7. Next Episode Teaser & Subscribe (50.0s - 57.0s) -> 7.0s
        # ---------------------------------------------------------
        self.play(
            FadeOut(big_banner), FadeOut(big_text), FadeOut(quote_box), FadeOut(header_group),
            run_time=0.8
        )

        teaser_card = RoundedRectangle(corner_radius=0.25, height=4.2, width=9.5, fill_color=PANEL_BG, fill_opacity=0.95, stroke_color=PURPLE, stroke_width=3)
        teaser_content = VGroup(
            Text("NEXT EPISODE: THE AFTERMATH", font_size=26, font="Segoe UI", weight=BOLD, color=PURPLE),
            Text("What Happens to Jobs, Wages & GDP in the 5 Years After a Crash?", font_size=17, font="Segoe UI", weight=BOLD, color=WHITE),
            Line(start=LEFT * 3.5, end=RIGHT * 3.5, color=MUTED, stroke_width=1),
            Text("• 50 Years of Macroeconomic Recovery Data Analyzed\n• The Real Impact on Everyday People & Wealth Creation\n• Subscribe to Follow The Entire Series", font_size=15, font="Segoe UI", color=WHITE, line_spacing=1.3)
        ).arrange(DOWN, buff=0.2).move_to(teaser_card.get_center())

        self.play(FadeIn(teaser_card, scale=0.95), FadeIn(teaser_content), run_time=1.2)
        # Pad remaining time to hit exactly 57.0s
        self.wait(5.8)
