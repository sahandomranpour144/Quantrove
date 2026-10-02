"""
EP04 Voiceover Generator
Generates scene-by-scene audio using Gemini TTS (Orus voice) and outputs directly into TIMELINE_MEDIA/.
Run: python generate_voiceover_ep04.py
"""
import os, wave, subprocess, time
from google import genai
from google.genai import types

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EP_ROOT = os.path.dirname(BASE_DIR)
MEDIA_DIR = os.path.join(EP_ROOT, "TIMELINE_MEDIA")
os.makedirs(MEDIA_DIR, exist_ok=True)

SYSTEM_CONTEXT = (
    "Scene: A sleek, dark technology studio. The narrator is a calm, analytical, "
    "authoritative voice -- the voice of someone who understands complex systems deeply "
    "and explains them with precision, clarity, and intellectual weight. Deliberate pacing, "
    "no dramatic exaggeration, measured intelligence. Channel: Quantrove."
)

SEGMENTS = [
    {
        "filename": "01_T00-00_to_00-45_VO_scene01_hook.wav",
        "title": "Scene 1: The Simons Paradox & Cold Hook",
        "text": (
            "In 1988, a former Cold War codebreaker and mathematician named Jim Simons launched a fund that did something Wall Street thought was mathematically impossible.\n\n"
            "For more than thirty years, his Medallion Fund generated an average return of sixty-six percent a year -- turning a thousand dollars into more than forty-two million dollars. And they did it by enforcing one strict rule: they completely banned anyone with a finance background, hiring only physicists, cryptographers, and mathematicians.\n\n"
            "Yet today, across the rest of Wall Street, firms spend billions on deep neural networks and supercomputers to predict stock prices... and the vast majority still fail to beat a simple index fund.\n\n"
            "How did a team of mathematicians crack the market with an edge that was barely fifty-one percent, while today's most powerful AI models fail every single day?\n\n"
            "Let's look at the real mathematics of why AI cannot predict the stock market the way most people think."
        )
    },
    {
        "filename": "02_T00-45_to_02-15_VO_scene02_reflexivity.wav",
        "title": "Scene 2: The 50.75% Edge & Reflexivity Trap",
        "text": (
            "Here is the first great illusion about quantitative trading: people assume Jim Simons built an oracle that predicted the future with ninety percent accuracy.\n\n"
            "In reality, Simons himself admitted that Medallion's statistical edge was microscopic. They were right roughly fifty point seventy-five percent of the time.\n\n"
            "Their entire fortune was built on the law of large numbers -- executing millions of micro-trades where a tiny probability edge turned into billions of dollars.\n\n"
            "But if it's just math and probability, why can't today's generative AI models simply look at decades of price data and do the same thing?\n\n"
            "Because markets have a property almost no other prediction problem in computer science possesses: they react to being predicted.\n\n"
            "Think about how an image recognition AI works. If a neural network learns to identify a cat, the cat does not change its shape because the computer got good at recognizing it.\n\n"
            "But the financial market is a competitive, zero-sum game of human and algorithmic participants. If an AI discovers a genuine, profitable pattern that says Apple will rise tomorrow, and traders deploy capital on that signal... their own buying pressure instantly drives the price up today.\n\n"
            "The prediction itself erases the pattern. The moment an edge becomes predictable, it self-destructs."
        )
    },
    {
        "filename": "03_T02-15_to_03-30_VO_scene03_alpha_decay.wav",
        "title": "Scene 3: Pattern #1 - The Alpha Decay Curve",
        "text": (
            "In quantitative finance, this inevitable self-destruction is known as alpha decay.\n\n"
            "In the physical world, gravity doesn't stop working because millions of physicists understand it. But in finance, alpha behaves like an expiring patent.\n\n"
            "The second a profitable trading anomaly appears in price data, competing quantitative funds, high-frequency algorithms, and market makers sniff out the same volume spikes.\n\n"
            "As hundreds of automated systems rush in to exploit the exact same inefficiency, they crowd the trade. They bid up the entry price, compress the profit spread, and push the market back to mathematical equilibrium.\n\n"
            "This is why an AI model that looks brilliant in a backtest can quietly stop making money within four months of going live. It isn't that the code failed. It's that the market adapted around it."
        )
    },
    {
        "filename": "04_T03-30_to_04-45_VO_scene04_overfitting.wav",
        "title": "Scene 4: Pattern #2 - The Overfitting Illusion",
        "text": (
            "The second fatal flaw is something every machine learning engineer knows, but almost every retail trader ignores: the overfitting trap.\n\n"
            "Stock prices are what statisticians call low signal-to-noise ratio data. On any given Tuesday, a stock price moves due to institutional rebalancing, algorithmic hedging, geopolitical rumors, or random liquidity flows. Ninety-five percent of daily price movement is pure noise.\n\n"
            "But modern deep neural networks have millions, sometimes billions, of parameters. If you feed thirty years of noisy price data into a deep learning model, the mathematics guarantees it will find correlations.\n\n"
            "It might discover that every time the temperature in Chicago drops by three degrees on a Thursday, semiconductor stocks rally on Friday morning.\n\n"
            "In a backtest, the curve looks like a straight line up and to the right. But the moment you connect that model to real capital, it encounters new data it hasn't memorized. And the phantom pattern evaporates immediately."
        )
    },
    {
        "filename": "05_T04-45_to_06-15_VO_scene05_real_use_cases.wav",
        "title": "Scene 5: The 4 Engines - Where AI Dominates",
        "text": (
            "So does this mean institutional Wall Street doesn't use AI?\n\n"
            "Not at all. Institutional firms spend fortunes on AI. But they don't ask it the naive question: 'What will Tesla stock trade at tomorrow at noon?'\n\n"
            "Instead, they deploy AI across four completely different engines:\n\n"
            "First, Extreme Risk Modeling. Rather than predicting direction, machine learning simulates hundreds of thousands of catastrophic market scenarios -- extreme liquidity freezes, interest rate shocks, currency collapses -- to calculate the exact probability of portfolio ruin.\n\n"
            "Second, Execution and Slippage Minimization. When a pension fund needs to buy five billion dollars of stock, placing that order in one block would crash the price against them. Reinforcement learning agents break massive orders into thousands of micro-slices, hiding order flow across dark pools and saving millions in execution costs.\n\n"
            "Third, Real-Time Fraud and Anomaly Detection. Scanning hundreds of thousands of institutional transactions per second to detect spoofing, wash trading, and unusual order cancellations before regulators even notice.\n\n"
            "And fourth, Mathematical Portfolio Rebalancing. Given five hundred correlated assets, calculating the mathematically optimal covariance matrix to maximize Sharpe ratio while minimizing volatility.\n\n"
            "Notice what all four of these have in common: none of them require predicting the future. They are optimization problems, not crystal balls."
        )
    },
    {
        "filename": "06_T06-15_to_07-25_VO_scene06_verdict_outro.wav",
        "title": "Scene 6: The Quantitative Verdict & Outro",
        "text": (
            "If you want to understand the modern intersection of artificial intelligence and finance, remember this fundamental rule:\n\n"
            "The stock market is not a puzzle to be solved like chess or protein folding. It is an evolving, reflexive ecosystem of competing intelligences.\n\n"
            "The funds that survive long term never search for magic prediction algorithms. They focus on structural speed, disciplined risk control, and microscopic statistical edges compounded across millions of trades -- just like Jim Simons did almost forty years ago.\n\n"
            "In our next breakdown, we're going behind the scenes of YouTube's own black-box recommendation algorithm to see the exact neural network mechanics that decided to put this video on your screen.\n\n"
            "If you want the real data and mathematics behind modern technology without the hype, hit subscribe and join Quantrove."
        )
    }
]

