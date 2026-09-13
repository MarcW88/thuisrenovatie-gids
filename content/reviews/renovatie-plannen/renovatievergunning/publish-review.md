# PUBLISH_REVIEW — Renovatievergunning

- Route: `/renovatie-plannen/renovatievergunning/`
- Reviewed: 2026-09-13
- Result: **PASS — READY_FOR_HUMAN_VALIDATION**

## Intent and ownership

PASS.

The page now owns the general permission/check workflow for renovation. It no longer behaves like a brittle list of projects that supposedly are or are not permit-required. Project-specific pages can mention local attention points without duplicating this framework.

## Research and competitive coverage

PASS.

The page was rebuilt from a persisted SERP/coverage matrix using current official Dutch sources plus Vereniging Eigen Huis as a secondary homeowner-language benchmark. The dominant search task — `heb ik voor mijn verbouwing een vergunning nodig en wat moet ik nu doen?` — is answered directly while the location/activity-specific official check remains authoritative.

## Factuality and legal boundary

PASS.

- Omgevingsloket location/activity workflow verified.
- Permit / notification / information outcomes verified.
- Omgevingsplan vs technical-building layers verified against official/IPLO material.
- `vergunningvrij is niet regelvrij` verified against Rijksoverheid.
- Application-document claim verified.
- Regular-procedure timing (normally 8 weeks; one possible extension up to 6 weeks) verified and correctly caveated.
- No individual legal conclusion is given without the official check.

See `fact-check.md`.

## Information gain

PASS.

Distinctive assets now present:

- two-layer permission model;
- four-result action model;
- multiple-activity / multiple-authority explanation;
- early-attention signals instead of fake universal permit rules;
- hard `vergunninggate` before costly irreversible commitments;
- result-to-action guidance;
- separation of public-law permission from burenrecht, VvE/landlord and contractual responsibilities.

## GEO / AEO

PASS.

- direct answer appears immediately;
- key legal concepts are atomic and extractable;
- two decision tables make distinctions machine-readable and user-readable;
- time-sensitive procedural information is adjacent to named official sources;
- no synthetic FAQ block or unsupported schema added;
- strongest extractable recommendation remains the official location/activity-specific Vergunningscheck.

## Style / anti-AI-slop

PASS.

The page avoids generic `it depends` filler by explaining what determines the result and what the reader should do next. No repetitive conclusion, fake urgency or forced rule-of-three structure was introduced.

## Internal linking / cannibalisation

PASS.

- links to `renovatiefasen` for lifecycle context;
- links to `aanbouw` for a concrete project route;
- does not duplicate `huis-renoveren` orientation or project-specific technical pages.

## On-page / technical

PASS.

- title: `Vergunning verbouwing: wanneer nodig? | Thuisrenovatie Gids`;
- meta description aligned with permit / notification / information intent;
- canonical unchanged and correct;
- generated H1: `Renovatievergunning`;
- generated page remains `noindex,follow`;
- site-level indexing remains disabled.

## Gap gate

PASS.

`post-write-gap-check.md` reports:

- `MUST = MISSING`: 0
- `MUST = PARTIAL`: 0
- blocking factual issue: none

## Human validation

Still required before any future decision to enable indexation. This review does not change the site's global `indexing_enabled: false` state.
