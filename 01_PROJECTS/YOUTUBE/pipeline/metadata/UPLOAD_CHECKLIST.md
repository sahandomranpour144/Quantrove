# Quantrove Master Video Upload & Publishing Checklist

**Purpose**: Systematic pre-flight checklist for uploading and publishing YouTube episodes. Enforces zero-defect quality control across metadata, packaging, visual assets, and YouTube Studio configuration.  
**Authority**: Standing Channel Architecture  

---

## 1. Title Verification (Rule L1 / Standing Standard)
- [ ] **Word Count**: Exactly 6 to 7 words (Hard ceiling: max 8 words).
- [ ] **Character Count**: Strictly `< 60` characters (prevents truncation on mobile feeds).
- [ ] **Human Appeal**: Clear promise, curiosity-driven, avoids sterile textbook jargon.
- [ ] **Keyword Alignment**: First 5 seconds of spoken voiceover includes at least 2 primary title keywords.
- [ ] **Packaging Symmetry**: Title text directly complements (does not merely duplicate) thumbnail text.

---

## 2. Thumbnail Pre-Flight Check
- [ ] **Resolution**: Exactly `1280 x 720` px (16:9 aspect ratio, PNG format).
- [ ] **Palette Lock**: Strictly `#202322`, `#233D4C`, `#C3D809`, `#FD802E`, `#E6EDF3`. Zero generic red/green.
- [ ] **Text Quantity**: Maximum `1–3 words` total (e.g. `"$0 ISN'T FREE"`, `"1 LOSS"`).
- [ ] **Typography**: Nohemi Bold 700 (or Inter Bold).
- [ ] **Mobile Legibility Test**: Verified crisp and immediately legible when scaled down to a 1.5-inch mobile thumbnail preview.
- [ ] **Focal Clarity**: Single clear visual focal point (no cluttered collages).

---

## 3. Description Verification (6-Block Architecture)
- [ ] **Block 1 (Hook)**: First 150 characters state the title keywords and core click promise.
- [ ] **Block 2 (Synopsis)**: 2–3 sentences explaining what empirical data proves and why it matters.
- [ ] **Block 3 (Chapters)**: Chronological chapters starting with `00:00`; derived from actual `ffprobe` video timestamps; each chapter `>= 10s`.
- [ ] **Block 4 (Sources)**: Primary empirical sources, academic papers, and SEC filings explicitly cited.
- [ ] **Block 5 (Watch Next)**: Companion video title and working playlist link included.
- [ ] **Block 6 (Disclaimer & Tags)**: Educational disclaimer present; exactly 3 hashtags at the end (`#Quantrove #{PillarHashtag} #{TopicHashtag}`).

---

## 4. Tag String Assembly (3-Tier Rule)
- [ ] **Tier 3 (Episode)**: Primary topic phrase is placed as Tag #1.
- [ ] **Tier 2 (Pillar)**: Standard pillar tags included from `PLAYLIST_METADATA.md`.
- [ ] **Tier 1 (Core)**: 5 core Quantrove channel tags included.
- [ ] **Character Count**: Target `<= 300` characters total (strictly `< 500` characters).
- [ ] **No Keyword Stuffing**: Zero unrelated trending tags.

---

## 5. Master Video & Audio QC
- [ ] **Container & Video**: MP4 (H.264), 1920x1080 @ 60.00 fps constant.
- [ ] **Audio Loudness**: Integrated loudness normalized to `-14.0 ± 1.0 LUFS`, True Peak `<= -1.0 dBFS`.
- [ ] **Voice / Music Balance**: Music ducked `>= 16 dB` below dialogue during narration.
- [ ] **End Screen Clearance**: Final 20 seconds clear of focal graphics to accommodate YouTube subscribe and next-video cards.

---

## 6. YouTube Studio Configuration (Step-by-Step)
1. **Initial Upload**: Upload master MP4 as **Unlisted** at least 6–12 hours before public release.
2. **HD & 1080p Processing**: Verify YouTube finishes 1080p60 encoding and checks pass with zero copyright flags.
3. **Playlist Assignment**: Add video to its designated permanent pillar playlist.
4. **End Screen Cards**:
   - Add **Subscribe** element.
   - Add **Best for Viewer** or **Specific Video** pointing to the companion episode from the playlist.
   - Position cards within the final 20-second clear zone.
5. **Pinned Comment**: Draft and pin the primary discussion question and companion video link.
6. **Publish / Schedule**: Set public release time according to channel cadence schedule.
