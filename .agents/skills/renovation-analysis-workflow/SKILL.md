---
name: renovation-analysis-workflow
description: Workflow unique d'analyse des pages de thuisrenovatie-gids.nl. Audite une URL ou un cluster, contrôle intention, rôle éditorial, frontières entre clusters, preuves, fraîcheur, sécurité, valeur affiliée, industrialisation éditoriale et SEO, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. En mode PUBLISH_REVIEW, sert de gate final avant validation humaine.
provenance: custom
metadata:
  adapted_for: thuisrenovatie-gids.nl
  source_engine: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/guide-analysis-workflow
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + renovation cluster integrity + safety + category boundaries + cluster similarity"
---

# Renovation Analysis Workflow

## Rôle

C'est le **seul workflow d'analyse éditoriale** à utiliser pour les contenus de Thuisrenovatie Gids.

Il ne rédige pas la page. Il orchestre en priorité les skills spécialisés du dépôt et ajoute uniquement les contrôles propres au site : frontières entre clusters rénovation, sécurité, fraîcheur des règles/prix/subsides et similarité structurelle entre pages.

Séparation des responsabilités :

- `renovation-analysis-workflow` = diagnostiquer, comparer le cluster, décider et effectuer le publish review ;
- `renovation-content-workflow` = produire ou corriger uniquement lorsqu'une décision d'analyse le demande.

Les familles de routes servent à définir la **propriété d'une intention**, jamais un template de page :

- `/renovatie-plannen/` = décider quoi faire, dans quel ordre, avec quel budget, quelles contraintes et quel niveau de priorité ;
- `/renovatieprojecten/` = décider et préparer un projet de rénovation concret ;
- `/verduurzamen/` = décider d'une mesure liée à énergie, confort ou installations ;
- `/problemen-oplossen/` = comprendre un symptôme, les causes possibles, les contrôles sûrs et la prochaine action ;
- `/doe-het-zelf/` = accomplir une tâche réellement adaptée au DIY, avec limites de sécurité explicites ;
- `/vakman-en-offertes/` = décider quand déléguer, comment choisir, cadrer et comparer une prestation.

---

# 1. Modes

## `AUDIT`

Mode par défaut pour une URL existante.

Retourne une décision et un plan de correction **sans réécrire la page**. L'audit est individuel mais compare aussi les URLs voisines lorsque le risque de chevauchement, cannibalisation ou structure clonée existe.

## `CLUSTER_AUDIT`

Analyse plusieurs URLs d'un même cluster afin de détecter :

- intentions ou tâches qui se chevauchent ;
- pages qui devraient être fusionnées ;
- sous-questions qui appartiennent mieux à un autre cluster ;
- couverture fragmentée d'un même sujet ;
- trous utiles dans le parcours ;
- architectures éditoriales industrialisées ;
- répétitions de conclusions, tableaux, procédures, blocs décisionnels ou CTA sans justification ;
- maillage qui ne suit pas les vraies étapes du parcours.

Le mode cluster ne déclenche aucune réécriture automatiquement.

## `PUBLISH_REVIEW`

Gate final après correction ou production via `renovation-content-workflow`.

Il réexécute le validateur machine et les contrôles substantiels, puis retourne exactement :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais à activer l'indexation, merger, rediriger ou déployer une décision structurelle sans instruction explicite.

---

# 2. Entrées

Lire selon disponibilité :

- `AGENTS.md` et les règles de design/rendu si concernées ;
- la page cible ;
- sa source de vérité `content/<route>/body.html` ;
- son brief `content/briefs/<route>.md` et son review `content/reviews/<route>.md` lorsqu'ils existent ;
- les pages voisines du cluster ;
- les pages des autres clusters qui couvrent des sous-questions proches ;
- l'analyse sémantique, GSC, historique, logs ou autres signaux disponibles ;
- la SERP actuelle lorsque l'intention est incertaine ou susceptible d'avoir évolué ;
- les sources actuelles pour les faits instables.

