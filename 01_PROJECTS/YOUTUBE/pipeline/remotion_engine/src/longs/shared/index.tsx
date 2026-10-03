// Shared building blocks for 16:9 long-form data-graphics scenes (EP07+).
// Palette lock: #202322 / #233D4C / #C3D809 / #FD802E / #E6EDF3. Nohemi (Inter fallback).
import React, { useMemo } from "react";
import {
  AbsoluteFill,
  Easing,
  Sequence,
  continueRender,
  delayRender,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
} from "remotion";
import { PALETTE } from "../../brandTokens";

export const FPS = 60;
export const C = {
  bg: PALETTE.BACKGROUND, // #202322
  chrome: PALETTE.UI_STRUCTURE, // #233D4C  lines/chrome only, never text
  lime: PALETTE.SUCCESS, // #C3D809
  pumpkin: PALETTE.RISK, // #FD802E
  text: PALETTE.TEXT, // #E6EDF3
};
export const FONT = "'Nohemi', 'Inter', sans-serif";
// #233D4C at alpha, for card fills (stays inside the palette)
export const chromeA = (a: number) => `rgba(35,61,76,${a})`;
export const textA = (a: number) => `rgba(230,237,243,${a})`;
export const limeA = (a: number) => `rgba(195,216,9,${a})`;
export const pumpkinA = (a: number) => `rgba(253,128,46,${a})`;

// ---- Fonts: block rendering until Nohemi is loaded ----
if (typeof document !== "undefined") {
  const h = delayRender("Nohemi");
  Promise.all(
    (
      [
        ["Nohemi-Medium.ttf", "500"],
        ["Nohemi-Bold.ttf", "700"],
      ] as const
    ).map(([file, weight]) =>
      new FontFace("Nohemi", `url(${staticFile("fonts/" + file)})`, { weight }).load(),
    ),
  )
    .then((faces) => faces.forEach((ff) => document.fonts.add(ff)))
    .finally(() => continueRender(h));
}

// ---- Timeline → beat frame ranges ----
export type Timeline = {
  scenes: {
    scene: number;
    engine: string;
    asset: string;
    start: number;
    end: number;
    beats: { start: number; end: number; text: string }[];
  }[];
};
export type BeatF = { from: number; to: number; dur: number; text: string };
export type SceneInfo = { scene: number; durationInFrames: number; beats: BeatF[] };

export const sceneInfo = (tl: Timeline, asset: string): SceneInfo => {
  const s = tl.scenes.find((x) => x.asset === asset);
  if (!s) throw new Error(`Asset ${asset} not in timeline`);
  const s0 = Math.round(s.start * FPS);
  const durationInFrames = Math.round(s.end * FPS) - s0;
  const beats = s.beats.map((b, i) => {
    const from = i === 0 ? 0 : Math.round(b.start * FPS) - s0;
    const to = i === s.beats.length - 1 ? durationInFrames : Math.round(b.end * FPS) - s0;
    return { from, to, dur: to - from, text: b.text };
  });
  return { scene: s.scene, durationInFrames, beats };
};
export const useBeats = (tl: Timeline, asset: string) =>
  useMemo(() => sceneInfo(tl, asset), [tl, asset]);

// ---- Motion helpers ----
const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
/** eased 0..1 (or from..to) between frames a..b */
export const ease = (f: number, a: number, b: number, from = 0, to = 1) =>
  interpolate(f, [a, Math.max(b, a + 1)], [from, to], { ...CL, easing: Easing.inOut(Easing.cubic) });
/** spring 0..1 starting at `delay`, damping 200; exactly 1 after `dur` */
export const sp = (f: number, delay = 0, dur = 36) =>
  f - delay >= dur ? 1 : spring({ frame: f - delay, fps: FPS, config: { damping: 200 }, durationInFrames: dur });
/** 0..1..0 pulse lasting `dur` frames starting at `at` */
export const pulse = (f: number, at: number, dur = 30) =>
  interpolate(f, [at, at + dur * 0.35, at + dur], [0, 1, 0], CL);
