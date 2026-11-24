# DER LETZTE ERBE
## Ein Mord. Ein verschollenes Herzogserbe. 551 Jahre nach der Hochzeit.

**Konzept- und Spielleitungsdokumentation für einen weihnachtlichen Krimi-Stadtrundgang in Landshut**  
**Stand:** 24. November 2026  
**Fassung:** 2.0 – an die App angeglichen (Zweig `kuerzer-und-runder`, Überarbeitung vom 12.11.2026)  
**Zielgruppe:** Erwachsene · ein Team, jedes Mitglied mit eigenem Handy · ca. 120–150 Minuten  
**Spielort:** Landshuter Altstadt und Ringelstecherwiese  
**Format:** Stadtrundgang + Kriminalfall + Smartphone-Ermittlungsspiel („Falkenrieds Handy“)

> **Maßgeblich ist die App** (`src/index.html`). Dieses Dokument beschreibt, was die App tatsächlich zeigt und verlangt. Wo App und Dokument auseinanderlaufen, gilt die App; das Dokument wird nachgezogen. Technische Details, Deploy und offene Punkte stehen in `docs/STAND_1475.md`.

> **KENNZEICHNUNG:** Die Landshuter Hochzeit 1475, die Hochzeitsrechnung, Ludwig der Reiche, Georg der Reiche, Hedwig von Polen, Elisabeth, Albrecht IV., Georgs Tod 1503, der Landshuter Erbfolgekrieg und die realen Spielorte sind historisch. **Maximilian von Falkenried, alle Gegenwartsfiguren, der Mord, die Kiste von 1503 mit den drei Hochzeitsgaben, das Überleben von Elisabeths Sohn Georg, jede Abstammung davon, die Sage vom Ritter am Ländtor und alle Ermittlungsbeweise sind erfunden.** Auch die Zeile „Beglichen durch Herzog Ludwig, den Vater des Bräutigams“ in Falkenrieds Abschrift der Rechnung ist eine dramaturgische Ergänzung, keine Reproduktion eines Originals.

---

# 1. Die Idee auf einer Seite

Am Abend des **19. Dezember 2026** wird der Kunstsammler **Maximilian von Falkenried** nach einem Adventsessen in seinem Archiv erschlagen. Fünf Menschen waren im Haus. Falkenried wollte an diesem Abend verkünden, dass er drei verschollene Hochzeitsgaben von 1475 gefunden hat und sie der Stadt Landshut zurückgibt.

Kommissarin **Martina Seidl** von der Kripo Landshut spielt den Spielern ein Abbild von Falkenrieds Handy auf ihre eigenen Handys. Falkenried ahnte, dass jemand in seinen Papieren liest, und hat Notizbuch, Archiv, Mappe und Haustechnik mit Dingen gesichert, die man nur draußen in der Stadt sieht: der Höhe des Martinsturms, den Herzögen an der Fassade des Landschaftshauses, der Jahreszahl am Denkmal, dem Wappen über der Rathausuhr. Wer seinen Weg durch die Stadt geht, kommt an sein Wissen.

Unterwegs meldet sich eine verfremdete Stimme als **„Unbekannt“**, gibt sich als Helferin aus und lenkt den Verdacht auf Notar Mair und Kunsthändlerin Clara Weiß. In Wahrheit ist es die Täterin, **Dr. Helena Dorn**: Sie hat die Stücke längst an einen Käufer versprochen, die Kassette aber nicht gefunden, und braucht die Spieler, um an sie zu kommen.

Am Ende stehen die Spieler auf der Ringelstecherwiese vor Seidl und Notar Mair. Sie müssen die Täterin mit Beweisen überführen, erst dann bekommen sie Falkenrieds Kassette. Sie öffnet sich nur mit dem Namen der Frau, der all das gehören sollte: **Elisabeth**. Dann wird Dorn in einer Falle festgenommen.

**Ton:** atmosphärisch, erwachsen, ruhig erzählt; keine Gewaltdarstellung. **Design der App:** bewusst dunkel (helle Varianten wurden verworfen).

---

# 2. Spielprofil

| Merkmal | Umsetzung in der App |
|---|---|
| Name | **Der letzte Erbe – Akte 1475**, App-Titel „Falkenrieds Handy“ |
| Genre | Historischer Weihnachtskrimi / Stadtrundgang |
| Spieler | Ein Team; jedes Mitglied öffnet die App auf dem eigenen Handy. Alle Handys mit derselben Adresse (`?team=name`) teilen den Spielstand. |
| Spielleitung | Ist dabei; eigener Spielleitungsmodus (Kapitel 10.4) |
| Stationen | 8, dazu ein kurzer Zwischenstopp an der Herzogswand |
| Dauer | ca. 120–150 Minuten mit Laufwegen |
| Fortbewegung | Zu Fuß, alles im öffentlichen Außenraum, kein Innenzutritt |
| Technik | Web-App (PWA, installierbar, offlinefähig), GPS, Audio mit Mitlesetext, gemeinsamer Spielstand über Supabase |
| Ausstattung | Handy mit Akku und Internet, Standortfreigabe; optional Powerbank, Kopfhörer, echte Kassette mit Zahlenschloss |
| Hinweise | Pro Station drei Stufen in der App, dazu zwei Ortstipps für unterwegs |
| Finale | Anklage mit vier Beweisfragen, dann Namensschloss der Kassette, dann Festnahme |

**Designprinzipien:**

1. **Jeder Weg hat eine Begründung.** Der nächste Ort ergibt sich aus einer Spur (Tagebuch, Memo, Zeugin, Abholauftrag), nicht aus einer Liste. Die Auftragskarte zeigt nur Spur und „Wozu“, nicht den Ort.
2. **Vor Ort lösen.** Fast jede Station braucht einen Blick auf das echte Bauwerk.
3. **Der Schluss verlangt Beweise.** Ein Name allein reicht nicht; Seidl fragt die Beweiskette ab.
4. **Gemeinsam rätseln, nicht wild raten.** Pro Rätselschritt hat jedes Handy einen Versuch. Erst wenn alle einmal danebenlagen, hat wieder jeder einen.

---

# 3. Historisches Fundament

## 3.1 Was belegt ist und im Spiel vorkommt

- **14. November 1475:** Hochzeit von Georg dem Reichen (20) und Hedwig (18), Tochter des Königs von Polen, in St. Martin. Bezahlt hat Georgs Vater, Herzog Ludwig IX. der Reiche [Q1].
- **Hochzeitsrechnung:** überlieferte Mengen, u. a. 323 Ochsen, 285 Schweine, 1.133 ungarische Schafe, 11.500 Gänse, 40.000 Hühner, 194.345 Eier [Q1, Q2].
- **St. Martin:** Turm ca. 130 m, höchster Backsteinturm der Welt [Q13].
- **Landschaftshaus, Altstadt 28:** Fassadenbemalung von 1599 mit 30 Wittelsbachern in drei Reihen zu je zehn. Im Spiel gebraucht: Ludwig der Kelheimer (oben 2, gründete 1204 Landshut), Ludwig der Bayer (oben 4, einzige sitzende Figur, 1328 Kaiser), Heinrich der Reiche (Mitte 6), Ludwig IX. der Reiche (Mitte 9), Georg der Reiche (Mitte 10, polnischer Adler zu seinen Füßen), Albrecht IV. der Weise (unten 1) [Q11, Q12].
- **Denkmal Ludwigs des Reichen** am Dreifaltigkeitsplatz, errichtet 1858; auf der Rückseite **MDCCCLVIII** [Q3, Q4].
- **Erbfolge:** Georg hatte keinen überlebenden Sohn und setzte gegen die Hausverträge seine Tochter Elisabeth als Erbin ein. Nach seinem Tod im Dezember 1503 zog sein Vetter Albrecht IV. von München in den Landshuter Erbfolgekrieg und gewann. Elisabeth starb 1504 [Q5].
- **Stadtresidenz:** Baubeginn 1536 unter Ludwig X. Ein Brief von 1503, der sie nennt, ist unmöglich [Q6].
- **Rathaus:** Über der Uhr das Stadtwappen mit drei roten Helmen auf weißem Schild (vor Ort bestätigt) [Q15].
- **Heiliggeistkirche:** Baubeginn 1407 unter Heinrich dem Reichen; der Turm sollte höher werden als der von St. Martin, das Geld reichte nicht [Q14].
- **Ländtor:** Wappen mit den drei Helmen über dem Torbogen [Q10].
- **Ringelstecherwiese:** Christkindlmarkt 2026 vom 19. November bis 23. Dezember [Q8].

## 3.2 Erfunden

Falkenried und alle Figuren, der Mord, die Kiste, die im Winter 1503 aus der Stadt gebracht wurde, die drei Hochzeitsgaben darin (Rubinbrosche, zehn goldene Taler, Familiensiegel), die beiden Inventarlisten, das Überleben von Elisabeths kleinem Sohn Georg, jede Abstammung davon, die Sage vom Ritter am Ländtor, alle Briefe, Protokolle und Kameraaufnahmen. Die App zeigt das am Ende unter **„Was war echt?“**.

**Rechtlicher Realismus:** Eine Abstammung von Herzögen begründet keinen Anspruch auf irgendein Vermögen. Falkenried will deshalb nichts behalten, sondern alles der Stadt zurückgeben.

