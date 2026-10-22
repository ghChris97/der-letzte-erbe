# Der letzte Erbe – Akte 1475

Weihnachtlicher Krimi-Stadtrundgang durch Landshut. Die Spieler ermitteln mit „Falkenrieds Handy“, einer Web-App im Stil eines Smartphones, an acht Stationen der Altstadt.

**Live:** https://der-letzte-erbe.netlify.app (eigenes Team: `?team=name`)

## Aufbau

| Pfad | Inhalt |
|---|---|
| `src/index.html` | Die komplette App (HTML, CSS, JS in einer Datei) |
| `src/img/` | Bilder: Porträts, Tatort, Hintergrund, Platzhalter-Motive, App-Icons, QR-Code |
| `src/audio/` | Stimmen (MP3) und `cues.json` mit Satz-Zeitmarken |
| `src/sw.js` | Service Worker (Installation, Offline-Cache) |
| `build.py` | Baut `dist/` für Netlify (Head, Manifest, Vollbild auf dem Handy) |
| `docs/` | Spielkonzept und Druckvorlagen |
| `tools/` | Skripte für Stimmen (Microsoft-Neuralstimmen) und Bilder (xAI) |

## Bauen und deployen

```bash
python3 build.py              # erzeugt dist/
npx netlify deploy --prod --dir dist
```

## Gemeinsamer Spielstand

Supabase-Projekt `der-letzte-erbe` (Tabelle `games`, Funktion `save_game`). Alle Handys mit derselben Team-Adresse teilen Fortschritt, Ereignisse und Versuchssperren. Ohne Verbindung läuft die App allein auf dem Gerät.

## Spielleitung

Fünfmal auf die Uhrzeit oben links tippen, PIN `2412`: Ereignisse auslösen, Stationen springen, Druckvorlagen, Spielstand zurücksetzen.

## Offene Platzhalter

Echte Büste (St. Martin), Fassadendetails (Landschaftshaus), Siegel mit Helmen und Rauten (Rathaus), Fassadendetail für den Brief (Residenz), Tympanon-Motive (Heiliggeist), genaue Koordinaten Landschaftshaus und Ländtor.
