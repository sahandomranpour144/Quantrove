# EP07 — CapCut Assembly & Finishing Guide
*How AI Turns Every Word Into Geometry* · master 687.64 s (11:28) · Gate 2 approved 2026-10-03
Clip list with exact in-points: `CAPCUT_IMPORT_ORDER.md`. All media: `../TIMELINE_MEDIA/`.

## 1. Project setup
1. New project, **1920×1080, 60 fps**. Canvas color `#202322`.
2. Import everything in `TIMELINE_MEDIA/` plus the VO `../VOICEOVER/ElevenLabs_2026-10-03T06_01_28__s60_v4.mp3` and `assets/audio/BGM.mp3` (workspace root).
3. **V1**: drop the 47 `EP07_SCnn_*.mp4` clips in filename order, back to back from 00:00. Each clip is frame-exact, so they meet the VO with no trimming. Check: the last clip (S47 end screen) ends at **11:27.64**.
4. **V2**: `00_OVERLAY_EP07_kinetic_word_pops_60fps.mov` at 00:00, blend Normal, opacity 100%. It has alpha, so you should see the clips underneath.
5. **A1**: VO at 00:00. **A2**: music (section 4).
6. Sync spot-checks (scrub, listen):
   - 00:15.4 the arrow lands on QUEEN as you say "queen"
   - 04:44.3 KING appears on "Start at king"
   - 11:07 the end screen starts as the VO ends

## 2. Transitions (hard cuts everywhere except these)
| At | Between | Transition |
|---|---|---|
| 00:00.00 | head | Fade in from black 0.50 s (visual), 0.05 s (audio) |
| 00:32.08 | S2 → S3 (Ch1) | Cross-dissolve 0.30 s |
| 02:09.06 | S10 → S11 (Ch2) | Cross-dissolve 0.30 s |
| 04:44.32 | S22 → S23 (Ch3) | Cross-dissolve 0.30 s |
| 06:58.10 | S30 → S31 (Ch4) | Cross-dissolve 0.30 s |
| 09:38.70 | S40 → S41 (Answer) | Cross-dissolve 0.30 s |
| 11:07.64 | S46 → S47 (end screen) | Dip to black 0.20 s |
| 11:27.14 → 11:27.64 | tail | Fade to black 0.50 s, video + music |

Centre each dissolve on the cut. Do not shift clip positions; the cuts are word-anchored.

## 3. Color: zero grade
Every clip is final. Manim, Remotion and HyperFrames render exact brand hex values. The Flow clips were already graded to the canvas at ingest, including the warm printing press at S27, which stays warm (CEO call). **Apply no LUT, filter, sharpening or global adjustment.** If CapCut offers "auto color" or "enhance", leave it off.

## 4. Audio
| Track | Source | Target |
|---|---|---|
| A1 Voice | ElevenLabs VO | Normalize to **−14 LUFS** integrated, true peak ≤ −1 dBFS. High-pass at 80 Hz. Light compression (2:1, 2–3 dB max). |
| A2 Music | `assets/audio/BGM.mp3` (2:55) | Loop 4× to cover 11:28 (back-to-back copies, 1–2 s crossfade at each join). **≥ 16 dB under the voice** while it speaks (≈ −30 dBFS); use CapCut's auto-ducking or keyframes. |
| End screen | music only | From 11:07.64, raise music +10 dB over 1 s, then fade out with the video at 11:27.14–11:27.64. |

**Music license (CC BY-ND 3.0)**: you may loop, set volume, duck and fade. Do not cut it into a new arrangement, pitch-shift or time-stretch it. The credit block is already in `METADATA/EP07_METADATA.md`.

Optional SFX (−18 to −22 dBFS, no whooshes or risers): a soft tick on each arrow move in S1, S23 and S24; a soft click on the counters in S17 and S33. Skip these if you're short on time; the visuals already carry the rhythm.

## 5. Pre-export checklist
**Visual**
- [ ] No black frame between any two V1 clips (47 clips, head to tail).
- [ ] V2 overlay visible and transparent from 00:00 to 11:07; nothing in the end screen.
- [ ] The S47 end screen (11:07.64–11:27.64) has no text or graphics, so the YouTube cards are clear.
- [ ] The HyperFrames clips (S7, S12, S31, S40) hold their last frame; none loop or flash black.
**Audio**
- [ ] Voice sits at about −14 LUFS; music never masks words (check S5, S27 and S38 especially).
- [ ] No clipping; music fades to silence at the end.
**Export**
- [ ] 1080p, **60 fps**, H.264, high bitrate (≥ 16 Mbps, or CapCut "Higher"), AAC 320 kbps.
- [ ] Exported length = **11:28** (±1 frame).
- [ ] Save as `EP07 - How AI Turns Every Word Into Geometry.mp4` in this episode folder (outside TIMELINE_MEDIA).

## 6. Upload
Everything to paste is in `METADATA/EP07_METADATA.md`:
- title, description (chapters, sources, music credit), tags, hashtags and pinned comment
- end screen setup
- thumbnail `METADATA/EP07_THUMBNAIL.png`

Playlist: **AI & Machine Learning Explained**. Publish **before EP08**.