---

# 4. Hintergrund für die Spielleitung (Spoiler)

## 4.1 Drei Zeitebenen

**1475, die Hochzeit.** Georg heiratet Hedwig, Ludwig bezahlt. Unter den Hochzeitsgaben (Liste 1475, acht Stücke) sind eine Rubinbrosche, zehn goldene Taler und ein Familiensiegel mit dem W der Wittelsbacher.

**Winter 1503/04, das Erbe.** Georg stirbt, Elisabeth soll erben, Albrecht zieht in den Krieg. *Fiktion:* In den Wintertagen nach Georgs Tod bringt ein treuer Mann eine Kiste mit den drei Stücken aus der Stadt. In der Liste von 1503 (nach Räumen sortiert, fünf Einträge) fehlen sie. 1504 heißt es, Elisabeths kleiner Sohn Georg sei gestorben. Falkenried glaubt: Er wurde heimlich in Sicherheit gebracht, und er selbst stammt von ihm ab.

**Herbst/Advent 2026, Fund und Mord.** Falkenried findet am 2. November in Kirchenbüchern in Neuburg an der Donau einen durchgestrichenen Kindernamen von 1504 und danach die Kiste mit den drei Stücken. Er legt sie in eine Kassette und vertraut sie **Notar Benedikt Mair** an. Ende November merkt er, dass jemand an seinem Schreibtisch war. Am Tatabend will er nach dem Dessert verkünden, dass alles an die Stadt geht.

## 4.2 Die Wahrheit des Falls

**Täterin ist Dr. Helena Dorn**, Historikerin, betreut seit drei Jahren Falkenrieds Archiv und leitete 2025 die Digitalisierung einschließlich der Zutrittstechnik.

- Sie fälscht am **18.12. um 23:14** einen Herkunftsbrief „1503“ (Datei `LETTER-1503-B`, Kennung `HDORN`), damit die Stücke für einen Käufer echt und wertvoll aussehen.
- Um **19:30** am Tatabend geht der verschlüsselte Abholauftrag raus: drei Stücke, Anbieterin **HD**, Käufer **CW-04**, Übergabe Ringelstecherwiese. Clara Weiß vermittelt.
- Um **20:30** verabschiedet sie sich im Flur („Kopfschmerzen“), zieht den Mantel an, fährt aber nicht. Ihr Wagen bleibt in der Einfahrt.
- Um **20:48** öffnet sie mit der gestohlenen Karte **R7** von Restaurator Jonas Feld die Archivtür, erschlägt Falkenried mit einer Messing-Leselampe (Handschuhe) und nimmt die Liste von 1475 (Seite 5 seiner Abschriften) mit. Die Kassette findet sie nicht.
- Um **21:02** geht sie im Mantel mit Kapuze an der Seitentür vorbei und fährt weg.
- Um **21:25** findet Tobias seinen Onkel.

**Warum sie die Spieler braucht:** Mair gibt die Kassette nur an Ermittler heraus. Als „Unbekannt“ schickt Dorn die Spieler deshalb weiter, lenkt auf Mair und Clara und will die Kassette am Ende auf der Wiese abholen.

## 4.3 Zeitstrahl des Tatabends (Spielkanon)

| Zeit | Ereignis | Quelle im Spiel |
|---|---|---|
| 18.12., 23:14 | `LETTER-1503-B` erstellt unter HDORN | Dateiprotokoll (Station 5) |
| 19.12., 10:02 | dieselbe Datei geöffnet unter BMAIR | Dateiprotokoll |
| 19:00 | Gäste kommen | Vorspann, Tagebuch |
| 19:30 | Abholauftrag HD → CW-04 verschickt | Postfach (Station 7) |
| 20:30 | Dorn verabschiedet sich im Flur | Protokoll Haustechnik |
| 20:30–20:33 | Dorns Wagen steht, niemand steigt ein | Kamera Einfahrt |
| 20:34–20:52 | Mair telefoniert am Hoftor, 18 Minuten, außerhalb des Haus-WLANs | Kamera Einfahrt, Protokoll |
| 20:44–20:58 | Tobias raucht auf der Terrasse | Kamera Terrasse |
| 20:44–20:52 | Claras Platz am Tisch leer (Seidentuch über der Lehne) | Kamera Terrasse, Zoom durch die Glastür |
| 20:44–20:50 | Clara telefoniert im Flur mit CW-04 | Kamera Flurfenster, Handyauswertung |
| 20:48 | Archivtür geöffnet mit Karte R7 (zunächst geschwärzt) | Zutrittsprotokoll |
| 21:02 | Frau im Mantel mit Kapuze an der Seitentür, Dorns Wagen fährt los | Kamera Einfahrt |
| 21:06 | Taxi, Clara steigt ein, zieht im Gehen den Mantel an | Kamera Einfahrt |
| 21:25 | Tobias findet Falkenried im Archiv | Protokoll, Vorspann |

## 4.4 Falsche Fährten und ihre Auflösung

| Person | Was verdächtig wirkt | Auflösung |
|---|---|---|
| **Tobias** | Schulden, lauter Streit, galt als möglicher Erbe; Tagebuch: „hat wieder nach Geld gefragt. Nein.“ | Terrassenkamera 20:44–20:58. Seine Aussage stimmt. |
| **Mair** | „Kurz telefoniert“ (18 Minuten), Verwahrvermerk geschwärzt, hatte die Brief-Datei offen, „Unbekannt“ verdächtigt ihn | Treuhänder der Kassette, Schweigepflicht. Telefonat am Hoftor belegt. Halb wahr. |
| **Clara** | Lügt über den Tisch, Preisnotiz „CW: 40.000?“, Käuferkontakt CW-04 | Telefonierte 20:44–20:50 im Flur mit dem Käufer. Sie vermittelt, sie mordet nicht. |
| **Jonas Feld (R7)** | Seine Karte öffnete die Archivtür | War in Regensburg (drei Kollegen), Karte seit einer Woche verschwunden, zuletzt im Archiv. |

## 4.5 Das zweite Geheimnis

Die Stücke sind in der Spielwelt **echt**, der Brief von 1503 ist **falsch**. Ein gefälschtes Dokument macht nicht die ganze Geschichte falsch. Falkenrieds eigentliches Geheimnis, das Überleben des kleinen Georg und seine eigene Abstammung, erfahren die Spieler erst im Finale von Mair. Der Stammbaum lässt dafür eine sichtbare Lücke („?“) zwischen Georg und Falkenried.

---

# 5. Figuren

Alle Figuren sind erfunden. Porträts, Kurzprofile und Vernehmungen stehen in der App unter „Verdächtige“ bzw. „Wer ist wer“.

| Person | Rolle | Akte / Behauptung | Wahrheit |
|---|---|---|---|
| **Maximilian von Falkenried**, 62 | Opfer, Kunstsammler, Gastgeber | Am 19.12. um 21:25 tot im Archiv | Fand die Stücke, wollte sie der Stadt geben |
| **Dr. Helena Dorn**, 47 | Historikerin, betreute das Archiv | „Um halb neun gegangen, Kopfschmerzen. Mantel an und ins Hotel.“ | **Täterin**, Fälscherin, Anbieterin HD, Stimme „Unbekannt“ |
| **Benedikt Mair**, 55 | Notar, kennt das Testament | „Kurz telefoniert, draußen. Mehr nicht.“ | 18 Minuten am Hoftor; verwahrt die Kassette |
| **Tobias von Falkenried**, 31 | Neffe, Schulden | „Ja, wir haben gestritten. Laut. Danach rauchen.“ | Stimmt |
| **Clara Weiß**, 43 | Kunsthändlerin | „Den ganzen Abend bei den anderen am Tisch.“ | Gelogen; telefonierte mit Käufer CW-04 |
| **Jonas Feld**, 39 | Externer Restaurator, Karte R7 | „Die Karte ist mir vor einer Woche abhandengekommen.“ | War in Regensburg |
| **Rosa Brandl**, 58 | Haushälterin, Zeugin | Hängte die Mäntel an die Garderobe | Sah Clara telefonieren und eine Frau im Mantel zum Archiv gehen |
| **Martina Seidl**, 52 | Kriminalhauptkommissarin | Führt per Sprachnachricht und Lagebesprechung durchs Spiel | – |
| **„Unbekannt“** | Verfremdete Stimme am Telefon, Chat | Scheint zu helfen | Dr. Dorn; verrät sich durch Täterwissen (20:48, R7) |

**Vernehmungen** (freiwillig, Audio mit Text, „✓ angehört“ nach kompletter Aufnahme): Helena, Mair, Tobias, Clara, dazu das Telefonat mit Feld. Gebraucht werden sie an der Heiliggeistkirche und beim Streichen am Ländtor.

---

# 6. Spielstart

Ablauf in der App:

