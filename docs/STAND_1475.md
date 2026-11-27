# 1475 · Der letzte Erbe – Projektstand

Stand: 15. November 2026. Übergabe-Dokument, damit in einem anderen Projekt nahtlos weitergearbeitet werden kann.

---

## 1. Kurzüberblick

| | |
|---|---|
| **Was** | Weihnachtlicher Krimi-Stadtrundgang durch die Landshuter Altstadt. Ein Team ermittelt mit „Falkenrieds Handy“, einer Web-App im Look eines Smartphones, an 8 Stationen einen Mord auf. |
| **Spieler** | Voraussichtlich ein Team; jedes Mitglied hat die App auf dem eigenen Handy (gemeinsamer Spielstand). Spielleitung ist dabei. |
| **Live** | https://der-letzte-erbe.netlify.app (eigenes Team: `?team=name`) |
| **Repo** | `github.com/ghChris97/der-letzte-erbe` (öffentlich) |
| **Aktueller Arbeitszweig** | `kuerzer-und-runder` – **noch nicht in `main` zusammengeführt**. `main` hat den Stand vor der Überarbeitung vom 12.11.2026. |
| **Deployt** | Live ist der Stand von `kuerzer-und-runder` (Commit `076d5f8`, Deploy am 12.11.2026, 22:17). |
| **Regel** | Vor **jedem einzelnen** Netlify-Deploy fragen. Pushen nach GitHub ist ohne Freigabe okay. |

---

## 2. Technik

### Aufbau des Repos

| Pfad | Inhalt |
|---|---|
| `src/index.html` | Die komplette App (HTML, CSS, JS in einer Datei, ca. 290 KB) |
| `src/img/` | Bilder: Porträts, Tatort, Kamerabilder, Fassadenfotos, historische Porträts, App-Icons |
| `src/audio/` | Sprachaufnahmen (MP3) und `cues.json` mit Satz-Zeitmarken für den Mitlesetext |
| `src/sw.js` | Service Worker (Installation als App, Offline-Cache) |
| `build.py` | Baut `dist/` (Head, Manifest, Vollbild auf dem Handy, kopiert img/audio) |
| `netlify.toml` | Publish `.`, Header `X-Robots-Tag: noindex` |
| `docs/Spielkonzept.md` | Ursprüngliches Konzept – **teilweise veraltet** (z. B. alte Station 1 mit Büste/Siegel). Die App ist maßgeblich. |
| `docs/Druckvorlagen_Der_letzte_Erbe.pdf` | Druckvorlagen |
| `tools/make_audio.py` | Erzeugt Sprachnachrichten + Zeitmarken (Microsoft-Neuralstimmen über `edge-tts`) |
| `tools/make_cut.py` | Sprechertexte der Szenen (Vorspann `CUT_V*`, Festnahme `CUT_F*`), Aufruf mit Schlüsseln möglich: `python3 tools/make_cut.py CUT_F1 CUT_F4` |
| `tools/make_sage.py`, `make_verhoer*.py` | Sage am Ländtor, Vernehmungen |
| `tools/make_audio_el.py`, `make_verhoer_el.py` | ElevenLabs-Varianten (für die Endfassung, Schlüssel nötig) |
| `tools/grok_bilder.py` | Bild-Prompts (xAI). Enthält u. a. `k_mair`, `k_flur`, `k_taxi` |

### Bauen, testen, deployen

```bash
python3 build.py                       # erzeugt dist/
cd dist && python3 -m http.server 8765 # lokal testen
# Deploy: über Netlify (Projekt der-letzte-erbe, Site-ID 764132e1-da65-4c23-98ec-f72750a26bf3), Ordner dist/
```

Audio neu erzeugen (nach Textänderung):
```bash
python3 tools/make_audio.py V_MAIR       # einzelne Aufnahme
# danach src/audio/cues.json in die Konstante CUES in src/index.html übernehmen
```
Wichtig: Die Satzanzahl im App-Text muss zur Anzahl der Zeitmarken in `cues.json` passen. Im Sprechtext für die Tonerzeugung Jahreszahlen ausschreiben („fünfzehnhundertvier“), im App-Text Ziffern.

