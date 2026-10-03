// EP07 "How AI Turns Every Word Into Geometry" — Remotion data-graphics scenes.
import React from "react";
import { AbsoluteFill, interpolate, random, useCurrentFrame } from "remotion";
import tlJson from "../../data/ep07_timeline.json";
import {
  Appear,
  Arrow,
  BarChart,
  Beat,
  C,
  Card,
  Check,
  Counter,
  IllustrativeTag,
  Label,
  RecapStack,
  Scene,
  SourceTag,
  Strike,
  Tag,
  Timeline,
  TimelineAxis,
  TypeOn,
  axisX,
  chromeA,
  ease,
  limeA,
  pulse,
  pumpkinA,
  sp,
  textA,
  useBeats,
} from "../shared";

const tl = tlJson as Timeline;
const useScene = (asset: string) => {
  const { beats: B } = useBeats(tl, asset);
  const f = useCurrentFrame();
  const at = (k: number, off = 0) => B[k].from + off;
  return { B, f, at };
};

// ---------------------------------------------------------------- S4
const Clipping: React.FC = () => (
  <div style={{ width: "100%", height: "100%", background: C.bg, border: `3px solid ${C.text}`, borderRadius: 4, padding: 22, boxSizing: "border-box" }}>
    <Label size={16} style={{ textAlign: "center", marginBottom: 8 }}>NEW YORK · JAN 1954</Label>
    <div style={{ height: 3, background: C.text, opacity: 0.8, marginBottom: 4 }} />
    <div style={{ height: 3, background: C.text, opacity: 0.8, marginBottom: 18 }} />
    <div style={{ height: 26, width: "92%", background: C.text, opacity: 0.85, borderRadius: 2, marginBottom: 10 }} />
    <div style={{ height: 26, width: "70%", background: C.text, opacity: 0.85, borderRadius: 2, marginBottom: 18 }} />
    <div style={{ height: 150, background: chromeA(0.9), borderRadius: 2, marginBottom: 16, position: "relative" }}>
      {[0, 1, 2].map((i) => (
        <div key={i} style={{ position: "absolute", left: 24 + i * 100, top: 26, width: 70, height: 100, border: `2px solid ${textA(0.5)}`, borderRadius: 2 }}>
          <div style={{ margin: "14px auto", width: 34, height: 34, borderRadius: 17, border: `3px solid ${textA(0.5)}` }} />
        </div>
      ))}
    </div>
    <div style={{ display: "flex", gap: 14 }}>
      {[0, 1].map((c) => (
        <div key={c} style={{ flex: 1 }}>
          {Array.from({ length: 7 }).map((_, i) => (
            <div key={i} style={{ height: 7, background: C.chrome, marginBottom: 9, width: i === 6 ? "60%" : "100%" }} />
          ))}
        </div>
      ))}
    </div>
  </div>
);

