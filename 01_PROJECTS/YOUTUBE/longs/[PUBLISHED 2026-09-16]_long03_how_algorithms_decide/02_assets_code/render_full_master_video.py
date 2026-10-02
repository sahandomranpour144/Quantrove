"""
Master Full Episode 03 Video Renderer
Assembles all 20 timeline video assets + master voiceover + 60fps kinetic pop overlay
into the final 05:18.60 continuous master video.
"""
import os, sys, subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIMELINE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "TIMELINE_MEDIA"))

# Master Audio & Overlay
master_audio = os.path.join(TIMELINE_DIR, "00_AUDIO_00m00s_to_05m19s_full_voiceover_ep03_orus.mp3")
master_overlay = os.path.join(TIMELINE_DIR, "00_OVERLAY_00m00s_to_05m19s_kinetic_word_pops_60fps.mov")
out_master = os.path.join(TIMELINE_DIR, "MASTER_EP03_FULL_WITH_KINETIC_POPS.mp4")

# Scene 1 clips
s1_c1 = os.path.join(TIMELINE_DIR, "01_00m00s_to_00m10s_Scene_01_flow_infinite_feed_vortex.mp4")
s1_c2 = os.path.join(TIMELINE_DIR, "01_00m10s_to_00m18s_Scene_01_flow_billions_scrolling_darkness.mp4")
s1_c3 = os.path.join(TIMELINE_DIR, "01_00m18s_to_00m36s_Scene_01_ScaleOfUploads_manim.mp4")
s1_c4 = os.path.join(TIMELINE_DIR, "01_00m36s_to_00m42s_Scene_01_flow_glass_touchpoint.mp4")

# Scene 2 clips
s2_c1 = os.path.join(TIMELINE_DIR, "02_00m42s_to_00m57s_Scene_02_TwoTowerVectorSpace_manim.mp4")
s2_c2 = os.path.join(TIMELINE_DIR, "02_01m05s_to_01m13s_Scene_02_flow_two_viewers_different_feeds.mp4")

# Scene 3 clips
s3_c1 = os.path.join(TIMELINE_DIR, "03_01m22s_to_01m34s_Scene_03_ThreeStageFunnel_manim.mp4")
s3_c2 = os.path.join(TIMELINE_DIR, "03_01m34s_to_01m47s_Scene_03_flow_holographic_sorting_prism.mp4")
s3_c3 = os.path.join(TIMELINE_DIR, "03_01m47s_to_02m03s_Scene_03_NeuralScoringMatrix_manim.mp4")

# Scene 4 clips
s4_c1 = os.path.join(TIMELINE_DIR, "04_02m02s_to_02m13s_Scene_04_flow_dopamine_trance.mp4")
s4_c2 = os.path.join(TIMELINE_DIR, "04_02m13s_to_02m21s_Scene_04_flow_clickbait_history_trap.mp4")
s4_c3 = os.path.join(TIMELINE_DIR, "04_02m21s_to_02m29s_Scene_04_flow_bf_skinner_behavioral_box.mp4")
s4_c4 = os.path.join(TIMELINE_DIR, "04_02m29s_to_02m48s_Scene_04_VariableRewardCurve_manim.mp4")

# Scene 5 clips
s5_c1 = os.path.join(TIMELINE_DIR, "05_02m48s_to_02m59s_Scene_05_TransformerAttention_manim.mp4")
s5_c2 = os.path.join(TIMELINE_DIR, "05_03m08s_to_03m32s_Scene_05_DivergentMetrics_manim.mp4")

# Scene 6 clips
s6_c1 = os.path.join(TIMELINE_DIR, "06_03m32s_to_03m43s_Scene_06_gemini_infinite_hallway_echoes.jpg")
s6_c2 = os.path.join(TIMELINE_DIR, "06_03m43s_to_03m51s_Scene_06_flow_filter_bubble_isolated_mind.mp4")
s6_c3 = os.path.join(TIMELINE_DIR, "06_03m51s_to_04m06s_Scene_06_EchoChamberDiversity_manim.mp4")
s6_c4 = os.path.join(TIMELINE_DIR, "06_04m06s_to_04m20s_Scene_06_gemini_deliberate_agency_control.jpg")

# Scene 7 clips
s7_c1 = os.path.join(TIMELINE_DIR, "07_04m20s_to_04m46s_Scene_07_AlgorithmSummaryRules_manim.mp4")
s7_c2 = os.path.join(TIMELINE_DIR, "07_04m46s_to_04m56s_Scene_07_flow_quantum_bridge_ep04_teaser.mp4")
s7_c3 = os.path.join(TIMELINE_DIR, "07_04m56s_to_05m19s_Scene_07_flow_ep04_ai_stock_market_bridge.mp4")