### Stimmen (aktuell kostenlose Microsoft-Stimmen, Endfassung später)
| Figur | Stimme |
|---|---|
| Kommissarin Seidl | de-DE-AmalaNeural |
| Falkenried | de-DE-ConradNeural |
| Notar Mair | de-DE-KillianNeural |
| Rosa Brandl | de-AT-IngridNeural |
| Unbekannt | de-DE-KatjaNeural, verfremdet (ffmpeg-Filter) |

Alle Aufnahmen laufen in der App mit **1,1-facher Geschwindigkeit** (`VO_RATE = 1.1`, Tonhöhe bleibt).

### Gemeinsamer Spielstand
Supabase-Projekt `der-letzte-erbe` (`https://jsiwhmzblewnldjtpcye.supabase.co`), Tabelle `games`, Funktion `save_game`. Alle Handys mit derselben Team-Adresse teilen Fortschritt, Ereignisse und Versuchssperren. Ohne Verbindung läuft die App allein auf dem Gerät.

Lokaler Speicher: `falkenried-v…` (Spielstand), `falkenried-dev` (Entwickler-/Testmodus), `falkenried-tree` (gesehene Stammbaum-Personen), `falkenried-news`, `falkenried-photo`, `falkenried-local`.

### Spielleitung
Fünfmal auf die Uhrzeit oben links tippen, PIN **1432**: Ereignisse auslösen, Stationen springen, Standortprüfung aus (Testmodus), Druckvorlagen, Spielstand zurücksetzen.

---

## 3. Die Geschichte

**Fall:** Kunstsammler Maximilian von Falkenried wird am Abend des 19. Dezember 2026 in seinem Archiv erschlagen. Fünf Menschen waren im Haus.

**Täterin:** Dr. Helena Dorn (Historikerin, betreute sein Archiv). Sie tat um 20:30 so, als würde sie gehen, öffnete um 20:48 mit der Ersatzkarte R7 (aus der Digitalisierung 2025, als verloren gemeldet) das Archiv, erschlug Falkenried und nahm die Liste von 1475 mit. Die Kassette fand sie nicht – deshalb braucht sie die Spieler und meldet sich als „Unbekannt“.

**Motiv:** Drei Hochzeitsgaben von 1475 (Rubinbrosche, Taler, Siegel) aus einer Kiste, die im Winter 1503 aus der Stadt gebracht wurde. Dorn wollte sie über Kunsthändlerin Clara Weiß an Käufer „CW-04“ verkaufen und fälschte dafür einen Herkunftsbrief von 1503.

**Zweites Geheimnis:** Falkenried glaubte, dass Elisabeths kleiner Sohn Georg 1504 nicht starb, sondern heimlich in Sicherheit gebracht wurde, und dass er selbst von ihm abstammt. Er wollte nichts verkaufen; alles sollte zurück nach Landshut.

**Historischer Rahmen (echt):** Landshuter Hochzeit am 14. November 1475 in St. Martin (Georg der Reiche, 20, und Hedwig, 18, Tochter des Königs von Polen); Ludwig der Reiche bezahlte. Georg setzte seine Tochter Elisabeth als Erbin ein, obwohl die Hausverträge nur Männer erlaubten; nach seinem Tod im Dezember 1503 zog sein Vetter Albrecht IV. von München in den Landshuter Erbfolgekrieg und gewann. Elisabeth starb 1504. **Erfunden:** Falkenried und alle Figuren, der Mord, die Kiste, das Überleben des kleinen Georg, jede Abstammung.

### Figuren
| Figur | Rolle | Behauptung | Wahrheit |
|---|---|---|---|
| Dr. Helena Dorn, 47 | Historikerin | „Um halb neun gegangen.“ | Gelogen: Wagen fuhr erst 21:02. Täterin. |
| Benedikt Mair, 55 | Notar | „Kurz telefoniert, draußen.“ | Halb wahr: 18 Min. am Hoftor (20:34–20:52). Verwahrt die Kassette. |
| Tobias von Falkenried, 31 | Neffe, Schulden | „Gestritten, danach rauchen.“ | Stimmt: Terrassenkamera 20:44–20:58. |
| Clara Weiß, 43 | Kunsthändlerin | „Den ganzen Abend am Tisch.“ | Gelogen: telefonierte 20:44–20:50 im Flur mit CW-04. Vermittelt nur. |
| Rosa Brandl, 58 | Haushälterin, Zeugin | – | Sah Clara telefonieren und eine Frau im Mantel zum Archiv gehen. |
| Martina Seidl | Kommissarin, Kripo Landshut | – | Führt durch das Spiel. |

