// EP08 "The 2017 Paper That Rebuilt Modern AI" — Remotion data-graphics scenes.
import React from "react";
import { interpolate, random, useCurrentFrame } from "remotion";
import tlJson from "../../data/ep08_timeline.json";
import {
  Appear,
  Arrow,
  BarChart,
  Beat,
  C,
  Card,
  Check,
  CoreGrid,
  Counter,
  IllustrativeTag,
  Label,
  Paper,
  RecapStack,
  Scene,
  SourceTag,
  Tag,
  Timeline,
  TimelineAxis,
  TypeOn,
  axisX,
  chromeA,
  ease,
  fmt,
  limeA,
  pulse,
  pumpkinA,
  sp,
  textA,
} from "../shared";
import { useBeats } from "../shared";

const tl = tlJson as Timeline;
const useScene = (asset: string) => {
  const { beats: B } = useBeats(tl, asset);
  const f = useCurrentFrame();
  const at = (k: number, off = 0) => B[k].from + off;
  return { B, f, at };
};

const AUTHORS = [
  { n: "Ashish Vaswani", i: "AV", co: "ESSENTIAL AI", named: false },
  { n: "Noam Shazeer", i: "NS", co: "CHARACTER.AI", named: true },
  { n: "Niki Parmar", i: "NP", co: "ESSENTIAL AI", named: false },
  { n: "Jakob Uszkoreit", i: "JU", co: "INCEPTIVE", named: false },
  { n: "Llion Jones", i: "LJ", co: "SAKANA AI", named: true },
  { n: "Aidan N. Gomez", i: "AG", co: "COHERE", named: true },
  { n: "Łukasz Kaiser", i: "ŁK", co: "OPENAI", named: true },
  { n: "Illia Polosukhin", i: "IP", co: "NEAR", named: false },
];

// ---------------------------------------------------------------- S1
export const R1_PAPER_COUNTER: React.FC = () => {
  const { B, f, at } = useScene("R1_PAPER_COUNTER");
  const up = ease(f, at(1), at(1, 40));
  const dim = 1 - 0.75 * ease(f, at(3), at(3, 30));
  const tPop = pulse(f, at(4), 26);
  return (
    <Scene beats={B} hud={<SourceTag at={at(2)}>Vaswani et al. (2017) · Google Scholar</SourceTag>}>
      <Beat b={B[0]}>
        <div
          style={{
            position: "absolute",
            left: interpolate(up, [0, 1], [960, 160]),
            top: interpolate(up, [0, 1], [440, 214]),
            translate: `${-50 * (1 - up)}% ${-50 * (1 - up)}%`,
            scale: String(interpolate(up, [0, 1], [1, 0.42]) * (0.85 + 0.15 * sp(f, 0, 30))),
            transformOrigin: "left top",
            opacity: sp(f, 0, 24) * (up > 0 ? dim : 1),
            textAlign: up > 0.5 ? "left" : "center",
          }}
        >
          <div style={{ fontSize: 170, fontWeight: 700, lineHeight: 1 }}>JUNE 2017</div>
          <div style={{ fontSize: 40, fontWeight: 500, marginTop: 24, opacity: sp(f, 130, 30) * 0.8, letterSpacing: "0.14em" }}>GOOGLE · 8 RESEARCHERS</div>
        </div>
      </Beat>
      <Beat b={B[1]}>
        <div style={{ position: "absolute", left: 0, top: 0, opacity: dim, width: 1920, height: 1080 }}>
          {/* faint vinyl-record rings */}
          <svg width={700} height={700} style={{ position: "absolute", left: 420, top: 175, opacity: 0.7 * sp(f, at(1), 40), rotate: `${f * 0.4}deg` }}>
            {[340, 300, 260, 220, 180].map((r, k) => (
              <circle key={r} cx={350} cy={350} r={r} fill="none" stroke={C.chrome} strokeWidth={k === 0 ? 6 : 3} strokeDasharray={k === 2 ? "40 18" : undefined} />
            ))}
            <circle cx={350} cy={350} r={70} fill={chromeA(0.6)} />
          </svg>
          <Appear dx={-80} dy={0} style={{ left: 620, top: 300 }}>
            <Paper w={300} h={400} accent={C.lime} />
          </Appear>
          {Array.from({ length: 8 }).map((_, k) => (
            <Appear key={k} delay={20 + k * 4} style={{ left: 600 + k * 44, top: 252 }}>
              <div style={{ width: 26, height: 26, borderRadius: 13, background: C.lime }} />
            </Appear>
          ))}
        </div>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: 1110, top: 400, opacity: 1 }}>
          <div style={{ opacity: dim }}>
            <Counter to={250000} from={1} log suffix="+" size={124} color={C.lime} dur={150} />
            <Label style={{ marginTop: 14 }}>CITATIONS</Label>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <div style={{ position: "absolute", left: 0, top: 330, width: 1920, display: "flex", justifyContent: "center", gap: 40 }}>
          {["G", "P", "T"].map((ch, k) => (
            <div key={ch} style={{ fontSize: 300, fontWeight: 700, lineHeight: 1, color: ch === "T" ? C.lime : C.text, opacity: sp(f, at(3, k * 14), 30), translate: `0 ${30 * (1 - sp(f, at(3, k * 14), 30))}px`, scale: ch === "T" ? String(1 + 0.08 * pulse(f, at(3, 120), 50) + 0.18 * tPop) : "1", textShadow: ch === "T" ? `0 0 ${40 * (pulse(f, at(3, 120), 50) + tPop)}px ${limeA(0.7)}` : undefined }}>
              {ch}
            </div>
          ))}
        </div>
      </Beat>
      <Beat b={B[4]}><span /></Beat>
      <Beat b={B[5]}>
        <div style={{ position: "absolute", left: 0, width: 1920, top: 680, textAlign: "center", fontSize: 72, fontWeight: 700, color: C.lime, letterSpacing: "0.2em" }}>
          <TypeOn text="TRANSFORMER" cps={14} />
        </div>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S6
const CHAIN = ["THE", "TROPHY", "DIDN'T", "FIT", "IN", "THE", "SUITCASE", "BECAUSE"];
const Chain: React.FC<{ y: number; x0?: number; w?: number; step?: number }> = ({ y, x0 = 230, w = 150, step = 190 }) => {
  const f = useCurrentFrame();
  const pos = (f / 30) % CHAIN.length; // one word per 0.5 s
  return (
    <>
      {CHAIN.map((wd, k) => {
        const active = Math.floor(pos) === k;
        const age = (pos - k + CHAIN.length) % CHAIN.length;
        return (
          <div key={k} style={{ position: "absolute", left: x0 + k * step, top: y, width: w, height: 64, border: `3px solid ${active ? C.lime : C.chrome}`, borderRadius: 6, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22, fontWeight: 700, color: active ? C.lime : C.text, opacity: active ? 1 : 0.35 + 0.4 * Math.max(0, 1 - age / 4), background: C.bg }}>
            {wd}
            {k < CHAIN.length - 1 && <div style={{ position: "absolute", right: -(step - w) + 6, top: 29, width: step - w - 12, height: 4, background: C.chrome }} />}
          </div>
        );
      })}
    </>
  );
};