inputs = [
    s1_c1, s1_c2, s1_c3, s1_c4,       # 0, 1, 2, 3
    s2_c1, s2_c2,                     # 4, 5
    s3_c1, s3_c2, s3_c3,               # 6, 7, 8
    s4_c1, s4_c2, s4_c3, s4_c4,       # 9, 10, 11, 12
    s5_c1, s5_c2,                     # 13, 14
    s6_c1, s6_c2, s6_c3, s6_c4,       # 15, 16, 17, 18
    s7_c1, s7_c2, s7_c3,               # 19, 20, 21
    master_overlay, master_audio      # 22, 23
]

filter_script = (
    # Scene 1 (0:00.00 - 0:42.04) -> 42.040s
    "[0:v]trim=0:10.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v0];"
    "[1:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v1];"
    "[2:v]trim=0:18.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v2];"
    "[3:v]trim=0:6.040,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v3];"
    
    # Scene 2 (0:42.04 - 1:22.32) -> 40.280s
    "[4:v]trim=0:14.700,tpad=stop_mode=clone:stop_duration=8.500,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v4];"
    "[5:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v5];"
    "[4:v]trim=14.65:14.70,tpad=stop_mode=clone:stop_duration=9.030,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v5_hold];"
    
    # Scene 3 (1:22.32 - 2:02.72) -> 40.400s
    "[6:v]trim=0:11.700,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v6];"
    "[7:v]trim=0:10.000,tpad=stop_mode=clone:stop_duration=3.460,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v7];"
    "[8:v]trim=0:10.400,tpad=stop_mode=clone:stop_duration=4.840,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v8];"
    
    # Scene 4 (2:02.72 - 2:47.76) -> 45.040s
    "[9:v]trim=0:10.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v9];"
    "[10:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v10];"
    "[11:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v11];"
    "[12:v]trim=0:12.000,tpad=stop_mode=clone:stop_duration=7.040,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v12];"
    
    # Scene 5 (2:47.76 - 3:32.24) -> 44.480s
    "[13:v]trim=0:11.400,tpad=stop_mode=clone:stop_duration=8.820,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v13];"
    "[14:v]trim=0:11.600,tpad=stop_mode=clone:stop_duration=12.660,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v14];"
    
    # Scene 6 (3:32.24 - 4:20.40) -> 48.160s
    "[15:v]loop=loop=624:size=1:start=0,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:10.400,setpts=PTS-STARTPTS[v15];"
    "[16:v]trim=0:8.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v16];"
    "[17:v]trim=0:15.800,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v17];"
    "[18:v]loop=loop=838:size=1:start=0,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:13.960,setpts=PTS-STARTPTS[v18];"
    
    # Scene 7 (4:20.40 - 5:18.60) -> 58.200s
    "[19:v]trim=0:10.500,tpad=stop_mode=clone:stop_duration=15.040,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v19];"
    "[20:v]trim=0:10.000,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v20];"
    "[21:v]trim=0:8.000,tpad=stop_mode=clone:stop_duration=14.660,setpts=PTS-STARTPTS,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60[v21];"
    
    # Concat all 22 video segments (Total: 318.600s)
    "[v0][v1][v2][v3][v4][v5][v5_hold][v6][v7][v8][v9][v10][v11][v12][v13][v14][v15][v16][v17][v18][v19][v20][v21]concat=n=23:v=1:a=0[vbase];"
    
    # Overlay kinetic pop layer (input 22)
    "[22:v]scale=1920:1080,setsar=1,fps=60[vover];"
    "[vbase][vover]overlay=0:0:format=auto[vfinal]"
)

cmd = ["ffmpeg", "-y"]
for inp in inputs:
    cmd.extend(["-i", inp])

cmd.extend([
    "-filter_complex", filter_script,
    "-map", "[vfinal]",
    "-map", f"{len(inputs)-1}:a",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    "-t", "318.600",
    out_master
])

def render_master():
    print(f"\n========================================================")
    print(f"Rendering Full Episode 03 Master Composite (05:18.60)...")
    print(f"========================================================")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg error:\n", res.stderr[-2000:])
        sys.exit(1)
    print(f"\n✓ Master video rendered successfully to:\n  {out_master}")

if __name__ == "__main__":
    render_master()