export const fmt = (v: number, d = 0) =>
  v.toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d });

// ---- Scene shell: background, ambient grid, camera drift, HUD ----
export const AmbientGrid: React.FC<{ opacity?: number }> = ({ opacity = 0.3 }) => {
  const f = useCurrentFrame();
  const s = 80;
  return (
    <svg width={1920} height={1080} style={{ position: "absolute", inset: 0, opacity }}>
      <defs>
        <pattern
          id="qgrid"
          width={s}
          height={s}
          patternUnits="userSpaceOnUse"
          patternTransform={`translate(${(f * 0.22) % s} ${(f * 0.11) % s})`}
        >
          <path d={`M ${s} 0 L 0 0 0 ${s}`} fill="none" stroke={C.chrome} strokeWidth={2} />
        </pattern>
      </defs>
      <rect width={1920} height={1080} fill="url(#qgrid)" />
    </svg>
  );
};

export const Scene: React.FC<{
  beats: BeatF[];
  hud?: React.ReactNode;
  children: React.ReactNode;
}> = ({ beats, hud, children }) => {
  const f = useCurrentFrame();
  const total = beats[beats.length - 1].to;
  let i = beats.findIndex((b) => f < b.to);
  if (i < 0) i = beats.length - 1;
  const p = ease(f, beats[i].from, beats[i].to);
  // global push 1.00→1.03 plus a per-beat breathing 0..0.02 that reverses each beat (continuous, ≤1.05)
  const scale = 1 + 0.03 * ease(f, 0, total) + 0.02 * (i % 2 === 0 ? p : 1 - p);
  return (
    <AbsoluteFill style={{ backgroundColor: C.bg, fontFamily: FONT, color: C.text, overflow: "hidden" }}>
      <AmbientGrid />
      <AbsoluteFill style={{ scale: String(scale) }}>{children}</AbsoluteFill>
      {hud}
    </AbsoluteFill>
  );
};

/** One <Sequence> per timeline beat; children see beat-relative frames. */
export const Beat: React.FC<{ b: BeatF; children: React.ReactNode }> = ({ b, children }) => (
  <Sequence from={b.from} layout="none" name={b.text.slice(0, 48)}>
    {children}
  </Sequence>
);

// ---- Primitives ----
type Pos = React.CSSProperties;

export const Appear: React.FC<{
  delay?: number;
  dur?: number;
  dx?: number;
  dy?: number;
  scaleFrom?: number;
  out?: number; // frame (same clock) at which to fade out
  style?: Pos;
  children: React.ReactNode;
}> = ({ delay = 0, dur = 36, dx = 0, dy = 24, scaleFrom = 1, out, style, children }) => {
  const f = useCurrentFrame();
  const p = sp(f, delay, dur);
  const o = out === undefined ? 1 : 1 - ease(f, out, out + 20);
  return (
    <div
      style={{
        position: "absolute",
        opacity: p * o,
        translate: `${dx * (1 - p)}px ${dy * (1 - p)}px`,
        scale: String(scaleFrom + (1 - scaleFrom) * p),
        ...style,
      }}
    >
      {children}
    </div>
  );
};

export const Label: React.FC<{ children: React.ReactNode; size?: number; color?: string; dim?: boolean; style?: Pos }> = ({
  children,
  size = 22,
  color = C.text,
  dim = true,
  style,
}) => (
  <div
    style={{
      fontSize: size,
      fontWeight: 500,
      letterSpacing: "0.14em",
      textTransform: "uppercase",
      color,
      opacity: dim ? 0.7 : 1,
      whiteSpace: "nowrap",
      ...style,
    }}
  >
    {children}
  </div>
);

