# PUBLISH_REVIEW — Renovatievolgorde

- Route: `/renovatie-plannen/renovatie-volgorde/`
- Workflow: `renovation-analysis-workflow` v2
- Review date: 2026-09-13
- Source decision: `DEEP_REWRITE`
- Research artifact: `content/research/renovatie-plannen/renovatie-volgorde/serp-coverage.md`
- Post-write check: `content/reviews/renovatie-plannen/renovatie-volgorde/post-write-gap-check.md`

## Gate A — machine blockers

PR checks on the completed content head:

- `Validate editorial engine`: PASS
- `Validate renovation structure`: PASS
- generated page keeps `noindex,follow`, canonical and expected metadata

Machine validation is treated only as an invariant check, not as proof of semantic quality.

## Gate B — research traceability

- Current SERP/content-depth research persisted: PASS
- Brief explicitly consumes MUST / SHOULD + data gaps: PASS
- Post-write gap check exists: PASS
- `MUST = MISSING`: none
- Blocking data gap: none for this content decision

Unmeasured and explicitly not claimed: keyword volume, GSC history, backlink/authority metrics and cross-engine AI citation visibility.

## Gate C — substantive review

### Intent / information gain

PASS. The page satisfies the SERP expectation for an explicit sequence while adding decision value beyond a generic contractor steps list.

Distinctive assets are present:

- dependency-first execution spine;
- pre-sloop safety/regulatory blockers;
- `ready for next trade` checkpoints;
- closure checks before walls, floors and maatwerk are fixed;
- conditional kitchen-vs-floor logic;
- underfloor-heating / floor-build-up dependency;
- occupied-renovation exception.

### Cannibalisation

PASS.

- `/huis-renoveren/` = readiness, scope and uncertainty before planning.
- `/renovatie-volgorde/` = physical execution order and trade dependencies.
- `/renovatiefasen/` = project lifecycle from inventory to handover.
- `/complete-renovatie/` = multi-system coordination and phasing.

The central answers and section logic are not interchangeable.

### Factuality / freshness

PASS.

- Demolition / permit / notification guidance is routed to Omgevingsloket and Rijksoverheid.
- Asbestos stop-work guidance is supported by Milieu Centraal.
- Floor build-up / floor heating sequence is supported by Vereniging Eigen Huis.
- Insulation, ventilation and future heating are treated as coordinated choices with current Milieu Centraal guidance.
- No universal drying time, project duration or kitchen/floor rule is invented.

### Safety

PASS. Unknown structure, unexplained moisture and suspected asbestos are blockers before destructive work or closure. The page does not provide unsafe DIY structural/asbestos instructions.

### GEO / AEO

PASS for structural/citation-worthiness review.

- direct extractable answer appears early;
- dependency rules are stated atomically;
- sensitive claims have adjacent dated sources;
- tables encode genuine decision/checkpoint information;
- no manufactured FAQ or unsupported AI visibility claim.

### Voice / anti-slop

PASS.

- no generic throat-clearing introduction;
- numbered sequence is justified by procedural intent rather than reused as a cluster template;
- repeated handoff labels are functional checkpoints, not filler;
- no universal-sounding false precision where the order is system-dependent;
- no HIGH anti-AI-slop signal identified in the editorial review.

### SEO / rendered page

PASS.

- title `Renovatie volgorde: 8 stappen van sloop tot afwerking` matches the eight execution layers;
- H1 / lede / body align to the target intent;
- canonical/slug remain unchanged;
- rendered page retains `noindex,follow`;
- internal handoffs reduce rather than increase cannibalisation.

## Result

PASS — READY_FOR_HUMAN_VALIDATION

Indexation remains a separate human decision. This review does not change `indexing_enabled`.
