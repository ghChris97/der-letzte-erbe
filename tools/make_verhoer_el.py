"""Vernehmungen mit ElevenLabs (Zeile für Zeile, dann zusammengesetzt mit leisem Raumrauschen).
Texte stammen aus make_verhoer.py und make_verhoer_feld.py. Schlüssel aus ELEVENLABS_API_KEY.
Aufruf: python3 tools/make_verhoer_el.py [VERHOER_HELENA ...]
"""
import ast, os, subprocess, sys
from elevenlabs import ElevenLabs, VoiceSettings

T = "tools/tmp"; OUT = "src/audio"; MODEL = os.environ.get("EL_MODEL", "eleven_v4")
os.makedirs(T, exist_ok=True)
VOICE = {"seidl":"Xb7hH8MSUJpSbSDYk0k2", "helena":"EXAVITQu4vr4xnSDxMaL", "mair":"onwK4e9ZLuTAKqWW03F9",
         "tobias":"TX3LPaxmHKxFdv7VOQHJ", "clara":"hpp4J3VqNfWAUOO0d1Us", "feld":"iP95p4xoKVk53GoZ742B"}

def literal(path, name):
    tree = ast.parse(open(path, encoding="utf-8").read())
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(getattr(t, "id", None) == name for t in n.targets):
            return ast.literal_eval(n.value)
D = literal("tools/make_verhoer.py", "D")
D["VERHOER_FELD"] = literal("tools/make_verhoer_feld.py", "L")

def sh(*a): subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *a], check=True)

def build(client, k):
    sh("-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.45", f"{T}/gap44.wav")
    sh("-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.6", f"{T}/lead44.wav")
    seq = [f"{T}/lead44.wav"]
    for i, (who, text) in enumerate(D[k]):
        mp3 = f"{T}/{k}_{i}.el.mp3"; wav = f"{T}/{k}_{i}.wav"
        if not os.path.exists(mp3):   # bereits bezahlte Zeilen nicht neu erzeugen
            audio = client.text_to_speech.convert(voice_id=VOICE[who], text=text, model_id=MODEL, language_code="de",
                voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.75), output_format="mp3_44100_128")
            open(mp3, "wb").write(b"".join(audio))
        af = "highpass=f=300,lowpass=f=3400,acompressor,volume=1.3" if (k == "VERHOER_FELD" and who == "feld") else "loudnorm=I=-18:TP=-2"
        sh("-i", mp3, "-af", af, "-ar", "44100", "-ac", "1", wav)
        seq += [wav, f"{T}/gap44.wav"]
    open(f"{T}/{k}.txt", "w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in seq))
    sh("-f", "concat", "-safe", "0", "-i", f"{T}/{k}.txt", "-f", "lavfi", "-i", "anoisesrc=color=brown:amplitude=0.008:r=44100",
       "-filter_complex", "[0:a]highpass=f=100,lowpass=f=9000[a];[a][1:a]amix=inputs=2:duration=first:weights=1 1,volume=1.6",
       "-ac", "1", "-b:a", "64k", f"{OUT}/{k}.mp3")
    print(k, "ok", flush=True)

if __name__ == "__main__":
    c = ElevenLabs()
    for k in (sys.argv[1:] or list(D)): build(c, k)