export const R1_GEORGETOWN_CARD: React.FC = () => {
  const { B, f, at } = useScene("R1_GEORGETOWN_CARD");
  const move = ease(f, at(2), at(2, 45));
  const clipIn = sp(f, at(1), 20);
  const flash = pulse(f, at(1), 24);
  const failed = f >= at(6, 8);
  const wipe = ease(f, at(5), at(5, 45));
  return (
    <Scene
      beats={B}
      hud={
        <>
          <SourceTag at={at(2)}>Hutchins (2004), AMTA</SourceTag>
          <AbsoluteFill style={{ background: C.text, opacity: 0.88 * flash }} />
        </>
      }
    >
      {/* b1 — Russian → English typewriter (ILLUSTRATIVE phrase) */}
      <Beat b={B[0]}>
        <Appear out={at(1) - 4} style={{ left: 330, top: 300, width: 1260 }}>
          <div style={{ position: "relative", border: `2px solid ${C.chrome}`, background: chromeA(0.28), borderRadius: 6, padding: "30px 44px", height: 360, boxSizing: "border-box" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <Label>IBM 701 · RUSSIAN → ENGLISH</Label>
              <Tag color={C.pumpkin} size={16}>ILLUSTRATIVE</Tag>
            </div>
            <div style={{ fontSize: 60, fontWeight: 700, marginTop: 44 }}>
              <TypeOn text="Наука развивает технику." delay={18} cps={15} caret={false} />
            </div>
            <div style={{ height: 6, background: C.chrome, marginTop: 18, borderRadius: 3, width: "100%" }}>
              <div style={{ height: 6, borderRadius: 3, background: C.lime, width: `${ease(f, 100, 190) * 100}%` }} />
            </div>
            <div style={{ fontSize: 54, fontWeight: 700, marginTop: 22, color: C.lime }}>
              <TypeOn text="Science develops technology." delay={190} cps={20} />
            </div>
          </div>
        </Appear>
        <Appear delay={270} out={at(1) - 4} style={{ left: 1310, top: 680 }}>
          <Tag color={C.text}>60+ SENTENCES</Tag>
        </Appear>
      </Beat>

      {/* b2 — camera flash on a press clipping */}
      <Beat b={B[1]}>
        <div
          style={{
            position: "absolute",
            left: interpolate(move, [0, 1], [760, 170]),
            top: interpolate(move, [0, 1], [250, 270]),
            width: 400,
            height: 540,
            opacity: clipIn,
            rotate: `${-4 + 2 * move}deg`,
            scale: String(interpolate(move, [0, 1], [1.12, 0.9]) + 0.2 * (1 - clipIn)),
          }}
        >
          <Clipping />
        </div>
      </Beat>

      {/* b3 — card + 250 WORDS */}
      <Beat b={B[2]}>
        <Card kicker="JANUARY 1954 · NEW YORK" title="GEORGETOWN–IBM EXPERIMENT · 1954" titleSize={40} delay={8} style={{ left: 660, top: 220 }} />
        <Appear delay={16} style={{ left: 660, top: 400 }}>
          <Counter to={250} size={130} color={C.lime} delay={16} dur={60} />
          <Label style={{ marginTop: 12 }}>WORDS</Label>
        </Appear>
      </Beat>

      {/* b4 — 6 GRAMMAR RULES */}
      <Beat b={B[3]}>
        <Appear style={{ left: 1120, top: 400 }}>
          <Counter to={6} size={130} color={C.lime} dur={40} />
          <Label style={{ marginTop: 12 }}>GRAMMAR RULES</Label>
        </Appear>
      </Beat>

      {/* b5/b6/b7 — prediction quote, then strike */}
      <Beat b={B[4]}>
        <Appear style={{ left: 660, top: 600, width: 1080 }}>
          <div
            style={{
              position: "relative",
              height: 170,
              border: `2px solid ${failed ? C.pumpkin : C.chrome}`,
              borderLeft: `8px solid ${failed ? C.pumpkin : C.lime}`,
              background: chromeA(0.28),
              borderRadius: 6,
              padding: "22px 34px",
              boxSizing: "border-box",
            }}
          >
            <Label size={20}>THE 1954 PREDICTION</Label>
            <div
              style={{
                marginTop: 16,
                fontSize: 64,
                fontWeight: 700,
                color: failed ? C.text : C.lime,
                opacity: failed ? 0.7 : 1,
                clipPath: `inset(-20px ${(1 - wipe) * 100}% -20px 0)`,
                whiteSpace: "nowrap",
              }}
            >
              SOLVED IN{" "}
              <span style={{ position: "relative", display: "inline-block", scale: String(1 + 0.08 * pulse(f, at(5, 150), 40)) }}>
                3–5
                {f >= at(6) && <Strike at={at(6) - at(4)} thickness={10} />}
              </span>{" "}
              YEARS
            </div>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[5]}>
        <span />
      </Beat>
      <Beat b={B[6]}>
        <Appear delay={14} style={{ left: 1500, top: 552 }}>
          <Tag color={C.pumpkin} fill>
            NOT SOLVED
          </Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S5
export const R2_ALPAC_1966: React.FC = () => {
  const { B, f, at } = useScene("R2_ALPAC_1966");
  const H = 560; // human reference bar length
  const rows = [
    { label: "SPEED", m: 0.55, at: at(1, 30), note: "SLOWER" },
    { label: "ACCURACY", m: 0.68, at: at(2, 4), note: "LESS ACCURATE" },
    { label: "COST", m: 2, at: at(3, 4), note: "≈2× THE COST" },
  ];
  const fade = 1 - ease(f, at(4), at(4, 30));
  const fund = ease(f, at(4, 10), at(4, 90));
  // funding line: flat high then cliff (ILLUSTRATIVE shape)
  const pts = [
    [0, 0.25], [0.2, 0.22], [0.4, 0.2], [0.55, 0.2], [0.62, 0.85], [0.75, 0.9], [1, 0.92],
  ];
  const fx = (u: number) => 300 + u * 1380;
  const fy = (v: number) => 430 + v * 320;
  const d = pts.map(([u, v], i) => `${i ? "L" : "M"} ${fx(u)} ${fy(v)}`).join(" ");
  return (
    <Scene beats={B} hud={<><SourceTag>ALPAC (1966), NAS / NRC</SourceTag><IllustrativeTag at={at(1)} label="ILLUSTRATIVE SCALE" /></>}>
      <Beat b={B[0]}>
        <TimelineAxis x={170} y={280} width={820} from={1950} to={1970} step={1} labelEvery={5} drawDur={70} markers={[{ t: 1954, at: 30, color: C.pumpkin }, { t: 1966, at: 90, color: C.lime }]} />
        <div style={{ position: "absolute", left: axisX(1954, 170, 820, 1950, 1970), top: 232, height: 4, background: C.lime, width: ease(f, 200, 260) * (axisX(1966, 170, 820, 1950, 1970) - axisX(1954, 170, 820, 1950, 1970)), borderRadius: 3 }} />
        <Appear delay={40} style={{ left: 1080, top: 212 }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 26 }}>
            <Counter from={1954} to={1966} format={(v) => String(Math.round(v))} size={92} color={C.lime} delay={40} dur={70} />
            <div>
              <Label size={20}>U.S. GOVERNMENT COMMITTEE</Label>
              <div style={{ fontSize: 46, fontWeight: 700, marginTop: 6 }}>ALPAC REPORT</div>
            </div>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: 1220, top: 400, opacity: 1 }}>
          <div style={{ display: "flex", gap: 30, opacity: fade }}>
            <span style={{ display: "flex", alignItems: "center", gap: 10 }}><span style={{ width: 22, height: 22, background: textA(0.55) }} /><Label>HUMAN</Label></span>
            <span style={{ display: "flex", alignItems: "center", gap: 10 }}><span style={{ width: 22, height: 22, background: C.pumpkin }} /><Label>MACHINE</Label></span>
          </div>
        </Appear>
      </Beat>
      {/* bar rows: human vs machine */}
      {rows.map((r, k) => {
        const y = 470 + k * 118;
        const show = sp(f, r.at - 6, 20);
        const hp = sp(f, r.at, 40);
        const mp = r.label === "COST" ? ease(f, r.at + 10, r.at + 40) * 0.5 + ease(f, r.at + 60, r.at + 100) * 0.5 : sp(f, r.at + 12, 40);
        const mlen = r.label === "COST" ? H * 2 * mp : H * r.m * mp;
        return f < r.at - 6 ? null : (
          <div key={k} style={{ position: "absolute", left: 160, top: y, opacity: show * fade }}>
            <div style={{ position: "absolute", left: 0, width: 230, top: 14, fontSize: 30, fontWeight: 700 }}>{r.label}</div>
            <div style={{ position: "absolute", left: 260, top: 0, height: 30, width: H * hp, background: textA(0.55), borderRadius: "0 4px 4px 0" }} />
            <div style={{ position: "absolute", left: 260, top: 40, height: 30, width: mlen, background: C.pumpkin, borderRadius: "0 4px 4px 0" }} />
            <div style={{ position: "absolute", left: 260 + mlen + 18, top: 36, fontSize: 28, fontWeight: 700, color: C.pumpkin, whiteSpace: "nowrap", opacity: sp(f, r.at + (r.label === "COST" ? 100 : 40), 20) }}>
              {r.note}
            </div>
          </div>
        );
      })}
      <Beat b={B[2]}><span /></Beat>
      <Beat b={B[3]}><span /></Beat>
      {/* b5 — funding drops off a cliff */}
      <Beat b={B[4]}>
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          <path d={d} fill="none" stroke={C.pumpkin} strokeWidth={8} strokeLinejoin="round" pathLength={1} strokeDasharray={`${fund} 1`} />
          <line x1={fx(0)} x2={fx(1)} y1={fy(1) + 4} y2={fy(1) + 4} stroke={C.chrome} strokeWidth={3} />
          <circle cx={fx(0.62)} cy={fy(0.85)} r={14 + 10 * pulse(f, at(4, 70), 40)} fill={C.pumpkin} opacity={sp(f, at(4, 64), 16)} />
        </svg>
        <Appear delay={20} style={{ left: 300, top: 380 }}>
          <Label color={C.pumpkin} dim={false}>U.S. MT FUNDING</Label>
        </Appear>
        <Appear delay={70} style={{ left: fx(0.62) + 30, top: fy(0.85) - 70 }}>
          <Tag color={C.pumpkin} fill>1966</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S10
export const R3_TIMELINE_1957: React.FC = () => {
  const { B, f, at } = useScene("R3_TIMELINE_1957");
  const X = 200, W = 1520, Y = 580;
  const x57 = axisX(1957, X, W, 1950, 2025);
  const sweep = ease(f, 150, 240);
  const cursorX = interpolate(sweep, [0, 1], [axisX(2025, X, W, 1950, 2025), x57]);
  const span = ease(f, at(2, 140), at(2, 240));
  return (
    <Scene beats={B} hud={<SourceTag at={at(2)}>Firth (1957), A Synopsis of Linguistic Theory</SourceTag>}>
      <Beat b={B[0]}>
        <TimelineAxis x={X} y={Y} width={W} from={1950} to={2025} step={5} labelEvery={10} drawAt={10} drawDur={120} markers={[{ t: 1957, at: 236, label: "1957", up: true }]} />
        {/* search cursor sweeping back to 1957 */}
        <div style={{ position: "absolute", left: cursorX - 2, top: Y - 120, width: 4, height: 150, background: C.lime, opacity: sp(f, 140, 16) * (1 - ease(f, 250, 280)) }} />
        <Appear delay={150} out={250} style={{ left: cursorX - 100, top: Y - 160, width: 200, textAlign: "center" }}>
          <Label size={18} color={C.lime} dim={false}>SCANNING</Label>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: x57 - 150, top: Y + 110, width: 300, textAlign: "center" }}>
          <Tag color={C.lime} fill>LINGUISTICS</Tag>
        </Appear>
        <Appear delay={30} style={{ left: x57 + 220, top: Y + 110 }}>
          <span style={{ position: "relative", display: "inline-block", opacity: 0.6 }}>
            <Tag color={C.text}>ENGINEERING</Tag>
            <Strike at={50} thickness={6} angle={0} />
          </span>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: x57 - 70, top: 290 }}>
          <svg width={130} height={110} viewBox="0 0 120 100" style={{ scale: String(1 + 0.14 * pulse(f, at(2, 10), 50) + 0.08 * pulse(f, at(2, 110), 50) + 0.08 * pulse(f, at(2, 210), 50)) }}>
            {[0, 58].map((dx) => (
              <g key={dx} transform={`translate(${dx} 0)`}>
                <circle cx={28} cy={70} r={20} fill={C.lime} />
                <path d="M 12 66 C 10 36, 26 14, 50 6" fill="none" stroke={C.lime} strokeWidth={12} strokeLinecap="round" />
              </g>
            ))}
          </svg>
        </Appear>
        <Card kicker="LINGUIST · LONDON" title="J. R. FIRTH" sub="A Synopsis of Linguistic Theory" delay={20} style={{ left: x57 + 140, top: 250 }} />
        {/* the field builds on it: lime span 1957 → 2025 */}
        <div style={{ position: "absolute", left: x57, top: Y - 4, height: 8, width: span * (X + W - x57), background: C.lime, borderRadius: 4, boxShadow: `0 0 18px ${limeA(0.6)}` }} />
        {[2013, 2018, 2020].map((t, k) => (
          <div key={t} style={{ position: "absolute", left: axisX(t, X, W, 1950, 2025) - 9, top: Y - 9, width: 18, height: 18, borderRadius: 9, background: C.lime, opacity: sp(f, at(2, 200 + k * 12), 16) }} />
        ))}
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S17
export const R4_SCALE_COUNTERS: React.FC = () => {
  const { B, f, at } = useScene("R4_SCALE_COUNTERS");
  const mv = ease(f, at(1), at(1, 40));
  const flip = ease(f, at(4, 20), at(4, 44));
  const fill = ease(f, at(4, 40), at(4, 120));
  const rowStyle = (y: number): React.CSSProperties => ({ left: 160, top: y, display: "flex", alignItems: "center", gap: 40 });
  return (
    <Scene beats={B} hud={<><SourceTag at={at(1)}>Mikolov et al. (2013b) · word2vec</SourceTag><IllustrativeTag at={at(4, 40)} label="ILLUSTRATIVE VALUES" /></>}>
      <Beat b={B[0]}>
        <div
          style={{
            position: "absolute",
            left: interpolate(mv, [0, 1], [960, 160]),
            top: interpolate(mv, [0, 1], [470, 214]),
            translate: `${-50 * (1 - mv)}% ${-50 * (1 - mv)}%`,
            scale: String(interpolate(mv, [0, 1], [1, 0.4]) * (0.8 + 0.2 * sp(f, 0, 30))),
            transformOrigin: "left top",
            opacity: sp(f, 0, 24),
            textAlign: mv > 0.5 ? "left" : "center",
          }}
        >
          <Label size={30} style={{ marginBottom: 12 }}>GOOGLE · 2013</Label>
          <div style={{ fontSize: 170, fontWeight: 700, color: C.lime, lineHeight: 1 }}>WORD2VEC</div>
        </div>
      </Beat>
      <Beat b={B[1]}>
        <Appear delay={10} style={rowStyle(320)}>
          <Counter to={100_000_000_000} from={1} log prefix="~" size={88} color={C.lime} delay={10} dur={110} />
          <div>
            <div style={{ fontSize: 34, fontWeight: 700 }}>WORDS READ</div>
            <Label size={18}>GOOGLE NEWS TEXT</Label>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={rowStyle(450)}>
          <Counter to={3_000_000} from={1} log size={88} dur={80} />
          <div style={{ fontSize: 34, fontWeight: 700 }}>WORDS & PHRASES</div>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <Appear style={rowStyle(580)}>
          <Counter to={300} size={88} color={C.lime} dur={60} />
          <div style={{ fontSize: 34, fontWeight: 700 }}>NUMBERS PER WORD</div>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        {/* word card flips into a 300-cell strip */}
        <div style={{ position: "absolute", left: 160, top: 712, width: 220, height: 80, opacity: sp(f, at(4), 14), rotate: `y ${flip * 90}deg`, border: `3px solid ${C.lime}`, borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 38, fontWeight: 700 }}>
          COFFEE
        </div>
        <svg width={1600} height={84} style={{ position: "absolute", left: 160, top: 710, opacity: flip }}>
          {Array.from({ length: 300 }).map((_, i) => {
            const v = random(`cf-${i}`) * 2 - 1;
            const show = fill * 300 > i ? 1 : 0;
            const h = 6 + 36 * Math.abs(v) * (0.85 + 0.15 * Math.sin(f / 9 + i));
            return <rect key={i} x={i * (1600 / 300)} y={v >= 0 ? 42 - h : 42} width={1600 / 300 - 1.4} height={h} fill={v >= 0 ? C.lime : C.pumpkin} opacity={show} />;
          })}
        </svg>
        <Appear delay={60} style={{ left: 160, top: 664 }}>
          <Label size={18}>COFFEE · 300 NUMBERS</Label>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S25
export const R5_ANALOGY_TEST: React.FC = () => {
  const { B, f, at } = useScene("R5_ANALOGY_TEST");
  const L = 1000, LW = 260, top = 572, th = 58, gap = 34;
  const gapP = ease(f, at(5), at(5, 30));
  return (
    <Scene beats={B} hud={<SourceTag at={at(1)}>Mikolov et al. (2013a), arXiv:1301.3781</SourceTag>}>
      <Beat b={B[0]}>
        <Card kicker="MIKOLOV ET AL. · 2013" title="ANALOGY TEST" style={{ left: 160, top: 210 }} />
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: 160, top: 360 }}>
          <Counter to={19544} size={128} color={C.lime} dur={80} />
        </Appear>
        <Appear delay={20} style={{ left: 640, top: 372 }}>
          <div style={{ fontSize: 36, fontWeight: 700 }}>ANALOGY QUESTIONS</div>
        </Appear>
        <Appear delay={130} style={{ left: 640, top: 432 }}>
          <Tag color={C.text} size={22}>ATHENS : GREECE :: OSLO : ?</Tag>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: 1150, top: 232 }}>
          <Tag color={C.text} size={20}>SKIP-GRAM · 640 DIMS · 6B WORDS</Tag>
        </Appear>
      </Beat>
      <BarChart
        style={{ left: 160, top }}
        length={L}
        labelWidth={LW}
        thickness={th}
        gap={gap}
        max={100}
        ticks={[{ v: 0, label: "0%" }, { v: 50, label: "50%" }, { v: 100, label: "100%" }]}
        ticksAt={at(3)}
        items={[
          { label: "MEANING", value: 55, at: at(3, 6), valueLabel: (v) => `${Math.round(v)}%` },
          { label: "GRAMMAR", value: 59, at: at(4, 4), valueLabel: (v) => `${Math.round(v)}%` },
        ]}
      />
      {/* b6 — "not perfect": the missing share in Pumpkin */}
      {[55, 59].map((v, k) => (
        <div key={k} style={{ position: "absolute", left: 160 + LW + (v / 100) * L, top: top + k * (th + gap), width: ((100 - v) / 100) * L * gapP, height: th, border: gapP > 0 ? `3px dashed ${C.pumpkin}` : "none", boxSizing: "border-box", opacity: gapP }} />
      ))}
      <Beat b={B[3]}><span /></Beat>
      <Beat b={B[4]}><span /></Beat>
      <Beat b={B[5]}>
        <Appear delay={6} style={{ left: 160 + LW + 0.8 * L, top: top - 52 }}>
          <Label color={C.pumpkin} dim={false}>MISSED</Label>
        </Appear>
      </Beat>
      <Beat b={B[6]}>
        <Appear style={{ left: 1380, top: 340 }}>
          <div style={{ border: `3px solid ${C.lime}`, borderRadius: 8, padding: "16px 34px", textAlign: "center", boxShadow: `0 0 ${30 * pulse(f, at(6, 20), 60)}px ${limeA(0.6)}` }}>
            <Label size={20}>FACTS TAUGHT</Label>
            <Counter from={9} to={0} size={110} color={C.lime} dur={40} />
          </div>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S26
