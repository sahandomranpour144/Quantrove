import React from "react";
import {
  Easing,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

export interface CaptionChunk {
  chunk_id: number;
  start: number;
  end: number;
  text: string;
  words: string[];
  highlightWord?: string | null;
  highlightColor?: string | null;
}

interface CaptionsLayerProps {
  chunks: CaptionChunk[];
  topY?: number;
}

export const CaptionsLayer: React.FC<CaptionsLayerProps> = ({
  chunks,
  topY = 1180,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;

  // Find active chunk
  const activeChunk = chunks.find(
    (c) => currentTime >= c.start && currentTime < c.end
  );

  if (!activeChunk) {
    return null;
  }

  const startFrame = Math.floor(activeChunk.start * fps);
  const elapsed = frame - startFrame;
  // Entrance duration: ~200ms (12 frames @ 60fps, 6 frames @ 30fps)
  const animFrames = Math.max(4, Math.round(0.2 * fps));

  const progress = interpolate(elapsed, [0, animFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const translateY = interpolate(progress, [0, 1], [14, 0]);
  const opacity = interpolate(progress, [0, 1], [0, 1]);
  const blur = interpolate(progress, [0, 1], [4, 0]);

  return (
    <div
      style={{
        position: "absolute",
        left: 60,
        top: topY,
        width: 820, // Leaves 200px safe margin on the right for Shorts UI
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        pointerEvents: "none",
        zIndex: 50,
        transform: `translateY(${translateY}px)`,
        opacity,
        filter: blur > 0.1 ? `blur(${blur}px)` : "none",
      }}
    >
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          gap: "10px 14px",
          textAlign: "center",
          fontFamily: "'Nohemi', 'Inter', -apple-system, sans-serif",
          fontSize: 48,
          lineHeight: 1.25,
          letterSpacing: "-0.02em",
          maxWidth: 780,
        }}
      >
        {activeChunk.words.map((word, idx) => {
          const isHighlight =
            activeChunk.highlightWord &&
            word.toLowerCase().includes(activeChunk.highlightWord.toLowerCase().replace(/[^a-z0-9$]/g, ""));
          const color = isHighlight
            ? activeChunk.highlightColor || "#C3D809"
            : "#E6EDF3";
          const fontWeight = isHighlight ? 700 : 500;

          return (
            <span
              key={idx}
              style={{
                color,
                fontWeight,
                display: "inline-block",
              }}
            >
              {word}
            </span>
          );
        })}
      </div>
    </div>
  );
};