Ne jamais combler une donnée absente avec la mémoire du modèle. Signaler les inconnues qui peuvent changer la décision.

---

# 3. Chaîne de skills réutilisés — source principale de l'analyse

Le workflow doit d'abord **exécuter les skills existants**. Ne pas recopier leurs méthodes ici et ne pas créer un sous-agent custom lorsqu'une brique existante couvre le besoin.

## 3.1 `seo-content-audit`

Utiliser `.agents/skills/seo-content-audit/SKILL.md` pour déterminer si l'URL mérite d'être conservée, mise à jour, consolidée ou retirée du cluster.

Ce skill porte la logique amont `KEEP / UPDATE / MERGE / REDIRECT / DELETE`. Les actions destructives restent des recommandations tant que l'utilisateur ne les demande pas explicitement.

## 3.2 `seo-keyword`

Utiliser `.agents/skills/seo-keyword/SKILL.md` pour confirmer, lorsque les données le permettent :

- requête ou cluster principal ;
- intention ;
- forme attendue de la réponse ;
- proximité avec d'autres URLs ;
- périmètre trop large ou trop étroit.

Les données sémantiques, GSC ou SERP disponibles priment sur une supposition tirée du slug.

## 3.3 `search-intent`

Utiliser pour examiner finement la page comme réponse à une tâche ou une décision : résultat attendu, maturité, sous-questions, route propriétaire et sections qui ne servent plus l'intention.

## 3.4 `content-refresh`

Uniquement si une mise à jour est nécessaire. Utiliser le skill pour identifier intent drift, obsolescence, thin value, faiblesse structurelle, cannibalisation, generic prose, trust gap, safety gap ou structural cloning. Le présent workflow décide ensuite si la correction reste légère ou devient une reconstruction.

## 3.5 `fact-check`

Contrôler les affirmations vérifiables avec une exigence proportionnée à leur stabilité : prix, coûts, subsides, permis, réglementation, normes, performances, rendement, garanties, procédures, sécurité ou disponibilité.

Une affirmation plausible mais non sourcée reste non vérifiée.

## 3.6 `evidence-based-reviews`

Conditionnel, jamais automatique.

L'utiliser uniquement lorsqu'une conclusion expérientielle sur un produit, matériau, équipement, prestataire ou comportement réel dépasse ce qu'une documentation officielle permet d'établir. Ne jamais simuler un test ou une inspection.

## 3.7 `affiliate-value`

Utiliser lorsque la page influence une dépense, une demande de devis, un choix de professionnel ou un achat. La page doit rester utile sans lien affilié ni formulaire et apporter un raisonnement propre : arbitrages, limites, dépendances, risques, coût, scope ou prochaine étape pertinente.

## 3.8 `internal-linking-audit`

Vérifier que les liens répondent à la prochaine question logique du lecteur. Aucun quota de liens ; l'absence d'un lien n'est un problème que lorsqu'une vraie étape du parcours est manquante.

## 3.9 `anti-ai-slop`

Utiliser en review/detection pour rechercher prose générique, symétrie artificielle, sections interchangeables, procédures trop lisses, répétitions et architectures répliquées d'une page à l'autre.

Ce skill ne sert pas à détecter l'origine du texte.

## 3.10 SEO

- `seo-onpage` : title, meta, H1, couverture utile, structure, maillage, canonical et schema honnête ;
- `seo-technical` : robots, crawlabilité, canonical, HTML et données structurées réellement applicables ;
- `seo-drift` : uniquement lorsqu'un baseline avant/après existe et apporte une information utile.

Aucun quota de mots, headings, tableaux, FAQ, liens ou sources ne sert de proxy de qualité.

## 3.11 `editorial-qa`

Dernière QA générique : intention, valeur originale, factualité, naturel, utilité, SEO et cohérence sans dépendance à l'affiliation.

---

# 4. Couche custom n°1 — quel travail la page doit-elle accomplir ?

Le type dominant sert de **grille de risque, jamais de template éditorial**.

Trois familles génériques restent utiles :