export const R6_GLOVE_2014: React.FC = () => {
  const { B, f, at } = useScene("R6_GLOVE_2014");
  const rows = ["ICE", "STEAM"];
  const cols = ["SOLID", "GAS", "WATER", "FASHION"];
  const base = [
    [190, 7, 300, 2],
    [22, 78, 220, 2],
  ];
  const g = ease(f, at(2, 10), at(3, B[3].dur)); // counting progress across b3–b4
  const gx = 160, gy = 440, cw = 140, ch = 112, rl = 160;
  // analogy panel
  const P = { MAN: [1080, 700], WOMAN: [1300, 560], KING: [1420, 760], QUEEN: [1640, 620] } as const;
  const a1 = ease(f, at(4, 10), at(4, 50));
  const a2 = ease(f, at(5, 4), at(5, 40));
  const merge = ease(f, at(6, 10), at(6, 60));
  return (
    <Scene beats={B} hud={<><SourceTag>Pennington, Socher & Manning (2014), EMNLP</SourceTag><IllustrativeTag at={at(2)} label="ILLUSTRATIVE COUNTS" /></>}>
      <Beat b={B[0]}>
        <Card kicker="PENNINGTON · SOCHER · MANNING" title="2014 · STANFORD · GLOVE" style={{ left: 160, top: 210 }} />
        <Appear delay={150} style={{ left: 680, top: 262 }}>
          <Tag color={C.lime}>GLOBAL VECTORS</Tag>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <Appear out={at(6) - at(1)} style={{ left: 1030, top: 222 }}>
          <div style={{ position: "relative", border: `3px dashed ${textA(0.5)}`, borderRadius: 8, padding: "14px 28px", display: "flex", gap: 16, alignItems: "center" }}>
            <span style={{ fontSize: 48, fontWeight: 700, color: textA(0.6) }}>?</span>
            <Label>GUESS THE NEIGHBOR</Label>
            <Strike at={18} thickness={8} angle={-4} />
          </div>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: gx, top: gy - 50 }}>
          <Label size={18}>CO-OCCURRENCE COUNTS</Label>
        </Appear>
        {cols.map((c, j) => (
          <Appear key={c} delay={j * 4} style={{ left: gx + rl + j * cw, top: gy, width: cw, textAlign: "center" }}>
            <Label size={18} dim={false}>{c}</Label>
          </Appear>
        ))}
        {rows.map((r, i) => (
          <Appear key={r} delay={10 + i * 6} style={{ left: gx, top: gy + 40 + i * ch, height: ch - 12, display: "flex", alignItems: "center" }}>
            <div style={{ fontSize: 30, fontWeight: 700 }}>{r}</div>
          </Appear>
        ))}
        {rows.map((r, i) =>
          cols.map((c, j) => {
            const v = base[i][j];
            const inten = Math.min(1, v / 300) * g;
            const hot = (r === "ICE" && c === "SOLID") || (r === "STEAM" && c === "GAS");
            return (
              <Appear key={r + c} delay={14 + (i * 4 + j) * 3} style={{ left: gx + rl + j * cw + 6, top: gy + 40 + i * ch, width: cw - 12, height: ch - 12 }}>
                <div style={{ width: "100%", height: "100%", border: `3px solid ${hot && g > 0.5 ? C.pumpkin : inten > 0.15 ? C.lime : C.chrome}`, background: inten > 0.55 ? C.lime : chromeA(0.35), color: inten > 0.55 ? C.bg : C.text, borderRadius: 4, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 32, fontWeight: 700 }}>
                  {Math.round(v * g)}
                </div>
              </Appear>
            );
          }),
        )}
      </Beat>
      <Beat b={B[3]}>
        <Appear style={{ left: gx, top: gy + 40 + 2 * ch + 6 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <Label size={18}>TEXT SCANNED</Label>
            <div style={{ width: 420, height: 10, background: C.chrome, borderRadius: 5 }}>
              <div style={{ width: `${ease(f, at(3), at(3, B[3].dur)) * 100}%`, height: 10, background: C.lime, borderRadius: 5 }} />
            </div>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 1030, top: 400 }}>
          <Label size={18}>SAME DIRECTIONS</Label>
        </Appear>
        {Object.entries(P).map(([w, [x, y]], k) => (
          <Appear key={w} delay={k * 4} style={{ left: x - 14, top: y - 14 }}>
            <div style={{ width: 28, height: 28, borderRadius: 14, background: C.text }} />
            <div style={{ position: "absolute", top: w === "WOMAN" || w === "QUEEN" ? -40 : 34, left: -60, width: 150, textAlign: "center", fontSize: 24, fontWeight: 700 }}>{w}</div>
          </Appear>
        ))}
        <Arrow x1={P.MAN[0]} y1={P.MAN[1]} x2={P.WOMAN[0] - 14} y2={P.WOMAN[1] + 10} p={a1} width={6} />
        <Arrow x1={P.KING[0]} y1={P.KING[1]} x2={P.QUEEN[0] - 14} y2={P.QUEEN[1] + 10} p={a1} width={6} />
      </Beat>
      <Beat b={B[5]}>
        <Arrow x1={P.MAN[0]} y1={P.MAN[1] - 22} x2={P.WOMAN[0] - 14} y2={P.WOMAN[1] - 12} p={a2} width={4} dashed dashOffset={f / 200} color={C.text} head={false} />
        <Arrow x1={P.KING[0]} y1={P.KING[1] - 22} x2={P.QUEEN[0] - 14} y2={P.QUEEN[1] - 12} p={a2} width={4} dashed dashOffset={f / 200} color={C.text} head={false} />
        <Appear style={{ left: 1300, top: 400 }}>
          <div style={{ display: "flex", gap: 22, alignItems: "center" }}>
            <span style={{ width: 40, height: 6, background: C.lime }} /><Label size={18}>GLOVE</Label>
            <span style={{ width: 40, height: 0, borderTop: `4px dashed ${C.text}` }} /><Label size={18}>WORD2VEC</Label>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[6]}>
        {[
          { t: "PREDICT", x0: 1030 },
          { t: "COUNT", x0: 1560 },
        ].map((m) => (
          <div key={m.t} style={{ position: "absolute", left: interpolate(merge, [0, 1], [m.x0, 1290]), top: 232, opacity: sp(f, at(6), 16) * (1 - ease(f, at(6, 50), at(6, 64))) }}>
            <Tag color={C.text}>{m.t}</Tag>
          </div>
        ))}
        <div style={{ position: "absolute", left: 1170, top: 222, opacity: ease(f, at(6, 50), at(6, 70)), scale: String(0.8 + 0.2 * ease(f, at(6, 50), at(6, 70))) }}>
          <Tag color={C.lime} fill size={30}>ONE GEOMETRY</Tag>
        </div>
      </Beat>
      <Beat b={B[7]}>
        <Check p={ease(f, at(7, 4), at(7, 40))} size={86} style={{ left: 1520, top: 206 }} />
        <div style={{ position: "absolute", left: 1020, top: 520, width: 720, height: 320, borderRadius: 12, boxShadow: `0 0 ${40 * pulse(f, at(7, 30), 60)}px ${limeA(0.35)}`, border: `2px solid ${limeA(0.4 * sp(f, at(7), 20))}` }} />
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S30
const Toggle: React.FC<{ on: number }> = ({ on }) => (
  <div style={{ width: 120, height: 58, borderRadius: 29, background: on > 0.5 ? C.pumpkin : C.chrome, position: "relative" }}>
    <div style={{ position: "absolute", top: 7, left: 7 + on * 62, width: 44, height: 44, borderRadius: 22, background: C.text }} />
  </div>
);

