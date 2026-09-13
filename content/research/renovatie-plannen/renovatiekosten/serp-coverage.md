# SERP coverage — Renovatiekosten

- Route: `/renovatie-plannen/renovatiekosten/`
- Research date: 2026-09-13
- Decision: `DEEP_REWRITE`
- Primary queries: `renovatiekosten`, `huis renoveren kosten`, `verbouwing kosten 2026`, `renovatie kosten per m2`

## Search intent

Dominant intent is current cost orientation before a homeowner has project-specific quotes. The SERP mixes price tables by room/project, whole-house or €/m² estimates, cost drivers and calculators. The useful answer is not one national average but a set of current benchmarks whose scope is explicit.

## SERP observations

- Vereniging Eigen Huis publishes 2026 prices for five common renovation projects and explicitly states that its figures are minimum guideline prices, generally including VAT, materials and labour, with regional/location/market extras possible.
- Commercial guides often show much higher totals for the same label because their scope differs. For example, bathroom and kitchen ranges vary depending on whether demolition, disposal, installation changes and finish level are included.
- €/m² is common in the SERP but is unreliable across mixed scopes. A bathroom m² contains far more installation work than a bedroom m²; a casco extension price excludes major items that an 'afgewerkt' extension range may include.
- Freshness matters. CBS July 2026 input-price data for new housing construction was about 5.1% higher year-on-year; this is not a renovation-price index, but it confirms that undated old cost tables should not be treated as current market prices.

## MUST coverage

| Need | Current page | Required action |
|---|---|---|
| Current 2026 benchmark prices | COVERED | Keep, expand to all five common VEH project categories. |
| Source/date next to prices | COVERED | Keep and make methodology explicit. |
| Explain what figures include/exclude | PARTIAL | Make this a first-class table column and section. |
| Kitchen benchmark | COVERED | Keep segmented scope; avoid collapsing everything into one misleading range. |
| Bathroom benchmark | COVERED | Keep and state demolition exclusion. |
| Extension benchmark | COVERED | Keep and state casco/exclusions prominently. |
| Attic benchmark | COVERED | Keep and explain what the scenarios contain. |
| Dormer benchmark | MISSING | Add current 2026 VEH figures. |
| Why price sources disagree | PARTIAL | Add scope-normalisation explanation with an example. |
| Main cost drivers | COVERED | Reorganise into decision-relevant drivers. |
| How to turn benchmarks into a project estimate | COVERED but generic | Build a repeatable estimation method. |
| €/m² limitations | COVERED | Strengthen with cases where it is useful vs misleading. |
| Distinguish cost estimate from budget control | PARTIAL | Route budget allocation/reserve to `/renovatie-budget/`. |

## SHOULD coverage

- Distinguish product/finish cost from enabling works (demolition, electrical, plumbing, structural, access, waste, temporary measures).
- Explain that 'incl. montage' does not mean every surrounding construction task is included.
- Show why one quote can be cheaper simply because scope is missing.
- Add a price-freshness rule: always check source year and scope before carrying forward a range.
- Mention regional/location effects only where supported by source, not as a generic percentage uplift.

## Information gain

1. **Price anatomy:** each benchmark is shown with scope and major exclusions, not only a number.
2. **Scope normalisation test:** compare two prices only after checking demolition, labour, installations, finish level, waste/access and VAT.
3. **Three-layer estimate:** reference price → project-specific extras → uncertainty/reserve handled separately in `renovatie-budget`.
4. **Freshness context:** explain why 2026-labelled/current data matters and cite CBS only as construction-cost trend context, not as a renovation tariff.
5. **No fake whole-house average:** route integrated whole-house scope to `/complete-renovatie/` and keep this page focused on current project cost benchmarks.

## Evidence register

Primary/current:
- Vereniging Eigen Huis — `Wat kost verbouwen?`, price level 2026.
- CBS — input-price index construction costs for new dwellings, updated 28 Aug 2026; July 2026 total +5.1% YoY. Context only, not a renovation quote index.

Secondary SERP context:
- Homedeal 2026 project ranges, useful only to illustrate scope differences.
- Other commercial €/m² guides used for SERP-format analysis, not as primary evidence.

## Cannibalisation boundary

- `renovatiekosten` owns current benchmark prices and cost drivers.
- `renovatie-budget` owns allocation, affordability, contingency and spend control.
- `complete-renovatie` owns whole-house integrated scope, phasing and total-project coordination.
- project pages (`badkamer`, `keuken`, `aanbouw`, etc.) should own detailed project-specific buying/technical decisions.
