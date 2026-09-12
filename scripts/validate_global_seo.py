from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

R = Path(__file__).resolve().parents[1]
SITE = json.loads((R / "content" / "site.json").read_text(encoding="utf-8"))

BASE_URL = SITE["base_url"].rstrip("/")
EXPECTED_ROBOTS = "index,follow" if SITE.get("indexing_enabled", False) else "noindex,follow"
CATEGORY_DIRS = [
    "renovatie-plannen",
    "renovatieprojecten",
    "verduurzamen",
    "problemen-oplossen",
    "vakman-en-offertes",
    "doe-het-zelf",
]

html_files = [R / "index.html"]
for category in CATEGORY_DIRS:
    html_files.extend(sorted((R / category).rglob("index.html")))

errors = []
canonicals = []

for path in html_files:
    html = path.read_text(encoding="utf-8")
    rel = path.relative_to(R)

    route = "" if rel == Path("index.html") else str(rel.parent).replace("\\", "/")
    expected_canonical = f"{BASE_URL}/" if not route else f"{BASE_URL}/{route}/"

    robots_tag = f'<meta name="robots" content="{EXPECTED_ROBOTS}">'
    if robots_tag not in html:
        errors.append(f"{rel}: missing robots directive {EXPECTED_ROBOTS}")

    canonical_tag = f'<link rel="canonical" href="{expected_canonical}">'
    if canonical_tag not in html:
        errors.append(f"{rel}: missing self-canonical {expected_canonical}")
    else:
        canonicals.append(expected_canonical)

    if not re.search(r'<meta name="description" content="[^"]+">', html):
        errors.append(f"{rel}: missing meta description")

    if html.count("<h1") != 1:
        errors.append(f"{rel}: expected exactly one H1")

    if '<script type="application/ld+json">' not in html:
        errors.append(f"{rel}: missing JSON-LD")

    if route and '"BreadcrumbList"' not in html:
        errors.append(f"{rel}: missing BreadcrumbList schema")

    if not route and ('"WebSite"' not in html or '"Organization"' not in html):
        errors.append("index.html: missing WebSite/Organization schema")

    if route and 'class="empty"' in html:
        errors.append(f"{rel}: route is still an empty skeleton")

    if '/vakman-en-offertes/offertes-vergelijken/' not in html:
        errors.append(f"{rel}: missing global comparison CTA")

robots_path = R / "robots.txt"
if not robots_path.exists():
    errors.append("robots.txt: missing")
else:
    robots = robots_path.read_text(encoding="utf-8")
    if re.search(r"(?im)^\s*Disallow:\s*/\s*$", robots):
        errors.append("robots.txt: must not block crawling while pages are noindex")
    if f"Sitemap: {BASE_URL}/sitemap.xml" not in robots:
        errors.append("robots.txt: sitemap reference missing")

sitemap_path = R / "sitemap.xml"
if not sitemap_path.exists():
    errors.append("sitemap.xml: missing")
else:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.parse(sitemap_path).getroot()
    sitemap_urls = [loc.text for loc in root.findall("sm:url/sm:loc", ns)]
    expected_urls = [f"{BASE_URL}/"] + sorted(
        f"{BASE_URL}/{str(path.relative_to(R).parent).replace(chr(92), '/')}/"
        for path in html_files
        if path != R / "index.html"
    )
    if set(sitemap_urls) != set(expected_urls):
        missing = sorted(set(expected_urls) - set(sitemap_urls))
        extra = sorted(set(sitemap_urls) - set(expected_urls))
        if missing:
            errors.append(f"sitemap.xml: missing URLs: {missing}")
        if extra:
            errors.append(f"sitemap.xml: unexpected URLs: {extra}")

if len(canonicals) != len(set(canonicals)):
    errors.append("Duplicate canonical URLs detected")

if errors:
    print("Global SEO validation failed:")
    for error in errors:
        print("-", error)
    raise SystemExit(1)

print(
    f"Validated {len(html_files)} HTML pages: {EXPECTED_ROBOTS}, "
    "self-canonical, descriptions, schema, sitemap, robots and CTA."
)
