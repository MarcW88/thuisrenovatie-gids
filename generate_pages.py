from pathlib import Path
from html import escape

R = Path(__file__).parent
CONTENT_ROOT = R / "content"

ROUTES = {
    "renovatie-plannen": [
        "huis-renoveren", "renovatie-volgorde", "renovatiefasen",
        "complete-renovatie", "renovatiekosten", "renovatie-budget",
        "renovatievergunning", "subsidies-renovatie", "rendement-renovatie",
    ],
    "renovatieprojecten": [
        "badkamer-renovatie", "keuken-renovatie", "aanbouw", "fundering",
        "ramen-en-glas",
    ],
    "verduurzamen": [
        "isolatie", "isolatie/dakisolatie", "isolatie/vloerisolatie",
        "isolatie/gevelisolatie", "zonnepanelen", "warmtepomp", "cv-ketel",
        "ventilatie", "dubbel-glas", "energie-besparen",
    ],
    "problemen-oplossen": [
        "vochtproblemen", "opstijgend-vocht", "vocht-in-muren",
        "funderingsproblemen",
    ],
    "vakman-en-offertes": [
        "vakman-kiezen", "aannemer-kiezen", "offertes-vergelijken",
        "offerte-controleren", "zelf-doen-of-uitbesteden",
    ],
    "doe-het-zelf": [],
}

LABEL = {
    "renovatie-plannen": "Renovatie plannen",
    "renovatieprojecten": "Renovatieprojecten",
    "verduurzamen": "Verduurzamen",
    "problemen-oplossen": "Problemen oplossen",
    "vakman-en-offertes": "Vakman & offertes",
    "doe-het-zelf": "Doe het zelf",
}

META = {
    "renovatie-plannen": {
        "title": "Renovatie plannen: van idee naar uitvoerbaar plan | Thuisrenovatie Gids",
        "description": "Plan je renovatie op basis van beslissingen, afhankelijkheden, budget en regels. Start met de juiste volgorde en voorkom dubbel werk.",
    },
    "renovatie-plannen/huis-renoveren": {
        "title": "Huis renoveren: stappenplan voor een slimme renovatie | Thuisrenovatie Gids",
        "description": "Je huis renoveren? Ontdek waar je begint, welke beslissingen eerst komen en hoe je scope, budget, vergunningen en uitvoering logisch plant.",
    },
}


def name(slug):
    return LABEL.get(slug, slug.replace("-", " ").capitalize())


def route_body(route):
    content_file = CONTENT_ROOT / route / "body.html"
    if content_file.exists():
        return content_file.read_text(encoding="utf-8"), "content-page"

    skeleton = """<section class=\"blank\" aria-label=\"Lege contentruimte\"><div class=\"container\"><div class=\"skeleton\"><div><i></i><i></i><i></i><b></b></div><aside><i></i><i></i><b></b></aside></div></div></section>"""
    return skeleton, "empty"


def page(route):
    parts = route.split("/")
    h1 = name(parts[-1])
    trail = ['<a href="/">Home</a>']
    path = ""
    for part in parts[:-1]:
        path += f"/{part}"
        trail.append(f'<a href="{path}/">{escape(name(part))}</a>')
    trail.append(escape(h1))
    breadcrumbs = " / ".join(trail)

    route_meta = META.get(route, {})
    title = route_meta.get("title", f"{h1} | Thuisrenovatie Gids")
    description = route_meta.get("description")
    description_tag = (
        f'<meta name="description" content="{escape(description, quote=True)}">'
        if description else ""
    )
    body, main_class = route_body(route)

    return f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)}</title>{description_tag}<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="/css/style.css"><script src="/js/site.js" defer></script></head><body><header class="site-header"><div class="utility"><div class="container utility-inner"><span>Onafhankelijke renovatiekeuzes</span><a href="/vakman-en-offertes/offertes-vergelijken/">Zo werkt vergelijken ↗</a></div></div><nav class="container nav"><a class="brand" href="/"><span class="brand-mark"><i></i></span><span>Thuisrenovatie<small>Gids</small></span></a><button class="menu-toggle" aria-expanded="false"><span></span><span></span><span></span><em>Menu</em></button><div class="nav-links"><a href="/renovatie-plannen/">Renovatie plannen</a><a href="/renovatieprojecten/">Projecten</a><a href="/verduurzamen/">Verduurzamen</a><a href="/problemen-oplossen/">Problemen oplossen</a><a href="/vakman-en-offertes/">Vakman vinden</a></div><a class="button small" href="/vakman-en-offertes/offertes-vergelijken/">Vergelijk vakmensen ↗</a></nav></header><main class="{main_class}"><section class="page-head"><div class="container"><div class="breadcrumbs">{breadcrumbs}</div><h1>{escape(h1)}</h1></div></section>{body}</main><footer class="footer"><div class="container footer-grid"><a class="brand footer-brand" href="/"><span class="brand-mark"><i></i></span><span>Thuisrenovatie<small>Gids</small></span></a><div><h4>Plannen</h4><a href="/renovatie-plannen/">Renovatie plannen</a><a href="/renovatieprojecten/">Renovatieprojecten</a></div><div><h4>Verbeteren</h4><a href="/verduurzamen/">Verduurzamen</a><a href="/problemen-oplossen/">Problemen oplossen</a></div><div><h4>Uitvoeren</h4><a href="/vakman-en-offertes/">Vakman & offertes</a><a href="/doe-het-zelf/">Doe het zelf</a></div></div><div class="container bottom">© 2026 Thuisrenovatie Gids <span>Onafhankelijk beslissen. Beter renoveren.</span></div></footer></body></html>'''


for category, kids in ROUTES.items():
    routes = [category] + [f"{category}/{child}" for child in kids]
    for route in routes:
        destination = R / route / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(page(route), encoding="utf-8")

print("Generated", sum(1 + len(children) for children in ROUTES.values()), "routes")
