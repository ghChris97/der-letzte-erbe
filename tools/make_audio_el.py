"""Sprachaufnahmen mit ElevenLabs erzeugen (ersetzt make_audio.py, gleiche Dateinamen und cues.json).
Schlüssel kommt aus der Umgebung (ELEVENLABS_API_KEY), z. B. per:  set -a; . ./.env.local; set +a
Aufruf:  python3 tools/make_audio_el.py V_START CALL_01      (ohne Argumente: alle)
"""
import base64, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from elevenlabs import ElevenLabs, VoiceSettings

OUT = "src/audio"; TMP = "tools/tmp"; os.makedirs(TMP, exist_ok=True)
MODEL = os.environ.get("EL_MODEL", "eleven_v4")

# Besetzung (Standardstimmen, Free-Konto). Unbekannt wird zusätzlich verfremdet.
CAST = {
    "seidl":      dict(voice="Xb7hH8MSUJpSbSDYk0k2", stab=0.55),   # Alice
    "falkenried": dict(voice="JBFqnCBsd6RMkjVDRZzb", stab=0.45),   # George
    "mair":       dict(voice="onwK4e9ZLuTAKqWW03F9", stab=0.55),   # Daniel
    "rosa":       dict(voice="XrExE9yKIg1WjnnlVkGX", stab=0.5),    # Matilda
    "unbekannt":  dict(voice="FGY2WhTYpPnrIDTdsKH5", stab=0.4,     # Laura, verzerrt
                       fx="asetrate=44100*0.84,aresample=44100,atempo=1.19,highpass=f=350,lowpass=f=3200,acrusher=bits=11:mix=0.12,volume=1.6"),
}
# Texte wie bisher aus make_audio.py
src = open(os.path.join(os.path.dirname(__file__), "make_audio.py"), encoding="utf-8").read()
ITEMS = {k: (who, text) for k, who, text in re.findall(r'"([A-Z_0-9]+)":\("(\w+)","(.*?)"\)', src)}

SENT = re.compile(r'[^.!?…]+(?:[.!?…]+[“”"]?|$)\s*')   # wie sentencesOf() in der App

def cues_from_alignment(text, al):
    chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    spoken = "".join(chars)
    # Alignment-Zeichen auf den Originaltext abbilden (Normalisierung kann abweichen: dann proportional)
    out, pos = [], 0
    sents = SENT.findall(text) or [text]
    total = len(text)
    for s in sents:
        a, b = pos, pos + len(s); pos = b
        if spoken == text:
            i, j = a, max(a, b - 1)
            while j > a and text[j].isspace(): j -= 1
            out.append([round(st[i], 3), round(en[j], 3)])
        else:
            dur = en[-1]
            out.append([round(dur * a / total, 3), round(dur * b / total, 3)])
    return out

def one(client, k):
    who, text = ITEMS[k]; c = CAST[who]
    r = client.text_to_speech.convert_with_timestamps(
        voice_id=c["voice"], text=text, model_id=MODEL, language_code="de",
        voice_settings=VoiceSettings(stability=c["stab"], similarity_boost=0.75),
        output_format="mp3_44100_128")
    d = r.model_dump(); json.dump(d, open(f"{TMP}/{k}.el.json", "w"))   # erst sichern, dann verarbeiten
    raw = f"{TMP}/{k}.el.mp3"; open(raw, "wb").write(base64.b64decode(d.get("audio_base_64") or d.get("audio_base64")))
    af = c.get("fx", "loudnorm=I=-16:TP=-1.5:LRA=11")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", af, "-ac", "1", "-b:a", "64k", f"{OUT}/{k}.mp3"], check=True)
    cues = cues_from_alignment(text, d.get("normalized_alignment") if False else d["alignment"])
    if c.get("fx"):  # Tempo-Änderung der Verfremdung (0.84 * 1.19 ≈ 1.0) ändert die Zeiten kaum
        cues = [[round(a / 0.9996, 3), round(b / 0.9996, 3)] for a, b in cues]
    return cues

def main():
    client = ElevenLabs()
    keys = sys.argv[1:] or list(ITEMS)
    p = f"{OUT}/cues.json"; old = json.load(open(p)) if os.path.exists(p) else {}
    for k in keys:
        old[k] = one(client, k); print(k, len(old[k]), "Sätze", flush=True)
        json.dump(old, open(p, "w"))

if __name__ == "__main__":
    main()
