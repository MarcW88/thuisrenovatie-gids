#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REQUESTS = {
    "content/renovatie-plannen/renovatie-volgorde/body.html": "renovatie-volgorde-visual",
    "content/renovatie-plannen/renovatiefasen/body.html": "renovatiefasen-roadmap",
    "content/renovatieprojecten/keuken-renovatie/body.html": "keuken-renovatie-context",
    "content/renovatieprojecten/aanbouw/body.html": "aanbouw-context",
    "content/renovatieprojecten/fundering/body.html": "fundering-proces",
    "content/renovatieprojecten/ramen-en-glas/body.html": "ramen-en-glas-context",
    "content/verduurzamen/isolatie/dakisolatie/body.html": "dakisolatie-context",
    "content/verduurzamen/isolatie/vloerisolatie/body.html": "vloerisolatie-context",
    "content/verduurzamen/isolatie/gevelisolatie/body.html": "gevelisolatie-context",
    "content/verduurzamen/zonnepanelen/body.html": "zonnepanelen-context",
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
        insertion = f"\n\n      {marker}"
        text = text[: match.end()] + insertion + text[match.end() :]
        path.write_text(text, encoding="utf-8")
        changed += 1
        print(f"Added {marker} to {relative}")
    print(f"P0 image markers added: {changed}")


if __name__ == "__main__":
    main()
