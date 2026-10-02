import React, { useMemo, useEffect } from "react";
import { Easing, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig, delayRender, continueRender } from "remotion";
import { loadFont } from "@remotion/google-fonts/Inter";
import { PALETTE, TYPOGRAPHY, TEXT_COLOR_SCHEME } from "./brandTokens";

const { fontFamily: fallbackFontFamily } = loadFont("normal", {
  weights: ["500", "600", "700", "800"],
  subsets: ["latin"],
  ignoreTooManyRequestsWarning: true,
});

export const FONT_FAMILY = `"${TYPOGRAPHY.primary_font}", ${fallbackFontFamily}, sans-serif`;

const nohemiMediumUrl = staticFile("fonts/Nohemi-Medium.ttf");
const nohemiBoldUrl = staticFile("fonts/Nohemi-Bold.ttf");

const RISK_WORDS = new Set([
  "risk", "risks", "anomaly", "anomalies", "outlier", "outliers",
  "crash", "crashes", "loss", "losses", "downside", "drawdown",
  "liquidation", "liquidations", "panic", "toxic", "decay", "trap",
  "warning", "fail", "failure", "threat", "danger"
]);

export interface WordItem {
  word: string;
  start: number;
  end: number;
}

export interface TextEvent {
  start: number;
  end: number;
  words: WordItem[];
  type: "chunk" | "badge";
  y_pct: number;
  emphasis_word?: string | null;
}

export interface ShortsV2TextLayerProps {
  textEvents?: TextEvent[];
  words?: WordItem[];
  styleConfig?: any;
}

const STOP_WORDS = new Set(["the", "a", "an", "of", "to", "in", "on", "and", "or"]);

function autoGenerateChunks(words: WordItem[]): TextEvent[] {
  if (!words || words.length === 0) return [];
  const rawChunks: WordItem[][] = [];
  let curr: WordItem[] = [];

  for (let i = 0; i < words.length; i++) {
    const w = words[i];
    curr.push(w);
    const isLast = i === words.length - 1;
    const nextW = !isLast ? words[i + 1] : null;

    let shouldBreak = false;
    if (isLast) shouldBreak = true;
    else if (curr.length >= 4) shouldBreak = true;
    else if (nextW && nextW.start - w.end >= 0.25) shouldBreak = true;
    else if (/[.!?;\:]$/.test(w.word)) shouldBreak = true;

    const clean = w.word.replace(/[^\w]/g, "").toLowerCase();
    if (shouldBreak && !isLast && STOP_WORDS.has(clean)) {
      if (curr.length < 4 && nextW && nextW.start - w.end < 0.25) {
        shouldBreak = false;
      } else if (curr.length > 1) {
        curr.pop();
        rawChunks.push(curr);
        curr = [w];
        shouldBreak = false;
      }
    }

    if (shouldBreak && curr.length > 0) {
      rawChunks.push(curr);
      curr = [];
    }
  }
  if (curr.length > 0) rawChunks.push(curr);

  // Merge orphan non-emphasis lone words
  const merged: WordItem[][] = [];
  for (let i = 0; i < rawChunks.length; i++) {
    const c = rawChunks[i];
    const isSingle = c.length === 1;
    const isEmp = isSingle && /\d|[A-Z]{2,}|[$%]/.test(c[0].word);
    if (isSingle && !isEmp) {
      if (merged.length > 0 && merged[merged.length - 1].length + 1 <= 4) {
        merged[merged.length - 1].push(c[0]);
      } else if (i + 1 < rawChunks.length && rawChunks[i + 1].length + 1 <= 4) {
        rawChunks[i + 1].unshift(c[0]);
      } else {
        merged.push(c);
      }
    } else {
      merged.push(c);
    }
  }

  const events: TextEvent[] = [];
  for (let i = 0; i < merged.length; i++) {
    const c = merged[i];
    const startT = Math.max(0, Math.round((c[0].start - 0.02) * 1000) / 1000);
    let endT = Math.round(c[c.length - 1].end * 1000) / 1000;
    if (endT - startT < 0.7) {
      endT = Math.round((startT + 0.7) * 1000) / 1000;
    }

    let empWord: string | null = null;
    for (const w of c) {
      if (/\d|[A-Z]{2,}|[$%]/.test(w.word)) {
        empWord = w.word.replace(/[^\w]/g, "");
        break;
      }
    }

    events.push({
      start: startT,
      end: endT,
      words: c,
      type: "chunk",
      y_pct: 68,
      emphasis_word: empWord,
    });
  }

  // Eliminate overlaps
  for (let i = 0; i < events.length - 1; i++) {
    if (events[i].end > events[i + 1].start) {
      events[i].end = events[i + 1].start;
    }
  }

  return events;
}

