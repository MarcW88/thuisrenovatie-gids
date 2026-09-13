# Brief v2 — Renovatievergunning

- Route: `/renovatie-plannen/renovatievergunning/`
- Status: QA_COMPLETE
- Market: Netherlands / nl-NL
- Primary queries: `vergunning verbouwing`, `vergunning renovatie`, `omgevingsvergunning verbouwen`
- Reader task: determine what must be checked before committing to a renovation and understand the result of the official Vergunningcheck.
- Decision: `DEEP_REWRITE`
- Last researched: 2026-09-13

## Search intent and page role

The reader wants a practical answer to `heb ik een vergunning nodig?`, but a generic page cannot legally or reliably decide that without location and exact activities. The page must therefore do two jobs well:

1. make the Dutch permission model understandable enough that the homeowner knows what can trigger attention;
2. get the homeowner to the official Omgevingsloket Vergunningcheck at the right moment in the project.

This is a decision page, not a legal encyclopaedia and not a fixed list of permit-required renovations.

## Required information architecture

The final structure should follow the task, not a fixed article template, but it must cover these content assets:

- **Direct answer:** location + exact activity determine the result; use the official Vergunningcheck.
- **Two-layer model:** omgevingsplan/spatial layer vs technical building layer in plain Dutch.
- **Four-result model:** vergunning aanvragen / melding doen / informatie aanleveren / geen filing action shown for that activity.
- **Early-attention signals:** expansion/dakkapel/exterior changes, load-bearing/structural change, monument/protected context, demolition/asbestos, use change or conflict with omgevingsplan. These are check signals, not universal legal conclusions.
- **Permit gate:** run the check before definitive maatwerk orders, irreversible design choices or final contractor commitment.
- **After-the-check map:** what to do when the result says permit, notification or information duty; mention that required documents are shown by the Omgevingsloket and can include drawings/calculations.
- **Timing:** regular permit procedure is normally 8 weeks, with one possible extension of up to 6 weeks; clearly caveat that another procedure or extra information can change timing.
- **Permit-free is not rule-free:** Bbl and other rules still apply; private-law/project permissions can also remain relevant.
- **Boundary:** no individual legal verdict from this article.

## Evidence register

### Primary / normative

- Omgevingsloket — `Woning verbouwen`: the check uses location + selected work; results can require a permit, notification or information; approximately 15–30 minutes.
- Rijksoverheid — `Stappenplan bij bouwen en verbouwen`: check omgevingsplan, welstand, building rules, permit need and neighbour impact.
- Rijksoverheid — `Vergunningvrij bouwen en verbouwen`: permit-free does not remove Bbl/burenrecht or other possible permit requirements.
- Rijksoverheid — `Vergunning aanvragen voor (ver)bouwen`: application documents can include drawings and structural calculations; Omgevingsloket indicates required documents.
- IPLO — technical building activity / homeowner guidance for aanbouw and bijgebouw: technical and spatial rules are separate layers.
- IPLO — regular permit procedure: normally 8 weeks; one extension up to 6 weeks can apply.

### Secondary SERP / homeowner-language benchmark

- Vereniging Eigen Huis — `Heb ik een vergunning nodig voor mijn verbouwing?`: useful benchmark for how homeowners understand the two permit layers and common examples. Do not let it override official sources.

## Information gain

1. Explain why one renovation can receive more than one legal result instead of collapsing everything into `vergunning ja/nee`.
2. Show the reader what each Vergunningscheck result means operationally.
3. Put the legal check at a concrete project decision gate rather than mentioning it as an afterthought.
4. Separate public-law permission from VvE/landlord/burenrecht or contractual approval.
5. Avoid hard-coded universal thresholds unless they are necessary, current and directly sourced.

## GEO / extractability requirements

- Each major question opens with a direct 1–3 sentence answer.
- Keep definitions atomic: `omgevingsplanactiviteit`, `technische bouwactiviteit`, `melding`, `vergunningvrij`.
- Put source/date/context next to time-sensitive procedural claims.
- Do not manufacture FAQs or schema merely for GEO.
- The strongest extractable fact should remain: the official location/activity-specific Vergunningcheck owns the practical answer.

## Cannibalisation boundaries

- `/renovatievergunning/` owns the general permission/check workflow.
- `/aanbouw/`, dakkapel-related future pages or other project pages may explain project-specific decisions but should not recreate the general legal framework.
- `/renovatiefasen/` owns the lifecycle; this page owns the permission gate within it.
- `/huis-renoveren/` should only mention the need to check rules early and link here.

## Safety/legal boundary

Do not state that a particular homeowner definitely does or does not need a permit without the location- and activity-specific official check. Treat examples as attention signals and explicitly distinguish general guidance from the authoritative result.

## QA completion

- SERP matrix persisted and applied.
- Fact-check: PASS.
- Post-write gap check: no missing or partial MUST.
- Page is eligible for `PUBLISH_REVIEW` while site-level indexation remains disabled.
