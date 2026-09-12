---
name: seo-keyword
description: Bepaal primaire zoekvraag, ondersteunende cluster en zoekintentie voor een pagina.
provenance: upstream
upstream: https://github.com/rampstackco/claude-skills/tree/main/skills/seo-keyword
---

# SEO Keyword

Vendored adapter van de upstream `seo-keyword` skill.

Gebruik deze skill vóór het schrijven. Bepaal de dominante zoekintentie, relevante varianten en de rol van de pagina binnen het cluster. Kies geen keyword op basis van volume alleen: intentie, beslisfase en overlap met bestaande routes zijn leidend.

Voor Thuisrenovatie Gids:
- koppel de zoekvraag aan één van PLAN, PROJECT, SUSTAINABILITY, DIY, TROUBLESHOOTING of LEAD;
- signaleer kannibalisatie met bestaande routes;
- scheid informatieve vragen van vakman-/offerte-intentie;
- verzin geen volumes of rankings wanneer er geen data beschikbaar is.

Output: primaire zoekvraag, intentie, ondersteunende termen, pagina-rol, overlaprisico en eventuele datagaten.