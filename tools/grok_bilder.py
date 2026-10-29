"""
Der letzte Erbe – Tatortbilder mit der xAI-API (Grok Imagine) erzeugen.

Benutzung:
  1. API-Schlüssel auf https://console.x.ai anlegen.
  2. Schlüssel als Umgebungsvariable setzen (nicht in diese Datei schreiben!):
       macOS/Linux:  export XAI_API_KEY="xai-..."
       Windows (PowerShell):  $env:XAI_API_KEY="xai-..."
  3. Einmalig:  pip install requests
  4. Starten:   python grok_bilder.py            (alle Motive)
                python grok_bilder.py tatort     (nur ein Motiv)

Die Bilder landen im Ordner "tatort_bilder" neben diesem Skript.
"""

import base64
import os
import sys
import time
from pathlib import Path

import requests

API_URL = "https://api.x.ai/v1/images/generations"
MODEL = "grok-imagine-image-2.0"
VARIANTEN = 4          # Bilder pro Motiv (1–10)
AUFLOESUNG = "2k"      # "1k" oder "2k"
QUALITAET = "medium"   # "low", "medium" oder "auto"

MOTIVE = {
    "tatort": {
        "aspect_ratio": "3:2",
        "prompt": (
            "A realistic crime scene photograph taken at night in the private archive room of an elegant "
            "old Bavarian townhouse, shot from the doorway at a slightly elevated angle. Floor-to-ceiling dark "
            "wooden bookshelves filled with old ledgers, archive boxes and leather-bound books. In the foreground "
            "an antique brass reading lamp lies knocked over on the parquet floor, still glowing, casting warm "
            "golden light diagonally across the floorboards. Yellowed handwritten documents and inventory lists "
            "are scattered around the lamp. On a heavy wooden desk lies an open, empty leather document folder. "
            "A wooden chair is tipped over next to the desk. Five small yellow numbered police evidence markers "
            "stand on the floor next to the lamp, the papers, the chair and the door. In the background a heavy "
            "open oak door, and on the wall beside the door frame a small black modern access card reader with a "
            "faint green light. Through the open door, slightly out of focus, a decorated Christmas tree with "
            "warm lights in an elegant salon. No people, no body, no blood, no uniforms, no readable text, "
            "no logos. Moody, quiet, cinematic, documentary forensic photography, shallow depth of field, 35mm."
        ),
    },
    "kartenleser": {
        "aspect_ratio": "4:3",
        "prompt": (
            "Close-up photograph of a small modern black access card reader mounted on an old wooden door frame "
            "of a historic archive room at night, a faint green LED glowing, warm lamplight from the side, "
            "darkness around, shallow depth of field, realistic documentary photography. No people, no text, "
            "no logos."
        ),
    },
    "v_haus": {
        "aspect_ratio": "3:4",
        "prompt": (
            'Cinematic night photograph of an elegant historic three-storey townhouse in the old town of Landshut, Bavaria, gabled facade, light snow falling, warm golden light glowing in the tall windows of the ground floor, a Christmas wreath on the heavy wooden front door, cobblestones with fresh snow, a dark car parked in the small driveway beside the house. Quiet, mysterious, slightly ominous mood, deep blue night sky, 35mm, shallow depth of field. No people, no readable text, no logos.'
        ),
    },
    "v_tisch": {
        "aspect_ratio": "3:4",
        "prompt": (
            'Cinematic photograph of an elegant Advent dinner table in a wood-panelled dining room of an old Bavarian townhouse, set for five people, white tablecloth, candles burning in silver candlesticks, crystal wine glasses half full, fir branches and red berries as decoration, plates with remains of dessert, chairs slightly pushed back as if the guests just stood up. Warm candlelight, dark background, a large glass door to a terrace at night in the background. Moody, tense, 35mm, shallow depth of field. No people, no readable text, no logos.'
        ),
    },
    "v_tuer": {
        "aspect_ratio": "3:4",
        "prompt": (
            "Cinematic close-up at night: a heavy dark oak door to a private archive in an old townhouse, a small modern black access card reader on the door frame. A hand in a black leather glove, the sleeve of a long dark grey wool coat, holds a white plastic key card against the reader; the reader's LED glows green. Dark hallway, warm light from the side, suspenseful thriller mood, shallow depth of field. Face not visible, no readable text, no logos."
        ),
    },
    "t_lampe": {
        "aspect_ratio": "4:3",
        "prompt": (
            'Forensic close-up photograph: an antique heavy brass reading lamp lying knocked over on an old parquet floor in a dark archive room at night, its bulb still glowing warmly. Next to it a small yellow police evidence marker with the number 1. The brass base looks wiped clean. Scattered yellowed papers nearby. Documentary crime scene photography, moody, shallow depth of field. No people, no body, no blood, no readable text, no logos.'
        ),
    },
    "t_faden": {
        "aspect_ratio": "4:3",
        "prompt": (
            'Macro forensic photograph: a single dark charcoal-grey wool fibre caught on a splinter of a tipped-over antique wooden chair leg, lying on an old parquet floor. A small yellow police evidence marker with the number 2 beside it, tweezers of a forensic technician entering the frame. Warm low light, dark background, extremely shallow depth of field. No people visible, no readable text, no logos.'
        ),
    },
    "t_papiere": {
        "aspect_ratio": "4:3",
        "prompt": (
            'Forensic close-up photograph: several yellowed handwritten inventory pages scattered on an old parquet floor at night, each page with a page number in the corner, one page clearly missing from the sequence. A small yellow police evidence marker with the number 3. Warm lamplight from the side, documentary crime scene photography, shallow depth of field. Handwriting illegible, no readable text, no logos.'
        ),
    },
    "t_kalender": {
        "aspect_ratio": "4:3",
        "prompt": (
            'Forensic close-up photograph: a torn page from an elegant leather desk calendar lying on an old parquet floor, a short handwritten entry in fountain pen ink (illegible), a small yellow police evidence marker with the number 4 next to it. Warm low light, dark archive room, shallow depth of field. No readable text, no logos.'
        ),
    },
    "k_terrasse": {
        "aspect_ratio": "16:9",
        "prompt": (
            'Grainy black-and-white security camera footage at night, high-angle wide-angle view from the corner of a house onto a stone terrace with a snowy garden. A young man in a dark jacket stands smoking a cigarette, looking at his phone. Behind him a large glass door gives a clear view into a lit dining room: an elegant dinner table with candles, three people seated, and one empty chair with a patterned silk scarf draped over its backrest. Low resolution, noise, slight fisheye distortion, CCTV look. Faces not recognisable, no timestamp, no readable text, no logos.'
        ),
    },
    "k_auto": {
        "aspect_ratio": "16:9",
        "prompt": (
            'Grainy black-and-white security camera footage at night, high-angle wide-angle view over the small driveway of an old townhouse: a dark mid-size car parked, light snow on its roof, the front door of the house in the background with a lit lantern, nobody around. Low resolution, noise, slight fisheye distortion, CCTV look. No timestamp, no readable text, no licence plate, no logos.'
        ),
    },
    "k_mantel": {
        "aspect_ratio": "16:9",
        "prompt": (
            'Grainy black-and-white security camera footage at night, high-angle wide-angle view over the small driveway of an old townhouse: a slender woman in a long dark wool coat with the hood up, seen from behind, walking quickly from the side door of the house towards a dark parked car, head down, hands in black gloves. Slight motion blur, low resolution, noise, fisheye distortion, CCTV look. Face not visible, no timestamp, no readable text, no licence plate, no logos.'
        ),
    },
    "k_taxi": {
        "aspect_ratio": "16:9",
        "prompt": (
            'Grainy black-and-white security camera footage at night, high-angle wide-angle view over the small driveway of an old townhouse: a taxi with its roof sign lit waits at the gate, a woman with a short dark bob haircut and a patterned silk scarf around her neck walks out of the front door, pulling on a long dark coat while walking towards the taxi. Low resolution, noise, fisheye distortion, CCTV look. Face not recognisable, no timestamp, no readable text, no licence plate, no logos.'
        ),
    },
    "f_wiese": {
        "aspect_ratio": "3:4",
        "prompt": (
            'Cinematic night photograph of a wide snowy meadow at the edge of a Bavarian old town by the river Isar, in the distance the warm lights and wooden stalls of a Christmas market, the silhouette of a tall brick church tower against the dark blue sky. A few bare trees, footprints in the snow, a lonely street lamp. Quiet, tense thriller mood, 35mm. No people, no readable text, no logos.'
        ),
    },
    "f_uebergabe": {
        "aspect_ratio": "3:4",
        "prompt": (
            "Cinematic night photograph on a snowy meadow, Christmas market lights blurred in the background: a woman in a long dark grey wool coat with the hood up, seen from behind, stretches out a gloved hand towards a grey-haired man in an elegant dark overcoat who holds a small antique wooden casket with iron fittings. Tense moment, breath visible in the cold air, shallow depth of field. Woman's face not visible, no readable text, no logos."
        ),
    },
    "f_zugriff": {
        "aspect_ratio": "3:4",
        "prompt": (
            'Cinematic night photograph on a snowy meadow: plain-clothes police officers in dark jackets step in from both sides with flashlights, one holds up a police badge, surrounding a woman in a long dark hooded wool coat seen from behind, a small antique wooden casket held safely by a man in the background. Blue flashing light reflected on the snow from out of frame, Christmas market lights in the distance, dramatic thriller mood, motion blur. Faces not recognisable, no readable text, no logos.'
        ),
    },
    "f_beweis": {
        "aspect_ratio": "4:3",
        "prompt": (
            "Forensic evidence photograph: a pair of women's black leather gloves inside a transparent police evidence bag, lying in the open boot of a dark car next to a folded yellowed handwritten inventory list. Flashlight beam from above, night, dark background, documentary style, shallow depth of field. Handwriting illegible, no readable text, no licence plate, no logos."
        ),
    },
}