export const R6B_FAIR_ANALOGY_2020: React.FC = () => {
  const { B, f, at } = useScene("R6B_FAIR_ANALOGY_2020");
  const on = 1 - ease(f, at(2, 6), at(2, 30));
  const banStrike = ease(f, at(1, 150), at(1, 170)) - ease(f, at(3), at(3, 20));
  const flipped = f >= at(3, 24);
  const ansIn = sp(f, at(1, 210), 24);
  const ans2 = sp(f, at(3, 24), 24);
  return (
    <Scene beats={B} hud={<><SourceTag>Nissim, van Noord & van der Goot (2020), Comp. Linguistics 46(2)</SourceTag><IllustrativeTag at={at(1, 140)} label="ILLUSTRATIVE RANKING" /></>}>
      <Beat b={B[0]}>
        <Card kicker="2020 · A TWIST" title="Nissim, van Noord & van der Goot" titleSize={40} style={{ left: 160, top: 210 }} />
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: 160, top: 380 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 22, fontSize: 56, fontWeight: 700 }}>
            <span>MAN</span><span style={{ opacity: 0.5 }}>:</span><span>DOCTOR</span><span style={{ opacity: 0.5 }}>::</span><span>WOMAN</span><span style={{ opacity: 0.5 }}>:</span>
            <span style={{ position: "relative", display: "inline-block", width: 290, height: 86, border: `3px solid ${flipped ? C.lime : ansIn > 0.5 ? C.pumpkin : C.chrome}`, borderRadius: 8, textAlign: "center", lineHeight: "86px", boxShadow: flipped ? `0 0 ${36 * pulse(f, at(3, 180), 60) + 6}px ${limeA(0.5)}` : "none" }}>
              <span style={{ position: "absolute", inset: 0, opacity: 1 - ansIn }}>?</span>
              <span style={{ position: "absolute", inset: 0, color: C.pumpkin, opacity: ansIn * (1 - ans2), translate: `0 ${-20 * ans2}px` }}>NURSE</span>
              <span style={{ position: "absolute", inset: 0, color: C.lime, opacity: ans2, translate: `0 ${20 * (1 - ans2)}px` }}>DOCTOR</span>
            </span>
          </div>
        </Appear>
        <Appear delay={20} style={{ left: 1300, top: 222 }}>
          <div style={{ border: `2px solid ${C.chrome}`, background: chromeA(0.28), borderRadius: 6, padding: "18px 26px", display: "flex", alignItems: "center", gap: 24 }}>
            <div>
              <Label size={18}>SEARCH RULE</Label>
              <div style={{ fontSize: 26, fontWeight: 700, marginTop: 6 }}>EXCLUDE INPUT WORDS</div>
            </div>
            <div style={{ textAlign: "center" }}>
              <Toggle on={on} />
              <div style={{ fontSize: 20, fontWeight: 700, marginTop: 6, color: on > 0.5 ? C.pumpkin : C.text }}>{on > 0.5 ? "ON" : "OFF"}</div>
            </div>
          </div>
        </Appear>
        {/* nearest-word ranking */}
        <Appear delay={130} style={{ left: 160, top: 520, width: 620 }}>
          <Label size={18} style={{ marginBottom: 14 }}>NEAREST WORDS</Label>
          {[
            { r: 1, w: "DOCTOR", ban: true },
            { r: 2, w: "NURSE" },
            { r: 3, w: "PHYSICIAN" },
          ].map((row, k) => {
            const isDoc = row.w === "DOCTOR";
            const isNurse = row.w === "NURSE";
            const col = isDoc && flipped ? C.lime : isNurse && !flipped && ansIn > 0.5 ? C.pumpkin : C.text;
            const dim = isNurse && flipped ? 0.35 + 0.65 * (1 - ease(f, at(3, 170), at(3, 200))) : 1;
            return (
              <div key={k} style={{ display: "flex", alignItems: "center", gap: 20, height: 62, borderBottom: `2px solid ${C.chrome}`, opacity: dim }}>
                <span style={{ width: 40, fontSize: 26, fontWeight: 700, opacity: 0.6 }}>{row.r}</span>
                <span style={{ position: "relative", fontSize: 34, fontWeight: 700, color: col }}>
                  {row.w}
                  {row.ban && <div style={{ position: "absolute", left: -8, top: "50%", height: 6, width: `calc(${banStrike * 100}% + ${banStrike * 16}px)`, background: C.pumpkin }} />}
                </span>
                {row.ban && <span style={{ opacity: banStrike }}><Tag color={C.pumpkin} size={16}>BANNED</Tag></span>}
              </div>
            );
          })}
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear delay={6} style={{ left: 1300, top: 360 }}>
          <Label size={18} color={C.lime} dim={false}>BAN LIFTED</Label>
        </Appear>
      </Beat>
      <Beat b={B[3]}><span /></Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 900, top: 580 }}>
          <Tag color={C.pumpkin} size={30}>THE BIAS IS REAL</Tag>
        </Appear>
      </Beat>
      <Beat b={B[5]}>
        <Appear style={{ left: 900, top: 670 }}>
          <Tag color={C.text} size={30}>SOME FAMOUS EXAMPLES OVERSTATED IT</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S32
