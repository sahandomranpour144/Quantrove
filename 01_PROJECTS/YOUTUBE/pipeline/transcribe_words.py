"""Word-level transcription (word-sync skill schema). Usage: python transcribe_words.py <audio> <out.json>"""
import json, subprocess, sys
from faster_whisper import WhisperModel

audio, out = sys.argv[1], sys.argv[2]
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                     "-of", "csv=p=0", audio], text=True))
model = WhisperModel("base", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, beam_size=5, word_timestamps=True, language="en")
words, segs = [], []
for s in segments:
    segs.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
    words += [{"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3),
               "probability": round(w.probability, 3)} for w in s.words]
json.dump({"total_words": len(words), "audio_file": audio, "total_duration_s": round(dur, 3),
           "all_words": words, "all_segments": segs}, open(out, "w", encoding="utf-8"), indent=1)
print(f"{len(words)} words, {dur:.2f}s -> {out}")
