"""
Script: generate_all_voiceover.py
EP02: "What Does 50 Years of Data Say About Recessions?"
Generates crystal-clear, authoritative voiceover audio using Gemini TTS ('Orus' voice)
with the specified studio scene context and outputs high-quality MP3 & WAV files.
"""

import os
import wave
import subprocess
import time
from google import genai
from google.genai import types

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "generated_audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SYSTEM_CONTEXT = (
    "Scene: A modern financial data studio. A calm, focused environment for delivering a precise, authoritative economic breakdown. "
    "Sample Context: Financial data journalism and educational analysis. Deliberate, clear, analytical, authoritative pacing — "
    "a trusted narrator explaining complex economic patterns with precision and confidence. No dramatic flair, no suspense."
)

SEGMENTS = [
    {
        "filename": "scene01_hook",
        "title": "Scene 1: The Hook",
        "text": (
            "In almost every recession over the last fifty years, the single best day to invest in the stock market happened when the news was screaming that the world was ending.\n\n"
            "Most people believe recessions and market crashes move in lockstep. But when you look at five decades of actual economic data, you discover something completely counterintuitive: the market almost always starts a massive recovery months before the recession is even close to over.\n\n"
            "So what actually happens during a recession? How long do they really last? And why does almost everyone get the data completely backwards?"
        )
    },
    {
        "filename": "scene02_two_quarter_myth",
        "title": "Scene 2: The Two-Quarter Myth",
        "text": (
            "If you watch the financial news, you've probably heard the classic textbook rule: a recession is two consecutive quarters of negative GDP growth.\n\n"
            "Simple, clean, easy to remember.\n\n"
            "Except that's not actually how it works in the United States.\n\n"
            "In reality, recessions are officially determined by a private group of eight academic economists called the National Bureau of Economic Research — or the NBER.\n\n"
            "And they don't just look at GDP. They look at payroll employment, real personal income, consumer spending, wholesale retail sales, and industrial production across the entire economy.\n\n"
            "A real recession isn't just one sluggish quarter on a balance sheet. It is a widespread, severe contraction in economic activity that lasts more than a few months.\n\n"
            "But here is the fatal flaw with relying on an official definition: the referee always blows the whistle long after the play is already over."
        )
    },
    {
        "filename": "scene03_referee_lag",
        "title": "Scene 3: The 7-Month Referee Lag",
        "text": (
            "Because macroeconomic data takes months to collect, survey, revise, and verify, the NBER never calls a recession in real time.\n\n"
            "On average over the last fifty years, it takes the committee seven full months just to declare that a recession has started.\n\n"
            "Think about what that means.\n\n"
            "By the time the experts officially step up to a microphone and tell the public \"we are in a recession,\" the recession is already more than halfway finished.\n\n"
            "In the 1980 recession, the committee didn't announce the recession began until it was literally already over.\n\n"
            "And in 2020, they declared the recession in June — even though the stock market had already bottomed nearly three months earlier, on March 23rd, and the broader economy — jobs, spending, output — hit its actual low point in April.\n\n"
            "This lag creates a massive psychological trap. By the time everyday people start panicking about the word \"recession,\" smart money is already looking at what comes next."
        )
    },
    {
        "filename": "scene04_autopsy",
        "title": "Scene 4: The 50-Year Autopsy",
        "text": (
            "To see what really happens beneath the surface, let's look at fifty years of data across five completely different economic environments.\n\n"
            "In 1973, an OPEC oil embargo triggered a double shock: high inflation combined with falling economic output. This was stagflation — a brutal, sixteen-month grind that broke the post-war economic boom.\n\n"
            "Less than a decade later, in 1981, Federal Reserve Chairman Paul Volcker intentionally slammed the brakes on the economy. He jacked interest rates up to twenty percent to break the back of runaway inflation. It worked, but it triggered another painful sixteen-month downturn.\n\n"
            "In 2001, the culprit wasn't oil or interest rates — it was pure speculation. The dot-com bubble burst. It was a relatively mild eight-month recession, but it wiped out trillions in phantom tech valuations.\n\n"
            "In 2008, the global banking system froze. Wall Street's subprime mortgage machine collapsed, creating an eighteen-month crisis — the longest and deepest downturn since the Great Depression.\n\n"
            "And in 2020, the unexpected occurred: an artificial shutdown triggered the sharpest drop in GDP in recorded history. But it lasted just two months — the shortest recession in American history.\n\n"
            "Five completely different triggers. But when you step back and look at all eight recessions since 1970, two massive patterns emerge that almost nobody talks about."
        )
    },
    {
        "filename": "scene05_lead_lag",
        "title": "Scene 5: Pattern #1 — The Lead-Lag Paradox",
        "text": (
            "Pattern number one is what we call the Lead-Lag Paradox.\n\n"
            "Most people assume that because the economy is in trouble, stock prices will keep falling until the economic data improves.\n\n"
            "The data shows the exact opposite.\n\n"
            "The stock market is a leading indicator. It doesn't trade on what is happening today — it trades on what investors believe corporate profits will look like six to nine months in the future.\n\n"
            "Because of this, the stock market almost always peaks before a recession begins.\n\n"
            "But far more importantly: the market almost always bottoms out and begins a violent new bull market three to five months before the recession officially ends.\n\n"
            "In 2009, the S&P 500 hit its generational bottom on March 9th. On that exact day, unemployment was still skyrocketing, banks were still teetering, and the headlines were pure doom.\n\n"
            "Yet over the following twelve months, the stock market surged over sixty percent.\n\n"
            "If an investor waited for the news to report that the economy was \"safe,\" they missed the most profitable part of the entire economic cycle."
        )
    },
    {
        "filename": "scene06_time_jobs",
        "title": "Scene 6: Pattern #2 — The Asymmetry of Time & Jobs",
        "text": (
            "Pattern number two is the asymmetry of time.\n\n"
            "When you are living through a recession, the constant barrage of negative news makes it feel permanent.\n\n"
            "But the historical record tells a completely different story.\n\n"
            "Since 1950, the average U.S. recession has lasted just ten point four months.\n\n"
            "The average expansion period between recessions? Over five full years. And the longest expansion in modern history lasted over a decade — from 2009 all the way to 2020.\n\n"
            "Recessions are sharp, painful compressions, but expansions are long, steady, and dominant.\n\n"
            "However, there is one place where the scars last far longer: jobs.\n\n"
            "While asset prices can rebound in months, employment behaves like an elevator on the way down, and the stairs on the way up.\n\n"
            "Layoffs happen in weeks, but returning to pre-recession employment levels takes an average of three to five years.\n\n"
            "That is why even after the data confirms a recession is officially over, everyday families still feel the pressure long after Wall Street has moved on."
        )
    },
    {
        "filename": "scene07_outro",
        "title": "Scene 7: Conclusion & Next Video Hook",
        "text": (
            "So what does fifty years of economic data actually teach us?\n\n"
            "First: recessions are not economic death sentences. They are painful, brief, and historically recurring resets inside an ongoing story of growth.\n\n"
            "Second: the official data is always late. Waiting for certainty from the news guarantees you'll miss the turning point.\n\n"
            "And third: panic is always the most expensive trade you can make.\n\n"
            "Now you understand the macro rules of money and data. But in the modern world, the decisions you make every day aren't just influenced by interest rates — they're shaped by the algorithms running in your pocket.\n\n"
            "In our next breakdown, we're stepping into the world of artificial intelligence to reveal how recommendation algorithms actually decide what reaches your screen.\n\n"
            "If this helped you see the data beneath the headlines, subscribe to Quantrove — and we'll see you in the next breakdown."
        )
    }
]

