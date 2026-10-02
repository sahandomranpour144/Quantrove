"""
EP03 Manim Master Render Runner
Renders all 9 scenes at 1080p 60fps with native MarkupText kerning.
Copies final renders directly to TIMELINE_MEDIA with exact manifest filenames.
Run: python render_all_ep03.py
"""
import subprocess, sys, os, shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

TIMELINE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA"))
RENDERS_DIR = os.path.join(BASE_DIR, "renders")
os.makedirs(RENDERS_DIR, exist_ok=True)

SCENES = [
    ("scene01_scale_of_uploads.py",        "ScaleOfUploadsScene",        ["01_00m18s_to_00m36s_Scene_01_ScaleOfUploads_manim.mp4", "01_00m18s_Scene_01_ScaleOfUploads_manim.mp4"]),
    ("scene02_two_tower_vector_space.py",   "TwoTowerVectorSpaceScene",   ["02_00m42s_to_00m57s_Scene_02_TwoTowerVectorSpace_manim.mp4", "02_00m42s_Scene_02_TwoTowerVectorSpace_manim.mp4", "02_00m45s_Scene_02_TwoTowerVectorSpace_manim.mp4"]),
    ("scene03_three_stage_funnel.py",       "ThreeStageFunnelScene",       ["03_01m22s_to_01m34s_Scene_03_ThreeStageFunnel_manim.mp4", "03_01m22s_Scene_03_ThreeStageFunnel_manim.mp4"]),
    ("scene03_neural_scoring_matrix.py",    "NeuralScoringMatrixScene",    ["03_01m47s_to_02m03s_Scene_03_NeuralScoringMatrix_manim.mp4"]),
    ("scene04_variable_reward_curve.py",    "VariableRewardCurveScene",    ["04_02m29s_to_02m48s_Scene_04_VariableRewardCurve_manim.mp4"]),
    ("scene05_transformer_attention.py",    "TransformerAttentionScene",    ["05_02m48s_to_02m59s_Scene_05_TransformerAttention_manim.mp4"]),
    ("scene05_divergent_metrics.py",        "DivergentMetricsScene",        ["05_03m08s_to_03m32s_Scene_05_DivergentMetrics_manim.mp4"]),
    ("scene06_echo_chamber_diversity.py",   "EchoChamberDiversityScene",   ["06_03m51s_to_04m06s_Scene_06_EchoChamberDiversity_manim.mp4"]),
    ("scene07_algorithm_summary_rules.py",  "AlgorithmSummaryRulesScene",  ["07_04m20s_to_04m46s_Scene_07_AlgorithmSummaryRules_manim.mp4"]),
]

for i, (script, cls, media_names) in enumerate(SCENES, 1):
    out_name = f"{cls}.mp4"
    out_path = os.path.join(RENDERS_DIR, out_name)
    print(f"\n[{i}/{len(SCENES)}] Rendering {cls} from {script}...")
    
    cmd = [
        sys.executable, "-m", "manim", "-qh", "--fps", "60",
        "--media_dir", os.path.join(BASE_DIR, "media"),
        "-o", out_name,
        script, cls
    ]
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print(f"  ERROR rendering {cls}!")
        sys.exit(1)
        
    # Find generated file in media/videos/
    src_video = None
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, "media", "videos")):
        if out_name in files:
            src_video = os.path.join(root, out_name)
            break
            
    if src_video and os.path.exists(src_video):
        shutil.copy2(src_video, out_path)
        print(f"  Copied to renders/{out_name}")
        for mname in media_names:
            dst = os.path.join(TIMELINE_DIR, mname)
            shutil.copy2(src_video, dst)
            print(f"  Updated TIMELINE_MEDIA/{mname}")
    else:
        print(f"  Warning: generated video {out_name} not found in media tree!")

print("\n=== All 9 scenes rendered and synchronized successfully ===")
