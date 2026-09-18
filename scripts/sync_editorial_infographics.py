#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ITEMS = {
    "energie-besparen-hierarchy": ("verduurzamen/energie-besparen", "Hiërarchie van energiebesparing van instellingen tot duurzame opwekking"),
    "fundering-proces": ("renovatieprojecten/fundering", "Proces van funderingsonderzoek via offertes naar uitvoering en controle"),
    "funderingsproblemen-signalen": ("problemen-oplossen/funderingsproblemen", "Overzicht van signalen die nader funderingsonderzoek kunnen vragen"),
    "offerte-controleren-checklist": ("vakman-en-offertes/offerte-controleren", "Checklist voor het controleren van een renovatieofferte"),
    "opstijgend-vocht-bronnen": ("problemen-oplossen/opstijgend-vocht", "Overzicht van verschillende mogelijke vochtbronnen rond een muur"),
    "problemen-oplossen-diagnostic-flow": ("problemen-oplossen", "Diagnostische flow van signaal en observatie naar onderzoek en interventie"),
    "rendement-renovatie-value-matrix": ("renovatie-plannen/rendement-renovatie", "Matrix van woningwaarde, energie, comfort en onderhoud bij renovatierendement"),
    "renovatie-budget-reserve": ("renovatie-plannen/renovatie-budget", "Visuele verdeling van een renovatiebudget inclusief reserve"),
    "renovatie-plannen-roadmap": ("renovatie-plannen", "Roadmap voor renovatieplanning van scope tot waarde"),
    "renovatie-volgorde-visual": ("renovatie-plannen/renovatie-volgorde", "Renovatievolgorde van blokkades en sloop tot testen en opleveren"),
    "renovatiefasen-roadmap": ("renovatie-plannen/renovatiefasen", "Roadmap met zeven fasen van een renovatieproject"),
    "renovatiekosten-cost-structure": ("renovatie-plannen/renovatiekosten", "Overzicht van verschillende kostensoorten bij een renovatie"),
    "renovatievergunning-decision-flow": ("renovatie-plannen/renovatievergunning", "Beslisflow om vergunningen en meldingen vooraf te controleren"),
    "subsidies-renovatie-aid-map": ("renovatie-plannen/subsidies-renovatie", "Route om renovatiemaatregelen op mogelijke steun te controleren"),
    "ventilatie-luchtstroom": ("verduurzamen/ventilatie", "Schematische luchtstroom van verblijfsruimtes naar natte ruimtes"),
    "verduurzamen-layers": ("verduurzamen", "Vier samenhangende systemen voor woningverduurzaming"),
    "vocht-in-muren-bronnen": ("problemen-oplossen/vocht-in-muren", "Overzicht van meerdere mogelijke oorzaken van vocht in muren"),
    "warmtepomp-diy-veiligheidsgrenzen": ("doe-het-zelf/warmtepomp-zelf-plaatsen", "Professionele veiligheidsdomeinen rond een warmtepomp"),
    "zelf-doen-of-uitbesteden-matrix": ("vakman-en-offertes/zelf-doen-of-uitbesteden", "Beslismatrix voor zelf doen of renovatiewerk uitbesteden"),
    "zonnepanelen-diy-veiligheidsgrenzen": ("doe-het-zelf/zonnepanelen-zelf-plaatsen", "Veiligheidsgrenzen bij zonnepanelen op het dak en de elektrische installatie"),
}


def figure_markup(image_id: str, alt: str) -> str:
    return (
        f'<figure class="editorial-media editorial-infographic" data-editorial-infographic="{image_id}">\n'
        f'  <img src="/assets/infographics/{image_id}.svg" alt="{alt}" width="1024" height="672" loading="lazy" decoding="async">\n'
        f'</figure>'
    )


def replace_markup(text: str, image_id: str, alt: str) -> tuple[str, bool]:
    figure = figure_markup(image_id, alt)
    if f'data-editorial-infographic="{image_id}"' in text:
        pattern = re.compile(
            rf'<figure class="editorial-media editorial-infographic" data-editorial-infographic="{re.escape(image_id)}">.*?</figure>',
            re.S,
        )
        updated = pattern.sub(figure, text, count=1)
        return updated, updated != text

    patterns = [
        re.compile(
            rf'<section class="editorial-visual" data-editorial-visual="{re.escape(image_id)}".*?</section>',
            re.S,
        ),
        re.compile(
            rf'<figure class="editorial-media" data-generated-image="{re.escape(image_id)}">.*?</figure>',
            re.S,
        ),
    ]
    for pattern in patterns:
        if pattern.search(text):
            return pattern.sub(figure, text, count=1), True

    marker = f'<!-- EDITORIAL_IMAGE:{image_id} -->'
    if marker in text:
        return text.replace(marker, figure, 1), True

    raise SystemExit(f"Could not find infographic slot for {image_id}")


def main() -> None:
    changed = 0
    for image_id, (route, alt) in ITEMS.items():
        body = ROOT / "content" / route / "body.html"
        text = body.read_text(encoding="utf-8")
        updated, did_change = replace_markup(text, image_id, alt)
        if did_change:
            body.write_text(updated, encoding="utf-8")
            changed += 1
    print(f"Synchronized {len(ITEMS)} infographic slots; changed {changed} source files.")


if __name__ == "__main__":
    main()
