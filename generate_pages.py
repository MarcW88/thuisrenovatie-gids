#!/usr/bin/env python3
import os

def page(path, title, desc, cat, h1, body, related):
    rel = "\n".join(f'<a href="{h}" class="related-card"><h3>{t}</h3><p>{d}</p></a>' for h,t,d in related)
    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<header><nav class="container">
<div class="logo"><a href="/">Thuisrenovatie Gids</a></div>
<ul class="nav-menu">
<li><a href="/veranda/">Veranda</a></li>
<li><a href="/isolatie/">Isolatie</a></li>
</ul>
</nav></header>
<main><article class="article"><div class="container">
<div class="article-header">
<span class="article-category">{cat}</span>
<h1>{h1}</h1>
</div>
<div class="article-content">
{body}
</div>
<div class="related-articles">
<h2>Verwante artikelen</h2>
<div class="related-grid">{rel}</div>
</div>
</div></article></main>
<footer><div class="container">
<div class="footer-bottom"><p>&copy; 2026 Thuisrenovatie Gids</p></div>
</div></footer>
</body></html>"""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print(f"OK: {path.split('thuisrenovatie-gids/')[-1]}")

B = "/Users/marc/Desktop/thuisrenovatie-gids"
V = f"{B}/veranda"

# ── TYPE VERANDA & CONCEPT ────────────────────────────────────────────────────

page(f"{V}/type-en-concept/soorten-veranda/index.html",
"Soorten veranda's: aluminium, hout, kunststof en staal vergeleken",
"Vergelijk aluminium, hout, kunststof en staal op kosten, onderhoud en duurzaamheid.",
"Type veranda","Soorten veranda's: aluminium, hout, kunststof en staal vergeleken","""
<p>De keuze van het bouwmateriaal bepaalt het uiterlijk, de prijs en het onderhoud van je veranda. We vergelijken de vier populairste opties.</p>
<h2>Aluminium</h2><p>Het meest populaire materiaal. Duurzaam, onderhoudsarm en beschikbaar in alle RAL-kleuren. Slanke profielen zorgen voor maximale glasoppervlakken. <strong>Prijs: €2.500–€4.000/m²</strong></p>
<h2>Hout</h2><p>Warme, tijdloze uitstraling. Ideaal bij landelijke of klassieke woningen. Vereist om de 3–5 jaar schilderen of beitsen. <strong>Prijs: €2.000–€3.000/m²</strong></p>
<h2>Kunststof (PVC)</h2><p>Meest betaalbaar. Volledig onderhoudsvrij, maar profielen zijn dikker dan aluminium. <strong>Prijs: €1.500–€2.500/m²</strong></p>
<h2>Staal</h2><p>Voor industrieel en minimalistisch design. Ultra slanke profielen mogelijk, maar roestgevoelig en duurder. <strong>Prijs: €3.000–€5.000/m²</strong></p>
<h2>Vergelijking op een rij</h2>
<table style="width:100%;border-collapse:collapse;font-size:.9rem;margin:1rem 0">
<tr style="background:#f0f7e6"><th style="padding:.6rem;border:1px solid #ddd;text-align:left">Materiaal</th><th style="padding:.6rem;border:1px solid #ddd">Prijs</th><th style="padding:.6rem;border:1px solid #ddd">Onderhoud</th><th style="padding:.6rem;border:1px solid #ddd">Levensduur</th></tr>
<tr><td style="padding:.6rem;border:1px solid #ddd">Aluminium</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€€€</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Minimaal</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">30–50 jr</td></tr>
<tr style="background:#fafafa"><td style="padding:.6rem;border:1px solid #ddd">Hout</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€€</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Hoog</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">20–40 jr</td></tr>
<tr><td style="padding:.6rem;border:1px solid #ddd">Kunststof</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Minimaal</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">20–30 jr</td></tr>
<tr style="background:#fafafa"><td style="padding:.6rem;border:1px solid #ddd">Staal</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€€€€</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Middel</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">25–40 jr</td></tr>
</table>
<p><strong>Tip:</strong> Kies aluminium voor minimaal onderhoud, hout voor uitstraling, PVC voor budget en staal voor design.</p>
""",
[("/veranda/type-en-concept/moderne-vs-klassieke-veranda/","Moderne vs. klassieke veranda","Welke stijl past bij jou?"),
 ("/veranda/type-en-concept/veranda-plat-dak-vs-zadeldak/","Plat dak vs. zadeldak","Vergelijk de dakvormen"),
 ("/veranda/veranda-bouwen-renoveren/","Complete veranda gids","Kosten, materialen en vergunningen")])

page(f"{V}/type-en-concept/moderne-vs-klassieke-veranda/index.html",
"Moderne veranda vs. klassieke veranda: welke stijl past bij jouw huis?",
"Moderne of klassieke veranda? Vergelijk stijlen, materialen en kosten.",
"Type veranda","Moderne veranda vs. klassieke veranda: welke stijl past bij jouw huis?","""
<p>De stijlkeuze van je veranda bepaalt niet alleen de esthetiek, maar ook de materialen, de prijs en het onderhoud. Moderne en klassieke veranda's zijn fundamenteel verschillende producten.</p>
<h2>De moderne veranda</h2>
<p>Strakke lijnen, grote glasvlakken, zwarte of antraciet aluminium of stalen profielen. Plat dak of minimale daklijn. Past perfect bij kubistische woningen en nieuwbouw.</p>
<ul><li>Aluminium of staal — slanke profielen</li><li>Schuif- of harmonicadeuren voor open gevoel</li><li>Kleurpalet: zwart, antraciet, wit, betonlook</li><li>Prijs: €3.000–€5.000/m²</li></ul>
<h2>De klassieke veranda</h2>
<p>Warme uitstraling, houten of wit aluminium profielen, zadeldak met dakpannen, sierlijke details. Tijdloos en perfect bij jaren-30 woningen en landhuizen.</p>
<ul><li>Hout of wit aluminium</li><li>Zadeldak of mansardedak</li><li>Kleurpalet: crème, naturel, klassiek groen</li><li>Prijs: €2.000–€4.000/m²</li></ul>
<h2>Welke stijl past bij jouw woning?</h2>
<p>Laat de architectuur van je woning leidend zijn. Een moderne veranda bij een traditioneel rijtjeshuis kan de waarde negatief beïnvloeden. Controleer ook de welstandseisen van je gemeente.</p>
<ul><li><strong>Nieuwbouw, kubistisch:</strong> Moderne veranda</li><li><strong>Jaren-30, landelijk, traditioneel:</strong> Klassieke veranda</li><li><strong>Combinatie:</strong> Klassiek volume + moderne details (zwarte profielen in houten kader)</li></ul>
""",
[("/veranda/type-en-concept/soorten-veranda/","Soorten veranda materialen","Aluminium, hout, kunststof, staal"),
 ("/veranda/type-en-concept/serre-tuinkamer-of-veranda/","Serre, tuinkamer of veranda?","Wat zijn de verschillen?"),
 ("/veranda/veranda-bouwen-renoveren/","Complete veranda gids","Kosten, materialen en vergunningen")])

page(f"{V}/type-en-concept/veranda-als-leefruimte/index.html",
"Veranda als leefruimte: woonkameruitbreiding het hele jaar door",
"Hoe maak je van een veranda een volwaardige leefruimte? Tips voor isolatie, verwarming en inrichting.",
"Type veranda","Veranda als leefruimte: woonkameruitbreiding het hele jaar door","""
<p>Een veranda als extra woonkamer is de populairste manier om woonoppervlak te winnen. Met de juiste isolatie en verwarming geniet je er het hele jaar van.</p>
<h2>Wat maakt een veranda bewoonbaar?</h2>
<ul><li><strong>Isolatie:</strong> HR++ of triple glas, geïsoleerd dak (Rd ≥ 3,5), geïsoleerde vloer</li><li><strong>Verwarming:</strong> Aansluiting op cv, vloerverwarming of warmtepomp-airco</li><li><strong>Verbinding:</strong> Schuifpui of harmonicadeur die de veranda met de woonkamer verbindt</li></ul>
<h2>De open verbinding creëren</h2>
<p>Verwijder de buitenmuur of installeer een brede schuifpui. Dit vereist vaak een omgevingsvergunning. Laat de verbinding altijd door een constructeur beoordelen.</p>
<h2>Inrichting tips</h2>
<ul><li>Bank en fauteuils in UV-bestendige stof</li><li>Vloerkleed om de ruimte te definiëren</li><li>Dimbare verlichting voor sfeer</li><li>Planten voor het groene gevoel</li></ul>
<h2>Kosten</h2>
<p>Reken op €25.000–€60.000 voor een jaarrond bewoonbare veranda van 15–25 m², inclusief constructie, glas, vloerverwarming, schuifpui en afwerking.</p>
<h2>Waardestijging</h2>
<p>Een kwalitatieve veranda verhoogt de woningwaarde met 5–10%. Laat dit vastleggen in een taxatie voor hypotheekdoeleinden.</p>
""",
[("/veranda/type-en-concept/veranda-als-keukenuitbreiding/","Veranda als keuken","Tips en ventilatievereisten"),
 ("/veranda/isolatie-comfort-techniek/veranda-verwarmen/","Veranda verwarmen","Vloerverwarming, radiatoren en airco"),
 ("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer")])

page(f"{V}/type-en-concept/veranda-als-keukenuitbreiding/index.html",
"Veranda als keukenuitbreiding: ventilatie, indeling en materialen",
"Keuken uitbreiden met een veranda? Alles over ventilatie, condensatie en de juiste indeling.",
"Type veranda","Veranda als keukenuitbreiding: ventilatie, indeling en materialen","""
<p>Een veranda bij de keuken brengt daglicht, ruimte en een directe verbinding met de tuin. Maar een keukenomgeving stelt extra eisen aan ventilatie en materiaalgebruik.</p>
<h2>De ventilatie-uitdaging</h2>
<p>Koken produceert damp, warmte en geuren. Zonder goede ventilatie ontstaat condens op het glas en schimmel op termijn.</p>
<ul><li><strong>Afzuigkap:</strong> Minimaal 600 m³/h, bij voorkeur met directe buitenafvoer</li><li><strong>Dakramen met klep:</strong> Natuurlijke luchtcirculatie</li><li><strong>WTW-unit:</strong> Mechanische ventilatie met warmteterugwinning</li></ul>
<h2>Condensatie voorkomen</h2>
<ul><li>Triple glas: minder koudebrug = minder condensatie</li><li>Verwarming langs het glas (vloerverwarming of radiator onder raam)</li><li>Goede dakafdichting en isolatie</li></ul>
<h2>Populaire indelingen</h2>
<ul><li><strong>Kookeiland in bestaande keuken + eethoek in veranda</strong></li><li><strong>Volledige keuken in de veranda</strong> (maximaal licht)</li><li><strong>Schuifpui als verbinding</strong> voor een flexibele indeling</li></ul>
<h2>Materialen</h2>
<ul><li>Vloer: keramische tegels of betonlook PVC (waterbestendig)</li><li>Profielen: aluminium (roestvrij, eenvoudig te reinigen)</li><li>Glas: gelaagd veiligheidsglas</li></ul>
<h2>Kostenschatting</h2>
<p>Veranda 12–18 m² + ventilatie: €22.000–€40.000. Inclusief keukenverplaatsing: €30.000–€60.000.</p>
""",
[("/veranda/type-en-concept/veranda-als-leefruimte/","Veranda als leefruimte","Woonkamer het hele jaar"),
 ("/veranda/isolatie-comfort-techniek/veranda-ventilatie/","Ventilatie in veranda","Condens en schimmel voorkomen"),
 ("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer")])

page(f"{V}/type-en-concept/veranda-als-thuiskantoor/index.html",
"Veranda als thuiskantoor: akoestiek, licht en temperatuur",
"Gebruik je veranda als thuiskantoor. Tips voor akoestiek, lichtbeheer, temperatuurregeling en ergonomie.",
"Type veranda","Veranda als thuiskantoor: akoestiek, licht en temperatuur","""
<p>Een veranda als werkplek combineert daglicht, rustige sfeer en een gevoel van buiten zijn. Maar glas weerkaaist geluid en warmte. Hier lees je hoe je dat aanpakt.</p>
<h2>Akoestiek</h2>
<p>Glas weerkaatst geluid, waardoor een veranda echoërig kan zijn. Oplossingen:</p>
<ul><li>Zachte materialen: tapijt, gordijnen, zachte meubels</li><li>Akoestische wandpanelen of plafondtegels</li><li>Gevulde boekenkasten als geluiddemper</li></ul>
<h2>Licht en beeldschermen</h2>
<ul><li>Plaats bureau <strong>loodrecht op het raam</strong>, niet ervoor of erachter</li><li>Zonwerend glas of screens om schittering te beperken</li><li>Dimbare buitenzonwering voor optimale controle</li></ul>
<h2>Temperatuur</h2>
<ul><li><strong>Warmtepomp-airco:</strong> Koelt in zomer, verwarmt in winter</li><li><strong>Buitenzonwering:</strong> Werkt beter dan binnenzonwering</li><li><strong>Dakramen met klep:</strong> Warme lucht kan ontsnappen</li></ul>
<h2>Elektra en internet</h2>
<ul><li>Minimum 4–6 stopcontacten</li><li>Trek een UTP-kabel voor stabiel internet (wifi is minder stabiel in glazen ruimtes)</li><li>Aparte groep in meterkast</li></ul>
""",
[("/veranda/isolatie-comfort-techniek/zonwering-voor-veranda/","Zonwering voor veranda","Screens, lamellen en dakzonwering"),
 ("/veranda/isolatie-comfort-techniek/veranda-warm-winter-koel-zomer/","Veranda koel houden in zomer","Tips en technieken"),
 ("/veranda/type-en-concept/veranda-als-leefruimte/","Veranda als leefruimte","Jaarrond bewoonbaar")])

page(f"{V}/type-en-concept/veranda-schuifdeuren-vs-harmonicadeuren/index.html",
"Veranda met schuifdeuren vs. harmonicadeuren: wat kies je?",
"Schuifdeuren of harmonicadeuren voor je veranda? Vergelijk opening, prijs, isolatie en gebruiksgemak.",
"Type veranda","Veranda met schuifdeuren vs. harmonicadeuren: wat kies je?","""
<p>Schuifdeuren en harmonicadeuren (bi-fold) zijn de twee populairste keuzes voor de overgang tussen veranda en tuin of woning. Ze bieden beide een open verbinding, maar op fundamenteel verschillende manieren.</p>
<h2>Schuifdeuren</h2>
<p>Panelen die horizontaal schuiven. Vereisen weinig ruimte, zijn luchtdicht en elegant.</p>
<ul><li>Opening: max. ~50% van de breedte</li><li>Betere isolatiewaarde (luchtdichter)</li><li>Lagere prijs dan harmonicadeuren</li><li>Minder onderhoud</li></ul>
<h2>Harmonicadeuren (bi-fold)</h2>
<p>Panelen die als een accordeon vouwen en opzij schuiven. Spectaculair open gevoel bij grote openingen.</p>
<ul><li>Opening: tot ~100% van de breedte</li><li>Ideaal voor openingen van 4–8 meter</li><li>Hogere prijs (+€1.500–€2.500/m²)</li><li>Complexer mechanisme, meer onderhoud</li></ul>
<h2>Wanneer wat kiezen?</h2>
<ul><li><strong>Schuifdeuren:</strong> Kleiner budget, isolatie prioriteit, openingen tot 5m, minimalistische look</li><li><strong>Harmonicadeuren:</strong> Maximale opening gewenst, grote overgang met tuin, groter budget</li></ul>
""",
[("/veranda/type-en-concept/soorten-veranda/","Soorten veranda materialen","Aluminium, hout, kunststof, staal"),
 ("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer"),
 ("/veranda/veranda-bouwen-renoveren/","Complete veranda gids","Kosten en vergunningen")])

page(f"{V}/type-en-concept/veranda-plat-dak-vs-zadeldak/index.html",
"Veranda met plat dak vs. zadeldak: voor- en nadelen",
"Plat dak of zadeldak voor je veranda? Vergelijk op prijs, esthetiek, afwatering en onderhoud.",
"Type veranda","Veranda met plat dak vs. zadeldak: voor- en nadelen","""
<p>De dakvorm is bepalend voor het uiterlijk en de functionaliteit van je veranda. Plat dak of zadeldak — beide hebben duidelijke voor- en nadelen.</p>
<h2>Plat dak veranda</h2>
<ul><li>Moderne, strakke uitstraling</li><li>Eenvoudiger en goedkoper te bouwen</li><li>Goed te combineren met dakramen</li><li>Risico op lekkage bij slechte afwatering</li><li>Vraagt periodiek onderhoud aan de afvoer</li></ul>
<h3>Dakbedekkingsopties plat dak</h3>
<ul><li><strong>EPDM rubber:</strong> Duurzaam, 30+ jaar, onderhoudsvrij</li><li><strong>Glas (ISO-panelen):</strong> Maximaal licht, hoogste prijs</li><li><strong>Polycarbonaat:</strong> Goedkoop, minder isolerend</li><li><strong>Sandwichpanelen:</strong> Goed isolerend, ondoorzichtig</li></ul>
<h2>Zadeldak veranda</h2>
<ul><li>Klassieke, tijdloze uitstraling</li><li>Uitstekende afwatering door de helling</li><li>Past perfect bij traditionele woningen</li><li>Complexer en duurder om te bouwen</li><li>Kan bestaande ramen van de woning blokkeren</li></ul>
<h3>Dakbedekkingsopties zadeldak</h3>
<ul><li>Dakpannen (klassiek), leien (exclusief), glas (modern accent)</li></ul>
<h2>Wanneer wat kiezen?</h2>
<ul><li><strong>Moderne woning / nieuwbouw:</strong> Plat dak</li><li><strong>Traditionele / jaren-30 woning:</strong> Zadeldak</li><li><strong>Maximaal licht:</strong> Plat dak met volledig glas of zadeldak met nokraam</li></ul>
""",
[("/veranda/type-en-concept/soorten-veranda/","Soorten veranda materialen","Aluminium, hout, kunststof, staal"),
 ("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer"),
 ("/veranda/type-en-concept/moderne-vs-klassieke-veranda/","Moderne vs. klassieke veranda","Welke stijl?")])

page(f"{V}/type-en-concept/serre-tuinkamer-of-veranda/index.html",
"Serre, tuinkamer of veranda: wat is het verschil?",
"Serre, tuinkamer of veranda — ontdek de verschillen in comfort, isolatie, kosten en regelgeving.",
"Type veranda","Serre, tuinkamer of veranda: wat is het verschil?","""
<p>De termen worden door elkaar gebruikt, maar een serre, tuinkamer en veranda zijn drie wezenlijk verschillende concepten met elk hun eigen gebruikscomfort en prijsklasse.</p>
<h2>Veranda</h2>
<p>Een aanbouw met glas aan zijkanten en/of dak. Semi-buitenruimte of extra leefruimte. Isolatie varieert van geen tot uitstekend.</p>
<ul><li>Gebruik: seizoensgebonden of jaarrond (afhankelijk van isolatie)</li><li>Prijs: €1.500–€4.000/m²</li></ul>
<h2>Serre</h2>
<p>Volledig glazen aanbouw, traditioneel voor planten. Weinig isolatie — 's zomers heet, 's winters koud.</p>
<ul><li>Gebruik: planten, seizoensgebonden verblijf</li><li>Prijs: €800–€2.000/m²</li></ul>
<h2>Tuinkamer</h2>
<p>Modern concept: jaarrond bewoonbare aanbouw met volwaardige isolatie, verwarming en koeling. Bouwtechnisch een aanbouw op woningniveau.</p>
<ul><li>Gebruik: volwaardige extra kamer</li><li>Prijs: €2.500–€5.000/m²</li><li>Bijna altijd omgevingsvergunning vereist</li></ul>
<h2>Vergelijking</h2>
<table style="width:100%;border-collapse:collapse;font-size:.9rem;margin:1rem 0">
<tr style="background:#f0f7e6"><th style="padding:.6rem;border:1px solid #ddd;text-align:left">Criterium</th><th style="padding:.6rem;border:1px solid #ddd">Veranda</th><th style="padding:.6rem;border:1px solid #ddd">Serre</th><th style="padding:.6rem;border:1px solid #ddd">Tuinkamer</th></tr>
<tr><td style="padding:.6rem;border:1px solid #ddd">Isolatie</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Variabel</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Slecht</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Goed</td></tr>
<tr style="background:#fafafa"><td style="padding:.6rem;border:1px solid #ddd">Jaarrond</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Mogelijk</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Nee</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">Ja</td></tr>
<tr><td style="padding:.6rem;border:1px solid #ddd">Prijs/m²</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€€</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€</td><td style="padding:.6rem;border:1px solid #ddd;text-align:center">€€€</td></tr>
</table>
""",
[("/veranda/type-en-concept/soorten-veranda/","Soorten veranda materialen","Vergelijk aluminium, hout, kunststof"),
 ("/veranda/type-en-concept/veranda-als-leefruimte/","Veranda als leefruimte","Woonkameruitbreiding"),
 ("/veranda/veranda-bouwen-renoveren/","Complete veranda gids","Kosten en vergunningen")])

print("=== CLUSTER 1 DONE ===")

# ── ISOLATIE, COMFORT & TECHNIEK ──────────────────────────────────────────────

page(f"{V}/isolatie-comfort-techniek/veranda-isoleren/index.html",
"Veranda isoleren: dak, glas en vloer — complete gids",
"Hoe isoleer je een veranda optimaal? Alles over dakisolatie, beglazing (HR++ en triple) en vloerisolatie.",
"Isolatie","Veranda isoleren: dak, glas en vloer — complete gids","""
<p>Een slecht geïsoleerde veranda is in de zomer een broeikas en in de winter een vriezer. Met de juiste aanpak van dak, glas en vloer maak je van je veranda een jaarrond comfortabele ruimte.</p>
<h2>1. Dakisolatie</h2>
<p>Het dak is het grootste warmteverliesoppervlak. Afhankelijk van het daktype:</p>
<ul>
<li><strong>Glazen dak — HR++ glas:</strong> U-waarde ~1,1 W/m²K. Goede standaardkeuze.</li>
<li><strong>Glazen dak — Triple glas:</strong> U-waarde ~0,5 W/m²K. Beste isolatiewaarde.</li>
<li><strong>Massief dak — PIR-platen:</strong> Rd-waarde 3,5–5 m²K/W. Dun en zeer effectief.</li>
<li><strong>Massief dak — PUR-schuim:</strong> Goed voor moeilijk bereikbare hoeken, gespoten op maat.</li>
</ul>
<h2>2. Beglazing</h2>
<ul>
<li><strong>Enkel glas:</strong> Niet meer toepasbaar — warmteverlies is te groot</li>
<li><strong>HR++ glas:</strong> Standaard voor veranda's. Balans prijs/kwaliteit. U-waarde 1,0–1,2 W/m²K.</li>
<li><strong>Triple glas:</strong> Beste isolatie, hogere prijs (+20–30%). Ideaal in combinatie met vloerverwarming.</li>
<li><strong>Low-e coating:</strong> Weerspiegelt warmtestraling terug. Belangrijk voor dakglas (zomerse oververhitting beperken).</li>
</ul>
<h2>3. Vloerisolatie</h2>
<ul>
<li>Minimale Rd-waarde: 2,5 m²K/W</li>
<li><strong>EPS of PIR-platen</strong> onder de vloerafwerking</li>
<li>Combineer met vloerverwarming voor maximaal comfort</li>
<li>Zorg voor een damprem bij houten vloerconstructies</li>
</ul>
<h2>4. Koudebruggen aanpakken</h2>
<p>Koudebruggen bij de aansluiting van de veranda op de woning veroorzaken condensatie en warmteverlies. Gebruik thermisch onderbroken profielen (aluminium met polyamide kern) en isoleer de drempelaansluiting.</p>
<h2>Kosten isolatie</h2>
<ul>
<li>HR++ glas veranda (20 m²): €3.000–€5.000</li>
<li>Triple glas (upgrade): +€1.500–€3.000</li>
<li>Dakisolatie massief (PIR): €1.500–€3.000</li>
<li>Vloerisolatie: €800–€1.500</li>
</ul>
""",
[("/veranda/isolatie-comfort-techniek/beste-beglazing-voor-veranda/","Beste beglazing voor veranda","HR++, triple of gelaagd glas?"),
 ("/veranda/isolatie-comfort-techniek/veranda-verwarmen/","Veranda verwarmen","Vloerverwarming, radiatoren en airco"),
 ("/veranda/isolatie-comfort-techniek/veranda-ventilatie/","Veranda ventilatie","Condens en schimmel voorkomen")])

page(f"{V}/isolatie-comfort-techniek/beste-beglazing-voor-veranda/index.html",
"Beste beglazing voor veranda: dubbel, HR++ of triple glas?",
"Welk glas is het beste voor je veranda? Vergelijk dubbel glas, HR++, triple en gespecialiseerde beglazing op isolatie, prijs en comfort.",
"Isolatie","Beste beglazing voor veranda: dubbel, HR++ of triple glas?","""
<p>Beglazing is het hart van een veranda. De juiste keuze maakt het verschil tussen een comfortabele ruimte en een ruimte die te warm of te koud is. We vergelijken alle opties.</p>
<h2>Dubbel glas (verouderd)</h2>
<p>U-waarde: ~2,8 W/m²K. Niet meer geschikt voor nieuwe installaties. Bij renovatie altijd vervangen.</p>
<h2>HR++ glas</h2>
<p>De standaard voor veranda's in 2026. U-waarde: ~1,0–1,1 W/m²K. Goede balans prijs en prestatie.</p>
<ul><li>Prijs: €80–€120/m² (glas alleen)</li><li>Geschikt voor zijwanden en dak</li><li>Verkrijgbaar met zonweringscoating</li></ul>
<h2>Triple glas</h2>
<p>Drie glaslagen met twee spouwen. U-waarde: ~0,5–0,7 W/m²K. Beste isolatiewaarde, maar zwaarder en duurder.</p>
<ul><li>Prijs: €130–€200/m²</li><li>Ideaal voor noordelijke gevels en dak</li><li>Let op gewicht — constructie moet aangepast zijn</li></ul>
<h2>Gespecialiseerde beglazing</h2>
<ul>
<li><strong>Zonwerend glas:</strong> Filtert zonnestraling (g-waarde < 0,35). Onmisbaar voor dak- en zuidgericht glas.</li>
<li><strong>Akoestisch glas:</strong> Geluidsreducerende tussenlaag. Nuttig bij straatlawaai.</li>
<li><strong>Zelfreinigend glas:</strong> TiO₂-coating breekt organisch vuil af. Handig voor dakglas.</li>
<li><strong>Privacy glas:</strong> Gematteerd of bedrukt voor afscherming.</li>
</ul>
<h2>Aanbeveling per situatie</h2>
<table style="width:100%;border-collapse:collapse;font-size:.9rem;margin:1rem 0">
<tr style="background:#f0f7e6"><th style="padding:.6rem;border:1px solid #ddd;text-align:left">Situatie</th><th style="padding:.6rem;border:1px solid #ddd">Aanbevolen glas</th></tr>
<tr><td style="padding:.6rem;border:1px solid #ddd">Standaard veranda (budget)</td><td style="padding:.6rem;border:1px solid #ddd">HR++ met zonweringscoating</td></tr>
<tr style="background:#fafafa"><td style="padding:.6rem;border:1px solid #ddd">Jaarrond leefruimte</td><td style="padding:.6rem;border:1px solid #ddd">Triple glas + zonwerend</td></tr>
<tr><td style="padding:.6rem;border:1px solid #ddd">Glazen dak (warm klimaat)</td><td style="padding:.6rem;border:1px solid #ddd">HR++ zonewerend (g < 0,35)</td></tr>
<tr style="background:#fafafa"><td style="padding:.6rem;border:1px solid #ddd">Straatlawaai</td><td style="padding:.6rem;border:1px solid #ddd">HR++ akoestisch</td></tr>
</table>
""",
[("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer complete gids"),
 ("/veranda/isolatie-comfort-techniek/veranda-warm-winter-koel-zomer/","Warm in winter, koel in zomer","Tips voor thermisch comfort"),
 ("/veranda/isolatie-comfort-techniek/veranda-ventilatie/","Ventilatie in veranda","Condens en schimmel voorkomen")])

page(f"{V}/isolatie-comfort-techniek/veranda-warm-winter-koel-zomer/index.html",
"Veranda warm in de winter, koel in de zomer: tips en technieken",
"Hoe houd je een veranda comfortabel in alle seizoenen? Praktische tips voor verwarming, koeling en zonwering.",
"Comfort","Veranda warm in de winter, koel in de zomer: tips en technieken","""
<p>De grootste klacht over veranda's is dat ze in de zomer te warm zijn en in de winter te koud. Met de juiste combinatie van isolatie, zonwering en verwarming los je dit op.</p>
<h2>Te warm in de zomer</h2>
<p>Glas laat zonlicht door dat in de veranda als warmte achterblijft. Oplossingen in volgorde van effectiviteit:</p>
<ol>
<li><strong>Buitenzonwering (screens/lamellen):</strong> Houdt 60–80% van de warmte buiten vóór het glas</li>
<li><strong>Zonwerend glas:</strong> Filtert straling bij de bron (g-waarde &lt; 0,35)</li>
<li><strong>Dakramen of valventielen:</strong> Warme lucht kan via het dak ontsnappen</li>
<li><strong>Warmtepomp-airco:</strong> Actieve koeling voor hete dagen</li>
<li><strong>Binnenzonwering:</strong> Minst effectief (warmte is al binnen), maar optioneel voor privacy</li>
</ol>
<h2>Te koud in de winter</h2>
<ol>
<li><strong>Isolerende beglazing:</strong> Vervang enkel of oud dubbel glas door HR++ of triple</li>
<li><strong>Dakisolatie:</strong> PIR-platen of PUR-schuim bij massief dak</li>
<li><strong>Vloerverwarming:</strong> Meest comfortabel, koppel aan bestaande cv of warmtepomp</li>
<li><strong>Elektrische verwarming:</strong> Snelle oplossing, minder zuinig</li>
<li><strong>Warmtepomp-airco (reversibel):</strong> Verwarmt én koelt, COP van 3–5</li>
</ol>
<h2>Het ideale pakket</h2>
<p>Voor jaarrond comfort: <strong>HR++ of triple glas + buitenzonwering + reversibele warmtepomp-airco</strong>. Dit dekt alle seizoenen af met één systeem voor zowel verwarming als koeling.</p>
<h2>Kosten thermisch comfort</h2>
<ul><li>Buitenzonwering (screens): €500–€1.500 per raam</li><li>Reversibele airco: €1.500–€3.500 (installatie incl.)</li><li>Vloerverwarming (20 m²): €3.000–€6.000</li></ul>
""",
[("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dakisolatie, glas en vloer"),
 ("/veranda/isolatie-comfort-techniek/zonwering-voor-veranda/","Zonwering voor veranda","Screens, lamellen en dakzonwering"),
 ("/veranda/isolatie-comfort-techniek/veranda-verwarmen/","Veranda verwarmen","Vloerverwarming, radiatoren en airco")])

page(f"{V}/isolatie-comfort-techniek/zonwering-voor-veranda/index.html",
"Zonwering voor veranda: screens, lamellen en dakzonwering vergeleken",
"Welke zonwering past het best bij je veranda? Vergelijk screens, lamellen, dakzonwering en binnenzonwering op effectiviteit en prijs.",
"Comfort","Zonwering voor veranda: screens, lamellen en dakzonwering vergeleken","""
<p>Zonwering is voor een veranda geen luxe maar een noodzaak. Zonder zonwering wordt een veranda in de zomer onbewoonbaar. We bespreken alle opties van meest naar minst effectief.</p>
<h2>Buitenzonwering (meest effectief)</h2>
<h3>Screens</h3>
<p>Oprolbare doeken die voor het glas hangen. Ze blokkeren 70–95% van de zonnestraling terwijl je nog steeds naar buiten kunt kijken (afhankelijk van de opening van het weefsel).</p>
<ul><li>Openheid 3%: Maximale zonwering, nog zicht</li><li>Openheid 10%: Minder zonwering, beter zicht</li><li>Prijs: €400–€900 per raam (motorisch)</li><li>Windgevoelig — kies voor een model met windmeter</li></ul>
<h3>Buitenlamellen (persiennes)</h3>
<p>Aluminium of houten lamellen die de richting van de zon volgen. Bieden zonwering én privacy.</p>
<ul><li>Prijs: €600–€1.200 per raam</li><li>Duurzaam en onderhoudsarm (aluminium)</li></ul>
<h2>Dakzonwering</h2>
<p>Voor veranda's met een glazen dak is dakzonwering essentieel. Het dak vangt de meeste zonnestraling op.</p>
<ul><li><strong>Inwendige screens (tussen dubbel glas):</strong> Beschermd tegen wind, minder effectief dan buitenzonwering</li><li><strong>Uitwendige dakzonwering:</strong> Meest effectief, vereist robuuste montage</li><li><strong>Zonwerend dakglas (g-waarde &lt; 0,35):</strong> Permanente oplossing in het glas zelf</li></ul>
<h2>Binnenzonwering (minst effectief)</h2>
<p>Gordijnen, rolgordijnen of plissés zijn de minst effectieve oplossing — de warmte is al binnen het glas. Maar ze bieden wel privacy en sfeer.</p>
<ul><li>Reflecterende gordijnen verminderen warmte enigszins</li><li>Prijs: €100–€400 per raam (afhankelijk van kwaliteit)</li></ul>
<h2>Motorische bediening</h2>
<p>Koppel zonwering aan een windmeter en zonnesensor voor automatische bediening. Vereist bij screens (windgevoelig). Budget: +€200–€500 per zone voor automatisering.</p>
""",
[("/veranda/isolatie-comfort-techniek/veranda-warm-winter-koel-zomer/","Warm in winter, koel in zomer","Alle tips"),
 ("/veranda/isolatie-comfort-techniek/veranda-ventilatie/","Ventilatie in veranda","Condens voorkomen"),
 ("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer")])

page(f"{V}/isolatie-comfort-techniek/veranda-ventilatie/index.html",
"Veranda ventilatie: condens, schimmel en vocht voorkomen",
"Hoe ventileer je een veranda goed? Alles over condens op ramen, schimmelvorming en de beste ventilatie-oplossingen.",
"Comfort","Veranda ventilatie: condens, schimmel en vocht voorkomen","""
<p>Slechte ventilatie in een veranda leidt onvermijdelijk tot condens op het glas, vochtige lucht en op termijn schimmel. Inzicht in de oorzaken helpt je de juiste oplossing te kiezen.</p>
<h2>Waarom ontstaat condens in een veranda?</h2>
<p>Condens ontstaat wanneer vochtige warme lucht in contact komt met een koud glasoppervlak. In een veranda zijn de risicomomenten:</p>
<ul><li>'s Morgens vroeg (glastemperatuur laag)</li><li>Na koken, douchen of was drogen in de nabijgelegen ruimte</li><li>In de winter bij grote temperatuurverschillen</li></ul>
<h2>Oplossingen voor ventilatie</h2>
<h3>Natuurlijke ventilatie</h3>
<ul>
<li><strong>Roosters in profielen:</strong> Kleine permanente opening in het kozijn. Eenvoudig en goedkoop.</li>
<li><strong>Dakramen met klep (valramen):</strong> Warme vochtige lucht stijgt op en ontsnapt via het dak. Ideaal.</li>
<li><strong>Kiepramen:</strong> Ramen die op een kier kunnen staan voor continue doorluchting.</li>
</ul>
<h3>Mechanische ventilatie</h3>
<ul>
<li><strong>Badkamerventilator:</strong> Simpele oplossing voor een kleine veranda.</li>
<li><strong>WTW-unit (warmteterugwinning):</strong> Ververst de lucht zonder warmteverlies. Ideaal voor jaarrond bewoonbare veranda's.</li>
<li><strong>Decentrale WTW:</strong> Kleinere unit per ruimte, eenvoudiger te installeren dan centrale WTW.</li>
</ul>
<h2>Condens op glas verminderen</h2>
<ul><li>Upgrade naar triple glas: glastemperatuur blijft hoger</li><li>Verwarm langs het glas (vloerverwarming of radiator onder raam)</li><li>Zorg voor constante luchtcirculatie (rooster, kiepraam)</li></ul>
<h2>Schimmel herkennen en aanpakken</h2>
<p>Schimmel verschijnt als zwarte vlekken op siliconen, profielen en muren. Aanpak:</p>
<ul><li>Reinig met anti-schimmelspray en vervang aangetaste siliconen</li><li>Verbeter ventilatie om herhaling te voorkomen</li><li>Bij hardnekkige schimmel: laat de bron (lekkage?) controleren</li></ul>
""",
[("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer"),
 ("/veranda/isolatie-comfort-techniek/beste-beglazing-voor-veranda/","Beste beglazing","HR++, triple of gelaagd glas"),
 ("/veranda/isolatie-comfort-techniek/veranda-warm-winter-koel-zomer/","Thermisch comfort","Warm in winter, koel in zomer")])

page(f"{V}/isolatie-comfort-techniek/veranda-verwarmen/index.html",
"Veranda verwarmen: vloerverwarming, radiatoren of airco-warmtepomp?",
"Vergelijk alle verwarmingsopties voor je veranda: vloerverwarming, elektrische verwarming, radiatoren en de warmtepomp-airco.",
"Comfort","Veranda verwarmen: vloerverwarming, radiatoren of airco-warmtepomp?","""
<p>Een goed verwarmde veranda is het hele jaar door bewoonbaar. Er zijn meerdere verwarmingsopties, elk met hun eigen comfort, prijs en energieverbruik.</p>
<h2>1. Vloerverwarming</h2>
<p>De meest comfortabele optie. Warmte van beneden zorgt voor een aangenaam klimaat en verwarmt ook het glas langs de onderrand, wat condensatie vermindert.</p>
<ul><li><strong>Watervloerverwarming:</strong> Koppeling aan cv-ketel of warmtepomp. Meest efficiënt op lange termijn.</li><li><strong>Elektrische vloerverwarming:</strong> Eenvoudiger te installeren, maar hogere gebruikskosten.</li><li>Prijs installatie 20 m²: €3.000–€6.000 (water) / €800–€2.000 (elektrisch)</li></ul>
<h2>2. Warmtepomp-airco (reversibel)</h2>
<p>De meest populaire keuze voor veranda's. Verwarmt in de winter en koelt in de zomer — één systeem voor alle seizoenen.</p>
<ul><li>COP (rendement verwarming): 3–5 (voor elke kWh elektriciteit: 3–5 kWh warmte)</li><li>Prijs inclusief installatie: €1.500–€3.500</li><li>Tip: kies een model met wifi-bediening en een stil binnenunit</li></ul>
<h2>3. Radiatoren</h2>
<p>Aansluiting op het bestaande cv-systeem. Snelle opwarming, beproefd systeem.</p>
<ul><li>Radiator langs het glas plaatsen beperkt koudeval en condensatie</li><li>Prijs aansluiting (inclusief leidingwerk): €800–€2.000 per radiator</li></ul>
<h2>4. Elektrische verwarmingspanelen / infrarood</h2>
<p>Eenvoudig te installeren, geen leidingwerk. Infrarood straalt direct warmte af op mensen en objecten (niet de lucht), wat efficiënt voelt.</p>
<ul><li>Prijs: €200–€600 per paneel</li><li>Nadeel: hogere gebruikskosten dan warmtepomp</li></ul>
<h2>5. Buitenhaard / terrasverwarmers</h2>
<p>Voor een sfeervolle avond in een semi-open veranda. Niet geschikt als primaire verwarming voor een gesloten ruimte (CO₂ / verbrandingslucht).</p>
<h2>Aanbeveling</h2>
<p><strong>Beste keuze voor jaarrond comfort:</strong> Combineer vloerverwarming (op warmtepomp) met een reversibele airco als backup voor koeling. Dit geeft maximaal comfort met minimaal energieverbruik.</p>
""",
[("/veranda/isolatie-comfort-techniek/veranda-isoleren/","Veranda isoleren","Dak, glas en vloer"),
 ("/veranda/isolatie-comfort-techniek/veranda-warm-winter-koel-zomer/","Thermisch comfort","Warm in winter, koel in zomer"),
 ("/veranda/isolatie-comfort-techniek/zonwering-voor-veranda/","Zonwering","Screens, lamellen en dakzonwering")])

print("=== CLUSTER 2 DONE ===")
print("\nAlle pagina's aangemaakt!")
