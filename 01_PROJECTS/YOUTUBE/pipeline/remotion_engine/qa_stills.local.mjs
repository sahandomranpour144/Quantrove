// Fast QA: one browser, 6 stills per composition (late in 6 spread beats), tiled 3x2 by ffmpeg.
// usage: node qa_stills.local.mjs <bundleDir> <outDir> EP07|EP08 [ASSET ...]
import { openBrowser, selectComposition, renderStill } from "@remotion/renderer";
import { readFileSync, mkdirSync } from "fs";
import { execFileSync } from "child_process";
import path from "path";

const [bundle, outDir, ep, ...only] = process.argv.slice(2);
const tl = JSON.parse(readFileSync(`src/data/${ep.toLowerCase()}_timeline.json`, "utf8"));
mkdirSync(outDir, { recursive: true });
const browser = await openBrowser("chrome", { browserExecutable: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" });
for (const s of tl.scenes) {
  if (s.engine !== "Remotion" || (only.length && !only.includes(s.asset))) continue;
  const id = `${ep}-${s.asset.replace(/_/g, "-")}`;
  const s0 = Math.round(s.start * 60);
  const n = Math.round(s.end * 60) - s0;
  const B = s.beats;
  const idx = [...new Set(Array.from({ length: 6 }, (_, i) => Math.round((i * (B.length - 1)) / 5)))];
  while (idx.length < 6) idx.push(B.length - 1);
  const frames = idx.map((i, k) => {
    const b = B[i];
    const t = b.start + (b.end - b.start) * (k === 5 ? 0.97 : 0.8);
    return Math.min(n - 1, Math.max(0, Math.round(t * 60) - s0));
  });
  const composition = await selectComposition({ serveUrl: bundle, id, puppeteerInstance: browser });
  for (let k = 0; k < 6; k++) {
    await renderStill({ composition, serveUrl: bundle, output: path.join(outDir, `${id}_${k}.jpg`), frame: frames[k], puppeteerInstance: browser, imageFormat: "jpeg", overwrite: true });
  }
  execFileSync("ffmpeg", ["-y", "-v", "error", "-i", path.join(outDir, `${id}_%d.jpg`), "-vf", "scale=640:-1,tile=3x2", "-frames:v", "1", path.join(outDir, `${id}.png`)]);
  console.log(id, frames.join(","));
}
await browser.close({ silent: true });