1. **Push-Nachricht** auf dem Sperrbildschirm.
2. **Vorspann** (Bilder mit Sprecher, `CUT_V1`–`CUT_V4`): „Landshut. Samstag, 19. Dezember. 19 Uhr.“ → Adventsessen mit vier Gästen → „20:48 Uhr. Jemand öffnet die Tür zu seinem Archiv.“ → „21:25 Uhr. Sein Neffe findet ihn.“
3. **Sprachnachricht Seidl (`V_START`):** Fünf Menschen im Haus, mindestens einer lügt. Falkenried hat seine Sachen gesperrt und die Schlüssel in der Stadt versteckt. Code fürs Handy: **1475**. „Schaut euch kurz den Tatort an, dann treffen wir uns am Turm von Sankt Martin.“
4. **Tatort mit fünf Spuren** (antippen auf dem Tatortfoto):
   - T1 Tatwaffe: schwere Messing-Leselampe, abgewischt, Täter trug wohl Handschuhe.
   - T2 Dunkler Wollfaden am Stuhl, wie von einem Mantel.
   - T3 Seite 5 der Abschriften fehlt: die Liste von 1475.
   - T4 Kalenderblatt: „St. Martin – die Rechnung.“
   - T5 Kartenleser: Jeder Zutritt wird gespeichert, Daten in der gesperrten App „Haustechnik“.
5. **Team eintragen** (Namen für Urkunde und Zeitungsartikel).
6. **Sperrbildschirm**, Code **1475**.
7. **„Wer ist wer“** mit allen Personen; Vernehmungen können hier schon angehört werden.
8. Unterwegs zu St. Martin. Vor Ort „Wir sind da“, dann der **Anruf von Unbekannt (`CALL_01`):** „Falkenried hat etwas gefunden, das fünfhundert Jahre verschwunden war. Deshalb ist er tot. … Sein Notizbuch öffnet sich mit der Höhe des Turms über Ihnen.“

---

# 7. Stationen- und Routenübersicht

| Nr. | Ort | Koordinaten | Rätsel | Lösung |
|---|---|---|---|---|
| 1 | St. Martin, vor dem Turm | 48.534237, 12.151014 | Zahlenschloss Notizbuch: Turmhöhe schätzen (höher/tiefer) | **130** (±4 m) |
| 2 | Landschaftshaus, Altstadt 28 | 48.533888, 12.150226 | 4 Fotos an der Herzogswand finden, dann Rechnung: Vater des Bräutigams antippen | O2, O4, M6, M10; dann **M9 Ludwig der Reiche** |
| 3 | Denkmal Ludwigs des Reichen, Dreifaltigkeitsplatz | 48.532417, 12.149794 | Archiv-Passwort: Jahr in römischen Ziffern auf dem Rücken | **1858** (auch MDCCCLVIII) |
| ↪ | Zwischenstopp Herzogswand | – | Albrecht den Weisen finden | **U1** |
| 4 | Rathaus, Altstadt 315 | 48.536228, 12.152024 | Wappenschloss (3 Räder) + Listenvergleich 1475/1503 | **3 · Helm · Rot**; fehlend **2, 5, 7** |
| 5 | Stadtresidenz, gegenüber | 48.536103, 12.151237 | Brief „1503“: welche Zeile kann nicht stimmen? | „lagert sicher in der **Stadtresidenz** des Herzogs“ |
| 6 | Heiliggeistkirche | 48.538667, 12.152562 | a) Rundgang um die Kirche b) 6 Kameraclips + 4 Aussagen c) Frage zu Karte R7 | Tobias stimmt, Mair halb wahr, Clara gelogen, Helena gelogen; R7 „nur seine Karte benutzt“ |
| 7 | Ländtor | 48.535305, 12.149236 | Kuriernachricht `HIOVSBUN`, Schlüssel = Glockenschläge der Sage (7); dann Verdächtige streichen | **ABHOLUNG**; übrig bleibt Dorn |
| 8 | Ringelstecherwiese | 48.532814, 12.146553 | Anklage (4 Fragen), dann Namensschloss | **Elisabeth** (Falle: Hedwig) |

**Unterwegs:** Die Auftragskarte zeigt die Spur und wozu sie dient. „📍 Ort zeigen“ wird erst nach 5 Minuten frei (Station 2: nach 3 Minuten), dazu zwei Ortstipps vom vagen zum deutlichen. „Wir sind da“ klappt erst im Umkreis von etwa 50 m (Ringelstecherwiese: 200 m).

**Laufwege/Puffer:** etwa 20–30 Minuten. St. Martin, Landschaftshaus und Denkmal liegen dicht beieinander; der Zwischenstopp führt zurück zur Herzogswand, dann nach Norden zu Rathaus/Residenz und Heiliggeist, zurück nach Westen zum Ländtor und zur Wiese.

---

# 8. Stationsdrehbuch

## STATION 1 – ST. MARTIN: Die Höhe des Turms

**Spur:** Seidl: „Wir treffen uns am Turm von Sankt Martin.“  
**Vor Ort:** Anruf `CALL_01`, danach Auftrag „Notizbuch öffnen“.

**Zettel am Notizbuch (Handschrift Falkenried):**
> „Jemand liest meine Papiere. Passwörter kann man stehlen, diese Stadt nicht. Darum ist alles Wichtige mit dem verschlossen, was man nur draußen sehen kann. Mein Buch öffnet sich mit der Höhe dieses Turms in Metern. Schätzt: Das Schloss sagt euch, ob ihr zu tief oder zu hoch liegt.“

**Aktion:** Zahl eingeben. Antworten: „Viel zu tief“ (mehr als 40 m darunter), „Zu tief“, „Zu hoch“, „Viel zu hoch“. Richtig ist alles im Bereich **126–134**: „Klick. 130 Meter, der höchste Backsteinturm der Welt.“ Die Zahl der Versuche wird angezeigt.

**Freischaltung:** Tagebuch (Notizen-App, Beweis `E01` Hochzeitsrechnung). Es schlägt beim ersten Mal die Seite vom 17.12. auf („Alles beginnt mit einer Hochzeit“, Georg ∞ Hedwig). Danach Lagebesprechung Seidl (`B_1`): Im November hat Falkenried etwas gefunden, kurz danach war jemand an seinem Schreibtisch; traut der Stimme nicht. Auftrag: „Auf der Hochzeitsrechnung ist ein Name verwischt. Wer hat sie beglichen?“

**Tagebuchseiten** (Wochentage stimmen für 2026):

| Datum | Inhalt |
|---|---|
| Mo 2.11. | Neuburg an der Donau, Kirchenbücher, Eintrag von 1504 mit durchgestrichenem Kindernamen. „Bester Tag meines Lebens.“ |
| Sa 28.11. | Jemand war an meinem Schreibtisch, eine Datei im Archivprogramm war geöffnet. |
| Do 10.12. | Foto der ganzen Herzogswand, eingeklebt |
| Sa 12.12. | Tobias hat wieder nach Geld gefragt. „Nein.“ |
| Do 17.12. | Georg und Hedwig, Hochzeit am 14.11.1475 in St. Martin (Startseite) |
| Fr 18.12. | Abschrift der Hochzeitsrechnung; „Beglichen durch Herzog L▒▒▒▒▒, den Vater des Bräutigams.“ Hinweis auf Altstadt 28 |
| Sa 19.12., morgens | „Heute Abend sage ich es allen … Es gehört dieser Stadt. Und wenn mir etwas zustößt: Notar Mair weiß, was zu tun ist.“ |

**Hinweise:** Stockwerk ≈ 3 m → höchster Backsteinturm der Welt, deutlich über 100 m → 130 m.

---

## STATION 2 – LANDSCHAFTSHAUS: Die Herzogswand

**Spur:** Tagebuch vom 18.12.: „Beglichen durch Herzog L…, den Vater des Bräutigams. Wer es war, steht an einer Wand in der Altstadt, Hausnummer 28: drei Mann hoch, zehn Mann breit.“  
**Vor Ort:** „Dreißig Herzöge, eine Familie. Falkenried hat vier von ihnen fotografiert. Findet jeden an der Wand, dann klärt sich die Rechnung.“

**Aktion 1: Vier Fotos.** Nacheinander erscheint je ein Detailfoto mit Beschreibung; die Spieler tippen im Raster (3 Reihen × 10 Plätze) den Platz an. Jede Figur ist ein Kapitel:

| Kapitel | Figur | Platz | Erkennungsmerkmal | Text nach dem Fund |
|---|---|---|---|---|
| Die Stadt | Ludwig der Kelheimer, „Der Gründer“ | O2 | Hermelinkragen über der Rüstung, roter Mantel | Gründete 1204 Landshut und die Burg |
| Die Macht | Ludwig der Bayer, „Der Kaiser“ | O4 | Einziger, der sitzt; Reichsapfel | 1328 in Rom zum Kaiser gekrönt |
| Das Geld | Heinrich der Reiche, „Der Großvater“ | M6 | Goldener Umhang, Schwert quer vor dem Bauch | Füllte die Schatzkammer; unter ihm begann 1407 der Bau der Heiliggeistkirche |
| Die Hochzeit | Georg der Reiche, „Der Bräutigam“ | M10 | Zwei Wappen zu den Füßen, eines mit weißem Adler unter Krone | Heiratete 1475 Hedwig; die Rechnung beglich ein anderer |

**Aktion 2: Die Rechnung.** „Beglichen durch Herzog L▒▒▒▒▒, den Vater des Bräutigams.“ Der Vater steht direkt links neben seinem Sohn. **Lösung: M9, Ludwig der Reiche.** Falle M6: „Das ist der Großvater.“

