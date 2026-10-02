# CapCut Final Assembly & Editing Polish Guide
**Episode**: EP05 — *Why "Free" Trading Isn't Free*  
**Format**: Long-Form 16:9 (1920x1080 @ 60fps)  
**Measured Master Runtime**: **05m 37s** (337.12s)  
**Track Hierarchy**:
- **Track V3**: Adjustment Layer / Color Grade
- **Track V2**: 60fps Transparent RGBA Kinetic Keyword Overlay (`00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov`)
- **Track V1**: Master Visual Timeline (`TIMELINE_MEDIA/` Manim scenes + 3 Google Flow B-roll clips)
- **Track A1**: Master Voiceover (`00_00m00s_to_05m37s_ep05_master_voiceover.wav`, -14 LUFS)
- **Track A2**: Background Music Bed (Minimalist Tech Ambient, -30 dB, ducking to -34 dB under voice)
- **Track A3**: Sound Effects (SFX) Track

---

## 1. Master Clip Assembly Table (Track V1 & V2)

All timeline media files are stored in `TIMELINE_MEDIA/` with standardized chronological prefixes per Rule 3.8.

| Scene | Clip Filename in `TIMELINE_MEDIA/` | Exact Time Window (ffprobe) | Visual Content / Flow Inserts | Transition to Next Clip |
|---|---|---|---|---|
| **01** | `01_00m00s_to_00m20s_hook_buy_button_shatter.mp4` | 00:00.00 – 00:20.00 (20.00s) | Smartphone tap, button shatters to encrypted hex stream | **Hard Cut** (0.00s) |
| **02** | `02_00m20s_to_00m38s_pace_statement_progress_bar.mp4` | 00:20.00 – 00:38.24 (18.24s) | 3-part illuminated dossier progress bar + countdown clock | **Hard Cut** (0.00s) |
| **03** | `03_00m38s_to_01m03s_illusion_ticket_to_zero_loupe.mp4` | 00:38.24 – 01:03.40 (25.16s) | 1999 $19.95 ticket dissolves to $0.00, Pumpkin loupe zoom | **Cross-Dissolve** (0.20s `Dissolve`) |
| **04a** | `04_01m03s_to_01m07s_flow_hft_server_rack_corridor.mp4` | 01:03.40 – 01:07.00 (3.60s) | **Google Flow Clip 01**: High-tech data center server corridor | **Cross-Dissolve** (0.20s `Dissolve`) |
| **04b** | `04_01m07s_to_01m36s_order_routing_citadel_virtu.mp4` | 01:07.00 – 01:36.84 (29.84s) | Exchange switch-gate flips shut; Citadel/Virtu nodes activate | **Hard Cut** (0.00s) |
| **05** | `05_01m36s_to_02m11s_bid_ask_spread_order_book.mp4` | 01:36.84 – 02:11.80 (34.96s) | Currency booth analogy morphs to L2 book; 100x volume ramp | **Hard Cut** (0.00s) |
| **06** | `06_02m11s_to_02m47s_pfof_kickback_revenue_chart.mp4` | 02:11.80 – 02:47.04 (35.24s) | Dual pipeline PFOF kickback; Robinhood $200M/qtr revenue bar | **Cross-Dissolve** (0.20s `Dissolve`) |
| **07a** | `07_02m47s_to_02m50s_flow_institutional_trading_floor.mp4` | 02:47.04 – 02:50.50 (3.46s) | **Google Flow Clip 02**: Sleek corporate trading floor at dusk | **Cross-Dissolve** (0.20s `Dissolve`) |
| **07b** | `07_02m50s_to_03m20s_sec_65m_penalty_settlement.mp4` | 02:50.50 – 03:20.16 (29.66s) | SEC administrative document, $65M penalty stamp, invoice flip | **Hard Cut** (0.00s) |
| **08** | `08_03m20s_to_03m53s_compounding_penny_500_trade_grid.mp4` | 03:20.16 – 03:53.48 (33.32s) | Single $2 loss sliver zooms out to 500-trade grid compounding | **Hard Cut** (0.00s) |
| **09** | `09_03m53s_to_04m23s_nbbo_vs_pfof_price_ladder.mp4` | 03:53.48 – 04:23.00 (29.52s) | Side-by-side NBBO vs PFOF columns, $2 worse per 100 shares | **Hard Cut** (0.00s) |
| **10** | `10_04m23s_to_04m59s_three_defense_steps_limit_orders.mp4` | 04:23.00 – 04:59.88 (36.88s) | 3 cards: Limit order lock, NBBO audit, Direct routing broker | **Hard Cut** (0.00s) |
| **11** | `11_04m59s_to_05m16s_loop_ledger_four_checkmarks.mp4` | 04:59.88 – 05:16.80 (16.92s) | 4 dossier icons snap shut in sequence with Power Lime checks | **Cross-Dissolve** (0.20s `Dissolve`) |
| **12a** | `12_05m16s_to_05m20s_flow_macro_phone_trade_confirmation.mp4` | 05:16.80 – 05:20.50 (3.70s) | **Google Flow Clip 03**: Macro shot of phone trade confirmation | **Cross-Dissolve** (0.20s `Dissolve`) |
| **12b** | `12_05m20s_to_05m37s_cta_end_card_clear_zones.mp4` | 05:20.50 – 05:37.12 (16.62s) | Quantrove brandmark, 20s clear zones for video & subscribe | **Fade to Black** (0.50s `Fade Out`) |

