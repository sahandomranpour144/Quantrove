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
import captionChunks from "../data/short03_caption_chunks.json";

// Quantrove Brand Palette
const BG = "#202322";
const CARD_BG = "#1A1E1D";
const BORDER = "#233D4C";
const LIME = "#C3D809";
const PUMPKIN = "#FD802E";
const TEXT = "#E6EDF3";

export const Short03WhyMachineChangesPrice: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // Camera subtle push (1.0 -> 1.035 across the video)
  const cameraScale = interpolate(currentTime, [0, 51.07], [1.0, 1.035], {
    extrapolateRight: "clamp",
  });

  // Scene springs:
  // Beat 1: 0.0s - 8.0s (AMM target inventory Q = 0)
  // Beat 2: 8.0s - 13.0s (Machine buys 3 units at $100)
  // Beat 3: 13.0s - 22.2s (Stock drops to $99.85, inventory risk)
  // Beat 4: 22.2s - 35.5s (Avellaneda-Stoikov formula & quote skew)
  // Beat 5: 35.5s - 44.0s (Volatility & time horizon sensitivity)
  // Beat 6: 44.0s - 51.07s (Stock hasn't changed, exposure has)

  const b1Spring = spring({ frame, fps, config: { damping: 14 } });
  const b2Spring = spring({ frame: frame - Math.floor(8.0 * fps), fps, config: { damping: 14 } });
  const b3Spring = spring({ frame: frame - Math.floor(13.0 * fps), fps, config: { damping: 13, stiffness: 120 } });
  const b4Spring = spring({ frame: frame - Math.floor(22.2 * fps), fps, config: { damping: 14 } });
  const b5Spring = spring({ frame: frame - Math.floor(35.5 * fps), fps, config: { damping: 14 } });
  const b6Spring = spring({ frame: frame - Math.floor(44.0 * fps), fps, config: { damping: 14 } });

  // Inventory count animation during Beat 2 (8.0s to 12.0s)
  const inventoryUnits = Math.min(
    3,
    Math.floor(interpolate(currentTime, [8.2, 11.5], [0, 3], { extrapolateRight: "clamp" }))
  );

  // Stock price drop during Beat 3 (13.5s to 16.0s: 100.00 -> 99.85)
  const currentPrice = interpolate(currentTime, [13.5, 16.0], [100.0, 99.85], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  // Tilting scale balance (-8 degrees tilt when Q=+3)
  const balanceTilt = interpolate(currentTime, [9.0, 12.5], [0, 8], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
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
      <Audio src={staticFile("audio/short03_why_machine_changes_price_vo.mp3")} volume={1.0} />

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
            <pattern id="grid03" width="60" height="60" patternUnits="userSpaceOnUse">
              <path d="M 60 0 L 0 0 0 60" fill="none" stroke={BORDER} strokeWidth="1" />
            </pattern>
          </defs>
          <rect width="1080" height="1920" fill="url(#grid03)" />
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
              QUANTROVE // INVENTORY RISK
            </span>
          </div>
          <span style={{ fontSize: 18, color: BORDER, fontWeight: 600 }}>
            AVELLANEDA-STOIKOV
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
          {/* BEAT 1 & 2: Inventory Accumulation & Scale Tilt [0.0s - 13.0s] */}
          {currentTime < 13.0 && (
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
                  marginBottom: 24,
                  display: "flex",
                  alignItems: "center",
                  gap: 8,
                }}
              >
                <span>AMM STATE:</span>
                <span style={{ color: LIME, fontWeight: 700 }}>INVENTORY MONITOR</span>
              </div>

              {/* Central Inventory HUD Card */}
              <div
                style={{
                  width: "100%",
                  backgroundColor: CARD_BG,
                  borderRadius: 20,
                  border: `2px solid ${currentTime >= 8.0 ? LIME : BORDER}`,
                  padding: "36px 30px",
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                }}
              >
                <span style={{ fontSize: 20, fontWeight: 600, color: "#8E9E9C" }}>
                  CURRENT STOCK INVENTORY (Q)
                </span>

                <div
                  style={{
                    fontSize: 84,
                    fontWeight: 700,
                    color: inventoryUnits > 0 ? LIME : TEXT,
                    margin: "12px 0",
                    fontFamily: "'Nohemi', 'Inter', sans-serif",
                  }}
                >
                  +{inventoryUnits} UNITS
                </div>

                {/* 3 Unit Visual Blocks */}
                <div style={{ display: "flex", gap: 14, margin: "16px 0" }}>
                  {[1, 2, 3].map((u) => (
                    <div
                      key={u}
                      style={{
                        width: 70,
                        height: 50,
                        borderRadius: 10,
                        border: `2px solid ${inventoryUnits >= u ? LIME : BORDER}`,
                        backgroundColor:
                          inventoryUnits >= u ? "rgba(195, 216, 9, 0.2)" : BG,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        fontSize: 18,
                        fontWeight: 700,
                        color: inventoryUnits >= u ? LIME : "#7A8C8A",
                        transition: "all 0.3s ease",
                      }}
                    >
                      {inventoryUnits >= u ? "UNIT" : "EMPTY"}
                    </div>
                  ))}
                </div>

                <div
                  style={{
                    marginTop: 16,
                    fontSize: 18,
                    color: "#8E9E9C",
                    display: "flex",
                    justifyContent: "space-between",
                    width: "100%",
                    borderTop: `1px solid ${BORDER}`,
                    paddingTop: 16,
                  }}
                >
                  <span>AVG ACQUISITION: $100.00</span>
                  <span style={{ color: LIME, fontWeight: 600 }}>
                    {inventoryUnits === 3 ? "LONG EXPOSURE ACTIVE" : "TARGET: 0 UNITS"}
                  </span>
                </div>
              </div>
            </div>
          )}

          {/* BEAT 3: Stock Moves Against It (-$0.15) [13.0s - 22.2s] */}
          {currentTime >= 13.0 && currentTime < 22.2 && (
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
                opacity: b3Spring,
                boxShadow: "0 0 40px rgba(253, 128, 46, 0.2)",
              }}
            >
              <div
                style={{
                  fontSize: 18,
                  fontWeight: 700,
                  color: PUMPKIN,
                  letterSpacing: "0.08em",
                  marginBottom: 10,
                }}
              >
                ⚠️ UNHEDGED INVENTORY AT RISK
              </div>

              <div style={{ fontSize: 24, fontWeight: 600, color: TEXT, marginBottom: 12 }}>
                Market Price Moves Down:
              </div>

              <div
                style={{
                  fontSize: 78,
                  fontWeight: 700,
                  color: PUMPKIN,
                  letterSpacing: "-0.03em",
                }}
              >
                ${currentPrice.toFixed(2)}
              </div>

              {/* Risk Exposure Details */}
              <div
                style={{
                  marginTop: 24,
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
                  <span style={{ color: "#8E9E9C" }}>Holding Position:</span>
                  <span style={{ color: TEXT, fontWeight: 700 }}>+3 Units</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 18 }}>
                  <span style={{ color: "#8E9E9C" }}>Mark-to-Market PnL:</span>
                  <span style={{ color: PUMPKIN, fontWeight: 700 }}>-$0.45 Unrealized</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between", fontSize: 18 }}>
                  <span style={{ color: "#8E9E9C" }}>Next Trade Constraint:</span>
                  <span style={{ color: PUMPKIN, fontWeight: 700 }}>Cannot Absorb More Buys</span>
                </div>
              </div>
            </div>
          )}

          {/* BEAT 4: Avellaneda-Stoikov Reservation Price Formula [22.2s - 35.5s] */}
          {currentTime >= 22.2 && currentTime < 35.5 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `2px solid ${LIME}`,
                padding: "36px 26px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b4Spring,
                boxShadow: "0 0 45px rgba(195, 216, 9, 0.2)",
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
                AVELLANEDA-STOIKOV (2008)
              </div>

              <div style={{ fontSize: 26, fontWeight: 700, color: TEXT, marginBottom: 20 }}>
                Reservation Price Model
              </div>

              {/* The Mathematical Formula */}
              <div
                style={{
                  backgroundColor: BG,
                  border: `1px solid ${BORDER}`,
                  borderRadius: 14,
                  padding: "20px 28px",
                  fontSize: 28,
                  fontWeight: 700,
                  color: TEXT,
                  letterSpacing: "0.02em",
                  textAlign: "center",
                  width: "100%",
                  marginBottom: 20,
                }}
              >
                r(s, q) = s -{" "}
                <span style={{ color: PUMPKIN }}>q · γ · σ² · (T - t)</span>
              </div>

              {/* Asymmetric Quote Skew Breakdown */}
              <div
                style={{
                  width: "100%",
                  display: "flex",
                  gap: 12,
                }}
              >
                <div
                  style={{
                    flex: 1,
                    backgroundColor: BG,
                    borderRadius: 12,
                    padding: "16px 14px",
                    border: `1px solid ${BORDER}`,
                    textAlign: "center",
                  }}
                >
                  <div style={{ fontSize: 14, color: "#8E9E9C" }}>NEW BID (DISCOURAGE)</div>
                  <div style={{ fontSize: 28, fontWeight: 700, color: PUMPKIN, marginTop: 4 }}>
                    $99.80
                  </div>
                  <div style={{ fontSize: 13, color: "#7A8C8A", marginTop: 4 }}>
                    Dropped to avoid buying
                  </div>
                </div>

                <div
                  style={{
                    flex: 1,
                    backgroundColor: BG,
                    borderRadius: 12,
                    padding: "16px 14px",
                    border: `1px solid ${LIME}`,
                    textAlign: "center",
                  }}
                >
                  <div style={{ fontSize: 14, color: LIME }}>NEW ASK (ATTRACTIVE)</div>
                  <div style={{ fontSize: 28, fontWeight: 700, color: LIME, marginTop: 4 }}>
                    $99.86
                  </div>
                  <div style={{ fontSize: 13, color: LIME, marginTop: 4 }}>
                    Aggressively offloading
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* BEAT 5: Volatility & Time Horizon Sensitivity [35.5s - 44.0s] */}
          {currentTime >= 35.5 && currentTime < 44.0 && (
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
                opacity: b5Spring,
              }}
            >
              <div
                style={{
                  fontSize: 16,
                  fontWeight: 700,
                  color: LIME,
                  letterSpacing: "0.1em",
                  marginBottom: 12,
                }}
              >
                PARAMETER SENSITIVITY
              </div>
              <div style={{ fontSize: 26, fontWeight: 700, color: TEXT, marginBottom: 24 }}>
                Dynamic Inventory Penalty
              </div>

              {/* Parameter 1: Volatility */}
              <div
                style={{
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 14,
                  padding: "18px 20px",
                  border: `1px solid ${BORDER}`,
                  marginBottom: 14,
                }}
              >
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
                  <span style={{ fontSize: 18, fontWeight: 700, color: PUMPKIN }}>
                    σ² (MARKET VOLATILITY)
                  </span>
                  <span style={{ fontSize: 16, color: PUMPKIN, fontWeight: 600 }}>
                    HIGH VOL ➔ EXPANDS PENALTY
                  </span>
                </div>
                <div style={{ width: "100%", height: 8, backgroundColor: CARD_BG, borderRadius: 4 }}>
                  <div style={{ width: "85%", height: 8, backgroundColor: PUMPKIN, borderRadius: 4 }} />
                </div>
              </div>

              {/* Parameter 2: Time Horizon */}
              <div
                style={{
                  width: "100%",
                  backgroundColor: BG,
                  borderRadius: 14,
                  padding: "18px 20px",
                  border: `1px solid ${BORDER}`,
                }}
              >
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8 }}>
                  <span style={{ fontSize: 18, fontWeight: 700, color: LIME }}>
                    (T - t) (TIME TO CLOSE)
                  </span>
                  <span style={{ fontSize: 16, color: LIME, fontWeight: 600 }}>
                    URGENCY TO UNWIND
                  </span>
                </div>
                <div style={{ width: "100%", height: 8, backgroundColor: CARD_BG, borderRadius: 4 }}>
                  <div style={{ width: "65%", height: 8, backgroundColor: LIME, borderRadius: 4 }} />
                </div>
              </div>
            </div>
          )}

          {/* BEAT 6: Final Microstructure Insight [44.0s - 51.07s] */}
          {currentTime >= 44.0 && (
            <div
              style={{
                width: "100%",
                backgroundColor: CARD_BG,
                borderRadius: 20,
                border: `2px solid ${LIME}`,
                padding: "44px 30px",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                opacity: b6Spring,
                boxShadow: "0 0 50px rgba(195, 216, 9, 0.25)",
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
                THE CORE INSIGHT
              </div>

              <div
                style={{
                  fontSize: 34,
                  fontWeight: 700,
                  color: TEXT,
                  textAlign: "center",
                  lineHeight: 1.3,
                  marginBottom: 28,
                }}
              >
                The stock hasn't changed.
                <br />
                <span style={{ color: LIME }}>The machine's exposure has.</span>
              </div>

              <div
                style={{
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
                <span style={{ color: "#8E9E9C" }}>Fundamentals: Flat</span>
                <span style={{ color: LIME, fontWeight: 700 }}>Quote Skew: 100% Inventory</span>
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