export const R1B_LSTM_GNMT: React.FC = () => {
  const { B, f, at } = useScene("R1B_LSTM_GNMT");
  const keep = 0.5 + 0.5 * Math.sin(f / 20);
  const forget = 0.5 + 0.5 * Math.sin(f / 20 + Math.PI);
  return (
    <Scene beats={B} hud={<SourceTag at={at(1)}>Hochreiter & Schmidhuber (1997) · Wu et al. (2016)</SourceTag>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 0, top: 0 }}>
          <Chain y={720} />
        </Appear>
        <Appear delay={20} style={{ left: 230, top: 670 }}>
          <Label size={18}>ONE WORD AFTER ANOTHER</Label>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <Card kicker="HOCHREITER & SCHMIDHUBER" title="1997 · LSTM" style={{ left: 160, top: 210 }} />
      </Beat>
      <Beat b={B[2]}>
        {/* memory column + gates */}
        <Appear style={{ left: 230, top: 370 }}>
          <Label size={18} style={{ marginBottom: 10 }}>MEMORY</Label>
          {Array.from({ length: 5 }).map((_, k) => {
            const v = 0.5 + 0.5 * Math.sin(f / 25 + k * 1.3);
            return <div key={k} style={{ width: 90, height: 34, marginBottom: 8, borderRadius: 4, border: `2px solid ${C.chrome}`, background: limeA(0.15 + 0.6 * v * keep), scale: String(1 + 0.05 * pulse(f, at(3, 140), 50)) }} />;
          })}
        </Appear>
        {[
          { t: "KEEP", c: C.lime, o: keep, y: 400 },
          { t: "FORGET", c: C.pumpkin, o: forget, y: 520 },
        ].map((g, k) => (
          <Appear key={g.t} delay={10 + k * 8} style={{ left: 360, top: g.y }}>
            <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
              <div style={{ width: 70, height: 70, border: `3px solid ${g.c}`, borderRadius: 6, position: "relative", overflow: "hidden" }}>
                <div style={{ position: "absolute", left: 0, top: 0, width: "100%", height: `${(1 - g.o) * 100}%`, background: g.c }} />
              </div>
              <span style={{ fontSize: 26, fontWeight: 700, color: g.c }}>{g.t}</span>
            </div>
          </Appear>
        ))}
      </Beat>
      <Beat b={B[3]}>
        <Card kicker="2016 · GNMT" title="GOOGLE TRANSLATE → LSTM" style={{ left: 820, top: 210 }} />
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 820, top: 372 }}>
          <Label size={18}>TRANSLATION ERRORS · INDEX</Label>
        </Appear>
        <BarChart
          style={{ left: 820, top: 420 }}
          length={560}
          labelWidth={250}
          thickness={50}
          gap={22}
          labelSize={24}
          max={100}
          items={[
            { label: "PHRASE-BASED", value: 100, at: 10, color: textA(0.5) },
            { label: "LSTM (GNMT)", value: 40, at: 40, color: C.lime, valueLabel: (v) => `≈${Math.round(v)}` },
          ]}
        />
        <Appear delay={110} style={{ left: 1090, top: 560 }}>
          <Tag color={C.lime} fill size={26}>−60% ERRORS (AVG.)</Tag>
        </Appear>
      </Beat>
      <Beat b={B[5]}>
        <Check p={ease(f, at(5, 4), at(5, 40))} size={72} style={{ left: 1500, top: 552 }} />
      </Beat>
      <Beat b={B[6]}>
        <Appear style={{ left: 1100, top: 652 }}>
          <Tag color={C.pumpkin} size={24}>STILL ONE WORD AT A TIME</Tag>
        </Appear>
        <div style={{ position: "absolute", left: 220, top: 710, width: 1480, height: 84, borderRadius: 10, border: `3px solid ${pumpkinA(0.7 * sp(f, at(6), 20) * (0.6 + 0.4 * Math.sin(f / 10)))}` }} />
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S9
const COLS = 50, ROWS = 21;
export const R2_SEQUENTIAL_GPU: React.FC = () => {
  const { B, f, at } = useScene("R2_SEQUENTIAL_GPU");
  const step = f < at(2) ? 0 : Math.floor((f - at(2)) / 14) + 1; // one core per step
  const idleP = ease(f, at(4), at(4, 40));
  const sweep = f >= at(3) ? ((f - at(3)) / 70) * (COLS + ROWS) : -1;
  return (
    <Scene beats={B} hud={<><IllustrativeTag label="ILLUSTRATIVE GRID" /></>}>
      <Beat b={B[0]}>
        <CoreGrid
          cols={COLS}
          rows={ROWS}
          cell={18}
          gap={6}
          appearAt={0}
          style={{ left: 360, top: 290 }}
          lit={(i) => {
            if (f < at(1)) return 0;
            if (i === step) return 1 * (0.7 + 0.3 * Math.sin(f / 4));
            if (i < step) return 0.15;
            if (i === 0 && step === 0) return sp(f, at(1), 20);
            const c = i % COLS, r = Math.floor(i / COLS);
            return sweep >= 0 && Math.abs(c + r - sweep) < 1.5 && f < at(3, 90) ? 0 : 0;
          }}
          idle={(i) => (i > step ? idleP : 0)}
        />
        {/* b4 sweep highlight across all cores */}
        {f >= at(3) && f < at(3, 90) && (
          <div style={{ position: "absolute", left: 360 + ((f - at(3)) / 90) * 1200 - 60, top: 280, width: 120, height: 524, background: textA(0.08), borderLeft: `3px solid ${textA(0.4)}` }} />
        )}
      </Beat>
      <Beat b={B[1]}>
        <Appear delay={10} style={{ left: 360, top: 222 }}>
          <Label color={C.lime} dim={false}>CORE 1 · WORKING</Label>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: 760, top: 222 }}>
          <div style={{ fontSize: 26, fontWeight: 700 }}>
            {["STEP 1", "STEP 2", "STEP 3", "…"].map((s, k) => (
              <span key={k} style={{ opacity: sp(f, at(2, k * 14), 14), color: k === Math.min(3, step - 1) ? C.lime : C.text }}>
                {s}
                {k < 3 && <span style={{ opacity: 0.5 }}> → </span>}
              </span>
            ))}
          </div>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <Appear style={{ left: 1290, top: 214 }}>
          <Tag color={C.text} size={24}>GPU · 1,000+ CORES</Tag>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 360, top: 812 }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 16 }}>
            <Label color={C.pumpkin} dim={false}>IDLE CORES</Label>
            <Counter to={COLS * ROWS - step - 1} size={40} color={C.pumpkin} dur={50} />
            <span style={{ fontSize: 26, fontWeight: 700, opacity: 0.6 }}>/ {fmt(COLS * ROWS)}</span>
          </div>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S10
const IN_W = ["the", "agreement", "was", "signed", "in", "August"];
const OUT_W = ["l'", "accord", "a", "été", "signé", "en", "août"];
const inX = (k: number) => 300 + k * 264;
const outX = (k: number) => 300 + k * 220;
export const R3_BAHDANAU_2014: React.FC = () => {
  const { B, f, at } = useScene("R3_BAHDANAU_2014");
  const yIn = 640, yOut = 400;
  const active = f < at(2) ? 1 : 4; // "accord" → "signé"
  const reach = ease(f, at(1, 60), at(1, 110)) * (f < at(2) ? 1 : ease(f, at(2, 10), at(2, 50)));
  const wt = ease(f, at(3), at(3, 50));
  const weights = [0.06, 0.05, 0.12, 0.7, 0.03, 0.04];
  const chain = ease(f, at(5), at(5, 40));
  return (
    <Scene beats={B} hud={<><SourceTag>Bahdanau, Cho & Bengio (2014), arXiv:1409.0473</SourceTag><IllustrativeTag at={at(1)} label="ILLUSTRATIVE WEIGHTS" /></>}>
      <Beat b={B[0]}>
        <Card kicker="BAHDANAU · CHO · BENGIO" title="2014 · MONTREAL" style={{ left: 160, top: 210 }} />
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: 160, top: yIn + 14 }}><Label size={18}>INPUT</Label></Appear>
        <Appear style={{ left: 160, top: yOut + 14 }}><Label size={18}>OUTPUT</Label></Appear>
        {IN_W.map((w, k) => (
          <Appear key={w + k} delay={k * 5} style={{ left: inX(k) - 100, top: yIn, width: 200, textAlign: "center" }}>
            <div style={{ fontSize: 32, fontWeight: 700, padding: "8px 0", border: `2px solid ${f >= at(3) && k === 3 ? C.lime : C.chrome}`, borderRadius: 6, background: C.bg }}>{w}</div>
          </Appear>
        ))}
        {OUT_W.map((w, k) => {
          const isAct = k === active;
          const vis = k <= active ? 1 : 0.25;
          return (
            <Appear key={w + k} delay={30 + k * 5} style={{ left: outX(k) - 90, top: yOut, width: 180, textAlign: "center", opacity: vis }}>
              <div style={{ fontSize: 32, fontWeight: 700, padding: "8px 0", border: `3px solid ${isAct ? C.lime : C.chrome}`, color: isAct ? C.lime : C.text, borderRadius: 6, background: C.bg }}>{w}</div>
            </Appear>
          );
        })}
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          {IN_W.map((_, k) => {
            const w = 3 + wt * (weights[k] * 26 - 3 + 1);
            return (
              <line
                key={k}
                x1={outX(active)}
                y1={yOut + 58}
                x2={outX(active) + (inX(k) - outX(active)) * reach}
                y2={yOut + 58 + (yIn - yOut - 58) * reach}
                stroke={C.lime}
                strokeWidth={Math.max(2, w)}
                strokeLinecap="round"
                opacity={0.35 + 0.65 * (wt > 0 ? weights[k] / 0.7 : 1) * (reach > 0 ? 1 : 0)}
              />
            );
          })}
        </svg>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: outX(4) - 90, top: yOut - 50, width: 180, textAlign: "center" }}>
          <Label size={16} color={C.lime} dim={false}>WRITING NOW</Label>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <Appear delay={20} style={{ left: 1200, top: 560 }}>
          <Label size={18}>LINE WIDTH = WEIGHT</Label>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 1150, top: 228 }}>
          <div style={{ fontSize: 76, fontWeight: 700, color: C.lime, letterSpacing: "0.12em", textShadow: `0 0 ${30 * pulse(f, at(4, 10), 60)}px ${limeA(0.7)}` }}>ATTENTION</div>
        </Appear>
      </Beat>
      <Beat b={B[5]}>
        {/* grey sequential chain bolted under the input */}
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          {IN_W.slice(0, -1).map((_, k) => (
            <line key={k} x1={inX(k) + 100} y1={yIn + 30} x2={inX(k) + 100 + 64 * chain} y2={yIn + 30} stroke={C.text} strokeOpacity={0.6} strokeWidth={6} />
          ))}
          {(() => {
            const pk = Math.floor(((f - at(5)) / 24) % IN_W.length);
            return <rect x={inX(pk) - 104} y={yIn - 4} width={208} height={66} rx={8} fill="none" stroke={C.pumpkin} strokeWidth={4} opacity={chain} />;
          })()}
        </svg>
        <Appear delay={30} style={{ left: 1150, top: 740 }}>
          <Tag color={C.pumpkin} size={26}>STILL SEQUENTIAL</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S13