---

## 2. Kinetic Overlay Alignment (Track V2)

- **Master File**: `TIMELINE_MEDIA/00_00m00s_to_05m37s_kinetic_word_pops_overlay_60fps.mov`
- **Specification**: QuickTime RLE (`qtrle`) or Apple ProRes 4444 with Alpha Channel (`yuva420p` / `rgba`), exactly 60.0 fps, 1920x1080.
- **CapCut Blending Mode**: Set to **Normal** (alpha channel provides transparency natively).
- **Alignment Check**: Ensure `FREE TRADING ISN'T FREE` hits exactly at `00:06.10` on the master audio waveform.

---

## 3. Transitions & Fades (CapCut Free Tier)

**Brand Aesthetic Standard**: Institutional Data Intelligence — strictly zero stylistic flair, zero decorative wipes, zero zoom blur, zero glitch, zero spin, and zero camera shake. Clean, editorial, mathematically precise cuts throughout.

All transitions and fade controls specified below are **confirmed available in the CapCut Free Tier** (located in the standard *Basic* / *Overlay* transition libraries, video animation panels, and native audio inspector sliders). No CapCut Pro features or subscriptions required.

### 3.1 Master Cut Points Table (All 15 Clips / 14 Cut Points)

| Cut # | Outgoing Clip | Incoming Clip | Cut Timecode | Cut Type | Primary Transition (Free) | Backup Transition (Free) | Duration | Editorial Intent / Note |
|---|---|---|---|---|---|---|---|---|
| **01** | `01_00m00s_to_00m20s...` | `02_00m20s_to_00m38s...` | 00:20.00 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Crisp editorial cut on "how much it really costs" |
| **02** | `02_00m20s_to_00m38s...` | `03_00m38s_to_01m03s...` | 00:38.24 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Direct cut into 1999 commission ticket history |
| **03** | `03_00m38s_to_01m03s...` | `04_01m03s_to_01m07s...` | 01:03.40 | Cross-Dissolve | `Dissolve` | `Mix` | 0.20s | Soft entrance from vector graphics to live Flow server B-roll |
| **04** | `04_01m03s_to_01m07s...` | `04_01m07s_to_01m36s...` | 01:07.00 | Cross-Dissolve | `Dissolve` | `Mix` | 0.20s | Soft exit from server B-roll back into Manim order router |
| **05** | `04_01m07s_to_01m36s...` | `05_01m36s_to_02m11s...` | 01:36.84 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Crisp cut on "never heard of" into bid-ask order book |
| **06** | `05_01m36s_to_02m11s...` | `06_02m11s_to_02m47s...` | 02:11.80 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Clean cut on "risk-free profit" into PFOF kickback |
| **07** | `06_02m11s_to_02m47s...` | `07_02m47s_to_02m50s...` | 02:47.04 | Cross-Dissolve | `Dissolve` | `Mix` | 0.20s | Soft entrance into trading floor dusk live footage |
| **08** | `07_02m47s_to_02m50s...` | `07_02m50s_to_03m20s...` | 02:50.50 | Cross-Dissolve | `Dissolve` | `Mix` | 0.20s | Soft exit into SEC administrative proceeding document |
| **09** | `07_02m50s_to_03m20s...` | `08_03m20s_to_03m53s...` | 03:20.16 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Clean cut on "before you ever saw it" into penny loss grid |
| **10** | `08_03m20s_to_03m53s...` | `09_03m53s_to_04m23s...` | 03:53.48 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Direct shift from compounding grid to NBBO comparison |
| **11** | `09_03m53s_to_04m23s...` | `10_04m23s_to_04m59s...` | 04:23.00 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Direct cut into 3 actionable investor defense rules |
| **12** | `10_04m23s_to_04m59s...` | `11_04m59s_to_05m16s...` | 04:59.88 | Hard Cut | `None (Hard Cut)` | `None (Hard Cut)` | 0.00s | Crisp transition to dossier loop ledger checkmark cards |
| **13** | `11_04m59s_to_05m16s...` | `12_05m16s_to_05m20s...` | 05:16.80 | Cross-Dissolve | `Dissolve` | `Mix` | 0.20s | Soft entrance into macro smartphone trade confirmation |
| **14** | `12_05m16s_to_05m20s...` | `12_05m20s_to_05m37s...` | 05:20.50 | Cross-Dissolve | `Dissolve` | `Mix` | 0.20s | Soft return to final CTA outro & YouTube end card zones |

