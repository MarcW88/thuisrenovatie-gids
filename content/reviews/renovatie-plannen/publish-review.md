# PUBLISH_REVIEW — Renovatie plannen hub

- Route: `/renovatie-plannen/`
- Review date: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`

## Required artifacts

- SERP coverage matrix: PASS
- V2 brief: PASS
- Fact-check: PASS
- Post-write gap check: PASS
- Generated HTML: PASS

## Semantic gates

### Search intent / ownership
PASS. The hub now owns cluster orientation rather than a generic full-project stappenplan.

### Cannibalisation
PASS. It routes to `huis-renoveren`, `renovatiefasen`, `renovatie-volgorde`, `complete-renovatie`, `renovatiekosten`, `renovatie-budget`, `renovatievergunning`, `subsidies-renovatie` and `rendement-renovatie` without recreating their detailed answers.

### Content gap resolution
PASS. Every MUST from the pre-write matrix is COVERED. `MUST = MISSING`: 0. `MUST = PARTIAL`: 0.

### Information gain
PASS. The page adds a nine-question decision map, confusion-pair definitions and a ready-for-offers gate rather than another generic checklist.

### Factuality / freshness
PASS. No volatile price, subsidy, permit threshold or ROI figure is duplicated in the hub. Time-sensitive detail remains on the dedicated child pages.

### GEO usefulness
PASS. The page contains atomic definitions for the main planning distinctions and a one-question/one-owner route map that can be extracted without losing context.

### Brand / writing quality
PASS. Practical, concise and decision-oriented. No artificial FAQ, no generic filler, no repeated full-project step sequence.

### On-page / technical
PASS.
- Title: `Renovatie plannen: keuzes, kosten en volgorde | Thuisrenovatie Gids`
- Canonical: `https://thuisrenovatie-gids.nl/renovatie-plannen/`
- Generated output synchronised with source/meta.
- `noindex,follow` preserved.

### CI
PASS on pre-review head:
- Validate editorial engine
- Validate renovation structure

## Final status

**PASS — READY_FOR_HUMAN_VALIDATION**

Global indexation remains disabled.