export const R4_PAPER_CARD: React.FC = () => {
  const { B, f, at } = useScene("R4_PAPER_CARD");
  const shuffle = ease(f, at(4, 6), at(4, 50));
  const perm = [5, 2, 7, 0, 3, 6, 1, 4];
  const star = sp(f, at(3, 10), 20);
  return (
    <Scene beats={B} hud={<SourceTag>Vaswani et al. (2017), arXiv:1706.03762</SourceTag>}>
      <Beat b={B[0]}>
        <Appear dx={-60} dy={0} style={{ left: 200, top: 260 }}>
          <Paper w={340} h={460} accent={C.lime} />
        </Appear>
        <Appear delay={20} style={{ left: 640, top: 250 }}>
          <div style={{ display: "flex", gap: 18, alignItems: "center" }}>
            <Tag color={C.lime} fill>NeurIPS 2017</Tag>
            <Label>arXiv:1706.03762</Label>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <div style={{ position: "absolute", left: 640, top: 340, fontSize: 66, fontWeight: 700 }}>
          <TypeOn text="ATTENTION IS ALL YOU NEED" cps={16} />
        </div>
      </Beat>
      <Beat b={B[2]}>
        {AUTHORS.map((a, k) => {
          const slot = interpolate(shuffle, [0, 1], [k, perm[k]]);
          const lift = Math.sin(shuffle * Math.PI) * (k % 2 ? -40 : 40);
          return (
            <Appear key={a.i} delay={k * 3} style={{ left: 640 + slot * 128, top: 480 + lift }}>
              <div style={{ width: 96, height: 96, borderRadius: 48, border: `3px solid ${C.lime}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 30, fontWeight: 700, background: C.bg, position: "relative" }}>
                {a.i}
                <span style={{ position: "absolute", right: -6, top: -14, fontSize: 40, color: C.lime, opacity: star }}>*</span>
              </div>
            </Appear>
          );
        })}
      </Beat>
      <Beat b={B[3]}>
        <Appear style={{ left: 640, top: 640 }}>
          <div style={{ border: `2px solid ${C.chrome}`, borderLeft: `8px solid ${C.lime}`, background: chromeA(0.28), borderRadius: 6, padding: "18px 28px" }}>
            <div style={{ fontSize: 30, fontWeight: 700 }}>
              <span style={{ color: C.lime }}>* </span>EQUAL CONTRIBUTION
            </div>
            <div style={{ fontSize: 30, fontWeight: 700, marginTop: 10, color: C.lime, opacity: sp(f, at(4, 30), 20), height: sp(f, at(4, 30), 20) * 40 }}>LISTING ORDER IS RANDOM</div>
          </div>
        </Appear>
      </Beat>
      <Beat b={B[4]}><span /></Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S22
const HeadPanel: React.FC<{ x: number; label: string; words: string[]; from: number; to: number; delay?: number }> = ({ x, label, words, from, to }) => {
  const f = useCurrentFrame();
  const p = ease(f, 20, 60);
  const ws = 470 / words.length;
  const cx = (k: number) => x + 25 + ws * k + ws / 2;
  const y = 680;
  const x1 = cx(from), x2 = cx(to);
  const h = 80 + Math.abs(x2 - x1) * 0.25;
  return (
    <Appear style={{ left: 0, top: 0 }}>
      <div style={{ position: "absolute", left: x, top: 470, width: 520, height: 290, border: `2px solid ${C.chrome}`, borderRadius: 8, background: chromeA(0.2) }}>
        <div style={{ position: "absolute", left: 24, top: 20, fontSize: 24, fontWeight: 700, color: C.lime }}>{label}</div>
      </div>
      <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
        <path d={`M ${x1} ${y - 30} C ${x1} ${y - 30 - h}, ${x2} ${y - 30 - h}, ${x2} ${y - 34}`} fill="none" stroke={C.lime} strokeWidth={6} pathLength={1} strokeDasharray={`${p} 1`} strokeLinecap="round" />
        <circle cx={x2} cy={y - 34} r={9} fill={C.lime} opacity={p > 0.95 ? 1 : 0} />
      </svg>
      {words.map((w, k) => (
        <div key={k} style={{ position: "absolute", left: cx(k) - ws / 2, width: ws, top: y - 20, textAlign: "center", fontSize: 30, fontWeight: 700, color: k === from || k === to ? C.text : textA(0.6) }}>
          {w}
        </div>
      ))}
    </Appear>
  );
};

export const R4B_WHAT_HEADS_LEARN: React.FC = () => {
  const { B, f, at } = useScene("R4B_WHAT_HEADS_LEARN");
  const scan = f >= at(2) ? Math.floor((f - at(2)) / 9) : -1;
  const pick = [
    { k: 3, at: at(3) },
    { k: 7, at: at(4) },
    { k: 10, at: at(5) },
  ];
  return (
    <Scene beats={B} hud={<><SourceTag at={at(1)}>Clark, Khandelwal, Levy & Manning (2019), BlackboxNLP</SourceTag><IllustrativeTag at={at(3)} label="ILLUSTRATIVE SENTENCES" /></>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 160, top: 352 }}><Label size={18}>ATTENTION HEADS</Label></Appear>
        {Array.from({ length: 12 }).map((_, k) => {
          const chosen = pick.find((p) => p.k === k && f >= p.at);
          const scanning = scan >= 0 && scan % 12 === k && f < at(3);
          return (
            <Appear key={k} delay={k * 3} style={{ left: 160 + k * 80, top: 390 }}>
              <div style={{ width: 66, height: 46, borderRadius: 4, border: `3px solid ${chosen || scanning ? C.lime : C.chrome}`, background: chosen ? C.lime : scanning ? limeA(0.3) : chromeA(0.3) }} />
            </Appear>
          );
        })}
      </Beat>
      <Beat b={B[1]}>
        <Card kicker="2019 · STANFORD" title="Clark, Khandelwal, Levy, Manning" titleSize={38} style={{ left: 160, top: 206 }} />
        <Appear delay={150} style={{ left: 1150, top: 386 }}>
          <Tag color={C.text}>MODEL: BERT</Tag>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: 1150, top: 440 }}><Label size={16} color={C.lime} dim={false}>ONE BY ONE</Label></Appear>
      </Beat>
      <Beat b={B[3]}>
        <HeadPanel x={160} label="VERB → OBJECT" words={["she", "ate", "the", "apple"]} from={1} to={3} />
      </Beat>
      <Beat b={B[4]}>
        <HeadPanel x={700} label="NOUN → ARTICLE" words={["the", "old", "house"]} from={2} to={0} />
      </Beat>
      <Beat b={B[5]}>
        <HeadPanel x={1240} label="PRONOUN → REFERENT" words={["Ana", "said", "she", "left"]} from={2} to={0} />
      </Beat>
      <Beat b={B[6]}>
        <Appear style={{ left: 1400, top: 380 }}>
          <Tag color={C.lime} fill size={26}>FOUND, NOT PROGRAMMED</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S25
export const R5_TRAINING_COST: React.FC = () => {
  const { B, f, at } = useScene("R5_TRAINING_COST");
  const cols = 30, rows = 16;
  const seqStep = Math.floor(f / 12);
  const allOn = f >= at(2);
  const snap = ease(f, at(1, 20), at(1, 60));
  return (
    <Scene beats={B} hud={<><SourceTag at={at(3)}>Vaswani et al. (2017), §5.2</SourceTag><IllustrativeTag label="ILLUSTRATIVE GRID" /></>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 160, top: 280 }}><Label size={18}>GPU CORES</Label></Appear>
        <CoreGrid
          cols={cols}
          rows={rows}
          cell={16}
          gap={6}
          style={{ left: 160, top: 320 }}
          lit={(i) => {
            if (allOn) {
              const c = i % cols, r = Math.floor(i / cols);
              return sp(f, at(2, (c + r) * 0.8), 14) * (0.8 + 0.2 * Math.sin(f / 6 + i));
            }
            return i === seqStep % (cols * rows) ? 1 : 0;
          }}
        />
      </Beat>
      <Beat b={B[1]}>
        {/* the step-by-step chain snaps */}
        {Array.from({ length: 6 }).map((_, k) => (
          <React.Fragment key={k}>
            <div style={{ position: "absolute", left: 160 + k * 112 - snap * (2.5 - k) * 10, top: 708, width: 70, height: 44, borderRadius: 6, border: `3px solid ${C.text}`, opacity: sp(f, at(1, k * 3), 14) }} />
            {k < 5 && <div style={{ position: "absolute", left: 160 + k * 112 + 72, top: 728, width: 38, height: 5, background: C.pumpkin, opacity: sp(f, at(1, k * 3), 14) * (1 - snap), rotate: `${snap * 40 * (k % 2 ? 1 : -1)}deg` }} />}
          </React.Fragment>
        ))}
        <Appear delay={60} style={{ left: 160, top: 770 }}><Label size={18}>NO STEP DEPENDS ON THE LAST</Label></Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear delay={20} style={{ left: 600, top: 280 }}><Label size={18} color={C.lime} dim={false}>ALL AT ONCE</Label></Appear>
      </Beat>
      <Beat b={B[3]}>
        <Card kicker="HARDWARE" title="8 × NVIDIA P100" style={{ left: 980, top: 230 }} />
        <Appear delay={20} style={{ left: 980, top: 420 }}>
          <Label size={20}>BASE MODEL</Label>
          <div style={{ display: "flex", alignItems: "baseline", gap: 14, marginTop: 6 }}>
            <Counter to={12} size={96} color={C.lime} delay={20} dur={90} />
            <span style={{ fontSize: 44, fontWeight: 700 }}>HOURS</span>
          </div>
          <div style={{ width: 700, height: 10, background: C.chrome, borderRadius: 5, marginTop: 12 }}>
            <div style={{ width: `${ease(f, at(3, 20), at(3, 110)) * (12 / 84) * 100}%`, height: 10, background: C.lime, borderRadius: 5 }} />
          </div>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 980, top: 600 }}>
          <Label size={20}>BIG MODEL</Label>
          <div style={{ display: "flex", alignItems: "baseline", gap: 14, marginTop: 6 }}>
            <Counter to={3.5} decimals={1} size={96} color={C.lime} dur={90} />
            <span style={{ fontSize: 44, fontWeight: 700 }}>DAYS</span>
          </div>
          <div style={{ width: 700, height: 10, background: C.chrome, borderRadius: 5, marginTop: 12 }}>
            <div style={{ width: `${ease(f, at(4), at(4, 100)) * 100}%`, height: 10, background: C.lime, borderRadius: 5 }} />
          </div>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S26
export const R6_BLEU: React.FC = () => {
  const { B, f, at } = useScene("R6_BLEU");
  const L = 1000, LW = 320, th = 46, gp = 16, max = 45;
  const prev = textA(0.45);
  const bx = (v: number) => 160 + LW + (v / max) * L;
  return (
    <Scene beats={B} hud={<><SourceTag>Vaswani et al. (2017), Table 2</SourceTag><IllustrativeTag at={at(4)} label="ILLUSTRATIVE COST SCALE" /></>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 160, top: 206 }}>
          <div style={{ fontSize: 32, fontWeight: 700 }}>ENGLISH → GERMAN · BLEU</div>
        </Appear>
      </Beat>
      <BarChart
        style={{ left: 160, top: 262 }}
        length={L}
        labelWidth={LW}
        thickness={th}
        gap={gp}
        labelSize={24}
        max={max}
        items={[
          { label: "PREVIOUS BEST", value: 26.36, at: 30, color: prev, valueLabel: () => "" },
          { label: "TRANSFORMER", value: 28.4, at: at(1, 6), valueLabel: (v) => v.toFixed(1) },
        ]}
      />
      <Beat b={B[1]}><span /></Beat>
      <Beat b={B[2]}>
        <div style={{ position: "absolute", left: bx(26.36), top: 256, width: bx(28.4) - bx(26.36), height: 2 * th + gp + 12, border: `3px solid ${C.lime}`, borderRadius: 4, opacity: sp(f, at(2), 20), boxSizing: "border-box" }} />
        <Appear delay={10} style={{ left: bx(28.4) + 130, top: 266 }}>
          <Tag color={C.lime} fill size={24}>&gt; 2 POINTS ABOVE</Tag>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <Appear style={{ left: 160, top: 424 }}>
          <div style={{ fontSize: 32, fontWeight: 700 }}>ENGLISH → FRENCH · BLEU</div>
        </Appear>
        <BarChart
          style={{ left: 160, top: 480 }}
          length={L}
          labelWidth={LW}
          thickness={th}
          gap={gp}
          labelSize={24}
          max={max}
          items={[
            { label: "PREVIOUS BEST", value: 41.29, at: 6, color: prev, valueLabel: () => "" },
            { label: "TRANSFORMER", value: 41.8, at: 30, valueLabel: (v) => v.toFixed(1) },
          ]}
        />
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 160, top: 638 }}>
          <div style={{ fontSize: 32, fontWeight: 700 }}>TRAINING COST</div>
        </Appear>
        <BarChart
          style={{ left: 160, top: 690 }}
          length={L}
          labelWidth={LW}
          thickness={34}
          gap={12}
          labelSize={22}
          max={100}
          items={[
            { label: "EARLIER TOP MODELS", value: 100, at: 10, color: C.pumpkin, valueLabel: () => "" },
            { label: "TRANSFORMER", value: 12, at: 40, valueLabel: () => "" },
          ]}
        />
        <Appear delay={90} style={{ left: 160 + LW + 0.12 * L + 30, top: 728 }}>
          <Tag color={C.lime} size={22}>A SMALL FRACTION</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S28
const MiniCard: React.FC<{ x: number; y: number; w: number; kicker: string; title: string; accent?: string; children?: React.ReactNode }> = ({ x, y, w, kicker, title, accent = C.lime, children }) => (
  <Appear style={{ left: x, top: y, width: w }}>
    <div style={{ border: `2px solid ${C.chrome}`, borderTop: `6px solid ${accent}`, background: C.bg, borderRadius: 6, padding: "16px 24px" }}>
      <Label size={18}>{kicker}</Label>
      <div style={{ fontSize: 46, fontWeight: 700, marginTop: 6, color: accent === C.lime ? C.text : accent }}>{title}</div>
      {children}
    </div>
  </Appear>
);

export const R7_TIMELINE_2018_2022: React.FC = () => {
  const { B, f, at } = useScene("R7_TIMELINE_2018_2022");
  const X = 220, W = 1480, Y = 540;
  const ax = (t: number) => axisX(t, X, W, 2017, 2023);
  const gptHL = ease(f, at(1, 190), at(1, 230));
  const stem = (x: number, y1: number, y2: number, a: number) => (
    <div style={{ position: "absolute", left: x - 1.5, top: Math.min(y1, y2), width: 3, height: Math.abs(y2 - y1) * sp(f, a, 24), background: C.chrome }} />
  );
  return (
    <Scene beats={B} hud={<SourceTag at={at(1)}>Radford 2018 · Devlin 2018 · Brown 2020 · OpenAI 2022</SourceTag>}>
      <Beat b={B[0]}>
        <TimelineAxis
          x={X}
          y={Y}
          width={W}
          from={2017}
          to={2023}
          step={1}
          drawDur={90}
          markers={[
            { t: 2017.45, at: 60, color: C.text },
            { t: 2018.45, at: at(1), color: C.lime },
            { t: 2018.8, at: at(2), color: C.lime },
            { t: 2020.4, at: at(3), color: C.lime },
            { t: 2022.9, at: at(5), color: C.lime },
          ]}
        />
        <Appear delay={80} style={{ left: 160, top: 440 }}>
          <Tag color={C.text} size={20}>2017 · TRANSFORMER</Tag>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        {stem(ax(2018.45), Y - 14, 410, at(1, 10))}
        <MiniCard x={ax(2018.45) - 160} y={220} w={560} kicker="2018 · OPENAI" title="GPT">
          <div style={{ fontSize: 24, fontWeight: 700, marginTop: 8, whiteSpace: "nowrap" }}>
            {["GENERATIVE", "PRE-TRAINED", "TRANSFORMER"].map((w, k) => (
              <span key={k}>
                <span style={{ color: gptHL > 0.5 ? C.lime : C.text, fontSize: 24 + 8 * gptHL }}>{w[0]}</span>
                {w.slice(1)}{" "}
              </span>
            ))}
          </div>
        </MiniCard>
      </Beat>
      <Beat b={B[2]}>
        {stem(ax(2018.8), Y + 14, 640, at(2, 10))}
        <MiniCard x={ax(2018.8) - 150} y={640} w={420} kicker="2018 · GOOGLE" title="BERT">
          <div style={{ fontSize: 22, fontWeight: 500, marginTop: 6, opacity: 0.85 }}>← READS BOTH DIRECTIONS →</div>
        </MiniCard>
      </Beat>
      <Beat b={B[3]}>
        {stem(ax(2020.4), Y - 14, 470, at(3, 10))}
        <MiniCard x={ax(2020.4) - 170} y={208} w={470} kicker="2020 · OPENAI" title="GPT-3">
          <div style={{ display: "flex", alignItems: "baseline", gap: 12, marginTop: 6 }}>
            <Counter to={96} size={44} color={C.lime} dur={50} />
            <span style={{ fontSize: 24, fontWeight: 700 }}>LAYERS</span>
          </div>
          <div style={{ display: "flex", alignItems: "baseline", gap: 12, marginTop: 4, opacity: f >= at(4) ? 1 : 0, height: f >= at(4) ? 50 : 0 }}>
            <Counter to={175} size={44} color={C.lime} dur={60} delay={at(4) - at(3)} />
            <span style={{ fontSize: 24, fontWeight: 700 }}>BILLION PARAMETERS</span>
          </div>
        </MiniCard>
      </Beat>
      <Beat b={B[4]}>
        <div style={{ position: "absolute", left: ax(2020.4) - 30, top: Y - 30, width: 60, height: 60, borderRadius: 30, border: `3px solid ${C.lime}`, opacity: pulse(f, at(4, 10), 60) }} />
      </Beat>
      <Beat b={B[5]}>
        {stem(ax(2022.9), Y + 14, 640, at(5, 10))}
        <MiniCard x={1330} y={640} w={430} kicker="NOV 2022" title="ChatGPT">
          <div style={{ height: 6, marginTop: 10, width: `${ease(f, at(5, 30), at(5, 120)) * 100}%`, background: C.lime, borderRadius: 3 }} />
        </MiniCard>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S29
export const R8_PARAM_GROWTH: React.FC = () => {
  const { B, f, at } = useScene("R8_PARAM_GROWTH");
  const base = 740, H = 420, bw = 180, x1 = 500, x2 = 1060;
  const grow = ease(f, at(1, 4), at(1, 60)); // GPT-3 bar overshoots
  const rescale = ease(f, at(1, 70), at(1, 150));
  const maxV = Math.pow(10, interpolate(rescale, [0, 1], [Math.log10(250e6), Math.log10(200e9)]));
  const h1 = Math.max(4, (213e6 / maxV) * H) * sp(f, 10, 50);
  const h2fit = (175e9 / 200e9) * H;
  const h2 = f < at(1) ? 0 : interpolate(rescale, [0, 1], [grow * 900, h2fit]);
  const tilt = interpolate(grow, [0, 1], [0, 160]) * (1 - rescale);
  const ticks = [0.5, 1].map((u) => u * maxV);
  const lbl = (v: number) => (v >= 1e9 ? `${fmt(v / 1e9)}B` : `${fmt(v / 1e6)}M`);
  const stack = (x: number, n: number, gapPx: number, slab: number, a: number) =>
    Array.from({ length: n }).map((_, k) => (
      <div key={k} style={{ position: "absolute", left: x, top: base - (k + 1) * (slab + gapPx), width: 70, height: slab, background: C.lime, opacity: sp(f, a + k * (n > 20 ? 0.6 : 4), 10) * 0.85, borderRadius: 1 }} />
    ));
  return (
    <Scene beats={B} hud={<SourceTag>Vaswani et al. 2017 (Table 3) · Brown et al. 2020</SourceTag>}>
      <div style={{ position: "absolute", left: 0, top: tilt, width: 1920, height: 1080 }}>
        <Beat b={B[0]}>
          <Appear style={{ left: 160, top: 214 }}><Label>PARAMETERS</Label></Appear>
          {ticks.map((v, k) => (
            <div key={k} style={{ position: "absolute", left: 380, width: 1100, top: base - (v / maxV) * H, borderTop: `2px dashed ${C.chrome}`, opacity: sp(f, 30 + k * 8, 20) }}>
              <Label size={18} style={{ position: "absolute", left: -110, top: -12, width: 90, textAlign: "right" }}>{lbl(v)}</Label>
            </div>
          ))}
          <div style={{ position: "absolute", left: 380, width: 1100, top: base, height: 3, background: C.chrome }} />
          <div style={{ position: "absolute", left: x1, top: base - h1, width: bw, height: h1, background: C.text, borderRadius: "4px 4px 0 0" }} />
          <div style={{ position: "absolute", left: x1 - 60, width: bw + 120, textAlign: "center", top: base - h1 - 60 }}>
            <Counter to={213} suffix=" MILLION" size={34} dur={60} delay={10} />
          </div>
          <div style={{ position: "absolute", left: x1 - 80, width: bw + 160, textAlign: "center", top: base + 16 }}>
            <div style={{ fontSize: 26, fontWeight: 700 }}>TRANSFORMER (BIG)</div>
            <Label size={18}>2017</Label>
          </div>
        </Beat>
        <Beat b={B[1]}>
          <div style={{ position: "absolute", left: x2, top: base - h2, width: bw, height: h2, background: C.lime, borderRadius: "4px 4px 0 0", boxShadow: `0 0 30px ${limeA(0.4)}` }} />
          <div style={{ position: "absolute", left: x2 - 60, width: bw + 120, textAlign: "center", top: base - h2 - 60 }}>
            <Counter to={175} suffix=" BILLION" size={34} color={C.lime} dur={60} />
          </div>
          <div style={{ position: "absolute", left: x2 - 80, width: bw + 160, textAlign: "center", top: base + 16 }}>
            <div style={{ fontSize: 26, fontWeight: 700 }}>GPT-3</div>
            <Label size={18}>2020</Label>
          </div>
        </Beat>
      </div>
      <Beat b={B[2]}>
        <Appear style={{ left: 720, top: 330 }}>
          <div style={{ fontSize: 110, fontWeight: 700, color: C.lime }}>
            ≈<Counter to={820} suffix="×" size={110} color={C.lime} dur={70} />
          </div>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        {[x1, x2].map((x, k) => (
          <Appear key={k} delay={k * 6} style={{ left: x + bw + 24, top: 236 }}>
            <svg width={70} height={70} viewBox="0 0 70 70">
              <rect x={3} y={3} width={64} height={64} rx={6} fill="none" stroke={C.lime} strokeWidth={5} />
              <rect x={14} y={16} width={42} height={12} fill={C.lime} />
              <rect x={14} y={40} width={42} height={12} fill={C.text} />
            </svg>
          </Appear>
        ))}
        <Appear delay={10} style={{ left: 1360, top: 248 }}>
          <Tag color={C.lime} size={24}>SAME CORE BLOCK</Tag>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        {stack(x1 + bw + 24, 12, 4, 10, at(4))}
        {stack(x2 + bw + 24, 96, 1.2, 3, at(4))}
        <Appear delay={20} style={{ left: x1 + bw + 20, top: base + 16 }}><Label size={18}>6 + 6 LAYERS</Label></Appear>
        <Appear delay={40} style={{ left: x2 + bw + 20, top: base + 16 }}><Label size={18}>96 LAYERS</Label></Appear>
      </Beat>
      <Beat b={B[5]}>
        {Array.from({ length: 10 }).map((_, k) => (
          <Appear key={k} delay={k * 5} style={{ left: 1460 + (k % 5) * 54, top: 520 + Math.floor(k / 5) * 100 }}>
            <div style={{ width: 44, height: 60, border: `3px solid ${C.text}`, borderRadius: 4, padding: 6, boxSizing: "border-box" }}>
              {[0, 1, 2].map((i) => <div key={i} style={{ height: 4, background: C.chrome, marginBottom: 6 }} />)}
            </div>
          </Appear>
        ))}
        <Appear delay={30} style={{ left: 1460, top: 740 }}><Label size={18}>TRAINING TEXT</Label></Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S31
export const R8B_SCALING_LAWS: React.FC = () => {
  const { B, f, at } = useScene("R8B_SCALING_LAWS");
  const X0 = 360, X1 = 1260, Y0 = 260, Y1 = 740;
  const pts = Array.from({ length: 8 }).map((_, k) => {
    const u = 0.06 + k * 0.1;
    const v = 0.12 + u * 0.72 + (random(`sl${k}`) - 0.5) * 0.03;
    return { x: X0 + u * (X1 - X0), y: Y0 + v * (Y1 - Y0), u };
  });
  const lineP = ease(f, at(3), at(3, 70));
  const ext = ease(f, at(4), at(4, 60));
  const lx = (u: number) => X0 + u * (X1 - X0);
  const ly = (u: number) => Y0 + (0.12 + u * 0.72) * (Y1 - Y0);
  return (
    <Scene beats={B} hud={<><SourceTag at={at(1)}>Kaplan et al. (2020), arXiv:2001.08361</SourceTag><IllustrativeTag label="ILLUSTRATIVE SHAPE" /></>}>
      <Beat b={B[0]}>
        <Appear style={{ left: X0, top: 200 }}><div style={{ fontSize: 32, fontWeight: 700 }}>MODEL SIZE vs ERROR</div></Appear>
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          <path d={`M ${X0} ${Y0} L ${X0} ${Y1} L ${X1} ${Y1}`} fill="none" stroke={C.chrome} strokeWidth={4} pathLength={1} strokeDasharray={`${ease(f, 0, 60)} 1`} />
          {[0.25, 0.5, 0.75].map((u) => (
            <React.Fragment key={u}>
              <line x1={X0 + u * (X1 - X0)} x2={X0 + u * (X1 - X0)} y1={Y0} y2={Y1} stroke={C.chrome} strokeDasharray="6 8" strokeWidth={2} opacity={sp(f, 40, 30)} />
              <line x1={X0} x2={X1} y1={Y0 + u * (Y1 - Y0)} y2={Y0 + u * (Y1 - Y0)} stroke={C.chrome} strokeDasharray="6 8" strokeWidth={2} opacity={sp(f, 50, 30)} />
            </React.Fragment>
          ))}
        </svg>
        <Appear delay={50} style={{ left: X0, top: Y1 + 20 }}><Label size={18}>MODEL SIZE (LOG)</Label></Appear>
        <Appear delay={60} style={{ left: X0 - 230, top: Y0 + 4 }}><Label size={18}>ERROR (LOG)</Label></Appear>
      </Beat>
      <Beat b={B[1]}>
        <Card kicker="OPENAI" title="2020 · Kaplan et al." sub="SCALING LAWS" style={{ left: 1320, top: 260 }} />
      </Beat>
      <Beat b={B[2]}>
        {pts.map((p, k) => {
          const q = sp(f, k * 18, 24);
          return <div key={k} style={{ position: "absolute", left: p.x - 12, top: p.y - 12 - 80 * (1 - q), width: 24, height: 24, borderRadius: 12, background: C.lime, opacity: q }} />;
        })}
      </Beat>
      <Beat b={B[3]}>
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          <line x1={lx(0.02)} y1={ly(0.02)} x2={lx(0.02 + 0.76 * lineP)} y2={ly(0.02 + 0.76 * lineP)} stroke={C.lime} strokeWidth={6} strokeLinecap="round" />
        </svg>
      </Beat>
      <Beat b={B[4]}>
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          <line x1={lx(0.78)} y1={ly(0.78)} x2={lx(0.78 + 0.2 * ext)} y2={ly(0.78 + 0.2 * ext)} stroke={C.lime} strokeWidth={6} strokeDasharray="14 12" strokeDashoffset={-f} />
          <circle cx={lx(0.98)} cy={ly(0.98)} r={14 + 8 * pulse(f, at(4, 60) - at(4) + at(4), 50)} fill="none" stroke={C.lime} strokeWidth={4} opacity={ext} />
        </svg>
        <Appear delay={40} style={{ left: 1320, top: 600 }}>
          <Tag color={C.lime} fill size={26}>BIGGER → PREDICTABLY BETTER</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S32
export const R9_CHATGPT_USERS: React.FC = () => {
  const { B, f, at } = useScene("R9_CHATGPT_USERS");
  const X0 = 200, X1 = 1060, Y0 = 280, Y1 = 740, maxU = 120e6, maxT = 3;
  const t = f < at(1) ? ease(f, 20, at(1)) * 1.55 : 1.55 + ease(f, at(1), at(1, 90)) * 0.45;
  const users = (tt: number) => 100e6 * Math.pow(tt / 2, 1.7);
  const px = (tt: number) => X0 + (tt / maxT) * (X1 - X0);
  const py = (u: number) => Y1 - (u / maxU) * (Y1 - Y0);
  const N = 60;
  const d = Array.from({ length: N + 1 }).map((_, i) => {
    const tt = (i / N) * t;
    return `${i ? "L" : "M"} ${px(tt)} ${py(users(tt))}`;
  }).join(" ");
  const done = f >= at(1, 90);
  return (
    <Scene beats={B} hud={<><SourceTag at={at(2)}>UBS estimate, Feb 2023 (Reuters)</SourceTag><IllustrativeTag label="ILLUSTRATIVE CURVE" /></>}>
      <Beat b={B[0]}>
        <svg width={1920} height={1080} style={{ position: "absolute", left: 0, top: 0 }}>
          <line x1={X0} y1={Y1} x2={X1} y2={Y1} stroke={C.chrome} strokeWidth={4} />
          <line x1={X0} y1={Y0} x2={X0} y2={Y1} stroke={C.chrome} strokeWidth={4} />
          {[50e6, 100e6].map((u) => (
            <line key={u} x1={X0} x2={X1} y1={py(u)} y2={py(u)} stroke={u === 100e6 && done ? C.lime : C.chrome} strokeWidth={2} strokeDasharray="8 8" opacity={0.6 + 0.4 * pulse(f, u === 50e6 ? 190 : at(1, 80), 40)} />
          ))}
          <path d={d} fill="none" stroke={C.lime} strokeWidth={7} strokeLinecap="round" />
          <circle cx={px(t)} cy={py(users(t))} r={13} fill={C.lime} />
        </svg>
        {[
          { u: 50e6, l: "50M" },
          { u: 100e6, l: "100M" },
        ].map((g) => (
          <Label key={g.l} size={18} style={{ position: "absolute", left: X0 - 90, width: 76, textAlign: "right", top: py(g.u) - 12 }}>{g.l}</Label>
        ))}
        {["LAUNCH", "1 MO", "2 MO", "3 MO"].map((l, k) => (
          <Label key={l} size={18} style={{ position: "absolute", left: px(k) - 60, width: 120, textAlign: "center", top: Y1 + 18 }}>{l}</Label>
        ))}
        <Appear style={{ left: 1180, top: 300 }}>
          <Label>MONTHLY USERS</Label>
          <div style={{ marginTop: 10 }}>
            <Counter to={Math.round(users(t))} size={92} color={C.lime} dur={1} />
          </div>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <div style={{ position: "absolute", left: px(2) - 2, top: Y0, width: 4, height: Y1 - Y0, background: C.lime, opacity: sp(f, at(1, 70), 20) * 0.7 }} />
        <Appear delay={80} style={{ left: px(2) - 90, top: Y0 - 56 }}>
          <Tag color={C.lime} fill size={24}>≈2 MONTHS</Tag>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: 1180, top: 480 }}>
          <Tag color={C.lime} size={26}>FASTEST CONSUMER-APP GROWTH</Tag>
        </Appear>
        <Appear delay={20} style={{ left: 1180, top: 548 }}>
          <Label size={18}>PER UBS ANALYSTS</Label>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S35
export const R10_QUADRATIC_TABLE: React.FC = () => {
  const { B, f, at } = useScene("R10_QUADRATIC_TABLE");
  const dense = ease(f, at(3), at(3, 60));
  const n = Math.round(interpolate(dense, [0, 1], [8, 40]));
  const G = 380, gx = 1340, gy = 300;
  const cell = G / n;
  const fill = ease(f, 10, 120);
  return (
    <Scene beats={B} hud={<SourceTag>n tokens → n × n comparisons · ≈100,000-token novel is an estimate</SourceTag>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 160, top: 280 }}>
          <Counter to={1000} size={84} dur={40} />
          <Label style={{ marginTop: 10 }}>TOKENS</Label>
        </Appear>
        <Arrow x1={470} y1={322} x2={590} y2={322} p={ease(f, 40, 70)} color={C.text} width={5} />
        <Appear delay={60} style={{ left: 620, top: 280 }}>
          <Counter to={1000000} size={84} dur={60} delay={60} />
          <Label style={{ marginTop: 10 }}>COMPARISONS</Label>
        </Appear>
        <Appear style={{ left: gx, top: gy - 50 }}><Label size={18}>TOKENS × TOKENS</Label></Appear>
        <svg width={G} height={G} style={{ position: "absolute", left: gx, top: gy, overflow: "hidden" }}>
          <rect width={G} height={G} fill="none" stroke={C.chrome} strokeWidth={3} />
          {Array.from({ length: n * n }).map((_, i) => {
            const c = i % n, r = Math.floor(i / n);
            const on = dense > 0 ? 1 : fill * n * n > i ? 1 : 0;
            return <rect key={i} x={c * cell + 1} y={r * cell + 1} width={cell - 2} height={cell - 2} fill={dense > 0.5 ? C.pumpkin : C.lime} opacity={on * (0.25 + 0.5 * random(`q${i % 97}`))} />;
          })}
        </svg>
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: 620, top: 432 }}>
          <Tag color={C.text} size={22} style={{ boxShadow: `0 0 ${24 * pulse(f, at(4, 10), 50)}px ${textA(0.6)}` }}>PER HEAD, PER LAYER</Tag>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <Appear style={{ left: 160, top: 560 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
            <svg width={56} height={70} viewBox="0 0 56 70">
              <rect x={4} y={4} width={48} height={62} rx={4} fill="none" stroke={C.text} strokeWidth={4} />
              <line x1={14} y1={4} x2={14} y2={66} stroke={C.text} strokeWidth={4} />
              <line x1={22} y1={22} x2={44} y2={22} stroke={C.chrome} strokeWidth={4} />
              <line x1={22} y1={34} x2={44} y2={34} stroke={C.chrome} strokeWidth={4} />
            </svg>
            <Counter to={100000} size={72} dur={60} prefix="≈" />
          </div>
          <Label style={{ marginTop: 10 }}>TOKENS · A NOVEL · APPROX.</Label>
        </Appear>
      </Beat>
      <Beat b={B[3]}>
        <Arrow x1={510} y1={606} x2={600} y2={606} p={ease(f, at(3), at(3, 20))} color={C.pumpkin} width={5} />
        <Appear delay={10} style={{ left: 620, top: 566 }}>
          <Counter to={10_000_000_000} from={1000000} log size={72} color={C.pumpkin} dur={80} delay={10} />
          <Label style={{ marginTop: 10 }} color={C.pumpkin} dim={false}>COMPARISONS</Label>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Appear style={{ left: 620, top: 712 }}>
          <Tag color={C.pumpkin} size={22}>PER HEAD, PER LAYER</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S36
const MiniMat: React.FC<{ x: number; y: number; seed: string }> = ({ x, y, seed }) => (
  <svg width={150} height={150} style={{ position: "absolute", left: x, top: y }}>
    {Array.from({ length: 36 }).map((_, i) => (
      <rect key={i} x={(i % 6) * 25 + 1} y={Math.floor(i / 6) * 25 + 1} width={22} height={22} fill={C.lime} opacity={0.2 + 0.7 * random(`${seed}${i}`)} />
    ))}
  </svg>
);

export const R11_CONTEXT_WINDOWS: React.FC = () => {
  const { B, f, at } = useScene("R11_CONTEXT_WINDOWS");
  const shrink = ease(f, at(6, 20), at(6, 120));
  return (
    <Scene beats={B} hud={<SourceTag at={at(1)}>Brown et al. 2020 · Google, Feb 2024 · Dao et al. 2022</SourceTag>}>
      <Beat b={B[0]}>
        <Appear style={{ left: 160, top: 206 }}>
          <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
            <div style={{ fontSize: 32, fontWeight: 700 }}>CONTEXT WINDOW · TOKENS</div>
            <Tag color={C.text} size={18}>LOG SCALE</Tag>
          </div>
        </Appear>
        {[0, 1].map((k) => (
          <div key={k} style={{ position: "absolute", left: 160 + 360, top: 290 + k * 92, width: 950, height: 62, border: `2px dashed ${C.chrome}`, boxSizing: "border-box", opacity: sp(f, 30 + k * 10, 20) * (1 - ease(f, at(1 + k), at(1 + k, 20))) }} />
        ))}
      </Beat>
      <BarChart
        style={{ left: 160, top: 290 }}
        log
        min={1000}
        max={1000000}
        length={950}
        labelWidth={360}
        thickness={62}
        gap={30}
        labelSize={24}
        ticks={[
          { v: 1000, label: "1K" },
          { v: 10000, label: "10K" },
          { v: 100000, label: "100K" },
          { v: 1000000, label: "1M" },
        ]}
        ticksAt={150}
        dur={110}
        items={[
          { label: "GPT-3", sub: "2020", value: 2048, at: at(1, 6) },
          { label: "GEMINI 1.5", sub: "2024", value: 1000000, at: at(2, 6) },
        ]}
      />
      <Beat b={B[1]}><span /></Beat>
      <Beat b={B[2]}>
        <div style={{ position: "absolute", left: 160 + 360, top: 290 + 92, width: 950, height: 62, borderRadius: 4, boxShadow: `0 0 ${36 * pulse(f, at(2, 170), 60)}px ${limeA(0.7)}` }} />
      </Beat>
      <Beat b={B[3]}>
        <Appear style={{ left: 160, top: 486 }}>
          <Tag color={C.text} size={20}>2020 → 2024</Tag>
        </Appear>
      </Beat>
      <Beat b={B[4]}>
        <Card kicker="2022 · DAO ET AL." title="FLASHATTENTION" style={{ left: 160, top: 590 }} />
      </Beat>
      <Beat b={B[5]}>
        <Appear style={{ left: 0, top: 0 }}>
          <MiniMat x={700} y={580} seed="a" />
          <div style={{ position: "absolute", left: 870, top: 615, fontSize: 64, fontWeight: 700, color: C.lime }}>=</div>
          <MiniMat x={930} y={580} seed="a" />
        </Appear>
        <Appear delay={30} style={{ left: 760, top: 748 }}>
          <Tag color={C.lime} fill size={20}>SAME RESULT</Tag>
        </Appear>
      </Beat>
      <Beat b={B[6]}>
        <Appear style={{ left: 1160, top: 580 }}>
          <div style={{ width: 170, height: 150, border: `3px solid ${C.text}`, borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22, fontWeight: 700 }}>MEMORY</div>
        </Appear>
        <Appear delay={6} style={{ left: 1590, top: 580 }}>
          <div style={{ width: 170, height: 150, border: `3px solid ${C.lime}`, borderRadius: 8, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22, fontWeight: 700 }}>COMPUTE</div>
        </Appear>
        {Array.from({ length: 6 }).map((_, k) => {
          const keep = k === 2 ? 1 : 1 - shrink;
          const y = 600 + k * 22;
          return <Arrow key={k} x1={1340} y1={y} x2={1580} y2={y} p={ease(f, at(6, k * 3), at(6, 20 + k * 3)) * keep} color={k === 2 ? C.lime : C.pumpkin} width={k === 2 ? 4 : 4 + 6 * (1 - shrink)} />;
        })}
        <Appear delay={60} style={{ left: 1160, top: 748 }}>
          <Tag color={C.lime} size={20}>LESS MEMORY TRAFFIC</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S38
export const R11B_TRANSFORMER_ENGINE: React.FC = () => {
  const { B, f, at } = useScene("R11B_TRANSFORMER_ENGINE");
  const cx = 1100, cy = 250, S = 440;
  const eng = sp(f, at(2), 30);
  const arrowP = ease(f, at(3), at(3, 50));
  return (
    <Scene beats={B} hud={<SourceTag>NVIDIA (Mar 2022) · Vaswani et al. (2017)</SourceTag>}>
      <Beat b={B[0]}>
        <Appear dx={-50} dy={0} style={{ left: 240, top: 290 }}>
          <Paper w={280} h={380} accent={C.lime} />
        </Appear>
        <Appear delay={20} style={{ left: 240, top: 690, width: 280, textAlign: "center" }}>
          <Tag color={C.text} size={20}>2017 · THE PAPER</Tag>
        </Appear>
      </Beat>
      <Beat b={B[1]}>
        <Appear scaleFrom={0.9} style={{ left: cx, top: cy }}>
          <svg width={S} height={S} viewBox={`0 0 ${S} ${S}`} style={{ overflow: "visible" }}>
            {Array.from({ length: 10 }).map((_, k) => (
              <React.Fragment key={k}>
                <rect x={50 + k * 36} y={-22} width={14} height={24} fill={C.chrome} />
                <rect x={50 + k * 36} y={S - 2} width={14} height={24} fill={C.chrome} />
                <rect x={-22} y={50 + k * 36} width={24} height={14} fill={C.chrome} />
                <rect x={S - 2} y={50 + k * 36} width={24} height={14} fill={C.chrome} />
              </React.Fragment>
            ))}
            <rect x={2} y={2} width={S - 4} height={S - 4} rx={16} fill={C.bg} stroke={C.text} strokeWidth={4} />
            <rect x={40} y={40} width={S - 80} height={S - 80} rx={8} fill={chromeA(0.5)} stroke={C.chrome} strokeWidth={3} />
            {Array.from({ length: 4 }).map((_, k) => (
              <rect key={k} x={60 + (k % 2) * 170} y={250 + Math.floor(k / 2) * 0} width={150} height={110} rx={6} fill="none" stroke={C.chrome} strokeWidth={3} opacity={k < 2 ? 1 : 0} />
            ))}
          </svg>
        </Appear>
        <Appear delay={20} style={{ left: cx, top: cy + S + 34, width: S, textAlign: "center" }}>
          <Tag color={C.text} size={22}>2022 · NVIDIA H100</Tag>
        </Appear>
      </Beat>
      <Beat b={B[2]}>
        <div style={{ position: "absolute", left: cx + 60, top: cy + 60, width: S - 120, height: 160, borderRadius: 8, border: `4px solid ${C.lime}`, background: limeA(0.12 * eng), opacity: eng, boxShadow: `0 0 ${30 * eng}px ${limeA(0.5)}` }}>
          <svg width={S - 128} height={100} style={{ position: "absolute", left: 0, top: 50 }}>
            {Array.from({ length: 16 }).map((_, i) => {
              const ph = ((f - at(2)) / 6 - i) % 16;
              return <rect key={i} x={16 + i * 19} y={14} width={13} height={60} rx={2} fill={C.lime} opacity={0.25 + 0.6 * (ph > 0 && ph < 3 && f > at(2, 110) ? 1 : 0.3)} />;
            })}
          </svg>
          <div style={{ position: "absolute", left: 0, top: 12, width: "100%", textAlign: "center", fontSize: 26, fontWeight: 700, color: C.lime, letterSpacing: "0.08em" }}>TRANSFORMER ENGINE</div>
        </div>
      </Beat>
      <Beat b={B[3]}>
        <Arrow x1={540} y1={470} x2={cx - 40} y2={470} p={arrowP} width={6} curve={-60} />
        {Array.from({ length: 5 }).map((_, k) => {
          const u = (((f - at(3)) / 70 + k / 5) % 1);
          const x = 540 + u * (cx - 40 - 540);
          const y = 470 - Math.sin(u * Math.PI) * 60 * 0.5 * 2 * 0.5;
          return <div key={k} style={{ position: "absolute", left: x - 10, top: y - 10, width: 20, height: 20, borderRadius: 3, background: C.lime, opacity: arrowP > 0.9 ? 0.9 : 0 }} />;
        })}
        <Appear delay={20} style={{ left: 580, top: 330 }}>
          <Tag color={C.lime} fill size={24}>THE HARDWARE FOLLOWED</Tag>
        </Appear>
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S42
export const R13_RECAP: React.FC = () => {
  const { B, f, at } = useScene("R13_RECAP");
  const cw = 300, gap = 26, y = 440;
  const x0 = 960 - (5 * cw + 4 * gap) / 2;
  return (
    <Scene beats={B}>
      <RecapStack
        y={y}
        cardW={cw}
        gap={gap}
        cardH={230}
        alignAt={at(5)}
        items={[
          { year: "1997", label: "GATED MEMORY", at: at(0, 4), color: C.text },
          { year: "2014", label: "ATTENTION, BOLTED ON", at: at(1, 4), color: C.text },
          { year: "2017", label: "CHAIN DELETED", at: at(2, 4), color: C.lime, tagAt: at(5, 40) },
          { year: "2020", label: "≈800× BIGGER", at: at(3, 4), color: C.text },
          { year: "2023", label: "100M USERS IN ≈2 MONTHS", at: at(4, 4), color: C.text },
        ]}
      />
      <Beat b={B[0]}><span /></Beat>
      <Beat b={B[1]}><span /></Beat>
      <Beat b={B[2]}><span /></Beat>
      <Beat b={B[3]}><span /></Beat>
      <Beat b={B[4]}><span /></Beat>
      <Beat b={B[5]}>
        <div style={{ position: "absolute", left: x0, top: y + 230 + 40, height: 6, width: ease(f, at(5, 30), at(5, 90)) * (5 * cw + 4 * gap), background: C.lime, borderRadius: 3 }} />
        <div style={{ position: "absolute", left: x0 + 2 * (cw + gap) + cw / 2 - 14, top: y + 230 + 29, width: 28, height: 28, borderRadius: 14, background: C.lime, opacity: sp(f, at(5, 60), 20), boxShadow: `0 0 ${24 * pulse(f, at(5, 70), 60) + 4}px ${limeA(0.8)}` }} />
      </Beat>
    </Scene>
  );
};

// ---------------------------------------------------------------- S43
export const R12_AUTHORS_GRID: React.FC = () => {
  const { B, f, at } = useScene("R12_AUTHORS_GRID");
  const cw = 360, ch = 140, gx = 30, gy = 36;
  const x0 = 960 - (4 * cw + 3 * gx) / 2, y0 = 310;
  const ring = ease(f, at(6), at(6, 60));
  const coAt = (k: number) => {
    const named: Record<number, number> = { 5: at(3, 0), 1: at(3, 40), 4: at(3, 110), 6: at(3, 200) };
    if (named[k] !== undefined) return named[k];
    return at(2, 10 + [0, 0, 8, 16, 0, 0, 0, 24][k]);
  };
  return (
    <Scene beats={B} hud={<SourceTag at={at(1)}>Vaswani et al. (2017) · company and press announcements</SourceTag>}>
      <Beat b={B[0]}>
        {AUTHORS.map((a, k) => {
          const gxp = x0 + (k % 4) * (cw + gx);
          const gyp = y0 + Math.floor(k / 4) * (ch + gy);
          const ang = -Math.PI / 2 + (k / 8) * Math.PI * 2;
          const rxp = 960 + Math.cos(ang) * 620 - (cw * 0.72) / 2;
          const ryp = 528 + Math.sin(ang) * 255 - (ch * 0.72) / 2;
          const x = interpolate(ring, [0, 1], [gxp, rxp]);
          const y = interpolate(ring, [0, 1], [gyp, ryp]);
          const isNS = a.i === "NS";
          const hl = isNS ? sp(f, at(4), 20) : 0;
          const dimOthers = !isNS ? 1 - 0.5 * ease(f, at(4), at(4, 20)) * (1 - ring) : 1;
          const left = sp(f, at(1, 20 + k * 6), 16);
          const co = sp(f, coAt(k), 20);
          const back = isNS ? sp(f, at(5, 20), 20) : 0;
          return (
            <Appear key={a.i} delay={k * 4} style={{ left: x, top: y, scale: String(1 - 0.28 * ring), transformOrigin: "left top" }}>
              <div style={{ width: cw, height: ch, boxSizing: "border-box", border: `${isNS && hl > 0 ? 4 : 2}px solid ${isNS && hl > 0 ? C.lime : C.chrome}`, borderRadius: 8, background: C.bg, padding: "18px 22px", opacity: dimOthers, boxShadow: isNS ? `0 0 ${30 * hl}px ${limeA(0.4)}` : undefined }}>
                <div style={{ fontSize: 32, fontWeight: 700, whiteSpace: "nowrap" }}>{a.n}</div>
                <div style={{ display: "flex", gap: 10, marginTop: 16, alignItems: "center" }}>
                  {back > 0 ? (
                    <span style={{ opacity: back }}><Tag color={C.lime} fill size={17}>GOOGLE · 2024</Tag></span>
                  ) : (
                    <span style={{ position: "relative", display: "inline-block", opacity: 1 - 0.5 * left }}>
                      <Tag color={C.text} size={17}>GOOGLE</Tag>
                      <div style={{ position: "absolute", left: -4, top: "50%", height: 4, width: `calc(${left * 100}% + 8px)`, background: C.pumpkin }} />
                    </span>
                  )}
                  <span style={{ opacity: co, translate: `${20 * (1 - co)}px 0` }}>
                    <Tag color={back > 0 ? C.text : C.lime} size={17}>{a.co}</Tag>
                  </span>
                </div>
              </div>
            </Appear>
          );
        })}
      </Beat>
      <Beat b={B[1]}>
        <Appear style={{ left: 0, top: 218, width: 1920, textAlign: "center", opacity: 1 - ring }}>
          <Tag color={C.pumpkin} fill size={28}>BY 2023 · ALL 8 LEFT GOOGLE</Tag>
        </Appear>
      </Beat>
      <Beat b={B[2]}><span /></Beat>
      <Beat b={B[3]}><span /></Beat>
      <Beat b={B[4]}><span /></Beat>
      <Beat b={B[5]}><span /></Beat>
      <Beat b={B[6]}>
        <Appear delay={30} scaleFrom={0.8} style={{ left: 960 - 80, top: 380 }}>
          <Paper w={160} h={210} lines={6} accent={C.lime} />
        </Appear>
        <Appear delay={60} style={{ left: 760, top: 610, width: 400, textAlign: "center" }}>
          <Counter to={250000} from={1} log suffix="+" size={50} color={C.lime} dur={100} delay={60} />
          <Label size={16} style={{ marginTop: 6 }}>CITATIONS</Label>
        </Appear>
      </Beat>
    </Scene>
  );
};
