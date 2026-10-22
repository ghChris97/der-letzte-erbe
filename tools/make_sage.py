# Sage vom Ritter am Ländtor: Falkenried erzählt, dann 7 Glockenschläge und Hufschläge (synthetisch).
import asyncio, os, subprocess, numpy as np, edge_tts, wave
PROXY=os.environ.get("HTTPS_PROXY"); T="tools/tmp"; SR=24000
TEXT=("Am Ländtor erzählen sich die Leute eine alte Geschichte. Im Kriegsjahr fünfzehnhundertvier, in einer Nacht ohne Mond, "
 "schlug die Glocke von Sankt Martin die volle Stunde. Bei jedem Schlag kam ein Ritter näher, und beim letzten ritt er durch dieses Tor hinaus zur Isar. "
 "Unter seinem Mantel trug er etwas, das niemand sehen durfte. Seither, sagt man, hört man ihn wieder, wenn die Glocke diese Stunde schlägt. Hört genau hin, und zählt mit.")
N=7
def bell(dur=2.4):
    t=np.arange(int(SR*dur))/SR; f=[220,440,660,880,1320]; a=[1,.55,.35,.22,.12]; d=[.9,.7,.5,.35,.25]
    return sum(ai*np.sin(2*np.pi*fi*t)*np.exp(-t/di) for fi,ai,di in zip(f,a,d))*np.minimum(1,t*200)
def hoof():
    n=int(SR*.06); t=np.arange(n)/SR; return np.random.randn(n)*np.exp(-t/.012)*.9 + np.sin(2*np.pi*90*t)*np.exp(-t/.02)
def gallop(sec=4.5):
    out=np.zeros(int(SR*sec)); pos=0; step=.32
    for i in range(int(sec/step)):
        g=(i/(sec/step)); amp=min(1,0.25+1.6*g) if g<.6 else max(.15,1.6*(1-g))
        for off in (0,.08,.17):
            k=int((pos+off)*SR); h=hoof()*amp; out[k:k+len(h)]+=h[:len(out)-k]
        pos+=step
    return out
async def main():
    await edge_tts.Communicate(TEXT,"de-DE-ConradNeural",rate="-12%",pitch="-8Hz",proxy=PROXY).save(f"{T}/sage_v.mp3")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{T}/sage_v.mp3","-ar",str(SR),"-ac","1",f"{T}/sage_v.wav"],check=True)
    w=wave.open(f"{T}/sage_v.wav"); v=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float)/32768
    seg=[v, np.zeros(int(SR*1.2))]
    for i in range(N-1): b=bell(); seg.append(b[:int(SR*1.7)]*.5)  # plus ein ausklingender = N Schläge
    seg.append(bell()*.5*np.linspace(1,0,int(SR*2.4))); seg.append(gallop()*.6); seg.append(np.zeros(int(SR*.8)))
    a=np.concatenate(seg); wind=np.convolve(np.random.randn(len(a)),np.ones(400)/400,mode="same")*.25
    a=a+wind; a=a/np.max(np.abs(a))*.9
    with wave.open(f"{T}/sage.wav","wb") as o: o.setnchannels(1); o.setsampwidth(2); o.setframerate(SR); o.writeframes((a*32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{T}/sage.wav","-b:a","64k","src/audio/SAGE_LAENDTOR.mp3"],check=True)
    print("ok", round(len(a)/SR,1),"s")
asyncio.run(main())
