// Registers every long-form Remotion scene as EP0x-<ASSET> (ids use "-" since Remotion forbids "_").
import React from "react";
import { Composition } from "remotion";
import ep07 from "../data/ep07_timeline.json";
import ep08 from "../data/ep08_timeline.json";
import { FPS, Timeline, sceneInfo } from "./shared";
import * as EP07 from "./ep07/scenes";
import * as EP08 from "./ep08/scenes";

const eps: [string, Timeline, Record<string, React.FC>][] = [
  ["EP07", ep07 as Timeline, EP07],
  ["EP08", ep08 as Timeline, EP08],
];

export const LongCompositions: React.FC = () => (
  <>
    {eps.flatMap(([ep, tl, mod]) =>
      Object.entries(mod).map(([asset, Comp]) => (
        <Composition
          key={`${ep}-${asset}`}
          id={`${ep}-${asset.replace(/_/g, "-")}`}
          component={Comp}
          durationInFrames={sceneInfo(tl, asset).durationInFrames}
          fps={FPS}
          width={1920}
          height={1080}
        />
      )),
    )}
  </>
);
