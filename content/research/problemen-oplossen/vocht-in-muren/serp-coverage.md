# Research coverage — Vocht in muren

- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## Intent
The user has a specific damp wall and needs source localization, not a broad moisture encyclopedia or immediate treatment.

## Evidence
Current Vereniging Eigen Huis problem guides distinguish:
- leakage and hidden leakage;
- condensation on cold surfaces;
- penetrating rain through masonry/facade details;
- low-wall/rising-moisture patterns.

Sources:
- https://www.eigenhuis.nl/problemenwijzer/vochtplekken-muur-plafond
- https://www.eigenhuis.nl/problemenwijzer/lekkages
- https://www.eigenhuis.nl/problemenwijzer/vochtige-binnenmuur

## Information gain
`muurbronkaart` with six coordinates: side, height, shape, timing, weather/activity correlation, adjacent room/service.

## Boundary
Broad differential stays on `/vochtproblemen/`; capillary/rising damp stays on `/opstijgend-vocht/`.