**Freischaltung:** „Beglichen durch Herzog Ludwig … BEGLICHEN.“ Im Tagebuch wird der Name lesbar. Beweis `E03` mit Randnotiz: *„Ludwig steht noch einmal in dieser Stadt, aus Bronze, dort, wo die Dreifaltigkeit wacht.“* Danach Nachricht von Unbekannt (`N01`): „Ihr habt den Vater gefunden. Schön. Fragt euch lieber, wo Notar Mair am Tatabend war. Achtzehn Minuten sind eine lange Zeit für ein Telefonat.“

**Hinweise:** Wand wie ein Buch lesen → Plätze der vier Figuren → Vater steht auf Mitte 9.

---

## STATION 3 – DENKMAL LUDWIGS DES REICHEN: Das Jahr auf dem Rücken

**Spur:** Falkenrieds Randnotiz zu Ludwig (siehe oben).  
**Vor Ort:** „Das Passwort ist das Jahr, in dem dieses Denkmal aufgestellt wurde. Falkenrieds Notiz: ‚Es steht auf seinem Rücken. In der Schrift der Römer.‘“

**Aktion:** Passwort **1858** (MDCCCLVIII wird auch angenommen; andere römische Zahlen: „Schreibt die Jahreszahl in unseren Ziffern“).

**Freischaltung:** Archiv. Memo **`V_ERBE` „Die Familie“** (Falkenried, aufgenommen am 16.10.2026):
> „Wenn ihr das hört, steht ihr vor Ludwig dem Reichen. … 1475 heiratete sein Sohn Georg in Sankt Martin die polnische Königstochter Hedwig. Ludwig bezahlte alles. Doch Georgs Söhne starben früh. Es blieben nur Töchter, und das wurde zum Problem. Wer dieses Problem hatte, steht ebenfalls an der Herzogswand, ganz unten links. Geht zurück und sucht ihn. Dann erzähle ich weiter.“

**Hinweise:** Um den Sockel gehen → Wert der römischen Ziffern → 1858.

---

## ZWISCHENSTOPP – HERZOGSWAND: Der Gegenspieler

**Spur:** „Die bemalte Wand mit den Herzögen, an der ihr schon wart. … Gesucht ist der, der unten links steht.“  
**Aktion:** Foto Albrechts („Langer roter Mantel mit Pelzkragen, eine Urkunde in der Hand“), Platz antippen: **U1, Albrecht der Weise**, Herzog in München, Georgs Vetter und größter Gegenspieler.

**Freischaltung:** Memo **`V_ALBRECHT` „Der Erbfolgekrieg“**, darunter der Stammbaum, neue Personen leuchten auf:
> „Georg und Hedwig bekamen eine Tochter: Elisabeth. … Georg setzte trotzdem Elisabeth als Erbin ein. Doch in München saß sein Vetter Albrecht. Als Georg im Dezember 1503 starb, zog Albrecht gegen Elisabeth in den Krieg, und er gewann. Elisabeth starb 1504, mitten im Krieg. Ihr kleiner Sohn Georg, heißt es, im selben Jahr. Ich habe angefangen, daran zu zweifeln. In den Wintertagen nach Georgs Tod brachte jemand eine Kiste aus der Stadt. Was darin war, steht in zwei Listen in meiner Mappe. Ihr Schloss hat drei Räder. Was ihr einstellen müsst, hängt dort, wo die Bürger dieser Stadt seit Jahrhunderten ihren Rat halten.“

**Stammbaum** (App „Stammbaum“, Personen erscheinen im Spielverlauf): Heinrich XVI. → Ludwig IX. (vor der Herzogswand als „L. ?“) → Georg ∞ Hedwig (Hochzeit 1475) → Elisabeth (mittig, „Testament: Erbin“) → ihr Sohn Georg (1500–„1504“) → **?** → Maximilian von Falkenried – Tobias. Albrecht IV. steht als Vetter auf Georgs Höhe, eine rote Kriegslinie führt zu Elisabeth.

---

## STATION 4 – RATHAUS: Wappenschloss und zwei Listen

**Spur:** Falkenrieds Sprachmemo vom 16. Oktober (Ende von `V_ALBRECHT`).  
**Vor Ort:** „Die Mappe hat ein Wappenschloss mit drei Rädern. Die Einstellung hängt über der Rathausuhr.“

**Aktion 1: Wappenschloss.** Drei Räder: Anzahl (1–6), Zeichen (Löwe, Adler, Helm, Raute, Schlüssel, Krone), Farbe des Zeichens (Rot, Blau, Silber, Gold, Grün, Schwarz). **Lösung: 3 · Helm · Rot** (drei rote Helme auf weißem Schild, vor Ort bestätigt).

**Aktion 2: Was fehlt 1503?** Zwei erfundene Inventare. Die Spieler markieren in der Liste von 1475 genau drei Stücke, die in der Liste von 1503 fehlen.

| Nr. | Liste 1475 | in der Liste 1503 (nach Räumen, anders formuliert) |
|---|---|---|
| 1 | Goldener Hochzeitsbecher | Silberkammer: „Becher, golden, von der Hochzeit“ |
| **2** | **Rubinbesetzte Brosche** | – |
| 3 | Zwölf silberne Löffel | Silberkammer: „Löffel, silbern, 12 Stück“ |
| 4 | Polnisches Brautkleid aus Brokat | Schlafgemach: „Brautkleid, Brokat, aus Polen“ |
| **5** | **Zehn goldene Taler** | – |
| 6 | Silberne Gürtelschnalle | Silberkammer: „Schnalle für den Gürtel, Silber“ (Falle: keine Brosche) |
| **7** | **Familiensiegel mit dem W der Wittelsbacher** | – |
| 8 | Reliquienkreuz aus Bergkristall | Kapelle: „Kreuz, Bergkristall, mit Reliquie“ |

**Freischaltung, Inhalt der Mappe:** Fundbericht Herbst 2026: *„Ich habe sie gefunden. Alle drei, in der Kiste von 1503. Sie sind in Sicherheit, bei jemandem, dem ich vertraue.“* Dazu Vermerk „Notariat Mair – Verwahrung“ (geschwärzt) und Bleistiftnotiz „CW: 40.000?“. Beweise `E05`, `E06`, `E07`. Seidl: „Da ist das Motiv: drei Hochzeitsgaben, ein Vermögen wert. Die Stücke liegen offenbar bei Notar Mair. Und wer ist CW?“

Danach Nachricht von Unbekannt (`N02`) mit Anhang `Brief_1503.pdf`: „Ihr sucht die Kiste mit den fehlenden Erbstücken? Ich habe einen Brief aus dem Winter 1503. Er sagt, wo sie damals lag. Dreht euch um.“

**Hinweise:** Wappen zählen, Farbe beachten → Räder einstellen, jedes Stück einzeln abhaken → 3 · Helm · Rot; 2, 5, 7.

---

## STATION 5 – STADTRESIDENZ: Ein Brief aus der Zukunft

**Spur:** Anhang von Unbekannt, „Dreht euch um“.  
**Vor Ort:** „Ihr steht vor dem Gebäude, das der Brief nennt. Kann er wirklich von 1503 sein?“ Daneben ein Steckbrief: Bauherr Ludwig X., **Baubeginn 1536**, erster Palast im Stil der italienischen Renaissance nördlich der Alpen.

**Der Brief:**
> *Anno 1503, im Advent.*  
> Die versiegelte Kiste mit den Erbstücken  
> **lagert sicher in der Stadtresidenz des Herzogs,**  
> bewacht von zwei Männern seines Vertrauens.  
> Gott schütze das Erbe des Hauses.

**Aktion:** Die Zeile antippen, die es 1503 nicht geben kann. **Lösung:** „lagert sicher in der Stadtresidenz des Herzogs“.

**Freischaltung:** „Der Brief ist gefälscht.“ Dateiprotokoll: `LETTER-1503-B` erstellt unter **HDORN** am 18.12.2026, 23:14; geöffnet unter **BMAIR** am 19.12.2026, 10:02 (`E08`, `E09`). Dann Sprachnachricht **Seidl `V_RESIDENZ` „Die Archivtür“**: Wer alte Stücke teuer verkaufen will, braucht einen Herkunftsnachweis; erstellt hat ihn Dorn, geöffnet auch Mair; das beweist noch keinen Mord. „Das steht in Falkenrieds App Haustechnik. Sie öffnet sich nur an der Kirche, deren Bau unter Heinrich dem Reichen begann.“ Kurz danach `N03` von Unbekannt: „Ein falscher Brief? … Notar Mair hatte die Datei offen. Nur so als Hinweis.“

**Hinweise:** Zeile für Zeile prüfen → Baubeginn im Steckbrief → die Residenz-Zeile.

---

## STATION 6 – HEILIGGEISTKIRCHE: Der Tatabend

**Spur:** Seidl, Heinrichs Kirche (Fund M6 an der Herzogswand).  
**Vor Ort:** „Hier öffnet sich Falkenrieds App ‚Haustechnik‘. Lest seine Notiz dazu.“

