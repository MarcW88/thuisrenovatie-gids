#!/usr/bin/env python3
from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import wrap

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "infographics"

W, H = 1024, 672
BG = "#F7F5F0"
INK = "#202421"
GREEN = "#24483D"
TERRA = "#D86F48"
STONE = "#ECE8DF"
MUTED = "#66706A"
LINE = "#D7D7CF"
WHITE = "#FFFFFF"


def tx(x, y, text, size=20, weight=600, fill=INK, anchor="start", max_chars=None, line_gap=1.2):
    lines = wrap(text, max_chars) if max_chars else [text]
    parts = [f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Inter,Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">']
    for i, line in enumerate(lines):
        dy = 0 if i == 0 else int(size * line_gap)
        parts.append(f'<tspan x="{x}" dy="{dy}">{escape(line)}</tspan>')
    parts.append("</text>")
    return "".join(parts)


def icon(kind, cx, cy, s=1.0):
    sw = 3
    r = 34 * s
    out = [f'<g stroke="{GREEN}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round">']
    if kind == "house":
        out += [
            f'<path d="M {cx-26*s} {cy+6*s} L {cx} {cy-18*s} L {cx+26*s} {cy+6*s}"/>',
            f'<rect x="{cx-20*s}" y="{cy+5*s}" width="{40*s}" height="{30*s}" rx="{2*s}"/>',
            f'<rect x="{cx-6*s}" y="{cy+17*s}" width="{12*s}" height="{18*s}"/>',
        ]
    elif kind == "scope":
        out += [
            f'<rect x="{cx-24*s}" y="{cy-22*s}" width="{48*s}" height="{44*s}" rx="{5*s}"/>',
            f'<path d="M {cx-13*s} {cy-8*s} H {cx+13*s} M {cx-13*s} {cy+3*s} H {cx+8*s} M {cx-13*s} {cy+14*s} H {cx+2*s}"/>',
        ]
    elif kind == "search":
        out += [
            f'<circle cx="{cx-8*s}" cy="{cy-6*s}" r="{17*s}"/>',
            f'<path d="M {cx+4*s} {cy+7*s} L {cx+25*s} {cy+28*s}"/>',
        ]
    elif kind == "document":
        out += [
            f'<path d="M {cx-20*s} {cy-28*s} H {cx+10*s} L {cx+22*s} {cy-16*s} V {cy+30*s} H {cx-20*s} Z"/>',
            f'<path d="M {cx+10*s} {cy-28*s} V {cy-16*s} H {cx+22*s}"/>',
            f'<path d="M {cx-10*s} {cy-3*s} H {cx+11*s} M {cx-10*s} {cy+8*s} H {cx+11*s} M {cx-10*s} {cy+19*s} H {cx+5*s}"/>',
        ]
    elif kind == "money":
        out += [
            f'<circle cx="{cx}" cy="{cy}" r="{25*s}"/>',
        ]
        out.append(tx(cx, cy+8*s, "€", int(27*s), 700, GREEN, "middle"))
    elif kind == "wallet":
        out += [
            f'<rect x="{cx-27*s}" y="{cy-18*s}" width="{54*s}" height="{37*s}" rx="{6*s}"/>',
            f'<path d="M {cx+5*s} {cy-5*s} H {cx+29*s} V {cy+10*s} H {cx+5*s} Q {cx-3*s} {cy+2*s} {cx+5*s} {cy-5*s} Z"/>',
            f'<circle cx="{cx+17*s}" cy="{cy+2*s}" r="{2*s}" fill="{GREEN}"/>',
        ]
    elif kind == "check":
        out += [
            f'<circle cx="{cx}" cy="{cy}" r="{26*s}"/>',
            f'<path d="M {cx-13*s} {cy+1*s} L {cx-3*s} {cy+11*s} L {cx+17*s} {cy-13*s}"/>',
        ]
    elif kind == "layers":
        out += [
            f'<rect x="{cx-25*s}" y="{cy-22*s}" width="{50*s}" height="{12*s}" rx="{2*s}"/>',
            f'<rect x="{cx-20*s}" y="{cy-4*s}" width="{40*s}" height="{12*s}" rx="{2*s}"/>',
            f'<rect x="{cx-15*s}" y="{cy+14*s}" width="{30*s}" height="{12*s}" rx="{2*s}"/>',
        ]
    elif kind == "air":
        out += [
            f'<path d="M {cx-28*s} {cy-14*s} H {cx+8*s} Q {cx+22*s} {cy-14*s} {cx+22*s} {cy-2*s} Q {cx+22*s} {cy+10*s} {cx+8*s} {cy+10*s} H {cx-10*s}"/>',
            f'<path d="M {cx-25*s} {cy+20*s} H {cx+2*s} Q {cx+14*s} {cy+20*s} {cx+14*s} {cy+10*s}"/>',
        ]
    elif kind == "heat":
        out += [
            f'<path d="M {cx-18*s} {cy+24*s} Q {cx-32*s} {cy+6*s} {cx-17*s} {cy-9*s} Q {cx-4*s} {cy-22*s} {cx-10*s} {cy-30*s} Q {cx+14*s} {cy-18*s} {cx+19*s} {cy+1*s} Q {cx+23*s} {cy+20*s} {cx} {cy+31*s}"/>',
            f'<path d="M {cx-5*s} {cy+20*s} Q {cx-12*s} {cy+7*s} {cx+2*s} {cy-4*s} Q {cx+13*s} {cy+8*s} {cx+7*s} {cy+20*s}"/>',
        ]
    elif kind == "sun":
        out += [f'<circle cx="{cx}" cy="{cy}" r="{15*s}"/>']
        for dx, dy in [(0,-28),(0,28),(-28,0),(28,0),(-20,-20),(20,-20),(-20,20),(20,20)]:
            out.append(f'<path d="M {cx+dx*.72*s} {cy+dy*.72*s} L {cx+dx*s} {cy+dy*s}"/>')
    elif kind == "shield":
        out += [
            f'<path d="M {cx} {cy-29*s} L {cx+24*s} {cy-19*s} V {cy+1*s} Q {cx+20*s} {cy+22*s} {cx} {cy+31*s} Q {cx-20*s} {cy+22*s} {cx-24*s} {cy+1*s} V {cy-19*s} Z"/>',
        ]
    elif kind == "drop":
        out += [f'<path d="M {cx} {cy-30*s} C {cx-8*s} {cy-14*s} {cx-22*s} {cy} {cx-22*s} {cy+14*s} A {22*s} {22*s} 0 0 0 {cx+22*s} {cy+14*s} C {cx+22*s} {cy} {cx+8*s} {cy-14*s} {cx} {cy-30*s} Z"/>']
    elif kind == "crack":
        out += [f'<path d="M {cx-16*s} {cy-30*s} L {cx-4*s} {cy-8*s} L {cx-13*s} {cy+3*s} L {cx+4*s} {cy+18*s} L {cx-2*s} {cy+31*s}"/>']
    elif kind == "tools":
        out += [
            f'<path d="M {cx-25*s} {cy+22*s} L {cx+14*s} {cy-17*s}"/>',
            f'<path d="M {cx+7*s} {cy-24*s} Q {cx+25*s} {cy-31*s} {cx+29*s} {cy-13*s} L {cx+16*s} {cy}"/>',
            f'<circle cx="{cx-17*s}" cy="{cy+15*s}" r="{7*s}"/>',
        ]
    elif kind == "bolt":
        out += [f'<path d="M {cx+5*s} {cy-31*s} L {cx-16*s} {cy+5*s} H {cx-1*s} L {cx-8*s} {cy+31*s} L {cx+18*s} {cy-8*s} H {cx+3*s} Z"/>']
    elif kind == "roof":
        out += [
            f'<path d="M {cx-30*s} {cy+2*s} L {cx} {cy-24*s} L {cx+30*s} {cy+2*s}"/>',
            f'<path d="M {cx-21*s} {cy+2*s} V {cy+28*s} H {cx+21*s} V {cy+2*s}"/>',
        ]
    elif kind == "panel":
        out += [
            f'<path d="M {cx-30*s} {cy-20*s} H {cx+28*s} L {cx+21*s} {cy+20*s} H {cx-37*s} Z"/>',
            f'<path d="M {cx-17*s} {cy-20*s} L {cx-24*s} {cy+20*s} M {cx-2*s} {cy-20*s} L {cx-9*s} {cy+20*s} M {cx+13*s} {cy-20*s} L {cx+6*s} {cy+20*s} M {cx-33*s} {cy} H {cx+24*s}"/>',
        ]
    elif kind == "clock":
        out += [f'<circle cx="{cx}" cy="{cy}" r="{27*s}"/>', f'<path d="M {cx} {cy-14*s} V {cy+2*s} L {cx+12*s} {cy+10*s}"/>']
    elif kind == "wrench":
        out += [
            f'<path d="M {cx-25*s} {cy+24*s} L {cx+3*s} {cy-4*s}"/>',
            f'<path d="M {cx+2*s} {cy-5*s} Q {cx+18*s} {cy-28*s} {cx+30*s} {cy-13*s} L {cx+17*s} {cy} L {cx+28*s} {cy+11*s} Q {cx+13*s} {cy+25*s} {cx-3*s} {cy+7*s}"/>',
        ]
    else:
        out += [f'<circle cx="{cx}" cy="{cy}" r="{r}"/>']
    out.append("</g>")
    return "".join(out)


def frame(title, subtitle):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">',
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
        f'<path d="M42 0 V94 M58 0 V132" stroke="{GREEN}" stroke-width="2" opacity=".55"/>',
        f'<path d="M982 {H} V{H-94} M966 {H} V{H-132}" stroke="{GREEN}" stroke-width="2" opacity=".55"/>',
        tx(64, 64, title, 31, 700, GREEN),
        tx(64, 96, subtitle, 16, 400, MUTED),
        f'<line x1="64" y1="118" x2="960" y2="118" stroke="{LINE}" stroke-width="1"/>',
    ]


