# Post-write gap check - Renovatievolgorde

- Route: `/renovatie-plannen/renovatie-volgorde/`
- Workflow version: 2
- Decision consumed: `DEEP_REWRITE`
- Research artifact: `content/research/renovatie-plannen/renovatie-volgorde/serp-coverage.md`
- Brief: `content/briefs/renovatie-plannen/renovatie-volgorde.md`
- Checked: 2026-09-13
- Status: `QA_IN_PROGRESS`

## MUST coverage

| MUST from pre-write matrix | Final status | Where covered | Evidence / note |
|---|---|---|---|
| Give a usable default physical sequence | COVERED | quick answer + `De basisvolgorde van de werkzaamheden` | Eight execution layers from sloop to testing/hand-over; pre-sloop blockers kept outside the physical sequence |
| Explain why each layer precedes the next | COVERED | each execution layer + transition text | Sequence is expressed through accessibility, dependency and closure logic rather than numbers alone |
| Separate execution order from planning/project phases | COVERED | intro handoff to `/huis-renoveren/` + closing handoff to `/renovatiefasen/` | No inventory/design/procurement lifecycle duplicated in the main sequence |
| Put demolition behind regulatory/safety blockers | COVERED | `Vóór de sloop: los eerst de blokkades op` | Omgevingsloket, Rijksoverheid and Milieu Centraal sources linked directly |
| Explain what must be complete before walls/floors are closed | COVERED | execution steps 3-5 + `Sluit dit nog niet af` matrix | Hidden routes, access, floor build-up and system conditions are explicit |
| Address kitchen vs floor without a false universal rule | COVERED | step 6 + decision matrix | Page explicitly states there is no universal winner; system and supplier instructions determine order |
| Address underfloor heating / floor build-up dependency | COVERED | steps 5-6 + decision matrix + VEH source box | Heating is placed in the build-up before visible floor finish; floor heights and kitchen levels are noted |
| Explain stop signs that pause the sequence | COVERED | pre-sloop blockers + closure checkpoints | Structure, moisture, asbestos suspicion, unresolved hidden work and levels stop progression |
| Add current legal/safety evidence where needed | COVERED | first source box | Current official/independent sources, checked September 2026 |

## SHOULD coverage

| SHOULD | Final status | Where covered |
|---|---|---|
| Coordinate insulation, ventilation and heating | COVERED | execution step 4 + four-decisions table + Milieu Centraal source |
| Explain occupied/phased renovation exception | COVERED | `Wat als je tijdens de renovatie in het huis blijft wonen?` |
| Add ready-for-next-trade checkpoints | COVERED | `Klaar om door te gaan wanneer` markers throughout steps 1-6 |
| Add pairwise decision help beyond generic sequence | COVERED | four-decisions table + closure checkpoint table |
| Improve GEO extractability without artificial FAQ | COVERED | direct answer, atomic dependency rules, structured tables, dated source boxes |

## Fact-check pass

| Claim | Status | Source | Checked | Action |
|---|---|---|---|---|
| Permit/notification outcome depends on activity/location and demolition/asbestos can be separate activities | CONFIRMED | Omgevingsloket `Woning verbouwen` | 2026-09-13 | kept with source |
| Demolition can trigger notification requirements | CONFIRMED | Rijksoverheid `Checken of vergunning nodig is voor (ver)bouwen` | 2026-09-13 | kept, no unnecessary threshold repeated in body |
| Stop work when suspected asbestos is encountered and verify procedure | CONFIRMED | Milieu Centraal `Wat te doen bij asbest?` | 2026-09-13 | kept in safety gate |
| Floor replacement can combine construction floor, insulation, floor heating, screed and final finish | CONFIRMED | Vereniging Eigen Huis `Vloer vervangen` | 2026-09-13 | used as dependency evidence |
| Insulation/ventilation/heating choices should be coordinated; future heat demand affects heat-pump sizing | CONFIRMED | Milieu Centraal energy-efficient-home guidance + warmtepomp guidance | 2026-09-13 | wording kept conditional, not universal |

No price, duration, drying-time or legal threshold was invented.

## Cannibalisation review

### `/huis-renoveren/`
PASS. That page owns readiness, scope and uncertainty before planning. `renovatie-volgorde` begins once physical execution can be sequenced.

### `/renovatiefasen/`
PASS. The page no longer repeats the project lifecycle. It owns physical layers and trade dependencies only.

### `/complete-renovatie/`
PASS. Only the occupied/phased exception is mentioned, with a handoff for whole-house coordination.

## GEO/AEO review

- Direct answer is early and self-contained.
- The page contains extractable dependency statements rather than manufactured FAQ snippets.
- Sensitive facts have adjacent dated sources.
- Distinctive information gain survives: closure checkpoints, conditional kitchen/floor logic, and next-trade readiness.
- No claim of original field testing or inspection.

## Humanizer / general-writing / anti-ai-slop review

- No em dash or en dash prose pattern.
- No promotional contractor voice.
- No generic conclusion summarizing the article.
- Repeated `Klaar om door te gaan wanneer` labels are retained intentionally because they encode the handoff framework; they are functional UI labels, not filler.
- Tables are justified by real comparison/checkpoint tasks.
- No artificial FAQ section.
- No `HIGH` anti-AI-slop finding remains.

## SEO / technical review

- Primary query/variant appears naturally in title/H1/lede.
- Existing title `Renovatie volgorde: 8 stappen van sloop tot afwerking` remains accurate after the rewrite.
- Canonical/slug ownership unchanged.
- Internal links route out to adjacent intentions instead of duplicating them.
- No indexation change requested; `noindex,follow` must remain.

## Result before PUBLISH_REVIEW

- `MUST = MISSING`: 0
- blocking unverifiable claim: 0
- blocking data gap: 0
- unresolved intent/cannibalisation issue: 0

Ready for `renovation-analysis-workflow / PUBLISH_REVIEW`.
