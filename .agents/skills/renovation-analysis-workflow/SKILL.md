---
name: renovation-analysis-workflow
description: Sitespecifieke analyse-orkestratie voor renovatie-, probleem-, verduurzamings-, DIY- en leadpagina's.
provenance: custom
---

# Renovation Analysis Workflow

Deze custom skill bevat alleen de sitespecifieke orkestratie voor Thuisrenovatie Gids. De inhoudelijke expertise wordt gedelegeerd aan upstream skills.

## 1. Classificeer de pagina

Bepaal op basis van route en taak:
- `PLAN` → `renovatie-plannen/`
- `PROJECT` → `renovatieprojecten/`
- `SUSTAINABILITY` → `verduurzamen/`
- `DIY` → `doe-het-zelf/`
- `TROUBLESHOOTING` → `problemen-oplossen/`
- `LEAD` → `vakman-en-offertes/`

Bij een onduidelijke route kies je de dominante gebruikersbeslissing en meld je eventuele overlap.

## 2. Delegeer de analyse

Gebruik minimaal:
1. `jtbd-framing` voor de echte gebruikersjob;
2. `seo-keyword` voor intentie en cluster;
3. `seo-content-audit` wanneer er bestaande content is;
4. `information-architecture` voor pagina-rol en interne links;
5. `evidence-based-reviews` voor bewijsniveau van claims;
6. `seo-onpage` en waar relevant `seo-technical`.

Voor `LEAD`: voeg `cro-optimization` toe.

## 3. Domeinchecks

Markeer afzonderlijk:
- prijzen en kostenbandbreedtes;
- premies/subsidies;
- vergunningen en regelgeving;
- technische prestaties en rendement;
- veiligheid en stopcondities;
- markt-/regiocontext;
- claims die een actuele bron nodig hebben.

## 4. Type-specifieke focus

- `PLAN`: volgorde, afhankelijkheden, budgetfactoren, beslismomenten.
- `PROJECT`: opties, voorbereiding, uitvoering, trade-offs, onderhoud.
- `SUSTAINABILITY`: baseline, maatregel, comfort, energie-effect, aannames.
- `DIY`: haalbaarheid, gereedschap, stappen, fouten, veilige grens.
- `TROUBLESHOOTING`: symptomen, veilige diagnosevolgorde, mogelijke oorzaken, professional-escalatie.
- `LEAD`: wanneer uitbesteden, scope, offerte-inhoud, vergelijking, vragen, red flags, CTA.

## Verplicht outputformat

1. Contenttype en route
2. Primaire gebruikersjob
3. Zoekintentie en pagina-rol
4. Wat al goed is / wat ontbreekt
5. Claims die verificatie vereisen
6. Structuuradvies
7. Interne links
8. Conversie/trust (indien relevant)
9. Veiligheidsrisico's
10. Prioriteiten: CRITICAL / IMPORTANT / OPTIONAL

Schrijf nog geen definitieve artikeltekst tenzij de calling task dit expliciet vraagt.