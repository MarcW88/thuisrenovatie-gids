#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUESTS = {
    "content/verduurzamen/ventilatie/body.html": "ventilatie-luchtstroom",
    "content/problemen-oplossen/opstijgend-vocht/body.html": "opstijgend-vocht-bronnen",
    "content/problemen-oplossen/vocht-in-muren/body.html": "vocht-in-muren-bronnen",
    "content/problemen-oplossen/funderingsproblemen/body.html": "funderingsproblemen-signalen",
    "content/doe-het-zelf/zonnepanelen-zelf-plaatsen/body.html": "zonnepanelen-diy-veiligheidsgrenzen",
    "content/doe-het-zelf/warmtepomp-zelf-plaatsen/body.html": "warmtepomp-diy-veiligheidsgrenzen",
    "content/renovatie-plannen/complete-renovatie/body.html": "complete-renovatie-context",
    "content/verduurzamen/cv-ketel/body.html": "cv-ketel-context",
    "content/verduurzamen/dubbel-glas/body.html": "dubbel-glas-context",
    "content/vakman-en-offertes/vakman-kiezen/body.html": "vakman-kiezen-context",
}
LEAD = re.compile(r'(<p class="content-lead">.*?</p>)', re.DOTALL)

def main() -> None:
    changed = 0
    for relative, request_id in REQUESTS.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        marker = f"<!-- EDITORIAL_IMAGE:{request_id} -->"
        if marker in text:
            continue
        match = LEAD.search(text)
        if not match:
            raise RuntimeError(f"No content-lead found in {relative}")
        text = text[:match.end()] + f"\n\n      {marker}" + text[match.end():]
        path.write_text(text, encoding="utf-8")
        changed += 1
        print(f"Added {marker} to {relative}")
    print(f"Batch 2 image markers added: {changed}")

if __name__ == "__main__":
    main()
