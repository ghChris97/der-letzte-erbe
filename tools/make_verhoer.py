import asyncio, os, subprocess, json, edge_tts
PROXY=os.environ.get("HTTPS_PROXY"); T="tools/tmp"; OUT="src/audio"
V={"seidl":("de-DE-AmalaNeural","-4%","-2Hz"),"helena":("de-DE-KatjaNeural","-6%","-2Hz"),"mair":("de-DE-KillianNeural","-6%","-2Hz"),
   "tobias":("de-DE-FlorianMultilingualNeural","+2%","+0Hz"),"clara":("de-DE-SeraphinaMultilingualNeural","-4%","-4Hz")}
D={
 "VERHOER_HELENA":[("seidl","Frau Doktor Dorn, wann haben Sie das Haus verlassen?"),("helena","Ich bin um halb neun gegangen. Kopfschmerzen. Ich habe mich im Flur verabschiedet, das hat Frau Brandl gesehen."),("seidl","Und dann?"),("helena","Direkt ins Hotel. Um kurz nach neun lag ich im Bett. Von alldem habe ich erst heute Morgen erfahren."),("seidl","Sie haben Herrn von Falkenrieds Archiv betreut?"),("helena","Seit drei Jahren. Ich kenne jedes Blatt darin. Gerade deshalb tut das so weh.")],
 "VERHOER_MAIR":[("seidl","Herr Mair, Sie waren während des Abends eine Weile nicht im Salon."),("mair","Ich habe kurz telefoniert, draußen. Ein beruflicher Anruf."),("seidl","Mit wem?"),("mair","Dazu kann ich nichts sagen. Ich bin an meine Schweigepflicht gebunden."),("seidl","Wie lange waren Sie draußen?"),("mair","Ein paar Minuten. Mehr nicht.")],
 "VERHOER_TOBIAS":[("seidl","Herr von Falkenried, man hat Sie mit Ihrem Onkel streiten hören."),("tobias","Ja, wir haben gestritten. Laut. Es ging um Geld, um was sonst."),("seidl","Und danach?"),("tobias","Danach war ich rauchen, auf der Terrasse. Bestimmt eine Viertelstunde. Ich wollte nicht mehr rein."),("seidl","Sie haben ihn gefunden."),("tobias","Kurz vor halb zehn. Die Archivtür stand offen. Ich … ich will darüber nicht reden.")],
 "VERHOER_CLARA":[("seidl","Frau Weiß, wo waren Sie zwischen halb neun und neun?"),("clara","Im Salon. Den ganzen Abend. Fragen Sie die anderen."),("seidl","Sie haben ein Taxi bestellt."),("clara","Ja, gegen neun. Ich wollte nach Hause, die Stimmung war … unangenehm."),("seidl","Kannten Sie Herrn von Falkenrieds Sammlung?"),("clara","Natürlich. Ich bin Kunsthändlerin. Aber nur aus seinen Erzählungen.")],
}
async def line(i,k,who,text):
    v,r,p=V[who]; f=f"{T}/{k}_{i}.mp3"
    await edge_tts.Communicate(text,v,rate=r,pitch=p,proxy=PROXY).save(f); return f
async def main():
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t","0.45",f"{T}/gap.mp3"],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","lavfi","-i","anullsrc=r=24000:cl=mono","-t","0.6",f"{T}/lead.mp3"],check=True)
    tx={}
    for k,lines in D.items():
        files=[await line(i,k,w,t) for i,(w,t) in enumerate(lines)]
        seq=[f"{T}/lead.mp3"]
        for f in files: seq+=[f,f"{T}/gap.mp3"]
        open(f"{T}/{k}.txt","w").write("".join(f"file '{x}'\n" for x in seq))
        # leises Raumrauschen wie bei einer Aufnahme
        subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"{T}/{k}.txt","-ar","24000","-ac","1",f"{T}/{k}_dry.wav"],check=True)
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"{T}/{k}_dry.wav","-f","lavfi","-i","anoisesrc=color=brown:amplitude=0.012:r=24000","-filter_complex","[0:a]highpass=f=120,lowpass=f=7000[a];[a][1:a]amix=inputs=2:duration=first:weights=1 1,volume=1.4","-ac","1","-b:a","64k",f"{OUT}/{k}.mp3"],check=True)
        print(k,"ok")
asyncio.run(main())
