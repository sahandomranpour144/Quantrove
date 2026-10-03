import { Composition } from "remotion";
import { Short01WhySpreadExists } from "./shorts/Short01WhySpreadExists";
import { Short02SpeedDoesntPredictMarket } from "./shorts/Short02SpeedDoesntPredictMarket";
import { Short03WhyMachineChangesPrice } from "./shorts/Short03WhyMachineChangesPrice";
import { Short04HowOneLosingDayHappens } from "./shorts/Short04HowOneLosingDayHappens";
import { OrderRoutingBenchmark } from "./OrderRoutingBenchmark";
import { LongCompositions } from "./longs";
import "./index.css";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* Existing compositions */}
      <Composition
        id="OrderRoutingBenchmark"
        component={OrderRoutingBenchmark}
        durationInFrames={540}
        fps={60}
        width={1080}
        height={1920}
      />

      {/* EP06 SHORT 01: WHY DOES A SPREAD EXIST? */}
      <Composition
        id="Short01-WhySpreadExists"
        component={Short01WhySpreadExists}
        durationInFrames={1398} // 46.60s @ 30fps
        fps={30}
        width={1080}
        height={1920}
      />

      {/* EP06 SHORT 02: SPEED DOESN'T PREDICT THE MARKET */}
      <Composition
        id="Short02-SpeedDoesntPredictMarket"
        component={Short02SpeedDoesntPredictMarket}
        durationInFrames={1307} // 43.55s @ 30fps
        fps={30}
        width={1080}
        height={1920}
      />

      {/* EP06 SHORT 03: WHY DOES THE MACHINE CHANGE ITS PRICE? */}
      <Composition
        id="Short03-WhyMachineChangesPrice"
        component={Short03WhyMachineChangesPrice}
        durationInFrames={1532} // 51.07s @ 30fps
        fps={30}
        width={1080}
        height={1920}
      />

      {/* EP06 SHORT 04: HOW CAN ONE LOSING DAY HAPPEN? */}
      <Composition
        id="Short04-HowOneLosingDayHappens"
        component={Short04HowOneLosingDayHappens}
        durationInFrames={1586} // 52.85s @ 30fps
        fps={30}
        width={1080}
        height={1920}
      />

      {/* EP07+ long-form 16:9 data-graphics scenes */}
      <LongCompositions />
    </>
  );
};
