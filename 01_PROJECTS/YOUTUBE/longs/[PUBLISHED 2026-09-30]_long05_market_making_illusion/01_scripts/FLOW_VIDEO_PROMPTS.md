# EP05 Google Flow Video Generation Prompts (Fintech YouTube Aesthetic)
**Episode**: EP05 — *Market Making & The Illusion of Free Trading*  
**Tool**: Google Flow (`labs.google/flow`) — Manual generation by Sahand  
**Total Clips**: Exactly 3 Flow Video Clips (2 in body + 1 at the end)  
**Style Standard**: Modern Fintech Explainer on YouTube — clean architectural realism, institutional financial technology, pristine high-end tech workspace. Zero sci-fi fantasy, zero holographic lasers, zero Hollywood drama.

---

### CLIP 01: High-Frequency Trading Server Infrastructure (Scene 04 Cutaway)
- **Target In-Video Window**: Scene 04 (`01:05 – 01:12`, 1.5s to 2.0s establishing cutaway)
- **Narrative Context**: Demonstrates the physical reality of off-exchange wholesale market makers (Citadel, Virtu) executing trades in microseconds.
- **Aspect Ratio**: 16:9 Landscape (1920x1080)
- **Prompt for Google Flow (`labs.google/flow`)**:
  ```text
  Clean, high-end enterprise data center corridor for algorithmic financial trading. Pristine rows of modern matte-black server racks with subtle, realistic blinking fiber-optic LED indicator lights in lime green (#C3D809) and cool off-white (#E6EDF3). High shutter speed, sharp focus on server chassis texture, brushed metal finishes, high-density cable management. Smooth, continuous robotic camera push-in down the server aisle at eye level, paced for a full 3.5-second unbroken move — steady and mechanical throughout, no rushed motion. Dark charcoal (#202322) and deep slate (#233D4C) surfaces, realistic corporate architectural lighting. No sci-fi holograms, no fantasy elements. Photorealistic 4k, 60fps.
  ```
- **Motion Guidance**: Slow forward camera tracking (push <= 1.05x). Steady, mechanical, clinical precision.

---

### CLIP 02: Institutional Financial Trading Floor at Dusk (Scene 07 Cutaway)
- **Target In-Video Window**: Scene 07 (`03:15 – 03:22`, 1.5s to 2.0s establishing cutaway)
- **Narrative Context**: Introduces the regulatory weight and institutional scale of the SEC enforcement proceeding against retail order routing.
- **Aspect Ratio**: 16:9 Landscape (1920x1080)
- **Prompt for Google Flow (`labs.google/flow`)**:
  ```text
  Cinematic wide interior shot of a sleek modern institutional financial office and trading desk at blue hour dusk. Floor-to-ceiling glass windows overlooking a dark metropolitan financial district skyline with soft architectural ambient lights. Multi-monitor workstations display dark-mode financial charts and order-book data with lime-green (#C3D809) and orange (#FD802E) accents. Soft atmospheric reflections on dark polished stone and glass. Slow, continuous horizontal dolly movement sustained across a full 3.4-second beat — quiet institutional gravity, no abrupt starts or stops. Crisp, zero clutter, no people visible. Photorealistic 4k, 60fps.
  ```
- **Motion Guidance**: Slow lateral slider / dolly right. Quiet institutional gravity.

---

### CLIP 03: Personal Trade Audit & Clean Fintech Desk (Scene 12 End Scene Cutaway)
- **Target In-Video Window**: Scene 12 (`05:45 – 05:52`, 2.0s to 2.5s establishing cutaway)
- **Narrative Context**: Direct call-to-action moment prompting the viewer to open their brokerage app and audit their own trade confirmation.
- **Aspect Ratio**: 16:9 Landscape (1920x1080)
- **Prompt for Google Flow (`labs.google/flow`)**:
  ```text
  Macro top-down overhead shot of a minimalist fintech workspace on a matte dark slate desk (#202322). A sleek black smartphone lies flat, screen brightly illuminated showing a dark-mode brokerage app with an executed order confirmation, sharp lime-green (#C3D809) checkmark, and clean off-white (#E6EDF3) execution timestamps. A matte-black keyboard and dark titanium watch sit beside it. Soft directional studio rim lighting, subtle shadows. Slow, continuous vertical tilt and micro-zoom into the phone screen, sustained smoothly across a full 3.7-second move. Premium, clinical fintech aesthetic. Photorealistic 4k, 60fps.
  ```
- **Motion Guidance**: Gentle tilt-down / micro-push toward the phone display.

---

### Ingestion & Timeline Placement SOP
Once Sahand generates these 3 video clips in Google Flow:
1. Download 1080p/4K MP4 files from `labs.google/flow`.
2. Move them into `TIMELINE_MEDIA/` with standard chronological names:
   - `04a_01m05s_to_01m08s_flow_hft_server_rack_corridor.mp4`
   - `07a_03m15s_to_03m18s_flow_institutional_trading_floor_dusk.mp4`
   - `12a_05m45s_to_05m48s_flow_macro_phone_trade_confirmation.mp4`
3. CapCut: Insert into Track V1 at the exact scene boundary cutaways per `CAPCUT_FINAL_ASSEMBLY_GUIDE.md`.
