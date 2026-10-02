"""
EP03 Voiceover Generator
Generates scene-by-scene MP3 audio using Gemini TTS (Orus voice).
Run: python generate_voiceover_ep03.py
Requires: GEMINI_API_KEY environment variable
"""
import os, wave, subprocess, time
from google import genai
from google.genai import types

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "generated_audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SYSTEM_CONTEXT = (
    "Scene: A sleek, dark technology studio. The narrator is a calm, analytical, "
    "authoritative voice -- the voice of someone who understands complex systems deeply "
    "and explains them with precision and clarity. No dramatic flair, no suspense music. "
    "Deliberate pacing, measured intelligence. Channel: Quantrove."
)

SEGMENTS = [
    {
        "filename": "scene01_hook",
        "title": "Scene 1: The Hook",
        "text": (
            "There is a system you interact with more times per day than you talk "
            "to any single human being in your life. It was never built to inform you. "
            "It was built to do exactly one thing: keep you watching. "
            "And it is frighteningly good at its job.\n\n"
            "Most people think they know how it works. "
            "They are almost always wrong.\n\n"
            "So what is the algorithm actually optimizing for? "
            "Why do two nearly identical videos get wildly different results? "
            "And once you understand the real mechanism, how does it change the way "
            "you use every platform you are on?"
        )
    },
    {
        "filename": "scene02_the_myth",
        "title": "Scene 2: The Myth",
        "text": (
            "Ask most people how recommendations work, and you will hear some version "
            "of the same answer: it shows you what is popular. What is trending. "
            "What everyone else is already watching.\n\n"
            "That is not what is actually happening.\n\n"
            "If it were true, everyone logged in at the same moment would see the same "
            "recommended videos. They do not. Two people can open the same platform, "
            "at the same second, and see almost completely different feeds -- "
            "built from completely different signals.\n\n"
            "This is not a popularity contest. "
            "It is a prediction system, built individually, for you specifically."
        )
    },
    {
        "filename": "scene03_two_stage_system",
        "title": "Scene 3: The Two-Stage System",
        "text": (
            "Publicly documented research from the engineers who build these systems "
            "describes a two-stage architecture.\n\n"
            "Stage one: candidate generation. Out of literally millions of available videos, "
            "a first system narrows the field down to a few hundred -- using your watch history, "
            "your session context, and patterns from viewers similar to you.\n\n"
            "Stage two: ranking. A second system takes that shortlist and scores every single one -- "
            "not by how good the video objectively is, but by how likely it is to keep you, "
            "specifically, watching."
        )
    },
    {
        "filename": "scene04_optimization_target",
        "title": "Scene 4: The Real Optimization Target",
        "text": (
            "Here is the detail almost nobody outside the industry knows: for years, "
            "recommendation systems were built to maximize clicks. "
            "And that created an obvious problem -- creators learned that outrageous, "
            "misleading thumbnails and titles got clicked more, even when the actual "
            "video disappointed viewers.\n\n"
            "So platforms changed the target. Not clicks -- watch time.\n\n"
            "The system stopped asking what will get clicked, and started asking "
            "what will this specific person actually keep watching.\n\n"
            "That single change is the most important thing to understand about "
            "how your feed is built today."
        )
    },
    {
        "filename": "scene05_personalization_paradox",
        "title": "Scene 5: The Personalization Paradox",
        "text": (
            "Pattern number one: the exact same video can perform completely differently "
            "depending on who is watching it -- not because the video changed, "
            "but because the prediction target did.\n\n"
            "Show a video to someone whose history is full of long-form documentaries, "
            "and the system predicts they will watch it fully. Show the identical video "
            "to someone who only watches short clips, and the system predicts they will "
            "drop off in seconds -- and simply will not show it to them at all.\n\n"
            "This is why two creators can post nearly identical content and get wildly "
            "different results. The algorithm is not judging the video in isolation. "
            "It is predicting a specific outcome for a specific person."
        )
    },
    {
        "filename": "scene06_rabbit_hole",
        "title": "Scene 6: The Rabbit Hole Effect",
        "text": (
            "Pattern number two is the one that has drawn the most public scrutiny: "
            "when a system is purely optimized for keeping you watching, session after session, "
            "it can quietly narrow what you see -- nudging toward more intense, more extreme, "
            "or more emotionally charged versions of whatever you started with.\n\n"
            "This is not a secret. Platforms have publicly acknowledged the effect and made "
            "real changes to reduce it -- because a system optimized purely for engagement, "
            "left unchecked, does not just reflect what you are interested in. "
            "It can actively reshape it.\n\n"
            "Understanding that is not about paranoia. It is about knowing what the system "
            "is actually doing so you can use it deliberately, instead of being used by it."
        )
    },
    {
        "filename": "scene07_conclusion",
        "title": "Scene 7: Conclusion & Teaser",
        "text": (
            "So what does understanding the algorithm actually change?\n\n"
            "First: it was never a popularity contest. "
            "It is an individual prediction, built from your own behavior.\n\n"
            "Second: it optimizes for attention, not accuracy or importance -- "
            "those are very different things, and conflating them is where most "
            "misunderstandings start.\n\n"
            "And third: the moment you understand what it is actually predicting, "
            "you can deliberately feed it different signals -- and get a genuinely "
            "different feed back.\n\n"
            "We have now covered how markets crash, how recessions really move, "
            "and how the algorithm decides what reaches you. "
            "In our next breakdown, we are going back to the data.\n\n"
            "If this helped you see the system behind the screen, "
            "subscribe to Quantrove -- we are just getting started."
        )
    },
]


