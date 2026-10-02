import React from "react";
import {
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  Easing,
} from "remotion";

// Quantrove Institutional Data Intelligence Palette
const BACKGROUND = "#202322";
const CARD_FILL = "#161B22";
const UI_STRUCTURE = "#233D4C";
const SUCCESS = "#C3D809";
const RISK = "#FD802E";
const TEXT = "#E6EDF3";

export const OrderRoutingBenchmark: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // ---------------------------------------------------------
  // CAMERA PUSH: Restrained 1.00 -> 1.045 scale in final 3 seconds
  // ---------------------------------------------------------
  const cameraScale = interpolate(frame, [360, 540], [1.0, 1.045], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  // ---------------------------------------------------------
  // BEAT 1: [Frames 0 - 90 / 0.0s - 1.5s] System & Broker Node In
  // ---------------------------------------------------------
  const headerSpring = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 100 },
  });
  const headerY = interpolate(headerSpring, [0, 1], [-50, 0]);
  const headerOpacity = interpolate(headerSpring, [0, 1], [0, 1]);

  const brokerSpring = spring({
    frame: frame - 15,
    fps,
    config: { damping: 13, stiffness: 110 },
  });
  const brokerY = interpolate(brokerSpring, [0, 1], [-70, 0]);
  const brokerOpacity = interpolate(brokerSpring, [0, 1], [0, 1]);

  // Order packets traveling into broker
  const packet1Prog = interpolate(frame, [10, 55], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const packet2Prog = interpolate(frame, [30, 75], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  // ---------------------------------------------------------
  // BEAT 2: [Frames 90 - 240 / 1.5s - 4.0s] Bifurcation & Bypassed Gate
  // ---------------------------------------------------------
  const routesSpring = spring({
    frame: frame - 75,
    fps,
    config: { damping: 14, stiffness: 95 },
  });
  const routesOpacity = interpolate(routesSpring, [0, 1], [0, 1]);
  const routesScale = interpolate(routesSpring, [0, 1], [0.94, 1.0]);

  // Public Route Bypass Animation (Frames 120 - 160)
  const bypassFlash = interpolate(frame, [120, 132, 145], [0, 1, 0.85], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const publicRouteDim = interpolate(frame, [120, 140], [1, 0.4], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Wholesale Route Active Flow Pulse (Frames 120 - 240)
  const flowDashOffset = (frame * 7) % 60;
  const wholesalePulse = Math.sin(frame * 0.12) * 0.03 + 0.99;

  // ---------------------------------------------------------
  // BEAT 3: [Frames 240 - 390 / 4.0s - 6.5s] Execution Quality Spread Card
  // ---------------------------------------------------------
  const spreadSpring = spring({
    frame: frame - 220,
    fps,
    config: { damping: 13, stiffness: 105 },
  });
  const spreadY = interpolate(spreadSpring, [0, 1], [80, 0]);
  const spreadOpacity = interpolate(spreadSpring, [0, 1], [0, 1]);

  // Numeric ticker: $100.00 -> $100.02
  const priceScrub = interpolate(frame, [250, 310], [100.0, 100.02], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const priceText = `$${priceScrub.toFixed(2)}`;

  // ---------------------------------------------------------
  // BEAT 4: [Frames 390 - 540 / 6.5s - 9.0s] SEC Finding Payoff
  // ---------------------------------------------------------
  const findingSpring = spring({
    frame: frame - 370,
    fps,
    config: { damping: 14, stiffness: 110 },
  });
  const findingY = interpolate(findingSpring, [0, 1], [60, 0]);
  const findingOpacity = interpolate(findingSpring, [0, 1], [0, 1]);
  const findingScale = interpolate(findingSpring, [0, 1], [0.96, 1.0]);

  return (
    <div
      style={{
        width: 1080,
        height: 1920,
        backgroundColor: BACKGROUND,
        color: TEXT,
        fontFamily: "'Nohemi', 'Inter', -apple-system, sans-serif",
        overflow: "hidden",
        position: "relative",
      }}
    >
      {/* BACKGROUND TELEMETRY GRID */}
      <svg
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: 1080,
          height: 1920,
          opacity: 0.22,
          pointerEvents: "none",
        }}
      >
        <defs>
          <pattern
            id="bench-grid"
            width="60"
            height="60"
            patternUnits="userSpaceOnUse"
          >
            <path
              d="M 60 0 L 0 0 0 60"
              fill="none"
              stroke={UI_STRUCTURE}
              strokeWidth="1"
            />
          </pattern>
        </defs>
        <rect width="1080" height="1920" fill="url(#bench-grid)" />
        <circle cx="540" cy="960" r="4" fill={UI_STRUCTURE} />
        <line
          x1="510"
          y1="960"
          x2="570"
          y2="960"
          stroke={UI_STRUCTURE}
          strokeWidth="1"
        />
        <line
          x1="540"
          y1="930"
          x2="540"
          y2="990"
          stroke={UI_STRUCTURE}
          strokeWidth="1"
        />
      </svg>

      {/* MAIN MOTION WRAPPER (Controlled Camera Scale) */}
      <div
        style={{
          width: "100%",
          height: "100%",
          transform: `scale(${cameraScale})`,
          transformOrigin: "540px 1100px",
          position: "relative",
        }}
      >
        {/* TOP STATUS BAR & HEADER */}
        <div
          style={{
            position: "absolute",
            top: 130,
            left: 70,
            right: 70,
            transform: `translateY(${headerY}px)`,
            opacity: headerOpacity,
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            borderBottom: `1.5px solid ${UI_STRUCTURE}`,
            paddingBottom: 16,
          }}
        >
          <div>
            <div
              style={{
                fontSize: 14,
                fontWeight: 700,
                letterSpacing: "0.15em",
                color: SUCCESS,
                textTransform: "uppercase",
              }}
            >
              ORDER ROUTING ARCHITECTURE
            </div>
            <div
              style={{
                fontSize: 26,
                fontWeight: 700,
                color: TEXT,
                marginTop: 4,
              }}
            >
              THE SEC ORDER FLOW INQUIRY
            </div>
          </div>
          <div
            style={{
              padding: "8px 16px",
              borderRadius: 6,
              border: `1.5px solid ${UI_STRUCTURE}`,
              backgroundColor: "rgba(35, 61, 76, 0.4)",
              fontSize: 13,
              fontWeight: 700,
              color: TEXT,
              letterSpacing: "0.08em",
            }}
          >
            BEAT 03 // 60 FPS
          </div>
        </div>

        {/* 1. RETAIL BROKER NODE (Top Center) */}
        <div
          style={{
            position: "absolute",
            top: 250,
            left: 100,
            right: 100,
            transform: `translateY(${brokerY}px)`,
            opacity: brokerOpacity,
            backgroundColor: CARD_FILL,
            border: `2px solid ${UI_STRUCTURE}`,
            borderRadius: 16,
            padding: "24px 28px",
            boxShadow: "0 20px 40px rgba(0,0,0,0.5)",
          }}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div>
              <div
                style={{
                  fontSize: 13,
                  fontWeight: 700,
                  letterSpacing: "0.1em",
                  color: "rgba(230, 237, 243, 0.7)",
                }}
              >
                CUSTOMER ENTRY POINT
              </div>
              <div
                style={{
                  fontSize: 28,
                  fontWeight: 700,
                  color: TEXT,
                  marginTop: 2,
                }}
              >
                RETAIL BROKER NODE
              </div>
            </div>
            <div
              style={{
                padding: "8px 16px",
                borderRadius: 8,
                backgroundColor: "rgba(195, 216, 9, 0.15)",
                border: `1.5px solid ${SUCCESS}`,
                color: SUCCESS,
                fontSize: 14,
                fontWeight: 700,
              }}
            >
              $0 COMMISSION
            </div>
          </div>

          {/* Incoming order packet stream visualization */}
          <div
            style={{
              marginTop: 18,
              padding: "12px 18px",
              borderRadius: 8,
              backgroundColor: "#10131A",
              border: `1px dashed ${UI_STRUCTURE}`,
              display: "flex",
              justifyContent: "space-between",
              fontSize: 14,
              fontFamily: "monospace",
              color: TEXT,
            }}
          >
            <span>ORDER #84920: BUY 100 SHARES</span>
            <span style={{ color: SUCCESS, fontWeight: 700 }}>
              ROUTING ACTIVE...
            </span>
          </div>
        </div>

        {/* 2. SVG CONDUITS / ROUTING PIPELINES */}
        <svg
          style={{
            position: "absolute",
            top: 420,
            left: 0,
            width: 1080,
            height: 380,
            pointerEvents: "none",
          }}
        >
          {/* Left Path: To Public Exchange */}
          <path
            d="M 540 20 C 540 130, 310 110, 310 250"
            fill="none"
            stroke={UI_STRUCTURE}
            strokeWidth="3.5"
            strokeDasharray={frame > 130 ? "8 6" : "none"}
            opacity={publicRouteDim}
          />

          {/* Right Path: To Wholesale Internalizer */}
          <path
            d="M 540 20 C 540 130, 770 110, 770 250"
            fill="none"
            stroke={SUCCESS}
            strokeWidth="4.5"
            strokeDasharray="18 10"
            strokeDashoffset={-flowDashOffset}
            opacity={routesOpacity}
          />

          {/* Dynamic Traveling Order Packet along Wholesale route */}
          {frame >= 105 && (
            <circle
              cx={540 + (770 - 540) * Math.min(1, (frame - 105) / 45)}
              cy={20 + (250 - 20) * Math.min(1, (frame - 105) / 45)}
              r="8"
              fill={SUCCESS}
            />
          )}
        </svg>

        {/* 3. DUAL ROUTING DESTINATIONS */}
        <div
          style={{
            position: "absolute",
            top: 670,
            left: 70,
            right: 70,
            display: "flex",
            gap: 30,
            opacity: routesOpacity,
            transform: `scale(${routesScale})`,
          }}
        >
          {/* LEFT: Public Exchange Route (Bypassed) */}
          <div
            style={{
              flex: 1,
              backgroundColor: CARD_FILL,
              border: `2px solid ${UI_STRUCTURE}`,
              borderRadius: 16,
              padding: 24,
              opacity: publicRouteDim,
              position: "relative",
              overflow: "hidden",
            }}
          >
            <div
              style={{
                fontSize: 12,
                fontWeight: 700,
                color: "rgba(230,237,243,0.6)",
                letterSpacing: "0.08em",
              }}
            >
              LIT MARKET
            </div>
            <div
              style={{
                fontSize: 22,
                fontWeight: 700,
                color: TEXT,
                marginTop: 4,
              }}
            >
              PUBLIC EXCHANGES
            </div>
            <div
              style={{
                fontSize: 13,
                color: "rgba(230,237,243,0.7)",
                marginTop: 2,
              }}
            >
              NYSE // NASDAQ
            </div>

            {/* Bypassed Stamp */}
            {frame >= 120 && (
              <div
                style={{
                  marginTop: 20,
                  padding: "10px 14px",
                  borderRadius: 8,
                  backgroundColor: "rgba(253, 128, 46, 0.18)",
                  border: `2.5px solid ${RISK}`,
                  color: RISK,
                  fontSize: 15,
                  fontWeight: 800,
                  letterSpacing: "0.12em",
                  textAlign: "center",
                  opacity: bypassFlash,
                  transform: "rotate(-3deg)",
                }}
              >
                BYPASSED
              </div>
            )}
          </div>

          {/* RIGHT: Wholesale Market Maker Route (Selected) */}
          <div
            style={{
              flex: 1,
              backgroundColor: "#152418",
              border: `2.5px solid ${SUCCESS}`,
              borderRadius: 16,
              padding: 24,
              transform: `scale(${wholesalePulse})`,
              boxShadow: "0 10px 30px rgba(195, 216, 9, 0.18)",
              position: "relative",
            }}
          >
            <div
              style={{
                fontSize: 12,
                fontWeight: 700,
                color: SUCCESS,
                letterSpacing: "0.08em",
              }}
            >
              INTERNALIZER ROUTE
            </div>
            <div
              style={{
                fontSize: 22,
                fontWeight: 700,
                color: TEXT,
                marginTop: 4,
              }}
            >
              WHOLESALE MMs
            </div>
            <div
              style={{
                fontSize: 13,
                color: "rgba(230,237,243,0.8)",
                marginTop: 2,
              }}
            >
              HIGHEST BIDDER
            </div>

            <div
              style={{
                marginTop: 20,
                padding: "10px 14px",
                borderRadius: 8,
                backgroundColor: "rgba(195, 216, 9, 0.22)",
                border: `2px solid ${SUCCESS}`,
                color: SUCCESS,
                fontSize: 15,
                fontWeight: 800,
                letterSpacing: "0.08em",
                textAlign: "center",
              }}
            >
              MAX PFOF PAYMENT
            </div>
          </div>
        </div>

        {/* 4. EXECUTION QUALITY DISPARITY (Mid Screen) */}
        <div
          style={{
            position: "absolute",
            top: 980,
            left: 70,
            right: 70,
            transform: `translateY(${spreadY}px)`,
            opacity: spreadOpacity,
            backgroundColor: "#1B1718",
            border: `2px solid ${RISK}`,
            borderRadius: 18,
            padding: 28,
            boxShadow: "0 20px 40px rgba(0,0,0,0.6)",
          }}
        >
          <div
            style={{
              fontSize: 13,
              fontWeight: 700,
              letterSpacing: "0.1em",
              color: RISK,
            }}
          >
            EXECUTION QUALITY REALITY
          </div>
          <div
            style={{
              fontSize: 26,
              fontWeight: 700,
              color: TEXT,
              marginTop: 4,
            }}
          >
            PRICE IMPROVEMENT ELIMINATED
          </div>

          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginTop: 24,
              padding: "18px 24px",
              backgroundColor: "#12141B",
              borderRadius: 12,
              border: `1.5px solid ${UI_STRUCTURE}`,
            }}
          >
            <div>
              <div
                style={{
                  fontSize: 13,
                  fontWeight: 600,
                  color: "rgba(230,237,243,0.7)",
                }}
              >
                NATIONAL BEST OFFER (NBBO)
              </div>
              <div
                style={{
                  fontSize: 30,
                  fontWeight: 700,
                  color: TEXT,
                  marginTop: 2,
                }}
              >
                $100.00
              </div>
            </div>

            <div style={{ fontSize: 26, color: UI_STRUCTURE }}>→</div>

            <div style={{ textAlign: "right" }}>
              <div style={{ fontSize: 13, fontWeight: 700, color: RISK }}>
                ROUTED FILL PRICE
              </div>
              <div
                style={{
                  fontSize: 34,
                  fontWeight: 800,
                  color: RISK,
                  marginTop: 2,
                }}
              >
                {priceText}
              </div>
            </div>
          </div>

          <div
            style={{
              marginTop: 18,
              display: "flex",
              justifyContent: "space-between",
              fontSize: 15,
              fontWeight: 700,
            }}
          >
            <span style={{ color: "rgba(230,237,243,0.7)" }}>
              HIDDEN SPREAD DRAG:
            </span>
            <span style={{ color: RISK }}>
              -$2.00 / 100 SHARES
            </span>
          </div>
        </div>

        {/* 5. SEC OFFICIAL FINDING (Bottom Safe Third) */}
        <div
          style={{
            position: "absolute",
            bottom: 150,
            left: 70,
            right: 70,
            transform: `translateY(${findingY}px) scale(${findingScale})`,
            opacity: findingOpacity,
            backgroundColor: "#22130D",
            border: `2.5px solid ${RISK}`,
            borderRadius: 18,
            padding: "26px 30px",
            boxShadow: "0 25px 50px rgba(0,0,0,0.8)",
          }}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <div
              style={{
                fontSize: 13,
                fontWeight: 700,
                letterSpacing: "0.15em",
                color: RISK,
              }}
            >
              OFFICIAL SEC PROCEEDING
            </div>
            <div
              style={{
                fontSize: 12,
                fontWeight: 700,
                padding: "4px 10px",
                borderRadius: 4,
                backgroundColor: RISK,
                color: BACKGROUND,
              }}
            >
              DECEMBER 2020
            </div>
          </div>

          <div
            style={{
              fontSize: 26,
              fontWeight: 700,
              color: TEXT,
              marginTop: 8,
              lineHeight: 1.25,
            }}
          >
            INFERIOR TRADE EXECUTION
          </div>

          <div
            style={{
              fontSize: 15,
              color: "rgba(230, 237, 243, 0.85)",
              marginTop: 8,
              lineHeight: 1.4,
            }}
          >
            Customers received worse execution prices than other brokers,
            quietly depriving investors of $34.1 million.
          </div>

          <div
            style={{
              marginTop: 18,
              paddingTop: 16,
              borderTop: `1px solid rgba(253, 128, 46, 0.35)`,
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <span
              style={{
                fontSize: 13,
                fontWeight: 700,
                color: "rgba(230,237,243,0.7)",
              }}
            >
              SETTLEMENT PENALTY:
            </span>
            <span
              style={{
                fontSize: 24,
                fontWeight: 800,
                color: RISK,
                letterSpacing: "0.05em",
              }}
            >
              $65,000,000
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