*Cut Summary*: 8 Manim-to-Manim cuts are strictly `Hard Cut` (0.00s). The 6 cuts entering and exiting the 3 Flow live-action cutaways use a subtle 0.20s `Dissolve` (Backup: `Mix`) to ease the visual transition between rendered graphics and realistic footage.

### 3.2 Opening & Closing Fades

1. **Opening Fade-In (00:00.00)**:
   - **Track V1 (Video)**: Set CapCut video animation to **Fade In** (Video → Animation → In → *Fade In*, or place *Black Fade* transition at the clip head) set to **0.30s**. Fades smoothly from Raisin Black (`#202322`) canvas. Primary: `Fade In` | Backup: `Black Fade`.
   - **Track A1 (Master Narration)**: Set audio inspector *Fade In* slider to **0.25s** (narration speech starts cleanly at 00:00.35).
   - **Track A2 (Music Bed)**: Set audio inspector *Fade In* slider to **0.50s** (music bed rises from silence to baseline -30 dB).
   - **Track V2 (Kinetic Overlay)**: No fade needed (overlay stream remains fully transparent until first word pop appears at 00:06.10).

2. **Closing Fade-Out (05:37.12)**:
   - **Track V1 (Video)**: Set CapCut video animation to **Fade Out** (Video → Animation → Out → *Fade Out*, or place *Black Fade* / *Fade to Black* transition on the tail of Clip 12b) set to **0.50s** (active from 05:36.62 to 05:37.12). Primary: `Fade Out` | Backup: `Black Fade` (or manual Opacity keyframes: 100% to 0% over 0.50s).
   - **Track A1 (Master Narration)**: Narration concludes at 05:36.50; apply a **0.20s** audio tail fade to zero.
   - **Track A2 (Music Bed)**: Set audio inspector *Fade Out* slider to **1.50s** (starts fading at 05:35.50, reaches absolute silence by 05:37.00).

### 3.3 Audio Ducking & Crossfade Under Flow Cutaways