def save_pcm_to_wav(pcm_bytes, wav_path, sample_rate=24000, channels=1, sampwidth=2):
    with wave.open(wav_path, 'wb') as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(pcm_bytes)

def convert_wav_to_mp3(wav_path, mp3_path):
    cmd = [
        "ffmpeg", "-y", "-i", wav_path,
        "-codec:a", "libmp3lame", "-b:a", "192k",
        mp3_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def generate_segment(client, segment, index, total):
    print(f"🎙️ [{index+1}/{total}] Generating Voiceover: {segment['title']}...")
    prompt = f"{SYSTEM_CONTEXT}\n\nRead the following script verbatim with clear, deliberate articulation:\n\n{segment['text']}"
    
    response = client.models.generate_content(
        model="gemini-3.1-flash-tts-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Orus",
                    )
                )
            ),
        ),
    )

    audio_bytes = None
    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.data:
            audio_bytes = part.inline_data.data
            break

    if not audio_bytes:
        raise RuntimeError(f"No audio returned for {segment['filename']}")

    wav_path = os.path.join(OUTPUT_DIR, f"{segment['filename']}.wav")
    mp3_path = os.path.join(OUTPUT_DIR, f"{segment['filename']}.mp3")

    save_pcm_to_wav(audio_bytes, wav_path)
    convert_wav_to_mp3(wav_path, mp3_path)
    print(f"✅ Created: {mp3_path} ({os.path.getsize(mp3_path):,} bytes)")

def combine_all_audio():
    print("\n🎧 Concatenating all scenes into full master track: full_voiceover_ep02.mp3...")
    concat_list_path = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for seg in SEGMENTS:
            wav_file = f"{seg['filename']}.wav"
            f.write(f"file '{wav_file}'\n")

    master_wav = os.path.join(OUTPUT_DIR, "full_voiceover_ep02.wav")
    master_mp3 = os.path.join(OUTPUT_DIR, "full_voiceover_ep02.mp3")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy", master_wav
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    convert_wav_to_mp3(master_wav, master_mp3)
    print(f"🎉 Master Audio Generated: {master_mp3} ({os.path.getsize(master_mp3):,} bytes)")

def main():
    print("🚀 Initializing Gemini Voiceover Engine (Voice: Orus)...")
    client = genai.Client()
    for i, seg in enumerate(SEGMENTS):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                generate_segment(client, seg, i, len(SEGMENTS))
                time.sleep(1.0)
                break
            except Exception as e:
                print(f"⚠️ Attempt {attempt+1} failed for {seg['filename']}: {e}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(2.5)

    combine_all_audio()
    print("\n✨ All voiceover audio files successfully generated in e:\\AI_COMPANY\\01_PROJECTS\\YOUTUBE\\longs\\long02_50_years_recession_data\\voiceover\\generated_audio\\")

if __name__ == "__main__":
    main()