- `CHOICE` : aider à arbitrer entre options, priorités, contraintes ou approches ;
- `EXPLAINER` : rendre compréhensible un mécanisme, un coût, une règle, un risque ou une technologie ;
- `HOW_TO` : permettre d'accomplir une tâche, une préparation, un contrôle ou une procédure vérifiable.

Une page peut être hybride. Le type ne doit jamais imposer un nombre de H2, leur ordre, un tableau, une FAQ, une checklist ou une conclusion standard.

## Pour `CHOICE`

Vérifier surtout :

- la décision exacte à prendre ;
- les critères qui changent réellement cette décision ;
- les compromis et critères éliminatoires ;
- les dépendances avec d'autres travaux ;
- les situations où chaque option cesse d'être adaptée ;
- l'absence de recommandation commerciale déguisée.

## Pour `EXPLAINER`

Vérifier surtout :

- concept et termes voisins distingués ;
- mécanisme expliqué sans fausse causalité ;
- lien entre mécanisme et conséquence pratique ;
- limites, exceptions et hypothèses importantes ;
- absence de pseudo-précision sur prix, performance ou réglementation.

## Pour `HOW_TO`

Vérifier surtout :

- prérequis et contexte nécessaires ;
- étapes vérifiables uniquement lorsque l'ordre compte réellement ;
- résultat attendu et moyen de vérifier qu'il est obtenu ;
- échecs probables, limites ou alternatives utiles ;
- stop conditions de sécurité ;
- absence d'étape inventée à partir de la mémoire du modèle.

---

# 5. Couche custom n°2 — frontières entre clusters

## `renovatie-plannen` vs `renovatieprojecten`

La première famille possède les décisions transversales de planification : scope, ordre, budget, phases, permis, aides, rendement. La seconde possède la décision et la préparation d'un chantier concret : badkamer, keuken, aanbouw, fundering, ramen, etc.

## `renovatieprojecten` vs `verduurzamen`

Une page projet traite d'abord le chantier et ses arbitrages. Une page verduurzamen traite d'abord l'effet énergie/confort/installation et les conditions qui rendent la mesure pertinente.

## `problemen-oplossen` vs projet

Une page problème part d'un symptôme ou d'un risque et aide à diagnostiquer prudemment la prochaine action. Elle ne doit pas devenir une page projet générique simplement parce qu'une réparation peut suivre.

## `doe-het-zelf` vs autres clusters

Une page DIY existe seulement si la tâche peut être décrite de façon réellement exécutable et sûre pour le public visé. Une tâche à risque élevé reste dans un cluster explicatif/décisionnel avec escalade professionnelle.

## `vakman-en-offertes` vs contenu informationnel

Les pages lead possèdent la sélection du prestataire, la préparation du scope, la comparaison d'offres et le CTA. Elles ne doivent pas voler l'intention principale d'une page plan/projet/problème uniquement pour convertir plus tôt.

### Test pratique

Si deux URLs peuvent garder le même H1, la même réponse centrale, les mêmes critères et le même bloc décisionnel en ne changeant que quelques termes, leur séparation est probablement insuffisante.

---

# 6. Couche custom n°3 — intégrité décisionnelle, sécurité et fraîcheur

Une page n'est pas jugée à sa longueur mais à sa capacité à rendre une chose **plus claire, plus faisable, plus sûre ou plus décidable**.

Vérifier :

- la réponse principale arrive assez tôt pour l'intention ;
- chaque grande section ajoute une information, une preuve, un arbitrage ou une limite distincte ;
- un tableau est utilisé seulement s'il rend une comparaison plus lisible ;
- une procédure est détaillée seulement autant que nécessaire pour être exécutable et sûre ;
- une définition ne remplace pas l'explication de l'impact ;
- une liste ne remplace pas une règle de décision lorsque le lecteur doit arbitrer ;
- les cas limites, contre-indications et dépendances importantes ne sont pas masqués ;
- les travaux à risque ne sont pas banalisés en DIY.

