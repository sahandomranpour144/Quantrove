# CapCut Assembly & Verification Checklist — EP06

**Episode Title**: The Machines Trading Before You Blink  
**Target Video Duration**: `07:20.91` (440.91s)  
**Media Source Folder**: `01_PROJECTS/YOUTUBE/longs/[IN_PROGRESS 2026-09-30]_long06_hft_microsecond_pricing/TIMELINE_MEDIA/`  
**Finishing Guide**: Refer to [`ASSEMBLY/POST_ASSEMBLY_FINISHING_GUIDE.md`](POST_ASSEMBLY_FINISHING_GUIDE.md) for scene transitions, color grade, fade timings, and effects policy.  

---

## Phase 1: Project Setup & Import
- [ ] **Canvas Profile**: 1920x1080 (16:9), Framerate: 60.00 fps constant.
- [ ] **Track A1 (Master Narration)**:
  - [ ] Import `EP06_VO_FINAL.mp3`.
  - [ ] Place at timeline start `00:00:00.00`.
  - [ ] Confirm audio ends at `07:00.91` (spoken ends at `07:00.46`).
  - [ ] Lock Track A1.
- [ ] **Track V1 (Visual Media)**:
  - [ ] Import all 25 clips `EP06_SC01_DATA_HALL.mp4` through `EP06_SC25_END_SCREEN_BG.mp4`.
  - [ ] Snap clips head-to-tail matching `ASSEMBLY/CAPCUT_IMPORT_ORDER.md` and transition table in `POST_ASSEMBLY_FINISHING_GUIDE.md`.
  - [ ] Apply 0.25s–0.30s soft dissolves at major chapter bridges (S06→S07, S10→S11, S16→S17, S23→S24) per finishing guide.
  - [ ] Confirm Flow clips (S01, S07, S11, S17, S24) hold final frames or J-cut into next scene.
  - [ ] Confirm html_motion clips (S03, S06, S14, S19) hold final readout frames cleanly to match voiceover.
  - [ ] Confirm Scene 25 end screen starts at `07:00.91` and ends at `07:20.91`.
- [ ] **Track V2 (Kinetic Overlay)**:
  - [ ] Import `00_OVERLAY_EP06_kinetic_word_pops_60fps.mov`.
  - [ ] Place at `00:00:00.00`.
  - [ ] Set Blending mode to `Normal` (verify alpha transparency renders clean, zero black background).
  - [ ] Verify pop-up cards display within safe band `y = 56..176` and do not obstruct charts.

---

## Phase 2: Audio Mixing & Sound Design (per Finishing Guide §6)
- [ ] **Dialogue (Track A1)**:
  - [ ] Normalize to `-14.0 ± 1.0 LUFS` integrated loudness.
  - [ ] Ensure vocal clarity with high-pass filter at 80 Hz.
- [ ] **Sound FX (Track A2)**:
  - [ ] Place soft click / tick sounds on order fills (S03, S06, S14, S20).
  - [ ] Place subtle danger / alert pulse on Knight Capital loss (S22).
  - [ ] Keep peak SFX levels between `-18 and -22 dBFS`.
- [ ] **Music Bed (Track A3)**:
  - [ ] Minimalist electronic / ambient documentary track without vocals.
  - [ ] Ducking: Set volume between `-28 and -32 dBFS` during narration (`>= 16 dB` below dialogue).
  - [ ] Swell: Fade up to `-18 dBFS` starting at `07:00.46` as narration concludes.
  - [ ] Outro Fade: 0.5s audio fade to black ending at `07:20.41`.

---

## Phase 3: Visual & Safe Area Quality Control (per Finishing Guide §3 & §5)
- [ ] **Palette Consistency & Color Grade**:
  - [ ] Manim & HTML motion clips left at 0% grade (untouched mathematical RGB).
  - [ ] Flow clips matched: shadows aligned with Raisin Black (`#202322`), desaturated -5% to -10% if warm hues bleed.
  - [ ] Zero unapproved effects (no whip pans, no particles, no stylized LUTs).
  - [ ] Opening fade-in: 0.50s from black at head. Outro fade-out: 0.50s to black at tail.
  - [ ] Primary accents are Power Lime (`#C3D809`), risk accents Pumpkin (`#FD802E`), text Off-White (`#E6EDF3`).
  - [ ] Zero generic red/green.
  - [ ] Risk/Anomalies are Pumpkin (`#FD802E`).
  - [ ] Text is Off-White (`#E6EDF3`).
  - [ ] Zero generic red/green.
- [ ] **Typography**:
  - [ ] Clean sans-serif rendering.
  - [ ] Zero `.notdef` white square boxes.
  - [ ] Formulas in S13 and S15 render Greek characters cleanly.
- [ ] **Safe Zone Verification**:
  - [ ] Lower caption zone (`y = 864..1080`) is clear of visual focal elements.
  - [ ] Scene 25 end screen (`07:00.91` to `07:20.91`) contains zero text or graphics competing with YouTube cards.

---

## Phase 4: Master Export Verification
- [ ] Format: MP4 (H.264 / AAC).
- [ ] Resolution: 1920x1080.
- [ ] Framerate: 60.00 fps constant.
- [ ] Total File Duration: exactly `07:20` to `07:21` (440.91s).
- [ ] Final video ready for upload.
