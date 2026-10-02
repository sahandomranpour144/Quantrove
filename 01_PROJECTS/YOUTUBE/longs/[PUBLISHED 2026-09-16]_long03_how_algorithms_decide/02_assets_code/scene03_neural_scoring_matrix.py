from manim import *
import numpy as np

config.background_color = "#0B0E14"
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 60

class NeuralScoringMatrixScene(Scene):
    def construct(self):
        CYAN, GOLD, WHITE = "#06B6D4", "#F59E0B", "#FFFFFF"
        MUTED, PANEL_BG   = "#94A3B8", "#151B26"
        GREEN, RED        = "#10B981", "#EF4444"
        COOL_BLUE, AMBER_DARK = "#0369A1", "#D97706"

        # 1. Header (0.0 - 1.5s)
        title = Text(
            "STAGE 2: DEEP NEURAL RANKING & SCORING",
            font="Segoe UI", weight=BOLD, font_size=32, color=CYAN
        ).to_edge(UP, buff=0.4)
        subtitle = Text(
            "Scoring 1,000 Candidates Across Multi-Task Neural Objectives",
            font="Segoe UI", font_size=15, color=MUTED
        ).next_to(title, DOWN, buff=0.15)
        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(subtitle), run_time=1.0)
        self.wait(0.5)

        # 2. Table Column Headers
        col_widths = [2.8, 2.5, 2.3, 2.3, 2.6]
        col_names = ["CANDIDATE", "P(WATCH TIME)", "P(RELEVANCE)", "FRESHNESS", "TOTAL SCORE"]
        xs = [-4.6, -1.9, 0.5, 2.8, 5.2]
        header_y = 1.8

        header_group = VGroup()
        for name, x in zip(col_names, xs):
            col_color = GOLD if name == "TOTAL SCORE" else CYAN
            col_txt = Text(name, font="Segoe UI", weight=BOLD,
                          font_size=13, color=col_color).move_to([x, header_y, 0])
            header_group.add(col_txt)

        divider = Line(start=[-6.2, header_y - 0.35, 0], end=[6.6, header_y - 0.35, 0], color=MUTED, stroke_width=1.5, stroke_opacity=0.4)
        self.play(FadeIn(header_group), Create(divider), run_time=0.8)

        # 3. Rows Definition
        rows_data = [
            {
                "id": "Video #402",
                "cells": [("0.94", RED), ("0.89", GOLD), ("0.78", CYAN), ("0.912", GOLD)],
                "selected": True
            },
            {
                "id": "Video #189",
                "cells": [("0.65", CYAN), ("0.72", CYAN), ("0.88", GOLD), ("0.715", CYAN)],
                "selected": False
            },
            {
                "id": "Video #731",
                "cells": [("0.41", COOL_BLUE), ("0.81", CYAN), ("0.34", COOL_BLUE), ("0.528", COOL_BLUE)],
                "selected": False
            },
            {
                "id": "Video #094",
                "cells": [("0.22", COOL_BLUE), ("0.38", COOL_BLUE), ("0.92", GOLD), ("0.406", COOL_BLUE)],
                "selected": False
            },
        ]

        row_y_starts = [0.8, -0.05, -0.9, -1.75]
        row_groups = []
        top_row_box = None

        for r_idx, rdata in enumerate(rows_data):
            ry = row_y_starts[r_idx]
            r_group = VGroup()

            # Row container box
            row_bg = RoundedRectangle(
                corner_radius=0.12, width=13.0, height=0.72,
                fill_color=PANEL_BG, fill_opacity=0.9,
                stroke_color=MUTED if not rdata["selected"] else CYAN,
                stroke_width=1.0 if not rdata["selected"] else 1.5,
                stroke_opacity=0.5
            ).move_to([0.2, ry, 0])
            r_group.add(row_bg)
            if r_idx == 0:
                top_row_box = row_bg

            # Candidate label
            cand_lbl = Text(rdata["id"], font="Segoe UI", weight=BOLD,
                           font_size=16, color=WHITE).move_to([xs[0], ry, 0])
            r_group.add(cand_lbl)

            # Cells
            for c_idx, (val, col) in enumerate(rdata["cells"]):
                cx = xs[c_idx + 1]
                # Heatmap cell background
                cell_box = RoundedRectangle(
                    corner_radius=0.08, width=col_widths[c_idx + 1] - 0.4, height=0.52,
                    fill_color=col, fill_opacity=0.25 if not rdata["selected"] else 0.4,
                    stroke_color=col, stroke_width=1.5
                ).move_to([cx, ry, 0])
                val_txt = Text(val, font="Segoe UI", weight=BOLD,
                              font_size=15, color=col).move_to([cx, ry, 0])
                r_group.add(cell_box, val_txt)

            row_groups.append(r_group)

        # Animate rows appearing row-by-row
        for rg in row_groups:
            self.play(FadeIn(rg, shift=DOWN * 0.15), run_time=0.6)
            self.wait(0.2)

        self.wait(0.5)

        # 4. Highlight Selected Top Row (Video #402)
        highlight_box = RoundedRectangle(
            corner_radius=0.15, width=13.2, height=0.82,
            stroke_color=GREEN, stroke_width=3.5,
            fill_color=GREEN, fill_opacity=0.1
        ).move_to(top_row_box.get_center())

        selected_badge = RoundedRectangle(
            corner_radius=0.1, width=3.4, height=0.45,
            fill_color=GREEN, fill_opacity=1.0, stroke_width=0
        ).next_to(top_row_box, RIGHT, buff=-3.6).shift(UP * 0.55)
        badge_txt = Text("RANK #1: SELECTED FOR FEED", font="Segoe UI",
                        weight=BOLD, font_size=11, color="#0B0E14"
                        ).move_to(selected_badge)

        self.play(
            Create(highlight_box),
            FadeIn(selected_badge),
            FadeIn(badge_txt),
            run_time=0.9
        )
        self.wait(0.5)

        # 5. Bottom Takeaway Callout (8.5 - 10.4s)
        callout = Text(
            "Not ranked by objective quality -- scored solely on predicted watch duration for THIS user.",
            font="Segoe UI", weight=BOLD, font_size=16, color=GOLD
        ).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(callout, shift=UP * 0.2), run_time=0.8)
        self.wait(2.2)
