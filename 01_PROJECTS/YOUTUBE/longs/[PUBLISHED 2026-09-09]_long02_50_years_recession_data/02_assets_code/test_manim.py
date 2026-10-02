from manim import *

config.background_color = "#0B0E14"
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60

class TestScene(Scene):
    def construct(self):
        title = Text("MANIM ENGINE TEST", font_size=40, color="#06B6D4")
        self.play(FadeIn(title), run_time=1.0)
        self.wait(1.0)
