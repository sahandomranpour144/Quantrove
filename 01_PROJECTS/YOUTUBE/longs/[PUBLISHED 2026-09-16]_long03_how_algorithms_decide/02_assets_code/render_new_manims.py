import subprocess, sys, os

DIR = r"e:\AI_COMPANY\01_PROJECTS\YOUTUBE\longs\[IN_PROGRESS] long03_how_algorithms_decide\02_assets_code"
os.chdir(DIR)

scenes = [
    ("scene03_neural_scoring_matrix.py", "NeuralScoringMatrixScene"),
    ("scene05_divergent_metrics.py", "DivergentMetricsScene"),
]

for script, cls in scenes:
    print(f"\nRendering {cls} from {script}...")
    cmd = [
        sys.executable, "-m", "manim", "-qh", "--fps", "60",
        "-o", f"{cls}.mp4", script, cls
    ]
    res = subprocess.run(cmd)
    print(f"Result for {cls}: {res.returncode}")

print("\nRender script completed.")
