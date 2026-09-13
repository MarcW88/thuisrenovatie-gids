# Publish review — Subsidies renovatie

- Route: `/renovatie-plannen/subsidies-renovatie/`
- Review date: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`

## Required artifacts

- SERP coverage matrix: PASS
- Brief v2: PASS / `QA_COMPLETE`
- Fact-check: PASS
- Post-write gap check: PASS
- Generated page: PASS

## Semantic gates

- Search intent ownership: PASS — page owns subsidy eligibility/application logic, not technical measure selection or budget control.
- Content-gap resolution: PASS — all MUST items covered; combination logic and evidence workflow added.
- Information gain: PASS — decision chain, combination matrix and subsidy dossier go beyond a static amount list.
- Factuality/currentness: PASS — time-sensitive claims grounded in current RVO/Rijksoverheid sources.
- Volatile-data handling: PASS — complete tariff tables avoided; conflicting warm-network amount excluded rather than guessed.
- GEO usefulness: PASS — direct answer, atomic 2026 facts and extractable combination table.
- Safety/financial framing: PASS — subsidy not treated as guaranteed cash and loans not presented as subsidy.
- Cannibalisation: PASS — clear boundary with renovation budget, costs and technical sustainability pages.
- Style / anti-slop: PASS — practical decision-led structure; no filler FAQ or artificial length expansion.

## Technical gates

- canonical: PASS
- robots: `noindex,follow` preserved
- site-level indexing: unchanged / disabled
- generated route: PASS
- CI before final review commit: editorial engine PASS; renovation structure PASS

## Final status

`PASS — READY_FOR_HUMAN_VALIDATION`

This status does not enable indexing and does not constitute approval to flip `content/site.json` indexing.