**Aktion 1: Rundgang.** Die App „Haustechnik“ öffnet sich erst, wenn das Team einmal um die Kirche gegangen ist.
- Karte von oben (Leaflet + OpenStreetMap), Kirche als Fläche aus vier vor Ort gemessenen Ecken.
- Ein Ring folgt dem vor Ort eingezeichneten Laufweg (ca. 155 m) über den Platz, aufgeteilt in **12 Wegstücke, 11 nötig** (ein Aussetzer erlaubt), Fangradius 15 m, GPS-Genauigkeit ≤ 35 m.
- Eigener Standort als blauer Punkt mit Genauigkeitskreis und Blickrichtung (Kompass, ersatzweise Laufrichtung). Auf iOS gibt es dafür den Knopf „🧭 Blickrichtung zeigen“.
- Danach Memo **`V_TURM`**: „Sie wollten hier einen Turm, höher als Sankt Martin. Das Geld reichte nicht. Manche wollen eben mehr, als ihnen zusteht.“

**Aktion 2: Kameras und Aussagen.** Zwei Außenkameras, im Haus gibt es keine. Alle sechs Clips müssen angesehen werden, bevor die Aussagen geprüft werden können:

| Clip | Bild | Inhalt |
|---|---|---|
| Terrasse 20:44–20:58 | `k_terrasse.jpg` | Tobias raucht. Danach Zoom durch die Glastür: Claras Platz ist leer, ihr Seidentuch über der Lehne, 20:44–20:52 |
| Einfahrt 20:30–20:33 | `k_auto.jpg` | Dorns Wagen steht, niemand steigt ein |
| Einfahrt 20:34–20:52 | `k_mair.jpg` | Mair am Hoftor mit Handy, Dorns Wagen steht noch |
| Flurfenster 20:44–20:50 | `k_flur.jpg` | Clara im Flur am Telefon, sechs Minuten |
| Einfahrt 21:02 | `k_mantel.jpg` | Frau im langen dunklen Mantel mit Kapuze, kurz darauf fährt Dorns Wagen |
| Einfahrt 21:06 | `k_taxi.jpg` | Taxi, Einfahrt leer; Clara steigt ein und zieht im Gehen den Mantel an |

Darunter das Protokoll der Haustechnik (7 Zeilen, aufgeklappt) und ein Zeitstrahl, der pro Person Behauptung (gestrichelt) und Beleg (ausgefüllt) zeigt. Die Aussagen kommen einzeln, jeweils „Stimmt“ oder „Gelogen“:

| Reihenfolge | Aussage | Urteil | Begründung in der App |
|---|---|---|---|
| 1 | Tobias: „Ja, wir haben gestritten. Laut. Danach war ich rauchen, auf der Terrasse.“ | stimmt | Terrassenkamera 20:44–20:58 |
| 2 | Mair: „Ich habe kurz telefoniert, draußen. Mehr nicht.“ | halb wahr, **beide Antworten zählen** | Telefoniert hat er, aber 18 Minuten |
| 3 | Clara: „Ich saß den ganzen Abend bei den anderen am Tisch.“ | gelogen | Platz 20:44–20:52 leer, sie telefoniert im Flur |
| 4 | Helena: „Ich bin um halb neun gegangen. … Um kurz nach neun lag ich im Hotel.“ | gelogen | Wagen stand noch da, fuhr erst 21:02 |

Beweis `E10`.

**Aktion 3: Der Anruf (`CALL_06`).**
> „Ihr seid gut. Aber ihr schaut auf die Falschen. Clara Weiß, die Kunsthändlerin, lügt, glaubt mir. Und Notar Mair war achtzehn Minuten verschwunden. Um 20:48 ging die Archivtür auf, mit der Karte R7.“

Danach wird im Protokoll die Zeile frei: „Karte R7 (J. Feld, Restaurator) – Archivtür geöffnet um 20:48“. Beweis `E13` Täterwissen. Seidl: „20:48 und die Karte R7 waren in der Akte noch geschwärzt. Das weiß nur, wer an der Archivtür war.“ Sie stellt Jonas Feld vor (Telefonat anhörbar).

**Aktion 4: R7 einordnen.** „Was beweist der Eintrag ‚Karte R7, 20:48‘?“ → **„Es wurde nur seine Karte benutzt, von wem ist offen.“** Beweise `E12`, `E11`.

**Übergang:** Aussage der Zeugin **`V_ZEUGIN`** (Rosa Brandl):
> „Kurz vor neun stand Frau Weiß im Flur und telefonierte, ganz leise. Ich habe nur verstanden: Der Wagen soll die Stadt durch das Tor verlassen, über dem die drei Helme hängen. Und hinter ihr ging eine Frau zum Archiv, im langen dunklen Mantel, die Kapuze auf. Die Gäste hatten ihre Mäntel doch längst an der Garderobe. Dann klickte die Archivtür.“

Seidl danach: „Eine Frau im Mantel, mitten im Haus. Denkt an den Wollfaden am Stuhl. Und welcher Wagen sollte durch das Tor mit den drei Helmen?“

**Hinweise:** Karte offen lassen und ganz herumgehen → Wann fuhr Dorns Wagen, wessen Platz ist leer? → Feld war in Regensburg, also nur seine Karte.

---

## STATION 7 – LÄNDTOR: Die Sage vom Ritter

**Spur:** Zeugin: „Der Wagen soll die Stadt durch das Tor verlassen, über dem die drei Helme hängen.“  
**Vor Ort:** „Die Kripo hat eine verschlüsselte Nachricht vom Tatabend in Falkenrieds Postfach gelegt. Den Schlüssel verrät seine Aufnahme der Sage vom Ritter am Ländtor.“

**Postfach:** `HIOVSBUN`. Seidl: „Jeder Buchstabe wurde nach vorn geschoben. Falkenried hatte im selben Ordner eine Aufnahme: die Sage vom Ritter am Ländtor. Hört sie euch am Tor an.“

**Die Sage (erfunden, Falkenrieds Stimme, danach Glocken und Hufschläge):**
> „Am Ländtor erzählen sich die Leute eine alte Geschichte. Im Kriegsjahr 1504, in einer Nacht ohne Mond, schlug die Glocke von Sankt Martin die volle Stunde. Bei jedem Schlag kam ein Ritter näher, und beim letzten ritt er durch dieses Tor hinaus zur Isar. Unter seinem Mantel trug er etwas, das niemand sehen durfte. … Hört genau hin, und zählt mit.“

Es folgen **sieben Glockenschläge**.

**Aktion 1: Entschlüsseln.** Jeden Buchstaben sieben Stellen zurück (Buchstabentastatur in der App): `HIOVSBUN` → **ABHOLUNG**.

**Freischaltung, Abholauftrag (`E14`):**
> **Vertraulich · 19.12.2026 · 19:30 Uhr**  
> ABHOLUNG  
> Drei Stücke aus der Falkenried-Sammlung: Brosche, Taler, Siegel.  
> Anbieter: **HD** · Käufer: **CW-04**  
> Übergabe: **Ringelstecherwiese**, sobald die Ware greifbar ist.

Seidl: „Verschickt um 19:30, also vor der Tat. Mit dem Käufer CW-04 hat Clara Weiß von 20:44 bis 20:50 telefoniert (`E15`). Sie vermittelt nur. Aber wer ist HD?“

**Aktion 2: Streichen.** „Wer war um 20:48 nachweislich woanders?“ Jede Person zeigt ihr Alibi oder „Kein Alibi um 20:48“. Wer kein belegtes Alibi hat, lässt sich nicht streichen.

| Person | Alibi |
|---|---|
| Tobias | Terrassenkamera |
| Mair | Telefonat am Hoftor |
| Clara | Telefonat mit CW-04 im Flur |
| Feld | Regensburg |
| Dorn | keins, „Die Kamera zeigt: Sie war bis 21:02 im Haus.“ |

**Danach:** Lagebesprechung `B_7` „Es bleibt nur eine“: „Alle anderen waren um 20:48 woanders. Es bleibt Dr. Helena Dorn. HD. Für eine Festnahme reicht das nicht. Ich brauche Beweise, die halten.“ Dann Anruf **`CALL_07`**:
> „Ihr seid sehr nah dran. Notar Mair wartet auf der Ringelstecherwiese, er hat etwas für euch. Holt es dort ab, aber öffnet es nicht. Ich komme und nehme es euch ab.“

**Hinweise:** Glockenschläge zählen → sieben zurück, H wird A → ABHOLUNG.

---

## STATION 8 – RINGELSTECHERWIESE: Anklage, Kassette, Festnahme

**Spur:** Abholauftrag: „Übergabe: Ringelstecherwiese.“  
**Vor Ort:** „Seidl und Notar Mair warten hier. Mair gibt die Kassette erst heraus, wenn ihr beweist, wer es war.“ (Fangradius 200 m, große Wiese.)

**Teil A – Die Anklage gegen Dr. Helena Dorn.** Seidl stellt vier Fragen mit je drei Antworten. Falsche Antwort: „Das reicht nicht.“ plus Hinweis.

| Frage | Richtige Antwort |
|---|---|
| Wie beweist ihr, dass sie um 20:48 noch im Haus war? | Ihr Wagen verließ das Grundstück erst um 21:02. |
| Wer hat den Brief „1503“ gefälscht? | Sie selbst, die Datei wurde unter HDORN erstellt. |
| Warum hat sie es getan? | Sie wollte die drei Stücke an Käufer CW-04 verkaufen; der Abholauftrag nennt „HD“. |
| Wer war die Stimme am Telefon, und woran erkennt man das? | Dr. Dorn. Sie nannte 20:48 und die Karte R7, bevor beides bekannt war. |

