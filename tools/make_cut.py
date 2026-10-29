"""Sprecher für die Szenen (Vorspann, Festnahme). Vorläufig mit der kostenlosen Edge-Stimme, später ElevenLabs.
Aufruf: python3 tools/make_cut.py"""
import asyncio, os, subprocess, edge_tts
PROXY = os.environ.get("HTTPS_PROXY"); OUT = "src/audio"; T = "tools/tmp"; os.makedirs(T, exist_ok=True)
V = {"erzaehler":("de-DE-FlorianMultilingualNeural","-12%","-6Hz"), "seidl":("de-DE-AmalaNeural","-2%","-2Hz"), "dorn":("de-DE-KatjaNeural","-8%","-3Hz")}
CUT = {
 "CUT_V1":("erzaehler","Landshut. Samstag, 19. Dezember. Neunzehn Uhr."),
 "CUT_V2":("erzaehler","Der Kunstsammler Maximilian von Falkenried hat vier Gäste zum Adventsessen eingeladen. Er will ihnen etwas verkünden."),
 "CUT_V3":("erzaehler","Zwanzig Uhr achtundvierzig. Jemand öffnet die Tür zu seinem Archiv."),
 "CUT_V4":("erzaehler","Einundzwanzig Uhr fünfundzwanzig. Sein Neffe findet ihn. Maximilian von Falkenried ist tot."),
 "CUT_F1":("erzaehler","Die Ringelstecherwiese. Eine Frau im dunklen Mantel betritt die Wiese. Sie glaubt, die Kassette wartet auf sie."),
 "CUT_F2a":("erzaehler","Sie geht auf Notar Mair zu und streckt die Hand aus."),
 "CUT_F2b":("dorn","Geben Sie sie mir."),
 "CUT_F3":("seidl","Zugriff! Doktor Helena Dorn, Sie sind festgenommen wegen Mordes an Maximilian von Falkenried."),
 "CUT_F4":("erzaehler","Eine Stunde später. In Doktor Dorns Wagen: ein Paar Lederhandschuhe, daran Spuren vom Fuß der Messinglampe. Und die Liste von vierzehnhundertfünfundsiebzig, die am Tatort fehlte."),
}
async def main():
    for k, (who, text) in CUT.items():
        v, r, p = V[who]; raw = f"{T}/{k}.raw.mp3"
        await edge_tts.Communicate(text, v, rate=r, pitch=p, proxy=PROXY).save(raw)
        af = "aecho=0.8:0.6:40:0.25,volume=1.2" if k == "CUT_F3" else "volume=1.15"
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",raw,"-af",af,"-ac","1","-b:a","64k",f"{OUT}/{k}.mp3"], check=True)
        print(k, "ok", flush=True)
asyncio.run(main())
