"""Align script beats ('‖' segments) to faster-whisper word timestamps -> MASTER_TIMELINE.json.

Usage: python beat_align.py <EPxx_SCRIPT_AND_SHOTLIST.md> <EPxx_words.json> <out MASTER_TIMELINE.json> [end_screen_s=20]
Cuts land on the first word of each beat; pauses belong to the preceding beat.
"""
import difflib, json, re, sys

def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower().replace("’", "'"))

def parse_script(path):
    s = open(path, encoding="utf-8").read()
    body = s[s.index("## 4. Script"):s.index("## 5. ")]
    scenes = []
    for m in re.finditer(r"\*\*Scene (\d+) — (\S+) \((\w+)[^\n]*\n((?:(?!\*\*Scene ).*\n)*)", body):
        narr = re.search(r'\[NARRATION\] "(.*)"', m[4])
        beats = [b.strip() for b in narr[1].split("‖") if b.strip()] if narr else []
        scenes.append({"scene": int(m[1]), "engine": m[2], "asset": m[3], "beat_text": beats})
    return scenes

def align(script_md, words_json, end_screen_s=20.0):
    scenes = parse_script(script_md)
    wj = json.load(open(words_json, encoding="utf-8"))
    words, vo_dur = wj["all_words"], wj["total_duration_s"]
    s_tok, owner = [], []                       # script tokens and (scene_idx, beat_idx)
    for si, sc in enumerate(scenes):
        for bi, b in enumerate(sc["beat_text"]):
            for w in b.split():
                if norm(w):
                    s_tok.append(norm(w)); owner.append((si, bi))
    w_tok = [norm(w["word"]) for w in words]
    sm = difflib.SequenceMatcher(a=s_tok, b=w_tok, autojunk=False)
    s2w = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            s2w[a + k] = b + k
    match_ratio = len(s2w) / max(len(s_tok), 1)
    # first script-token index of each beat -> time of first matched word at/after it
    first_idx = {}
    for i, o in enumerate(owner):
        first_idx.setdefault(o, i)
    def t_at(i):
        for j in range(i, len(s_tok)):
            if j in s2w:
                return words[s2w[j]]["start"]
        return vo_dur
    starts = {o: t_at(i) for o, i in first_idx.items()}
    order = sorted(starts)                       # (scene, beat) order == script order
    times = [starts[o] for o in order]
    for k in range(1, len(times)):               # monotonic guard
        times[k] = max(times[k], times[k - 1] + 0.2)
    times[0] = 0.0
    out_scenes, k = [], 0
    for si, sc in enumerate(scenes):
        beats = []
        for bi, text in enumerate(sc["beat_text"]):
            st = times[k]; en = times[k + 1] if k + 1 < len(times) else vo_dur
            beats.append({"start": round(st, 3), "end": round(en, 3), "text": text}); k += 1
        if not beats:                            # end screen / silent scene
            st = out_scenes[-1]["end"] if out_scenes else 0.0
            beats = [{"start": round(st, 3), "end": round(st + end_screen_s, 3), "text": ""}]
        out_scenes.append({"scene": sc["scene"], "engine": sc["engine"], "asset": sc["asset"],
                           "start": beats[0]["start"], "end": beats[-1]["end"],
                           "duration": round(beats[-1]["end"] - beats[0]["start"], 3), "beats": beats})
    # Flow clips are 8 s and never stretched: move trailing beats of an over-long Flow scene to the next scene
    for i, sc in enumerate(out_scenes[:-1]):
        while sc["engine"] == "Flow" and sc["duration"] > 8.5 and len(sc["beats"]) > 1:
            nxt = out_scenes[i + 1]
            nxt["beats"].insert(0, sc["beats"].pop())
            for x in (sc, nxt):
                x["start"], x["end"] = x["beats"][0]["start"], x["beats"][-1]["end"]
                x["duration"] = round(x["end"] - x["start"], 3)
            nxt.setdefault("moved_in_beats", 0)
            nxt["moved_in_beats"] += 1
    return {"script": script_md, "vo_file": wj["audio_file"], "vo_duration_s": vo_dur,
            "total_duration_s": out_scenes[-1]["end"], "match_ratio": round(match_ratio, 3),
            "scenes": out_scenes}

def report(tl):
    long_beats = [(s["scene"], b["text"][:40], round(b["end"] - b["start"], 2))
                  for s in tl["scenes"] for b in s["beats"] if b["text"] and b["end"] - b["start"] > 6.0]
    flow_long = [(s["scene"], s["asset"], s["duration"]) for s in tl["scenes"]
                 if s["engine"] == "Flow" and s["duration"] > 8.0]
    beats = [b["end"] - b["start"] for s in tl["scenes"] for b in s["beats"] if b["text"]]
    beats.sort()
    print(f"match {tl['match_ratio']:.1%} | total {tl['total_duration_s']:.2f}s | beats {len(beats)} "
          f"| median {beats[len(beats)//2]:.2f}s | >6s: {len(long_beats)} | Flow>8s: {len(flow_long)}")
    for x in long_beats: print("  LONG", x)
    for x in flow_long: print("  FLOW", x)

if __name__ == "__main__":
    tl = align(sys.argv[1], sys.argv[2], float(sys.argv[4]) if len(sys.argv) > 4 else 20.0)
    json.dump(tl, open(sys.argv[3], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    report(tl)