export const ShortsV2TextLayer: React.FC<ShortsV2TextLayerProps> = ({
  textEvents = [],
  words = [],
  styleConfig,
}) => {
  const frame = useCurrentFrame();
  const { fps, height } = useVideoConfig();
  const currentTime = frame / fps;

  const resolvedEvents = useMemo(() => {
    if (textEvents && textEvents.length > 0) return textEvents;
    return autoGenerateChunks(words);
  }, [textEvents, words]);

  useEffect(() => {
    const handle = delayRender("Load Nohemi Font");
    const fontMedium = new FontFace("Nohemi", `url(${nohemiMediumUrl})`, { weight: "500", style: "normal" });
    const fontBold = new FontFace("Nohemi", `url(${nohemiBoldUrl})`, { weight: "700", style: "normal" });
    const fontExtraBold = new FontFace("Nohemi", `url(${nohemiBoldUrl})`, { weight: "800", style: "normal" });

    Promise.all([
      fontMedium.load().then((f) => document.fonts.add(f)),
      fontBold.load().then((f) => document.fonts.add(f)),
      fontExtraBold.load().then((f) => document.fonts.add(f)),
      document.fonts.ready,
    ])
      .then(() => {
        continueRender(handle);
      })
      .catch((err) => {
        console.warn("Nohemi font load error:", err);
        continueRender(handle);
      });
  }, []);

  const fontStyle = (
    <style>{`
      @font-face {
        font-family: 'Nohemi';
        src: url('${nohemiMediumUrl}') format('truetype');
        font-weight: 500;
        font-style: normal;
        font-display: block;
      }
      @font-face {
        font-family: 'Nohemi';
        src: url('${nohemiBoldUrl}') format('truetype');
        font-weight: 700;
        font-style: normal;
        font-display: block;
      }
      @font-face {
        font-family: 'Nohemi';
        src: url('${nohemiBoldUrl}') format('truetype');
        font-weight: 800;
        font-style: normal;
        font-display: block;
      }
    `}</style>
  );

  // Find active event at currentTime
  const activeEvent = resolvedEvents.find(
    (ev) => currentTime >= ev.start && currentTime < ev.end
  );

  if (!activeEvent) {
    return fontStyle;
  }

  // --- RENDER BADGE ---
  if (activeEvent.type === "badge") {
    const elapsedSec = currentTime - activeEvent.start;
    const badgeSpring = spring({
      frame: elapsedSec * fps,
      fps,
      config: { damping: 15, mass: 0.8 },
    });

    const slideX = interpolate(badgeSpring, [0, 1], [300, 0], {
      extrapolateRight: "clamp",
    });

    return (
      <React.Fragment>
        {fontStyle}
        <div
          style={{
            position: "absolute",
            top: `${activeEvent.y_pct ?? 47}%`,
            left: 0,
            right: 0,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: 95,
            pointerEvents: "none",
            transform: `translateX(${slideX}px)`,
          }}
        >
          <div
            style={{
              fontFamily: FONT_FAMILY,
              backgroundColor: PALETTE.TEXT,
              color: PALETTE.BACKGROUND,
              fontWeight: TYPOGRAPHY.weights.bold,
              fontSize: height * 0.038, // ~73px
              padding: "16px 36px",
              borderRadius: 6,
              letterSpacing: "-0.02em",
              textTransform: "uppercase",
              boxShadow: "none",
              display: "inline-block",
              textAlign: "center",
            }}
          >
            {activeEvent.words.map((w) => w.word).join(" ")}
          </div>
        </div>
      </React.Fragment>
    );
  }

  // --- RENDER CHUNK CAPTIONS ---
  const elapsedSec = currentTime - activeEvent.start;
  const animProgress = interpolate(elapsedSec, [0, 0.2], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.ease),
  });

  const translateY = interpolate(animProgress, [0, 1], [12, 0]);
  const opacity = animProgress;
  const blurPx = interpolate(animProgress, [0, 1], [4, 0]);

  const fontSize = height * 0.045; // 4.5% of frame height ~86px

  return (
    <React.Fragment>
      {fontStyle}
      <div
        style={{
          position: "absolute",
          top: `${activeEvent.y_pct ?? 68}%`,
          left: "10%",
          right: "10%",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          zIndex: 90,
          pointerEvents: "none",
          opacity,
          filter: blurPx > 0.1 ? `blur(${blurPx}px)` : "none",
          transform: `translateY(${translateY}px)`,
        }}
      >
        <div
          style={{
            fontFamily: FONT_FAMILY,
            fontSize,
            lineHeight: 1.25,
            letterSpacing: "-0.02em",
            textAlign: "center",
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
            gap: "14px",
            maxWidth: "90%",
          }}
        >
          {activeEvent.words.map((w, idx) => {
            const isSpoken = currentTime >= w.start;
            const cleanWord = w.word.replace(/[^\w]/g, "").toLowerCase();
            const isRisk =
              Boolean((activeEvent as any).is_risk) ||
              ((activeEvent as any).risk_word && cleanWord === (activeEvent as any).risk_word?.toLowerCase()) ||
              RISK_WORDS.has(cleanWord);
            const isEmphasis =
              !isRisk &&
              Boolean(activeEvent.emphasis_word) &&
              cleanWord === activeEvent.emphasis_word?.toLowerCase();

            const wordColor = isRisk
              ? PALETTE.RISK
              : isEmphasis
                ? PALETTE.SUCCESS
                : PALETTE.TEXT;
            const wordWeight = (isEmphasis || isRisk)
              ? TYPOGRAPHY.weights.bold
              : TYPOGRAPHY.weights.medium;
            const wordOpacity = isSpoken ? 1.0 : TEXT_COLOR_SCHEME.dim_opacity;

            return (
              <span
                key={idx}
                style={{
                  color: wordColor,
                  fontWeight: wordWeight,
                  opacity: wordOpacity,
                  transition: "opacity 0.05s ease-out",
                  display: "inline-block",
                }}
              >
                {w.word}
              </span>
            );
          })}
        </div>
      </div>
    </React.Fragment>
  );
};
