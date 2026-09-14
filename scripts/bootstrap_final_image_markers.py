#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUESTS = {
    "content/renovatie-plannen/body.html": "renovatie-plannen-roadmap",
    "content/renovatie-plannen/renovatiekosten/body.html": "renovatiekosten-cost-structure",
    "content/renovatie-plannen/renovatie-budget/body.html": "renovatie-budget-reserve",
    "content/renovatie-plannen/renovatievergunning/body.html": "renovatievergunning-decision-flow",
    "content/renovatie-plannen/subsidies-renovatie/body.html": "subsidies-renovatie-aid-map",
    "content/renovatie-plannen/rendement-renovatie/body.html": "rendement-renovatie-value-matrix",
    "content/verduurzamen/body.html": "verduurzamen-layers",
    "content/verduurzamen/energie-besparen/body.html": "energie-besparen-hierarchy",
    "content/problemen-oplossen/body.html": "problemen-oplossen-diagnostic-flow",
    "content/vakman-en-offertes/aannemer-kiezen/body.html": "aannemer-kiezen-context",
    "content/vakman-en-offertes/offerte-controleren/body.html": "offerte-controleren-checklist",
    "content/vakman-en-offertes/zelf-doen-of-uitbesteden/body.html": "zelf-doen-of-uitbesteden-matrix",
    "content/doe-het-zelf/traprenovatie-zelf-doen/body.html": "traprenovatie-diy-context",
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
    print(f"Final image markers added: {changed}")


if __name__ == "__main__":
    main()
