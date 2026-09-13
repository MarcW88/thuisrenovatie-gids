# PUBLISH_REVIEW — Renovatiefasen

- Route: `/renovatie-plannen/renovatiefasen/`
- Workflow: `renovation-analysis-workflow` v2
- Review date: 2026-09-13
- Source decision: `LIGHT_UPDATE`
- Research artifact: `content/research/renovatie-plannen/renovatiefasen/serp-coverage.md`
- Post-write check: `content/reviews/renovatie-plannen/renovatiefasen/post-write-gap-check.md`

## Gate A — machine blockers

PR checks on the completed content head:

- `Validate editorial engine`: PASS
- `Validate renovation structure`: PASS
- generated page keeps `noindex,follow`, canonical and expected metadata

Machine validation is treated only as an invariant check, not proof of semantic quality.

## Gate B — research traceability

- Current SERP/content-depth research persisted: PASS
- Brief consumes MUST / SHOULD gaps: PASS
- Post-write gap check exists: PASS
- `MUST = MISSING`: none
- Blocking data gap: none for this content decision

## Gate C — substantive review

### Intent / information gain

PASS.

The page keeps its correct lifecycle ownership rather than being converted into another physical work-order article. Information gain is operational rather than volumetric:

- central question per phase;
- concrete result per phase;
- `Ga pas door als...` gate per phase;
- practical project dossier that grows through the project;
- explicit guidance on which decisions can remain open;
- calibrated handoff to sibling pages.

### Cannibalisation

PASS.

- `/huis-renoveren/` = where to start / what must be known first.
- `/renovatiefasen/` = lifecycle, decision maturity and handoffs.
- `/renovatie-volgorde/` = physical order of works.
- `/complete-renovatie/` = coordination of interdependent whole-house systems.

### Factuality / freshness

PASS.

- Regulatory feasibility claims are supported by current Rijksoverheid guidance and route project-specific checks to Omgevingsloket.
- Preparation, offer/contract and handover guidance is aligned with current Vereniging Eigen Huis material.
- The page preserves VEH's nuance that formal handover is not always customary for renovations while still recommending a clear joint review moment.
- No unsupported phase durations, cost ranges or universal professional requirements are introduced.

### GEO / AEO

PASS for structural/citation-worthiness review.

- direct lifecycle answer near the top;
- atomic distinctions between phase purpose, output and gate;
- authoritative sources adjacent to unstable/legal claims;
- no manufactured FAQ;
- no unsupported AI visibility claim.

### Voice / anti-slop

PASS.

The repeated phase structure is purpose-built navigation for this specific decision model. It is not a generic site template. No high-severity anti-AI-slop pattern identified after review.

## Result

PASS — READY_FOR_HUMAN_VALIDATION

Indexation remains a separate human decision. This review does not change `indexing_enabled`.