def save_pcm_to_wav(pcm_bytes, wav_path, sample_rate=24000, channels=1, sampwidth=2):
    with wave.open(wav_path, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm_bytes)


def wav_to_mp3(wav_path, mp3_path):
    subprocess.run(
        ["ffmpeg", "-y", "-i", wav_path, "-codec:a", "libmp3lame", "-b:a", "192k", mp3_path],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
    )


def generate_segment(client, seg, idx, total):
    print(f"[{idx+1}/{total}] Generating: {seg['title']}...")
    prompt = (
        f"{SYSTEM_CONTEXT}\n\n"
        f"Read the following script verbatim with clear, deliberate articulation:\n\n"
        f"{seg['text']}"
    )
    response = client.models.generate_content(
        model="gemini-3.1-flash-tts-preview",
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
    if not audio_bytes:
        raise RuntimeError(f"No audio returned for {seg['filename']}")

    wav = os.path.join(OUTPUT_DIR, f"{seg['filename']}.wav")
    mp3 = os.path.join(OUTPUT_DIR, f"{seg['filename']}.mp3")
    save_pcm_to_wav(audio_bytes, wav)
    wav_to_mp3(wav, mp3)
    print(f"  OK: {mp3} ({os.path.getsize(mp3):,} bytes)")


def combine_all():
    print("\nConcatenating all scenes into full master track...")
    concat = os.path.join(OUTPUT_DIR, "concat_list.txt")
    with open(concat, "w") as f:
        for seg in SEGMENTS:
            f.write(f"file '{seg['filename']}.wav'\n")
    master_wav = os.path.join(OUTPUT_DIR, "full_voiceover_ep03.wav")
    master_mp3 = os.path.join(OUTPUT_DIR, "full_voiceover_ep03.mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
         "-i", concat, "-c", "copy", master_wav],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
    )
    wav_to_mp3(master_wav, master_mp3)
    print(f"Master audio: {master_mp3} ({os.path.getsize(master_mp3):,} bytes)")


def main():
    print("Initializing Gemini TTS (Voice: Orus)...")
    client = genai.Client()
    for i, seg in enumerate(SEGMENTS):
        for attempt in range(3):
            try:
                generate_segment(client, seg, i, len(SEGMENTS))
                time.sleep(1.0)
                break
            except Exception as e:
                print(f"  Attempt {attempt+1} failed: {e}")
                if attempt == 2:
                    raise
                time.sleep(2.5)
    combine_all()
    print("\nAll EP03 voiceover audio generated.")


if __name__ == "__main__":
    main()