## Fraîcheur proportionnée

Adapter le niveau de recherche au risque d'obsolescence :

- physique du bâtiment ou principe stable → vérifier l'exactitude sans exiger artificiellement une source récente ;
- prix, coûts de main-d'œuvre, disponibilité → vérifier actuellement et dater ;
- subsides, fiscalité, permis, réglementation, normes ou conditions administratives → source officielle actuelle + territoire + date ;
- performances techniques, rendement et économies → vérifier conditions, hypothèses et source ;
- une date de vérification ne compense jamais une source faible.

## Sécurité

Escalade claire vers un professionnel qualifié lorsque la tâche implique notamment :

- structure porteuse ou fondations ;
- gaz ;
- électricité au-delà des contrôles sûrs pour un particulier ;
- amiante ou matériau potentiellement dangereux ;
- toiture/hauteur ;
- humidité ou dommage dont la cause peut être structurelle ;
- intervention réglementée ou nécessitant une qualification.

Ne jamais présenter une absence d'inspection comme un diagnostic certain.

---

# 7. Couche custom n°4 — similarité structurelle du cluster

En `AUDIT`, comparer la cible aux pages les plus proches. En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, regarder le sous-cluster pertinent dans son ensemble.

Chercher notamment :

- mêmes fonctions de H2/H3 dans le même ordre ;
- intro et conclusion identiques avec substitution du sujet ;
- tableau placé systématiquement au même endroit ;
- blocs « voordelen / nadelen / stappen / kosten / FAQ » répliqués sans besoin ;
- procédures qui gardent artificiellement le même nombre d'étapes ;
- mêmes CTA et mêmes liens comme fin obligatoire ;
- mêmes transitions et rythme de paragraphes ;
- types `PLAN / PROJECT / SUSTAINABILITY / DIY / TROUBLESHOOTING / LEAD` transformés en squelettes de production ;
- références `CHOICE / EXPLAINER / HOW_TO` transformées en templates.

Les composants visuels communs sont normaux. Le problème apparaît lorsque **la pensée éditoriale est déterminée avant l'intention et les preuves**.

Une industrialisation substantielle peut déclencher `DEEP_REWRITE`.

---

# 8. Décisions `AUDIT` / `CLUSTER_AUDIT`

## `KEEP`

La page possède une tâche claire, distincte, actuelle, sûre et utile. Aucun changement substantiel n'est nécessaire.

## `LIGHT_UPDATE`

Corrections ciblées : faits, sources, exemple, metadata, maillage, sécurité, frontière avec une autre URL ou quelques passages. L'architecture fondamentale reste pertinente.

## `DEEP_REWRITE`

Réserver ce statut aux problèmes structurants :

- intention ou rôle mal cadré ;
- procédure non fiable, dangereuse ou substantiellement obsolète ;
- explication incapable de relier mécanisme et conséquence ;
- page de choix qui ne permet pas réellement d'arbitrer ;
- valeur originale faible ;
- preuves insuffisantes sur les claims centraux ;
- cannibalisation forte ;
- architecture fortement industrialisée.

`DEEP_REWRITE` ne signifie pas « tout jeter ». Préserver faits, sources, exemples, passages et raisonnements valides identifiés par l'audit.

## `MERGE`

Une autre URL couvre essentiellement la même tâche ou intention. Indiquer la cible recommandée, sans merger/rediriger automatiquement.

## `NOINDEX`

La page n'a pas encore assez de valeur, de preuve, de sécurité ou de justification pour être indexée. Aucune suppression automatique.

Pour chaque décision fournir :

- confiance ;
- valeur existante à préserver ;
- preuves utilisées ;
- unknowns importants ;
- blockers ;
- améliorations secondaires ;
- risques de cannibalisation ;
- risques de sécurité ou de fraîcheur ;
- prochaine étape.

### Handoff

- `KEEP` → aucune rédaction ;
- `LIGHT_UPDATE` → `renovation-content-workflow` avec scope limité ;
- `DEEP_REWRITE` → `renovation-content-workflow` avec reconstruction guidée par l'intention et les preuves ;
- `MERGE` / `NOINDEX` → décision humaine avant action structurelle.

