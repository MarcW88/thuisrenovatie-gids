# SERP coverage matrix — Renovatie plannen hub

- Workflow version: 2
- Route: `/renovatie-plannen/`
- Market: Netherlands / nl-NL
- Research date: 2026-09-13
- Decision: `DEEP_REWRITE`

## Query set

Primary:
- `renovatie plannen`
- `verbouwing plannen`
- `huis verbouwen plannen`

Variants / sub-intents:
- `waar beginnen met verbouwen`
- `stappenplan verbouwing`
- `verbouwing checklist`
- `renovatie planning maken`
- `renovatie kosten budget vergunning`

## Current SERP evidence

| Source | Format / angle | Strong coverage | Weakness / opportunity |
| --- | --- | --- | --- |
| Vereniging Eigen Huis — Checklist verbouwen | Full-project checklist | wishes, scope, permit, adviser, sustainability, budget, financing, contractor, execution, handover | Strong lifecycle checklist, but the reader must still decide which issue is blocking them now |
| Vereniging Eigen Huis — Maak een plan | Orientation / preparation | current situation, future needs, layout, budget, priorities | Excellent early-stage framing; less useful once the reader already has one concrete planning problem |
| Homedeal — Stappenplan huis verbouwen, 14 Jul 2026 | Linear 7-step guide | goals, budget, offers, permits, planning, execution, handover | Generic linear sequence; overlaps heavily with lifecycle/sequence intents |
| DamTask — Renovatie-planner, updated 29 Jul 2026 | Interactive planning tool | dwelling inputs, works, complexity, order, duration, attention points | Useful personalisation, but claims a relatively fixed sequence and mainly serves execution order |
| Rijksoverheid — Stappenplan bij bouwen en verbouwen | Official regulatory checklist | omgevingsplan, welstand, building rules, permit, neighbours | Authoritative but only owns regulatory preparation |

## Intent ownership

The hub must **not** own a full renovation stappenplan. That would cannibalise:
- `/huis-renoveren/` — where to start and what to investigate/decide first;
- `/renovatiefasen/` — project lifecycle and phase gates;
- `/renovatie-volgorde/` — physical order/dependencies of works.

The hub owns: **orientation across the cluster**. It should help a reader identify the uncertainty that is currently blocking the project and route them to the page that owns that decision.

## Coverage matrix

| Reader need | Current hub | Priority | Owner / action |
| --- | --- | --- | --- |
| Know where to start when the whole project is still vague | COVERED | MUST | Route to `/huis-renoveren/` |
| Distinguish project phase from physical execution order | PARTIAL | MUST | Explain distinction and route to `/renovatiefasen/` vs `/renovatie-volgorde/` |
| Estimate market cost vs build a controllable budget | PARTIAL | MUST | Explain distinction and route to `/renovatiekosten/` vs `/renovatie-budget/` |
| Check permit/regulatory uncertainty early | COVERED | MUST | Route to `/renovatievergunning/`; do not recreate legal framework |
| Recognise when multiple systems make this a complete renovation | COVERED | MUST | Route to `/complete-renovatie/` |
| Handle subsidy as a conditional funding input | PARTIAL | SHOULD | Route to `/subsidies-renovatie/`; no tariff duplication |
| Evaluate whether a project is worth doing | PARTIAL | SHOULD | Route to `/rendement-renovatie/` |
| Understand which question to solve before requesting offers | PARTIAL | MUST | Add explicit readiness / routing logic |
| See all planning pages without scanning generic prose | PARTIAL | MUST | Build a decision map covering every child route |
| Avoid treating planning as one fixed universal sequence | PARTIAL | MUST | State that the next decision depends on what is still uncertain |

## Information-gain opportunities

1. **Decision-router instead of another stappenplan:** route by uncertainty (`scope`, `sequence`, `cost`, `budget`, `rules`, `integration`, `subsidy`, `return`).
2. **Confusion pairs:** explicitly separate:
   - `renovatiefasen` vs `renovatie-volgorde`;
   - `renovatiekosten` vs `renovatiebudget`;
   - `huis-renoveren` vs `complete-renovatie`.
3. **Ready-for-offers gate:** before serious quote comparison, the reader should at minimum know scope, relevant technical unknowns, regulatory blockers and budget ceiling; the detailed mechanics stay on child pages.
4. **Cluster map as GEO asset:** short, atomic descriptions of what each page answers and when to use it.

## GEO / citation opportunities

The hub itself should contain few volatile facts. Its strongest extractable information should be definitional:
- project phases organise decisions and handoffs; execution order organises physical dependencies;
- market cost is not the same as a project budget;
- a broad renovation plan is ready for serious quote comparison only when the scope and the main blockers are sufficiently explicit.

Regulatory claims should link to the dedicated permit page, which in turn cites Omgevingsloket/Rijksoverheid.

## Internal overlap / cannibalisation

- High risk with `/huis-renoveren/` if the hub becomes a broad “where do I start?” article.
- High risk with `/renovatiefasen/` if the hub publishes a lifecycle checklist.
- High risk with `/renovatie-volgorde/` if it publishes an execution sequence.
- Medium risk with `/renovatiekosten/` and `/renovatie-budget/` if it repeats price tables or budget mechanics.

Mitigation: hub = navigation + distinction + readiness logic; children = depth.

## Data gaps

No blocking data gap. The hub does not need volatile price/subsidy/legal numbers to satisfy its intent.

## Gate

- [x] Current SERP inspected
- [x] Search intent and ownership explicit
- [x] All MUST needs identified
- [x] Cannibalisation risks identified
- [x] No blocking source/data gap
- [x] Ready for v2 brief