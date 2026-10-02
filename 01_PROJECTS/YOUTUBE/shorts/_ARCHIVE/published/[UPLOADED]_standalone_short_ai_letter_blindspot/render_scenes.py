import os
import sys
import subprocess
from manim import *

# Configure Manim for 9:16 Vertical video (1080x1920 @ 60fps)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9.0
config.frame_height = 16.0
config.frame_rate = 60
config.background_color = "#0B0F19"  # Obsidian dark luxury

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.join(CURRENT_DIR, "TIMELINE_MEDIA")
os.makedirs(TIMELINE_DIR, exist_ok=True)

# Mandatory CleanText vector engine helper (CLAUDE.md §3.5)
def CleanText(text, font="Segoe UI", font_size=28, color="#FFFFFF", **kwargs):
    ref_size = 72
    scale_factor = font_size / ref_size
    return Text(text, font=font, font_size=ref_size, color=color, **kwargs).scale(scale_factor)

# Palette constants
COLOR_BG = "#0B0F19"
COLOR_CYAN = "#00F0FF"
COLOR_MINT = "#00FFA3"
COLOR_GOLD = "#FFD700"
COLOR_CRIMSON = "#FF3366"
COLOR_WHITE = "#FFFFFF"
COLOR_SLATE = "#8892B0"
COLOR_CARD_BG = "#121826"