**Teil B – Mairs Nachricht (`V_MAIR`).** Seidl nimmt die Anklage an, Mair übergibt die Kassette:
> „Ich habe geschwiegen, das tut mir leid. Er hat mir im Herbst diese Kassette anvertraut. Er war überzeugt, dass Elisabeths kleiner Sohn Georg den Krieg 1504 überlebt hat, heimlich in Sicherheit gebracht. Und dass er selbst von diesem Georg abstammt. Verkaufen wollte er nie etwas. Es sollte alles zurück nach Landshut. Die Kassette gehört jetzt euch. Das Schloss kennt nur einen Namen: den der Frau, der all das gehören sollte.“

Diese Nachricht enthält seit der Überarbeitung auch Falkenrieds Geheimnis; eine eigene Abschiedsnachricht Falkenrieds (`V_FINALE`) wird nicht mehr abgespielt.

**Teil C – Das Namensschloss (App „Tresor“).**
- **Elisabeth** (auch „Elisabeth von …“): richtig.
- **Hedwig:** „Sie war die Braut. Aber wem hatte Georg sein Erbe vermacht?“
- Sonst: „Das Schloss bleibt zu. Hört noch einmal, wem Georg sein Land vermacht hat.“

**Echte Kassette (optional):** Hat die Spielleitung einen Zahlencode hinterlegt, zeigt die App nach „Elisabeth“ einen Zettel in Falkenrieds Handschrift mit der Kombination. Das Team öffnet die echte Kassette und bestätigt „Die Kassette ist offen“. Ohne Code geht es direkt weiter.

**Teil D – Die Falle.** Seidl: „Sie kommt. Dr. Dorn ist schon auf dem Weg hierher. Sie glaubt, ihr bringt ihr die Kassette. Gebt sie Notar Mair zurück und versteckt euch hinter den Buden. Er übergibt sie ihr, und wir greifen zu. Auf frischer Tat.“ → „Verstecken“.

**Festnahme-Szene** (`CUT_F1`–`CUT_F4`, Bilder mit Sprecher):
1. „Ringelstecherwiese, [aktuelle Uhrzeit]. Eine Frau im dunklen Mantel betritt die Wiese. Sie sucht euch. Dann sieht sie Notar Mair mit der Kassette.“
2. „Sie geht auf ihn zu und streckt die Hand aus. ‚Geben Sie sie mir.‘“
3. Seidl: „Zugriff. Dr. Helena Dorn, Sie sind festgenommen wegen Mordes an Maximilian von Falkenried.“
4. „Eine Stunde später. In Dr. Dorns Wagen: ein Paar Lederhandschuhe mit Spuren vom Tatort. Und die Liste von 1475, die am Tatort fehlte.“

**Abschluss („Fall gelöst“):**
- Verdienstmedaille, Glückwünsche von Seidl als Sprachnachricht (`SEIDL_ENDE`).
- **Urkunde** mit Teamname und Namen, Datum, Ermittlungszeit und Zahl der benutzten Tipps.
- **Zeitungsartikel** „Landshuter Abendpost“: „Mordfall Falkenried aufgeklärt – Historikerin Dr. Helena Dorn auf der Ringelstecherwiese festgenommen“, mit Teamfoto (falls hochgeladen).
- **Auflösung:** Die Kassette enthält Rubinbrosche, zehn goldene Taler und das Familiensiegel, „das Erbe Elisabeths, 523 Jahre verborgen“. Die Stimme war Dorn. „Das Erbe geht zurück nach Landshut.“
- **„Was war echt?“** (siehe 3.1/3.2).

**Hinweise:** Wer war um 20:48 nicht woanders? → die vier Belege → „Wem hatte Georg sein Erbe vermacht? Nicht der Braut.“

---

# 9. Rätselübersicht mit Lösungen

| ID | Ort | Aufgabe | Lösung | Mechanik | Vor Ort nötig |
|---|---|---|---|---|---|
| R01 | St. Martin | Turmhöhe schätzen | 130 (126–134) | Schätzen mit höher/tiefer | ✅ |
| R02 | Landschaftshaus | Vier Fotos an der Wand finden | O2, O4, M6, M10 | Suchen, antippen | ✅ |
| R03 | Landschaftshaus | Wer hat die Rechnung beglichen? | M9, Ludwig der Reiche | Folgern | ✅ |
| R04 | Denkmal | Jahr auf dem Rücken | 1858 | Römische Zahl lesen | ✅ |
| R05 | Herzogswand | Albrecht finden | U1 | Suchen | ✅ |
| R06 | Rathaus | Wappenschloss | 3 · Helm · Rot | Vergleichen | ✅ |
| R07 | Rathaus | Was fehlt 1503? | 2, 5, 7 | Listen abgleichen | – |
| R08 | Stadtresidenz | Unmögliche Zeile im Brief | „lagert sicher in der Stadtresidenz“ | Quellenkritik | ✅ |
| R09 | Heiliggeist | Rundgang | 11 von 12 Wegstücken | Gehen (GPS) | ✅ |
| R10 | Heiliggeist | Vier Aussagen prüfen | Tobias stimmt, Mair beides, Clara und Helena gelogen | Vergleichen | – |
| R11 | Heiliggeist | Was beweist R7? | nur die Karte | Beweiswert | – |
| R12 | Ländtor | `HIOVSBUN` entschlüsseln | ABHOLUNG (7 zurück) | Hören, Chiffre | ✅ (Sage am Tor) |
| R13 | Ländtor | Verdächtige streichen | Tobias, Mair, Clara, Feld | Ausschluss | – |
| R14 | Wiese | Anklage, vier Fragen | siehe Station 8 | Beweiskette | – |
| R15 | Wiese | Namensschloss | Elisabeth (Falle: Hedwig) | Zuhören, Folgern | – |

**Konsistenzprüfung:** Elisabeth als Erbin kommt in `V_ALBRECHT` und im Stammbaum, die Falle Hedwig im Tagebuch und in `V_ERBE`. Die Türzeit 20:48 kennen die Spieler zwar aus dem Vorspann, die Karte R7 und den Eintrag im Protokoll aber erst nach dem Anruf; Seidl wertet beides als Täterwissen. Die Heiliggeistkirche wird über Heinrich (M6) eingeführt, das Ländtor über die Zeugin, die Wiese über den Abholauftrag.

---

# 10. App und Technik

## 10.1 Aufbau

- **Eine Datei:** `src/index.html` (HTML, CSS, JS), Bilder in `src/img/`, Audio in `src/audio/`, Service Worker `src/sw.js`.
- **Build:** `python3 build.py` erzeugt `dist/` (Manifest, Vollbild, kopiert Medien). Deploy über Netlify, **vor jedem Deploy Chris fragen**.
- **Handy-Oberfläche:** Sperrbildschirm, Homescreen mit Apps und Auftragskarte oben. Apps: Telefon (Sprachnachrichten, Anrufe), Nachrichten, Notizen (Tagebuch), Karte, Tresor, Haustechnik, Ermittlung, Fallakte (alle Beweise, Memos und Lagebesprechungen gesammelt), Verdächtige, Beweisboard, Stammbaum, Hinweise. Die Rätselfenster der Stationen (Eingeklebte Fotos, Archiv, Mappe, Brief, Postfach, Anklage) öffnen sich über die Auftragskarte.
- **Auftragskarte:** zeigt Spur, „Wozu“, Ort-Timer, Abstand zum Ziel und „Wir sind da“; die letzte Aufnahme lässt sich dort jederzeit nochmal anhören.
- **Neu-Zähler** an den Apps wie bei Messengern, pro Handy.

## 10.2 Audio

- Alle Sprachaufnahmen als MP3 mit Satz-Zeitmarken (`cues.json` → Konstante `CUES`) für den Mitlesetext. Wiedergabe mit 1,1-facher Geschwindigkeit.
- Aktuell kostenlose Microsoft-Neuralstimmen (`edge-tts`): Seidl AmalaNeural, Falkenried ConradNeural, Mair KillianNeural, Rosa de-AT-IngridNeural, Unbekannt KatjaNeural verfremdet. Endfassung mit ElevenLabs ganz zum Schluss.

| ID | Sprecher | Wann |
|---|---|---|
| `CUT_V1`–`V4` | Erzähler | Vorspann |
| `V_START` | Seidl | Start |
| `VERHOER_*` | Seidl + Person | freiwillig, „Wer ist wer“ / Verdächtige |
| `CALL_01` | Unbekannt | an St. Martin |
| `V_ERBE` | Falkenried | Station 3 gelöst |
| `V_ALBRECHT` | Falkenried | Zwischenstopp Albrecht |
| `V_RESIDENZ` | Seidl | Station 5 gelöst |
| `V_TURM` | Falkenried | Rundgang geschafft |
| `CALL_06` | Unbekannt | nach den vier Aussagen |
| `VERHOER_FELD` | Seidl + Feld | bei der Frage R7 |
| `V_ZEUGIN` / `ZEUGIN_KURZ` | Rosa | nach R7 / in der Haustechnik |
| `SAGE_LAENDTOR` | Falkenried + Glocken | Station 7 |
| `CALL_07` | Unbekannt | Station 7 gelöst |
| `V_MAIR` | Mair | nach der Anklage |
| `CUT_F1`–`F4` | Erzähler, Dorn, Seidl | Festnahme |
| `SEIDL_ENDE` | Seidl | Abschluss |