/** Count-up number with spring easing and fixed-width digits (tabular). */
export const Counter: React.FC<{
  to: number;
  from?: number;
  delay?: number;
  dur?: number;
  decimals?: number;
  prefix?: string;
  suffix?: string;
  size?: number;
  color?: string;
  log?: boolean;
  format?: (v: number) => string;
  style?: Pos;
}> = ({ to, from = 0, delay = 0, dur = 54, decimals = 0, prefix = "", suffix = "", size = 96, color = C.text, log, format, style }) => {
  const f = useCurrentFrame();
  const p = sp(f, delay, dur);
  const v = log ? Math.max(from, 1) * Math.pow(to / Math.max(from, 1), p) : from + (to - from) * p;
  const txt = prefix + (format ? format(p >= 1 ? to : v) : fmt(p >= 1 ? to : v, decimals)) + suffix;
  return (
    <span style={{ fontSize: size, fontWeight: 700, color, lineHeight: 1, whiteSpace: "nowrap", ...style }}>
      {[...txt].map((ch, i) =>
        /\d/.test(ch) ? (
          <span key={i} style={{ display: "inline-block", width: "0.62em", textAlign: "center" }}>
            {ch}
          </span>
        ) : (
          <span key={i}>{ch}</span>
        ),
      )}
    </span>
  );
};

export const Card: React.FC<{
  kicker?: string;
  title: React.ReactNode;
  sub?: React.ReactNode;
  accent?: string;
  titleSize?: number;
  titleColor?: string;
  delay?: number;
  out?: number;
  style?: Pos;
}> = ({ kicker, title, sub, accent = C.lime, titleSize = 44, titleColor = C.text, delay = 0, out, style }) => (
  <Appear delay={delay} out={out} style={style}>
    <div
      style={{
        border: `2px solid ${C.chrome}`,
        borderLeft: `8px solid ${accent}`,
        background: chromeA(0.28),
        borderRadius: 6,
        padding: "20px 30px 22px",
      }}
    >
      {kicker && <Label size={20} style={{ marginBottom: 10 }}>{kicker}</Label>}
      <div style={{ fontSize: titleSize, fontWeight: 700, color: titleColor, lineHeight: 1.1, whiteSpace: "nowrap" }}>
        {title}
      </div>
      {sub && <div style={{ fontSize: 24, fontWeight: 500, marginTop: 10, opacity: 0.8, whiteSpace: "nowrap" }}>{sub}</div>}
    </div>
  </Appear>
);

export const Tag: React.FC<{ children: React.ReactNode; color?: string; fill?: boolean; size?: number; style?: Pos }> = ({
  children,
  color = C.lime,
  fill,
  size = 22,
  style,
}) => (
  <span
    style={{
      display: "inline-block",
      border: `2px solid ${color}`,
      background: fill ? color : "transparent",
      color: fill ? C.bg : color,
      fontSize: size,
      fontWeight: 700,
      letterSpacing: "0.12em",
      textTransform: "uppercase",
      padding: "6px 14px 5px",
      borderRadius: 4,
      whiteSpace: "nowrap",
      ...style,
    }}
  >
    {children}
  </span>
);

/** Pinned HUD tag (outside camera drift), bottom-right of the safe area. */
export const IllustrativeTag: React.FC<{ at?: number; label?: string }> = ({ at = 0, label = "ILLUSTRATIVE" }) => {
  const f = useCurrentFrame();
  return (
    <div style={{ position: "absolute", right: 96, top: 800, opacity: sp(f, at) }}>
      <Tag color={C.pumpkin} size={18}>
        {label}
      </Tag>
    </div>
  );
};

/** Pinned HUD source line, bottom-left of the safe area. */
export const SourceTag: React.FC<{ children: React.ReactNode; at?: number }> = ({ children, at = 12 }) => {
  const f = useCurrentFrame();
  return (
    <div
      style={{
        position: "absolute",
        left: 96,
        top: 812,
        fontSize: 19,
        fontWeight: 500,
        letterSpacing: "0.06em",
        color: C.text,
        opacity: 0.62 * sp(f, at),
        whiteSpace: "nowrap",
      }}
    >
      SOURCE · {children}
    </div>
  );
};