---

## 4. Spielablauf und Lösungen

**Start:** Push-Nachricht → Vorspann (Szene mit Sprecher) → Seidls Sprachnachricht (Code fürs Handy) → Tatort mit 5 Spuren → Team eintragen → Sperrbildschirm, Code **1475** → „Wer ist wer“ (Vernehmungen freiwillig) → Anruf von Unbekannt.

| # | Station | Koordinaten | Rätsel | Lösung |
|---|---|---|---|---|
| 1 | St. Martin (Turm) | 48.534237, 12.151014 | Notizbuch-Zahlenschloss: Turmhöhe schätzen (höher/tiefer) | **130** |
| 2 | Landschaftshaus, Altstadt 28 (Herzogswand) | 48.533888, 12.150226 | 4 Fotos an der Wand finden: Gründer (oben 2), Kaiser (oben 4, sitzt), Großvater Heinrich (Mitte 6), Bräutigam Georg (Mitte 10). Dann die verwischte Rechnung „Beglichen durch Herzog L▒▒▒▒▒“: Vater des Bräutigams antippen | **Mitte 9, Ludwig der Reiche** |
| 3 | Denkmal Ludwigs des Reichen (Dreifaltigkeitsplatz) | 48.532417, 12.149794 | Archiv-Passwort: Jahr in römischen Ziffern auf dem Rücken | **1858** (MDCCCLVIII) |
| ↪ | Zwischenstopp Herzogswand | – | Albrecht der Weise suchen (unten links) → Memo zum Erbfolgekrieg mit Stammbaum | Platz U1 |
| 4 | Rathaus | 48.536228, 12.152024 | Wappenschloss (Wappen über der Rathausuhr) + Listenvergleich 1475/1503 | **3 · Helm · Rot**; fehlende Stücke **2, 5, 7** |
| 5 | Stadtresidenz | 48.536103, 12.151237 | Gefälschter Brief „1503“: welche Zeile passt nicht? | „lagert sicher in der **Stadtresidenz** des Herzogs“ (Bau erst 1536) |
| 6 | Heiliggeistkirche | 48.538667, 12.152562 | a) Rundgang um die Kirche (Ring) b) Kameras + 4 Aussagen (stimmt/gelogen) c) Anruf, Frage Karte R7 | Tobias stimmt, Mair halb wahr (beides zählt), Clara gelogen, Helena gelogen; R7: „nur seine Karte benutzt“ |
| 7 | Ländtor | 48.535305, 12.149236 | Verschlüsselte Kuriernachricht; Schlüssel = Glockenschläge der Sage (7) → 7 zurück | **ABHOLUNG**; dann Verdächtige streichen → bleibt HD |
| 8 | Ringelstecherwiese | 48.532814, 12.146553 | Anklage (4 Beweisfragen) → Mair-Nachricht → Tresor-Namensschloss | Name **Elisabeth** |

**Ende:** Nach „Elisabeth“ → Seidls Karte „Sie kommt – gebt Mair die Kassette zurück, versteckt euch“ → Festnahme-Szene (`CUT_F*`) → Seidls Dank (`SEIDL_ENDE`), Urkunde, Zeitungsartikel, Auflösung, „Was war echt?“.

### Rundgang Heiliggeist (Station 6a)
- Karte von oben (Leaflet + OpenStreetMap), Kirche als Fläche (`CHURCH`, 4 gemessene Ecken).
- Ring folgt dem **vor Ort eingezeichneten Laufweg** (`WALK_PATH`, ca. 155 m) über den Platz, 12 Wegstücke, **11 nötig**, Fangradius 15 m, GPS-Genauigkeit ≤ 35 m.
- Standort als blauer Punkt mit Genauigkeitskreis und **Blickrichtung** (Kompass; ersatzweise GPS-Laufrichtung). Auf iOS erscheint der Knopf „🧭 Blickrichtung zeigen“ (Berechtigung).
- Testmodus: Knopf „Rundgang simulieren“, echtes GPS zählt trotzdem.

