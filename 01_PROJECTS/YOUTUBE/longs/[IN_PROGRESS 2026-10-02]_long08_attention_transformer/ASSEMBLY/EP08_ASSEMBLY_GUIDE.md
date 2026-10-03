# EP08 — CapCut Assembly & Finishing Guide
*The 2017 Paper That Built ChatGPT* · master 661.80 s (11:02) · Gate 2 approved 2026-10-03
Clip list with exact in-points: `CAPCUT_IMPORT_ORDER.md`. All media: `../TIMELINE_MEDIA/`.

## 1. Project setup
1. New project, **1920×1080, 60 fps**. Canvas color `#202322`.
2. Import everything in `TIMELINE_MEDIA/`, plus the VO `../VOICEOVER/ElevenLabs_2026-10-03T06_29_48__s35_v4.mp3` and `assets/audio/BGM.mp3` (workspace root).
3. **V1**: place the 46 `EP08_SCnn_*.mp4` clips in filename order, back to back from 00:00. Each clip is frame-exact, so they line up with the VO with no trimming. Check: the last clip (S46 end screen) ends at **11:01.80**.
4. **V2**: put `00_OVERLAY_EP08_kinetic_word_pops_60fps.mov` at 00:00, blend Normal, opacity 100%. It has alpha, so you should see the clips underneath.
5. **A1**: VO at 00:00. **A2**: music (section 4).
6. Sync spot-checks (scrub and listen):
   - 00:00–00:05 "JUNE 2017" is on screen as you say "In June 2017"
   - 02:29.7 the paper card shows ATTENTION IS ALL YOU NEED as you say "Attention is all you need"
   - 04:23.2 the eight heads are visible on "heads"
   - 10:41.8 the end screen starts as the VO ends

## 2. Transitions (hard cuts everywhere except these)
| At | Between | Transition |
|---|---|---|
| 00:00.00 | head | Fade in from black 0.50 s (visual), 0.05 s (audio) |
| 00:28.28 | S2 → S3 (Ch1) | Cross-dissolve 0.30 s |
| 02:19.76 | S11 → S12 (Ch2) | Cross-dissolve 0.30 s |
| 04:18.06 | S20 → S21 (Ch3) | Cross-dissolve 0.30 s |
| 05:58.74 | S27 → S28 (Ch4) | Cross-dissolve 0.30 s |
| 07:45.26 | S33 → S34 (Ch5) | Cross-dissolve 0.30 s |
| 08:56.88 | S38 → S39 (Answer) | Cross-dissolve 0.30 s |
| 10:41.80 | S45 → S46 (end screen) | Dip to black 0.20 s |
| 11:01.30 → 11:01.80 | tail | Fade to black 0.50 s, video + music |

Centre each dissolve on the cut. Don't shift clip positions; the cuts are anchored to words in the VO.

## 3. Color: zero grade
Every clip is final. Manim, Remotion and HyperFrames render exact brand hex values. The three Flow clips (S3 interpreter booth, S12 night office, S27 data-center dawn) were already conformed to the canvas at ingest. **Apply no LUT, filter, sharpening or global adjustment.** If CapCut offers "auto color" or "enhance", leave it off.

## 4. Audio
| Track | Source | Target |
|---|---|---|
| A1 Voice | ElevenLabs VO | Normalize to **−14 LUFS** integrated, true peak ≤ −1 dBFS. High-pass at 80 Hz. Light compression (2:1, 2–3 dB max). |
| A2 Music | `assets/audio/BGM.mp3` (2:55) | Loop 4× to cover 11:02 (back-to-back copies, 1–2 s crossfade at each join). Keep it **≥ 16 dB under the voice** while the VO plays (≈ −30 dBFS), using CapCut's auto-ducking or keyframes. |
| End screen | music only | From 10:41.80, raise the music +10 dB over 1 s, then fade it out with the video at 11:01.30–11:01.80. |

**Music license (CC BY-ND 3.0)**: you may loop it, set its volume, duck it and fade it. You may not cut it into a new arrangement, pitch-shift it or time-stretch it. The credit block is already in `METADATA/EP08_METADATA.md`.

Optional SFX (−18 to −22 dBFS, no whooshes or risers):
- a soft tick on each count-up landing in S1 (citations), S15 (144) and S34 (n²)
- a soft click as each attention head lights up in S21 and S22

Skip these if you're short on time; the visuals already carry the rhythm.

## 5. Pre-export checklist
**Visual**
- [ ] No black frame between any two V1 clips (46 clips, head to tail).
- [ ] V2 overlay visible and transparent from 00:00 to 10:41; nothing during the end screen.
- [ ] The S46 end screen (10:41.80–11:01.80) has no text, so the YouTube elements are clear.
- [ ] The HyperFrames clips (S7 Winograd, S37 token meter) hold their last frame; neither loops or flashes black.
**Audio**
- [ ] Voice sits at about −14 LUFS; the music never masks words (check S3, S12 and S27, the Flow scenes, where the music is most exposed).
- [ ] No clipping; the music fades to silence at the end.
**Export**
- [ ] 1080p, **60 fps**, H.264, high bitrate (≥ 16 Mbps, or CapCut "Higher"), AAC 320 kbps.
- [ ] Exported length = **11:02** (±1 frame).
- [ ] Save as `EP08 - The 2017 Paper That Built ChatGPT.mp4` in this episode folder (outside TIMELINE_MEDIA).

## 6. Upload
Everything to paste is in `METADATA/EP08_METADATA.md`:
- title, description (chapters, sources, music credit), tags, hashtags and pinned comment
- end screen + card setup
- thumbnails A + B (Test & Compare)

Playlist: **AI & Machine Learning Explained**, placed after EP07. Publish **after EP07**, and put EP07's URL into the description's WATCH NEXT line first.