## 10.3 Gemeinsamer Spielstand

- Supabase-Projekt `der-letzte-erbe`, Tabelle `games`, Funktion `save_game`. Alle Handys mit derselben Team-Adresse teilen Fortschritt, Ereignisse und Versuchssperren. Ohne Verbindung läuft die App allein auf dem Gerät.
- Rätselauswahlen (z. B. Räder, markierte Listenstücke) gelten nur fürs eigene Handy; gelöst wird gemeinsam.
- Ein neues Rätsel startet erst, wenn alle aktiven Handys die vorherige Nachricht gesehen haben.
- **Versuche:** pro Rätselschritt ein Versuch je Handy; „Keine Versuche mehr … Jetzt kann es noch jemand anderes aus dem Team versuchen.“ Wenn alle einmal danebenlagen, hat wieder jeder einen.

## 10.4 Spielleitungsmodus

Fünfmal auf die Uhrzeit oben links tippen, PIN **1432**:
- Ereignisse auslösen (Anrufe, Nachrichten), Station vor/zurück, Spielstand anzeigen.
- Testmodus nur für dieses Handy: Standortprüfung aus, Ort-Timer aus, begrenzte Versuche aus, „Rundgang simulieren“.
- Team abschließen oder für neue Handys öffnen, Geräteliste.
- Teamfoto für den Zeitungsartikel aufnehmen.
- **Code der echten Kassette** hinterlegen (bleibt beim Zurücksetzen erhalten).
- Spieler einladen (Link teilen), Druckvorlagen öffnen (`docs/Druckvorlagen_Der_letzte_Erbe.pdf`), Handy sperren, Spielstand zurücksetzen.

## 10.5 Hinweise

Pro Station drei Stufen in der App „Hinweise“ (vom Anstoß bis zur Lösung, Texte siehe Kapitel 8). Die Zahl der benutzten Tipps steht auf der Urkunde. Für unterwegs zusätzlich zwei Ortstipps pro Station.

## 10.6 Barrierefreiheit und Ausfälle

Alle Audios mit Mitlesetext; Vernehmungen als Text lesbar. Ohne Standortfreigabe lässt sich „Wir sind da“ nicht bestätigen, dann hilft die Spielleitung mit dem Testmodus. Druckvorlagen als Ersatz für Kernbeweise.

---

# 11. Beweise in der Fallakte

| ID | Titel | Wann |
|---|---|---|
| T1–T5 | Tatortspuren (Lampe, Wollfaden, fehlende Seite, Kalenderblatt, Kartenleser) | Start |
| E01 | Hochzeitsrechnung 1475 | Station 1 |
| E03 | Beglichen: Ludwig der Reiche | Station 2 |
| E05 | Inventarvergleich | Station 4 |
| E06 | Verwahrvermerk Notariat Mair | Station 4 |
| E07 | Preisnotizen „CW“ | Station 4 |
| E08 | Brief „1503“ – gefälscht | Station 5 |
| E09 | Dateiprotokoll HDORN / BMAIR | Station 5 |
| E10 | Widersprüche der Aussagen | Station 6 |
| E13 | Täterwissen im Anruf | Station 6 |
| E12 | Karte R7 | Station 6 |
| E11 | Zeugin: Frau im Mantel an der Archivtür | Station 6 |
| E14 | Abholauftrag 19:30 | Station 7 |
| E15 | Handyauswertung Clara Weiß | Station 7 |

Dazu in der Fallakte: Tagebuch, Mappe, Brief, Haustechnik, alle Memos/Sprachnachrichten und die Lagebesprechungen `B_1` und `B_7`.

---

# 12. Medien und Requisiten

| Was | Stand |
|---|---|
| Porträts aller Figuren (groß und als Avatar) | in `src/img/` |
| Vorspann- und Festnahmebilder (`v_*`, `f_*`), Tatortfoto und Spurenbilder (`t_*`, `kartenleser`) | vorhanden |
| Kamerabilder `k_terrasse`, `k_auto`, `k_mair`, `k_flur`, `k_mantel`, `k_taxi` | vorhanden; Bild-Prompts in `tools/grok_bilder.py` |
| Fassadenfotos Landschaftshaus (ganze Wand, Gründer, Kaiser, Heinrich, Georg, Ludwig, Albrecht) | vorhanden |
| Historische Porträts für Tagebuch und Stammbaum (`hist_*`) | vorhanden |
| Alle Audios (Kapitel 10.2) | vorhanden, Microsoft-Stimmen; Endfassung offen |
| Druckvorlagen | `docs/Druckvorlagen_Der_letzte_Erbe.pdf` |
| Echte Kassette mit Zahlenschloss, Repliken (Brosche, Taler, Siegel), Gebäck | optional, Spielleitung |

---

# 13. Spielleitung vor Ort

## 13.1 Vor Spielbeginn

- Route bei ähnlicher Tageszeit ablaufen: Lesbarkeit der Denkmal-Inschrift, Sichtbarkeit der Fassadenfiguren und des Rathauswappens in der Dämmerung, Netzqualität, Weihnachtsmarktbetrieb.
- **Am Handy testen:** Rundgang Heiliggeist (GPS-Fang, Kompass/Blickrichtung), Haken „Vernehmung angehört“.
- Team-Adresse festlegen (`?team=name`) und an alle Spieler schicken; nach dem Start Team abschließen.
- Falls echte Kassette: Code im Spielleitungsmodus hinterlegen.
- Standortfreigabe auf allen Handys prüfen; Powerbank einpacken.

## 13.2 Teambriefing (ca. 2 Minuten)

> „Ihr löst heute einen **vollständig erfundenen Kriminalfall**, der mit echter Landshuter Geschichte verknüpft ist. Alle Figuren, Anrufe und Bilder sind Teil des Spiels. Bewegt euch rücksichtsvoll, betretet keine gesperrten Bereiche, fasst nichts an und sprecht keine Passanten an. Ratet nicht wild: Jeder hat pro Schritt einen Versuch. Wenn ihr hängt, nutzt die Hinweise.“

## 13.3 Tempo

- Nach einigen Minuten ohne Fortschritt auf die Hinweise-App verweisen.
- Bei Technikproblemen: Station im Spielleitungsmodus überspringen; die App vergibt dann die Beweise der Station.
- Keine Station blockiert endgültig.

## 13.4 Finale auf dem Markt

Die Ringelstecherwiese kann voll, gesperrt oder leer sein. Treffpunkt am Rand wählen, nicht an einen bestimmten Stand binden. **Keine unbeaufsichtigte Kassette im öffentlichen Raum deponieren.**

---

# 14. Nachrichten und Reaktionen (Textbausteine)

**Unbekannt (Chat):**
- `N01` nach Station 2: „Ihr habt den Vater gefunden. Schön. Fragt euch lieber, wo Notar Mair am Tatabend war. Achtzehn Minuten sind eine lange Zeit für ein Telefonat.“
- `N02` nach Station 4, mit Anhang `Brief_1503.pdf`: „Ihr sucht die Kiste mit den fehlenden Erbstücken? Ich habe einen Brief aus dem Winter 1503. Er sagt, wo sie damals lag. Dreht euch um.“
- `N03` nach Station 5: „Ein falscher Brief? Dann hat jemand im Archiv gepfuscht. Notar Mair hatte die Datei offen. Nur so als Hinweis.“

**Unbekannt (Anrufe):** `CALL_01`, `CALL_06`, `CALL_07` (Wortlaut in Kapitel 6 und 8).

**Fehlermeldungen (Auswahl):**
- Herzogswand: „Dort ist sie nicht. Schaut noch einmal an der Wand.“ / „Das ist der Großvater. Gesucht ist der Vater des Bräutigams.“
- Denkmal: „Falsches Passwort. Die Zahl steht auf der Rückseite des Sockels.“
- Listen: „Noch nicht richtig. Hakt jedes Stück von 1475 einzeln in der Liste von 1503 ab.“
- Brief: „Daran ist nichts Verdächtiges. Schaut auf den Baubeginn im Steckbrief.“
- R7: „Er war in Regensburg. Was zeigt die Karte also wirklich?“
- Postfach: „Das ergibt noch keinen Sinn. Zählt die Glockenschläge in der Sage.“
- Streichen ohne Beleg: „Dafür gibt es noch keinen Beleg.“
- Anklage: „Seidl: ‚Das reicht nicht. …‘“ mit Hinweis zur jeweiligen Frage.
- Tresor: „Sie war die Braut. Aber wem hatte Georg sein Erbe vermacht?“

---

# 15. Fairness und Qualität

**Fairness-Test je Rätsel:**
1. Liegen alle nötigen Informationen **vor der Lösung** vor?
2. Ist die richtige Antwort klar von den falschen unterscheidbar?
3. Findet ein ortsfremdes Team den Ort (Ortstipps, „Ort zeigen“)?
4. Ist der historische Sachverhalt korrekt?
5. Lässt sich das Rätsel bei Dunkelheit, Regen oder Andrang lösen?
6. Gibt es einen Ersatzweg bei GPS-, Netz- oder Audioproblemen (Spielleitungsmodus, Mitlesetext, Druckvorlagen)?

