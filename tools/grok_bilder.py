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
