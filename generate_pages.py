from pathlib import Path
from html import escape
import json

R = Path(__file__).parent
CONTENT_ROOT = R / "content"

SITE = json.loads((CONTENT_ROOT / "site.json").read_text(encoding="utf-8"))
SITE_URL = SITE["base_url"].rstrip("/")
SITE_NAME = SITE["site_name"]
SITE_LANGUAGE = SITE.get("language", "nl-NL")
INDEXING_ENABLED = bool(SITE.get("indexing_enabled", False))
ROBOTS_DIRECTIVE = "index,follow" if INDEXING_ENABLED else "noindex,follow"

META = {}
for meta_file in sorted(CONTENT_ROOT.glob("meta*.json")):
    META.update(json.loads(meta_file.read_text(encoding="utf-8")))

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
    "doe-het-zelf": [
        "zonnepanelen-zelf-plaatsen", "traprenovatie-zelf-doen",
        "warmtepomp-zelf-plaatsen",
    ],
}

LABEL = {
    "renovatie-plannen": "Renovatie plannen",
    "renovatie-budget": "Renovatiebudget",
    "renovatieprojecten": "Renovatieprojecten",
    "verduurzamen": "Verduurzamen",
    "problemen-oplossen": "Problemen oplossen",
    "vakman-en-offertes": "Vakman & offertes",
    "doe-het-zelf": "Doe het zelf",
}


def name(slug):
    return LABEL.get(slug, slug.replace("-", " ").capitalize())


def all_routes():
    routes = []
    for category, kids in ROUTES.items():
        routes.append(category)
        routes.extend(f"{category}/{child}" for child in kids)
    return routes


def canonical_url(route):
    return f"{SITE_URL}/{route.strip('/')}/"


def route_body(route):
    content_file = CONTENT_ROOT / route / "body.html"
    if content_file.exists():
        return content_file.read_text(encoding="utf-8"), "content-page"

    skeleton = '<section class="blank" aria-label="Lege contentruimte"><div class="container"><div class="skeleton"><div><i></i><i></i><i></i><b></b></div><aside><i></i><i></i><b></b></aside></div></div></section>'
    return skeleton, "empty"


def structured_data(route, title, description):
    canonical = canonical_url(route)
    parts = route.split("/")
    breadcrumb_items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": f"{SITE_URL}/",
        }
    ]
    path = ""
    for position, part in enumerate(parts, start=2):
        path += f"/{part}"
        breadcrumb_items.append(
            {
                "@type": "ListItem",
                "position": position,
                "name": name(part),
                "item": f"{SITE_URL}{path}/",
            }
        )

    graph = [
        {
            "@type": "WebPage",
            "@id": f"{canonical}#webpage",
            "url": canonical,
            "name": title,
            "inLanguage": SITE_LANGUAGE,
            "isPartOf": {"@id": f"{SITE_URL}/#website"},
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{canonical}#breadcrumb",
            "itemListElement": breadcrumb_items,
        },
    ]
    if description:
        graph[0]["description"] = description

    return json.dumps(
        {"@context": "https://schema.org", "@graph": graph},
        ensure_ascii=False,
        separators=(",", ":"),
    )


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
    title = route_meta.get("title", f"{h1} | {SITE_NAME}")
    description = route_meta.get("description")
    canonical = canonical_url(route)
    description_tag = (
        f'<meta name="description" content="{escape(description, quote=True)}">'
        if description else ""
    )
    og_description_tag = (
        f'<meta property="og:description" content="{escape(description, quote=True)}">'
        if description else ""
    )
    schema = structured_data(route, title, description)
    body, main_class = route_body(route)
    content_style_tag = (
        '<link rel="stylesheet" href="/css/content.css">'
        if main_class == "content-page" else ""
    )

    return f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="{ROBOTS_DIRECTIVE}"><meta name="theme-color" content="#24483D"><title>{escape(title)}</title>{description_tag}<link rel="canonical" href="{canonical}"><meta property="og:locale" content="nl_NL"><meta property="og:type" content="website"><meta property="og:site_name" content="{escape(SITE_NAME, quote=True)}"><meta property="og:title" content="{escape(title, quote=True)}">{og_description_tag}<meta property="og:url" content="{canonical}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="/css/style.css">{content_style_tag}<script type="application/ld+json">{schema}</script><script src="/js/site.js" defer></script></head><body><header class="site-header"><div class="utility"><div class="container utility-inner"><span>Onafhankelijke renovatiekeuzes</span><a href="/vakman-en-offertes/offertes-vergelijken/">Zo werkt vergelijken ↗</a></div></div><nav class="container nav"><a class="brand" href="/"><span class="brand-mark"><i></i></span><span>Thuisrenovatie<small>Gids</small></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span><em>Menu</em></button><div class="nav-links" id="nav-links"><a href="/renovatie-plannen/">Renovatie plannen</a><a href="/renovatieprojecten/">Projecten</a><a href="/verduurzamen/">Verduurzamen</a><a href="/problemen-oplossen/">Problemen oplossen</a><a href="/vakman-en-offertes/">Vakman vinden</a></div><a class="button small" href="/vakman-en-offertes/offertes-vergelijken/">Vergelijk vakmensen ↗</a></nav></header><main class="{main_class}"><section class="page-head"><div class="container"><div class="breadcrumbs">{breadcrumbs}</div><h1>{escape(h1)}</h1></div></section>{body}</main><footer class="footer"><div class="container footer-grid"><a class="brand footer-brand" href="/"><span class="brand-mark"><i></i></span><span>Thuisrenovatie<small>Gids</small></span></a><div><h4>Plannen</h4><a href="/renovatie-plannen/">Renovatie plannen</a><a href="/renovatieprojecten/">Renovatieprojecten</a></div><div><h4>Verbeteren</h4><a href="/verduurzamen/">Verduurzamen</a><a href="/problemen-oplossen/">Problemen oplossen</a></div><div><h4>Uitvoeren</h4><a href="/vakman-en-offertes/">Vakman & offertes</a><a href="/doe-het-zelf/">Doe het zelf</a></div></div><div class="container bottom">© 2026 {escape(SITE_NAME)} <span>Onafhankelijk beslissen. Beter renoveren.</span></div></footer></body></html>'''


def write_sitemap(routes):
    urls = [f"{SITE_URL}/"] + [canonical_url(route) for route in routes]
    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    xml.extend(f"  <url><loc>{escape(url)}</loc></url>" for url in urls)
    xml.append("</urlset>")
    (R / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")


def write_robots():
    content = (
        "# Crawling blijft toegestaan zodat zoekmachines de noindex-directive kunnen zien.\n"
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_URL}/sitemap.xml\n"
    )
    (R / "robots.txt").write_text(content, encoding="utf-8")


routes = all_routes()
for route in routes:
    destination = R / route / "index.html"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page(route), encoding="utf-8")

write_sitemap(routes)
write_robots()

print(
    "Generated",
    len(routes),
    "routes + sitemap.xml + robots.txt with",
    ROBOTS_DIRECTIVE,
)
