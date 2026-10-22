# Telefonische Vernehmung Jonas Feld (Feld mit Telefonfilter)
import asyncio, os, subprocess, edge_tts
PROXY=os.environ.get("HTTPS_PROXY"); T="tools/tmp"; OUT="src/audio"
V={"seidl":("de-DE-AmalaNeural","-4%","-2Hz"),"feld":("de-AT-JonasNeural","-2%","-3Hz")}
L=[("seidl","Herr Feld, danke, dass Sie zurückrufen. Wo waren Sie am Abend des neunzehnten Dezember?"),
   ("feld","In Regensburg. Ich restauriere gerade ein Altarbild im Dom. Wir haben bis nach zehn gearbeitet, das können Ihnen drei Kollegen bestätigen."),
   ("seidl","Ihre Zutrittskarte wurde an diesem Abend an der Archivtür benutzt."),
   ("feld","Das kann nicht sein. Die Karte ist mir vor einer Woche abhandengekommen. Zuletzt hatte ich sie im Archiv, als ich dort an den Urkunden gearbeitet habe."),
   ("seidl","Haben Sie den Verlust gemeldet?"),
   ("feld","Ich hab es Herrn von Falkenried gesagt. Er meinte nur, die taucht schon wieder auf.")]
async def main():
    seq=[]
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t","0.45",f"{T}/gap.wav"],check=True)
    for i,(w,t) in enumerate(L):
        v,r,p=V[w]; f=f"{T}/F_{i}.mp3"; o=f"{T}/F_{i}.wav"
        await edge_tts.Communicate(t,v,rate=r,pitch=p,proxy=PROXY).save(f)
        af="highpass=f=300,lowpass=f=3400,acompressor,volume=1.3" if w=="feld" else "anull"
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f,"-af",af,"-ar","24000","-ac","1",o],check=True)
        seq+=[o,f"{T}/gap.wav"]
    open(f"{T}/F.txt","w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in seq))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{T}/F.txt","-f","lavfi","-i","anoisesrc=color=brown:amplitude=0.012:r=24000","-filter_complex","[0:a][1:a]amix=inputs=2:duration=first:weights=1 1,volume=1.4","-ac","1","-b:a","64k",f"{OUT}/VERHOER_FELD.mp3"],check=True)
    print("ok")
asyncio.run(main())
