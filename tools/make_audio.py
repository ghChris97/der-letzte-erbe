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
 "V_START":("seidl","Hallo, hier ist Martina Seidl, Kriminalhauptkommissarin bei der Kripo Landshut. Danke, dass ihr so schnell erreichbar seid. Gestern Abend wurde der Kunstsammler Maximilian von Falkenried tot in seinem Archiv gefunden. In seinem eigenen Haus, während nebenan seine Gäste beim Adventsessen saßen. Wir gehen von Mord aus. Fünf Menschen waren an dem Abend im Haus, und mindestens einer von ihnen lügt.  Falkenried hatte Angst, dass jemand in seinen Papieren liest. Deshalb hat er alles Wichtige gesperrt: sein Notizbuch, sein Archiv, seine Haustechnik. Die Schlüssel dazu hat er draußen in der Stadt versteckt. Ich glaube, er wollte, dass jemand seiner Spur folgt, falls ihm etwas zustößt. Das seid jetzt ihr.  Sein Handy haben wir sichergestellt. Ein Abbild davon spiele ich gerade auf eure Handys. Der Code lautet: eins, vier, sieben, fünf. Vierzehnhundertfünfundsiebzig, das Jahr der Landshuter Hochzeit. Falkenried war besessen von dieser Hochzeit und von den Wittelsbachern, die damals hier geherrscht haben. Ich bin sicher: Was er über sie herausgefunden hat, ist der Grund, warum er sterben musste.  Schaut euch jetzt den Tatort an und tragt euch als Ermittlungsgruppe ein. Danach treffen wir uns am Turm von Sankt Martin."),
 "V_ERBE":("falkenried","Hier spricht Maximilian von Falkenried. Wenn ihr das hört, habt ihr mein Archiv geöffnet und steht am Dreifaltigkeitsplatz vor Ludwig dem Reichen. Schaut aber zuerst einmal den Hang hinauf. Dort oben thront Burg Trausnitz. Ludwig der Kelheimer hat sie zwölfhundertvier gegründet, zusammen mit der Stadt. Von da oben regierten die Herzöge von Niederbayern über Landshut, bis fünfzehnhundertdrei. Die drei Reichen Herzöge bauten sie prächtig aus, mit neuen Sälen, Mauern und Türmen. In einer Oktobernacht neunzehnhunderteinundsechzig brannte der Fürstenbau aus, mit den prunkvollen Zimmern von König Ludwig dem Zweiten. In den Akten steht als Ursache ein Tauchsieder. Restauriert wird bis heute.  Aber zurück zu Ludwig dem Reichen. Lasst mich euch von seiner Familie erzählen, denn um sie geht es in allem, was ich gefunden habe.  Ludwigs Vater war Heinrich, der erste der drei Reichen Herzöge von Landshut. Er hinterließ seinem Sohn eine volle Schatzkammer. Ludwig machte daraus das prächtigste Fest, das diese Stadt je gesehen hat. vierzehnhundertfünfundsiebzig heiratete sein Sohn Georg in Sankt Martin die polnische Königstochter Hedwig. Tausende Gäste kamen, Ritter aus halb Europa, und Ludwig bezahlte alles.  Georg und Hedwig bekamen Kinder, doch ihre Söhne starben früh. Es blieben zwei Töchter. Und das wurde zum Problem. Wer dieses Problem hatte, steht ebenfalls an der Wand, ganz unten. Geht noch einmal zurück und sucht ihn. Dann erzähle ich weiter."),
 "V_ALBRECHT":("falkenried","Nach den Hausverträgen der Wittelsbacher durfte das Land nur an Männer der Familie fallen. Georg setzte trotzdem seine Tochter Elisabeth als Erbin ein, sie und ihren Mann, Ruprecht von der Pfalz. Am ersten Dezember fünfzehnhundertdrei starb Georg in Ingolstadt. In München las Albrecht das Testament, und er lachte nicht.  Es folgte der Landshuter Erbfolgekrieg. Dörfer brannten in ganz Niederbayern. Der König stellte sich auf Albrechts Seite und ließ sich das gut bezahlen. Im Sommer fünfzehnhundertvier starb Ruprecht, wenige Wochen später auch Elisabeth. Sie hinterließen vier kleine Söhne. Die Zwillinge Georg und Ruprecht starben noch im selben Jahr. So steht es jedenfalls in den Büchern. Ich habe angefangen, daran zu zweifeln.  fünfzehnhundertfünf entschied der König in Köln: Landshut ging an Albrecht nach München. Für die beiden übrigen Söhne schuf man ein kleines Land an der Donau, mit der Hauptstadt Neuburg.  Aber in den Wintertagen nach Georgs Tod, als noch niemand wusste, wer gewinnen würde, brachte jemand eine Kiste aus der Stadt. Was darin war, steht in zwei Listen in meiner Mappe. Die Mappe hat ein Schloss mit drei Rädern. Was ihr einstellen müsst, hängt dort, wo die Bürger dieser Stadt seit Jahrhunderten ihren Rat halten."),
 "V_RESIDENZ":("seidl","Hallo, hier ist noch einmal Kommissarin Seidl. Gute Arbeit, der Brief ist gefälscht. Ich glaube, ich weiß auch, wozu: Wer alte Stücke verkaufen will, braucht einen Nachweis, woher sie stammen. Ein Brief aus der Herzogsresidenz macht aus drei alten Stücken einen Schatz, für den ein Sammler viel Geld bezahlt.  Erstellt hat die Datei Doktor Helena Dorn, die Historikerin, die Falkenrieds Archiv betreut hat. Geöffnet hat sie auch Notar Mair. Einen Mord beweist das noch nicht. Dafür müssen wir wissen, wer am Tatabend an die Archivtür kam. Der Kartenleser hat jeden Zutritt gespeichert, das war Spur fünf am Tatort. Die Daten liegen in Falkenrieds App Haustechnik. Wo sie sich öffnet, steht auf der Rückseite seiner Fassadenfotos."),
 "V_TURM":("falkenried","Sie wollten hier einen Turm, höher als Sankt Martin. Das Geld reichte nicht. Manche wollen eben mehr, als ihnen zusteht."),
 "V_ZEUGIN":("rosa","Hier ist Rosa Brandl, ich führe bei Herrn von Falkenried den Haushalt. Mir ist noch etwas eingefallen. Kurz vor neun ging ich durch den Flur. Da stand Frau Weiß und telefonierte, ganz leise. Ich habe nur einen Satz verstanden: Der Wagen soll die Stadt durch das Tor verlassen, über dem die drei Helme hängen. Und hinter ihr ging eine Frau zum Archiv, im langen dunklen Mantel, die Kapuze auf. Ich dachte, ein Gast holt noch etwas. Aber die Gäste hatten ihre Mäntel doch längst an der Garderobe. Dann klickte die Archivtür."),
 "V_MAIR":("mair","Hier spricht Benedikt Mair, ich bin der Notar von Herrn von Falkenried. Ja, ich habe geschwiegen, und das tut mir leid. Herr von Falkenried hat mir im Herbst eine Kassette anvertraut und mich zur Verschwiegenheit verpflichtet. Am Tatabend habe ich draußen mit dem Kulturreferenten der Stadt telefoniert, wegen der Übergabe. Achtzehn Minuten, ja. Den Brief habe ich geöffnet, weil Frau Doktor Dorn ihn Herrn von Falkenried als Beweis vorgelegt hatte und mir das seltsam vorkam. Die Kassette gebe ich nur denen, die herausgefunden haben, was ihm zugestoßen ist. Das seid ihr."),
 "V_FINALE":("falkenried","Hier spricht Maximilian von Falkenried. Wenn ihr das hört, ist mir etwas zugestoßen. Dann hat jemand versucht, meine Geschichte zu Geld zu machen. Ich wollte nie etwas verkaufen.  fünfzehnhundertvier, im Kriegsjahr, hieß es, Elisabeths kleiner Sohn Georg sei gestorben, wie sein Zwillingsbruder Ruprecht. Es war gelogen. Derselbe treue Mann, der im Winter davor die Kiste aus der Stadt gebracht hatte, brachte auch den Jungen in Sicherheit. Die Kiste war sein Erbe. Man hat Elisabeth das Land genommen, den Mann und das Leben. Aber ihren Sohn haben sie nicht bekommen.  Ich glaube, dass ich von diesem Georg abstamme. Vielleicht irre ich mich. Aber was in der Kiste war, gehört zurück nach Landshut. Das Schloss kennt nur einen Namen: den der Frau, der all das gehören sollte."),
 "CALL_01":("unbekannt","Sie sind also gekommen. Hören Sie gut zu, ich habe nicht viel Zeit. Falkenried hat etwas gefunden, das fünfhundert Jahre verschwunden war. Deshalb ist er tot. Wenn Sie seiner Spur folgen, finden Sie, was er gefunden hat. Sein Notizbuch öffnet sich mit der Höhe des Turms über Ihnen. Darin steht die Rechnung für ein Fest, bei dem eine ganze Stadt satt wurde. Fragen Sie sich, wer die Zeche bezahlt hat."),
 "CALL_06":("unbekannt","Ihr seid gut. Aber ihr schaut auf die Falschen. Clara Weiß, die Kunsthändlerin, lügt, glaubt mir. Und Notar Mair war achtzehn Minuten verschwunden. Um zwanzig Uhr achtundvierzig ging die Archivtür auf, mit der Karte R sieben."),
 "CALL_07":("unbekannt","Ihr seid sehr nah dran. Notar Mair wird euch gleich etwas geben. Öffnet es nicht. Bringt es auf die Ringelstecherwiese, ich hole es dort ab."),
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
