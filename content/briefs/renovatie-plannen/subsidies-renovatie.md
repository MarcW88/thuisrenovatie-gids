# Brief v2 — Renovatiesubsidies

- Route: `/renovatie-plannen/subsidies-renovatie/`
- Status: QA_COMPLETE
- Market: Netherlands / nl-NL
- Primary queries: `subsidie verbouwing 2026`, `renovatie subsidie 2026`, `ISDE 2026`
- Reader task: identify the current national subsidy route, understand combination rules and preserve eligibility through execution and application.
- Decision: `DEEP_REWRITE`
- Last researched: 2026-09-13

## Page role

This page owns the general subsidy decision and application workflow for homeowners. It should not become a giant static tariff table and should not choose technical measures for the reader.

## Required structure

- Direct answer: ISDE is the main national homeowner subsidy route for energy-saving renovation measures; local support can exist separately.
- Eligibility route: homeowner/situation → measure → current conditions → meldcode/technical evidence → execution → application.
- Current 2026 measure families: five insulation categories; warmtepomp; zonneboiler; ventilation when combined with isolation; warm-network connection; electric cooking provision in the applicable warm-network situation.
- Explain that exact isolation support depends on material/measure and m²; pumps/boilers depend on the product/system. Use live RVO calculator/registers as source of truth.
- **Combination matrix:** isolation subsidy can double when combined within the applicable 24-month logic with another isolation measure or with warmtepomp, zonneboiler or warm-network connection. Ventilation by itself does **not** double the isolation amount.
- **Ventilation 2026:** one-time €400, only with one or more qualifying isolation measures and subject to RVO product/installation conditions.
- **Evidence gate:** check conditions before commissioning; capture required photos/work evidence; ensure invoice/product details and meldcode/technical documentation are available; apply within current deadline.
- Meldcode nuance: a product absent from a live list may still be submitted with technical documentation where RVO allows this, but subsidy is not guaranteed.
- Distinguish subsidy from financing/loan. Warmtefonds or mortgage financing is not subsidy.
- Monument/VvE/other ownership situations may have different conditions or schemes; route rather than overgeneralise.
- Local schemes: mention only as location-dependent and time-sensitive; never invent availability.

## Evidence register

Primary/current:
- RVO — ISDE decision tree for homeowners.
- RVO — ISDE calculator 2026.
- RVO — live meldcode lists for insulation, glass, ventilation, heat pumps and solar boilers; several registers checked 9–10 September 2026.
- Rijksoverheid — current homeowner sustainability subsidy/financing guidance.

Secondary translation/benchmark:
- Milieu Centraal — 2026 isolation and ventilation subsidy explanations.
- Vereniging Eigen Huis — homeowner-language ISDE 2026 overview.

## Current facts allowed in copy

- RVO lists five insulation categories for homeowners.
- 2026 ventilation: €400 one time when qualifying conditions and isolation combination are met.
- For isolation, the support can double under RVO's combination rule; ventilation alone does not trigger that doubling.
- The 24-month timing is central to combination/application logic and must be checked against the current measure conditions.
- Live meldcode lists are current product-level evidence; absent products may require technical documentation and can still be rejected.

## Facts not to freeze

- Do not reproduce complete per-m² isolation tables or broad product subsidy tables.
- Do not publish a fixed warm-network amount in this pass because current RVO indexed surfaces show inconsistent cached values.
- Do not state a municipality/province subsidy without current location-specific verification.

## Information gain

1. Make the subsidy process a **decision chain**, not a list of measures.
2. Make the **combination rule** explicit enough that homeowners do not assume ventilation doubles isolation support.
3. Treat **evidence collection as part of the renovation workflow**, not post-project administration.
4. Explain the hierarchy of evidence: live RVO rule/product source > current official explainer > secondary guide > old/static blog table.
5. Connect subsidy to budget cautiously: expected support until concrete conditions are satisfied, not guaranteed money.

## Cannibalisation boundaries

- `/subsidies-renovatie/`: eligibility/application logic.
- `/renovatie-budget/`: financial allocation and cash control.
- `/verduurzamen/*`: technical measure selection.
- `/renovatiekosten/`: gross market costs.

## GEO / style

- Direct answer first.
- Atomic definitions and current-source dates near volatile facts.
- One compact combination table is useful; do not add artificial FAQ blocks.
- Practical, exact Dutch; avoid bureaucratic paraphrase where plain language works.

## QA completion

- Research matrix persisted.
- Conflicting warm-network amount identified and excluded.
- All MUST items handed to production.
- Eligible for production while global indexation remains disabled.