**Vermeiden:** Insiderwissen als Voraussetzung, Aufklärung durch einen einzigen Satz der App, eine Täterin, die schon nach zwei Stationen feststeht, Zwang zu echten Anrufen oder Herausgabe persönlicher Daten. Die Figuren dürfen lügen, der **Spielkanon** (Kapitel 4.3) muss konsistent bleiben.

---

# 16. Sicherheit und Datenschutz

- Fiktion klar kennzeichnen (Start, „Was war echt?“).
- Gebäude und Denkmäler nicht bekleben, besteigen oder als Ablage nutzen.
- Die App nutzt Standort (für „Wir sind da“ und den Rundgang) und optional Kompass; keine Kontakte, kein Mikrofon. Das Teamfoto ist freiwillig.
- Gemeinsamer Spielstand pseudonym über die Team-Adresse; die Seite ist mit `X-Robots-Tag: noindex` von Suchmaschinen ausgenommen.
- Die Anrufe sind reine Simulation in der App, kein echter Telefonanruf.
- Rechte an Fotos, Stimmen und Musik prüfen, spätestens für die ElevenLabs-Endfassung.
- Nicht auf Fuß- oder Radwegen stehen bleiben, besonders am Ländtor und auf dem Markt.

---

# 17. Offene Punkte

Stand 24.11.2026, Details in `docs/STAND_1475.md`:

1. **Am Handy vor Ort testen:** Rundgang (GPS-Fang, Kompass/Blickrichtung), Haken „Vernehmung angehört“.
2. **Zweig `kuerzer-und-runder` nach `main` zusammenführen**, sobald der Test passt.
3. **Kurze Meldung oben am Rand** (z. B. „Neues Alibi“): Entscheidung offen.
4. **Endfassung der Stimmen** mit ElevenLabs ganz zum Schluss.
5. Optional: Tagebuchseiten Hochzeit/Rechnung weiter nach vorne ziehen (jetzt Seite 5 und 6).
6. Optional: Albrecht im Stammbaum auf Elisabeths Höhe (aus historischen Gründen bisher nicht umgesetzt).
7. **„Was war echt?“ prüfen:** Die Liste nennt noch Burg Trausnitz und ihren Brand 1961, den Kölner Spruch von 1505 und Elisabeths vier Söhne. Diese Inhalte kommen im aktuellen Spielablauf nicht mehr vor (die Trausnitz-Karte `I_TRAUSNITZ` wird nicht ausgelöst, die Söhne wurden aus dem Stammbaum entfernt). Entweder streichen oder wieder einbauen.
8. **Unbenutzte Inhalte im Code:** `V_FINALE`, `N06` und mehrere Lagebesprechungen (`B_2`–`B_6`, `I_MAIR`, `I_ZEUGIN`, `I_ANRUF`, `I_FALLE`, `I_TRAUSNITZ`, `I_CW04`) stehen noch in `src/index.html`, werden aber nicht mehr angezeigt. `B_2` erwähnt noch die entfallene „Rückseite der Fotos“. Aufräumen oder bewusst als Reserve behalten.

---

# 18. Historische Quellen

Die Quellen dienen der historischen Einordnung. Alle im Spiel gezeigten Briefe, Listen und Protokolle sind keine Originaldokumente.

- **[Q1] Historisches Lexikon Bayerns – Landshuter Hochzeit, 1475.**  
  https://www.historisches-lexikon-bayerns.de/Lexikon/Landshuter_Hochzeit%2C_1475
- **[Q2] Bayerischer Rundfunk, radioWissen – „Die Landshuter Hochzeit“.** Überlieferte Mengen und Kosten.  
  https://www.br.de/radio/bayern2/sendungen/radiowissen/geschichte/landshuter-hochzeit-144.html
- **[Q3] Denkmal Ludwigs des Reichen.** Errichtungsjahr 1858.  
  https://de.wikipedia.org/wiki/Denkmal_Ludwigs_des_Reichen
- **[Q4] Liste der Baudenkmäler in Landshut-Altstadt.**  
  https://de.wikipedia.org/wiki/Liste_der_Baudenkm%C3%A4ler_in_Landshut-Altstadt
- **[Q5] Historisches Lexikon Bayerns – Wittelsbachische Primogeniturordnung (1506).** Erbfolgestreit nach Georgs Tod.  
  https://www.historisches-lexikon-bayerns.de/Lexikon/Wittelsbachische_Primogeniturordnung_%281506%29
- **[Q6] Bayerische Schlösserverwaltung – Stadtresidenz.** Baubeginn 1536.  
  https://schloesser.bayern.de/deutsch/service/tourismus/Besucherinformation2026.pdf
- **[Q8] Stadt Landshut – Dulten, Märkte, Messen.** Christkindlmarkt 2026.  
  https://landshut.de/kultur-sport/dulten-maerkte-messen
- **[Q10] Landshut erleben – Ländtor.** Drei-Helme-Wappen über dem Torbogen.  
  https://erleben.landshut.de/blog/laendtor-das-tor-zur-stadt/
- **[Q11] RegioWiki Niederbayern – Landschaftshaus.**  
  https://www.niederbayern-wiki.de/wiki/Landschaftshaus
- **[Q12] Verein Landshuter Gästeführer – „who's who am Landschaftshaus“.** Alle 30 Figuren mit Position. Nur als Recherchequelle, Fotos und Texte geschützt.  
  https://www.stadtfuehrung-landshut.com/landschaftshaus.php
- **[Q13] Wikipedia – St. Martin (Landshut).** Turmhöhe.  
  https://de.wikipedia.org/wiki/St._Martin_(Landshut)
- **[Q14] Wikipedia – Heilig-Geist-Kirche (Landshut).** Baubeginn 1407, unvollendeter Turm.  
  https://de.wikipedia.org/wiki/Heilig-Geist-Kirche_(Landshut)
- **[Q15] MVV-Stadtrallye Landshut 2026, Seite 8.** Rathaus, Wappen über der Uhr, Residenzfassade.  
  https://www.mvv-muenchen.de/stadtrallye-mobil/mvv-stadtrallyes-2026/landshut/seite-8

---

# 19. Änderungen gegenüber Fassung 1.2 (22.10.2026)

Für alle, die das alte Konzept kennen:

- **Start:** Kein Umschlag und keine QR-Codes mehr; Start über Push, Vorspann, Seidls Sprachnachricht, Tatort mit fünf Spuren und Handy-Code 1475. Seidl führt durchs Spiel.
- **Station 1:** Statt Büste Hans von Burghausens nun Schätzrätsel Turmhöhe (130 m). Der erste Anruf führt zum Turm statt zum Baumeister.
- **Station 2:** Statt drei Detailfotos (Adler, Reichsapfel, Ludwig X.) nun vier Figuren (Gründer, Kaiser, Großvater, Bräutigam) und die verwischte Rechnung. Keine Notizen zu Helmen und 1536 mehr, keine Rückseite der Fotos, kein Expertenmodus „Inschrift lügt“.
- **Neu:** Zwischenstopp Albrecht an der Herzogswand mit Memo zum Erbfolgekrieg und Stammbaum.
- **Station 3:** Audio „Das Erbe“ deutlich kürzer; der Erbfolgekrieg wird erst beim Zwischenstopp erzählt.
- **Station 4:** Statt Siegelfragment ein Wappenschloss mit drei Rädern; Listen mit acht bzw. fünf Stücken. Die Schätze heißen jetzt Rubinbrosche, **zehn goldene Taler** (statt zwölf Silberschalen) und Familiensiegel, alle in **einer** Kiste (statt drei Kisten).
- **Station 5:** Statt Fassadendetail nun die Zeile „Stadtresidenz“ gegen den Baubeginn 1536. Seidl erklärt den Zweck der Fälschung (Herkunftsnachweis).
- **Station 6:** Statt Weltgericht im Tympanon ein GPS-Rundgang um die Kirche; statt Zeitstrahl zum Markieren sechs Kameraclips und vier einzelne Urteile. Stromausfall und akkugepufferter Kartenleser entfallen. Feld wird per Telefonat entlastet.
- **Station 7:** Schlüssel ist nicht mehr „drei Helme“, sondern die **sieben Glockenschläge** der (erfundenen) Sage vom Ritter. Die Zeugin führt zum Tor.
- **Leitbegriff „Pfand der Verbindung“ entfällt** ganz; die Stimme verrät sich nur noch durch Täterwissen (20:48, R7).
- **Station 8:** Statt Beweisboard mit Beweisgruppen vier Fragen von Seidl; Mairs Nachricht enthält Falkenrieds Geheimnis (keine eigene Abschiedsnachricht mehr). Neu: Falle und Festnahme-Szene, Urkunde, Zeitungsartikel, Teamfoto. Keine goldenen/silbernen Enden mehr.
- **Team:** mehrere Handys pro Team mit gemeinsamem Spielstand und Versuchssperren statt einem Gerät pro Team.

---

**ENDE – DER LETZTE ERBE**

*Konzept- und Spielleitungsfassung. Alle erfundenen Figuren und Ereignisse sind Teil einer fiktiven Erzählung.*
