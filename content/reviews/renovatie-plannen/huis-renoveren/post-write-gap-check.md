# Post-write gap check — Huis renoveren

- Route: `/renovatie-plannen/huis-renoveren/`
- Workflow: `renovation-content-workflow` v2
- Decision entering production: `DEEP_REWRITE`
- Research: `content/research/renovatie-plannen/huis-renoveren/serp-coverage.md`
- Brief: `content/briefs/renovatie-plannen/huis-renoveren.md`
- Review date: 2026-09-13
- Status: `QA_IN_PROGRESS`

## MUST coverage

| MUST from pre-write matrix | Final status | Where it is covered | Proof / note |
|---|---|---|---|
| Direct answer to “where do I start?” | COVERED | lead + quick answer | Answer now starts with state, desired end state, uncertainty and dependencies rather than a generic lifecycle |
| Separate technical necessity from wishes | COVERED | opening + startscan `Staat` / `Verandering` | Preserves the strongest idea from the previous version |
| Classify renovation depth / complexity | COVERED | `Welke renovatie heb je eigenlijk?` | Three editorial levels: opknappen / gericht verbouwen / ingrijpend renoveren; explicitly labelled non-official |
| Identify high-impact / hard-to-reverse decisions | COVERED | quick answer + startscan `Afhankelijkheden` + dependency test | Mentions layout, structural choices, routes, floor build-up, heating and ventilation |
| Know when specialist investigation comes before planning | COVERED | `Wanneer moet je eerst laten onderzoeken?` | Structure/foundation signals, unexplained moisture, gas/electric safety, suspected asbestos; no DIY diagnostic instruction |
| Know what must be clear before requesting comparable quotes | COVERED | `Wat moet vaststaan vóór je offertes serieus vergelijkt?` | Minimum viable renovation plan lists scope, unknowns, functions/performance, dependencies, responsibilities and financial ceiling |
| Permit / formal check | COVERED | `Controleer regels...` + source box | Official Omgevingsloket / Rijksoverheid logic; no universal permit claim |
| Budget ceiling versus cost estimate | COVERED | `Budgetplafond en begroting zijn niet hetzelfde` | Distinguishes early financial ceiling from increasingly precise estimate |
| Physical work order should be handed off | COVERED | final routing table | `/renovatie-volgorde/` owns sloop/constructie/installaties/afwerking; sequence is no longer reproduced here |
| Project lifecycle should be handed off | COVERED | final routing table | `/renovatiefasen/` owns inventarisatie → ontwerp → uitvoering → oplevering; lifecycle is no longer page architecture |
| Practical readiness check before planning / quotes | COVERED | `Renovatie-startscan` + minimum plan | Main information-gain asset of the rewrite |

**MUST = MISSING:** none.

## SHOULD coverage

| SHOULD | Final status | Where / rationale |
|---|---|---|
| Current budget buffer context | COVERED | NN source box states 10–20% guidance with source/date and explicit limitation |
| Explain decisions that can wait | COVERED | `Wat hoef je nog niet te beslissen?` distinguishes reversible finish choices from dimensions/connections/build-up |
| Quote readiness tangible | COVERED | minimum plan + explicit same-project / same-responsibility logic |
| Whole-house coordination handoff | COVERED | final routing table links `/complete-renovatie/` |
| Detailed costs | HANDOFF | intentionally delegated to `/renovatiekosten/`; not duplicated |
| Contract / payment / guarantees | HANDOFF | intentionally delegated to `vakman-en-offertes`; not central to pre-planning job |

## Factuality pass

### Verified claim 1 — permit check

Claim in page: whether permit / notification applies depends on the concrete activity and location, and the reader should use the official Vergunningscheck before fixing design or execution.

Verified against:

- Rijksoverheid — `Checken of vergunning nodig is voor (ver)bouwen`, accessed 2026-09-13: directs people who build, renovate or demolish to the Vergunningscheck for permit / demolition-notification requirements.
- Rijksoverheid — `Wanneer moet ik een omgevingsvergunning aanvragen?`, accessed 2026-09-13: explicitly states that a permit is not always needed and that the outcome depends among other things on project location and answers in the check.
- Omgevingsloket — `https://omgevingswet.overheid.nl/checken`.

Result: `PASS`.

### Verified claim 2 — NN buffer guidance

Claim in page: Nationale-Nederlanden recommends first clarifying what you want to do, requesting several quotes per component, and reserving 10–20% extra budget for unexpected costs.

Verified against NN, `Wat kost een verbouwing?`, last edited 2026-07-01 and accessed 2026-09-13. The page states the scope/quote sequence and 10–20% buffer.

Result: `PASS`.

### Safety / diagnosis

The page does not claim to diagnose cracks, foundation, moisture, gas/electricity or asbestos. It uses them only as stop conditions for appropriate investigation.

Result: `PASS`.

## GEO / AEO pass

- Direct answer is present at the start without repeating it in a manufactured FAQ: `PASS`.
- Distinctions are atomic and extractable: `technische noodzaak vs wens`, `budgetplafond vs begroting`, `projectfasen vs werkvolgorde`: `PASS`.
- Current factual claims have adjacent named sources / dates: `PASS`.
- The `renovatie-startscan` is clearly an editorial framework, not presented as an external standard: `PASS`.
- No FAQPage-style block was added solely for bots: `PASS`.
- No AI-visibility or citation claim is made without measurement: `PASS`.

## Brand voice / humanizer / general-writing / anti-ai-slop review

### Preserved / improved

- No generic `Bij een renovatie komt veel kijken` opening.
- No fixed eight-step chronology.
- Paragraphs explain consequences rather than restating headings.
- Technical terms are limited and explained by context.
- Safety tone is sober and non-alarmist.
- CTA pressure is absent until quote readiness is established.

### Structural pattern check

- One three-card classification is retained because the three levels change planning depth; it is not repeated as a decorative rule-of-three throughout the page.
- Two tables have different jobs: the first diagnoses readiness; the final one routes distinct follow-up intents. They are not duplicate summary tables.
- Headings mix questions and declarative instructions; there is no forced all-question SEO template.
- No automatic FAQ, pros/cons block or generic conclusion.

Result: `PASS`, no HIGH anti-AI-slop signal identified in this review.

## Internal linking / cannibalisation pass

- `/huis-renoveren/` now owns pre-planning diagnosis / decision readiness.
- `/renovatiefasen/` keeps project lifecycle ownership.
- `/renovatie-volgorde/` keeps physical work-order ownership.
- `/complete-renovatie/` keeps multi-system coordination.
- `/renovatiekosten/` and `/renovatie-budget/` keep detailed financial coverage.
- `/offertes-vergelijken/` receives readers only once scope readiness has been explained.

The page no longer shares the same central architecture as `/renovatiefasen/`.

Result: `PASS`.

## Residual data gaps

These are non-blocking for this rewrite but remain unmeasured:

- no GSC query / impression history because the site is still noindex/new;
- no Ahrefs/Semrush backlink or keyword-overlap export in this run;
- no measured cross-engine AI citation visibility test.

None is represented as completed or estimated.

## Post-write result

`PASS — READY_FOR_PUBLISH_REVIEW`

This is **not** final publication approval. The page still requires the repository machine checks and `renovation-analysis-workflow / PUBLISH_REVIEW`; indexation remains unchanged.