---

# 9. Mode `PUBLISH_REVIEW`

Exécuter uniquement sur une version considérée terminée.

## Étape A — validation machine

Exécuter :

```bash
python3 scripts/validate_content_quality.py
```

Le validateur contrôle uniquement des blockers détectables automatiquement. Il ne valide ni profondeur, ni style, ni exactitude factuelle avec des quotas structurels.

## Étape B — gates substantiels

Réexécuter les skills pertinents et vérifier au minimum :

- intention ou tâche réellement satisfaite ;
- frontière nette avec les clusters voisins ;
- faits et procédures importants correctement sourcés ;
- fraîcheur adaptée au risque d'obsolescence ;
- territoire explicite pour règles, permis, aides ou conditions locales ;
- aucun faux test, faux diagnostic, fausse inspection ni faux hands-on ;
- explication, décision ou procédure réellement exploitable ;
- cas limites, dépendances et restrictions significatives présents ;
- sécurité correctement escaladée ;
- valeur réelle sans affiliation ;
- absence de merchant/lead rewrite ;
- pas de cannibalisation non résolue ;
- pas de signal `HIGH` d'AI-slop ;
- architecture justifiée par la page et non par un type réutilisé ;
- absence de clonage structurel substantiel avec les pages voisines ;
- title/H1/canonical/robots/liens/schema cohérents ;
- lecture complète de la version rendue si le rendu est disponible.

## Étape C — résultat

### PASS

Retourner exactement :

`PASS — READY_FOR_HUMAN_VALIDATION`

### FAIL

Retourner exactement :

`FAIL — KEEP_NOINDEX`

Lister les gates en échec et router vers le skill ou la passe qui doit corriger le problème. Un FAIL n'entraîne pas automatiquement une réécriture totale.

---

# 10. Indexation

Le site conserve actuellement la logique globale définie dans `content/site.json` et `generate_pages.py`. Le workflow ne modifie jamais `indexing_enabled` de lui-même.

Indexation uniquement après :

1. aucun blocker machine ;
2. `PUBLISH_REVIEW` = `PASS — READY_FOR_HUMAN_VALIDATION` pour le périmètre concerné ;
3. validation humaine explicite ;
4. instruction explicite de rendre le site ou les pages concernées indexables.

---

# 11. Répartition 80/20

La méthodologie doit venir majoritairement des skills existants :

- SEO/recherche : `seo-content-audit`, `seo-keyword`, `search-intent`, `content-refresh`, `seo-onpage`, `seo-technical`, `seo-drift` ;
- preuve/confiance : `fact-check`, `evidence-based-reviews`, `affiliate-value` ;
- production éditoriale : `content-brief-authoring`, `content-and-copy`, `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `editorial-qa`, `seo-best-practices` ;
- selon le besoin : `information-architecture`, `jtbd-framing`, `cro-optimization`.

La couche custom de ce workflow se limite à :

1. orchestration et mapping des décisions ;
2. frontières entre clusters ;
3. risques propres à la rénovation : sécurité, règles, prix, aides, dépendances ;
4. fraîcheur proportionnée et similarité structurelle du cluster.

Ne pas ajouter de deuxième méthode SEO, fact-check, rédaction ou qualité à l'intérieur du workflow.

---

# 12. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- quota de liens ou de sources ;
- nombre obligatoire d'étapes ;
- tableau ou FAQ obligatoire ;
- score artificiel de qualité ;
- template fixe `PLAN`, `PROJECT`, `SUSTAINABILITY`, `DIY`, `TROUBLESHOOTING`, `LEAD`, `CHOICE`, `EXPLAINER` ou `HOW_TO` ;
- générateur de texte ;
- duplication des méthodes déjà maintenues dans les skills spécialisés.

Sa valeur est l'orchestration, la décision et le contrôle inter-pages propre aux clusters rénovation.