export const TypeOn: React.FC<{ text: string; delay?: number; cps?: number; caret?: boolean; style?: Pos }> = ({
  text,
  delay = 0,
  cps = 22,
  caret = true,
  style,
}) => {
  const f = useCurrentFrame();
  const n = Math.max(0, Math.min(text.length, Math.floor(((f - delay) / FPS) * cps)));
  const showCaret = caret && f >= delay && (n < text.length || Math.floor(f / 18) % 2 === 0);
  return (
    <span style={{ whiteSpace: "pre", ...style }}>
      {text.slice(0, n)}
      <span
        style={{
          display: "inline-block",
          width: "0.45em",
          height: "0.9em",
          marginLeft: 4,
          verticalAlign: "-0.08em",
          background: C.lime,
          opacity: showCaret ? 1 : 0,
        }}
      />
    </span>
  );
};

/** Animated strike-through line over its positioned parent. */
export const Strike: React.FC<{ at: number; color?: string; thickness?: number; angle?: number }> = ({
  at,
  color = C.pumpkin,
  thickness = 8,
  angle = -6,
}) => {
  const f = useCurrentFrame();
  return (
    <div
      style={{
        position: "absolute",
        left: -10,
        top: "50%",
        height: thickness,
        width: `calc(${ease(f, at, at + 18) * 100}% + ${ease(f, at, at + 18) * 20}px)`,
        background: color,
        rotate: `${angle}deg`,
        borderRadius: thickness,
      }}
    />
  );
};

// ---- Charts ----
export type BarItem = {
  label: string;
  sub?: string;
  value: number;
  at: number; // frame (chart clock) the bar starts growing
  color?: string;
  valueLabel?: (v: number) => string; // default fmt
  dimAt?: number;
};

/** Bar chart; horizontal by default, `vertical` for columns, `log` for log10 scale (min..max). */
export const BarChart: React.FC<{
  items: BarItem[];
  max: number;
  min?: number;
  log?: boolean;
  vertical?: boolean;
  length: number; // px of the value axis
  thickness?: number;
  gap?: number;
  labelSize?: number;
  labelWidth?: number; // horizontal only
  dur?: number;
  ticks?: { v: number; label: string }[];
  ticksAt?: number;
  style?: Pos;
}> = ({ items, max, min = 1, log, vertical, length, thickness = 64, gap = 36, labelSize = 26, labelWidth = 300, dur = 60, ticks = [], ticksAt = 0, style }) => {
  const f = useCurrentFrame();
  const frac = (v: number) =>
    log ? (Math.log10(Math.max(v, min)) - Math.log10(min)) / (Math.log10(max) - Math.log10(min)) : v / max;
  const cross = items.length * thickness + (items.length - 1) * gap;
  const grid = ticks.map((t, k) => {
    const o = sp(f, ticksAt + k * 6) * 0.9;
    const pos = frac(t.v) * length;
    return vertical ? (
      <div key={k} style={{ position: "absolute", left: -20, width: cross + 40, bottom: pos, borderTop: `2px dashed ${C.chrome}`, opacity: o }}>
        <Label size={18} style={{ position: "absolute", right: cross + 56, top: -12 }}>{t.label}</Label>
      </div>
    ) : (
      <div key={k} style={{ position: "absolute", left: labelWidth + pos, top: -16, height: cross + 32, borderLeft: `2px dashed ${C.chrome}`, opacity: o }}>
        <Label size={18} style={{ position: "absolute", top: cross + 40, left: -40, width: 80, textAlign: "center" }}>{t.label}</Label>
      </div>
    );
  });
  const bars = items.map((it, k) => {
    const p = sp(f, it.at, dur);
    const shown = log ? min * Math.pow(it.value / min, p) : it.value * p;
    const L = Math.max(0, frac(shown)) * length;
    const color = it.color ?? C.lime;
    const dim = it.dimAt === undefined ? 1 : 1 - 0.6 * ease(f, it.dimAt, it.dimAt + 24);
    const vtxt = p >= 1 ? (it.valueLabel ?? ((v) => fmt(v)))(it.value) : (it.valueLabel ?? ((v) => fmt(v)))(shown);
    const appear = sp(f, it.at - 10, 20);
    const c0 = k * (thickness + gap);
    return vertical ? (
      <div key={k} style={{ position: "absolute", left: c0, bottom: 0, width: thickness, opacity: appear * dim }}>
        <div style={{ position: "absolute", bottom: 0, width: thickness, height: L, background: color, borderRadius: "4px 4px 0 0" }} />
        <div style={{ position: "absolute", bottom: L + 14, left: -80, width: thickness + 160, textAlign: "center", fontSize: 40, fontWeight: 700, color }}>
          {vtxt}
        </div>
        <div style={{ position: "absolute", top: 18, left: -90, width: thickness + 180, textAlign: "center" }}>
          <div style={{ fontSize: labelSize, fontWeight: 700 }}>{it.label}</div>
          {it.sub && <Label size={18} style={{ marginTop: 6 }}>{it.sub}</Label>}
        </div>
      </div>
    ) : (
      <div key={k} style={{ position: "absolute", top: c0, left: 0, height: thickness, width: labelWidth + length, opacity: appear * dim }}>
        <div style={{ position: "absolute", left: 0, width: labelWidth - 28, textAlign: "right", top: "50%", translate: "0 -50%" }}>
          <div style={{ fontSize: labelSize, fontWeight: 700, whiteSpace: "nowrap" }}>{it.label}</div>
          {it.sub && <Label size={17} style={{ marginTop: 4 }}>{it.sub}</Label>}
        </div>
        <div style={{ position: "absolute", left: labelWidth, top: 0, height: thickness, width: L, background: color, borderRadius: "0 4px 4px 0" }} />
        <div style={{ position: "absolute", left: labelWidth + L + 18, top: "50%", translate: "0 -50%", fontSize: Math.min(44, thickness * 0.7), fontWeight: 700, color, whiteSpace: "nowrap" }}>
          {vtxt}
        </div>
      </div>
    );
  });
  const axisO = sp(f, ticksAt);
  return (
    <div style={{ position: "absolute", ...style }}>
      {vertical ? (
        <div style={{ position: "relative", width: cross, height: length }}>
          {grid}
          <div style={{ position: "absolute", left: -30, width: cross + 60, bottom: -2, height: 3, background: C.chrome, opacity: axisO }} />
          {bars}
        </div>
      ) : (
        <div style={{ position: "relative", width: labelWidth + length, height: cross }}>
          {grid}
          <div style={{ position: "absolute", left: labelWidth - 3, top: -16, width: 3, height: cross + 32, background: C.chrome, opacity: axisO }} />
          {bars}
        </div>
      )}
    </div>
  );
};

