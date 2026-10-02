import { Config } from "@remotion/cli/config";
import fs from "fs";

const candidateBrowsers = [
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
];

for (const p of candidateBrowsers) {
  if (fs.existsSync(p)) {
    Config.setBrowserExecutable(p);
    break;
  }
}
Config.setOverwriteOutput(true);
