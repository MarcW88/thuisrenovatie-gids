# Content brief — Problemen oplossen

- Route: `/problemen-oplossen/`
- Type: `TROUBLESHOOTING_HUB`
- Markt: Nederland
- Workflow version: 2
- Status: `QA_COMPLETE`
- Last source check: 2026-09-13
- Decision: `DEEP_REWRITE`

## Gebruikersjob
Ik zie een probleem in huis en wil bepalen welke diagnostische route logisch is zonder op basis van één symptoom meteen een oorzaak of behandeling te kopen.

## Centrale thesis
**Symptomen zijn observaties, geen diagnoses.** Leg eerst patroon, locatie, timing en verandering vast; bepaal daarna welke hypothese onderzocht moet worden en wanneer deskundige hulp nodig is.

## Ownership
Deze hub owns:
- symptoomrouter;
- `probleemlogboek` voor foto, locatie, timing en verandering;
- urgente stop-/escalatiesignalen;
- route naar juiste diagnostische child.

Children own:
- `/vochtproblemen/`: brede vochttriage;
- `/vocht-in-muren/`: bron van één vochtige muur systematisch verkleinen;
- `/opstijgend-vocht/`: specifieke hypothese capillair/opstijgend vocht onderaan muren;
- `/funderingsproblemen/`: signalen combineren en beslissen wanneer funderingsonderzoek logisch is.

`/renovatieprojecten/fundering/` begint pas **na voldoende diagnose** en owns herstelproject/PvE/offertes.

## MUST
1. Open met `symptoom ≠ oorzaak`.
2. Introduceer `probleemlogboek`: foto + datum, exacte locatie, omvang, timing, weer/gebeurtenis, recente werkzaamheden.
3. Routeer vocht/schimmel eerst naar brede vochttriage wanneer bron onbekend is.
4. Routeer vocht laag in muur alleen naar `opstijgend-vocht` als hypothese, niet als diagnose.
5. Routeer lokale vochtige muur naar patroon-/bronanalyse.
6. Routeer combinatie scheuren/vervorming/verzakking naar funderingssignalen.
7. Benoem veilige eerste controles: ventilatie, zichtbare lekkage, buitenzijde, recente werkzaamheden; geen destructief onderzoek.
8. Stop/escalatie bij snel veranderende constructieve vervorming, grote/terugkerende onbekende vochtproblemen of onveilige situatie.
9. Behandeling/offerte pas nadat oorzaak of onderzoeksvraag voldoende is afgebakend.
10. Geen vochtmeter, scheurvorm of één foto als sluitend bewijs presenteren.

## Information gain
`probleemlogboek` + `bewijssterkte`:
- **observatie**: wat zie je?
- **correlatie**: wanneer verandert het?
- **hypothese**: welke bronnen passen?
- **onderzoeksvraag**: wat moet worden uitgesloten/bevestigd?
- **behandeling**: pas na voldoende diagnose.

## Safety
Geen constructieve veiligheid op afstand goedkeuren, geen chemische vochtbehandeling voorschrijven, geen live-elektrische/gas-/destructieve inspecties als DIY.