Master voiceover runs continuously as a single unbroken 337.12s WAV file across all 15 clips without interruptions:
- **Track A1 (Voiceover)**: Continuous playback, no cuts, normalized to -14.0 LUFS.
- **Track A2 (Music Bed)**: Maintained continuously at ducked level (-34 dB under voiceover).
- **Track A3 (B-Roll Ambience / SFX for Flow Clips)**:
  - *Cutaway 01 (01:03.40 – 01:07.00, Server Corridor)*: Low data center server hum at -24 dB with a **0.20s audio fade-in** at 01:03.40 and **0.20s audio fade-out** at 01:06.80.
  - *Cutaway 02 (02:47.04 – 02:50.50, Trading Floor)*: Subtle trading floor room tone at -26 dB with a **0.20s audio fade-in** at 02:47.04 and **0.20s audio fade-out** at 02:50.30.
  - *Cutaway 03 (05:16.80 – 05:20.50, Macro Phone)*: Low-key haptic desk tone at -26 dB with a **0.20s audio fade-in** at 05:16.80 and **0.20s audio fade-out** at 05:20.30.
  *(All audio fade-in and fade-out adjustments use CapCut Free's native audio clip inspector handles).*

---

## 4. SFX Cue Sheet (Track A3)

| Timecode | Beat / Trigger | SFX Asset Type | Volume (dB) | Character / Feel |
|---|---|---|---|---|
| `00:04.50` | Phone button tap | Haptic UI Click | -12 dB | Clean mobile glass tap |
| `00:05.50` | Data packet explosion | Digital Particle Rush | -18 dB | High-frequency white-noise whoosh |
| `00:25.50` | Dossier segment 1 | Relay Switch Click | -14 dB | Heavy mechanical keyboard snap |
| `00:30.00` | Dossier segment 2 | Relay Switch Click | -14 dB | Pitch +1 semitone |
| `00:34.00` | Dossier segment 3 | Relay Switch Click | -14 dB | Pitch +2 semitones |
| `00:58.00` | Loupe zooms into fine print | Servo Motor Hum | -20 dB | Optical camera lens zoom |
| `01:18.00` | Exchange gate closes | Pneumatic Gate Slam | -15 dB | Metallic latch / industrial circuit breaker |
| `01:28.00` | Server racks activate | Data Center Server Ping | -22 dB | High-tech sonar blip |
| `01:57.00` | Bid/Ask spread highlights | Financial Ticker Tick | -16 dB | Crisp analog clock tick |
| `02:08.00` | Speed ramp on market making | High-Speed Coin Counter | -18 dB | Ramping mechanical cash counter |
| `02:40.00` | Revenue bar shoots upward | Heavy Bar Impact Thud | -14 dB | Clean bass transient |
| `02:54.00` | SEC penalty stamp hits | Official Gavel / Heavy Thud | -10 dB | Deep wooden impact with low-end |
| `03:38.00` | 500-cell grid multiplies | Cascading Digital Dominoes | -18 dB | Rapid micro-clicks (granular synthesis) |
| `04:31.00` | Limit order lock snaps | Heavy Padlock Snap | -12 dB | Vault deadbolt latching shut |
| `05:03.00` | Loop closure #1 | Satisfying Snap | -14 dB | UI completion chime |
| `05:08.50` | Loop closure #2 | Satisfying Snap | -14 dB | UI completion chime |
| `05:11.50` | Loop closure #3 | Satisfying Snap | -14 dB | UI completion chime |
| `05:14.50` | Loop closure #4 | Satisfying Snap | -14 dB | UI completion chime |

---

## 5. YouTube Studio Upload Checklist

1. **Unlisted Staging Upload**:
   - Date: **Wednesday, September 30, 2026 @ 06:00 AM ET (13:30 IRST)**.
   - Wait for `HD` and `4K` blue badges before toggling to Public.
2. **Metadata**:
   - Title: **Why "Free" Trading Isn't Free** (Option 1).
   - Paste description with calibrated timestamps and regulatory citations.
   - Paste 24 tags.
3. **Thumbnail Slot**:
   - Upload `99_00m00s_to_05m37s_thumbnail_ep05_market_making.png` (`$0 ISN'T FREE` badge).
4. **Interactive Video Elements**:
   - **End Screen** (Trigger at `05:17` / T-20s):
     - Left: Best for Viewer / EP04 Flagship Video Card.
     - Right: Quantrove Subscribe Card.
   - **Info Cards**:
     - At `02:50` (SEC Case): Card pointing to EP03 ("How Algorithms Decide").
     - At `04:35` (Limit Orders): Card pointing to Quantrove Playlist.
5. **Playlist**:
   - Assign to **💰 Finance & Trading, Simplified** (Pillar 3).
6. **Public Release**:
   - Set automated premiere / public release for **10:00 AM ET sharp (17:30 IRST / 14:00 UTC)**.
   - Pin top comment directing viewers to audit their own trade confirmations.
