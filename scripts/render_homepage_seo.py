from pathlib import Path
from html import escape
import json
import re

R = Path(__file__).resolve().parents[1]
SITE = json.loads((R / "content" / "site.json").read_text(encoding="utf-8"))

SITE_URL = SITE["base_url"].rstrip("/")
SITE_NAME = SITE["site_name"]
SITE_LANGUAGE = SITE.get("language", "nl-NL")
INDEXING_ENABLED = bool(SITE.get("indexing_enabled", False))
ROBOTS_DIRECTIVE = "index,follow" if INDEXING_ENABLED else "noindex,follow"

HOME = SITE["homepage"]
TITLE = HOME["title"]
DESCRIPTION = HOME["description"]
CANONICAL = f"{SITE_URL}/"

schema = json.dumps(
    {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": f"{SITE_URL}/#organization",
                "name": SITE_NAME,
                "url": CANONICAL,
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": CANONICAL,
                "name": SITE_NAME,
                "inLanguage": SITE_LANGUAGE,
                "publisher": {"@id": f"{SITE_URL}/#organization"},
            },
            {
                "@type": "WebPage",
                "@id": f"{SITE_URL}/#webpage",
                "url": CANONICAL,
                "name": TITLE,
                "description": DESCRIPTION,
                "inLanguage": SITE_LANGUAGE,
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
                "about": {"@id": f"{SITE_URL}/#organization"},
            },
        ],
    },
    ensure_ascii=False,
    separators=(",", ":"),
)

head = f'''<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="{ROBOTS_DIRECTIVE}"><meta name="theme-color" content="#24483D"><title>{escape(TITLE)}</title><meta name="description" content="{escape(DESCRIPTION, quote=True)}"><link rel="canonical" href="{CANONICAL}"><meta property="og:locale" content="nl_NL"><meta property="og:type" content="website"><meta property="og:site_name" content="{escape(SITE_NAME, quote=True)}"><meta property="og:title" content="{escape(TITLE, quote=True)}"><meta property="og:description" content="{escape(DESCRIPTION, quote=True)}"><meta property="og:url" content="{CANONICAL}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="/css/style.css"><script type="application/ld+json">{schema}</script><script src="/js/site.js" defer></script></head>'''

homepage = R / "index.html"
html = homepage.read_text(encoding="utf-8")
updated, count = re.subn(r"<head>.*?</head>", head, html, count=1, flags=re.DOTALL)
if count != 1:
    raise SystemExit("Could not replace homepage <head>")

homepage.write_text(updated, encoding="utf-8")
print("Updated homepage SEO with", ROBOTS_DIRECTIVE)
