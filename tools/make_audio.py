import asyncio, os, re, json, subprocess, edge_tts
PROXY=os.environ.get("HTTPS_PROXY")
OUT="src/audio"
CAST={
 "falkenried":dict(voice="de-DE-ConradNeural", rate="-12%", pitch="-8Hz"),
 "unbekannt": dict(voice="de-DE-KatjaNeural",  rate="-10%", pitch="-6Hz", fx="asetrate=24000*0.84,aresample=24000,atempo=1.19,highpass=f=350,lowpass=f=3200,acrusher=bits=11:mix=0.12,volume=1.6"),
 "mair":      dict(voice="de-DE-KillianNeural", rate="-6%",  pitch="-2Hz"),
 "rosa":      dict(voice="de-AT-IngridNeural",  rate="-8%",  pitch="-4Hz"),
 "seidl":     dict(voice="de-DE-AmalaNeural",   rate="-4%",  pitch="-2Hz"),
}
ITEMS={
 "V_START":("seidl","Hallo, hier ist Martina Seidl von der Kripo Landshut. Ihr habt gesehen, was gestern Abend passiert ist. Fünf Menschen waren im Haus, und mindestens einer lügt. Falkenried hatte Angst, dass jemand in seinen Papieren liest. Darum hat er sein Notizbuch, sein Archiv und seine Haustechnik gesperrt und die Schlüssel draußen in der Stadt versteckt. Folgt seiner Spur. Ein Abbild seines Handys spiele ich jetzt auf eure Handys. Der Code lautet: eins, vier, sieben, fünf. Das Jahr der Landshuter Hochzeit. Schaut euch kurz den Tatort an, dann treffen wir uns am Turm von Sankt Martin."),
 "V_ERBE":("falkenried","Hier spricht Maximilian von Falkenried. Wenn ihr das hört, steht ihr vor Ludwig dem Reichen. Um seine Familie geht es in allem, was ich gefunden habe. Vierzehnhundertfünfundsiebzig heiratete sein Sohn Georg in Sankt Martin die polnische Königstochter Hedwig. Ludwig bezahlte alles. Doch Georgs Söhne starben früh. Es blieben nur Töchter, und das wurde zum Problem. Wer dieses Problem hatte, steht ebenfalls an der Herzogswand, ganz unten links. Geht zurück und sucht ihn. Dann erzähle ich weiter."),
 "V_ALBRECHT":("falkenried","Das Land durfte nur an Männer der Familie fallen. Georg setzte trotzdem seine Tochter Elisabeth als Erbin ein. Als er im Dezember fünfzehnhundertdrei starb, zog Albrecht gegen sie in den Krieg, und er gewann. Elisabeth starb noch im Kriegsjahr. Von ihren kleinen Söhnen, heißt es, starben zwei im selben Jahr. Ich habe angefangen, daran zu zweifeln. In den Wintertagen nach Georgs Tod brachte jemand eine Kiste aus der Stadt. Was darin war, steht in zwei Listen in meiner Mappe. Ihr Schloss hat drei Räder. Was ihr einstellen müsst, hängt dort, wo die Bürger dieser Stadt seit Jahrhunderten ihren Rat halten."),
 "V_RESIDENZ":("seidl","Seidl hier. Gute Arbeit, der Brief ist gefälscht. Wer alte Stücke teuer verkaufen will, braucht einen Nachweis, woher sie stammen. Erstellt hat die Datei Doktor Helena Dorn, geöffnet hat sie auch Notar Mair. Einen Mord beweist das noch nicht. Wir müssen wissen, wer am Tatabend an die Archivtür kam. Das steht in Falkenrieds App Haustechnik. Sie öffnet sich nur an der Kirche, deren Bau unter Heinrich dem Reichen begann."),
 "V_TURM":("falkenried","Sie wollten hier einen Turm, höher als Sankt Martin. Das Geld reichte nicht. Manche wollen eben mehr, als ihnen zusteht."),
 "V_ZEUGIN":("rosa","Hier ist Rosa Brandl, die Haushälterin. Mir ist noch etwas eingefallen. Kurz vor neun stand Frau Weiß im Flur und telefonierte, ganz leise. Ich habe nur verstanden: Der Wagen soll die Stadt durch das Tor verlassen, über dem die drei Helme hängen. Und hinter ihr ging eine Frau zum Archiv, im langen dunklen Mantel, die Kapuze auf. Die Gäste hatten ihre Mäntel doch längst an der Garderobe. Dann klickte die Archivtür."),
 "V_MAIR":("mair","Hier spricht Benedikt Mair, der Notar von Herrn von Falkenried. Ja, ich habe geschwiegen, und das tut mir leid. Er hat mir im Herbst eine Kassette anvertraut und mich zur Verschwiegenheit verpflichtet. Am Tatabend habe ich draußen mit der Stadt telefoniert, wegen der Übergabe. Den Brief habe ich nur geöffnet, weil er mir seltsam vorkam. Die Kassette gebe ich denen, die herausgefunden haben, was ihm zugestoßen ist. Das seid ihr. Ach ja, und noch etwas: Herr von Falkenried hat mir eine Sprachnachricht hinterlassen. Für euch. Hört sie euch an."),
 "V_FINALE":("falkenried","Hier spricht Maximilian von Falkenried. Wenn ihr das hört, ist mir etwas zugestoßen. Ich wollte nie etwas verkaufen. Fünfzehnhundertvier hieß es, Elisabeths kleiner Sohn Georg sei gestorben. Es war gelogen. Derselbe treue Mann, der die Kiste aus der Stadt gebracht hatte, brachte auch den Jungen in Sicherheit. Die Kiste war sein Erbe. Ich glaube, dass ich von diesem Georg abstamme. Vielleicht irre ich mich. Aber was in der Kiste war, gehört zurück nach Landshut. Das Schloss kennt nur einen Namen: den der Frau, der all das gehören sollte."),
 "CALL_01":("unbekannt","Sie sind also gekommen. Hören Sie gut zu. Falkenried hat etwas gefunden, das fünfhundert Jahre verschwunden war. Deshalb ist er tot. Folgen Sie seiner Spur. Sein Notizbuch öffnet sich mit der Höhe des Turms über Ihnen."),
 "CALL_06":("unbekannt","Ihr seid gut. Aber ihr schaut auf die Falschen. Clara Weiß, die Kunsthändlerin, lügt, glaubt mir. Und Notar Mair war achtzehn Minuten verschwunden. Um zwanzig Uhr achtundvierzig ging die Archivtür auf, mit der Karte R sieben."),
 "CALL_07":("unbekannt","Ihr seid sehr nah dran. Notar Mair wartet auf der Ringelstecherwiese, er hat etwas für euch. Holt es dort ab, aber öffnet es nicht. Ich komme und nehme es euch ab."),
 "ZEUGIN_KURZ":("rosa","Kurz vor neun stand Frau Weiß im Flur und telefonierte. Hinter ihr ging eine Frau zum Archiv, im langen dunklen Mantel, die Kapuze auf. Die Gäste hatten ihre Mäntel doch längst an der Garderobe. Dann klickte die Archivtür."),
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
