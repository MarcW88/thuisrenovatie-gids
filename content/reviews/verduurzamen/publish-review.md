# PUBLISH_REVIEW — `/verduurzamen/`

- Reviewed: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`
- Result: **PASS — READY_FOR_HUMAN_VALIDATION**
- Indexing decision: unchanged; page remains `noindex,follow`

## 1. Research gate

**PASS**

- current Dutch SERP inspected for broad `woning verduurzamen / waar beginnen / welke maatregel eerst / volgorde` intent;
- strongest independent source inspected: Milieu Centraal;
- competitor patterns inspected across current August/September 2026 results;
- prewrite research persisted at `content/research/verduurzamen/serp-coverage.md`;
- central SERP conflict resolved: many competitors impose a linear sequence, while Milieu Centraal explicitly states that the order is not fixed.

## 2. Intent / ownership gate

**PASS**

Hub ownership is now clear:

- current house state;
- blockers before investment;
- dependencies between shell, ventilation, heating and generation;
- natural renovation moments;
- route to the correct child page.

The hub no longer tries to own detailed isolation, glazing, ventilation, heat-pump, boiler or solar decisions.

### Cannibalisation — `/verduurzamen/energie-besparen/`

**PASS with follow-up noted for child rewrite.**

The hub now owns the investment/renovation route. `energie-besparen` is explicitly positioned as the route for reducing current energy use and prioritising measures when no major renovation project is active.

The existing child content itself still requires its own future V2 rewrite, but the hub no longer duplicates the child's old four-level sequence.

## 3. Brief adherence

**PASS**

Brief status: `QA_COMPLETE`.

All required assets are present:

- no fixed universal sequence;
- `woning-nulmeting`;
- blockers before measures;
- isolation/ventilation dependency;
- heating dependency on demand/emission/future plan;
- solar dependency on roof/future electricity demand;
- natural renovation moments;
- unique routing to child intents;
- boundary with `energie-besparen`;
- no universal price/savings/subsidy/ROI ranking.

## 4. Post-write gap gate

**PASS**

- MUST covered: 10/10
- MUST partial: 0
- MUST missing: 0

See `content/reviews/verduurzamen/post-write-gap-check.md`.

## 5. Factuality / freshness

**PASS**

See `content/reviews/verduurzamen/fact-check.md`.

Verified against current Milieu Centraal sources:

- sequence not fixed;
- logical renovation moments can be entry points;
- improved airtightness increases the importance of controlled ventilation;
- heat-pump choice depends on house readiness and heat emission;
- future electricity demand is relevant when planning solar;
- external shading is part of the energy-efficient-home basis.

No universal cost, saving, ROI or subsidy amount is published on this hub.

## 6. Information gain

**PASS**

The page adds decision support that the dominant linear SERP guides mostly lack:

1. `volgende-blokkade-model`;
2. house-state baseline instead of product-first choice;
3. natural renovation moments;
4. startsituation router;
5. no-regret gate before difficult-to-reverse purchases.

## 7. GEO / extractability

**PASS**

Standalone answers are available for:

- where to start with home sustainability;
- whether there is a fixed order;
- which blockers come before measures;
- when to combine measures with renovation moments;
- what to know before a heat pump or solar project;
- which child route matches a given startsituation.

Facts are stated atomically and the main current-source block is adjacent to the claim it supports.

## 8. Voice / anti-slop

**PASS**

- practical, direct Dutch;
- no generic sustainability marketing language;
- no fake urgency;
- no forced conclusion repeating the page;
- tables are used for actual decision comparisons;
- sequence language is deliberately bounded instead of overstated.

## 9. On-page SEO

**PASS**

Title:

`Woning verduurzamen: waar begin je? | Thuisrenovatie Gids`

Meta:

`Woning verduurzamen? Kies je volgende maatregel vanuit de staat van je huis, technische blokkades en geplande renovaties. Geen vaste volgorde nodig.`

- primary broad intent appears early;
- H1 remains `Verduurzamen` and is consistent with route role;
- descriptive H2 structure;
- rich internal routing to the full child set;
- canonical URL unchanged.

## 10. Technical gate

**PASS**

Rendered HTML checked:

- canonical: `https://thuisrenovatie-gids.nl/verduurzamen/`
- robots: `noindex,follow`
- WebPage + BreadcrumbList JSON-LD present;
- critical body content is rendered in HTML;
- generated metadata matches source metadata.

Repository CI on pre-review head:

- `Validate renovation structure`: SUCCESS
- `Validate editorial engine`: SUCCESS

## Final decision

**PASS — READY_FOR_HUMAN_VALIDATION**

This status does not change indexing. Human validation remains a separate gate before any future `indexing_enabled` change.