### Haustechnik-Kameras (Station 6b)
| Clip | Bild | Inhalt |
|---|---|---|
| Terrasse 20:44–20:58 | `k_terrasse.jpg` | Tobias raucht; durch die Glastür Claras leerer Platz |
| Einfahrt 20:30–20:33 | `k_auto.jpg` | Dorns Wagen steht, niemand steigt ein |
| Einfahrt 20:34–20:52 | `k_mair.jpg` | Mair am Hoftor mit Handy |
| Flurfenster 20:44–20:50 | `k_flur.jpg` | Clara im Flur am Telefon |
| Einfahrt 21:02 | `k_mantel.jpg` | Frau im Mantel am Wagen |
| Einfahrt 21:06 | `k_taxi.jpg` | Taxi, Einfahrt leer (Wagen weg) |

Protokoll (7 Zeilen, aufgeklappt) u. a.: „Handy von Benedikt Mair: Anruf, 18 Minuten, außerhalb des Haus-WLANs“.

### Sprachnachrichten / Anrufe (Auslöser)
| ID | Sprecher | Wann |
|---|---|---|
| V_START | Seidl | Start (Code 1475) |
| CALL_01 | Unbekannt | nach „Wer ist wer“ |
| V_ERBE | Falkenried | Station 3 gelöst (Denkmal) |
| V_ALBRECHT | Falkenried | Zwischenstopp Albrecht; Stammbaum darunter, neue Personen leuchten |
| V_RESIDENZ | Seidl | Station 5 gelöst; nennt Heiliggeist direkt |
| V_TURM | Falkenried | Rundgang geschafft |
| CALL_06 | Unbekannt | nach den 4 Aussagen |
| V_ZEUGIN / ZEUGIN_KURZ | Rosa | nach Frage R7 |
| CALL_07 | Unbekannt | Station 7 gelöst („Mair wartet auf der Ringelstecherwiese … holt es ab, öffnet es nicht“) |
| V_MAIR | Mair | nach der Anklage – enthält jetzt auch Falkenrieds Geheimnis und den Hinweis aufs Namensschloss |
| V_FINALE | – | **nicht mehr verwendet** (Inhalt in V_MAIR) |

Die letzte Aufnahme lässt sich auf der Auftragskarte jederzeit nochmal anhören.

### Stammbaum
Nur noch: Heinrich XVI. → Ludwig IX. (vor der Herzogswand als „L. ?“) → Georg ∞ Hedwig (Hochzeit 1475) → Elisabeth (mittig, „Testament: Erbin“) → ihr Sohn Georg (1500–„1504“) → ? → Maximilian v. Falkenried – Tobias. Albrecht IV. steht als Vetter auf Georgs Höhe (historisch korrekt), rote Kriegslinie zu Elisabeth. Entfernt: König Maximilian, Ruprecht, Zwilling, Ottheinrich, Philipp.

### Tagebuch (Notizen-App)
Öffnet beim ersten Mal auf **Seite 1**. Seiten: Mo 2.11., Sa 28.11., Do 10.12. (Wandfoto), Sa 12.12., **Do 17.12. (Georg & Hedwig, Hochzeit 14.11.1475)**, Fr 18.12. (Abschrift der Rechnung, Name verwischt bis zur Herzogswand), Sa 19.12. Wochentage stimmen für 2026.

---

