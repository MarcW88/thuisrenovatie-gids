# SERP coverage — fundering

- Route: `/renovatieprojecten/fundering/`
- Market: Nederland
- Reviewed: 2026-09-13
- Workflow version: 2
- Audit decision: `DEEP_REWRITE`

## Ownership

This page owns the job **after sufficient investigation shows that foundation repair is needed**: turn research into a repair scope, shared technical assumptions, comparable quotations, financing/planning and a controlled handover.

It does **not** own the earlier diagnostic intent. `/problemen-oplossen/funderingsproblemen/` owns signals, risk context, deciding whether investigation is needed and the transition to specialist investigation.

## Query set and sub-intents

Inspected queries:

- `fundering herstellen`
- `funderingsherstel kosten`
- `funderingsherstel stappenplan`
- `fundering herstel offerte`
- `funderingsonderzoek funderingsherstel`
- `funderingsherstel programma van eisen`

Sub-intents:

1. Is repair actually needed and what document proves that?
2. How do I go from investigation to a repair plan?
3. Do neighbouring/connected owners need to act together?
4. What must all contractors price on the same basis?
5. What costs sit outside the contractor's core foundation work?
6. How can I estimate costs without publishing a misleading universal average?
7. What financing/support may exist?
8. What must be documented after completion?

## Current SERP / inspected results

### Vereniging Eigen Huis — Funderingsherstel

Strong on the overall consumer journey from information gathering toward research and repair. Useful as a broad orientation page. It still leaves room for a more operational handoff from a completed investigation to a comparable tender package.

### KCAF — Stappenplan funderingsherstel

The strongest operational source inspected. KCAF explicitly separates suspicion, expert input, investigation, repair preparation, financing, quotations and execution. Important findings for this page:

- investigation should follow the applicable foundation-investigation guideline and may concern an entire `bouwkundige eenheid`;
- when repair is needed, wishes and requirements can be captured in a `Programma van Eisen`;
- all repair contractors should receive the same information;
- contractors should inspect the relevant parts of all affected homes before pricing;
- quotation comparison is difficult enough that expert support can be useful;
- owner-side costs can include relocated services/sewers, soil disposal, fees, notary, water/electricity, temporary accommodation, process guidance, supervision, zero measurement, structural/finishing repair, garden repair and unforeseen costs;
- execution should include appropriate direction/supervision.

### KCAF — Herstelkostencalculator

Current 2026 tool for an **indicative** repair-cost estimate. It uses property-level inputs such as foundation type, repair method and building size. This is more defensible than publishing one universal national price range on this page.

### KCAF — Funderingsrisico onderzoeken / FAQ

Useful boundary evidence: risk report and QuickScan are not equivalent to full foundation investigation. KCAF advises specialist investigation where needed and notes that the research report contains measurement outcomes and an estimate of the remaining enforcement/maintenance horizon (`handhavingstermijn`).

### Rijksoverheid — Nationale Aanpak Funderingen, 28 August 2026

Current policy context. Foundation repair remains primarily an owner responsibility, but national support is expanding. Owners unable to finance urgent repair through their normal lender can use the Fonds Duurzaam Funderingsherstel subject to its conditions. The government is also improving nationwide information about foundation risk and damage.

### KCAF — Nationaal Funderingsherstel Register, 2026

After validated repair, owners can register the work and supply evidence such as an as-built drawing, permit or invoice. Registration creates a certificate and records the repaired status in the national dataset.

## Coverage matrix

| Need | Existing page | Strong SERP/source coverage | Priority |
|---|---|---|---|
| Explicit handoff: diagnosis page → repair project | PARTIAL | KCAF/VEH | MUST |
| Define what the investigation must tell you before tendering | PARTIAL | KCAF | MUST |
| Explain `bouwkundige eenheid` / shared-owner issue | MISSING | KCAF | MUST |
| Convert investigation into a repair brief / PvE | MISSING | KCAF | MUST |
| Same information and access for every bidder | PARTIAL | KCAF | MUST |
| Compare method rationale, not only price | PARTIAL | KCAF | MUST |
| Separate contractor repair price from total owner-side `stichtingskosten` | MISSING | KCAF | MUST |
| Give a current cost-estimation route without fake national average | MISSING | KCAF calculator | MUST |
| Financing/support context | MISSING | Rijksoverheid | SHOULD |
| Directie/toezicht and zero measurement / handover evidence | PARTIAL | KCAF | MUST |
| Post-repair registration | MISSING | KCAF NHR | SHOULD |
| Acute-safety warning | COVERED | general safety boundary | MUST |
| Avoid method prescriptions without investigation | COVERED | KCAF logic | MUST |

## Information gain selected

### 1. `Herstelklaar dossier`

A repair quotation should not start from symptoms. It starts from a dossier containing the investigation conclusion, scope/building unit, relevant drawings/data, constraints, desired outcome, owner coordination and the items that all bidders must price.

### 2. `PvE before prijs`

Translate the research into a shared Programma van Eisen. Every bidder receives the same information and access. This is the strongest way to prevent false quotation comparison.

### 3. `Aannemersprijs ≠ stichtingskosten`

The contractor's foundation-repair amount is only one part of the owner's total project cost. Make external and consequential costs visible before financing is fixed.

### 4. `Onderzoek → uitvoering → bewijs`

The page should show the closed loop: investigation, repair brief, quotation, execution with supervision, completion/as-built evidence and optional national registration.

## GEO / answer-engine opportunities

Standalone extractable answers should include:

- `Wanneer kun je offertes voor funderingsherstel vergelijken?`
- `Wat moet in een Programma van Eisen voor funderingsherstel staan?`
- `Waarom moeten alle herstelbedrijven dezelfde informatie krijgen?`
- `Welke kosten vallen vaak buiten de herstelofferte?`
- `Wat is het verschil tussen de herstelofferte en de totale stichtingskosten?`
- `Wat leg je na funderingsherstel vast?`

## Cannibalisation check

- `/problemen-oplossen/funderingsproblemen/`: owns symptoms, risk, whether investigation is needed. This page should link back when the user has **no sufficiently clear investigation outcome yet**.
- `/renovatie-plannen/renovatiekosten/`: owns broad cross-project market-cost comparison, not specialist foundation tendering.
- `/vakman-en-offertes/offertes-vergelijken/`: owns generic quotation comparison mechanics. This page owns the foundation-specific input package and technical comparability requirements.
- `/renovatie-plannen/renovatievergunning/`: owns general Dutch permit logic. This page may tell users to check the concrete repair plan, but should not duplicate permit rules.

## Data gaps / claim boundaries

- Do not publish one universal 2026 repair price as if it applies to every home.
- Use the KCAF Herstelkostencalculator as the current indicative-estimate route; an actual price requires project-specific research and quotations.
- Do not prescribe a repair method from foundation type or symptoms alone.
- Do not state that every project requires the same permit, engineering package, temporary relocation or neighbouring-owner arrangement.
- Do not diagnose structural safety remotely.

## Prewrite result

`DEEP_REWRITE`

The current page has the correct high-level principle (research before repair) but overlaps too much with the diagnostic page and lacks the strongest repair-project mechanics found in KCAF guidance. The rewrite must start **after diagnosis** and make the repair project tender-ready.