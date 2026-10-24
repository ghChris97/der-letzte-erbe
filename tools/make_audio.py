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
 "V_START_B":("seidl","Noch etwas zum Code: Vierzehnhundertfünfundsiebzig, das ist das Jahr der Landshuter Hochzeit. Falkenried war besessen von dieser Hochzeit und von den Wittelsbachern. Jahrelang hat er ihren Stammbaum erforscht. Warum, wissen wir noch nicht. Wir treffen uns am Turm von Sankt Martin."),
 "V_START":("seidl","Hallo, hier spricht Martina Seidl, Kriminalhauptkommissarin bei der Kripo Landshut. Danke, dass ihr so schnell erreichbar seid. Gestern Abend wurde der Kunstsammler Maximilian von Falkenried tot in seinem Archiv gefunden. Wir gehen von Mord aus. Den ersten Bericht schicke ich euch gleich hinterher. Falkenrieds Handy haben wir sichergestellt und alle Daten heruntergeladen. Ein Abbild davon wird gerade auf eure Handys gespielt. Ihr könnt es bedienen wie sein eigenes Telefon, mit Nachrichten, Mailbox und Notizen. Der Code zum Entsperren lautet: eins, vier, sieben, fünf. Merkt ihn euch gut. Ich brauche eure Hilfe, und zwar dringend. Gebt mir eure Namen, dann trage ich euch als Ermittlungsgruppe ein. Danach kommt niemand mehr dazu."),
 "CALL_01":("unbekannt","Sie sind also gekommen. Falkenried hat gehofft, dass jemand die Zeichen versteht. Fangen Sie bei seinem Notizbuch an. Er hat es mit einer Zahl verschlossen, die hier über Ihnen in den Himmel ragt. Darin finden Sie die Rechnung für ein Fest, das eine ganze Stadt satt machte. Und dann fragen Sie sich: Wer hat die Zeche wirklich bezahlt?"),
 "CALL_06":("unbekannt","Ihr seid gut. Aber ihr schaut auf die Falschen. Clara Weiß, die Kunsthändlerin, lügt, glaubt mir. Und Notar Mair war achtzehn Minuten weg. Um zwanzig Uhr achtundvierzig ging die Archivtür auf, mit der Karte R sieben."),
 "CALL_07":("unbekannt","Ihr seid sehr nah dran. Notar Mair wird euch gleich etwas geben. Öffnet es nicht. Bringt es auf die Ringelstecherwiese, ich kümmere mich um den Rest."),
 "V_ERBE":("falkenried","Wenn ihr das hört, steht ihr vor Ludwig dem Reichen. Lasst mich euch seine Familie erzählen, denn um sie geht es in allem, was ich gefunden habe. Ludwigs Vater war Heinrich, der erste der drei Reichen Herzöge von Landshut. In seiner Zeit begann der Bau von Heiliggeist, und er hinterließ seinem Sohn eine volle Schatzkammer. Ludwig machte daraus das prächtigste Fest, das diese Stadt je gesehen hat. Vierzehnhundertfünfundsiebzig heiratete sein Sohn Georg in Sankt Martin Hedwig, die Tochter des polnischen Königs. Tausende Gäste kamen, Ritter aus halb Europa, und Ludwig hat alles bezahlt. Georg und Hedwig bekamen Kinder, doch ihre Söhne starben früh. Am Ende blieben zwei Töchter."),
 "V_ALBRECHT":("falkenried","Und genau das wurde zum Problem. Nach den Hausverträgen der Wittelsbacher durfte das Land nur an Männer der Familie fallen. Georg setzte trotzdem seine Tochter Elisabeth als Erbin ein, sie und ihren Mann, Ruprecht von der Pfalz. Am ersten Dezember fünfzehnhundertdrei starb Georg in Ingolstadt. In München las sein Vetter, Herzog Albrecht, das Testament, und er lachte nicht. Was folgte, war kein Streit mehr. Es war der Landshuter Erbfolgekrieg. Dörfer brannten in ganz Niederbayern. Der König stellte sich auf Albrechts Seite und ließ sich das gut bezahlen. Im Sommer fünfzehnhundertvier starb Ruprecht, wenige Wochen später auch Elisabeth. Sie hinterließen vier kleine Söhne in einem Land voller Feinde. Die Zwillinge Georg und Ruprecht starben noch im selben Jahr, so steht es jedenfalls in den Büchern. Ich habe angefangen, daran zu zweifeln. Fünfzehnhundertfünf tagte der Reichstag in Köln, und der König entschied. Landshut ging an Albrecht nach München. Für die beiden anderen, Ottheinrich und Philipp, schuf man ein kleines neues Land an der Donau, mit der Hauptstadt Neuburg. Aber in den Wintertagen nach Georgs Tod, als noch niemand wusste, wer gewinnen würde, hat jemand eine Kiste aus der Stadt gebracht. Was in ihr war, steht in zwei Listen in meiner Mappe. Ihr Schloss stellt ihr dort ein, wo die Bürger dieser Stadt seit Jahrhunderten ihren Rat halten. Nicht oben auf der Burg, sondern unten in der Altstadt."),
 "V_RESIDENZ":("seidl","Hier Seidl. Gute Arbeit, der Brief ist eine Fälschung. Ich glaube, ich weiß auch, wozu: Wer alte Stücke verkaufen will, braucht eine Herkunft. Ein Brief aus der Herzogsresidenz macht aus einer alten Kiste einen Schatz, den ein Sammler teuer bezahlt. Jetzt die entscheidende Frage: Wer kam am Abend an die Archivtür? Falkenrieds Haustechnik speichert jeden Zutritt in einem Ordner auf seinem Handy. Er hat ihn im Herbst gesperrt. Wo er sich öffnet, steht in Falkenrieds Notizen zur Fassade."),
 "V_TURM":("falkenried","Sie wollten hier einen Turm, höher als Sankt Martin. Das Geld reichte nicht. Manche wollen eben mehr, als ihnen zusteht."),
 "V_ZEUGIN":("rosa","Kurz vor neun hörte ich Schritte im Flur. Eine Frau im dunklen Mantel ging zum Archiv. Dann klickte die Archivtür. Ich dachte mir nichts dabei. Später hörte ich am Telefon, der Wagen sollte die Stadt durch das Tor verlassen, über dem die drei Helme hängen."),
 "ZEUGIN_KURZ":("rosa","Kurz vor neun hörte ich Schritte im Flur. Eine Frau im dunklen Mantel ging zum Archiv. Dann klickte die Archivtür. Ich dachte mir nichts dabei."),
 "V_MAIR":("mair","Ja, ich habe geschwiegen. Herr von Falkenried hat mir eine Kassette anvertraut und mich zur Verschwiegenheit verpflichtet. Am Tatabend habe ich mit der Verwahrstelle telefoniert, wegen der Übergabe an die Stadt. Die Datei habe ich geöffnet, weil ich prüfen wollte, was Frau Dorn ihm da vorgelegt hatte. Die Kassette und seine letzte Nachricht gebe ich nur Ermittlern."),
 "V_FINALE":("falkenried","Wenn ihr das hört, ist mir etwas zugestoßen. Dann hat jemand versucht, meine Geschichte zu Geld zu machen. Ich wollte nichts verkaufen. Im Kriegsjahr fünfzehnhundertvier hieß es, Elisabeths kleiner Sohn Georg sei gestorben, wie sein Zwillingsbruder Ruprecht. Es war gelogen. Derselbe treue Mann, der im Winter davor die Kiste aus der Stadt gebracht hatte, holte auch den Jungen heraus. Die Kiste war sein Erbe. Man hat Elisabeth das Land genommen, den Mann und das Leben. Aber ihren Sohn haben sie nicht bekommen. Ich glaube, dass ich von diesem Georg abstamme. Vielleicht irre ich mich. Aber das, was er mitnahm, gehört zurück nach Landshut. Das Schloss kennt nur einen Namen: den der Frau, der all das gehören sollte. Und gebt es niemandem, der sich nicht zeigt."),
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