# ==========================================
# SCENE 1: 0.00s -> 5.50s (Duration: 5.50s)
# ==========================================
class Scene01Hook(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Category pill
        pill_bg = RoundedRectangle(corner_radius=0.2, width=3.8, height=0.6, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_SLATE, stroke_width=1.5)
        pill_txt = CleanText("AI CAPABILITIES", font_size=20, color=COLOR_SLATE)
        pill = VGroup(pill_bg, pill_txt).move_to(UP * 5.6)

        # Card 1: Novel capability
        card1_bg = RoundedRectangle(corner_radius=0.3, width=7.4, height=2.6, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_MINT, stroke_width=2.5)
        card1_title = CleanText("WRITES ENTIRE NOVELS", font_size=32, color=COLOR_WHITE).move_to(card1_bg.get_center() + UP * 0.55)
        card1_sub = CleanText("Generated in two seconds flat ✓", font_size=22, color=COLOR_MINT).move_to(card1_bg.get_center() + DOWN * 0.25)

        # Progress indicator inside card 1
        bar_bg = RoundedRectangle(corner_radius=0.1, width=5.5, height=0.22, fill_color="#1E293B", fill_opacity=1.0, stroke_width=0).move_to(card1_bg.get_center() + DOWN * 0.8)
        bar_fill = RoundedRectangle(corner_radius=0.1, width=5.5, height=0.22, fill_color=COLOR_MINT, fill_opacity=1.0, stroke_width=0).move_to(bar_bg.get_center())
        card1 = VGroup(card1_bg, card1_title, card1_sub, bar_bg, bar_fill).move_to(UP * 3.2)

        # Card 2: Sudden failure barrier
        card2_bg = RoundedRectangle(corner_radius=0.3, width=7.4, height=2.8, fill_color="#1A1016", fill_opacity=0.95, stroke_color=COLOR_CRIMSON, stroke_width=3.0)
        card2_title = CleanText("CANNOT COUNT TO 3", font_size=34, color=COLOR_CRIMSON).move_to(card2_bg.get_center() + UP * 0.6)
        card2_sub = CleanText("The 'Strawberry' Test 🍓", font_size=26, color=COLOR_GOLD).move_to(card2_bg.get_center() + DOWN * 0.15)
        card2_badge = CleanText("CRITICAL REASONING FLAW ✗", font_size=20, color=COLOR_CRIMSON).move_to(card2_bg.get_center() + DOWN * 0.75)
        card2 = VGroup(card2_bg, card2_title, card2_sub, card2_badge).move_to(UP * 0.2)

        self.play(FadeIn(pill, shift=DOWN*0.3), FadeIn(card1, shift=UP*0.5), run_time=0.8)
        self.wait(1.4)
        self.play(FadeIn(card2, shift=UP*0.5), card2_bg.animate.set_stroke(color=COLOR_CRIMSON, width=4.0), run_time=0.8)
        self.wait(2.50)


# ==========================================
# SCENE 2: 5.50s -> 11.90s (Duration: 6.40s)
# ==========================================
class Scene02Guesses(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Header tag
        tag = CleanText("EXHIBIT A: THE WORD", font_size=22, color=COLOR_SLATE).move_to(UP * 5.6)

        # Word card with letter R highlighted
        word_bg = RoundedRectangle(corner_radius=0.3, width=7.8, height=1.6, fill_color=COLOR_CARD_BG, fill_opacity=0.95, stroke_color=COLOR_CYAN, stroke_width=2.0).move_to(UP * 4.2)

        # Build colored letters: S T R A W B E R R Y
        letters_text = [
            ("S", COLOR_WHITE), ("T", COLOR_WHITE), ("R", COLOR_GOLD),
            ("A", COLOR_WHITE), ("W", COLOR_WHITE), ("B", COLOR_WHITE),
            ("E", COLOR_WHITE), ("R", COLOR_GOLD), ("R", COLOR_GOLD), ("Y", COLOR_WHITE)
        ]
        letter_mobs = [CleanText(ch, font_size=38, color=c) for ch, c in letters_text]
        letters_group = VGroup(*letter_mobs).arrange(RIGHT, buff=0.25).move_to(word_bg.get_center())
        word_card = VGroup(word_bg, letters_group)

        # User question card
        prompt_bg = RoundedRectangle(corner_radius=0.2, width=7.4, height=1.1, fill_color="#1E293B", fill_opacity=0.9, stroke_color=COLOR_SLATE, stroke_width=1.5).move_to(UP * 2.5)
        prompt_txt = CleanText("User: How many 'R's in strawberry?", font_size=23, color=COLOR_WHITE).move_to(prompt_bg.get_center())
        prompt_card = VGroup(prompt_bg, prompt_txt)

        # Response 1: 2 R's
        resp1_bg = RoundedRectangle(corner_radius=0.2, width=7.4, height=1.1, fill_color="#201117", fill_opacity=0.95, stroke_color=COLOR_CRIMSON, stroke_width=2.5).move_to(UP * 1.1)
        resp1_txt = CleanText("AI: There are 2 'r's.  ✗", font_size=25, color=COLOR_CRIMSON).move_to(resp1_bg.get_center())
        resp1 = VGroup(resp1_bg, resp1_txt)

        # Response 2: 4 R's
        resp2_bg = RoundedRectangle(corner_radius=0.2, width=7.4, height=1.1, fill_color="#201117", fill_opacity=0.95, stroke_color=COLOR_CRIMSON, stroke_width=2.5).move_to(DOWN * 0.3)
        resp2_txt = CleanText("AI: There are 4 'r's.  ✗", font_size=25, color=COLOR_CRIMSON).move_to(resp2_bg.get_center())
        resp2 = VGroup(resp2_bg, resp2_txt)

        # Key takeaway footer (moved to bottom safe margin: DOWN 4.6)
        takeaway_bg = RoundedRectangle(corner_radius=0.25, width=7.8, height=1.4, fill_color=COLOR_CARD_BG, fill_opacity=0.95, stroke_color=COLOR_CYAN, stroke_width=2.0).move_to(DOWN * 4.6)
        takeaway_txt = CleanText("IT LITERALLY CANNOT", font_size=25, color=COLOR_CYAN).move_to(takeaway_bg.get_center() + UP * 0.3)
        takeaway_sub = CleanText("SEE THE INDIVIDUAL LETTERS", font_size=21, color=COLOR_WHITE).move_to(takeaway_bg.get_center() + DOWN * 0.3)
        takeaway = VGroup(takeaway_bg, takeaway_txt, takeaway_sub)

        self.play(FadeIn(tag), FadeIn(word_card, shift=DOWN*0.3), FadeIn(prompt_card, shift=UP*0.2), run_time=0.8)
        self.wait(1.0)
        self.play(FadeIn(resp1, shift=UP*0.2), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(resp2, shift=UP*0.2), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(takeaway, shift=UP*0.3), run_time=0.7)
        self.wait(1.10)


# ==========================================
# SCENE 3: 11.90s -> 22.30s (Duration: 10.40s)
# ==========================================
class Scene03Tokens(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        tag = CleanText("THE REALITY: TOKENIZATION", font_size=22, color=COLOR_SLATE).move_to(UP * 5.6)

        # Unified word
        full_word_bg = RoundedRectangle(corner_radius=0.3, width=7.4, height=1.6, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_WHITE, stroke_width=2.0).move_to(UP * 3.8)
        full_word_txt = CleanText("S T R A W B E R R Y", font_size=36, color=COLOR_WHITE).move_to(full_word_bg.get_center())
        full_word = VGroup(full_word_bg, full_word_txt)

        # Token 1: straw
        tok1_bg = RoundedRectangle(corner_radius=0.3, width=3.4, height=2.0, fill_color="#0F243A", fill_opacity=0.95, stroke_color=COLOR_CYAN, stroke_width=3.0)
        tok1_txt = CleanText("straw", font_size=36, color=COLOR_CYAN).move_to(tok1_bg.get_center() + UP * 0.3)
        tok1_id = CleanText("Token ID: 496", font_size=20, color=COLOR_GOLD).move_to(tok1_bg.get_center() + DOWN * 0.4)
        tok1 = VGroup(tok1_bg, tok1_txt, tok1_id).move_to(LEFT * 1.9 + UP * 2.0)

        # Token 2: berry
        tok2_bg = RoundedRectangle(corner_radius=0.3, width=3.4, height=2.0, fill_color="#0D2E26", fill_opacity=0.95, stroke_color=COLOR_MINT, stroke_width=3.0)
        tok2_txt = CleanText("berry", font_size=36, color=COLOR_MINT).move_to(tok2_bg.get_center() + UP * 0.3)
        tok2_id = CleanText("Token ID: 675", font_size=20, color=COLOR_GOLD).move_to(tok2_bg.get_center() + DOWN * 0.4)
        tok2 = VGroup(tok2_bg, tok2_txt, tok2_id).move_to(RIGHT * 1.9 + UP * 2.0)

        tokens = VGroup(tok1, tok2)

        # Explanatory comparison banner (moved to UP 0.0, leaving lower third clear)
        banner_bg = RoundedRectangle(corner_radius=0.3, width=7.8, height=2.4, fill_color=COLOR_CARD_BG, fill_opacity=0.95, stroke_color=COLOR_GOLD, stroke_width=2.5).move_to(UP * 0.1)
        line1 = CleanText("NOT 10 INDIVIDUAL LETTERS", font_size=24, color=COLOR_CRIMSON).move_to(banner_bg.get_center() + UP * 0.6)
        line2 = CleanText("2 DISCRETE VECTOR CHUNKS", font_size=30, color=COLOR_MINT).move_to(banner_bg.get_center())
        line3 = CleanText("Seen together millions of times", font_size=20, color=COLOR_SLATE).move_to(banner_bg.get_center() + DOWN * 0.6)
        banner = VGroup(banner_bg, line1, line2, line3)

        self.play(FadeIn(tag), FadeIn(full_word, shift=DOWN*0.3), run_time=0.8)
        self.wait(1.2)
        # Transform full word into two split tokens
        self.play(FadeOut(full_word), FadeIn(tokens, shift=UP*0.3), run_time=1.2)
        self.wait(1.5)
        self.play(FadeIn(banner, shift=UP*0.4), run_time=1.0)
        self.wait(4.70)


# ==========================================
# SCENE 4: 22.30s -> 30.60s (Duration: 8.30s)
# ==========================================
class Scene04BlackBox(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        tag = CleanText("THE INFERENCE PROCESS", font_size=22, color=COLOR_SLATE).move_to(UP * 5.6)

        # Transformer Neural Network Box (moved to UP 3.2)
        box_bg = RoundedRectangle(corner_radius=0.3, width=7.4, height=2.8, fill_color="#0D1117", fill_opacity=0.98, stroke_color=COLOR_CYAN, stroke_width=2.5).move_to(UP * 3.4)
        box_title = CleanText("TRANSFORMER BLACK BOX", font_size=25, color=COLOR_CYAN).move_to(box_bg.get_center() + UP * 0.9)

        # Neural nodes diagram inside
        nodes = VGroup(*[Circle(radius=0.14, fill_color=COLOR_MINT, fill_opacity=0.8, stroke_color=COLOR_WHITE, stroke_width=1.0) for _ in range(6)]).arrange(RIGHT, buff=0.8).move_to(box_bg.get_center())
        box_lbl = CleanText("Zero letters inside — Matrix Weights Only", font_size=19, color=COLOR_SLATE).move_to(box_bg.get_center() + DOWN * 0.8)
        box = VGroup(box_bg, box_title, nodes, box_lbl)

        # Probability outputs (moved to UP 0.7)
        prob_bg = RoundedRectangle(corner_radius=0.3, width=7.4, height=2.3, fill_color=COLOR_CARD_BG, fill_opacity=0.95, stroke_color=COLOR_GOLD, stroke_width=2.0).move_to(UP * 0.6)
        prob_title = CleanText("NEXT-TOKEN PROBABILITY:", font_size=23, color=COLOR_GOLD).move_to(prob_bg.get_center() + UP * 0.6)

        # Simulated probabilities
        p1 = CleanText("P(\"2\") = 48.2%  (Learned Pattern)", font_size=21, color=COLOR_WHITE).move_to(prob_bg.get_center() + UP * 0.05)
        p2 = CleanText("P(\"3\") = 39.1%  (True Count)", font_size=21, color=COLOR_MINT).move_to(prob_bg.get_center() + DOWN * 0.45)
        prob_card = VGroup(prob_bg, prob_title, p1, p2)

        # Metaphor stamp (moved to DOWN 4.6)
        metaphor = CleanText("GUESSING, NOT COUNTING", font_size=30, color=COLOR_CRIMSON).move_to(DOWN * 4.6)

        self.play(FadeIn(tag), FadeIn(box, shift=DOWN*0.3), run_time=0.8)
        self.wait(1.2)
        self.play(FadeIn(prob_card, shift=UP*0.3), run_time=0.9)
        self.wait(1.5)
        self.play(FadeIn(metaphor, scale=1.1), run_time=0.8)
        self.wait(3.10)


# ==========================================
# SCENE 5: 30.60s -> 39.00s (Duration: 8.40s)
# ==========================================
class Scene05Blindspot(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        tag = CleanText("THE CORE DISCONNECT", font_size=22, color=COLOR_SLATE).move_to(UP * 5.6)

        # Human view card (moved to UP 3.6)
        c1_bg = RoundedRectangle(corner_radius=0.25, width=7.6, height=2.0, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_MINT, stroke_width=2.0).move_to(UP * 3.6)
        c1_title = CleanText("WHAT YOU SEE (Letters)", font_size=22, color=COLOR_MINT).move_to(c1_bg.get_center() + UP * 0.45)
        c1_val = CleanText("s · t · r · a · w · b · e · r · r · y", font_size=28, color=COLOR_WHITE).move_to(c1_bg.get_center() + DOWN * 0.25)
        c1 = VGroup(c1_bg, c1_title, c1_val)

        # AI view card (moved to UP 1.3)
        c2_bg = RoundedRectangle(corner_radius=0.25, width=7.6, height=2.0, fill_color=COLOR_CARD_BG, fill_opacity=0.9, stroke_color=COLOR_CYAN, stroke_width=2.0).move_to(UP * 1.3)
        c2_title = CleanText("WHAT THE AI SEES (Tokens)", font_size=22, color=COLOR_CYAN).move_to(c2_bg.get_center() + UP * 0.45)
        c2_val = CleanText("[ 496 ]    [ 675 ]", font_size=32, color=COLOR_GOLD).move_to(c2_bg.get_center() + DOWN * 0.25)
        c2 = VGroup(c2_bg, c2_title, c2_val)

        # Explains half of mistakes (moved to DOWN 0.7)
        foot_bg = RoundedRectangle(corner_radius=0.25, width=7.6, height=1.7, fill_color="#181324", fill_opacity=0.95, stroke_color=COLOR_GOLD, stroke_width=2.5).move_to(DOWN * 0.7)
        foot_txt = CleanText("THE TOKENIZER BLIND SPOT", font_size=27, color=COLOR_GOLD).move_to(foot_bg.get_center() + UP * 0.3)
        foot_sub = CleanText("Spelling · Rhyming · Math Drift", font_size=21, color=COLOR_WHITE).move_to(foot_bg.get_center() + DOWN * 0.3)
        foot = VGroup(foot_bg, foot_txt, foot_sub)

        self.play(FadeIn(tag), FadeIn(c1, shift=DOWN*0.3), run_time=0.8)
        self.wait(1.0)
        self.play(FadeIn(c2, shift=UP*0.3), run_time=0.8)
        self.wait(1.2)
        self.play(FadeIn(foot, shift=UP*0.3), run_time=0.8)
        self.wait(3.80)


# ==========================================
# SCENE 6: 39.00s -> 43.12s (Duration: 4.12s)
# ==========================================
class Scene06CTA(Scene):
    def construct(self):
        self.camera.background_color = COLOR_BG

        # Outro call to action (centered at UP 1.2)
        card_bg = RoundedRectangle(corner_radius=0.35, width=7.8, height=5.2, fill_color=COLOR_CARD_BG, fill_opacity=0.98, stroke_color=COLOR_CYAN, stroke_width=3.0).move_to(UP * 1.2)
        q_txt = CleanText("WHICH AI MISTAKE", font_size=34, color=COLOR_WHITE).move_to(card_bg.get_center() + UP * 1.6)
        q_sub = CleanText("SHOULD WE EXPLAIN NEXT?", font_size=29, color=COLOR_CYAN).move_to(card_bg.get_center() + UP * 0.9)

        divider = Line(LEFT * 3.0, RIGHT * 3.0, stroke_color=COLOR_SLATE, stroke_width=1.5).move_to(card_bg.get_center() + UP * 0.2)

        brand = CleanText("QUANTROVE", font_size=38, color=COLOR_GOLD).move_to(card_bg.get_center() + DOWN * 0.6)
        brand_sub = CleanText("Real Engineering Behind AI", font_size=22, color=COLOR_MINT).move_to(card_bg.get_center() + DOWN * 1.3)
        comment_cta = CleanText("Drop your prompt below 👇", font_size=20, color=COLOR_SLATE).move_to(card_bg.get_center() + DOWN * 1.9)

        cta = VGroup(card_bg, q_txt, q_sub, divider, brand, brand_sub, comment_cta)

        self.play(FadeIn(cta, scale=0.95), run_time=0.8)
        self.wait(3.32)

if __name__ == "__main__":
    scenes = [
        ("Scene01Hook", "01_00m00s_to_00m06s_hook_novel_vs_count.mp4"),
        ("Scene02Guesses", "02_00m06s_to_00m12s_strawberry_guesses.mp4"),
        ("Scene03Tokens", "03_00m12s_to_00m22s_token_blocks_split.mp4"),
        ("Scene04BlackBox", "04_00m22s_to_00m31s_transformer_blackbox_seeds.mp4"),
        ("Scene05Blindspot", "05_00m31s_to_00m39s_tokenizer_blindspot_comparison.mp4"),
        ("Scene06CTA", "06_00m39s_to_00m43s_cta_which_mistake_next.mp4")
    ]

    for class_name, out_filename in scenes:
        print(f"\n🎬 Rendering {class_name} -> {out_filename}...")
        out_path = os.path.join(TIMELINE_DIR, out_filename)
        cmd = [
            "manim",
            "-qh",
            "--media_dir", os.path.join(CURRENT_DIR, "manim_build"),
            __file__,
            class_name
        ]
        subprocess.run(cmd, check=True)

        # Locate generated file
        gen_file = os.path.join(CURRENT_DIR, "manim_build", "videos", "render_scenes", "1920p60", f"{class_name}.mp4")
        if not os.path.exists(gen_file):
            # Fallback path if directory name varies
            for root, dirs, files in os.walk(os.path.join(CURRENT_DIR, "manim_build")):
                if f"{class_name}.mp4" in files:
                    gen_file = os.path.join(root, f"{class_name}.mp4")
                    break

        # Move to TIMELINE_MEDIA with canonical name
        if os.path.exists(out_path):
            os.remove(out_path)
        os.rename(gen_file, out_path)
        print(f"✅ Saved to: {out_path}")
