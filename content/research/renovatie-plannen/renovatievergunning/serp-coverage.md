# SERP coverage — Renovatievergunning

- Route: `/renovatie-plannen/renovatievergunning/`
- Research date: 2026-09-13
- Decision: `DEEP_REWRITE`
- Primary queries: `vergunning verbouwing`, `vergunning renovatie`, `omgevingsvergunning verbouwen`, `vergunning nodig verbouwing`, `vergunning dakkapel`, `vergunning aanbouw`

## Search intent

The dominant task is not to learn every article of Dutch building law. Homeowners want to know whether their intended renovation needs a permit or another filing, which parts of the project create risk, and what to check before ordering or commissioning work. The authoritative answer is location- and activity-specific and belongs in the Omgevingsloket Vergunningcheck.

## SERP observations

- Omgevingsloket owns the transactional answer. Its `Woning verbouwen` flow asks for location and activities, then returns whether the user must apply for a permit, submit a notification, provide information, or take no filing action. The check takes roughly 15–30 minutes and can be saved.
- Rijksoverheid frames building/renovation as a sequence of checks: omgevingsplan, welstand, building rules, permit requirement, and neighbours. It explicitly states that rules continue to apply even when no permit is required.
- IPLO explains that building can involve separate legal layers: the technical building activity and the omgevingsplan activity. For an aanbouw/bijgebouw, technical and spatial rules can therefore produce different conclusions.
- Vereniging Eigen Huis performs well by explaining these two permit layers in homeowner language and then routing to the Omgevingsloket. It also covers common examples such as aanbouw/dakkapel and the effect of monument/protected-area context.
- The current Thuisrenovatie page gives the right high-level warning but collapses these layers into a generic `soms wel, soms niet` answer. It does not explain the four practical outcomes of the check or why one project may trigger several authorities/rules.

## MUST coverage

| Need | Current page | Required action |
|---|---|---|
| State that there is no universal yes/no answer | COVERED | Keep. |
| Route to the official Omgevingsloket Vergunningcheck | COVERED | Keep and make it the core action. |
| Explain that location and exact activity determine the result | PARTIAL | Make explicit at the top. |
| Explain technical building activity vs omgevingsplan activity | MISSING | Add a simple two-layer model. |
| Explain possible outcomes: permit / notification / information / no filing | PARTIAL | Add as a decision table. |
| Explain that multiple authorities/rules may apply | MISSING | Add municipality / province / water board / national-government context without overwhelming the reader. |
| Explain `vergunningvrij is niet regelvrij` | COVERED | Keep, strengthen with Bbl + other rules. |
| Give common trigger situations without pretending they are universal permit rules | COVERED | Rework as `check early when...`, not a yes/no list. |
| Cover monument/protected context | COVERED | Keep. |
| Cover structural interventions/draagconstructie as a strong attention signal | COVERED | Keep, tie to technical layer. |
| Explain when in the project to run the check | COVERED | Turn into a hard project gate before definitive order/maatwerk. |
| Explain what happens after a permit result at a high level | MISSING | Add application/required documents/typical regular-procedure timing caveat. |
| Preserve legal boundary: no individual legal conclusion from this article | COVERED | Keep prominently. |

## SHOULD coverage

- Mention that Omgevingsloket can show more than one required action for one project.
- State that the regular procedure is normally 8 weeks and can be extended once by up to 6 weeks, while making clear other/longer procedures can apply.
- Explain that the application can require drawings and structural calculations depending on the activity; the Omgevingsloket indicates required documents.
- Mention VvE, landlord or neighbour/private-law approval only as separate from the public-law permit question; do not imply the Vergunningcheck resolves those relationships.
- Explain that rear-facing dakkapellen/ordinary maintenance can sometimes be permit-free under conditions, but avoid turning examples into a universal checklist.
- Explain that a technical permit-free conclusion does not automatically mean the spatial/omgevingsplan layer is also clear.

## Information gain

1. **Two-layer permit model** — spatial/omgevingsplan vs technical building activity.
2. **Four-outcome model** — permit, notification, information duty, or no filing action.
3. **Permit gate** — a concrete moment in the renovation workflow before definitive ordering, structural drawings or contractor commitment become expensive to change.
4. **Result-to-action map** — what the homeowner should do after each type of Vergunningscheck result.
5. **Separate public-law vs private/project permissions** — Omgevingsloket does not replace VvE/landlord/burenrecht checks.
6. **No false certainty** — examples are attention signals; only the official location/activity-specific check owns the final practical answer.

## Evidence register

Primary/current:
- Omgevingsloket — `Woning verbouwen`: location/activity-specific Vergunningcheck, 15–30 minutes, result may require permit, notification or information.
- Rijksoverheid — `Stappenplan bij bouwen en verbouwen`: omgevingsplan, welstand, building rules, permit check, neighbours; rules also apply without a permit.
- Rijksoverheid — `Vergunningvrij bouwen en verbouwen`: permit-free does not mean rule-free; Bbl and burenrecht still apply and other permits may be needed.
- Rijksoverheid — `Vergunning aanvragen voor (ver)bouwen`: application documents such as drawings/strength calculations can be required; Omgevingsloket indicates required submissions.
- IPLO — technical building activity / permit-notification framework and homeowner information for aanbouw/bijgebouw.
- IPLO — regular omgevingsvergunning procedure: normally 8 weeks, one extension of up to 6 weeks possible.

Secondary SERP context:
- Vereniging Eigen Huis — homeowner explanation of the two permit layers and common renovation examples. Useful for format/intent analysis; official sources remain normative.

## Cannibalisation boundary

- `renovatievergunning` owns permission/rules workflow for renovation generally.
- `/renovatieprojecten/aanbouw/` and other project pages may mention project-specific permit attention points but should route here/Omgevingsloket rather than duplicate the legal framework.
- `renovatiefasen` owns project lifecycle; this page owns the legal/permission gate within that lifecycle.
- `huis-renoveren` only needs a short early warning that rules/permits must be checked.