export const R7_DIMENSION_GROWTH: React.FC = () => {
  const { B, f, at } = useScene("R7_DIMENSION_GROWTH");
  const left = 760, base = 720, len = 320, th = 170, gap = 210;
  const tilt = ease(f, at(3, 10), at(3, 80)) * 44;
  const y768 = base - ((Math.log10(768) - 1) / 2) * len;
  return (
    <Scene beats={B} hud={<SourceTag>Mikolov 2013 · Devlin et al. 2018 · Brown et al. 2020</SourceTag>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 160, top: 214 }}>
          <div style={{ fontSize: 40, fontWeight: 700 }}>NUMBERS PER TOKEN</div>
          <div style={{ marginTop: 10 }}><Tag color={C.text} size={18}>LOG SCALE</Tag></div>
        </Appear>
        {/* empty slots (b1 mid-beat) */}
        {["WORD2VEC", "BERT", "GPT-3"].map((n, k) => (
          <div key={n} style={{ position: "absolute", left: left + k * (th + gap), top: base - len + tilt, width: th, height: len, border: `2px dashed ${C.chrome}`, boxSizing: "border-box", opacity: sp(f, 150 + k * 10, 24) * (1 - ease(f, at(1 + k), at(1 + k, 20))) }} />
        ))}
      </Beat>
      <div style={{ position: "absolute", left: 0, top: tilt, width: 1920, height: 1080 }}>
        <BarChart
          vertical
          log
          min={10}
          max={1000}
          length={len}
          thickness={th}
          gap={gap}
          labelSize={28}
          style={{ left, top: base - len }}
          ticks={[
            { v: 10, label: "10" },
            { v: 100, label: "100" },
            { v: 1000, label: "1,000" },
          ]}
          ticksAt={20}
          items={[
            { label: "WORD2VEC", sub: "2013", value: 300, at: at(1, 4), dimAt: at(3, 220) },
            { label: "BERT", sub: "2018", value: 768, at: at(2, 4), dimAt: at(3, 230) },
            { label: "GPT-3", sub: "2020", value: 12288, at: at(3, 6) },
          ]}
          dur={70}
        />
        {/* 10,000 gridline revealed by the tilt */}
        <div style={{ position: "absolute", left: left - 20, width: 3 * th + 2 * gap + 40, top: base - 1.5 * len, borderTop: `2px dashed ${C.chrome}`, opacity: ease(f, at(3, 30), at(3, 60)) }}>
          <Label size={18} style={{ position: "absolute", right: 3 * th + 2 * gap + 56, top: -12 }}>10,000</Label>
        </div>
        {/* b3 mid-beat: 768 reference line toward the GPT-3 slot */}
        <div style={{ position: "absolute", left: left + th + gap + th, top: y768, height: 0, borderTop: `3px dashed ${C.lime}`, width: ease(f, at(2, 160), at(2, 220)) * (gap + th + 20), opacity: 0.7 * (1 - ease(f, at(3, 40), at(3, 70))) }} />
      </div>
      <Beat b={B[1]}><span /></Beat>
      <Beat b={B[2]}><span /></Beat>
      <Beat b={B[3]}><span /></Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S33
export const R8_EMBEDDING_MATRIX: React.FC = () => {
  const { B, f, at } = useScene("R8_EMBEDDING_MATRIX");
  const cols = 25, rows = 16, cs = 20, mx = 430, my = 470;
  const shimmer = ease(f, 110, 160);
  const glow = sp(f, at(3, 60), 30);
  return (
    <Scene beats={B} hud={<><SourceTag>Brown et al. (2020), GPT-3 · 50,257 × 12,288</SourceTag><IllustrativeTag at={110} label="ILLUSTRATIVE VALUES" /></>}>
      <Beat b={B[0]}>
        <Card kicker="GPT-3" title="EMBEDDING MATRIX" style={{ left: 160, top: 210 }} />
        <svg width={cols * cs} height={rows * cs} style={{ position: "absolute", left: mx, top: my, filter: glow ? `drop-shadow(0 0 ${14 * glow}px ${limeA(0.6)})` : undefined }}>
          {Array.from({ length: cols * rows }).map((_, i) => {
            const c = i % cols, r = Math.floor(i / cols);
            const a = sp(f, 6 + r * 4 + c * 0.8, 16);
            const v = random(`m-${i}-${Math.floor(f / 24)}`) * 2 - 1;
            const col = shimmer * 1.6 > random(`ms-${i}`) ? (v > 0.45 ? C.lime : v < -0.45 ? C.pumpkin : C.chrome) : C.chrome;
            return <rect key={i} x={c * cs} y={r * cs} width={cs - 3} height={cs - 3} rx={2} fill={col} opacity={a * 0.9} />;
          })}
        </svg>
      </Beat>
      <Beat b={B[1]}>
        <Appear dx={-20} dy={0} style={{ left: 160, top: my + 100, width: 228, textAlign: "right" }}>
          <Counter to={50257} size={54} dur={24} />
          <Label size={18} style={{ marginTop: 8 }}>TOKENS · ROWS</Label>
        </Appear>
        <div style={{ position: "absolute", left: mx - 22, top: my, width: 8, height: rows * cs * ease(f, at(1), at(1, 20)), background: C.text, borderRadius: 4 }} />
      </Beat>
      <Beat b={B[2]}>
        <div style={{ position: "absolute", left: mx, top: my - 24, height: 8, width: cols * cs * ease(f, at(2), at(2, 24)), background: C.text, borderRadius: 4 }} />
        <Appear style={{ left: mx, top: my - 96 }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 14 }}>
            <Counter to={12288} size={54} dur={40} />
            <Label size={18}>NUMBERS EACH · COLUMNS</Label>
          </div>
        </Appear>
        <Appear delay={110} style={{ left: 1040, top: 400 }}>
          <div style={{ fontSize: 60, fontWeight: 700, whiteSpace: "nowrap", clipPath: `inset(-10px ${(1 - ease(f, at(2, 110), at(2, 160))) * 100}% -10px 0)` }}>50,257 × 12,288</div>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <Appear style={{ left: 1040, top: 500 }}>
          <span style={{ fontSize: 84, fontWeight: 700, color: C.lime }}>= </span>
          <Counter to={617558016} size={84} color={C.lime} dur={110} />
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 1040, top: 630 }}>
          <Tag color={C.lime} fill size={28}>THE DICTIONARY ALONE</Tag>
        </Appear>
      </Beat>
      <Beat b={B[5]}>
        {[0, 1, 2, 3].map((k) => (
          <Appear key={k} delay={k * 5} style={{ left: 1040 + k * 26, top: 722 - k * 14 }}>
            <div style={{ width: 150, height: 56, border: `3px dashed ${textA(0.5)}`, borderRadius: 6, background: C.bg }} />
          </Appear>
        ))}
        <Appear delay={24} style={{ left: 1290, top: 712 }}>
          <Label size={20} color={C.pumpkin} dim={false}>MODEL LAYERS · NOT STARTED</Label>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S35
