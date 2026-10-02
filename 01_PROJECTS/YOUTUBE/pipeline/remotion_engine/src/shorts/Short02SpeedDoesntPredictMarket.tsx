import React from "react";
import {
  AbsoluteFill,
  Audio,
  Easing,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { CaptionsLayer } from "../components/CaptionsLayer";
import captionChunks from "../data/short02_caption_chunks.json";

// Quantrove Brand Palette
const BG = "#202322";
const CARD_BG = "#1A1E1D";
const BORDER = "#233D4C";
const LIME = "#C3D809";
const PUMPKIN = "#FD802E";
const TEXT = "#E6EDF3";

export const Short02SpeedDoesntPredictMarket: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // Camera subtle push (1.0 -> 1.035 across the video)
  const cameraScale = interpolate(currentTime, [0, 43.55], [1.0, 1.035], {
    extrapolateRight: "clamp",
  });

  // Scene transitions:
  // Beat 1: 0.0s - 6.0s (Dual exchanges at $150.00 / $150.02)
  // Beat 2: 6.0s - 14.5s (Exchange A updates to $150.05, Stale quote window)
  // Beat 3: 14.5s - 23.8s (Fast machine races to stale quote)
  // Beat 4: 23.8s - 35.2s (10 machines at same price: Queue priority)
  // Beat 5: 35.2s - 43.55s (Microsecond fill delta)

  const b1Spring = spring({ frame, fps, config: { damping: 14 } });
  const b2Spring = spring({ frame: frame - Math.floor(6.0 * fps), fps, config: { damping: 14 } });
  const b3Spring = spring({ frame: frame - Math.floor(14.5 * fps), fps, config: { damping: 13, stiffness: 110 } });
  const b4Spring = spring({ frame: frame - Math.floor(23.8 * fps), fps, config: { damping: 14 } });
  const b5Spring = spring({ frame: frame - Math.floor(35.2 * fps), fps, config: { damping: 14 } });

  // Laser packet race animation across Beat 3 (16.5s to 20.0s)
  const packetProgress = interpolate(currentTime, [17.0, 19.8], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const microsecondClock = Math.round(
    interpolate(currentTime, [17.0, 19.8], [0, 210], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    })
  );

  return (
    <AbsoluteFill
      style={{
        backgroundColor: BG,
        color: TEXT,
        fontFamily: "'Nohemi', 'Inter', -apple-system, sans-serif",
        overflow: "hidden",
      }}
    >
      {/* Voiceover Master Audio */}
      <Audio src={staticFile("audio/short02_speed_doesnt_predict_market_vo.mp3")} volume={1.0} />

      {/* Main Container with subtle camera push */}
      <div
        style={{
          width: "100%",
          height: "100%",
          transform: `scale(${cameraScale})`,
          transformOrigin: "center center",
          position: "relative",
        }}
      >
        {/* Subtle Background Grid Lines */}
        <svg
          style={{
            position: "absolute",
            inset: 0,
            width: 1080,
            height: 1920,
            opacity: 0.15,
            pointerEvents: "none",
          }}
        >
          <defs>
            <pattern id="grid02" width="60" height="60" patternUnits="userSpaceOnUse">
              <path d="M 60 0 L 0 0 0 60" fill="none" stroke={BORDER} strokeWidth="1" />
            </pattern>
          </defs>
          <rect width="1080" height="1920" fill="url(#grid02)" />
        </svg>

        {/* Top Header Telemetry (y: 130px) */}
        <div
          style={{
            position: "absolute",
            top: 130,
            left: 60,
            right: 200,
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderBottom: `1px solid ${BORDER}`,
            paddingBottom: 16,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
            <div style={{ width: 8, height: 8, borderRadius: "50%", backgroundColor: LIME }} />
            <span style={{ fontSize: 20, fontWeight: 700, letterSpacing: "0.08em", color: TEXT }}>
              QUANTROVE // LATENCY ARBITRAGE
            </span>
          </div>
          <span style={{ fontSize: 18, color: BORDER, fontWeight: 600 }}>
            EP06.02 · SUB-MILLISECOND
          </span>
        </div>

        {/* ============================================================ */}
        {/* VISUAL STAGE BAND (y: 250px to 1040px) */}
        {/* ============================================================ */}
        <div
          style={{
            position: "absolute",
            top: 250,
            left: 60,
            width: 820,
            height: 780,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          {/* BEAT 1, 2, 3: Dual Exchange Venues & Cross-Venue Arb [0.0s - 23.8s] */}
          {currentTime < 23.8 && (
            <div
              style={{
                width: "100%",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b1Spring,
                transform: `scale(${interpolate(b1Spring, [0, 1], [0.94, 1.0])})`,
              }}
            >
              {/* Asset Badge */}
              <div
                style={{
                  backgroundColor: CARD_BG,
                  border: `1px solid ${BORDER}`,
                  borderRadius: 20,
                  padding: "8px 20px",
                  fontSize: 18,
                  fontWeight: 600,
                  color: TEXT,
                  marginBottom: 20,
                  display: "flex",
                  alignItems: "center",
                  gap: 8,
                }}
              >
                <span>STOCK:</span>
                <span style={{ color: LIME, fontWeight: 700 }}>SPY</span>
                <span style={{ color: BORDER }}>|</span>
                <span style={{ fontSize: 16, color: "#8E9E9C" }}>DUAL-LISTED VENUES</span>
              </div>

              {/* Dual Exchange Cards */}
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  width: "100%",
                  gap: 16,
                  position: "relative",
                }}
              >
                {/* EXCHANGE A (Carteret) */}
                <div
                  style={{
                    flex: 1,
                    backgroundColor: CARD_BG,
                    borderRadius: 16,
                    border: `2px solid ${currentTime >= 6.5 ? LIME : BORDER}`,
                    padding: "24px 18px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    boxShadow:
                      currentTime >= 6.5 ? "0 0 30px rgba(195, 216, 9, 0.2)" : "none",
                  }}
                >
                  <span style={{ fontSize: 16, fontWeight: 700, color: LIME, letterSpacing: "0.05em" }}>
                    EXCHANGE A (CARTERET)
                  </span>
                  <div
                    style={{
                      fontSize: 52,
                      fontWeight: 700,
                      margin: "16px 0",
                      color: currentTime >= 6.5 ? LIME : TEXT,
                    }}
                  >
                    {currentTime >= 6.5 ? "$150.05" : "$150.02"}
                  </div>
                  <span
                    style={{
                      fontSize: 14,
                      fontWeight: 600,
                      color: currentTime >= 6.5 ? LIME : "#7A8C8A",
                      textAlign: "center",
                    }}
                  >
                    {currentTime >= 6.5 ? "⚡ PRICE UPDATED FIRST" : "BID $150.00 / ASK $150.02"}
                  </span>
                </div>

                {/* EXCHANGE B (Secaucus) */}
                <div
                  style={{
                    flex: 1,
                    backgroundColor: CARD_BG,
                    borderRadius: 16,
                    border: `2px solid ${
                      currentTime >= 6.5 && currentTime < 21.0 ? PUMPKIN : BORDER
                    }`,
                    padding: "24px 18px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    boxShadow:
                      currentTime >= 6.5 && currentTime < 21.0
                        ? "0 0 30px rgba(253, 128, 46, 0.2)"
                        : "none",
                  }}
                >
                  <span style={{ fontSize: 16, fontWeight: 700, color: TEXT, letterSpacing: "0.05em" }}>
                    EXCHANGE B (SECAUCUS)
                  </span>
                  <div
                    style={{
                      fontSize: 52,
                      fontWeight: 700,
                      margin: "16px 0",
                      color: currentTime >= 6.5 && currentTime < 21.0 ? PUMPKIN : TEXT,
                    }}
                  >
                    $150.02
                  </div>
                  <span
                    style={{
                      fontSize: 14,
                      fontWeight: 600,
                      color: currentTime >= 6.5 && currentTime < 21.0 ? PUMPKIN : "#7A8C8A",
                      textAlign: "center",
                    }}
                  >
                    {currentTime >= 6.5 && currentTime < 21.0
                      ? "⚠️ STALE QUOTE (OLD PRICE)"
                      : "BID $150.00 / ASK $150.02"}
                  </span>
                </div>
              </div>

              {/* BEAT 2 & 3: Microwave Laser Packet Travel & Stale Quote Race */}
              {currentTime >= 6.5 && (
                <div
                  style={{
                    marginTop: 28,
                    width: "100%",
                    backgroundColor: CARD_BG,
                    borderRadius: 16,
                    border: `1px solid ${BORDER}`,
                    padding: "24px 20px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    opacity: b2Spring,
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      width: "100%",
                      fontSize: 16,
                      fontWeight: 700,
                      color: "#A2B4B2",
                      marginBottom: 12,
                    }}
                  >
                    <span>CARTERET, NJ</span>
                    <span style={{ color: LIME }}>35-MILE DIRECT MICROWAVE LINK</span>
                    <span>SECAUCUS, NJ</span>
                  </div>

                  {/* Laser Beam Progress Bar */}
                  <div
                    style={{
                      width: "100%",
                      height: 12,
                      backgroundColor: BG,
                      borderRadius: 6,
                      overflow: "hidden",
                      position: "relative",
                      marginBottom: 16,
                    }}
                  >
                    <div
                      style={{
                        position: "absolute",
                        left: 0,
                        top: 0,
                        bottom: 0,
                        width: `${packetProgress * 100}%`,
                        backgroundColor: LIME,
                        boxShadow: "0 0 15px #C3D809",
                      }}
                    />
                  </div>

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      width: "100%",
                      alignItems: "center",
                    }}
                  >
                    <span style={{ fontSize: 18, color: TEXT }}>
                      HFT ORDER TRANSIT:{" "}
                      <span style={{ color: LIME, fontWeight: 700 }}>
                        {microsecondClock} µs
                      </span>
                    </span>
                    <span
                      style={{
                        fontSize: 16,
                        color: packetProgress >= 1 ? LIME : PUMPKIN,
                        fontWeight: 700,
                      }}
                    >
                      {packetProgress >= 1
                        ? "✓ FILLED STALE QUOTE (+$0.03 ARB)"
                        : "STALE WINDOW: 280 µs"}
                    </span>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* BEAT 4 & 5: The Order Book Queue & Microsecond Priority [23.8s - 43.55s] */}
          {currentTime >= 23.8 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `1px solid ${BORDER}`,
                padding: "32px 24px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b4Spring,
                transform: `scale(${interpolate(b4Spring, [0, 1], [0.94, 1.0])})`,
              }}
            >
              <div
                style={{
                  fontSize: 18,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.08em",
                  marginBottom: 8,
                }}
              >
                PRICE-TIME PRIORITY (FIFO)
              </div>
              <div style={{ fontSize: 26, fontWeight: 700, color: TEXT, marginBottom: 20 }}>
                10 Machines At Same Price ($150.00)
              </div>

              {/* Queue Stacks */}
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  gap: 10,
                  width: "100%",
                }}
              >
                {/* POSITION #1: FIRST ARRIVAL (ALGO A) */}
                <div
                  style={{
                    backgroundColor: currentTime >= 35.2 ? "rgba(195, 216, 9, 0.15)" : BG,
                    borderRadius: 12,
                    border: `2px solid ${currentTime >= 35.2 ? LIME : BORDER}`,
                    padding: "16px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    boxShadow:
                      currentTime >= 35.2 ? "0 0 25px rgba(195, 216, 9, 0.2)" : "none",
                  }}
                >
                  <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                    <div
                      style={{
                        backgroundColor: LIME,
                        color: BG,
                        fontWeight: 700,
                        fontSize: 16,
                        padding: "4px 10px",
                        borderRadius: 8,
                      }}
                    >
                      #1
                    </div>
                    <div>
                      <div style={{ fontSize: 18, fontWeight: 700, color: TEXT }}>
                        ALGO A (09:30:00.000102)
                      </div>
                      <div style={{ fontSize: 14, color: "#8E9E9C" }}>
                        ARRIVED 1.4 µs AHEAD OF ALGO B
                      </div>
                    </div>
                  </div>
                  <span
                    style={{
                      fontSize: 18,
                      fontWeight: 700,
                      color: currentTime >= 35.2 ? LIME : "#A2B4B2",
                    }}
                  >
                    {currentTime >= 35.2 ? "100% FILLED" : "FIRST IN LINE"}
                  </span>
                </div>

                {/* POSITION #2: ALGO B */}
                <div
                  style={{
                    backgroundColor: BG,
                    borderRadius: 12,
                    border: `1px solid ${BORDER}`,
                    padding: "14px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    opacity: 0.6,
                  }}
                >
                  <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                    <div
                      style={{
                        backgroundColor: BORDER,
                        color: TEXT,
                        fontWeight: 600,
                        fontSize: 16,
                        padding: "4px 10px",
                        borderRadius: 8,
                      }}
                    >
                      #2
                    </div>
                    <div style={{ fontSize: 18, color: TEXT }}>ALGO B (09:30:00.000104)</div>
                  </div>
                  <span style={{ fontSize: 16, color: PUMPKIN, fontWeight: 600 }}>
                    {currentTime >= 35.2 ? "UNFILLED" : "+1.4 µs BEHIND"}
                  </span>
                </div>

                {/* POSITIONS #3 - #10 (Collapsed representation) */}
                <div
                  style={{
                    backgroundColor: BG,
                    borderRadius: 12,
                    border: `1px solid ${BORDER}`,
                    padding: "12px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    opacity: 0.35,
                  }}
                >
                  <span style={{ fontSize: 16, color: "#8E9E9C" }}>
                    POSITIONS #3 THROUGH #10 (ALGOS C TO J)
                  </span>
                  <span style={{ fontSize: 14, color: "#8E9E9C" }}>
                    QUEUE DEPTH: 90,000 SHARES
                  </span>
                </div>
              </div>

              {/* BEAT 5 Callout: Microsecond Delta */}
              {currentTime >= 35.2 && (
                <div
                  style={{
                    marginTop: 24,
                    width: "100%",
                    backgroundColor: "rgba(195, 216, 9, 0.1)",
                    borderRadius: 12,
                    border: `1px solid ${LIME}`,
                    padding: "16px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    opacity: b5Spring,
                  }}
                >
                  <span style={{ fontSize: 18, fontWeight: 700, color: LIME }}>
                    MICROSECOND REALITY:
                  </span>
                  <span style={{ fontSize: 18, color: TEXT, fontWeight: 600 }}>
                    1.4 µs = ALL PROFIT vs ZERO FILL
                  </span>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Captions Layer in Safe Text Band (y: 1160px) */}
        <CaptionsLayer chunks={captionChunks} topY={1160} />
      </div>
    </AbsoluteFill>
  );
};