def erzeuge(name: str, motiv: dict, key: str, ziel: Path) -> None:
    print(f"→ {name}: {VARIANTEN} Varianten werden erzeugt …")
    antwort = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={
            "model": MODEL,
            "prompt": motiv["prompt"],
            "n": VARIANTEN,
            "aspect_ratio": motiv["aspect_ratio"],
            "resolution": AUFLOESUNG,
            "quality": QUALITAET,
            "response_format": "b64_json",
        },
        timeout=180,
    )
    if antwort.status_code != 200:
        print(f"  Fehler {antwort.status_code}: {antwort.text[:500]}")
        return
    daten = antwort.json()
    stempel = time.strftime("%Y%m%d-%H%M%S")
    for i, bild in enumerate(daten.get("data", []), start=1):
        roh = bild.get("b64_json")
        if not roh:
            continue
        endung = "jpg" if "jpeg" in (bild.get("mime_type") or "") else "png"
        datei = ziel / f"{name}_{stempel}_{i}.{endung}"
        datei.write_bytes(base64.b64decode(roh))
        print(f"  gespeichert: {datei.name}")
    kosten = (daten.get("usage") or {}).get("cost_in_usd_ticks")
    if kosten is not None:
        print(f"  Kosten laut API: {kosten} Ticks")


def main() -> None:
    key = os.environ.get("XAI_API_KEY")
    if not key:
        sys.exit("XAI_API_KEY ist nicht gesetzt. Siehe Anleitung oben in der Datei.")
    auswahl = sys.argv[1:] or list(MOTIVE)
    unbekannt = [m for m in auswahl if m not in MOTIVE]
    if unbekannt:
        sys.exit(f"Unbekanntes Motiv: {', '.join(unbekannt)}. Möglich: {', '.join(MOTIVE)}")
    ziel = Path(__file__).with_name("tatort_bilder")
    ziel.mkdir(exist_ok=True)
    for name in auswahl:
        erzeuge(name, MOTIVE[name], key, ziel)
    print(f"Fertig. Bilder im Ordner: {ziel}")


if __name__ == "__main__":
    main()