const Box: React.FC<{ x: number; y: number; w: number; h: number; label: string; color?: string; fillP?: number }> = ({ x, y, w, h, label, color = C.text, fillP = 0 }) => (
  <div style={{ position: "absolute", left: x, top: y, width: w, height: h, border: `3px solid ${color}`, borderRadius: 8, background: chromeA(0.3), display: "flex", alignItems: "center", justifyContent: "center", overflow: "hidden" }}>
    <svg width={w} height={h} style={{ position: "absolute", left: 0, top: 0 }}>
      {Array.from({ length: 24 }).map((_, i) => (
        <circle key={i} cx={20 + random(`bx${i}`) * (w - 40)} cy={20 + random(`by${i}`) * (h - 40)} r={5} fill={C.lime} opacity={fillP * 24 > i ? 0.6 : 0} />
      ))}
    </svg>
    <span style={{ position: "relative", fontSize: 32, fontWeight: 700, letterSpacing: "0.08em" }}>{label}</span>
  </div>
);

export const R8B_TRAINED_TOGETHER: React.FC = () => {
  const { B, f, at } = useScene("R8B_TRAINED_TOGETHER");
  const collapse = ease(f, at(4, 90), at(4, 150));
  const loopP = ease(f, at(2), at(2, 40));
  const dash = f / 120;
  const lx = -collapse * 420;
  return (
    <Scene beats={B} hud={<SourceTag at={at(1)}>Mikolov et al. 2013 · Brown et al. 2020</SourceTag>}>
      <Beat b={B[0]}>
        <div style={{ position: "absolute", left: 160 + lx * 0.2, top: 230, width: 740, height: 520, border: `2px solid ${C.chrome}`, borderRadius: 10, opacity: sp(f, 0, 30) * (1 - collapse), translate: `${collapse * 500}px 0` }}>
          <Label style={{ position: "absolute", left: 28, top: 22 }}>2013 · WORD2VEC</Label>
        </div>
        <div style={{ position: "absolute", left: 1020 - collapse * 430, top: 230, width: 740 + collapse * 0, height: 520, border: `2px solid ${C.chrome}`, borderRadius: 10, opacity: sp(f, 20, 30), boxShadow: `0 0 ${30 * collapse}px ${limeA(0.3)}` }}>
          <Label style={{ position: "absolute", left: 28, top: 22 }}>TODAY · CHATBOT</Label>
        </div>
      </Beat>
      <Beat b={B[1]}>
        <div style={{ position: "absolute", left: 0, top: 0, opacity: 1 - collapse, translate: `${collapse * 500}px 0` }}>
          <Appear>
            <Box x={230} y={400} w={220} h={150} label="MAP" fillP={ease(f, at(1, 10), at(1, 70))} />
          </Appear>
          <Arrow x1={470} y1={475} x2={600} y2={475} p={ease(f, at(1, 70), at(1, 100))} color={C.text} />
          <div style={{ position: "absolute", left: 620, top: 405, width: 140, height: 140, opacity: sp(f, at(1, 100), 20), scale: String(0.6 + 0.4 * sp(f, at(1, 100), 20)) }}>
            <svg width={140} height={140} viewBox="0 0 100 100">
              <polygon points="30,2 70,2 98,30 98,70 70,98 30,98 2,70 2,30" fill={C.pumpkin} />
            </svg>
            <div style={{ position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 30, fontWeight: 700, color: C.bg }}>STOP</div>
          </div>
        </div>
      </Beat>
      <Beat b={B[2]}>
        <div style={{ position: "absolute", left: -collapse * 430, top: 0, width: 1920, height: 1080 }}>
          <Appear><Box x={1090} y={400} w={220} h={150} label="MAP" fillP={1} /></Appear>
          <Appear delay={10}><Box x={1470} y={400} w={220} h={150} label="MODEL" /></Appear>
          <Arrow x1={1320} y1={430} x2={1460} y2={430} curve={-50} p={loopP} dashed dashOffset={dash} width={5} />
          <Arrow x1={1460} y1={520} x2={1320} y2={520} curve={-50} p={loopP} dashed dashOffset={dash} width={5} />
          {[0, 1, 2].map((k) => {
            const u = (f / 90 + k / 3) % 1;
            const top = u < 0.5;
            const t = top ? u * 2 : (u - 0.5) * 2;
            const x = top ? 1320 + t * 140 : 1460 - t * 140;
            const y = (top ? 430 : 520) + (top ? -1 : 1) * 50 * Math.sin(Math.PI * t) * 1;
            return <div key={k} style={{ position: "absolute", left: x - 8, top: y - 8, width: 16, height: 16, borderRadius: 8, background: C.lime, opacity: ease(f, at(2, 110), at(2, 140)) }} />;
          })}
        </div>
      </Beat>
      <Beat b={B[3]}>
        <div style={{ position: "absolute", left: -collapse * 430, top: 0, width: 1920, height: 1080 }}>
          <Appear style={{ left: 1340, top: 620, width: 100 }}>
            <div style={{ border: `3px solid ${C.text}`, borderRadius: 6, padding: 12, background: C.bg }}>
              {[0, 1, 2, 3, 4].map((i) => <div key={i} style={{ height: 5, background: C.chrome, marginBottom: 7, width: i === 4 ? "60%" : "100%" }} />)}
            </div>
          </Appear>
          <Arrow x1={1360} y1={615} x2={1230} y2={560} p={ease(f, at(3, 8), at(3, 40))} color={C.text} width={3} />
          <Arrow x1={1420} y1={615} x2={1550} y2={560} p={ease(f, at(3, 8), at(3, 40))} color={C.text} width={3} />
          <Appear delay={20} style={{ left: 1460, top: 700 }}><Label size={18}>TRAINING TEXT</Label></Appear>
        </div>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 1110 - collapse * 430, top: 300 }}>
          <Tag color={C.lime} fill size={30}>PREDICT THE NEXT TOKEN</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S39
