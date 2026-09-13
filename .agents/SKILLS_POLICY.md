# Skill policy — 80/20

Thuisrenovatie Gids gebruikt dezelfde orkestratiegedachte als `bloc-notes-numerique`: generieke expertise komt uit bestaande skills; custom code blijft beperkt tot domeinspecifieke routing, veiligheid en clustercontrole.

## Huidige verdeling

- Upstream/reused skills: **21**
- Custom skills: **2**
- Totaal: **23**
- Upstream/reused: **91,3%**
- Custom: **8,7%**

De CI faalt zodra custom skills meer dan 20% van het totaal vormen.

## Upstream / reused catalogus

### Reeds aanwezige Rampstack-skills

- `seo-keyword`
- `seo-content-audit`
- `seo-onpage`
- `seo-technical`
- `content-brief-authoring`
- `content-and-copy`
- `editorial-qa`
- `evidence-based-reviews`
- `information-architecture`
- `jtbd-framing`
- `cro-optimization`

### Uit het bestaande `bloc-notes-numerique` editorial engine hergebruikt

- `search-intent`
- `content-refresh`
- `fact-check`
- `affiliate-value`
- `internal-linking-audit`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-best-practices`

Elke reused skill bevat een `upstream` GitHub-URL in de frontmatter. Skills die op een ander domein waren afgestemd zijn inhoudelijk aangepast aan renovatie, maar behouden dezelfde verantwoordelijkheid in de keten.

## Custom catalogus

| Skill | Waarom custom? |
|---|---|
| `renovation-analysis-workflow` | sitebrede audit/cluster/publish orchestration, renovatiegrenzen, safety en structurele similariteit |
| `renovation-content-workflow` | productie-orchestratie, renovatiegrenzen, safety en integratie in de lokale source of truth |

## Verplichte architectuur

De custom workflows mogen geen tweede versie bevatten van methodes die al in de reused skills bestaan. Ze mogen alleen:

1. de juiste skills in de juiste volgorde routeren;
2. beslissingen mappen naar `KEEP / LIGHT_UPDATE / DEEP_REWRITE / MERGE / NOINDEX`;
3. grenzen tussen renovatieclusters bewaken;
4. renovatiespecifieke veiligheids- en actualiteitsrisico's bewaken;
5. clusterbrede structurele cloning detecteren;
6. `PUBLISH_REVIEW` en handoff naar menselijke validatie organiseren.

## Anti-template regel

`PLAN`, `PROJECT`, `SUSTAINABILITY`, `TROUBLESHOOTING`, `DIY`, `LEAD`, `CHOICE`, `EXPLAINER` en `HOW_TO` zijn classificaties of risicogrids. Ze mogen nooit een verplicht redactioneel template worden.

Geen nieuwe custom skill toevoegen tenzij de taak werkelijk sitespecifieke orkestratie vereist én de 80/20-regel na toevoeging nog steeds slaagt.
