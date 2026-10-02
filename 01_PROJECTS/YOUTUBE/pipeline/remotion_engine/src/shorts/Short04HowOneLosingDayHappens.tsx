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
import captionChunks from "../data/short04_caption_chunks.json";

// Quantrove Brand Palette
const BG = "#202322";
const CARD_BG = "#1A1E1D";
const BORDER = "#233D4C";
const LIME = "#C3D809";
const PUMPKIN = "#FD802E";
const TEXT = "#E6EDF3";

export const Short04HowOneLosingDayHappens: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // Camera subtle push (1.0 -> 1.035 across the video)
  const cameraScale = interpolate(currentTime, [0, 52.85], [1.0, 1.035], {
    extrapolateRight: "clamp",
  });

  // Scene springs:
  // Beat 1: 0.0s - 8.2s (Virtu 1,238 trading days matrix)
  // Beat 2: 8.2s - 15.0s (Micro-edge + instant delta hedge)
  // Beat 3: 15.0s - 29.0s (Law of Large Numbers across 5M trades)
  // Beat 4: 29.0s - 36.8s (Monotonic equity curve + fragility shift)
  // Beat 5: 36.8s - 46.2s (Knight Capital August 2012 tech glitch)
  // Beat 6: 46.2s - 52.85s (-$460M loss in 45 minutes)

  const b1Spring = spring({ frame, fps, config: { damping: 14 } });
  const b2Spring = spring({ frame: frame - Math.floor(8.2 * fps), fps, config: { damping: 14 } });
  const b3Spring = spring({ frame: frame - Math.floor(15.0 * fps), fps, config: { damping: 14 } });
  const b4Spring = spring({ frame: frame - Math.floor(29.0 * fps), fps, config: { damping: 14 } });
  const b5Spring = spring({ frame: frame - Math.floor(36.8 * fps), fps, config: { damping: 13, stiffness: 120 } });
  const b6Spring = spring({ frame: frame - Math.floor(46.2 * fps), fps, config: { damping: 14 } });

  // High-frequency trade counter for Beat 3 (15.0s to 26.0s: 0 -> 5,000,000)
  const tradeCounter = Math.round(
    interpolate(currentTime, [15.5, 25.0], [0, 5000000], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: Easing.out(Easing.cubic),
    })
  );

  // Plunging Knight Capital loss for Beat 6 (46.5s to 50.0s: 0 -> -460,000,000)
  const knightLoss = Math.round(
    interpolate(currentTime, [46.5, 49.5], [0, 460000000], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
      easing: Easing.bezier(0.16, 1, 0.3, 1),
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
      <Audio src={staticFile("audio/short04_how_one_losing_day_happens_vo.mp3")} volume={1.0} />

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
            <pattern id="grid04" width="60" height="60" patternUnits="userSpaceOnUse">
              <path d="M 60 0 L 0 0 0 60" fill="none" stroke={BORDER} strokeWidth="1" />
            </pattern>
          </defs>
          <rect width="1080" height="1920" fill="url(#grid04)" />
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
              QUANTROVE // STATISTICAL ARB
            </span>
          </div>
          <span style={{ fontSize: 18, color: BORDER, fontWeight: 600 }}>
            VIRTU (S-1) · KNIGHT CAPITAL
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
          {/* BEAT 1: 1,238 Trading Days Matrix [0.0s - 8.2s] */}
          {currentTime < 8.2 && (
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
              <div
                style={{
                  backgroundColor: CARD_BG,
                  border: `1px solid ${BORDER}`,
                  borderRadius: 20,
                  padding: "8px 22px",
                  fontSize: 18,
                  fontWeight: 600,
                  color: TEXT,
                  marginBottom: 16,
                  display: "flex",
                  alignItems: "center",
                  gap: 8,
                }}
              >
                <span>VIRTU FINANCIAL S-1 (2009–2014)</span>
              </div>

              {/* Matrix of 1,238 Days SVG Representation */}
              <div
                style={{
                  width: "100%",
                  backgroundColor: CARD_BG,
                  borderRadius: 20,
                  border: `2px solid ${LIME}`,
                  padding: "24px 20px",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  boxShadow: "0 0 35px rgba(195, 216, 9, 0.15)",
                }}
              >
                <div
                  style={{
                    display: "flex",
                    justifyContent: "space-between",
                    width: "100%",
                    marginBottom: 14,
                    fontSize: 18,
                    fontWeight: 700,
                  }}
                >
                  <span style={{ color: LIME }}>1,237 WINNING DAYS</span>
                  <span style={{ color: PUMPKIN }}>1 LOSING DAY</span>
                </div>

                {/* Simulated Dot Density Grid */}
                <div
                  style={{
                    width: "100%",
                    height: 200,
                    backgroundColor: BG,
                    borderRadius: 12,
                    border: `1px solid ${BORDER}`,
                    padding: 12,
                    display: "flex",
                    flexWrap: "wrap",
                    gap: 4,
                    alignContent: "flex-start",
                    overflow: "hidden",
                    position: "relative",
                  }}
                >
                  {Array.from({ length: 280 }).map((_, idx) => {
                    // One solitary losing day at index 142
                    const isLosingDay = idx === 142;
                    return (
                      <div
                        key={idx}
                        style={{
                          width: 8,
                          height: 8,
                          borderRadius: 2,
                          backgroundColor: isLosingDay ? PUMPKIN : LIME,
                          opacity: isLosingDay ? 1.0 : 0.75,
                          boxShadow: isLosingDay ? "0 0 10px #FD802E" : "none",
                        }}
                      />
                    );
                  })}

                  <div
                    style={{
                      position: "absolute",
                      bottom: 8,
                      right: 12,
                      fontSize: 14,
                      color: "#8E9E9C",
                      fontWeight: 600,
                    }}
                  >
                    ... 1,238 TOTAL SESSIONS
                  </div>
                </div>

                <div
                  style={{
                    marginTop: 18,
                    fontSize: 28,
                    fontWeight: 700,
                    color: TEXT,
                    textAlign: "center",
                  }}
                >
                  99.92% PROFITABLE SESSIONS
                </div>
              </div>
            </div>
          )}

          {/* BEAT 2: Micro-Edge & Instant Hedging [8.2s - 15.0s] */}
          {currentTime >= 8.2 && currentTime < 15.0 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `1px solid ${BORDER}`,
                padding: "36px 28px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b2Spring,
                transform: `scale(${interpolate(b2Spring, [0, 1], [0.94, 1.0])})`,
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.1em",
                  marginBottom: 10,
                }}
              >
                THE CORE EXECUTION ENGINE
              </div>

              <div style={{ fontSize: 26, fontWeight: 700, color: TEXT, marginBottom: 24 }}>
                Micro-Margin + Instant Delta Hedge
              </div>

              {/* Execution Graphic */}
              <div
                style={{
                  width: "100%",
                  display: "flex",
                  gap: 14,
                  marginBottom: 20,
                }}
              >
                <div
                  style={{
                    flex: 1,
                    backgroundColor: BG,
                    borderRadius: 12,
                    padding: "20px 16px",
                    border: `1px solid ${LIME}`,
                    textAlign: "center",
                  }}
                >
                  <div style={{ fontSize: 16, color: "#8E9E9C" }}>SPREAD CAPTURE</div>
                  <div style={{ fontSize: 32, fontWeight: 700, color: LIME, margin: "6px 0" }}>
                    +$0.002
                  </div>
                  <div style={{ fontSize: 14, color: TEXT }}>0.2 cents per share</div>
                </div>

                <div
                  style={{
                    flex: 1,
                    backgroundColor: BG,
                    borderRadius: 12,
                    padding: "20px 16px",
                    border: `1px solid ${BORDER}`,
                    textAlign: "center",
                  }}
                >
                  <div style={{ fontSize: 16, color: "#8E9E9C" }}>HEDGE LATENCY</div>
                  <div style={{ fontSize: 32, fontWeight: 700, color: TEXT, margin: "6px 0" }}>
                    &lt; 5 ms
                  </div>
                  <div style={{ fontSize: 14, color: LIME, fontWeight: 600 }}>Net Delta = 0.00</div>
                </div>
              </div>

              <span style={{ fontSize: 18, color: "#A2B4B2", textAlign: "center" }}>
                Zero directional exposure. Pure liquidity spread capture.
              </span>
            </div>
          )}

          {/* BEAT 3: Law of Large Numbers (5,000,000 Trades) [15.0s - 29.0s] */}
          {currentTime >= 15.0 && currentTime < 29.0 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `2px solid ${LIME}`,
                padding: "36px 28px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b3Spring,
                boxShadow: "0 0 40px rgba(195, 216, 9, 0.15)",
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.1em",
                  marginBottom: 10,
                }}
              >
                THE LAW OF LARGE NUMBERS
              </div>

              <div style={{ fontSize: 24, fontWeight: 600, color: TEXT, marginBottom: 12 }}>
                Trades Executed Per Day:
              </div>

              {/* Fast Spinning Trade Counter */}
              <div
                style={{
                  fontSize: 66,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "-0.02em",
                  fontFamily: "'Nohemi', 'Inter', sans-serif",
                }}
              >
                {tradeCounter.toLocaleString()}
              </div>

              <div
                style={{
                  marginTop: 24,
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 14,
                  padding: "18px 24px",
                  border: `1px solid ${BORDER}`,
                  display: "flex",
                  justifyContent: "space-between",
                  fontSize: 18,
                }}
              >
                <span style={{ color: "#8E9E9C" }}>Edge Per Trade: +$0.002</span>
                <span style={{ color: LIME, fontWeight: 700 }}>Statistical Variance ➔ 0</span>
              </div>
            </div>
          )}

          {/* BEAT 4: Smooth Equity Curve vs System Fragility [29.0s - 36.8s] */}
          {currentTime >= 29.0 && currentTime < 36.8 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `1px solid ${PUMPKIN}`,
                padding: "36px 28px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b4Spring,
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: PUMPKIN,
                  letterSpacing: "0.1em",
                  marginBottom: 10,
                }}
              >
                THE DUAL NATURE OF HIGH FREQUENCY
              </div>

              <div style={{ fontSize: 26, fontWeight: 700, color: TEXT, marginBottom: 20, textAlign: "center" }}>
                1,238 Days of Monotonic Growth...
              </div>

              {/* Ascending Equity Curve Diagram */}
              <div
                style={{
                  width: "100%",
                  height: 120,
                  backgroundColor: BG,
                  borderRadius: 12,
                  border: `1px solid ${BORDER}`,
                  position: "relative",
                  overflow: "hidden",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  marginBottom: 20,
                }}
              >
                <svg width="100%" height="100%" style={{ overflow: "visible" }}>
                  <polyline
                    fill="none"
                    stroke={LIME}
                    strokeWidth="3"
                    points="20,100 120,85 240,70 380,50 520,35 680,20"
                  />
                </svg>
                <span
                  style={{
                    position: "absolute",
                    right: 20,
                    bottom: 12,
                    fontSize: 16,
                    color: LIME,
                    fontWeight: 700,
                  }}
                >
                  SHARPE &gt; 4.0
                </span>
              </div>

              <div
                style={{
                  color: PUMPKIN,
                  fontSize: 20,
                  fontWeight: 700,
                  textAlign: "center",
                }}
              >
                ⚠️ BUT THE SYSTEM HAS ANOTHER SIDE
              </div>
            </div>
          )}

          {/* BEAT 5: Knight Capital August 2012 Glitch [36.8s - 46.2s] */}
          {currentTime >= 36.8 && currentTime < 46.2 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `2px solid ${PUMPKIN}`,
                padding: "36px 28px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b5Spring,
                boxShadow: "0 0 45px rgba(253, 128, 46, 0.25)",
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: PUMPKIN,
                  letterSpacing: "0.1em",
                  marginBottom: 10,
                }}
              >
                CASE STUDY: CRITICAL FAILURE
              </div>

              <div style={{ fontSize: 26, fontWeight: 700, color: TEXT, marginBottom: 8, textAlign: "center" }}>
                Knight Capital Group
              </div>
              <div style={{ fontSize: 18, color: "#8E9E9C", marginBottom: 20 }}>
                August 1, 2012 · 09:30 AM to 10:15 AM
              </div>

              {/* Glitch Breakdown */}
              <div
                style={{
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 14,
                  padding: "20px 24px",
                  border: `1px solid ${BORDER}`,
                  display: "flex",
                  flexDirection: "column",
                  gap: 12,
                }}
              >
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 18 }}>
                  <span style={{ color: "#8E9E9C" }}>Glitch Duration:</span>
                  <span style={{ color: TEXT, fontWeight: 700 }}>45 Minutes</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 18 }}>
                  <span style={{ color: "#8E9E9C" }}>Rogue Orders:</span>
                  <span style={{ color: PUMPKIN, fontWeight: 700 }}>4,000,000 Executions</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 18 }}>
                  <span style={{ color: "#8E9E9C" }}>Cause:</span>
                  <span style={{ color: TEXT, fontWeight: 600 }}>SMARS Deployment Bug</span>
                </div>
              </div>
            </div>
          )}

          {/* BEAT 6: Final Plunge: -$460 Million [46.2s - 52.85s] */}
          {currentTime >= 46.2 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `2px solid ${PUMPKIN}`,
                padding: "44px 28px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b6Spring,
                boxShadow: "0 0 60px rgba(253, 128, 46, 0.35)",
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: PUMPKIN,
                  letterSpacing: "0.1em",
                  marginBottom: 10,
                }}
              >
                TOTAL LOSS IN A SINGLE DAY
              </div>

              <div
                style={{
                  fontSize: 72,
                  fontWeight: 700,
                  color: PUMPKIN,
                  fontFamily: "'Nohemi', 'Inter', sans-serif",
                  letterSpacing: "-0.03em",
                  margin: "12px 0",
                }}
              >
                -${Math.round(knightLoss / 1000000)}M
              </div>

              <div style={{ fontSize: 22, fontWeight: 600, color: TEXT, textAlign: "center", marginBottom: 20 }}>
                ~$460 Million Lost in 45 Minutes
              </div>

              <div
                style={{
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 14,
                  padding: "16px 20px",
                  border: `1px solid ${BORDER}`,
                  textAlign: "center",
                  fontSize: 18,
                  color: PUMPKIN,
                  fontWeight: 700,
                }}
              >
                ONE SOFTWARE FAILURE ERASED THE ENTIRE FIRM
              </div>
            </div>
          )}
        </div>

        {/* Captions Layer in Safe Text Band (y: 1160px) */}
        <CaptionsLayer chunks={captionChunks} topY={1160} />
      </div>
    </AbsoluteFill>
  );
};