## 5. Änderungen der Überarbeitung (12.11.2026, Zweig `kuerzer-und-runder`)
- Sprachnachrichten etwa halbiert und neu erzeugt; Stationstexte gestrafft; Wiederholungen (Mord dreifach erzählt, doppelte Täterfrage, dreifache Festnahme) entfernt.
- Auftragskarte: nur Spur + „Wozu“ (die Zeile „Ihr sucht“ verriet den Ort); rote Leiste „neue Hinweise“ entfernt.
- Herzogswand von 8 auf 4 Fotos + Rechnungsrätsel; Rückseite der Fotos entfällt (Denkmal-Hinweis direkt auf der Ludwig-Karte).
- Heiliggeist: Schritt für Schritt statt einer langen Seite; neue Kameraclips für Mair und Clara; neues Taxi-Bild.
- Rundgang als Karte mit eingezeichnetem Laufweg, Standort mit Blickrichtung.
- Vernehmungen spielten über die Gerätestimme statt als Datei → behoben; „✓ angehört“ erscheint.
- Unbekannts Brief-Nachricht: „Ihr sucht die Kiste mit den fehlenden Erbstücken?“
- Finale: CALL_07 neu formuliert, Falle vor der Festnahme, Handschuhe „mit Spuren vom Tatort“, nur noch eine Nachricht (Mair) statt zwei.
- Design bewusst **unverändert dunkel** (helle Varianten A/B und dunkle C/D wurden gezeigt und verworfen).

---

## 6. Offene Punkte
1. **Am Handy vor Ort testen:** Rundgang (GPS-Fang, Kompass/Blickrichtung), Haken „Vernehmung angehört“ nach kompletter Aufnahme.
2. **Zweig zusammenführen:** `kuerzer-und-runder` → `main`, sobald der Test passt.
3. **Kurze Meldung oben am Rand** (z. B. „Neues Alibi“): noch drin, Entscheidung offen.
4. **Endfassung der Stimmen** (ElevenLabs) ganz zum Schluss; aktuell überall Microsoft-Stimmen.
5. Optional: Tagebuchseiten Hochzeit/Rechnung weiter nach vorne ziehen (stehen jetzt auf Seite 5 und 6).
6. Optional: Albrecht im Stammbaum auf Elisabeths Höhe (vom Nutzer gewünscht, aus historischen Gründen nicht umgesetzt).
7. `docs/Spielkonzept.md` ist in Teilen veraltet und könnte an die App angeglichen werden.

---

## 7. Überarbeitung vom 27.11.2026 (Zweig `claude/project-thread-1fs3cv`)
- Neuburg an der Donau komplett entfernt (Tagebuch, Stammbaum, Fallakte), dazu „Was war echt?“ ohne Trausnitz, Kölner Spruch, vier Söhne.
- Jonas Feld gestrichen: Karte R7 ist jetzt eine verlorene Ersatzkarte aus der Digitalisierung; R7-Frage ohne Feld, Streichliste mit 4 Personen. Audio VERHOER_FELD und Bilder entfernt.
- Unbekannt reduziert: nur noch Anruf CALL_06 (Täterwissen 20:48/R7) und Nachricht N02 (Brief 1503). CALL_01, CALL_07, N01, N03 entfernt; die Wiese kündigt Seidls Lagebesprechung B_7 an.
- Seidls Sprachnachrichten im Spiel (V_RESIDENZ) kommen als eingehender Anruf mit Profilbild.
- Nach dem Archiv-Passwort (Station 3): Schloss springt auf, Belohnung „Glückwunsch, ihr habt Falkenrieds Archiv geöffnet“ mit Inhalt (Memo, Mappe) und Erklärung, warum es zurück zur Herzogswand geht; danach Falkenrieds Memo.
- Eigene Optik je Bereich (Archivkarton, Pappmappe mit Gummiband und Schloss, Haustechnik, Postfach, Tresor, Notizen), gesperrte Inhalte vorher sichtbar, Aufspring-Animation bei jedem geknackten Schloss, Fallakte mit Dateityp (Audio mit Tonspur, Textdokument, Foto, Mappe).
- Unbenutzte Texte entfernt: V_FINALE, N06, I_MAIR, I_ZEUGIN, I_ANRUF, I_FALLE, I_TRAUSNITZ, B_2 bis B_6.
- Rundgang Heiliggeist: 36 Wegstücke à ca. 4 m (vorher 12), Fangradius 8 m, GPS nur bis 20 m Ungenauigkeit; alle Stücke nötig, Lücken bis 2 Stücke werden aufgefüllt; Schloss erst 1,8 s nach der ganz grünen Runde. Eingezeichnetes Kirchen-Viereck entfernt.
- Jedes Schloss öffnet erst auf Tippen („Schloss öffnen“), dann Animation, dann „Weiter …“ mit dem Ziel. Auch nach dem Rundgang („Runde geschafft!“).