const Mag: React.FC<{ color: string; size?: number }> = ({ color, size = 64 }) => (
  <svg width={size} height={size} viewBox="0 0 64 64">
    <circle cx={26} cy={26} r={17} fill="none" stroke={color} strokeWidth={6} />
    <line x1={39} y1={39} x2={56} y2={56} stroke={color} strokeWidth={7} strokeLinecap="round" />
  </svg>
);

export const R9_BERT_SEARCH: React.FC = () => {
  const { B, f, at } = useScene("R9_BERT_SEARCH");
  const toPoint = ease(f, at(6), at(6, 50));
  const upper = 1 - toPoint;
  const words = ["2019", "brazil", "traveler", "to", "usa", "need", "a", "visa"];
  const typed = Math.floor(ease(f, at(3, 4), at(3, 120)) * words.length + 0.001);
  const toDim = ease(f, at(4, 10), at(4, 30)) * (1 - ease(f, at(5), at(5, 20)));
  const toLime = ease(f, at(5), at(5, 20));
  const flip = ease(f, at(5, 30), at(5, 70));
  const pages = Array.from({ length: 42 }).map((_, i) => {
    const ang = random(`pa${i}`) * Math.PI * 2;
    const r = 150 + random(`pr${i}`) * 480;
    return { x: 960 + Math.cos(ang) * r * 1.25, y: 520 + Math.sin(ang) * r * 0.48, r };
  });
  const near = [...pages].sort((a, b) => a.r - b.r).slice(0, 3);
  const ring = ease(f, at(7), at(7, 60));
  return (
    <Scene beats={B} hud={<><SourceTag>Nayak, Google (25 Oct 2019)</SourceTag><IllustrativeTag at={at(6)} label="ILLUSTRATIVE MAP" /></>}>
      <div style={{ position: "absolute", left: 0, top: 0, width: 1920, height: 1080, opacity: upper, scale: String(1 - 0.25 * toPoint) }}>
        <Beat b={B[0]}>
          <Card kicker="BERT IN PRODUCTION" title="2019 · GOOGLE SEARCH" style={{ left: 160, top: 210 }} />
        </Beat>
        <Beat b={B[1]}>
          {Array.from({ length: 10 }).map((_, k) => {
            const lit = k === 6 && f >= at(1, 70);
            return (
              <Appear key={k} delay={k * 4} style={{ left: 160 + k * 112, top: 360, opacity: 1 - 0.6 * ease(f, at(2), at(2, 20)) }}>
                <div style={{ scale: String(lit ? 1 + 0.2 * pulse(f, at(1, 70), 40) : 1) }}>
                  <Mag color={lit ? C.lime : textA(0.45)} />
                </div>
              </Appear>
            );
          })}
          <Appear delay={90} style={{ left: 1300, top: 368 }}>
            <Tag color={C.lime} size={24}>≈1 IN 10 US ENGLISH QUERIES</Tag>
          </Appear>
        </Beat>
        <Beat b={B[2]}>
          <Appear style={{ left: 160, top: 520 }}>
            <div style={{ width: 1180, height: 96, border: `3px solid ${C.text}`, borderRadius: 48, display: "flex", alignItems: "center", gap: 18, padding: "0 30px", boxSizing: "border-box", background: chromeA(0.3) }}>
              <Mag color={C.text} size={46} />
              <div style={{ display: "flex", gap: 14, fontSize: 42, fontWeight: 500 }}>
                {words.slice(0, typed).map((w, i) => (
                  <span
                    key={i}
                    style={{
                      color: w === "to" ? (toLime > 0 ? C.lime : C.text) : C.text,
                      opacity: w === "to" ? 1 - 0.75 * toDim : 1,
                      fontWeight: w === "to" && toLime > 0 ? 700 : 500,
                      textShadow: w === "to" && toLime > 0 ? `0 0 ${18 * toLime}px ${limeA(0.9)}` : undefined,
                      textDecoration: w === "to" && toLime > 0 ? `underline ${C.lime} 4px` : undefined,
                      textUnderlineOffset: 10,
                    }}
                  >
                    {w}
                  </span>
                ))}
                {typed < words.length && f >= at(3) && <span style={{ width: 4, background: C.lime, opacity: Math.floor(f / 15) % 2 }} />}
              </div>
            </div>
          </Appear>
        </Beat>
        <Beat b={B[3]}><span /></Beat>
        <Beat b={B[4]}>
          <Appear delay={10} out={at(5) - at(4) - 4} style={{ left: 520, top: 650 }}>
            <Label color={C.pumpkin} dim={false}>OLDER SYSTEMS: “TO” IGNORED</Label>
          </Appear>
          {/* direction diagram */}
          <Appear style={{ left: 1420, top: 520 }}>
            <div style={{ position: "relative", width: 340, height: 100 }}>
              {[
                { t: "BR", x: 0 },
                { t: "US", x: 250 },
              ].map((n) => (
                <div key={n.t} style={{ position: "absolute", left: n.x, top: 4, width: 90, height: 90, borderRadius: 45, border: `3px solid ${C.text}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 30, fontWeight: 700 }}>
                  {n.t}
                </div>
              ))}
            </div>
          </Appear>
          <Arrow x1={flip > 0.5 ? 1515 : 1665} y1={570} x2={flip > 0.5 ? 1665 : 1515} y2={570} p={flip > 0.5 ? ease(f, at(5, 50), at(5, 80)) : ease(f, at(4, 10), at(4, 40)) * (1 - ease(f, at(5, 30), at(5, 50)))} color={flip > 0.5 ? C.lime : C.pumpkin} width={6} />
        </Beat>
        <Beat b={B[5]}>
          <Appear delay={10} style={{ left: 520, top: 650 }}>
            <Label color={C.lime} dim={false}>BERT: BRAZIL → USA</Label>
          </Appear>
        </Beat>
      </div>
      {/* query → point, nearest pages */}
      <Beat b={B[6]}>
        {pages.map((p, i) => {
          const isNear = near.includes(p);
          const lit = isNear ? sp(f, at(7, 20 + near.indexOf(p) * 14), 20) : 0;
          return (
            <div key={i} style={{ position: "absolute", left: p.x - 9, top: p.y - 9, width: 18, height: 18, borderRadius: 3, background: lit > 0 ? C.lime : textA(0.45), opacity: sp(f, at(6, 10 + i), 20), scale: String(1 + 0.5 * lit) }}>
              {isNear && lit > 0 && (
                <div style={{ position: "absolute", left: 24, top: -12, fontSize: 24, fontWeight: 700, color: C.lime, opacity: lit }}>#{near.indexOf(p) + 1}</div>
              )}
            </div>
          );
        })}
        <div style={{ position: "absolute", left: 960 - 20, top: 520 - 20, width: 40, height: 40, borderRadius: 20, background: C.lime, opacity: toPoint, scale: String(0.4 + 0.6 * toPoint), boxShadow: `0 0 30px ${limeA(0.8)}` }} />
        <Appear delay={40} style={{ left: 860, top: 560, width: 200, textAlign: "center" }}>
          <Label size={20} color={C.lime} dim={false}>YOUR QUERY</Label>
        </Appear>
      </Beat>
      <Beat b={B[7]}>
        <div style={{ position: "absolute", left: 960 - 200 * ring * 1.25, top: 520 - 200 * ring * 0.48, width: 400 * ring * 1.25, height: 400 * ring * 0.48, borderRadius: "50%", border: `3px dashed ${C.lime}`, opacity: 0.8 }} />
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S45
export const R10_RECAP_STACK: React.FC = () => {
  const { B, f, at } = useScene("R10_RECAP_STACK");
  const cw = 360, gap = 36, y = 430;
  const x0 = 960 - (4 * cw + 3 * gap) / 2;
  return (
    <Scene beats={B}>
      <RecapStack
        y={y}
        cardW={cw}
        gap={gap}
        alignAt={at(4)}
        items={[
          { year: "1954", label: "250 WORDS, 6 RULES", at: at(0, 4), color: C.pumpkin, tagAt: at(4, 30) },
          { year: "1957", label: "THE COMPANY IT KEEPS", at: at(1, 4), tagAt: at(5, 4) },
          { year: "2013", label: "300 NUMBERS", at: at(2, 4), tagAt: at(5, 12) },
          { year: "2020", label: "12,288 NUMBERS", at: at(3, 4), tagAt: at(5, 20) },
        ]}
      />
      <Beat b={B[0]}><span /></Beat>
      <Beat b={B[1]}><span /></Beat>
      <Beat b={B[2]}><span /></Beat>
      <Beat b={B[3]}><span /></Beat>
      <Beat b={B[4]}>
        <Appear delay={30} style={{ left: x0, top: y - 90 }}>
          <Tag color={C.pumpkin} fill size={26}>RULES FAILED</Tag>
        </Appear>
      </Beat>
      <Beat b={B[5]}>
        <div style={{ position: "absolute", left: x0 + cw + gap, top: y - 40, height: 6, width: ease(f, at(5), at(5, 30)) * (3 * cw + 2 * gap), background: C.lime, borderRadius: 3 }} />
        <Appear delay={10} style={{ left: x0 + cw + gap, top: y - 100 }}>
          <Tag color={C.lime} fill size={26}>NEIGHBORS WON</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};