def end(parts):
    parts.append("</svg>")
    return "\n".join(parts)


def timeline(title, subtitle, items):
    p = frame(title, subtitle)
    n = len(items)
    if n <= 6:
        y = 285
        start = 112
        gap = (912 - start) / max(1, n - 1)
        for i, item in enumerate(items):
            x = start + i*gap
            if i < n-1:
                p.append(f'<path d="M {x+56} {y} H {x+gap-56}" stroke="{TERRA}" stroke-width="3" marker-end="url(#a)"/>')
        p.insert(1, f'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="{TERRA}"/></marker></defs>')
        for i, (label, kind) in enumerate(items):
            x = start + i*gap
            p.append(f'<circle cx="{x}" cy="{y}" r="54" fill="{WHITE}" stroke="{GREEN}" stroke-width="4"/>')
            p.append(icon(kind, x, y, .58))
            p.append(f'<circle cx="{x-38}" cy="{y-42}" r="18" fill="{TERRA}"/>')
            p.append(tx(x-38, y-36, str(i+1), 14, 700, WHITE, "middle"))
            p.append(tx(x, y+88, label, 18, 700, INK, "middle", 15))
    else:
        cols = 3 if n >= 8 else 4
        cell_w = 286 if cols == 3 else 212
        start_x = 94
        start_y = 210
        row_gap = 178
        for i, (label, kind) in enumerate(items):
            row, col = divmod(i, cols)
            x = start_x + col*cell_w
            y = start_y + row*row_gap
            p.append(f'<rect x="{x}" y="{y}" width="{cell_w-24}" height="132" rx="18" fill="{WHITE}" stroke="{LINE}"/>')
            p.append(f'<circle cx="{x+46}" cy="{y+48}" r="31" fill="{STONE}"/>')
            p.append(icon(kind, x+46, y+48, .45))
            p.append(tx(x+88, y+42, f"{i+1:02d}", 13, 700, TERRA))
            p.append(tx(x+88, y+70, label, 17, 700, INK, "start", 19))
    return end(p)


