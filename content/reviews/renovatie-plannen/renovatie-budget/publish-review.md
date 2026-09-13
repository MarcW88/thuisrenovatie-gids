# Publish review — Renovatiebudget

- Route: `/renovatie-plannen/renovatie-budget/`
- Reviewed: 2026-09-13
- Decision entering production: `DEEP_REWRITE`
- Result: `PASS — READY_FOR_HUMAN_VALIDATION`

## Intent / ownership

PASS.

The page owns allocation and ongoing spend control. It no longer duplicates `/renovatiekosten/`, which owns market benchmarks. Financing products, supplier comparison, contract checking and subsidy eligibility are routed to their respective pages.

## Research / evidence

PASS.

Research artifact exists at `content/research/renovatie-plannen/renovatie-budget/serp-coverage.md`.

Volatile or externally sourced claims were fact-checked against:
- Nationale-Nederlanden, `Wat kost een verbouwing?`, updated 1 July 2026;
- Nationale-Nederlanden, `Je verbouwing betalen?`, updated 23 June 2026;
- Vereniging Eigen Huis, `Verbouwen: maak een plan`;
- Vereniging Eigen Huis, `Verbouwen: offerte en contract aannemer`.

The 10–20% contingency is presented as consumer guidance, not a universal technical rule.

## Information gain

PASS.

The page adds more than a static allocation table:
- five-number live budget dashboard (`budgetplafond`, `vastgelegd`, `verwacht`, `reserve`, `vrij`);
- separation of project contingency from household emergency buffer;
- priority ladder (`MOET / LIEFST / KAN LATER`);
- explicit treatment of `stelposten` as uncertainty;
- event-driven reforecast loop;
- dynamic EUR 80,000 worked scenario showing the decision caused by EUR 7,000 of additional expected cost.

## Post-write gap check

PASS.

`content/reviews/renovatie-plannen/renovatie-budget/post-write-gap-check.md` records zero `MUST = MISSING`.

## Factuality

PASS.

`fact-check.md` contains no blocking issue. The EUR 80,000 scenario arithmetic is correct and labelled illustrative rather than recommended allocation.

## Voice / anti-slop

PASS.

The page opens with the control problem rather than generic renovation commentary. It avoids artificial urgency, fake precision and an automatic FAQ block. Site-created methods are distinguishable from external guidance.

## GEO / extraction

PASS.

Direct answer, atomic definitions, structured comparison tables, dated evidence and an explicit worked example make the page extractable without manufacturing question blocks.

## Internal linking / boundaries

PASS.

Relevant handoffs:
- `/renovatie-plannen/renovatiekosten/` for current price benchmarks;
- `/vakman-en-offertes/offerte-controleren/` for offer details;
- `/vakman-en-offertes/offertes-vergelijken/` for supplier/scope comparison;
- `/renovatie-plannen/subsidies-renovatie/` for current subsidy eligibility.

## Technical publication blockers

PASS.

Generated page has:
- canonical `https://thuisrenovatie-gids.nl/renovatie-plannen/renovatie-budget/`;
- `noindex,follow` retained;
- title `Renovatiebudget maken: buffer en grip | Thuisrenovatie Gids`;
- current meta description;
- corrected Dutch H1/breadcrumb label `Renovatiebudget`.

## Human gate

Human validation remains pending. This PASS does not authorize changing global indexation.
