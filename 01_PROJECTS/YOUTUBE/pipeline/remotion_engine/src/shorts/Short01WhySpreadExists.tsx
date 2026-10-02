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
import captionChunks from "../data/short01_caption_chunks.json";

// Quantrove Brand Palette
const BG = "#202322";
const CARD_BG = "#1A1E1D";
const BORDER = "#233D4C";
const LIME = "#C3D809";
const PUMPKIN = "#FD802E";
const TEXT = "#E6EDF3";

export const Short01WhySpreadExists: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // Camera subtle push (1.0 -> 1.04 across the video)
  const cameraScale = interpolate(currentTime, [0, 46.6], [1.0, 1.035], {
    extrapolateRight: "clamp",
  });

  // Dynamic values per beat:
  // Beat 1 & 2: 0.0s - 9.5s (Quotes & Bid vs Ask)
  // Beat 3: 9.5s - 14.5s (Spread gap caliper)
  // Beat 4: 14.5s - 20.8s (MM execution at $100.01)
  // Beat 5: 20.8s - 28.8s (Stock surges to $100.10)
  // Beat 6: 28.8s - 33.8s (Lucky vs Informed)
  // Beat 7: 33.8s - 42.4s (What does the trader know?)
  // Beat 8: 42.4s - 46.6s (Uncertainty premium)

  // Spring animations for scene transitions
  const b1Spring = spring({ frame, fps, config: { damping: 14, stiffness: 100 } });
  const b3Spring = spring({ frame: frame - Math.floor(9.5 * fps), fps, config: { damping: 14 } });
  const b4Spring = spring({ frame: frame - Math.floor(14.5 * fps), fps, config: { damping: 14 } });
  const b5Spring = spring({ frame: frame - Math.floor(20.8 * fps), fps, config: { damping: 13, stiffness: 120 } });
  const b6Spring = spring({ frame: frame - Math.floor(28.8 * fps), fps, config: { damping: 14 } });
  const b7Spring = spring({ frame: frame - Math.floor(33.8 * fps), fps, config: { damping: 14 } });
  const b8Spring = spring({ frame: frame - Math.floor(42.4 * fps), fps, config: { damping: 14 } });

  // Price surge for Beat 5 (21.0s to 24.5s: 100.01 -> 100.10)
  const currentStockPrice = interpolate(currentTime, [21.0, 24.0], [100.01, 100.10], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

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
      <Audio src={staticFile("audio/short01_why_spread_exists_vo.mp3")} volume={1.0} />

      {/* Main Canvas with camera push */}
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
            <pattern id="grid01" width="60" height="60" patternUnits="userSpaceOnUse">
              <path d="M 60 0 L 0 0 0 60" fill="none" stroke={BORDER} strokeWidth="1" />
            </pattern>
          </defs>
          <rect width="1080" height="1920" fill="url(#grid01)" />
        </svg>

        {/* Top Header Telemetry (y: 120px) */}
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
              QUANTROVE // MICROSTRUCTURE
            </span>
          </div>
          <span style={{ fontSize: 18, color: BORDER, fontWeight: 600 }}>
            EP06.01 · L2 ORDER BOOK
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
          {/* BEAT 1, 2, 3: Dual Quotes & The Spread Gap [0.0s - 14.5s] */}
          {currentTime < 14.5 && (
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
                  fontSize: 20,
                  fontWeight: 600,
                  color: TEXT,
                  marginBottom: 24,
                  display: "flex",
                  alignItems: "center",
                  gap: 8,
                }}
              >
                <span>TICKER:</span>
                <span style={{ color: LIME, fontWeight: 700 }}>NVDA</span>
                <span style={{ color: BORDER }}>|</span>
                <span style={{ fontSize: 16, color: "#8E9E9C" }}>REAL-TIME BBO</span>
              </div>

              {/* Dual Quote Cards Container */}
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  width: "100%",
                  gap: 20,
                  position: "relative",
                }}
              >
                {/* BID CARD */}
                <div
                  style={{
                    flex: 1,
                    backgroundColor: CARD_BG,
                    borderRadius: 16,
                    border: `2px solid ${
                      currentTime >= 3.5 && currentTime < 6.2 ? LIME : BORDER
                    }`,
                    padding: "32px 24px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    transform:
                      currentTime >= 3.5 && currentTime < 6.2 ? "scale(1.03)" : "scale(1.0)",
                    transition: "all 0.25s ease",
                    boxShadow:
                      currentTime >= 3.5 && currentTime < 6.2
                        ? "0 0 30px rgba(195, 216, 9, 0.15)"
                        : "none",
                  }}
                >
                  <span style={{ fontSize: 22, fontWeight: 700, color: LIME, letterSpacing: "0.05em" }}>
                    BID
                  </span>
                  <span style={{ fontSize: 62, fontWeight: 700, margin: "12px 0", color: TEXT }}>
                    $100.00
                  </span>
                  <span
                    style={{
                      fontSize: 16,
                      fontWeight: 600,
                      color: currentTime >= 3.5 && currentTime < 6.2 ? LIME : "#7A8C8A",
                      textAlign: "center",
                    }}
                  >
                    {currentTime >= 3.5 && currentTime < 6.2
                      ? "SELLERS RECEIVE THIS"
                      : "4,200 SHARES WAITING"}
                  </span>
                </div>

                {/* ASK CARD */}
                <div
                  style={{
                    flex: 1,
                    backgroundColor: CARD_BG,
                    borderRadius: 16,
                    border: `2px solid ${
                      currentTime >= 6.2 && currentTime < 9.5 ? TEXT : BORDER
                    }`,
                    padding: "32px 24px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    transform:
                      currentTime >= 6.2 && currentTime < 9.5 ? "scale(1.03)" : "scale(1.0)",
                    transition: "all 0.25s ease",
                    boxShadow:
                      currentTime >= 6.2 && currentTime < 9.5
                        ? "0 0 30px rgba(230, 237, 243, 0.15)"
                        : "none",
                  }}
                >
                  <span style={{ fontSize: 22, fontWeight: 700, color: TEXT, letterSpacing: "0.05em" }}>
                    ASK
                  </span>
                  <span style={{ fontSize: 62, fontWeight: 700, margin: "12px 0", color: TEXT }}>
                    $100.01
                  </span>
                  <span
                    style={{
                      fontSize: 16,
                      fontWeight: 600,
                      color: currentTime >= 6.2 && currentTime < 9.5 ? TEXT : "#7A8C8A",
                      textAlign: "center",
                    }}
                  >
                    {currentTime >= 6.2 && currentTime < 9.5
                      ? "BUYERS MUST PAY THIS"
                      : "3,100 SHARES OFFERED"}
                  </span>
                </div>
              </div>

              {/* SPREAD MEASUREMENT CALIPER (Beat 3: 9.5s - 14.5s) */}
              {currentTime >= 9.5 && (
                <div
                  style={{
                    marginTop: 36,
                    width: "100%",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    opacity: b3Spring,
                    transform: `translateY(${interpolate(b3Spring, [0, 1], [20, 0])}px)`,
                  }}
                >
                  <div
                    style={{
                      display: "flex",
                      alignItems: "center",
                      gap: 16,
                      width: "80%",
                      justifyContent: "center",
                    }}
                  >
                    <div style={{ flex: 1, height: 2, backgroundColor: LIME }} />
                    <div
                      style={{
                        backgroundColor: CARD_BG,
                        border: `2px solid ${LIME}`,
                        borderRadius: 30,
                        padding: "10px 24px",
                        display: "flex",
                        alignItems: "center",
                        gap: 10,
                      }}
                    >
                      <span style={{ fontSize: 22, fontWeight: 700, color: LIME }}>
                        SPREAD GAP: $0.01
                      </span>
                    </div>
                    <div style={{ flex: 1, height: 2, backgroundColor: LIME }} />
                  </div>
                  <span
                    style={{
                      marginTop: 14,
                      fontSize: 20,
                      fontWeight: 600,
                      color: "#A2B4B2",
                      letterSpacing: "0.02em",
                    }}
                  >
                    WHY DOES THIS 1-CENT GAP EXIST?
                  </span>
                </div>
              )}
            </div>
          )}

          {/* BEAT 4: Market Maker Quoting & Buyer Takes Ask [14.5s - 20.8s] */}
          {currentTime >= 14.5 && currentTime < 20.8 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `1px solid ${BORDER}`,
                padding: "36px 30px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b4Spring,
                transform: `scale(${interpolate(b4Spring, [0, 1], [0.95, 1.0])})`,
              }}
            >
              <div
                style={{
                  fontSize: 18,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.08em",
                  marginBottom: 10,
                }}
              >
                YOUR ROLE: MARKET MAKER
              </div>
              <div style={{ fontSize: 26, fontWeight: 700, textAlign: "center", marginBottom: 30 }}>
                You Quote the Ask at <span style={{ color: LIME }}>$100.01</span>
              </div>

              {/* Execution Graphic */}
              <div
                style={{
                  width: "100%",
                  height: 180,
                  backgroundColor: BG,
                  borderRadius: 14,
                  border: `1px solid ${BORDER}`,
                  position: "relative",
                  overflow: "hidden",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                {/* Incoming Buyer Order Packet */}
                <div
                  style={{
                    position: "absolute",
                    top: interpolate(currentTime, [17.0, 18.2], [10, 80], {
                      extrapolateLeft: "clamp",
                      extrapolateRight: "clamp",
                    }),
                    padding: "8px 18px",
                    backgroundColor: currentTime >= 18.2 ? LIME : CARD_BG,
                    color: currentTime >= 18.2 ? BG : TEXT,
                    borderRadius: 20,
                    border: `1px solid ${LIME}`,
                    fontWeight: 700,
                    fontSize: 18,
                    display: "flex",
                    alignItems: "center",
                    gap: 8,
                    boxShadow: "0 0 20px rgba(195, 216, 9, 0.3)",
                  }}
                >
                  <span>BUY ORDER: 1,000 SHARES</span>
                  <span>➔</span>
                  <span>TAKES $100.01</span>
                </div>

                {currentTime >= 18.2 && (
                  <div
                    style={{
                      position: "absolute",
                      bottom: 24,
                      fontSize: 18,
                      fontWeight: 600,
                      color: LIME,
                    }}
                  >
                    ✓ TRADE EXECUTED · MM SHORT 1,000 SHARES
                  </div>
                )}
              </div>

              <div
                style={{
                  marginTop: 24,
                  display: "flex",
                  justifyContent: "space-between",
                  width: "100%",
                  fontSize: 18,
                  color: "#8E9E9C",
                }}
              >
                <span>CASH RECEIVED: +$100,010</span>
                <span>INVENTORY EXPOSURE: -1,000 SH</span>
              </div>
            </div>
          )}

          {/* BEAT 5: Stock Jumps to $100.10 — Adverse Selection [20.8s - 28.8s] */}
          {currentTime >= 20.8 && currentTime < 28.8 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `2px solid ${PUMPKIN}`,
                padding: "36px 30px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b5Spring,
                boxShadow: "0 0 40px rgba(253, 128, 46, 0.15)",
              }}
            >
              <div
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 10,
                  fontSize: 18,
                  fontWeight: 700,
                  color: PUMPKIN,
                  letterSpacing: "0.08em",
                  marginBottom: 10,
                }}
              >
                <span>⚠️ ADVERSE SELECTION WARNING</span>
              </div>

              <div style={{ fontSize: 24, fontWeight: 600, color: TEXT, marginBottom: 20 }}>
                Stock Jumps to:
              </div>

              {/* Big surging price display */}
              <div
                style={{
                  fontSize: 76,
                  fontWeight: 700,
                  color: PUMPKIN,
                  fontFamily: "'Nohemi', 'Inter', sans-serif",
                  letterSpacing: "-0.03em",
                }}
              >
                ${currentStockPrice.toFixed(2)}
              </div>

              <div
                style={{
                  fontSize: 20,
                  fontWeight: 600,
                  color: LIME,
                  backgroundColor: "rgba(195, 216, 9, 0.1)",
                  padding: "6px 18px",
                  borderRadius: 14,
                  marginTop: 10,
                }}
              >
                BUYER PROFIT: +$0.09 / SHARE (+$90.00)
              </div>

              <div
                style={{
                  marginTop: 26,
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 12,
                  padding: "16px 20px",
                  border: `1px solid ${BORDER}`,
                  display: "flex",
                  justifyContent: "space-between",
                  fontSize: 18,
                }}
              >
                <span style={{ color: "#8E9E9C" }}>Your Sold Price: $100.01</span>
                <span style={{ color: PUMPKIN, fontWeight: 700 }}>MM Loss: -$90.00</span>
              </div>
            </div>
          )}

          {/* BEAT 6: Lucky vs Informed Asymmetry [28.8s - 33.8s] */}
          {currentTime >= 28.8 && currentTime < 33.8 && (
            <div
              style={{
                width: "100%",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b6Spring,
                transform: `scale(${interpolate(b6Spring, [0, 1], [0.94, 1.0])})`,
              }}
            >
              <div
                style={{
                  fontSize: 22,
                  fontWeight: 700,
                  color: TEXT,
                  marginBottom: 28,
                  letterSpacing: "0.02em",
                }}
              >
                WHY DID THE BUYER TAKE THAT TRADE?
              </div>

              <div style={{ display: "flex", width: "100%", gap: 20 }}>
                {/* Hypothesis A: Lucky */}
                <div
                  style={{
                    flex: 1,
                    backgroundColor: CARD_BG,
                    border: `1px solid ${BORDER}`,
                    borderRadius: 16,
                    padding: "30px 20px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    opacity: 0.45,
                  }}
                >
                  <span style={{ fontSize: 36, marginBottom: 12 }}>🎲</span>
                  <span style={{ fontSize: 22, fontWeight: 700, color: TEXT, marginBottom: 8 }}>
                    PURE LUCK
                  </span>
                  <span style={{ fontSize: 16, color: "#8E9E9C", textAlign: "center" }}>
                    Random retail buyer. Coincidental timing.
                  </span>
                </div>

                {/* Hypothesis B: Informed */}
                <div
                  style={{
                    flex: 1,
                    backgroundColor: CARD_BG,
                    border: `2px solid ${LIME}`,
                    borderRadius: 16,
                    padding: "30px 20px",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    boxShadow: "0 0 35px rgba(195, 216, 9, 0.2)",
                  }}
                >
                  <span style={{ fontSize: 36, marginBottom: 12 }}>⚡</span>
                  <span style={{ fontSize: 22, fontWeight: 700, color: LIME, marginBottom: 8 }}>
                    INFORMED TRADER
                  </span>
                  <span style={{ fontSize: 16, color: TEXT, textAlign: "center", fontWeight: 600 }}>
                    They knew the stock was moving before you did.
                  </span>
                </div>
              </div>
            </div>
          )}

          {/* BEAT 7: What does the other trader know? [33.8s - 42.4s] */}
          {currentTime >= 33.8 && currentTime < 42.4 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `1px solid ${BORDER}`,
                padding: "44px 32px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b7Spring,
                transform: `scale(${interpolate(b7Spring, [0, 1], [0.94, 1.0])})`,
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.1em",
                  marginBottom: 16,
                }}
              >
                THE MARKET MAKER'S CONSTANT RISK
              </div>

              <div
                style={{
                  fontSize: 40,
                  fontWeight: 700,
                  textAlign: "center",
                  lineHeight: 1.25,
                  color: TEXT,
                  marginBottom: 28,
                  maxWidth: 680,
                }}
              >
                "What does the other trader <span style={{ color: LIME }}>know</span>?"
              </div>

              {/* Informational Radar Scanner Graphic */}
              <div
                style={{
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 12,
                  border: `1px solid ${BORDER}`,
                  padding: "20px 24px",
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                }}
              >
                <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                  <div
                    style={{
                      width: 12,
                      height: 12,
                      borderRadius: "50%",
                      backgroundColor: PUMPKIN,
                    }}
                  />
                  <span style={{ fontSize: 18, fontWeight: 600, color: TEXT }}>
                    INFORMATION ASYMMETRY
                  </span>
                </div>
                <span style={{ fontSize: 18, color: LIME, fontWeight: 700 }}>
                  TOXIC FLOW RISK
                </span>
              </div>
            </div>
          )}

          {/* BEAT 8: Uncertainty Premium in Spread Formula [42.4s - 46.6s] */}
          {currentTime >= 42.4 && (
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
                opacity: b8Spring,
                boxShadow: "0 0 50px rgba(195, 216, 9, 0.25)",
              }}
            >
              <div
                style={{
                  fontSize: 18,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.08em",
                  marginBottom: 12,
                }}
              >
                MICROSTRUCTURE PAYOFF
              </div>

              <div style={{ fontSize: 32, fontWeight: 700, color: TEXT, marginBottom: 24, textAlign: "center" }}>
                The True Anatomy of the Spread
              </div>

              {/* Formula Stack */}
              <div
                style={{
                  display: "flex",
                  flexDirection: "column",
                  gap: 12,
                  width: "100%",
                }}
              >
                <div
                  style={{
                    backgroundColor: BG,
                    borderRadius: 10,
                    padding: "14px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    fontSize: 18,
                    color: "#8E9E9C",
                    border: `1px solid ${BORDER}`,
                  }}
                >
                  <span>1. Inventory Holding Risk</span>
                  <span>Baseline</span>
                </div>

                <div
                  style={{
                    backgroundColor: BG,
                    borderRadius: 10,
                    padding: "14px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    fontSize: 18,
                    color: "#8E9E9C",
                    border: `1px solid ${BORDER}`,
                  }}
                >
                  <span>2. Operational & Exchange Fees</span>
                  <span>Baseline</span>
                </div>

                <div
                  style={{
                    backgroundColor: "rgba(195, 216, 9, 0.15)",
                    borderRadius: 10,
                    padding: "16px 20px",
                    display: "flex",
                    justifyContent: "space-between",
                    fontSize: 20,
                    fontWeight: 700,
                    color: LIME,
                    border: `1px solid ${LIME}`,
                  }}
                >
                  <span>3. UNCERTAINTY PREMIUM</span>
                  <span>+ ASYMMETRY</span>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Captions Layer in Safe Text Band (y: 1180px) */}
        <CaptionsLayer chunks={captionChunks} topY={1160} />
      </div>
    </AbsoluteFill>
  );
};