def grid(title, subtitle, items, cols=3):
    p = frame(title, subtitle)
    if cols == 3:
        cell_w, start_x, gap_x, label_chars, sub_chars = 286, 72, 28, 18, 22
    elif cols == 2:
        cell_w, start_x, gap_x, label_chars, sub_chars = 410, 82, 40, 28, 36
    else:
        cell_w, start_x, gap_x, label_chars, sub_chars = 210, 72, 28, 18, 22
    cell_h = 188 if len(items) <= 6 else 150
    start_y = 158
    gap_y = 24
    for i, (label, sub, kind) in enumerate(items):
        row, col = divmod(i, cols)
        x = start_x + col*(cell_w+gap_x)
        y = start_y + row*(cell_h+gap_y)
        p.append(f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" rx="22" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(f'<rect x="{x}" y="{y}" width="7" height="{cell_h}" rx="3.5" fill="{TERRA if i%2 else GREEN}"/>')
        p.append(f'<circle cx="{x+54}" cy="{y+58}" r="34" fill="{STONE}"/>')
        p.append(icon(kind, x+54, y+58, .47))
        p.append(tx(x+100, y+48, label, 18, 700, GREEN, "start", label_chars))
        p.append(tx(x+100, y+92, sub, 14, 400, MUTED, "start", sub_chars))
    return end(p)


def matrix(title, subtitle, items):
    p = frame(title, subtitle)
    x0, y0, cw, ch = 82, 168, 410, 205
    coords=[(x0,y0),(x0+430,y0),(x0,y0+225),(x0+430,y0+225)]
    for i,(label,sub,kind) in enumerate(items):
        x,y=coords[i]
        p.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="24" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{x+70}" cy="{y+74}" r="42" fill="{STONE}"/>')
        p.append(icon(kind,x+70,y+74,.58))
        p.append(tx(x+132,y+66,label,20,700,GREEN,"start",22))
        p.append(tx(x+132,y+110,sub,14,400,MUTED,"start",30))
        p.append(f'<text x="{x+350}" y="{y+55}" font-family="Inter,Arial,sans-serif" font-size="13" font-weight="700" fill="{TERRA}">0{i+1}</text>')
    return end(p)


def budget(title, subtitle):
    p=frame(title,subtitle)
    p.append(f'<rect x="86" y="166" width="852" height="72" rx="20" fill="{GREEN}"/>')
    p.append(tx(118,194,"Budgetplafond",13,700,"#C9D7D1"))
    p.append(tx(118,220,"Jouw maximale grens",21,700,WHITE))
    items=[("Vastgelegd","Getekende opdrachten en bestellingen","document"),("Verwacht","Nog niet definitief geprijsd","money"),("Projectreserve","Voor onzekerheden en wijzigingen","shield"),("Vrije ruimte","Nog niet toegewezen budget","wallet")]
    x=86
    for i,(label,sub,kind) in enumerate(items):
        y=272 + (i//2)*154
        xx=x+(i%2)*430
        p.append(f'<rect x="{xx}" y="{y}" width="412" height="132" rx="20" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{xx+58}" cy="{y+66}" r="36" fill="{STONE}"/>')
        p.append(icon(kind,xx+58,y+66,.5))
        p.append(tx(xx+112,y+56,label,19,700,GREEN))
        p.append(tx(xx+112,y+84,sub,14,400,MUTED,"start",29))
        p.append(tx(xx+372,y+38,f"0{i+1}",12,700,TERRA,"middle"))
    return end(p)


def decision(title, subtitle):
    p=frame(title,subtitle)
    p.append(f'<rect x="120" y="166" width="300" height="110" rx="24" fill="{WHITE}" stroke="{GREEN}" stroke-width="3"/>')
    p.append(icon("house",175,220,.6))
    p.append(tx(225,210,"Project + locatie",20,700,GREEN))
    p.append(tx(225,240,"Concrete werkzaamheden",14,400,MUTED))
    p.append(f'<path d="M430 220 H582" stroke="{TERRA}" stroke-width="4" marker-end="url(#b)"/>')
    p.insert(1,f'<defs><marker id="b" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{TERRA}"/></marker></defs>')
    p.append(f'<rect x="590" y="166" width="300" height="110" rx="24" fill="{GREEN}"/>')
    p.append(icon("check",646,220,.55))
    p.append(tx(700,210,"Officiële",19,700,WHITE))
    p.append(tx(700,238,"Vergunningscheck",19,700,WHITE))
    outcomes=["Geen indieningsactie","Informatieplicht","Melding","Vergunning"]
    for i,label in enumerate(outcomes):
        x=80+i*230
        p.append(f'<rect x="{x}" y="350" width="206" height="132" rx="20" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{x+103}" cy="382" r="16" fill="{TERRA}"/>')
        p.append(tx(x+103,387,str(i+1),12,700,WHITE,"middle"))
        p.append(tx(x+103,430,label,16,700,GREEN,"middle",20))
    p.append(tx(512,548,"De uitkomst hangt af van locatie, werkzaamheden en actuele regels.",14,400,MUTED,"middle"))
    return end(p)


def airflow(title, subtitle):
    p=frame(title,subtitle)
    zones=[("Toevoer","Woonkamer & slaapkamers","air"),("Doorstroom","Hal, overloop & deuropeningen","house"),("Afvoer","Keuken, badkamer & toilet","air")]
    xs=[92,372,652]
    for i,(label,sub,kind) in enumerate(zones):
        x=xs[i]
        p.append(f'<rect x="{x}" y="190" width="240" height="250" rx="28" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{x+120}" cy="260" r="48" fill="{STONE}"/>')
        p.append(icon(kind,x+120,260,.68))
        p.append(tx(x+120,340,label,21,700,GREEN,"middle"))
        p.append(tx(x+120,378,sub,14,400,MUTED,"middle",25))
        if i<2:
            p.append(f'<path d="M{x+248} 315 H{x+272}" stroke="{TERRA}" stroke-width="4"/>')
            p.append(f'<path d="M{x+264} 305 L{x+278} 315 L{x+264} 325" fill="none" stroke="{TERRA}" stroke-width="4"/>')
    p.append(tx(512,520,"Conceptuele luchtweg — geen installatieplan",14,600,TERRA,"middle"))
    return end(p)


def layers(title, subtitle):
    p=frame(title,subtitle)
    labels=[("Schil","Isolatie en glas","layers"),("Ventilatie","Toevoer, doorstroom en afvoer","air"),("Verwarming","Warmtevraag, afgifte en regeling","heat"),("Opwekking","Duurzame elektriciteit en warmte","sun")]
    widths=[800,700,600,500]
    for i,(label,sub,kind) in enumerate(labels):
        w=widths[i]; x=(W-w)//2; y=160+i*110
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="86" rx="24" fill="{WHITE}" stroke="{GREEN if i==0 else LINE}" stroke-width="{3 if i==0 else 1}"/>')
        p.append(f'<circle cx="{x+54}" cy="{y+43}" r="30" fill="{STONE}"/>')
        p.append(icon(kind,x+54,y+43,.42))
        p.append(tx(x+100,y+37,f"0{i+1}  {label}",18,700,GREEN))
        p.append(tx(x+100,y+64,sub,14,400,MUTED))
    p.append(tx(512,624,"Geen universele volgorde: vertrek van de toestand van je woning.",14,500,MUTED,"middle"))
    return end(p)


def criteria(title, subtitle):
    p=frame(title,subtitle)
    rows=[("Veiligheid","Laag risico","Hoog risico"),("Foutkosten","Eenvoudig herstelbaar","Duur of verborgen herstel"),("Vaardigheid","Bekend en controleerbaar","Specialistische kennis"),("Planning","Weinig afhankelijkheden","Blokkeert andere vakmensen"),("Verantwoordelijkheid","Geen keuring/garantie-impact","Keuring, garantie of aansprakelijkheid")]
    y=158
    for i,(label,left,right) in enumerate(rows):
        p.append(f'<rect x="80" y="{y}" width="864" height="78" rx="16" fill="{WHITE}" stroke="{LINE}"/>')
        p.append(tx(108,y+31,label,16,700,GREEN))
        p.append(tx(350,y+30,left,13,500,MUTED,"middle",20))
        p.append(f'<line x1="520" y1="{y+39}" x2="694" y2="{y+39}" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>')
        p.append(f'<circle cx="{552+i*26}" cy="{y+39}" r="9" fill="{TERRA}"/>')
        p.append(tx(830,y+30,right,13,500,MUTED,"middle",22))
        y+=88
    p.append(tx(160,625,"Eerder zelf doen",13,700,GREEN))
    p.append(tx(864,625,"Eerder uitbesteden",13,700,TERRA,"end"))
    return end(p)


SPECS = {
    "energie-besparen-hierarchy": lambda: timeline("Energie besparen", "Van eenvoudige ingrepen naar structurele maatregelen", [("Gedrag & instellingen","scope"),("Isolatie & glas","layers"),("Ventilatie","air"),("Verwarming","heat"),("Opwekking","sun")]),
    "fundering-proces": lambda: timeline("Funderingsherstel", "Van onderzoek naar controle en dossier", [("Onderzoek","search"),("Eisen & scope","scope"),("Offertes","document"),("Uitvoering","tools"),("Controle & dossier","check")]),
    "funderingsproblemen-signalen": lambda: grid("Mogelijke funderingssignalen", "Eén signaal op zichzelf bewijst geen funderingsprobleem", [("Scheuren","Patroon, breedte en verandering","crack"),("Deuren & ramen","Klemmen of uit lijn raken","house"),("Vloerniveau","Zichtbare of voelbare scheefstand","layers"),("Gevel & maaiveld","Verzakking of vervorming","house"),("Omgeving","Afwatering en aangrenzende panden","drop")], 3),
    "offerte-controleren-checklist": lambda: grid("Offerte controleren", "Vergelijk inhoud en voorwaarden, niet alleen het totaalbedrag", [("Scope","Wat wordt precies uitgevoerd?","scope"),("Hoeveelheden","Welke aantallen en maten?","document"),("Materialen","Welke kwaliteit en keuzes?","layers"),("Uitsluitingen","Wat zit er niet in?","search"),("Planning","Start, duur en afhankelijkheden","clock"),("Voorwaarden","Betaling, meerwerk en garantie","check")], 3),
    "opstijgend-vocht-bronnen": lambda: grid("Lage vochtplek: mogelijke bronnen", "De plek alleen bewijst de oorzaak niet", [("Bodemvocht","Capillaire route via materiaal","drop"),("Regeninslag","Gevel of aansluiting","drop"),("Leidinglek","Water- of afvoerleiding","wrench"),("Vloer / kruipruimte","Vocht uit aangrenzende bouwlaag","layers"),("Condensatie","Koud oppervlak en binnenklimaat","air"),("Detailaansluiting","Lokale bouwkundige route","house")], 3),
    "problemen-oplossen-diagnostic-flow": lambda: timeline("Problemen oplossen", "Van zichtbaar signaal naar gerichte interventie", [("Signaal vastleggen","document"),("Observeren","search"),("Hypotheses","scope"),("Gericht onderzoeken","search"),("Interventie kiezen","tools")]),
    "rendement-renovatie-value-matrix": lambda: matrix("Renovatierendement", "Waarde is breder dan financiële terugverdientijd", [("Woningwaarde","Bruikbaarheid en marktwaarde","house"),("Energie","Verbruik en structurele lasten","sun"),("Comfort","Temperatuur, geluid en gebruik","heat"),("Onderhoud & risico","Vermeden herstel en toekomstbestendigheid","shield")]),
    "renovatie-budget-reserve": lambda: budget("Renovatiebudget", "Houd plafond, verplichtingen, verwachtingen en reserve uit elkaar"),
    "renovatie-plannen-roadmap": lambda: timeline("Renovatie plannen", "Zes beslisvragen die je project sturen", [("Scope","scope"),("Volgorde","layers"),("Kosten","money"),("Budget","wallet"),("Regels","document"),("Waarde","check")]),
    "renovatie-volgorde-visual": lambda: timeline("Renovatievolgorde", "Eerst ruw en verborgen, daarna dicht en afgewerkt", [("Blokkades oplossen","search"),("Sloop","tools"),("Constructie & buitenschil","house"),("Leidingen & installaties","wrench"),("Isolatie & opbouw","layers"),("Ondergronden & droogwerk","layers"),("Vaste inrichting & vloeren","house"),("Afmontage","tools"),("Testen & opleveren","check")]),
    "renovatiefasen-roadmap": lambda: timeline("Renovatiefasen", "Zeven beslismomenten van idee tot oplevering", [("Inventarisatie","search"),("Ontwerp & scope","scope"),("Haalbaarheid","check"),("Begroting & contractering","money"),("Uitvoeringsvoorbereiding","document"),("Uitvoering & wijzigingen","tools"),("Oplevering","check")]),
    "renovatiekosten-cost-structure": lambda: grid("Waaruit bestaan renovatiekosten?", "De verhouding verschilt per project — geen vaste percentages", [("Constructie","Sloop, draagwerk en bouwkundige ingrepen","house"),("Installaties","Elektra, water, verwarming en ventilatie","wrench"),("Afwerking","Materialen en zichtwerk","layers"),("Arbeid","Montage en uitvoeringsuren","tools"),("Advies & ontwerp","Onderzoek, berekening en voorbereiding","document"),("Projectkosten & reserve","Logistiek, voorzieningen en onzekerheid","wallet")], 3),
    "renovatievergunning-decision-flow": lambda: decision("Vergunning of melding?", "Controleer altijd locatie én concrete werkzaamheden"),
    "subsidies-renovatie-aid-map": lambda: timeline("Subsidie controleren", "Niet alleen de maatregel bepaalt of steun mogelijk is", [("Maatregel","tools"),("Product & eisen","check"),("Uitvoerdatum","clock"),("Combinaties","layers"),("Bewijsstukken","document")]),
    "ventilatie-luchtstroom": lambda: airflow("Ventilatie", "Van verblijfsruimtes naar natte ruimtes"),
    "verduurzamen-layers": lambda: layers("Woning verduurzamen", "Vier systemen die elkaar beïnvloeden"),
    "vocht-in-muren-bronnen": lambda: grid("Vocht in muren: mogelijke bronnen", "Toets de bron aan patroon, locatie en omstandigheden", [("Regeninslag","Gevel, dakrand of aansluiting","drop"),("Leidinglek","Water, afvoer of installatie","wrench"),("Condensatie","Koud vlak en binnenvocht","air"),("Vloer / kruipruimte","Vocht uit aangrenzende zone","layers"),("Capillaire route","Vochttransport door poreus materiaal","drop"),("Bouwdetail","Lokale aansluiting of onderbreking","house")], 3),
    "warmtepomp-diy-veiligheidsgrenzen": lambda: grid("Warmtepomp: veiligheidsgrenzen", "Vier domeinen die professionele beoordeling kunnen vereisen", [("Koudemiddelcircuit","Gecertificeerd werk kan verplicht zijn","shield"),("Elektrische aansluiting","Beveiliging, voeding en aansluiting","bolt"),("Hydraulisch circuit","Verwarming, debiet en inregeling","wrench"),("Dimensionering & inbedrijfstelling","Vermogen, regeling en controle","check")], 2),
    "zelf-doen-of-uitbesteden-matrix": lambda: criteria("Zelf doen of uitbesteden?", "Beoordeel de taak, niet het hele project"),
    "zonnepanelen-diy-veiligheidsgrenzen": lambda: grid("Zonnepanelen: veiligheidsgrenzen", "Voorbereiding en uitvoering zijn niet hetzelfde", [("Werken op hoogte","Daktoegang, valrisico en bevestiging","roof"),("DC-zijde","Panelen, connectoren en gelijkspanning","panel"),("Groepenkast","Beveiliging en elektrische installatie","bolt"),("Netaansluiting & inbedrijfstelling","Controle en correcte ingebruikname","check")], 2),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, builder in SPECS.items():
        (OUT / f"{name}.svg").write_text(builder(), encoding="utf-8")
    print(f"Generated {len(SPECS)} controlled SVG infographics in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