def save_pcm_to_wav(pcm_bytes, wav_path, sample_rate=24000, channels=1, sampwidth=2):
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_bytes)

def generate():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY not found.")
        return
    client = genai.Client(api_key=api_key)
    generated_files = []
    
    for idx, seg in enumerate(SEGMENTS):
        out_wav = os.path.join(MEDIA_DIR, seg["filename"])
        if os.path.exists(out_wav) and os.path.getsize(out_wav) > 2000:
            print(f"[{idx+1}/{len(SEGMENTS)}] Already exists: {seg['filename']} ({os.path.getsize(out_wav)} bytes), skipping.")
            generated_files.append(out_wav)
            continue

        print(f"[{idx+1}/{len(SEGMENTS)}] Generating: {seg['title']} -> {seg['filename']}...")
        prompt = f"{SYSTEM_CONTEXT}\n\nRead the following script verbatim with clear, deliberate articulation:\n\n{seg['text']}"
        
        success = False
        for attempt in range(4):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash-preview-tts",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["AUDIO"],
                        speech_config=types.SpeechConfig(
                            voice_config=types.VoiceConfig(
                                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Orus")
                            )
                        ),
                    ),
                )
                audio_bytes = None
                for part in response.candidates[0].content.parts:
                    if part.inline_data and part.inline_data.data:
                        audio_bytes = part.inline_data.data
                        break
                if audio_bytes:
                    save_pcm_to_wav(audio_bytes, out_wav)
                    generated_files.append(out_wav)
                    print(f"[OK] Saved {out_wav} ({len(audio_bytes)} bytes)")
                    success = True
                    break
                else:
                    print(f"[WARN] No audio bytes returned on attempt {attempt+1}")
            except Exception as e:
                print(f"[WARN] Attempt {attempt+1} failed: {e}")
                time.sleep(3 * (attempt + 1))
        
        if not success:
            print(f"[ERROR] Failed to generate audio for {seg['filename']} after retries.")
        time.sleep(1.5)

    print(f"\n[DONE] Finished generating tracks in {MEDIA_DIR}.")

    # Concatenate all wav files into a master voiceover track
    if len(generated_files) == len(SEGMENTS):
        print("\n[INFO] Creating concatenated master voiceover track...")
        concat_list_file = os.path.join(MEDIA_DIR, "concat_vo_list.txt")
        with open(concat_list_file, "w", encoding="utf-8") as f:
            for seg in SEGMENTS:
                wav_path = os.path.join(MEDIA_DIR, seg["filename"]).replace("\\", "/")
                f.write(f"file '{wav_path}'\n")
        
        master_vo = os.path.join(MEDIA_DIR, "00_VOICEOVER_master.wav")
        cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list_file, "-c", "copy", master_vo]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(master_vo):
            print(f"[OK] Master voiceover generated: {master_vo} ({os.path.getsize(master_vo)} bytes)")
            try:
                os.remove(concat_list_file)
            except Exception:
                pass
        else:
            print(f"[WARN] Failed to concatenate audio: {res.stderr}")

if __name__ == "__main__":
    generate()