/** Horizontal time axis that draws in; markers drop at their own frame. */
export type Marker = { t: number; label?: string; at: number; color?: string; up?: boolean };
export const axisX = (t: number, x: number, width: number, from: number, to: number) => x + ((t - from) / (to - from)) * width;
export const TimelineAxis: React.FC<{
  x: number;
  y: number;
  width: number;
  from: number;
  to: number;
  step: number;
  labelEvery?: number;
  drawAt?: number;
  drawDur?: number;
  markers?: Marker[];
}> = ({ x, y, width, from, to, step, labelEvery = step, drawAt = 0, drawDur = 90, markers = [] }) => {
  const f = useCurrentFrame();
  const p = ease(f, drawAt, drawAt + drawDur);
  const ticks: number[] = [];
  for (let t = from; t <= to + 1e-9; t += step) ticks.push(t);
  return (
    <div style={{ position: "absolute", left: 0, top: 0 }}>
      <div style={{ position: "absolute", left: x, top: y - 2, width: width * p, height: 4, background: C.chrome }} />
      {ticks.map((t) => {
        const tx = axisX(t, x, width, from, to);
        const o = sp(f, drawAt + ((tx - x) / width) * drawDur - 4, 18);
        const major = Math.abs((t - from) % labelEvery) < 1e-9 || t === to;
        return (
          <div key={t} style={{ position: "absolute", left: tx - 1, top: y - (major ? 14 : 8), width: 3, height: major ? 28 : 16, background: C.chrome, opacity: o }}>
            {major && (
              <div style={{ position: "absolute", top: 40, left: -60, width: 120, textAlign: "center", fontSize: 22, fontWeight: 500, color: C.text, opacity: 0.7 }}>
                {t}
              </div>
            )}
          </div>
        );
      })}
      {markers.map((m, k) => {
        const tx = axisX(m.t, x, width, from, to);
        const q = sp(f, m.at, 30);
        const col = m.color ?? C.lime;
        return (
          <div key={k} style={{ position: "absolute", left: tx, top: y, opacity: q }}>
            <div style={{ position: "absolute", left: -13, top: -13 - 40 * (1 - q), width: 26, height: 26, borderRadius: 13, background: col, boxShadow: `0 0 ${24 * pulse(f, m.at + 20, 50) + 6}px ${col}` }} />
            {m.label && (
              <div style={{ position: "absolute", left: -200, width: 400, textAlign: "center", top: m.up ? -96 : 60, fontSize: 30, fontWeight: 700, color: col, letterSpacing: "0.08em" }}>
                {m.label}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

// ---- Reusable silhouettes ----
/** Generic paper page: title bars + text lines, no real text. */
export const Paper: React.FC<{ w?: number; h?: number; lines?: number; accent?: string; style?: Pos }> = ({
  w = 300,
  h = 400,
  lines = 12,
  accent = C.text,
  style,
}) => (
  <div style={{ position: "absolute", width: w, height: h, border: `3px solid ${C.text}`, borderRadius: 6, background: C.bg, padding: w * 0.09, boxSizing: "border-box", ...style }}>
    <div style={{ height: h * 0.04, width: "80%", background: accent, opacity: 0.85, margin: "0 auto 10px", borderRadius: 3 }} />
    <div style={{ height: h * 0.03, width: "55%", background: C.text, opacity: 0.5, margin: `0 auto ${h * 0.06}px`, borderRadius: 3 }} />
    {Array.from({ length: lines }).map((_, i) => (
      <div key={i} style={{ height: Math.max(4, h * 0.014), width: `${i % 4 === 3 ? 62 : 100}%`, background: C.chrome, marginBottom: h * 0.032, borderRadius: 2 }} />
    ))}
  </div>
);

/** Grid of GPU "cores". `lit(i)` returns 0..1 lime intensity, `idle(i)` 0..1 pumpkin tint. */
export const CoreGrid: React.FC<{
  cols: number;
  rows: number;
  cell: number;
  gap: number;
  appearAt?: number;
  lit: (i: number) => number;
  idle?: (i: number) => number;
  style?: Pos;
}> = ({ cols, rows, cell, gap, appearAt = 0, lit, idle, style }) => {
  const f = useCurrentFrame();
  const n = cols * rows;
  return (
    <svg width={cols * (cell + gap)} height={rows * (cell + gap)} style={{ position: "absolute", ...style }}>
      {Array.from({ length: n }).map((_, i) => {
        const c = i % cols;
        const r = Math.floor(i / cols);
        const a = sp(f, appearAt + (c + r) * 0.9, 20);
        const L = lit(i);
        const I = idle ? idle(i) : 0;
        return (
          <rect
            key={i}
            x={c * (cell + gap)}
            y={r * (cell + gap)}
            width={cell}
            height={cell}
            rx={2}
            fill={L > 0.01 ? C.lime : I > 0.01 ? C.pumpkin : C.chrome}
            opacity={a * (L > 0.01 ? 0.25 + 0.75 * L : I > 0.01 ? 0.25 + 0.45 * I : 0.9)}
          />
        );
      })}
    </svg>
  );
};

/** Year cards that cascade into a stack, then align on one row at `alignAt`. */
export const RecapStack: React.FC<{
  items: { year: string; label: string; at: number; color?: string; tagAt?: number }[];
  alignAt: number;
  cardW: number;
  cardH?: number;
  gap?: number;
  y: number;
}> = ({ items, alignAt, cardW, cardH = 210, gap = 32, y }) => {
  const f = useCurrentFrame();
  const n = items.length;
  const rowW = n * cardW + (n - 1) * gap;
  const a = ease(f, alignAt, alignAt + 40);
  return (
    <>
      {items.map((it, k) => {
        const p = sp(f, it.at, 30);
        // stack: cascade around centre; row: evenly spaced
        const sx = 960 - cardW / 2 + (k - (n - 1) / 2) * 120;
        const sy = y - 70 + k * 40;
        const rx = 960 - rowW / 2 + k * (cardW + gap);
        const x = sx + (rx - sx) * a;
        const yy = sy + (y - sy) * a;
        const col = it.color ?? C.lime;
        const tag = it.tagAt === undefined ? 0 : sp(f, it.tagAt, 24);
        return (
          <div
            key={k}
            style={{
              position: "absolute",
              left: x,
              top: yy + 40 * (1 - p),
              width: cardW,
              height: cardH,
              opacity: p,
              boxSizing: "border-box",
              border: `2px solid ${tag > 0 ? col : C.chrome}`,
              borderTop: `8px solid ${col}`,
              background: C.bg,
              borderRadius: 6,
              padding: "20px 24px",
              boxShadow: `0 0 ${30 * tag}px ${col === C.lime ? limeA(0.35 * tag) : pumpkinA(0.35 * tag)}`,
            }}
          >
            <div style={{ fontSize: 52, fontWeight: 700, color: col }}>{it.year}</div>
            <div style={{ fontSize: 26, fontWeight: 700, marginTop: 14, lineHeight: 1.2 }}>{it.label}</div>
          </div>
        );
      })}
    </>
  );
};

/** Full-frame SVG arrow from (x1,y1) to (x2,y2); `p` 0..1 draws it; `curve` bends it (px, perpendicular). */
export const Arrow: React.FC<{
  x1: number;
  y1: number;
  x2: number;
  y2: number;
  p: number;
  color?: string;
  width?: number;
  dashed?: boolean;
  dashOffset?: number;
  head?: boolean;
  curve?: number;
  opacity?: number;
}> = ({ x1, y1, x2, y2, p, color = C.lime, width = 4, dashed, dashOffset = 0, head = true, curve = 0, opacity = 1 }) => {
  const mx = (x1 + x2) / 2;
  const my = (y1 + y2) / 2;
  const len = Math.hypot(x2 - x1, y2 - y1) || 1;
  const cx = mx - ((y2 - y1) / len) * curve;
  const cy = my + ((x2 - x1) / len) * curve;
  const ang = (Math.atan2(y2 - cy, x2 - cx) * 180) / Math.PI;
  const hs = 8 + width * 2.2;
  return (
    <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0, overflow: "visible", opacity }}>
      <path
        d={`M ${x1} ${y1} Q ${cx} ${cy} ${x2} ${y2}`}
        pathLength={1}
        fill="none"
        stroke={color}
        strokeWidth={width}
        strokeLinecap="round"
        strokeDasharray={dashed ? "0.025 0.02" : `${p} 1`}
        strokeDashoffset={dashed ? -dashOffset : 0}
        opacity={dashed ? p : 1}
      />
      {head && (
        <polygon
          points={`0,0 ${-hs},${-hs * 0.55} ${-hs},${hs * 0.55}`}
          fill={color}
          transform={`translate(${x2} ${y2}) rotate(${ang})`}
          opacity={p > 0.94 ? 1 : 0}
        />
      )}
    </svg>
  );
};

/** Lime check mark that draws itself. */
export const Check: React.FC<{ p: number; size?: number; color?: string; style?: React.CSSProperties }> = ({ p, size = 80, color = C.lime, style }) => (
  <svg width={size} height={size} viewBox="0 0 100 100" style={{ position: "absolute", ...style }}>
    <circle cx={50} cy={50} r={45} fill="none" stroke={color} strokeWidth={6} pathLength={1} strokeDasharray={`${p} 1`} />
    <path d="M 28 52 L 44 67 L 73 36" fill="none" stroke={color} strokeWidth={9} strokeLinecap="round" strokeLinejoin="round" pathLength={1} strokeDasharray={`${Math.max(0, p * 1.4 - 0.4)} 1`} />
  </svg>
);
