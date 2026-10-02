import React from "react";
import { AbsoluteFill, Audio, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { ShortsV2TextLayer, TextEvent, FONT_FAMILY } from "./ShortsV2TextLayer";
import { PALETTE, TYPOGRAPHY } from "./brandTokens";

export interface WordTiming {
  word: string;
  start: number;
  end: number;
}

export interface SceneBeat {
  id: number;
  startSec: number;
  endSec: number;
  badge: string;
  headline: string;
  subtext: string;
  accentColor: string;
  type: string;
}

export interface ShortVideoProps {
  title: string;
  statCallout?: string;
  audioFileName: string;
  words: WordTiming[];
  scenes: SceneBeat[];
  style?: string;
  textEvents?: TextEvent[];
  overlayOnly?: boolean;
}

export const ShortVideo: React.FC<ShortVideoProps> = ({
  title = "HOW NVIDIA WON AI",
  statCallout = "80% AI MONOPOLY",
  audioFileName = "voiceover.mp3",
  words = [],
  scenes = [],
  style,
  textEvents = [],
  overlayOnly = false,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const currentTime = frame / fps;

  // Transparent Alpha Overlay Mode (CapCut Track V2)
  if (overlayOnly) {
    return (
      <AbsoluteFill
        style={{
          backgroundColor: "transparent",
          fontFamily: FONT_FAMILY,
          overflow: "hidden",
        }}
      >
        <ShortsV2TextLayer textEvents={textEvents} words={words} />
      </AbsoluteFill>
    );
  }

  const progress = (frame / durationInFrames) * 100;
  const gridY = interpolate(frame, [0, durationInFrames], [0, 140]);

  // Find active scene dynamically based on real audio timestamps
  const activeScene = scenes.find((s) => currentTime >= s.startSec && currentTime < s.endSec) || scenes[0];

  // Persistent Active Word Tracker (Never null between words)
  let activeWordIndex = words.findIndex((w, i) => {
    const nextStart = words[i + 1] ? words[i + 1].start : w.end + 0.5;
    return currentTime >= w.start && currentTime < nextStart;
  });
  if (activeWordIndex === -1 && words.length > 0) {
    activeWordIndex = currentTime > words[words.length - 1].end ? words.length - 1 : 0;
  }
  const activeWord = words[activeWordIndex];

  // Scene punch-in spring
  const sceneSpring = activeScene
    ? spring({ frame: (currentTime - activeScene.startSec) * fps, fps, config: { damping: 12 } })
    : 1;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: PALETTE.BACKGROUND,
        fontFamily: FONT_FAMILY,
        color: PALETTE.TEXT,
        overflow: "hidden",
      }}
    >
      {/* --- AUDIO MIX LAYER --- */}
      <Audio src={staticFile(audioFileName)} volume={1.0} />
      <Audio src={staticFile("bg_music.wav")} volume={0.22} />

      {/* Trigger Whoosh SFX at every dynamic scene cut */}
      {scenes.map((s, idx) => (
        <Sequence key={idx} from={Math.floor(s.startSec * fps)} durationInFrames={15}>
          <Audio src={staticFile("whoosh.wav")} volume={0.65} />
        </Sequence>
      ))}

      {/* --- TOP PROGRESS BAR --- */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: `${progress}%`,
          height: 14,
          backgroundColor: PALETTE.SUCCESS,
          boxShadow: `0 0 25px ${PALETTE.SUCCESS}`,
          zIndex: 100,
        }}
      />

      {/* --- BACKGROUND TECH GRID --- */}
      <div
        style={{
          position: "absolute",
          inset: -100,
          backgroundImage:
            `linear-gradient(to right, ${PALETTE.UI_STRUCTURE}40 1px, transparent 1px), linear-gradient(to bottom, ${PALETTE.UI_STRUCTURE}40 1px, transparent 1px)`,
          backgroundSize: "55px 55px",
          transform: `translateY(${gridY}px)`,
        }}
      />

      {/* ========================================================================= */}
      {/* DYNAMIC SCENE CONTAINER (SYNCHRONIZED DIRECTLY TO AUDIO TIMESTAMPS) */}
      {/* ========================================================================= */}
      {activeScene && (
        <AbsoluteFill
          key={activeScene.id}
          style={{
            justifyContent: "center",
            alignItems: "center",
            padding: 40,
            transform: `scale(${0.9 + sceneSpring * 0.1})`,
          }}
        >
          {/* Top Badge */}
          <div
            style={{
              position: "absolute",
              top: 140,
              backgroundColor: activeScene.accentColor || PALETTE.SUCCESS,
              color: PALETTE.BACKGROUND,
              fontWeight: TYPOGRAPHY.weights.bold,
              fontSize: 24,
              padding: "10px 30px",
              borderRadius: 40,
              letterSpacing: 2,
              textTransform: "uppercase",
              boxShadow: `0 0 35px ${activeScene.accentColor || PALETTE.SUCCESS}`,
            }}
          >
            {activeScene.badge}
          </div>

          {/* Main Content Card */}
          <div
            style={{
              width: "100%",
              maxWidth: 920,
              backgroundColor: PALETTE.BACKGROUND,
              border: `3px solid ${activeScene.accentColor || PALETTE.UI_STRUCTURE}`,
              borderRadius: 32,
              padding: "44px 36px",
              textAlign: "center",
              boxShadow: `0 30px 70px rgba(0,0,0,0.8), 0 0 30px ${PALETTE.UI_STRUCTURE}55`,
              backdropFilter: "blur(15px)",
            }}
          >
            <div
              style={{
                fontSize: activeScene.type === "payoff" || activeScene.type === "monopoly" ? 82 : 48,
                fontWeight: TYPOGRAPHY.weights.bold,
                color: PALETTE.TEXT,
                lineHeight: 1.15,
                textTransform: "uppercase",
                textShadow: "0 4px 25px rgba(0,0,0,0.9)",
              }}
            >
              {activeScene.headline}
            </div>

            {/* Dynamic SVG Chart if scene type is chart */}
            {activeScene.type === "chart" && (
              <div style={{ marginTop: 24, marginBottom: 12 }}>
                <svg width="100%" height="160" viewBox="0 0 800 160" style={{ overflow: "visible" }}>
                  <path
                    d="M 20 140 Q 200 130, 360 100 T 600 50 T 780 10"
                    fill="none"
                    stroke={PALETTE.SUCCESS}
                    strokeWidth="10"
                    strokeLinecap="round"
                  />
                </svg>
              </div>
            )}

            <div
              style={{
                marginTop: 20,
                fontSize: 28,
                color: PALETTE.TEXT,
                opacity: 0.75,
                fontWeight: TYPOGRAPHY.weights.medium,
                letterSpacing: 1,
              }}
            >
              {activeScene.subtext}
            </div>
          </div>
        </AbsoluteFill>
      )}

      {/* ========================================================================= */}
      {/* CAPTIONS: SHORTS V2 TEXT LAYER OR LEGACY BURNED-IN KINETIC CAPTIONS */}
      {/* ========================================================================= */}
      {style === "shorts_v2" ? (
        <ShortsV2TextLayer textEvents={textEvents} words={words} />
      ) : (
        <div
          style={{
            position: "absolute",
            bottom: 180,
            left: 40,
            right: 40,
            height: 180,
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: 90,
          }}
        >
          {activeWord ? (
            <div
              key={activeWord.start}
              style={{
                fontSize: 78,
                fontWeight: TYPOGRAPHY.weights.bold,
                color: PALETTE.BACKGROUND,
                backgroundColor: PALETTE.SUCCESS,
                padding: "16px 40px",
                borderRadius: 22,
                textTransform: "uppercase",
                boxShadow: `0 0 50px ${PALETTE.SUCCESS}99`,
                letterSpacing: 2,
                transform: `scale(${spring({ frame: (currentTime - activeWord.start) * fps, fps, config: { damping: 10 } }) * 1.06})`,
              }}
            >
              {activeWord.word}
            </div>
          ) : null}
        </div>
      )}
    </AbsoluteFill>
  );
};
