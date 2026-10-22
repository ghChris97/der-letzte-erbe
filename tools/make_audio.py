import asyncio, os, re, json, subprocess, edge_tts
PROXY=os.environ.get("HTTPS_PROXY")
OUT="src/audio"
CAST={
 "falkenried":dict(voice="de-DE-ConradNeural", rate="-12%", pitch="-8Hz"),
 "unbekannt": dict(voice="de-DE-KatjaNeural",  rate="-10%", pitch="-6Hz", fx="asetrate=24000*0.84,aresample=24000,atempo=1.19,highpass=f=350,lowpass=f=3200,acrusher=bits=11:mix=0.12,volume=1.6"),
 "mair":      dict(voice="de-DE-KillianNeural", rate="-6%",  pitch="-2Hz"),
 "rosa":      dict(voice="de-AT-IngridNeural",  rate="-8%",  pitch="-4Hz"),
}
ITEMS={
 "CALL_01":("unbekannt","Sie sind also gekommen. Falkenried hat gehofft, dass jemand die Zeichen versteht. Suchen Sie zuerst nach der Rechnung für ein Fest, das eine ganze Stadt satt machte. Und fragen Sie sich: Wer hat die Zeche wirklich bezahlt? Und wem sollte am Ende alles gehören? Verwechseln Sie die Namen nicht."),
 "CALL_06":("unbekannt","Ihr seid gut. Aber ihr schaut auf die Falschen. Die Kunsthändlerin lügt, das habt ihr gesehen. Und der Notar war achtzehn Minuten weg. Um zwanzig Uhr achtundvierzig ging die Archivtür auf, mit der Karte R sieben. Und das alles nur wegen dem Pfand der Verbindung."),
 "CALL_07":("unbekannt","Ihr seid sehr nah dran. Der Notar wird euch gleich etwas geben. Öffnet es nicht. Bringt es auf die Wiese, ich kümmere mich um den Rest."),
 "V_ERBE":("falkenried","Erster Dezember fünfzehnhundertdrei. In Ingolstadt stirbt Herzog Georg der Reiche. Er hinterlässt keinen Sohn, nur eine Tochter: Elisabeth. Und er hat etwas getan, das kein Wittelsbacher vor ihm gewagt hat. Gegen alle Hausverträge setzt er sie als Erbin ein. Sie und ihren Mann, Ruprecht von der Pfalz. In München liest Herzog Albrecht dieses Testament … und lacht nicht. Er ist Georgs Vetter. Nach Familienrecht gehört Landshut ihm. Was folgt, ist kein Streit mehr. Es ist Krieg. Dörfer brennen in ganz Niederbayern. Der König stellt sich auf Albrechts Seite und lässt sich das gut bezahlen. Und Elisabeth? Im Sommer fünfzehnhundertvier stirbt Ruprecht. Wenige Wochen später stirbt auch sie. Am Ende bekommt Albrecht das Land. Aber in den Wintertagen nach Georgs Tod, als noch niemand wusste, wer gewinnen würde … da hat jemand drei Kisten aus der Stadt gebracht. Und nicht nur Kisten. Was genau verschwunden ist, steht in zwei Listen. Lest sie dort, wo diese Stadt seit Jahrhunderten regiert wird."),
 "V_RESIDENZ":("falkenried","Wenn ihr das hört, habt ihr die Lüge gesehen. Ein falscher Brief macht noch keinen falschen Schatz. Achtet auf die Worte: Wer fälscht, verrät sich durch seine Sprache. Und fragt euch, wer am Abend an meine Archivtür kam. Die Antwort liegt in der zweiten Kirche des Baumeisters."),
 "V_TURM":("falkenried","Sie wollten hier einen Turm, höher als Sankt Martin. Das Geld reichte nicht. Manche wollen eben mehr, als ihnen zusteht."),
 "V_ZEUGIN":("rosa","Kurz nach Viertel vor neun ging das Licht aus. Ich hörte Schritte im Flur, eine Frau im dunklen Mantel. Dann klickte die Archivtür. Ich dachte mir nichts. Die Tür hat ja Strom aus der Batterie. Später hörte ich am Telefon, der Wagen sollte die Stadt durch das Tor verlassen, über dem die drei Helme hängen."),
 "ZEUGIN_KURZ":("rosa","Kurz nach Viertel vor neun ging das Licht aus. Ich hörte Schritte im Flur, eine Frau im dunklen Mantel. Dann klickte die Archivtür. Ich dachte mir nichts. Die Tür hat ja Strom aus der Batterie."),
 "V_MAIR":("mair","Ja, ich habe geschwiegen. Herr von Falkenried hat mir eine Kassette anvertraut und mich zur Verschwiegenheit verpflichtet. Am Tatabend habe ich mit der Verwahrstelle telefoniert, wegen der Übergabe an die Stadt. Die Datei habe ich geöffnet, weil ich prüfen wollte, was Frau Dorn ihm da vorgelegt hatte. Die Kassette und seine letzte Nachricht gebe ich nur Ermittlern."),
 "V_FINALE":("falkenried","Wenn ihr das hört, hat jemand meine Geschichte benutzt, um reich zu werden. Ich wollte nichts verkaufen. Im Winter fünfzehnhundertdrei hieß es, Elisabeths jüngstes Kind sei gestorben. Es war gelogen. Ein treuer Mann hat das Kind aus der Stadt gebracht, und mit ihm drei Kisten, sein Erbe. Man hat Elisabeth das Land genommen, den Mann und das Leben. Aber ihr Kind haben sie nicht bekommen. Ich glaube, dass ich von diesem Kind abstamme. Vielleicht irre ich mich. Aber das, was es mitnahm, gehört zurück nach Landshut. Das Schloss kennt nur einen Namen: den der Frau, der all das gehören sollte. Und gebt es niemandem, der euch nur eine Stimme angeboten hat."),
}
def ts(t):
    h,m,s=t.replace(",",".").split(":"); return round(int(h)*3600+int(m)*60+float(s),3)
async def one(k):
    who,text=ITEMS[k]; c=CAST[who]
    raw=f"tools/tmp/{k}.raw.mp3"; vtt=f"tools/tmp/{k}.vtt"
    sub=edge_tts.SubMaker()
    com=edge_tts.Communicate(text,c["voice"],rate=c["rate"],pitch=c["pitch"],proxy=PROXY,boundary="SentenceBoundary")
    with open(raw,"wb") as f:
        async for ch in com.stream():
            if ch["type"]=="audio": f.write(ch["data"])
            elif ch["type"] in ("WordBoundary","SentenceBoundary"): sub.feed(ch)
    open(vtt,"w").write(sub.get_srt())
    out=f"{OUT}/{k}.mp3"
    af=c.get("fx","volume=1.15")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",raw,"-af",af,"-ac","1","-b:a","64k",out],check=True)
    cues=[[ts(a),ts(b)] for a,b in re.findall(r"(\d\d:\d\d:\d\d,\d+) --> (\d\d:\d\d:\d\d,\d+)",open(vtt).read())]
    return k,cues
async def main():
    keys=sys_keys or list(ITEMS)
    res={}
    for k in keys:
        kk,c=await one(k); res[kk]=c; print(k,len(c),"Sätze")
    p=f"{OUT}/cues.json"
    old=json.load(open(p)) if os.path.exists(p) else {}
    old.update(res); json.dump(old,open(p,"w"))
import sys; sys_keys=sys.argv[1:]
asyncio.run(main())
