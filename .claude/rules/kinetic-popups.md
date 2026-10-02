> **LONG-FORM ONLY. Shorts use the text system in shorts-style.md (no glow, no bounce pop-ups, no separate captions).**

# Rule: Kinetic Keyword Pop-Ups

## What the Rule Is
Every video requires kinetic pop-up keywords (typography, font weights, and contrast must adhere to [visual-style-standard.md](visual-style-standard.md)):
- **Long-form**: 60fps transparent RGBA MOV (`00_OVERLAY_..._kinetic_word_pops_60fps.mov`) on CapCut Track V2 with `ease_out_back` spring easing, glowing halos, and margin-safe layout.
- **Shorts**: Burned-in 3-4 word captions with Nohemi font, Off-White (`#E6EDF3`) text, Power Lime (`#C3D809`) emphasis, and Pumpkin (`#FD802E`) risk words per `shorts-style.md` (no separate pop-ups, zero yellow fill boxes).

## Bug / Incident Prevented
Without kinetic visual anchors, viewer drop-off spikes during voiceover transitions. Exporting without transparency (RGB instead of RGBA) renders solid black boxes that obscure the underlying Manim visuals.

## Verification Check
Probe the exported long-form overlay file for alpha channel and framerate before assembly:

```bash
# Confirm alpha channel (rgba/yuva420p) and 60fps
ffprobe -v error -select_streams v:0 -show_entries stream=pix_fmt,r_frame_rate -of csv=p=0 TIMELINE_MEDIA/*kinetic_word_pops*
```
Expected output: `yuva420p,60/1` (or equivalent alpha format).

Pop-up slots, pill fills (#222022 @ 80%), 1px #233D4C borders, and safe bands are governed by `pipeline/config/layout_contract.json`. Every video must pass layout_qa before GATE2_READY.
