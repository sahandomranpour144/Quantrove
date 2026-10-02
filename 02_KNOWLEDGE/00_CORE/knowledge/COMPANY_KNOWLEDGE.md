# COMPANY KNOWLEDGE BASE

Version:
1.0

Purpose:
Store reusable knowledge that improves future projects.

---

# Company Principles

- Sahand is the CEO and final decision maker.
- High aesthetic quality and viewer retention are non-negotiable standards.
- Always provide structured, evidence-based recommendations.

---

# Successful Strategies

- **Kinetic Keyword Pop-Up Overlays (Track V2)**: Rendering a synchronized 60fps QuickTime RLE transparent MOV (`00_OVERLAY_...mov`) with elastic spring-pop easing (`ease_out_back`) and glowing colored ambient halos dramatically elevates production value and viewer retention without cluttering edit timelines.
- **Institutional Data Intelligence Aesthetic for Finance & AI**: Raisin Black background (`#202322`), Charcoal Slate chrome/dividers (`#233D4C`), Power Lime (`#C3D809`), Pumpkin (`#FD802E`), and Off-White (`#E6EDF3`) typography create a statistical, high-rigor Bloomberg-terminal aesthetic.
- **Centralized Timeline Media**: Storing all generated assets (Flow clips, Manim renders, voiceover stems, overlays) in a unified `TIMELINE_MEDIA/` folder with chronological timestamp prefixes eliminates missing assets and editing confusion.

---

# Failed Strategies

- **Raw Low-Point Manim Text with Bold Weight**: Manim's default Pango text rasterizer snaps character glyphs to discrete pixel advances when rendered at small point sizes with `weight=BOLD`, resulting in broken, scattered words (e.g. `m ar ket` instead of `market`).
  - *Fix*: Always use `CleanText` vector scaling (`ref_size=72`, scaled down) with Segoe UI or Arial.

---

# Technical Knowledge

- **Manim CleanText Vector Scaling Helper**:
  ```python
  def CleanText(text, font_size=28, color="#FFFFFF", font="Segoe UI", **kwargs):
      ref_size = 72
      scale = font_size / ref_size
      t = Text(text, font_size=ref_size, font=font, color=color, **kwargs)
      t.scale(scale)
      return t
  ```
- **Transparent 60fps Kinetic Text Overlay Pipeline**:
  - Pre-render high-DPI cards with Pillow (`RGBA` + GaussianBlur shadow + colored glow).
  - Stream raw RGBA frames directly into FFmpeg: `ffmpeg -y -f rawvideo -pix_fmt rgba -s 1920x1080 -r 60 -i - -c:v qtrle output.mov`.
  - Import directly into CapCut on Track V2 above base visuals (Track V1).

---

# Market Knowledge

(Useful market insights)

---

# Lessons Learned

- Cold YouTube Browse audiences drop off quickly during static narration; kinetic keyword pops and micro-animations provide continuous visual dopamine that extends Average View Duration (AVD).

---

END OF KNOWLEDGE BASE