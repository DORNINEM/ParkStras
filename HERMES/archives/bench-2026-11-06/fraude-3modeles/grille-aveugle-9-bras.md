# Notation à l'aveugle — thème **FRAUDE**, neuf veilles du même jour

Tu es un évaluateur éditorial indépendant. Les neuf veilles ci-dessous traitent **le même thème de veille
technologique, à la même date**, pour un public professionnel, avec une fenêtre de recherche : un mois.
Elles ont été produites par des modèles ou des procédures différents — tu ne sais pas lesquels, et cela ne
doit pas t'intéresser : juge chaque veille sur son texte.

## Ce que tu dois rendre, pour CHACUN des neuf bras
- Sept notes de 0 à 5 : **Conformité** (structure et exigences du thème), **Sourcing** (chaque fait appuyé
  par une source identifiable et datée), **Substance** (information utile, précise, exploitable),
  **Signal** (la section des signaux faibles éclaire vraiment, avec sources), **Lisibilité** (hiérarchie,
  concision, absence de remplissage).
- Deux notes supplémentaires de 0 à 5, propres à ce thème : **Couverture** (les sept axes obligatoires sont-ils tous servis, avec 1 à 3 entrées solides chacun — un axe vide ou rempli d'un article creux coûte des points), **Autorité des sources** (priorité aux sources institutionnelles : régulateurs, caisses, polices, textes de loi, contre la presse généraliste).
- Trois lignes : **Points forts**, **Points faibles**, **Verdict** (une phrase).
- Puis un **classement des neuf bras**, du meilleur au moins bon, avec une justification courte chacun.

Contraintes : **tu n'as pas le droit de naviguer** ; certaines URL peuvent renvoyer un mur anti-robot
(403) sans être fausses — distingue toujours « invérifiable » de « manifestement fausse ». Sois exigeant :
les neuf veilles sont directement comparables, donc chaque écart de note doit s'appuyer sur un élément
précis du texte.

Format attendu, exactement :

```
### bras-1
Conformité : 4/5
Sourcing : 3/5
Substance : 4/5
Signal : 2/5
Lisibilité : 5/5
Couverture : 4/5
Autorité des sources : 3/5
Points forts : ...
Points faibles : ...
Verdict : ...
```
… pour les neuf bras, puis :

```
## Classement
1. bras-x — ...
2. ...
```

---



---

# FICHIER : bras-1

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : Cette édition d'octobre 2026 recense 20 articles issus de 20 sources — 17 françaises (85 %) — répartis sur les sept thématiques obligatoires. Deux mouvements dominent le mois : la confirmation d'un niveau record de fraude détectée (946,3 M€ pour l'assurance en 2025 selon l'ALFA, +4,9 % ; 723 M€ pour l'Assurance Maladie, +15 %) et la bascule vers une fraude « industrialisée » par l'IA générative — faux documents, photos de sinistres truquées, deepfakes d'identité. Ce qui monte : l'exploitation des listes noires ACPR/AMF en open data pour sécuriser l'entrée en relation, la coopération parquet/assureurs contre les réseaux organisés (optique, courtage), et un durcissement réglementaire continu (paquet LCB-FT, loi du 25 juin 2026, article 50 de l'AI Act).

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : La fraude documentaire change d'échelle. Des photos de sinistres automobiles truquées par intelligence artificielle trompent les assureurs, et un professionnel sur cinq dit avoir déjà reçu un document numérique falsifié.
- **📈 Efficacité de gestion de la fraude** : L'assurance a détecté neuf cent quarante-six millions d'euros de fraude en deux mille vingt-cinq, un record. Le régulateur rappelle en parallèle les exigences de maturité en matière de lutte anti-blanchiment.
- **🗂️ Exploitation de l'opendata** : Les listes noires de l'ACPR et de l'AMF sont désormais ouvertes en données publiques et permettent de croiser les acteurs non autorisés. Plus de deux mille jeux de données ont été publiés en octobre.
- **🕸️ Lutte contre les bandes organisées** : Les réseaux restent au cœur des affaires : un système d'optique à Paris, un courtage d'assurances à Poitiers signalé par Tracfin, et une fraude à l'Assurance Maladie estimée à cinquante-huit millions d'euros.
- **🚪 Fraude en entrée en relation** : L'entrée en relation se fragilise. Une proposition de loi contre l'usurpation d'identité, une campagne mondiale contre les arnaques aux hypertrucages, et la vigilance de l'ACPR sur les faux conseillers assistés par intelligence artificielle.
- **🩺 Fraude à la santé** : L'Assurance Maladie a stoppé sept cent vingt-trois millions d'euros de fraudes en deux mille vingt-cinq, un record. Faux arrêts de travail, centres de santé fictifs et plus de quatre cents professionnels épinglés par la répression des fraudes.
- **🧪 Divers — sujet émergent** : Les véhicules autonomes produisent des données très détaillées qui pourraient accélérer le traitement des sinistres et mieux détecter la fraude. Europol décrit par ailleurs une cybercriminalité dopée à l'intelligence artificielle.

## 1. 🔍 Anti-fraude documentaire

- **[Assurances : quand l'IA simule des accidents](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)** — *franceinfo (France 2), 4 juillet 2026*
  Des escrocs retouchent en quelques clics, via l'IA générative, des photos de voitures pour simuler des sinistres auto. Direct Assurance détaille la détection (cassure de pare-brise non « en étoile ») et indique avoir « multiplié par 3,5 le nombre de faux documents reçus », pour jusqu'à 16 M€ de demandes frauduleuses repérées par an.
  **Pourquoi c'est pertinent ?** Le sinistre auto devient un point d'entrée IA : les gestionnaires de sinistres doivent exiger des photos géolocalisées et horodatées (type WeProov) plutôt que des pièces déjà modifiables.
  *À surveiller* : les applications de déclaration à photos analysées en direct comme nouveau standard anti-fraude. **Impact réglementaire** : peines rappelées (5 ans de prison, 375 000 € d'amende).
- **[Avec l'IA, la fraude documentaire s'industrialise : les assureurs sont-ils prêts ?](https://www.journaldunet.com/fintech/1557315-avec-l-ia-la-fraude-documentaire-s-industrialise-les-assureurs-sont-ils-prets/)** — *Journal du Net (chronique), 3 novembre 2026*
  La falsification n'est plus marginale mais « accessible et automatisable » : selon le baromètre Yousign × Ipsos 2026, un professionnel sur cinq déclare avoir déjà été confronté à un document numérique falsifié ou compromis. L'auteur en tire trois leviers : proportionner le niveau de preuve au risque, sécuriser tout le cycle de vie documentaire, intégrer la gouvernance documentaire au risk management.
  **Pourquoi c'est pertinent ?** La charge de la preuve pèse sur l'assureur : en souscription comme en sinistre, la valeur d'une pièce dépend de son horodatage, de sa traçabilité et du niveau eIDAS appliqué.
  **Impact réglementaire** : RGPD, DDA, Solvabilité II, eIDAS, contrôles ACPR.
- **[En forte hausse, la fraude documentaire se banalise à tous les niveaux de la société](https://www.archimag.com/veille-documentation/2026/07/10/forte-hausse-fraude-documentaire-banalise-tous-niveaux-societe)** — *Archimag, 10 juillet 2026*
  Relais du 2e rapport de l'Observatoire Tessi de la fraude documentaire : 903 M€ de fraudes détectées en assurance (+30 % en un an), 723 M€ pour l'Assurance Maladie et 13 % des Français déclarant avoir déjà falsifié un document. La fraude ne se limite plus à un document isolé mais à des ensembles cohérents (kits d'identité).
  **Pourquoi c'est pertinent ?** Le chiffrage transversal assurance/banque/santé aide à justifier un budget de forensique documentaire face à une direction qui ne voit que son propre silo.
  *À surveiller* : analyse des métadonnées et recoupement multi-documents comme socle de détection.

## 2. 📈 Efficacité de gestion de la fraude

- **[Rapport d'activité 2025 — Les chiffres clés de la fraude à l'assurance](https://www.alfa.asso.fr/)** — *ALFA (Agence de lutte contre la fraude à l'assurance), 17 juillet 2026*
  L'agence (19 des 20 principaux groupes français) chiffre 946,3 M€ de fraude identifiée en 2025 (+4,9 %), dont 626,6 M€ en IARD et 319 M€ en assurance de personnes et vie ; le taux de fraude atteint 1,27 % des prestations versées. L'ALFA rappelle que ces montants ne sont qu'une partie du phénomène, qu'elle estime à ~2,5 Md€ par an.
  **Pourquoi c'est pertinent ?** C'est la référence sectorielle annuelle pour calibrer un KPI de fraude détectée, comparer sa branche et argumenter un ROI (détection avant paiement vs recouvrement après versement).
  Complément : reprise presse — [La Tribune, 10 juillet 2026](https://www.latribune.fr/article/banques-finance/assurance/76854307418288/fraude-a-lassurance-pres-dun-milliard-deuros-detectes-en-2025).
- **[Synthèse des contrôles AMF en matière de LCB-FT et d'EAI (2022-2025)](https://www.amf-france.org/sites/institutionnel/files/private/2026-06/Synth%C3%A8se%20des%20contr%C3%B4les%20AMF%20en%20mati%C3%A8re%20de%20LCB-FT%20et%20d%E2%80%99EAI%20(2022-2025)_1.pdf)** — *AMF, juin 2026*
  L'Autorité des marchés financiers synthétise quatre ans de contrôles et de suites : insuffisances récurrentes sur la cartographie des risques LCB-FT, la connaissance client (KYC, bénéficiaires effectifs), les obligations déclaratives à Tracfin, la formation et le contrôle interne.
  **Pourquoi c'est pertinent ?** Grille de maturité directement transposable à un dispositif LCB-FT assurantiel : mêmes obligations de vigilance, de profilage du risque et de déclaration de soupçon.
  **Impact réglementaire** : CMF (L. 561 et suivants), positions AMF DOC-2019-14 à 18, 6e directive et paquet AML.
- **[Le paquet « AML » : ce qui change pour les assujettis](https://acpr.banque-france.fr/fr/actualites/le-paquet-aml)** — *ACPR / Banque de France, mise à jour 24 septembre 2026*
  L'ACPR détaille le nouveau corpus LCB-FT : la 6e directive (AMLD6) sur les registres centralisés de comptes (FICOBA, IBAN virtuels, bénéficiaires effectifs) et le règlement AMLR directement applicable (extension du champ supervisé, vigilance renforcée, nouveau régime de personnes politiquement exposées, seuil d'espèces). Transposition au plus tard le 10 juillet 2027 ; supervision directe de l'AMLA dès 2028.
  **Pourquoi c'est pertinent ?** Anticiper le chantier KYC/onboarding : mesures de vigilance sur les transactions occasionnelles et régime PPE élargi toucheront les parcours de souscription et les intermédiaires d'assurance.
  **Impact réglementaire** : AMLR, AMLD6, AMLA (calendrier 2027-2028).

## 3. 🗂️ Exploitation de l'opendata

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers (jeu de données)](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *data.gouv.fr, producteur AMF, mise à jour 5 novembre 2026*
  Le fichier CSV recense les sites et acteurs inscrits sur les listes noires de l'AMF ainsi que ceux usurpant l'identité d'un acteur régulé, avec nom, catégorie de produit concerné et date d'inscription. Il est également publié en PDF par l'AMF.
  **Pourquoi c'est pertinent ?** Croisement automatisable en entrée en relation : confronter les sites, domaines et IBAN d'un dossier candidat à cette base pour repérer une usurpation d'un acteur autorisé, sans attendre un signal de fraude.
- **[Escroqueries : l'ACPR met en garde le public contre les propositions frauduleuses de crédits, de livrets d'épargne, de services de paiement et d'assurances](https://acpr.banque-france.fr/fr/communiques-de-presse/escroqueries-lacpr-met-en-garde-le-public-contre-les-propositions-frauduleuses-de-credits-de-livrets-22)** — *ACPR / Banque de France, 13 janvier 2026*
  En 2025, l'ACPR a inscrit 1 190 sites ou entités sur sa liste noire (dont 146 au dernier trimestre) ; 62 % de ces offres usurpent l'identité d'un établissement autorisé. 99 sites ou courriels usurpant l'identité de l'ACPR, de la Banque de France ou de l'AMF ont aussi été inscrits.
  **Pourquoi c'est pertinent ?** Le taux d'usurpation (62 %) impose de croiser registres officiels (REGAFI, REFASSU, ORIAS) et liste noire, et pas seulement de contrôler des documents.
  **Impact réglementaire** : mission LCB-FT de l'ACPR ; listes noires mutualisées (Assurance-Banque-Épargne Info Service).
- **[Suivi des sorties — Octobre 2026](https://www.data.gouv.fr/posts/suivi-des-sorties-octobre-2026)** — *data.gouv.fr, 3 novembre 2026*
  2 181 jeux de données et 559 réutilisations publiés en octobre 2026 ; parmi les réutilisations, des outils de vérification d'entreprise par SIREN (identité, statut, procédures collectives) et une base de jurisprudence en accès libre.
  **Pourquoi c'est pertinent ?** Ces briques open data alimentent gratuitement un contrôle anti-fraude d'entrée en relation : faux fournisseurs, sociétés coquilles vides, entités en liquidation.

## 4. 🕸️ Lutte contre les bandes organisées

- **[Courtage d'assurances : entre abus de biens sociaux et escroqueries, un procès à 2,5 millions d'euros de préjudices à Poitiers](https://www.lanouvellerepublique.fr/poitiers/courtage-d-assurances-entre-abus-de-biens-sociaux-et-escroqueries-un-proces-a-2-5-millions-d-euros-de-prejudices-a-poitiers-1793651487)** — *La Nouvelle République, 2 novembre 2026*
  Un signalement de Tracfin a déclenché l'enquête pour escroquerie en bande organisée et abus de biens sociaux : la société de courtage ABD Solution vendait de faux « prêts participatifs » promettant 7 %, les nouveaux prêts couvrant les anciens jusqu'à la banqueroute. Trois anciens associés ont été jugés le 17 septembre 2026.
  **Pourquoi c'est pertinent ?** Illustration du courtage comme cheval de Troie (assurance et produits financiers) et du rôle du renseignement financier : l'alerte ne vient pas d'un sinistre mais de Tracfin.
  **Impact réglementaire** : LCB-FT, déclaration de soupçon Tracfin, escroquerie en bande organisée.
- **[Ils avaient organisé un système de fraude : le pacte aux millions d'euros entre opticiens, patients et ophtalmologues](https://actu.fr/ile-de-france/paris_75056/ils-avaient-organise-un-systeme-de-fraude-le-pacte-aux-millions-d-euros-entre-opticiens-patients-et-ophtalmologue_64842908.html)** — *actu.fr, 26 septembre 2026*
  Le parquet de Paris renvoie 22 personnes (opticiens, ophtalmologues, présidents d'associations de santé) devant le tribunal au printemps 2027 pour escroquerie et blanchiment en bande organisée : un système de récompenses (avoirs, montures de luxe) pour maximiser la prise en charge par les mutuelles. L'affaire a démarré sur des signalements de mutuelles.
  **Pourquoi c'est pertinent ?** Typologie du « pacte à trois » prestataire/prescripteur/assuré et rôle des signalements d'organismes complémentaires comme détecteur d'une fraude en réseau.
  **Impact réglementaire** : escroquerie et blanchiment aggravés (jusqu'à 10 ans de prison).
- **[Sept personnes mises en examen dans une affaire hors norme de fraudes à l'Assurance maladie (58 M€)](https://www.franceinfo.fr/economie/fraude/sept-personnes-mises-en-examen-dans-une-affaire-hors-norme-de-fraudes-a-l-assurance-maladie-pour-un-montant-estime-a-58-millions-d-euros_7896257.html)** — *franceinfo, 26 mars 2026*
  Un vaste réseau est poursuivi pour une fraude à la CPAM estimée à 58 M€ ; sept personnes ont été mises en examen, dont une figure présentée comme l'organisatrice.
  **Pourquoi c'est pertinent ?** Donne l'ordre de grandeur des fraudes « industrielles » et justifie des cellules d'enquête dédiées (pôles interrégionaux) et un partage d'information renforcé avec les parquets.

## 5. 🚪 Fraude en entrée en relation

- **[Proposition de loi n° 3228 visant à mieux réprimer l'usurpation d'identité et à garantir l'accompagnement et le rétablissement rapide des victimes](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi)** — *Assemblée nationale, déposée le 6 octobre 2026*
  Le texte (17e législature) durcit la répression de l'usurpation d'identité et organise le rétablissement des victimes.
  **Pourquoi c'est pertinent ?** L'usurpation d'identité est citée comme premier vecteur de fraude en assurance vie (devant les faux RIB) : un cadre pénal renforcé change les attentes de preuve et de coopération entre victimes, assureurs et autorités.
  **Impact réglementaire** : évolution du droit pénal de l'usurpation d'identité (article 226-4-1 du code pénal).
- **[INTERPOL launches public awareness campaign highlighting risk of AI deepfake scams](https://www.interpol.int/fr/Actualites-et-evenements/Actualites/2026/INTERPOL-launches-public-awareness-campaign-highlighting-risk-of-AI-deepfake-scams)** — *INTERPOL, 19 octobre 2026*
  Via le projet SynthWave PLUS, INTERPOL lance une campagne mondiale (trois vidéos elles-mêmes générées par IA) sur les arnaques aux deepfakes : imitation d'un proche ou d'un collègue, appel visio demandant un virement, manipulation émotionnelle. Recommandations : mot de sécurité, vérification par un canal connu, double authentification.
  **Pourquoi c'est pertinent ?** La disparition des « signaux faibles » (fautes, incohérences) rend inopérants les contrôles basés sur la forme : la vérification d'identité à distance doit combiner détection d'injection et multi-facteurs.
  *À surveiller* : la détection d'injection (caméra virtuelle, émulateur) en KYC.
- **[Fraudes et arnaques financières en ligne à l'ère de l'intelligence artificielle](https://acpr.banque-france.fr/system/files/2026-01/FRAUDES%20ET%20ARNAQUES%20FINANCI%C3%88RES%20%C3%A0%20l'%C3%A8re%20de%20l'IA_0.pdf)** — *ACPR / Banque de France, janvier 2026*
  Le guide de l'ACPR recense les schémas dopés à l'IA, dont l'usurpation d'identité et les deepfakes : un escroc se présentant comme un « distributeur d'assurances » pour soutirer des coordonnées bancaires ou faire transférer des fonds, avec clonage vocal et numéro de téléphone falsifié.
  **Pourquoi c'est pertinent ?** Les signaux d'alerte et réflexes listés (mot de sécurité, vérification indépendante, refus du virement sous pression) sont transposables aux scripts de relation client et aux alertes anti-fraude.

## 6. 🩺 Fraude à la santé

- **[Lutte contre les fraudes à l'Assurance Maladie : 723 M€ détectés et stoppés en 2025](https://www.assurance-maladie.ameli.fr/presse/2026-04-16-dp-lcf)** — *Assurance Maladie (CNAM), 16 avril 2026*
  Dossier de presse officiel : 723 M€ de fraudes détectées et stoppées en 2025 (+15 %), un record — dont 34 M€ de préjudice lié aux faux arrêts de travail et 9 700 dossiers de faux arrêts repérés ; 1 700 agents dédiés. Depuis juillet, de nouveaux arrêts de travail sécurisés (hologramme, bandes fluorescentes) et des détecteurs scannant 4 500 pages par heure.
  **Pourquoi c'est pertinent ?** Le poste le plus dynamique (faux arrêts) est un enjeu direct pour l'assurance de prévoyance : industrialisation du faux document, usurpation d'identité de médecins, sécurisation du support.
  *À surveiller* : l'ordonnance numérique et le contrôle automatique avant paiement.
- **[Factures incohérentes, devis non transparents… la répression des fraudes épingle plus de 400 professionnels de santé](https://www.liberation.fr/societe/sante/factures-incoherentes-devis-non-transparents-la-repression-des-fraudes-a-epingle-plus-de-400-professionnels-de-sante-20261012_ZAUWJA5BHFCCNEDQX6ULIW4C2Y/)** — *Libération, 12 octobre 2026*
  La DGCCRF a contrôlé 1 100 établissements et cabinets libéraux (dont 525 dentistes) : pour 40 % d'entre eux, des manquements graves (factures incohérentes, devis non transparents), avec amendes et procédures pénales. La quasi-totalité s'est mise en conformité.
  **Pourquoi c'est pertinent ?** Un angle « transparence tarifaire » souvent négligé : les mêmes factures et devis alimentent les remboursements des organismes complémentaires, qui ont intérêt à les contrôler.
  **Impact réglementaire** : obligations d'information tarifaire, signalements SignalConso.
- **[Fraude à l'assurance maladie : un rapport propose un meilleur ciblage des contrôles (IGF/IGAS)](https://www.vie-publique.fr/en-bref/304384-fraude-lassurance-maladie-rapport-inspection-igas-igf)** — *Vie-publique.fr, 25 août 2026*
  Synthèse officielle du rapport IGF/IGAS publié le 29 juillet 2026 : 628 M€ de fraude détectée en 2024 (contre 219 M€ en 2021), dont 69 % du préjudice imputable aux professionnels de santé ; le recouvrement ne récupère qu'environ la moitié des indus. Les inspecteurs recommandent plus de science des données, un contrôle automatique avant paiement et davantage d'échanges avec les organismes complémentaires.
  **Pourquoi c'est pertinent ?** Ces recommandations (datamining, contrôle avant paiement, échanges AM/OC) sont exactement ce que l'assurance santé complémentaire peut industrialiser côté fraude.

## 7. 🧪 Divers — sujet émergent

- **[Automated Vehicles and the Data Revolution in Motor Claims](https://insurance-edge.net/2026/11/05/automated-vehicles-and-the-data-revolution-in-motor-claims/)** — *Insurance Edge (DAC Beachcroft), 5 novembre 2026*
  Les véhicules autonomes enregistrent en continu vitesse, freinage, direction, environnement et décisions du système. Pour les assureurs, ces données (dont le DSSAD déjà imposé par l'UNECE) pourraient accélérer l'établissement des responsabilités et « améliorer la détection de la fraude » — à condition d'un jeu de données minimal standardisé et d'une chaîne de conservation fiable.
  **Pourquoi c'est pertinent ?** Anticiper un futur socle probatoire numérique : qui contrôlait le véhicule, et une preuve technique opposable en cas de sinistre contesté.
  *À surveiller* : accès des assureurs au DSSAD et standardisation des formats. (Source étrangère, sans équivalent français sur ce sujet.)
- **[IOCTA 2026 — How encryption, proxies and AI are expanding cybercrime](https://www.europol.europa.eu/publication-events/main-reports/iocta-2026-evolving-threat-landscape)** — *Europol, 28 avril 2026*
  L'Internet Organised Crime Threat Assessment annuel d'Europol décrit un paysage criminel où le chiffrement, les proxys et l'IA élargissent l'échelle des fraudes et des schémas en ligne.
  **Pourquoi c'est pertinent ?** Cadre européen de référence pour positionner l'exposition fraude/cyber d'un portefeuille et alimenter le dialogue avec Europol et l'ENISA.
  **Impact réglementaire** : priorités européennes EMPACT 2026-2029.

## Synthèse — 5 signaux faibles à surveiller

1. **La fraude documentaire générée par IA devient le premier vecteur d'entrée** (sinistres auto truqués, faux justificatifs, kits d'identité cohérents) : le contrôle « à l'œil » ne suffit plus, la preuve doit être horodatée et géolocalisée. Sources : [franceinfo, 4 juillet 2026](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html) ; [Archimag (Observatoire Tessi), 10 juillet 2026](https://www.archimag.com/veille-documentation/2026/07/10/forte-hausse-fraude-documentaire-banalise-tous-niveaux-societe) ; [Journal du Net, 3 novembre 2026](https://www.journaldunet.com/fintech/1557315-avec-l-ia-la-fraude-documentaire-s-industrialise-les-assureurs-sont-ils-prets/).
2. **Le chiffrage de la fraude atteint des records et s'installe comme indicateur de pilotage** : 946,3 M€ (assurance) et 723 M€ (Assurance Maladie) en 2025 — un socle de ROI pour les dispositifs de détection. Sources : [ALFA, 17 juillet 2026](https://www.alfa.asso.fr/) ; [Assurance Maladie (CNAM), 16 avril 2026](https://www.assurance-maladie.ameli.fr/presse/2026-04-16-dp-lcf).
3. **L'open data des listes noires devient un outil d'onboarding** : croiser listes ACPR/AMF, registres (REGAFI/REFASSU/ORIAS) et vérification SIREN pour repérer l'usurpation d'un acteur autorisé. Sources : [data.gouv.fr — listes noires AMF](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france) ; [ACPR, 13 janvier 2026](https://acpr.banque-france.fr/fr/communiques-de-presse/escroqueries-lacpr-met-en-garde-le-public-contre-les-propositions-frauduleuses-de-credits-de-livrets-22) ; [data.gouv.fr — suivi des sorties, 3 novembre 2026](https://www.data.gouv.fr/posts/suivi-des-sorties-octobre-2026).
4. **La coopération public-privé se durcit contre les réseaux organisés** : signalements de mutuelles et de Tracfin au cœur des dossiers (optique, courtage). Sources : [La Nouvelle République, 2 novembre 2026](https://www.lanouvellerepublique.fr/poitiers/courtage-d-assurances-entre-abus-de-biens-sociaux-et-escroqueries-un-proces-a-2-5-millions-d-euros-de-prejudices-a-poitiers-1793651487) ; [actu.fr, 26 septembre 2026](https://actu.fr/ile-de-france/paris_75056/ils-avaient-organise-un-systeme-de-fraude-le-pacte-aux-millions-d-euros-entre-opticiens-patients-et-ophtalmologue_64842908.html) ; [franceinfo, 26 mars 2026](https://www.franceinfo.fr/economie/fraude/sept-personnes-mises-en-examen-dans-une-affaire-hors-norme-de-fraudes-a-l-assurance-maladie-pour-un-montant-estime-a-58-millions-d-euros_7896257.html).
5. **Le cadre réglementaire se resserre sur l'identité et les deepfakes** : proposition de loi sur l'usurpation d'identité, paquet LCB-FT, article 50 de l'AI Act. Sources : [Assemblée nationale, 6 octobre 2026](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi) ; [ACPR — paquet AML](https://acpr.banque-france.fr/fr/actualites/le-paquet-aml) ; [INTERPOL, 19 octobre 2026](https://www.interpol.int/fr/Actualites-et-evenements/Actualites/2026/INTERPOL-launches-public-awareness-campaign-highlighting-risk-of-AI-deepfake-scams).


---

# FICHIER : bras-2

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : Treize articles retenus pour cette édition d'octobre 2026, dont trois publiés dans le mois lui-même et dix références de l'été 2026 sans lesquelles le tableau serait incomplet — octobre a été riche en mises à jour de fichiers publics mais discret en événements médiatisés, d'où ce recours assumé à la tolérance de dates. La tendance de fond est au **passage de la détection individuelle à l'infrastructure partagée** : fichier Banque de France des IBAN suspects opérationnel depuis mai, listes noires AMF/ACPR rafraîchies fin octobre sur data.gouv.fr, échéance EUDI Wallet fixée à la France par le ministère de l'Intérieur. Ce qui monte : l'industrialisation de la fraude documentaire par IA générative (faux documents multipliés par trois et demi chez un assureur auto) et le rebasculage des contrôles santé vers les professionnels, acté par le rapport IGF-IGAS. À noter côté méthode : L'Argus de l'assurance, Les Échos et les pages ACPR restent inaccessibles à l'automatisation (DataDome/Akamai) — les faits cités sont donc adossés à la source primaire quand elle est téléchargeable, ou à une reprise presse accessible ; la source étrangère unique (Commission européenne, AI Act) est gardée comme cadre réglementaire, la part française atteignant douze entrées sur treize.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : Les photos d'accident retouchées par intelligence artificielle inondent les déclarations : un assureur auto a vu les faux documents multipliés par trois et demi. Depuis août, le marquage européen des contenus synthétiques devient une arme de détection.
- **📈 Efficacité de gestion de la fraude** : Le rapport Alfa affiche neuf cent quarante-six millions d'euros de fraudes détectées en deux mille vingt-cinq, un taux d'un virgule vingt-sept pour cent des prestations. La loi de juin contre les fraudes sociales et fiscales ouvre de nouveaux leviers de recouvrement.
- **🗂️ Exploitation de l'opendata** : Les listes noires de l'AMF et de l'ACPR, actualisées fin octobre sur data point gouv, et le fichier Banque de France des IBAN suspects permettent d'alimenter automatiquement les contrôles d'entrée en relation et les blocages de virements.
- **🕸️ Lutte contre les bandes organisées** : Un réseau parisien d'ophtalmologues et d'opticiens, détournant douze millions d'euros par an au détriment des mutuelles, sera jugé en deux mille vingt-sept ; la police judiciaire de son côté démantèle une bande aux faux banquiers et faux procureurs.
- **🚪 Fraude en entrée en relation** : Banque de France et ACPR alertent sur des vidéos truquées imitant leurs dirigeants pour pousser à de faux virements ; l'application France Identité, futur portefeuille européen d'identité, deviendra une référence d'authentification à accepter d'ici deux mille vingt-sept.
- **🩺 Fraude à la santé** : Le rapport IGF-Igas publié cet été tord le cou aux idées reçues : les professionnels de santé concentrent soixante-treize et demi pour cent des fraudes détectées. Cap explicitement recommandé : cibler les gros dossiers et contrôler avant paiement.
- **🧪 Divers** : Le Grand Paris se porte candidat aux expérimentations de robotaxis dès deux mille vingt-huit avec Stellantis et Bolt. Une question neuve se pose aux assureurs : sans conducteur, qui garantit le véhicule, qui pilote la flotte, qui déclare le sinistre.

## 1. 🔍 Anti-fraude documentaire

- **[Assurances : quand l'IA simule des accidents](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)** — *franceinfo (France 2), 4 juillet 2026*
  Un reportage de JT documente la production industrielle de faux sinistres : photos de pare-brise ou de carrosserie truquées en quelques clics par IA générative, avec des artefacts visibles à l'œil expert (fracture « en étoile » mal répartie). Direct Assurance déclare jusqu'à 16 millions d'euros de demandes frauduleuses détectées par an et un nombre de faux documents **multiplié par 3,5** ; des assureurs imposent désormais des applications de déclaration photographiant en direct, géolocalisées et horodatées (WeProov).
  **Pourquoi c'est pertinent ?** Le gestionnaire de sinistres découvre ici la bascule du justificatif : la photo « reçue par mail » devient une pièce à risque, remplacée par la capture contrôlée in situ — un KPI concret (×3,5 de faux documents) à intégrer aux tableaux de bord SIU.
  *À surveiller* : la généralisation des parcours de déclaration avec photo live géolocalisée, transposable à l'habitation et à la santé ; la fraude documentaire passe du document isolé au capteur d'acquisition. Rappel pénal cité : 5 ans d'emprisonnement et 375 000 € d'amende.

- **[La Commission commence à faire appliquer les règles de la législation sur l'IA et les nouvelles exigences de transparence le 2 août](https://digital-strategy.ec.europa.eu/fr/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)** — *Commission européenne, communiqué du 31 juillet 2026 (source institutionnelle européenne, cadre réglementaire — seule source non française de l'édition)*
  Depuis le 2 août 2026, l'article 50 de l'AI Act oblige les fournisseurs d'IA générative à **marquer les contenus synthétiques dans un format lisible par machine** (audio, image, vidéo, texte) et les déployeurs à étiqueter les deepfakes ; les systèmes mis sur le marché avant le 2 août bénéficient d'un délai jusqu'au 2 décembre 2026 pour le marquage, et plus de 180 organisations ont signé le code de bonnes pratiques sur la transparence des contenus générés par IA.
  **Pourquoi c'est pertinent ?** C'est le premier socle juridique d'une forensique automatisable : une photo de sinistre non marquée mais détectée comme synthétique devient une pièce à charge, et l'absence de marquage côté fraudeur deviendra une présomption exploitable en contentieux.
  **Impact réglementaire (AI Act)** : à intégrer aux référentiels de preuve et aux clauses antifraude des polices ; le rapport DLA Piper de septembre 2026 (source non retenue, blog de cabinet) confirme le point de vigilance « marquer n'est pas prouver ».

## 2. 📈 Efficacité de gestion de la fraude

- **[Les chiffres clés de la fraude à l'assurance (en 2025) — Rapport d'activité 2025 de l'ALFA](https://www.alfa.asso.fr/)** — *ALFA (Agence de lutte contre la fraude à l'assurance), 17 juillet 2026 (présentation le 9 juillet)*
  L'agence consolidant les remontées de 19 des 20 plus grands groupes d'assurance affiche **946,3 M€ de fraudes identifiées en 2025 (+4,9 %)** — dont 626,6 M€ en IARD (−0,6 %), 294 M€ en assurances de personnes et 24,8 M€ en vie, cette dernière branche **quasi doublée (+101,7 %)** ; le taux de fraude rapporté aux prestations versées s'établit à **1,27 %**, pour un gisement réel estimé à 2,5 Md€. L'ALFA lit elle-même ce résultat comme « l'efficacité des mécanismes de détection déployés par les adhérents ».
  **Pourquoi c'est pertinent ?** C LA référence KPI du secteur : taux de fraude par branche, base de remontées volontaire et périmètre d'adhérents — la grille exacte pour benchmarker votre propre dispositif et arbitrer entre branches (le décrochage de la vie mérite un plan d'action).
  *À surveiller* : le ralentissement de la croissance (+4,9 % après +28 % en 2024) comme possible effet de maturité des dispositifs ; la sophistication des filières à l'IA générative déjà signalée dans le même rapport (recoupement avec l'axe documentaire).

- **[Loi n° 2026-534 du 25 juin 2026 relative à la lutte contre les fraudes sociales et fiscales](https://www.vie-publique.fr/loi/300456-lutte-contre-les-fraudes-sociales-et-fiscales-loi-du-25-juin-2026)** — *Vie publique / Légifrance, promulguée le 25 juin 2026, JO du 26 juin 2026*
  Le texte [déposé à l'Assemblée nationale (dossier n°52985)](https://www.assemblee-nationale.fr/dyn/17/dossiers/dlr5l17n52985) articule le triptyque « mieux prévenir et détecter, mieux lutter et sanctionner, mieux recouvrer », avec des dispositions directement assurarielles : **saisie de la valeur de rachat des contrats d'assurance-vie par opposition à tiers détenteur** pour désintéresser les créanciers sociaux, communication de documents aux organismes de contrôle à titre gratuit sous trente jours (amende de 1 500 € par bénéficiaire en cas de silence), géolocalisation certifiée obligatoire des véhicules de transport sanitaire conventionnés (au plus tard le 1er janvier 2027), identité d'emprunt autorisée pour certains contrôles.
  **Pourquoi c'est pertinent ?** Le service recouvrement et la direction juridique gagnent des outils actionnables — l'assurance-vie devient un gage de dettes de fraude — pendant que le contrôle de conformité document SIN-contrôle monte d'un cran (délai de réponse opposable aux assureurs).
  **Impact réglementaire (loi fraude / LCB-FT)** : plusieurs mesures entrent en vigueur par décret (échéances 2027) — à cartographier dès maintenant dans les procédures de réclamation et de tiers payant santé.

## 3. 🗂️ Exploitation de l'opendata

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers en France](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *AMF sur data.gouv.fr, dernière mise à jour du 29 octobre 2026 (jeu de données, admissible dans cet axe)*
  Le fichier ouvert des listes noires AMF/ACPR (sites, adresses mail et noms d'acteurs, catégorie de produit, date d'inscription) est actualisé quotidiennement — l'AMF y a encore inscrit le 8 octobre 2026 une salve de **sites crypto frauduleux et d'usurpations d'identité d'acteurs régulés** (Five Arrows Rothschild, Paris Majesté…). Téléchargeable en CSV, il alimente déjà des réutilisations industrielles (API Liste Noire AMF, outils de contrôle de domaines).
  **Pourquoi c'est pertinent ?** Croisé automatiquement en onboarding et en gestion de réclamations, il transforme une mise en garde réglementaire en règle de screening : détection temps réel des faux conseillers usurpant un nom d'intermédiaire inscrit à l'ORIAS. Limite assumée et documentée : liste non exhaustive.
  *À surveiller* : le rapprochement avec le registre REGAFI (agréments) et le registre ORIAS — trois bases publiques, un seul dispositif de vérification à la source.

- **[Lancement de la plateforme des IBAN suspects : le fichier national des comptes signalés pour risque de fraude (FNC-RF)](https://presse.economie.gouv.fr/lancement-de-la-plateforme-des-iban-suspects-un-nouvel-outil-cle-de-lutte-contre-la-fraude-aux-paiements/)** — *Ministère de l'Économie et Banque de France, communiqué du 7 mai 2026*
  Tenu par la Banque de France depuis le [7 mai 2026](https://www.banque-france.fr/system/files/2026-05/joe_20260428_arrete_technique.pdf) ([arrêté technique du 24 avril 2026, JO du 28 avril](https://www.banque-france.fr/system/files/2026-05/joe_20260428_arrete_technique.pdf)) en application de la loi du 6 novembre 2025, le FNC-RF mutualise entre tous les prestataires de services de paiement les IBAN signalés frauduleux : date de détection, canal, méthode, catégorie de fraude, et **l'existence d'une plainte pour usurpation d'identité**. Le fichier doit s'articuler au dispositif européen de partage des données de fraude (règlement services de paiement).
  **Pourquoi c'est pertinent ?** Pour l'anti-fraude assurance, c'est la fin du « silo bancaire » : un RIB de fraude au dédommagement signalé par une banque peut désormais être bloqué chez tous les acteurs de paiement — à croiser avec le fichier sinistres pour repérer un IBAN de bénéficiaire déjà blacklisté.
  *À surveiller* : le risque de duplication des bases (FEDRA au niveau européen) et l'extension de l'accès aux assureurs en tant que donneurs d'ordre de sinistres.

## 4. 🕸️ Lutte contre les bandes organisées

- **[Un système d'escroqueries impliquant des ophtalmologues et des opticiens démantelé à Paris](https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925)** — *Le Figaro (AFP), 25 septembre 2026*
  Sur signalement de **mutuelles de santé** en 2025, l'enquête de l'OCLTI (gendarmerie) pilotée par le parquet de Paris a démantelé un système « assuré–opticien–prescripteur » cherchant la prise en charge maximale puis la conversion en avoirs (montures de luxe, solaires) : quelque **12 M€ détournés par an depuis 2023**, un préjudice soupçonné de **250 M€ sur la plaque parisienne**, 22 prévenus (dont deux ophtalmologues et dix opticiens) et 15 structures renvoyés devant la justice en juin 2027, 1,3 M€ de matériel saisi.
  **Pourquoi c'est pertinent ?** Modèle type du signalement assurantiel déclencheur d'une procédure de bande organisée : le détecteur mutualiste (cohérence remboursement/prescription) a fait office de pièce de départ du dossier judiciaire — la démonstration que la détection interne nourrit le pénal.
  *À surveiller* : l'audience de juin 2027 (qualification, confiscations) et l'extension du schéma « généralisé » à d'autres enseignes ; typologie directement transposable à l'audioprothèse et au dentaire, déjà cités par l'IGAS-IGF.

- **[Un réseau de vol de lingots d'or démantelé à Toulouse](https://www.ouest-france.fr/region-occitanie/toulouse-31000/un-reseau-de-vol-de-lingots-dor-demantele-a-toulouse-7f11f6ae-c363-11f1-a107-88e926908e5f)** — *Ouest-France (AFP), 8 octobre 2026*
  La police judiciaire a démantelé un réseau d'escroqueries par ruse à qui onze faits sont imputés, pour plus de 2 M€ au total : les malfaiteurs « se faisaient passer pour des **banquiers, des procureurs, des policiers** ». Trois suspects — deux exécutants et un donneur d'ordre — ont été mis en examen le 8 octobre 2026 après l'interpellation en flagrant délit d'une seconde opération ; un septuagénaire toulousain avait été dépouillé de plus d'un million d'euros en lingots.
  **Pourquoi c'est pertinent ?** L'usurpation de « fausse qualité » est le mode opératoire que subissent aussi les assurés contactés au nom de leur assureur pour « débloquer un sinistre » : la géographie des interpellations (Toulouse–Limoges) et la répartition des rôles offrent une grille d'analyse réseau réusable en SIU (liste noire de numéros, récurrence des profils prête-noms).
  *À surveiller* : le basculement de ces bandes du patrimoine physique vers les remboursements d'assurance et de mutuelle, même matrice victime vulnérable/urgence/autorité usurpée.

## 5. 🚪 Fraude en entrée en relation

- **[La Banque de France et l'ACPR mettent en garde le public contre un risque de fraude avec usurpation de leur identité et de celle de leurs dirigeants](https://acpr.banque-france.fr/fr/communiques-de-presse/la-banque-de-france-et-lacpr-mettent-en-garde-le-public-contre-un-risque-de-fraude-avec-usurpation-0)** — *Banque de France / ACPR, 27 avril 2026 (page autorité protégée par WAF ; [repris en anglais par la Banque de France](https://www.banque-france.fr/en/press-release/banque-de-france-and-acpr-are-warning-public-risk-fraud-involving-identity-theft-both-institutions))*
  Les deux institutions signalent des fraudes utilisant l'IA pour créer des **deepfakes usurpant l'image du gouverneur François Villeroy de Galhau et de la secrétaire générale de l'ACPR** : faux messages sur les réseaux sociaux dirigeant vers des sites frauduleux, appels promettant un virement important (succession, épargne) contre paiement préalable de « frais ». La règle édictée par l'autorité : « jamais un dirigeant de la Banque de France ou de l'ACPR ne recommandera un site ou un produit ».
  **Pourquoi c'est pertinent ?** Même schéma d'hypertrucage applicable à un directeur régional ou à un service sinistres usurpé pour faire dévier un règlement — la consigne « le régulateur ne demande jamais de fonds » est à dupliquer verbatim dans les messages de l'assureur (SMS/espace client) comme anti-mesure d'onboarding inversé.
  **Impact réglementaire (LCB-FT / AI Act)** : ces usurpations alimentent la liste noire AMF/ACPR publiée en open data (cf. axe 3) — boucle alerte autorité → fichier partagé → screening.

- **[Reconnaissance de l'application « France Identité » par tous les services publics et fournisseurs de services — réponse du ministère de l'Intérieur](https://www.senat.fr/questions/base/2026/qSEQ260207874.html)** — *Sénat / JO Sénat du 28 mai 2026*
  Le ministère confirme que près de **3,5 millions de citoyens** ont créé une identité numérique via France Identité (CNIe), déjà utilisée pour une carte Vitale dématérialisée par ~850 000 assurés, mais que ses justificatifs « ne bénéficient pas d'une acceptation équivalente à la photocopie de carte d'identité » en droit français. Cap légal rappelé : chaque État membre doit fournir un **portefeuille EUDI au plus tard fin novembre 2026**, et les acteurs privés soumis à authentification forte devront le reconnaître d'ici 2027 ; un projet de décret « Attestation France Identité » est en préparation (DLPAJ).
  **Pourquoi c'est pertinent ?** Pour la souscription et la LCB-FT, l'échéance est opérationnelle : le parcours KYC assuré standard de 2027 sera la présentation sélective d'attributs vérifiés par l'État — anticiper les spécifications d'acceptation dans les schémas directeur d'onboarding.
  *À surveiller* : le décret Attestation France Identité et l'alignement eIDAS 2 de l'application (les comparateurs type didit.me, source non retenue, notaient au 5 octobre 2026 que la France n'avait pas annoncé de lancement EUDI conforme).

## 6. 🩺 Fraude à la santé

- **[Escroquerie de 723 millions d'euros à l'Assurance-maladie : un rapport à charge pour les professionnels de santé libéraux](https://www.lequotidiendumedecin.fr/liberal-soins-de-ville/escroquerie-de-723-millions-deuros-lassurance-maladie-un-rapport-charge-pour-les-professionnels-de)** — *Le Quotidien du Médecin, 27 août 2026 (sur le [rapport IGF-IGAS en ligne ici](https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf))*
  Le rapport conjoint IGF-IGAS (finalisé octobre 2025, mis en ligne à l'été 2026) documente que **73,5 % des 723 M€ de fraudes détectées et stoppées en 2025** proviennent de professionnels de santé ou de faux professionnels, alors que 30 % des dossiers traités sont des dossiers de moins de 1 000 € d'assurés : « 3 % des dossiers représentent 60 % du préjudice ». Quinze recommandations : basculer les contrôles de l'aval vers l'amont (contrôle automatique avant paiement), resserrer le tiers payant (présentation de la carte Vitale), simplifier les pénalités, couvrir tous les professionnels — le tout pour un gisement estimé à **1,4–1,9 Md€ par an**.
  **Pourquoi c'est pertinent ?** C'est la feuille de route méthodologique de l'anti-fraude santé pour les deux ans : les assureurs complémentaires, destinataires de ces contrôles, doivent aligner leurs propres règles de maîtrise médicalisée sur le « détecter avant débourser » et la data science de schémas.
  **Impact réglementaire** : les suites (décrets, circulaire Cnam) irrigueront les conventions du tiers payant ; recoupement direct avec la loi 2026-534 (axe 2, transport sanitaire).

- **[Une infirmière libérale condamnée en Essonne pour avoir escroqué près de 200 000 € à l'Assurance maladie](https://www.ouest-france.fr/societe/justice/une-infirmiere-liberale-condamnee-en-essonne-pour-avoir-escroque-pres-de-200-000-euros-a-lassurance-maladie-7a7da760-bb47-11f1-889b-45b1452cdab8)** — *Ouest-France (avec Actu Essonne / Le Parisien), 28 septembre 2026*
  Quatre infirmiers libéraux jugés à Évry-Courcouronnes pour ordonnances falsifiées et surfacturations au détriment de patients atteints de cancer (mars 2020–août 2023) : la principale condamnée écope de 15 mois de sursis et 20 000 € d'amende, avec saisie de ses biens à hauteur des **196 000 € détournés** ; un second infirmier d'un an de sursis et 9 000 €.
  **Pourquoi c'est pertinent ?** Cas d'école de la typologie « ordonnances détournées + actes de support (pansements, soins palliatifs) », celle que les modèles de scoring de complémentaire santé doivent apprendre à séparer de la simple courbe d'activité normale — une règle de détection par nomenclature vaut ici des années de contentieux.
  *À surveiller* : l'effet dissuasif des saisies de biens prononcées en répression, de plus en plus systématiques dans les jugements santé.

## 7. 🧪 Divers — sujet émergent

- **[Véhicules autonomes : des villes d'Île-de-France candidates pour tester les robots-taxis](https://www.la-croix.com/societe/vehicules-autonomes-des-villes-d-ile-de-france-candidates-pour-tester-les-robots-taxis-20261023)** — *La Croix, 23 octobre 2026*
  Aux Assises du véhicule autonome du 23 octobre, deux expérimentations françaises de robotaxis ont été présentées au programme européen ADACities : d'un côté Clichy avec G7 et la start-up Milla, de l'autre la **Métropole du Grand Paris avec Bolt et Stellantis** (jusqu'à 33 véhicules dans cinq communes dès 2028, extension à une trentaine et exploitation commerciale visée en 2030), technologie Pony.ai/NVIDIA. Les autorisations, la supervision à distance et le financement européen restent à trancher.
  **Pourquoi c'est pertinent ?** Sujet de couverture non encore assuré : sans conducteur au sens classique, la chaîne d'intérêt (propriétaire du véhicule, opérateur de flotte non désigné dans le consortium, constructeur, passager) n'a pas de nom — pour le souscripteur et le gestionnaire de sinistres auto, la fenêtre de qualification du risque s'ouvre maintenant, avant les premiers contrats commerciaux.
  *À surveiller* : le régime de responsabilité et le modèle assurantiel des flottes (le consortium ne désigne personne pour « faire rouler » les voitures), et la typologie de sinistre émergente que l'on n'a pas encore vue en IARD : l'accident simulé à un véhicule sans occupant.

## Synthèse — 5 signaux faibles à surveiller

1. **Le marquage machine-readable des contenus IA devient l'antidote naturel de la photo de sinistre truquée** : au-delà des détections d'artefacts, l'absence de marque obligatoire (AI Act art. 50) ou sa falsification est déjà une signalisation forensic exploitable — avec un délai de mise en conformité des systèmes anciens au 2 décembre 2026.
   Sources : https://digital-strategy.ec.europa.eu/fr/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august — https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html

2. **L'infrastructure française anti-fraude se monte par fichiers interconnectés** : IBAN suspects (FNC-RF), listes noires AMF/ACPR en open data, registres ORIAS/REGAFI — l'assureur qui ne branche pas son onboarding et sa gestion sinistres sur ces flux cross-secteurs paie seul le coût de l'information manquante.
   Sources : https://presse.economie.gouv.fr/lancement-de-la-plateforme-des-iban-suspects-un-nouvel-outil-cle-de-lutte-contre-la-fraude-aux-paiements/ — https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france

3. **Le signalement assurantiel devient la pièce de déclenchement des procédures de bande organisée** : le réseau optique parisien est né d'une alerte de mutuelles — la chaîne « détection interne → parquet → OCLTI/GIR » est désormais praticable, et l'audience de juin 2027 en testera la solidité probatoire.
   Sources : https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925 — https://www.ouest-france.fr/region-occitanie/toulouse-31000/un-reseau-de-vol-de-lingots-dor-demantele-a-toulouse-7f11f6ae-c363-11f1-a107-88e926908e5f

4. **La fraude à l'assurance-vie repart de l'avant (+101,7 % en 2025, presque doublée) sur la matrice usurpation d'identité + faux RIB + fraude documentaire** : la branche petite en montant, forte en croissance, signale un déplacement des fraudeurs vers les avoirs financiers — durcissement LCB-FT des parcours de rachat à anticiper.
   Sources : https://www.alfa.asso.fr/ — https://acpr.banque-france.fr/fr/communiques-de-presse/la-banque-de-france-et-lacpr-mettent-en-garde-le-public-contre-un-risque-de-fraude-avec-usurpation-0

5. **La France entre dans l'ère du justificatif d'identité d'État vérifiable** : EUDI Wallet au plus tard fin novembre 2026, reconnaissance par les acteurs à authentification forte d'ici 2027, décret « Attestation France Identité » en préparation — le KYC assurance se standardisera sur l'attribut certifié, pas sur le scan de pièce.
   Sources : https://www.senat.fr/questions/base/2026/qSEQ260207874.html — https://digital-strategy.ec.europa.eu/fr/faqs/transparency-obligations-under-article-50-ai-act


---

# FICHIER : bras-3

# Veille Fraude Assurance — 3 novembre 2026


**Synthèse** : Octobre 2026 confirme le basculement de la fraude assurance vers l'échelle industrielle — faux dégâts générés par IA, ordonnances fictives en réseau, usurpation d'identité par deepfake — et, en miroir, une mobilisation sans précédent des autorités françaises : DGCCRF qui publie le 12 octobre le bilan de 1 100 contrôles chez les professionnels de santé, AMF et ACPR qui ajoutent une cinquantaine de sites frauduleux à leurs listes noires au troisième trimestre, parquet et gendarmerie qui renvoient 22 personnes devant les juges pour le réseau d'escroquerie dans l'optique parisien. La référence chiffrée du marché reste le rapport ALFA de juillet 2026 : 946 millions d'euros de fraude identifiée en 2025 (+4,9 % seulement, contre +28 % en 2024), signe que les dispositifs de détection montent en maturité alors que la fraude réelle est estimée à 2,5 milliards d'euros. Ce qui monte : le partage de données entre assurance maladie et complémentaires (validé par le Conseil constitutionnel, avec la revue de dépenses IGF/IGAS qui pousse les contrôles en amont du paiement) et les obligations de marquage de l'AI Act applicables depuis le 2 août 2026, qui deviennent une infrastructure probante pour la lutte anti-fraude documentaire.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : Les faux dégâts produits par intelligence artificielle inondent les services sinistres, et la France doit s'équiper pour-authentifier le vrai. Depuis le deux août, le marquage lisible par machine des contenus générés par l'IA est une obligation légale européenne. Le rapport Tessi chiffre l'usage de l'IA par un tiers des faussaires.

- **📈 Efficacité de gestion de la fraude** : Année de maturité pour la détection : l'ALFA plafonne la hausse à cinq pour cent après vingt-huit l'an dernier, avec neuf cent quarante-six millions d'euros identifiés. Le rapport IGF IGAS recommande de basculer les contrôles avant le paiement et de mieux cibler par la science des données. La MAIF formalise un pôle fraude dédié.

- **🗂️ Exploitation de l'opendata** : Les listes noires AMF et ACPR s'enrichissent : une cinquantaine de sites ajoutés au troisième trimestre, consultables en fichiers ouverts sur data point gouv. Le Conseil constitutionnel valide l'échange de données entre assurance maladie et complémentaires pour la détection de fraude, sous conditions strictes.

- **🕸️ Lutte contre les bandes organisées** : Vingt-deux personnes, dont deux ophtalmologues et dix opticiens, seront jugées pour le réseau d'ordonnances fictives signalé par les mutuelles, douze millions d'euros par an détournés. À Poitiers, un tribunal juge trois courtiers en assurance sur signalement Tracfin, deux millions et demi de préjudice.

- **🚪 Fraude en entrée en relation** : Un escroc usurpait l'identité de commissaires et de magistrats pour vider les comptes de notaires, démasqué après un an de traque. L'ACPR publie son guide des arnaques à l'ère de l'IA : faux conseiller, deepfake vocal, urgence fabriquée. La vigilance à l'onboarding devient un poste de contrôle.

- **🩺 Fraude à la santé** : La DGCCRF publie le bilan de mille cent contrôles chez les soignants libéraux : trente-neuf pour cent de manquements, notamment chez les dentistes. Une ex-infirmière de Gironde est suspectée de neuf cent dix mille euros de détournements, avec une contestation inédite : celle de l'extrapolation statistique de la caisse.

- **🧪 Divers** : Après les pillages des dix-sept et vingt-quatre octobre, la taxe émeutes entre en scène : une contribution de zéro virgule huit pour cent sur les primes financera dès deux mille vingt-sept un fonds de mutualisation des dégâts graves. Nouvel aléa de couverture, et nouveau terrain de déclarations gonflées.

## 1. 🔍 Anti-fraude documentaire

- **[Assurances : des faux dégâts pour frauder](https://www.franceinfo.fr/economie/assurances-des-faux-degats-pour-frauder_8096006.html)** — *franceinfo, 6 juillet 2026*
  Reportage de référence sur l'industrialisation des faux sinistres : l'intelligence artificielle générative permet de produire en quelques clics des photos de dégâts crédibles (pare-chocs, infiltrations, bris de glace) adressées en gré à gré, sans expertise terrain. Les assureurs répondent par la capture d'images à la source via l'app de l'assuré, la métadonnée et la contre-vérification météo. Lien direct avec l'assurance : c'est le sinistre IARD et MRH qui est visé, cœur des SIU.
  **Pourquoi c'est pertinent ?** Le gré à gré photo-based est le maillon le plus exposé aux images synthétiques : l'article documente le rapport 1 dossier frauduleux détecté pour une centaine indemnisés à 2 000 euros, soit un risque de perte récurrente à faible unit cost mais fort volume.
  À surveiller : le passage d'une détection par artefacts (qui perd du terrain) à l'authentification à la source des médias — capture signée, chaînage des métadonnées, capteurs dans l'app mobile.

- **[Règlement européen sur l'IA : des mesures concrètes pour informer et protéger les internautes](https://www.economie.gouv.fr/actualites/reglement-europeen-sur-lia-des-mesures-concretes-pour-informer-et-proteger-les-internautes)** — *Bercy — economie.gouv.fr, 25 août 2026*
  Fiche officielle française sur l'entrée en application le 2 août 2026 de l'article 50 de l'AI Act : les fournisseurs de systèmes génératifs doivent incruster un marquage lisible par machine dans les images, vidéos, audios et textes produits ou manipulés par IA — comparable au filigrane d'un billet de banque — et les déployeurs étiqueter les deepfakes via trois pictogrammes européens (généré intégralement / partiellement modifié par IA). Impact assurance : la pièce produite au dossier de sinistre ou de souscription portera désormais une preuve de nature synthétique détectable par outil.
  **Pourquoi c'est pertinent ?** Pour un fraude manager, c'est le début d'une chaîne de traçabilité légale des médias de preuve : les moteurs de détection d'IA sur les justificatifs photographiques s'appuieront sur ce marquage, avec une opposabilité nouvelle en contentieux.
  Impact réglementaire : AI Act article 50, obligations applicables au 2 août 2026 (délai au 2 décembre 2026 pour le marquage des systèmes mis sur le marché avant cette date, pas d'étiquetage rétroactif du contenu antérieur) ; articulation RGPD à suivre sur la conservation des empreintes de génération.

- **[Fraude documentaire : le 2ᵉ rapport de l'Observatoire Tessi](https://www.tessi.eu/wp-content/uploads/2026/07/cp-fraude-documentaire-le-2e-rapport-de-lobservatoire-tessi-20260707.pdf)** — *Observatoire documentaire Tessi, 7 juillet 2026*
  Étude à méthodologie déclarée qui croise les chiffres d'autorité (903 M€ de fraudes détectées en assurance, 723 M€ par l'Assurance maladie) et des données terrain : 13 % des Français déclarent avoir déjà falsifié un document, 32 % des fraudeurs ayant falsifié un document ont utilisé l'IA générative, la fraude numérique atteint 57 % du total. Les experts nuancent : « l'IA est un auxiliaire pour le fraudeur, pas un faussaire autonome » — les documents générés conservent des artefacts détectables. Le rapport cartographie aussi les ripostes structurantes : registre européen des IBAN frauduleux opérationnel depuis mai 2026, eIDAS II, circulaires ALFA, dispositif Stop Fraudes.
  **Pourquoi c'est pertinent ?** Seule source datée quantifiant l'usage effectif de l'IA générative par les faussaires eux-mêmes — de quoi calibrer les seuils des modèles de détection documentaire et la formation des opérateurs.
  (Sélection : rapport d'un acteur technologique, accepté comme white paper à chiffres vérifiables — un seul par thématique ; les données d'autorité qu'il reprend, ALFA et Cnam, sont citées séparément en thèse 2.)

## 2. 📈 Efficacité de gestion de la fraude

- **[Fraude à l'assurance — chiffres clés 2025 (rapport d'activité)](https://www.alfa.asso.fr/fraude-a-lassurance/)** — *ALFA (Agence de lutte contre la fraude à l'assurance), rapport présenté le 9 juillet 2026*
  Bilan de référence du marché français : 946,3 millions d'euros de fraude identifiée en 2025 par les adhérents (dont 626,6 M€ en IARD, 182 M€ en prévoyance, 112,4 M€ en santé +20,5 %, 24,8 M€ en vie +86,5 %), soit +4,9 % seulement après le bond de +28 % de 2024 — l'ALFA y voit « l'efficacité des mécanismes de détection déployés par les adhérents ». Le taux de fraude s'établit à 1,27 % des prestations payées ; la fraude réelle est estimée à 2,5 milliards d'euros. Typologies dominantes : fausses déclarations, fraude documentaire (photos modifiées par IA incluses), surestimation.
  **Pourquoi c'est pertinent ?** C'est LE KPI de référence de la profession : la décélération de la hausse est l'argument ROI le plus solide à présenter en comité de direction pour justifier le budget antifraude.
  (Anti-doublons : le rapport ALFA a été massivement repris — Les Échos, Le Figaro, AFP, MoneyVox, comparateurs ; une seule entrée, l'organisme source.)

- **[La lutte contre la fraude aux prescriptions et aux facturations à l'assurance maladie](https://www.igf.gouv.fr/rapports-de-mission/la-lutte-contre-la-fraude-aux-prescriptions-et-aux-facturations-lassurance)** — *IGF / IGAS, revue de dépenses publiée le 29 juillet 2026 (màj 10 septembre 2026)*
  Revue inter-inspections officielle : la fraude détectée s'élève à 628 M€, dont 70 % imputables à des professionnels de santé ou à des usurpateurs/falsificateurs d'identité. Recommandations structurantes : bascule stratégique de l'aval vers l'amont des paiements (contrôles embarqués dans le système de paiement pour rejeter les indus avant décaissement), feuille de route de l'ordonnance numérique, ciblage par science des données des schémas émergents, rééquilibrage des contrôles vers les dossiers à fort enjeu financier et coordination renforcée CPAM-parquets. Le rapport documente aussi Asafo-Pharma (signalement d'ordonnances suspectes par les pharmaciens) et la généralisation progressive du contrôle automatique avant paiement.
  **Pourquoi c'est pertinent ?** C'est le modèle de maturité que les SIU des complémentaires doivent répliquer : déplacer la détection avant le paiement change l'équation du ROI antifraude, et l'extrapolation contrôlée des anomalies y est explicitement défendue.
  À surveiller : l'agenda de déploiement des contrôles embarqués (lot pharmacie finalisé, montée en gamme des contrôles automatisés prévue à mi-2027).

- **[Rapport sur la solvabilité et la situation financière 2025 du groupe MAIF — C.5.5 « Risque de fraude »](https://entreprise.maif.fr/files/live/sites/entreprise-Maif/files/pdf/nos-rapports/rapports-solvabilite/2025/rapport-solvabilite-groupe-maif-2025.pdf)** — *MAIF (rapport SFCR 2025, publié en 2026)*
  Un mutualiste décrit noir sur blanc son dispositif antifraude dans un document réglementaire : un pôle spécialisé qui définit la politique et coordonne l'opérationnel, la détection des situations litigieuses « en contrat qu'en sinistre », et une gouvernance reposant sur l'acculturation de l'ensemble des acteurs de l'entreprise. Exemple rare de publication par un assureur français de son organisation de lutte contre la fraude dans le cadre SFCR, sous le contrôle du régulateur.
  **Pourquoi c'est pertinent ?** Pour benchmarkant la maturité LCB-FT/antifraude, le SFCR d'un assureur est la source la plus opposable qui soit : le dispositif y est déclaré au régulateur, pas marketing.
  À surveiller : la généralisation de ce type de divulgation par les autres groupes (le « risque de fraude » tend à devenir une rubrique standard des rapports prudentiels).

## 3. 🗂️ Exploitation de l'opendata

- **[L'AMF et l'ACPR mettent en garde le public contre plusieurs acteurs proposant en France des investissements sur le Forex et sur des produits dérivés sur crypto-actifs sans y être autorisés](https://www.amf-france.org/fr/actualites-publications/communiques/communiques-de-lamf/lamf-et-lacpr-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-2)** — *AMF / ACPR, 22 octobre 2026*
  Communiqué conjoint d'octobre : depuis début 2026, 57 sites non autorisés ajoutés en catégorie Forex et 36 en dérivés sur crypto-actifs (respectivement 26 et 10 au troisième trimestre). Le communiqué renvoie aux vérifications croisées que toute équipe conformité ou souscription peut automatiser : registre REGAFI (prestataires habilités), annuaire ORIAS (intermédiaires CIF), listes ABE Infoservice et API data.gouv. Typologie récurrente côté épargne : usurpation de l'identité d'acteurs régulés — même vecteur que la souscription frauduleuse en assurance vie.
  **Pourquoi c'est pertinent ?** La périodicité trimestrielle et les comptages d'ajouts font de ces communiqués une métrique publique de la pression frauduleuse sur l'épargne-assurance, directement comparable trimestre après trimestre.
  Impact réglementaire : usage des listes noires AMF/ACPR comme socle de screening LCB-FT et de la vigilance à l'entrée en relation (art. L.561-5 CMF).

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers en France](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *data.gouv.fr (producteur : AMF), jeu ouvert mis à jour en continu — entrées datées du 8 octobre 2026*
  Le dataset ouvert agrège les mises en garde AMF/ACPR au format CSV (nom du site ou adresse mail frauduleuse, catégorie du produit, date d'inscription), sous Licence Ouverte 2.0, avec explorateur de données et réutilisations déclarées. Cas d'usage concret pour l'anti-fraude : alimenter un contrôle automatique de conformité des collecteurs d'épargne vie ou des intermédiaires présentés en souscription, et croiser les adresses mail usurpées avec les fichiers de sinistres/versements. Les entrées du 8 octobre 2026 montrent le rythme soutenu des ajouts (usurpations d'acteurs régulés en majorité).
  **Pourquoi c'est pertinent ?** Un fichier machine-readable des autorités, c'est un dispositif KYC/amont qui peut se tester en production sans contrat fournisseur : le coût d'entrée d'une brique opendata dans la stack antifraude est quasi nul.
  (Jeu de données admis ici car constitutif de la thématique opendata ; l'entrée précise ce qu'il permet de faire, au-delà de l'inventaire.)

- **[Projet de loi fraude : le Conseil constitutionnel valide l'échange de données entre Assurance maladie et complémentaires](https://www.egora.fr/actus-pro/politiques/projet-de-loi-fraude-le-conseil-constitutionnel-valide-lechange-de-donnees)** — *egora.fr (presse pro santé/assurance), 19 juin 2026*
  Décision 2026-904 DC du 18 juin 2026 sur la loi du 25 juin 2026 de lutte contre les fraudes sociales et fiscales : l'échange d'informations entre régimes obligatoires et complémentaires au titre de la lutte anti-fraude est validé « sous de strictes conditions » (finalité limitée à l'identification de l'auteur et des actes frauduleux, interdiction d'usage commercial ou tarifaire), la dérogation au secret médical encadrée — mais le recours à un « intermédiaire » technique est censuré pour défaut d'encadrement. Les mutuelles et assureurs complémentaires peuvent donc espérer un accès élargi aux données d'investigation des caisses.
  **Pourquoi c'est pertinent ?** C'est le texte fondateur du futur croisement de données AMO↔AMC : les gestionnaires de sinistres santé et les LCB-FT doivent se préparer à des sign entrants normalisés — et à un devoir de signalement en sens inverse.
  Impact réglementaire : loi n° 2026-534 du 25 juin 2026, art. L.114-9-1 CSS ; censure partielle de l'article 21 ; décret d'attente (saisine [dossier législatif](https://www.assemblee-nationale.fr/dyn/17/dossiers/dlr5l17n52985)).

## 4. 🕸️ Lutte contre les bandes organisées

- **[Un système d'escroqueries impliquant des ophtalmologues et des opticiens démantelé à Paris](https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925)** — *Le Figaro avec AFP, 25 septembre 2026*
  Vingt-deux personnes — dont deux ophtalmologues, dix opticiens et trois présidents d'associations de santé — et quinze personnes morales (cinq centres d'ophtalmologie) seront jugées en juin 2027 pour escroquerie en bande organisée et blanchiment : ordonnances fictives délivrées sans examen des patients, produits coûteux inutiles dissimulés dans les stocks, remboursements mutuelles détournés en avoirs. L'enquête OCLTI, ouverte en 2025 après le signalement de mutuelles, chiffre le détournement à environ 12 millions d'euros par an depuis 2023 — et soupçonne un volume généralisé de 250 millions d'euros sur la plaque parisienne. Perquisitions d'ampleur entre janvier et juillet 2026 ; le parquet a transmis les données aux administrations (redressements fiscaux, déconventionnement, sanctions ordinales).
  **Pourquoi c'est pertinent ?** Cas d'école de la coopération assureurs-justice : le signalement croisé de deux mutuelles a déclenché un démantèlement pénal — exactement le schéma SIU-multi-organismes que la profession appelle de ses vœux sur les réseaux santé.
  (Anti-doublons : même événement repris par La Tribune de l'Assurance et la presse régionale ; une entrée, le média national citant les communiqués du parquet de Paris et de la gendarmerie.)

- **[Courtage d'assurances : entre abus de biens sociaux et escroqueries, un procès à 2,5 millions d'euros de préjudices à Poitiers](https://www.lanouvellerepublique.fr/poitiers/courtage-d-assurances-entre-abus-de-biens-sociaux-et-escroqueries-un-proces-a-2-5-millions-d-euros-de-prejudices-a-poitiers-1793651487)** — *La Nouvelle République, 2 novembre 2026*
  Trois anciens associés d'une société de courtage jugés à Poitiers : sous couvert de courtage assurance, ils commercialisaient des « prêts participatifs » maison promettant 7 % de rendement — un montage où les nouveaux prêts couvraient les anciens jusqu'à la banqueroute, sur une enquête pénale ouverte après signalement Tracfin du procureur de la République. Sept ans de contrôle judiciaire avant le jugement du 17 septembre 2026, 2,5 millions d'euros de préjudices déclarés.
  **Pourquoi c'est pertinent ?** Typologie « cabine de courtage » : la fraude en réseau qui abuse de l'apparence de régulation (numéro ORIAS, façade d'expertise) — le signalement Tracfin rappelle que la chaîne LCB-FT est le déclencheur, et que la presse judiciaire locale documente les failles de contrôle des intermédiaires.

## 5. 🚪 Fraude en entrée en relation

- **[« Attrape-moi si tu peux » : la traque rocambolesque d'un jeune escroc qui narguait la police et usurpait l'identité de commissaires et de magistrats](https://www.lemonde.fr/societe/article/2026/10/13/attrape-moi-si-tu-peux-la-traque-rocambolesque-d-un-jeune-escroc-qui-narguait-la-police-et-usurpait-l-identite-de-commissaires-et-de-magistrats_6793112_3224.html)** — *Le Monde, 13 octobre 2026*
  Mis en examen et écroué le 11 septembre par le Parquet national anticriminalité organisée (PNACO), un Français de 25 ans opérait depuis Israël une fraude à l'ingénierie sociale cible : se faire passer pour un procureur du PNF ou un commissaire au téléphone, avec documents d'emprunt d'identité, pour détourner des fonds de cabinets notariaux et d'entreprises — des centaines de victimes sollicitées, une trentaine identifiées à ce stade, préjudice en cours d'évaluation (communiqué PNACO du 28 septembre).
  **Pourquoi c'est pertinent ?** Transposable trait pour trait au « faux conseiller / faux agent d'assureur » qui décroche au sujet d'un sinistre ou d'un contrat : l'usurpation d'autorité institutionnelle au téléphone reste le premier vecteur de manipulation des victimes, et la serialité confirme que le deepfake vocal n'est même plus nécessaire quand la posture suffit.
  À surveiller : la méthode du second canal de vérification (rappeler le numéro officiel du contrat, jamais celui fourni par l'appelant) comme standard de sensibilisation assurés.

- **[Fraudes et arnaques financières en ligne à l'ère de l'IA](https://acpr.banque-france.fr/system/files/2026-01/FRAUDES%20ET%20ARNAQUES%20FINANCI%C3%88RES%20%C3%A0%20l'%C3%A8re%20de%20l'IA_0.pdf)** — *ACPR — Banque de France, janvier 2026 (PDF vérifié en ligne)*
  Le régulateur assureurs-banque formalise la taxonomie des arnaques à l'ère générative : usurpation d'identité d'un conseiller ou d'un membre de la famille via deepfake vocal ou vidéo, appels à numéro falsifié, prétextes exploitant le contrat d'assurance (« activité suspecte sur votre compte ou problème avec votre contrat ») pour soutirer coordonnées bancaires, codes de validation ou installation de logiciels. Fiche pédagogique grand public — l'ACPR attend des assujettis LCB-FT qu'ils la relayent.
  **Pourquoi c'est pertinent ?** C'est la matrice officielle des scénarios d'ingénierie sociale en entrée en relation et en cours de vie du contrat : aligner les scripts de sensibilisation clients et les questions du contrôle interne sur la taxonomie ACPR est un gage d'opposabilité en inspection.
  Note d'accès : l'ACPR est derrière un mur anti-bot (Akamai) en navigation automatisée ; le PDF lui-même est chargé et vérifié le 8 novembre 2026 (réponse HTTP 200, 1,6 Mo).

## 6. 🩺 Fraude à la santé

- **[L'information du patient-consommateur par les professionnels de santé : des manquements relevés (bilan de contrôle DGCCRF 2025-2026)](https://www.economie.gouv.fr/dgccrf/laction-de-la-dgccrf/les-enquetes-et-les-controles/linformation-du-patient-consommateur-par-les-professionnels-de-sante-des-points)** — *DGCCRF, page publiée le 12 octobre 2026 (révélée par Libération)*
  Bilan officiel de la campagne de contrôles 2025-2026 : plus de 1 100 établissements de soignants libéraux et structures d'exercice collectif audités après signalements SignalConso, ordres professionnels et Assurance maladie — 39 % ont reçu une suite corrective ou répressive. Chez les 525 dentistes contrôlés, 52 % ne respectaient pas l'affichage des prix ou l'information sur le conventionnement, un quart ne remettaient pas le devis normalisé ; un centre d'imagerie a écopé de 150 000 € d'amende pour avoir fait croire au secteur 1 alors que les dépassements dominaient ; des structures facturaient l'accès ou des frais administratifs, avec des écarts constatés entre sommes encaissées et sommes déclarées à l'Assurance maladie et des demandes de paiement uniquement en liquide. Plus de 130 000 € d'amendes administratives au 1ᵉʳ octobre 2026 ; plusieurs procédures pénales en cours.
  **Pourquoi c'est pertinent ?** Les écarts prix déclarés/encaissés et le liquide sont des signaux d'indus et de double facturation qui remontent désormais par une autorité économique — un flux de données de contrôle que les complémentaires (tiers payant) ont tout intérêt à croiser avec leurs remboursements.
  (Anti-doublons : Libération 12/10, Le Quotidien du Médecin 13/10, Le Figaro 12/10 — une entrée, la source d'autorité.)

- **[Une infirmière du bassin d'Arcachon soupçonnée d'avoir escroqué près d'un million d'euros à la CPAM](https://www.lefigaro.fr/bordeaux/une-infirmiere-du-bassin-d-arcachon-soupconnee-d-avoir-escroque-pres-d-un-million-d-euros-a-la-cpam-20261016)** — *Le Figaro (avec Sud Ouest), 16 octobre 2026*
  Garde à vue de huit heures le 13 octobre à la gendarmerie d'Arcachon pour une ex-infirmière libérale d'Arès : la CPAM de Gironde a relevé 75 % d'anomalies sur ses facturations 2021-2022 (soins et pansements facturés à domicile pendant l'hospitalisation des patients, toilettes surdéclarées, actes des remplaçantes facturés à son nom) puis étendu ce taux aux cinq années d'exercice, chiffrant le préjudice à 910 000 euros ; saisie conservatoire de ses biens immobiliers ordonnée, investigations en cours. L'avocat conteste précisément la méthode : « la CPAM extrapole sans preuve ».
  **Pourquoi c'est pertinent ?** Le débat de l'extrapolation statistique au procès est le miroir exact du contentieux de la donnée dans les compagnies : toute détection par écart aux moyennes (anomalie de volume, actes impossibles) sera opposée au juge avec ou sans robustesse méthodologique — les SIU doivent documenter leurs modèles d'extrapolation comme la CPAM.
  Impact réglementaire : pénalités et suites conformes au cadre de la loi du 25 juin 2026 (cumul pénalités + sanctions conventionnelles) ; présomption d'innocence — décision de justice non intervenue.

## 7. 🧪 Divers — sujet émergent

- **[Quelle est cette « taxe émeutes » qui pourrait faire augmenter les prix des contrats d'assurance ?](https://www.lefigaro.fr/conjoncture/quelle-est-cette-taxe-emeutes-qui-pourrait-faire-augmenter-les-prix-des-contrats-d-assurance-20261029)** — *Le Figaro, 29 octobre 2026*
  Les violences et pillages des 17 et 24 octobre 2026 (au moins 3 000 commerces saccagés selon le gouvernement) remettront sur la table un dispositif voté dans la loi de finances 2026 mais jamais déclenché : un fonds de mutualisation garanti par l'État, alimenté aux trois quarts par une contribution de 0,8 % prélevée sur les primes auto, habitation et multirisque pro de tous les assureurs, opérationnel au 1ᵉʳ janvier 2027 sous réserve du Conseil d'État. Le fonds n'interviendra qu'au-delà de seuils massifs (dommages de plus de 700 000 € sur un épisode, 300 000 € sur bâtiments publics, ou 30 sinistres de plus de 10 000 €) — l'essentiel des dégâts d'octobre restant à la charge des assureurs, estimée globalement autour du milliard d'euros pour les deux week-ends selon la presse économique.
  **Pourquoi c'est pertinent ?** Nouvelle exposition non anticipée pour les porteurs auto et MRH : obligation de couvrir le risque émeute, seuils de déclenchement par événement, et en période de sinistres de masse gonflés, un terrain historiquement fertile pour déclarations tardives, rétroactives ou surfacturées — les SIU doivent prévoir des filtres « post-catastrophe ».
  À surveiller : la cartographie déclenchement du fonds vs garantie émeutes contractuelle, et la prime de 0,8 % comme signal tarifaire sur les renouvellements 2027.
  Voir aussi : [franceinfo — « Vers une taxe émeutes sur vos assurances ? »](https://www.franceinfo.fr/archives/2026/26-octobre-2026.html) (26 octobre 2026) et [Radio France — L'édito éco « Pillages : une taxe de 0,8 % sur nos assurances »](https://www.radiofrance.fr/franceinter/podcasts/l-edito-eco/l-edito-eco-du-lundi-26-octobre-2026-5361016) (26 octobre 2026).

## Synthèse — 5 signaux faibles à surveiller

1. **L'authentification à la source évince la détection d'artefacts.** Entre AI Act article 50 (marquage lisible par machine depuis le 2 août 2026) et capture signée des photos de sinistres, la chaîne de preuve documentaire se restructure — les outils de criminalistique IA ne suffisent plus seuls. Sources : https://www.economie.gouv.fr/actualites/reglement-europeen-sur-lia-des-mesures-concretes-pour-informer-et-proteger-les-internautes , https://www.franceinfo.fr/economie/assurances-des-faux-degats-pour-frauder_8096006.html , https://www.tessi.eu/wp-content/uploads/2026/07/cp-fraude-documentaire-le-2e-rapport-de-lobservatoire-tessi-20260707.pdf

2. **Le contrôle automatique avant paiement devient la doctrine officielle.** La revue IGF/IGAS consacre sa première recommandation au basculement de l'aval vers l'amont, avec feuille de route ordonnance numérique et échéance mi-2027 pour la montée en gamme des contrôles automatisés pharmacie ; la Cnam applique déjà le Cerfa sécurisé. Sources : https://www.igf.gouv.fr/rapports-de-mission/la-lutte-contre-la-fraude-aux-prescriptions-et-aux-facturations-lassurance , https://www.lefigaro.fr/bordeaux/une-infirmiere-du-bassin-d-arcachon-soupconnee-d-avoir-escroque-pres-d-un-million-d-euros-a-la-cpam-20261016

3. **Les mutuelles sont devenues donneuses d'alerte pénale.** Le démantèlement du réseau optique parisien est né du signalement conjoint de complémentaires santé au parquet — le modèle ALFA/multi-organismes s'étend à la santé et nourrit la coopération OCLTI/parquets. Sources : https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925 , https://www.egora.fr/actus-pro/politiques/projet-de-loi-fraude-le-conseil-constitutionnel-valide-lechange-de-donnees

4. **L'usurpation d'autorité institutionnelle — sans deepfake — progresse en entrée en relation.** Le PNACO démonte une escroquerie aux faux magistrats/commissaires par ingénierie sociale pure ; l'ACPR intègre le même scénario (faux conseiller, faux problème de contrat d'assurance) à sa taxonomie IA. À croiser avec la liste noire AMF/ACPR (usurpations = catégorie dominante des ajouts d'octobre). Sources : https://www.lemonde.fr/societe/article/2026/10/13/attrape-moi-si-tu-peux-la-traque-rocambolesque-d-un-jeune-escroc-qui-narguait-la-police-et-usurpait-l-identite-de-commissaires-et-de-magistrats_6793112_3224.html , https://acpr.banque-france.fr/system/files/2026-01/FRAUDES%20ET%20ARNAQUES%20FINANCI%C3%88RES%20%C3%A0%20l'%C3%A8re%20de%20l'IA_0.pdf , https://www.amf-france.org/fr/actualites-publications/communiques/communiques-de-lamf/lamf-et-lacpr-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-2

5. **Les fraudes de masse « opportunistes » guettent l'après-crise.** Le dispositif taxe émeutes/fonds de mutualisation (seuils par événement, entrée en vigueur 2027) arrive après deux week-ends de pillages : les gros volumes de sinistres déclenchent historiquement une vague de déclarations gonflées ou rétrodatées, à anticiper dans les filtres SIU MRH/pro. Sources : https://www.lefigaro.fr/conjoncture/quelle-est-cette-taxe-emeutes-qui-pourrait-faire-augmenter-les-prix-des-contrats-d-assurance-20261029 , https://www.radiofrance.fr/franceinter/podcasts/l-edito-eco/l-edito-eco-du-lundi-26-octobre-2026-5361016

---



---

# FICHIER : bras-4

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : dix sources retenues ce mois-ci, toutes françaises, avec une nette domination de la fraude santé et documentaire. La tendance de fond est l'industrialisation de la fraude par l'IA générative : faux accidents fabriqués pour l'assurance auto, preuves de sinistre synthétiques, marché noir du KYC vendant faux papiers et deepfakes. Côté chiffres, le socle reste le rapport d'activité 2025 de l'ALFA (946 millions d'euros de fraude détectée chez ses adhérents, dont 627 en IARD) et les 723 millions d'euros stoppés par l'Assurance maladie. Ce qui monte : le ciblage des professionnels de santé plutôt que des assurés (rapport IGF-IGAS) et le durcissement jurisprudentiel de la notion de manœuvre frauduleuse.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : l'intelligence artificielle générative permet désormais de fabriquer de faux accidents automobiles et des preuves de sinistre crédibles en quelques clics. Un couple a aussi mis en scène un cambriolage en incendiant sa maison pour effacer une dette.
- **📈 Efficacité de gestion de la fraude** : le rapport d'activité de l'agence de lutte contre la fraude à l'assurance chiffre à neuf cent quarante-six millions d'euros la fraude détectée en deux mille vingt-cinq. Les régulateurs poussent aussi les professionnels à relayer les alertes aux épargnants.
- **🗂️ Exploitation de l'opendata** : les listes noires de l'Autorité des marchés financiers et de l'Autorité de contrôle prudentiel restent le premier réflexe de contrôle. Une nouvelle mise en garde d'octobre visait Forex et produits dérivés sur crypto-actifs.
- **🕸️ Lutte contre les bandes organisées** : vingt-deux prévenus, dont des ophtalmologues et opticiens, seront jugés à Paris pour une escroquerie aux mutuelles estimée à deux cent cinquante millions d'euros. Le réseau mêlait ordonnances de complaisance et surfacturation massive.
- **🚪 Fraude en entrée en relation** : un marché clandestin du KYC prospère : faux papiers d'identité, comptes déjà vérifiés, vidéos générées par intelligence artificielle et opérateurs humains pour passer la vérification faciale à la place du fraudeur.
- **🩺 Fraude à la santé** : les inspections générales recommandent de concentrer les contrôles sur les professionnels de santé, là où se concentrent les montants. La Cour de cassation a par ailleurs précisé la notion de manœuvre frauduleuse pour les créances des caisses.
- **🧪 Divers — sujet émergent** : l'agence de lutte contre la fraude à l'assurance organise la troisième édition de son Hunter Game, un exercice de détection de fraude en conditions réelles qui forme les équipes des assureurs participants.

## 1. 🔍 Anti-fraude documentaire

- **Assurances : quand l'IA simule des accidents** — *franceinfo, 4 juillet 2026*
  France 2 montre comment des fraudeurs utilisent l'IA générative pour fabriquer de toutes pièces des images d'accidents automobiles et obtenir le remboursement de sinistres qui n'ont jamais existé. Le reportage confirme la migration de la fraude documentaire vers la déclaration de sinistre : la photo, preuve historique de l'expertise, n'est plus un socle fiable. Les dossiers de faux accidents créés par IA ont bondi en France.
  **Pourquoi c'est pertinent ?** L'expert doit désormais intégrer une vérification de provenance et de cohérence des images dans le traitement de chaque sinistre auto, sinon le faux devient indiscernable du vrai.
  *À surveiller* : la détection forensique d'images génératives (analyse de métadonnées, artefacts de diffusion) est directement transposable aux outils d'expertise.

- **Un couple fait croire à un cambriolage et incendie sa maison pour effacer sa dette de 151 000 euros** — *La Dépêche, 21/10/2026*
  Mise en scène complète d'un sinistre habitation : les époux ont organisé un faux cambriolage puis incendié leur maison de l'Aveyron pour faire annuler une dette de 151 000 euros auprès de leur assureur. L'affaire illustre la fraude sinistre classique, mais le contexte économique (dettes croissantes) en augmente l'attractivité.
  **Pourquoi c'est pertinent ?** Rappel utile pour la gestion de sinistres IARD : les indicateurs de stress financier de l'assuré restent un prédicteur de fraude sinistre aussi fort que les anomalies techniques du dossier.

## 2. 📈 Efficacité de gestion de la fraude

- **Rapport d'activité 2025 — ALFA** — *ALFA (alfa.asso.fr), 17 juillet 2026*
  Le rapport annuel de l'Agence de lutte contre la fraude à l'assurance chiffre à 946 millions d'euros la fraude détectée chez les adhérents en 2025, dont 627 millions en IARD — en hausse de 4,9 % sur un an. Il détaille la typologie par branche et confirme que « la fraude devient de plus en plus structurée », portée par des réseaux organisés. C'est la source primaire reprise par toute la presse nationale.
  **Pourquoi c'est pertinent ?** Référence de benchmark obligatoire : KPI par branche, évolution annuelle et typologies pour étalonner son propre dispositif de détection.
  Impact réglementaire : ces chiffres alimentent les travaux de la loi fraude et les attentes de reporting du régulateur.

- **L'AMF et l'ACPR encouragent les professionnels à poursuivre leurs efforts dans l'application de la réglementation lors de la commercialisation de produits d'épargne** — *AMF/ACPR, 12/10/2026*
  Les deux régulateurs publient le 12 octobre 2026 un rappel commun aux professionnels (assureurs, banquiers, conseillers) : poursuite des efforts de conformité dans la commercialisation des produits d'épargne, vigilance renforcée face aux sollicitations frauduleuses et relayage actif des mises en garde aux clients. L'efficacité du dispositif de lutte ne repose plus seulement sur la détection interne mais sur la chaîne complète profession-épargnant-régulateur.
  **Pourquoi c'est pertinent ?** Le signalage client devient un maillon de la chaîne de détection : les équipes conformité et LCB-FT doivent intégrer ces remontées de terrain dans leurs scénarios d'alerte.

## 3. 🗂️ Exploitation de l'opendata

- **L'AMF et l'ACPR mettent en garde le public contre plusieurs acteurs proposant des investissements sur le Forex et les crypto-actifs** — *AMF/ACPR, 22/10/2026*
  Nouvelle mise en garde conjointe du 22 octobre visant plusieurs plateformes non autorisées opérant en France. Les listes noires AMF/ACPR, publiées en opendata sur data.gouv.fr, permettent aux assureurs et banques d'automatiser le screening de ces entités lors de l'entrée en relation et des contrôles de virements sortants.
  **Pourquoi c'est pertinent ?** La liste noire régulière est le dataset le moins cher et le plus direct pour alimenter un contrôle automatique anti-escroquerie : chaque nouvelle publication doit être intégrée au SI de screening.
  Impact réglementaire : cadre AMF-ACPR des mises en garde et obligations de protection de l'épargnant.

## 4. 🕸️ Lutte contre les bandes organisées

- **Arnaque à l'optique : un système d'escroquerie à 250 millions d'euros soupçonné, 22 personnes jugées à Paris** — *La Provence (avec AFP), 27/09/2026*
  Le parquet de Paris renvoie vingt-deux prévenus — ophtalmologues, opticiens et intermédiaires — devant le tribunal correctionnel au printemps 2027 dans une escroquerie aux remboursements de mutuelles estimée jusqu'à 250 millions d'euros de pièces vendues. Le réseau s'appuyait sur des ordonnances de complaisance et la surfacturation de lunettes et lentilles ; l'enquête a été déclenchée par les signalements de Malakoff Humanis et Klesia. Le préjudice directement imputé aux complémentaires santé est chiffré à plusieurs dizaines de millions.
  **Pourquoi c'est pertinent ?** Typologie de référence de la fraude en réseau côté prestataires de santé : signalement assureur → enquête parquet → procès de masse, le modèle de coopération public-privé à reproduire.

## 5. 🚪 Fraude en entrée en relation

- **Le marché noir du KYC vend faux papiers et deepfakes** — *Vigineo, 20/10/2026*
  Le rapport de la société Flare, relayé en français par Vigineo, documente de mars à septembre 2026 un marché clandestin complet pour contourner la vérification d'identité : faux documents d'identité, comptes déjà vérifiés revendus, vidéos de visio générées par IA et — nouveauté — des opérateurs humains qui passent l'entretien liveness à la place du fraudeur. FinCEN et le NIST recommandent en réponse d'examiner le dossier complet et de durcir la preuve de vie.
  **Pourquoi c'est pertinent ?** L'usurpation d'identité en souscription ou en rachat d'assurance-vie ne se limite plus au deepfake : le « KYC as a service » humain déjoue même les contrôles vidéo, ce qui impose une évaluation comportementale et de cohérence du dossier entier.
  *À surveiller* : la détection des injections vidéo et des sessions relayées est transposable aux parcours de souscription à distance.

## 6. 🩺 Fraude à la santé

- **Fraude à l'Assurance maladie : un rapport propose un meilleur ciblage des contrôles (IGF-IGAS)** — *Vie-publique.fr / La Tribune (AFP), 26/08/2026*
  Les inspections générales des Finances et des Affaires sociales recommandent à la Cnam de prioriser les contrôles des professionnels de santé, porteurs de forts enjeux financiers, plutôt que les petits dossiers d'assurés, afin d'augmenter le rendement de la lutte contre la fraude. Le rapport s'appuie sur les 723 millions d'euros de fraudes détectées et stoppées en 2025, record historique, et constate que les soignants concentrent l'essentiel des montants.
  **Pourquoi c'est pertinent ?** Un changement de doctrine de ciblage qui annonce des contrôles plus lourds et plus rentables côté professionnels de santé — à anticiper pour les réseaux de soins et la détection de facturations fictives.

- **Cour de cassation, 2e chambre civile, 15 octobre 2026, pourvoi n° 24-15.050** — *Cour de cassation, 15/10/2026*
  Arrêt publié au Bulletin sur l'article L. 256-4 du code de la sécurité sociale : la manœuvre frauduleuse qui exclut la réduction des créances des caisses suppose une volonté de dissimulation en vue d'obtenir des prestations indues. La Cour censure l'interprétation extensive d'une caisse qui avait qualifié de frauduleuse une simple irrégularité de déclaration.
  **Pourquoi c'est pertinent ?** Garde-fou jurisprudentiel direct pour les recouvrements : la qualification de fraude exigée par les caisses (et par analogie les assureurs) doit être étayée par une dissimulation intentionnelle, pas par la seule irrégularité.

## 7. 🧪 Divers — sujet émergent

- **Hunter Game 3 : l'ALFA relance son jeu de détection de fraude** — *ALFA (alfa.asso.fr), 13/10/2026*
  L'Agence de lutte contre la fraude à l'assurance organise du 13 octobre 2026 la troisième édition de son Hunter Game, un exercice collectif où les équipes des assureurs participants traquent des cas de fraude reconstitués en conditions réelles. L'objectif affiché est de muscler la détection et de partager les typologies émergentes entre compagnies.
  **Pourquoi c'est pertinent ?** Le serious game devient un outil de montée en maturité des SIU et de benchmark inter-assureurs : y participer expose aux typologies d'autres compagnies avant qu'elles ne frappent son propre portefeuille.
  *À surveiller* : le format exercice collaboratif pourrait s'étendre aux fraudes assistées par IA générative.

## Synthèse — 5 signaux faibles à surveiller

1. **La preuve visuelle n'est plus une preuve** : l'IA générative fabrique des accidents et des dégâts inexistants ; les parcours d'expertise sans vérification d'authenticité d'image deviennent la porte d'entrée la moins défendue.
   https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html

2. **Le « KYC as a service » humain** : au-delà des deepfakes, des opérateurs réels passent les vérifications d'identité à la place des fraudeurs — la liveness seule ne suffit plus.
   https://vigineo.fr/2026/10/20/marche-clandestin-kyc-faux-papiers-deepfakes/

3. **Le pivot du ciblage vers les professionnels de santé** : le rapport IGF-IGAS recommande de concentrer les contrôles sur les soignants — attendez-vous à des affaires de facturation fictive plus grosses et plus médiatisées.
   https://www.vie-publique.fr/en-bref/304384-fraude-lassurance-maladie-rapport-inspection-igas-igf
   https://www.latribune.fr/article/economie/41751089770273/fraude-a-l-assurance-maladie-les-professionnels-de-sante-nouveaux-gros-poissons

4. **La fraude en réseau côté prestataires se judiciarise** : le procès des vingt-deux prévenus de l'escroquerie à l'optique (printemps 2027) fera jurisprudence sur la responsabilité des professionnels de santé dans les réseaux de facturation.
   https://www.laprovence.com/article/faits-divers-justice/49117694942881/arnaque-a-l-optique-un-systeme-d-escroquerie-a-250-millions-d-euros-soupconne-22-personnes-jugees-a-paris

5. **La qualification de fraude se resserre juridiquement** : l'arrêt du 15 octobre 2026 exige une dissimulation intentionnelle pour parler de manœuvre frauduleuse — les dossiers de recouvrement mal étayés risquent la censure.
   https://www.courdecassation.fr/decision/6ad099897a102021375f481d

---

*Méthode : chaque date de publication a été vérifiée sur la page source (format JJ/MM/AAAA). 100 % de sources françaises ; les pages ACPR/Banque de France et L'Argus de l'assurance sont inaccessibles à l'automation (murs Akamai/DataDome) — les faits correspondants ont été adossés à des sources accessibles (AMF.france.org, La Provence/AFP, Vigineo). L'article du Journal du Net du 3 novembre 2026 (chronique sponsorisée par un éditeur) et la reprise du rapport ALFA par jechange (comparateur) ont été écartés comme sources forcées ; l'anti-doublon a conduit à ne retenir qu'une seule entrée pour le rapport ALFA et une seule pour le rapport IGF-IGAS.*


---

# FICHIER : bras-5

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : L'édition d'octobre 2026 confirme l'industrialisation de la fraude à l'assurance : la fraude documentaire assistée par IA devient un standard (42 % des fausses preuves détectées seraient générées par IA selon L'Argus, jusqu'à une multiplication par 90 des documents synthétiques chez un éditeur de contrôle), tandis que les assureurs et complémentaires santé subissent une vague inédite de fuites de données (Malakoff Humanis, Actil, Mutuelle Communale, pharmacies). Côté institutionnel, l'AMF et l'ACPR poursuivent leur offensive opendata — listes noires mises à jour, 57 sites Forex et 36 sites crypto-actifs ajoutés depuis janvier — et la lutte contre les bandes organisées franchit l'étape judiciaire (réseau optique estimé à 250 M€ au préjudice des mutuelles, opération Europol). Ce qui monte : la preuve et la traçabilité documentaires (travaux AFNOR sur l'image probatoire, ordonnance numérique), la coopération public-privé et l'exigence de maturité des dispositifs LCB-FT.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : La falsification documentaire assistée par intelligence artificielle s'industrialise : produire un justificatif crédible ne demande plus de compétence technique. Selon les acteurs du secteur, une fausse preuve sur trois présente des traces de manipulation et plus de quarante pour cent seraient désormais générées par intelligence artificielle.
- **📈 Efficacité de gestion de la fraude** : Le pilotage du dispositif compte autant que les outils : détection, faux positifs, délais et préjudice évité. L'ACPR rappelle que la surveillance consolidée des groupes doit atteindre un niveau de maturité attendu, sous peine de sanctions européennes harmonisées pouvant atteindre dix millions d'euros ou dix pour cent du chiffre d'affaires.
- **🗂️ Exploitation de l'opendata** : Les listes noires de l'AMF et de l'ACPR restent l'arme la plus accessible, désormais diffusées aussi sur data point gouv point fr. Un seul jeu de données suffit à contrôler un site ou un démarcheur avant toute souscription.
- **🕸️ Lutte contre les bandes organisées** : La fraude en réseau frappe durement les complémentaires santé : un système d'escroquerie à l'optique a été démantelé à Paris, avec un préjudice estimé à deux cent cinquante millions d'euros. La coopération entre mutuelles, parquet et Europol s'intensifie.
- **🚪 Fraude en entrée en relation** : L'usurpation d'identité reste la fraude la plus fréquente en assurance vie, devant les faux relevés bancaires et la fraude documentaire. Les fuites massives de données de santé exposent numéros de sécurité sociale et coordonnées bancaires, matière première d'une fraude crédible dès la souscription.
- **🩺 Fraude à la santé** : L'Assurance maladie resserre les contrôles sur les prescripteurs d'arrêts de travail, avec six cent cinquante médecins généralistes ciblés, et sécurise la chaîne de prescription via l'ordonnance numérique. Les fausses ordonnances restent le principal vecteur de préjudice.
- **🧪 Divers** : La Banque de France lance une consultation auprès des victimes de fraudes et d'escroqueries financières. En parallèle, la vague de cyberattaques visant les assureurs santé illustre la porosité entre cybersécurité et fraude.

## 1. 🔍 Anti-fraude documentaire

- **[Intelligence artificielle : reconstruire la confiance à l'ère des deepfakes](https://www.argusdelassurance.com/tech/intelligence-artificielle/intelligence-artificielle-reconstruire-la-confiance-a-lere-des-deepfakes.2MRT6YZL6JA65LGG2F2C4RDILE.html)** — *L'Argus de l'assurance, 2 octobre 2026*
  L'analyse rappelle que 42 % des fausses preuves identifiées en assurance seraient désormais générées par des outils d'IA, et souligne un risque double pour l'assureur : un faux peut passer pour authentique, mais un contenu sincère peut aussi être contesté comme possiblement généré. Des travaux menés à l'AFNOR visent un socle commun d'exigences (capture, transmission, conservation) pour les photos et vidéos à usage probatoire, en associant assurance, bâtiment et confiance numérique.
  **Pourquoi c'est pertinent ?** Pour un fraude manager IARD ou un gestionnaire de sinistres, la preuve ne se joue plus seulement dans la détection ex post du faux mais dans la traçabilité « de la capture à l'archivage » — un enjeu de gestion du risque à part entière.
  *À surveiller* : le référentiel AFNOR, directement transposable à la déclaration de sinistre par mobile. **Impact réglementaire** : exigences probatoires à articuler avec le RGPD, la DDA et Solvabilité II.

- **[Avec l'IA, la fraude documentaire s'industrialise : les assureurs sont-ils prêts ?](https://www.journaldunet.com/fintech/1557315-avec-l-ia-la-fraude-documentaire-s-industrialise-les-assureurs-sont-ils-prets/)** — *Journal du Net, 3 novembre 2026*
  La relation assurantielle étant devenue massivement numérique, produire un justificatif crédible, modifier une pièce administrative ou générer un faux certificat cohérent ne requiert plus d'expertise technique. Le baromètre Yousign x Ipsos 2026 indique qu'un professionnel sur cinq a déjà été confronté à un document numérique falsifié.
  **Pourquoi c'est pertinent ?** L'article propose une grille de criticité des actes (engagement financier, exposition juridique, réputation) pour proportionner le niveau de preuve et de traçabilité — le sujet clé du KYC/onboarding et de l'auditabilité des dossiers.
  **Impact réglementaire** : la charge de la preuve reposant sur l'assureur, l'opposabilité (RGPD, DDA, Solvabilité II, contrôles ACPR) dépend de l'horodatage et de la journalisation.

- **[Assurances : quand l'IA simule des accidents](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)** — *franceinfo (France Télévisions), 4 juillet 2026*
  L'enquête montre comment des escrocs modifient en quelques clics une photo de véhicule pour y ajouter des dégâts fictifs (pare-brise, carrosserie) et obtenir un remboursement indu. Direct Assurance explique détecter jusqu'à 16 M€ de demandes frauduleuses par an et impose des applications de déclaration géolocalisées avec analyse en direct.
  **Pourquoi c'est pertinent ?** C'est le cas d'usage de référence sur la fraude documentaire « générée » : le contrôle ne peut plus se limiter à l'examen individuel d'un justificatif. *À surveiller* : les applis de constat mobile (géolocalisation, capture horodatée) comme contre-mesure industrialisable.

## 2. 📈 Efficacité de gestion de la fraude

- **[Forum Fintech ACPR-AMF 2026 — Atelier LCB-FT (supports)](https://acpr.banque-france.fr/system/files/2026-10/Forum-Fintech-2026_Atelier_LCB-FT.pdf)** — *ACPR / Banque de France, 5 octobre 2026*
  Les supports de l'atelier détaillent le nouveau cadre européen : bascule vers le paquet AML/AMLR, collecte des établissements éligibles pour l'AMLA, et méthodologie de sanctions harmonisées (au moins 10 M€ ou 10 % du chiffre d'affaires pour les entités). L'ACPR présente aussi sa démarche SUPTECH et le contrôle de la surveillance des opérations.
  **Pourquoi c'est pertinent ?** C'est la photographie officielle du niveau de maturité attendu des dispositifs LCB-FT en 2026 : utile pour arbitrer les investissements outils/processus et anticiper le risque de sanction.
  **Impact réglementaire** : paquet AML/AMLR, RTS AMLA et lignes directrices sur le gel des avoirs — le tout applicable aux assureurs vie.

- **[Cegedim Assurances et Shift Technology fêtent 5 ans de partenariat et intègrent WTW (communiqué)](https://www.cegedim.com/Communique/CegedimAssurances_Shift_WTW_07102026.pdf)** — *Cegedim Assurances / Shift Technology, 7 octobre 2026*
  Le dispositif commun de lutte contre la fraude en assurance de personnes (IA de détection + analyse des cas suspects) revendique une quinzaine d'organismes utilisateurs, plus de 5 millions de personnes protégées et 46 M€ d'économies générées depuis 2021, dont 14 M€ sur six mois. WTW devient le deuxième courtier gestionnaire à rejoindre l'écosystème.
  **Pourquoi c'est pertinent ?** C'est un ordre de grandeur de ROI chiffré et daté pour un dispositif anti-fraude santé/prévoyance, là où la plupart des articles de tendance n'apportent aucun chiffrage.
  *À surveiller* : l'ouverture du dispositif aux courtiers gestionnaires, qui déplace la lutte anti-fraude vers toute la chaîne de gestion des prestations.

## 3. 🗂️ Exploitation de l'opendata

- **[Listes noires des sociétés et sites non autorisés : Forex, options binaires, biens divers, produits dérivés sur crypto-actifs, usurpations…](https://www.amf-france.org/fr/espace-epargnants/proteger-son-epargne/listes-noires-et-mises-en-garde)** — *AMF, mise à jour des 8 et 9 octobre 2026*
  La liste recense les acteurs non autorisés et les usurpations d'acteurs régulés, avec de nouvelles inscriptions datées du 8 octobre 2026, dont de nombreuses entrées « Usurpation » (adresses e-mail génériques `prenom.nom@…` imitant des banques et gestionnaires) et des sites crypto-actifs.
  **Pourquoi c'est pertinent ?** C'est la base de contrôle de premier niveau, gratuite et datée, à croiser avant toute souscription ou partenariat pour détecter une usurpation de marque d'assureur ou de courtier.
  *À surveiller* : l'usage systématique de cette liste dans le parcours KYC/onboarding pour détecter les faux conseillers et faux sites.

- **[L'ACPR et l'AMF mettent en garde le public contre plusieurs acteurs proposant des investissements sur le Forex et sur des produits dérivés sur crypto-actifs sans y être autorisés](https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0)** — *ACPR / AMF, 22 octobre 2026*
  Depuis le début de l'année 2026, l'AMF et l'ACPR ont ajouté 57 sites non autorisés en catégorie Forex et 36 en produits dérivés sur crypto-actifs, dont respectivement 26 et 10 au seul troisième trimestre. Les listes sont accessibles sur ABEIS (Assurance Banque Épargne Info Service) et sur le site de l'AMF.
  **Pourquoi c'est pertinent ?** Le rythme d'inscription trimestriel mesure la pression des arnaques à l'épargne — un indicateur de risque à suivre pour la conformité et la LCB-FT des réseaux d'assurance vie.
  **Impact réglementaire** : renvoi explicite aux registres REGAFI, REFASSU et ORIAS comme référentiel d'authentification.

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers en France (jeu de données)](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *data.gouv.fr (AMF), jeu de données*
  Le jeu de données reprend les listes noires de l'AMF (entités non autorisées et usurpations), avec le nom du site/e-mail frauduleux, la catégorie et la date d'inscription, exploitable en CSV. Il permet de construire un contrôle automatisé et un croisement avec les bases client avant souscription.
  **Pourquoi c'est pertinent ?** Pour l'anti-fraude et la LCB-FT, c'est la même information que la liste noire AMF mais au format opendata — directement ingérable dans un dispositif de filtrage automatisé plutôt qu'en consultation manuelle.

## 4. 🕸️ Lutte contre les bandes organisées

- **[Un système d'escroqueries impliquant des ophtalmologues et des opticiens démantelé à Paris](https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925)** — *Le Figaro, 25 septembre 2026*
  22 personnes (dont deux ophtalmologues et dix opticiens) et 15 structures sont renvoyées devant la justice pour escroquerie et blanchiment en bande organisée : remboursement indu de la prise en charge mutuelle transformé en avoir, avec détournement d'environ 12 M€ par an depuis 2023. L'enquête, confiée à l'OCLTI après le signalement de mutuelles, a donné lieu à des perquisitions entre janvier et juillet 2026.
  **Pourquoi c'est pertinent ?** Illustration directe du rôle déclencheur des signalements d'assureurs/complémentaires dans un démantèlement en bande organisée, et de la bascule vers les procédures pénales (jusqu'à dix ans d'emprisonnement).
  *À surveiller* : le procès au printemps 2027 et la généralisation soupçonnée de ce montage à l'optique sur la plaque parisienne (jusqu'à 250 M€ estimés).

- **[International investment fraud scheme dismantled: seven arrests](https://www.eurojust.europa.eu/news/international-investment-fraud-scheme-dismantled-seven-arrests)** — *Eurojust / Europol, 3 novembre 2026*
  Sept personnes ont été arrêtées et plus de 100 serveurs saisis lors d'une journée d'action internationale visant un réseau d'arnaque à l'investissement (fausses plateformes de trading), pour des pertes estimées à plus de 4 M€. Une société basée à Chypre et en Israël aurait fourni du « crime-as-a-service » (sites frauduleux, centres d'appels) à plusieurs groupes criminels.
  **Pourquoi c'est pertinent ?** Le schéma « services criminels clés en main » (sites + call centers + données) modélise l'industrialisation de la fraude que rencontrent aussi les assureurs ; les typologies et la méthode d'enquête (analyse de données, coopération multi-pays) sont réutilisables.

## 5. 🚪 Fraude en entrée en relation

- **[Fraude au faux RIB : celui qui a de bonne foi viré l'argent à un escroc est-il libéré de sa dette ?](https://www.lemonde.fr/argent/article/2026/09/24/fraude-au-faux-rib-celui-qui-a-de-bonne-foi-vire-l-argent-a-un-escroc-est-il-libere-de-sa-dette_6781340_1657007.html)** — *Le Monde, 24 septembre 2026*
  Par un arrêt du 17 juin 2026 (Cass. com., n° 24-13.306), la Cour de cassation juge que « n'est pas créancier apparent le tiers qui usurpe l'identité du créancier » : le débiteur qui a viré l'argent au fraudeur n'est pas libéré et doit payer une seconde fois. La fraude repose sur le piratage de messagerie puis l'envoi d'un faux RIB.
  **Pourquoi c'est pertinent ?** Le faux RIB et l'usurpation d'identité touchent de plein fouet la souscription et les encaissements (assurance, courtage) : la décision renforce la vigilance contractuelle et l'intérêt des garanties fraude/cyber, et rappelle qu'une vérification par canal indépendant est indispensable.

- **[Ordonnances, numéros de Sécu, mutuelle : des pirates revendiquent le vol de 436 000 dossiers de pharmacies](https://www.capital.fr/conso/ordonnances-numeros-de-secu-mutuelle-des-pirates-revendiquent-le-vol-de-436-000-dossiers-de-pharmacies-1531512)** — *Capital.fr, 1er novembre 2026*
  Trois pharmacies (Paris, Strasbourg, Dijon) ont été visées le week-end des 31 octobre et 1er novembre 2026 ; les hackers revendiquent 436 000 dossiers médicaux exposant adresses, numéros de Sécurité sociale, données d'Assurance maladie, mutuelles et complémentaires, voire ordonnances.
  **Pourquoi c'est pertinent ?** Ces combinaisons (identité + NIR + organisme complémentaire + coordonnées) constituent exactement la matière première d'une usurpation d'identité et de dossiers frauduleux à l'entrée en relation ; elles exposent aussi à des campagnes d'hameçonnage imitant assureurs et mutuelles.

## 6. 🩺 Fraude à la santé

- **[Amendement n° 1739 au PLFSS 2027 (suspension temporaire du tiers payant de l'assuré fraudeur)](https://www.assemblee-nationale.fr/dyn/17/amendements/3211/AN/1739.pdf)** — *Assemblée nationale, 16 octobre 2026*
  L'amendement relève que la fausse ordonnance présentée au comptoir ne coûte rien à son porteur, la pharmacie étant réglée directement par l'Assurance maladie : le tiers payant devient un « complice involontaire ». Il cite des fraudes d'assurés représentant, en 2025, 53 % des dossiers détectés et environ 115 M€, et propose de renvoyer à un décret une suspension temporaire du tiers payant pour l'assuré déjà sanctionné ou condamné.
  **Pourquoi c'est pertinent ?** Le tiers payant intégral est le point faible structurel de la chaîne de remboursement santé ; ce texte dessine la prochaine évolution du contrôle (ciblage de l'assuré fraudeur, et plus seulement du professionnel).
  **Impact réglementaire** : à suivre dans le parcours législatif du PLFSS 2027 (articulation avec la loi du 25 juin 2026).

- **[Surprescripteurs d'arrêts de travail : « La méthode de la Cnam est arbitraire, violente et injuste », dénonce MG France](https://www.lequotidiendumedecin.fr/liberal-soins-de-ville/surprescripteurs-darrets-de-travail-la-methode-de-la-cnam-est-arbitraire-violente-et-injuste-denonce)** — *Le Quotidien du Médecin, 2 novembre 2026*
  La nouvelle campagne de mise sous objectifs (MSO) de la Cnam cible 650 médecins généralistes considérés comme gros prescripteurs d'indemnités journalières ; MG France conteste la méthode de ciblage. L'Assurance maladie revendique de son côté une baisse effective des prescriptions de 20 à 30 % chez les médecins encadrés.
  **Pourquoi c'est pertinent ?** Le contrôle automatisé des prescripteurs (datamining sur les volumes atypiques) devient un levier central de la lutte contre la fraude aux arrêts maladie — un modèle transposable à la détection d'anomalies de facturation côté assureurs.
  *À surveiller* : l'articulation MSO avec le plafonnement de la durée de prescription prévu par la LFSS 2026.

- **[Revue de dépenses : la lutte contre la fraude aux prescriptions et aux facturations à l'assurance maladie (rapport IGF-IGAS)](https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf)** — *IGF / IGAS, publié le 29 juillet 2026*
  Le rapport chiffre la fraude détectée à 628 M€ en 2024, dont près de 70 % imputables à des professionnels de santé (ou à des personnes usurpant/falsifiant leur identité), et recommande une bascule de l'aval vers l'amont des paiements : contrôles embarqués (programme METEORe), feuille de route de l'ordonnance numérique, datamining et meilleure coordination CPAM-parquets.
  **Pourquoi c'est pertinent ?** C'est le document de fond qui structure la stratégie anti-fraude santé à venir (prévention avant paiement, science des données), utile pour aligner les KPI et le ciblage des contrôles des organismes complémentaires.

## 7. 🧪 Divers — sujet émergent

- **[Questionnaire CCSF : les fraudes et escroqueries en matière financière (consultation publique)](https://www.banque-france.fr/system/files/2026-10/CP-lancement-questionnaire-fraude_CCSF.pdf)** — *Banque de France / CCSF, 14 octobre 2026*
  Le Comité consultatif du secteur financier lance une consultation anonyme auprès des personnes victimes de fraude ou d'escroquerie financière, ouverte du 13 octobre au 30 novembre 2026, pour mieux comprendre les pratiques des fraudeurs et nourrir ses travaux.
  **Pourquoi c'est pertinent ?** La victimologie officielle est une source rare : elle alimentera les priorités de prévention (souscription, épargne, manipulation) et les obligations d'information des assureurs.

- **[Cyberattaque : la série continue dans l'assurance](https://www.lassuranceenmouvement.com/2026/10/19/cyberattaque-la-serie-continue-dans-lassurance/)** — *L'Assurance en mouvement, 19 octobre 2026*
  Le 17 octobre 2026, un pirate a mis en ligne 16 556 documents de gestion santé liés à des assurés de Malakoff Humanis (prise en charge hospitalière, remboursements, optique, dentaire, pharmacie, NIR, adresses, plus de 800 IBAN), dans une série d'attaques visant les assureurs santé depuis la fin de l'été.
  **Pourquoi c'est pertinent ?** La répétition des combinaisons « identité + NIR + IBAN + prestations » montre que les assureurs santé concentrent exactement les données qui rendent une fraude crédible, et fait de la cybersécurité un prérequis de la lutte anti-fraude. **Impact réglementaire** : notification CNIL et enjeux RGPD.

## Synthèse — 5 signaux faibles à surveiller

1. **La preuve numérique se normalise (image, ordonnance, pièce justificative).** Des travaux AFNOR sur le contenu probatoire et la montée de l'ordonnance numérique déplacent la lutte de la détection du faux vers la certification d'un processus de capture/archivage. → [L'Argus de l'assurance, 02/10/2026](https://www.argusdelassurance.com/tech/intelligence-artificielle/intelligence-artificielle-reconstruire-la-confiance-a-lere-des-deepfakes.2MRT6YZL6JA65LGG2F2C4RDILE.html) ; [IGF-IGAS](https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf)

2. **La fuite de données de santé, nouvelle porte d'entrée de la fraude.** Les vols massifs de dossiers (Malakoff Humanis, pharmacies, tiers payant) livrent identité + NIR + IBAN + données de prestations, combinables pour des faux profils et des dossiers frauduleux. → [Capital.fr, 01/11/2026](https://www.capital.fr/conso/ordonnances-numeros-de-secu-mutuelle-des-pirates-revendiquent-le-vol-de-436-000-dossiers-de-pharmacies-1531512) ; [L'Assurance en mouvement, 19/10/2026](https://www.lassuranceenmouvement.com/2026/10/19/cyberattaque-la-serie-continue-dans-lassurance/)

3. **Les listes noires ouvertes deviennent un contrôle de premier niveau avant souscription.** Le rythme d'inscription (57 sites Forex, 36 crypto depuis janvier) et la mise à disposition en opendata invitent à automatiser ce filtrage en amont du KYC. → [AMF, 08-09/10/2026](https://www.amf-france.org/fr/espace-epargnants/proteger-son-epargne/listes-noires-et-mises-en-garde) ; [ACPR-AMF, 22/10/2026](https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0) ; [data.gouv.fr](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)

4. **La pression s'accentue sur les prescripteurs d'arrêts de travail.** Le ciblage automatisé des volumes atypiques (MSO) et les projets de suspension du tiers payant pour l'assuré fraudeur redessinent le contrôle des indemnités journalières. → [Le Quotidien du Médecin, 02/11/2026](https://www.lequotidiendumedecin.fr/liberal-soins-de-ville/surprescripteurs-darrets-de-travail-la-methode-de-la-cnam-est-arbitraire-violente-et-injuste-denonce) ; [Assemblée nationale, 16/10/2026](https://www.assemblee-nationale.fr/dyn/17/amendements/3211/AN/1739.pdf)

5. **La fraude documentaire générée par IA devient un standard industriel.** Documents synthétiques et fausses preuves visuelles se banalisent (jusqu'à ×90 de documents générés par IA chez un éditeur de contrôle), poussant à la traçabilité et non plus seulement au contrôle visuel. → [Journal du Net, 03/11/2026](https://www.journaldunet.com/fintech/1557315-avec-l-ia-la-fraude-documentaire-s-industrialise-les-assureurs-sont-ils-prets/) ; [franceinfo, 04/07/2026](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)


---

# FICHIER : bras-6

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : Le mois d'octobre 2026 confirme une montée en puissance de la fraude documentaire dopée à l'IA générative, désormais détection records chez les assureurs comme à l'Assurance maladie. Ce qui monte : la migration de la fraude vers l'amont (entrée en relation, souscription, usurpation d'identité), la professionnalisation des réseaux (centres de santé, courtage, accidents mis en scène) et l'outillage public de la riposte — listes noires ACPR/AMF en opendata, chantier LCB-FT et supervision de l'IA par l'ACPR, décisions de justice publiées qui redessinent la charge de la preuve. Les signaux faibles du mois viennent des autorités (ACPR, AMF, Cour de cassation) autant que des tribunaux : le document n'est plus une preuve, et le paiement fait à un usurpateur ne libère plus l'assureur.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : L'intelligence artificielle générative industrialise la fabrication de faux dégâts sur photo. Les assureurs ripostent en imposant la prise de vue en direct, géolocalisée et horodatée, et la fraude migre vers la souscription.
- **📈 Efficacité de gestion de la fraude** : La fraude détectée atteint un record historique, signe de détections plus efficaces autant que d'une fraude en hausse. L'autorité de contrôle fait de la supervision de l'IA et du dispositif anti-blanchiment ses priorités pour les assureurs.
- **🗂️ Exploitation de l'opendata** : Les listes noires des acteurs non autorisés, publiées par les autorités financières et ouvertes sur le portail des données publiques, permettent de vérifier automatiquement courtiers et sites douteux. Les inscriptions s'accelèrent trimestre après trimestre.
- **🕸️ Lutte contre les bandes organisées** : Courtiers montés en schéma de Ponzi, centres de santé fictifs, accidents mis en scène : les réseaux tombent grâce à la coopération entre parquet, Tracfin et assureurs. Ce modèle de coopération existe aussi à l'étranger.
- **🚪 Fraude en entrée en relation** : L'usurpation d'identité coûte désormais très cher aux organismes : payer un usurpateur ne libère pas de la dette envers le vrai titulaire. L'interdiction du démarchage téléphonique en assurance redéfinit les canaux d'entrée en relation.
- **🩺 Fraude à la santé** : Les faux arrêts de travail restent le premier gisement de fraude des assurés, tandis que le juge exige désormais une volonté de dissimulation caractérisée pour la qualifier. Un vaste réseau d'optique sera jugé l'an prochain à Paris.
- **🧪 Divers** : Après les intempéries, les démarchages frauduleux aux réparations se multiplient et les mairies alertent les sinistrés. À l'étranger, des assureurs mènent des enquêtes infiltrées conjointes avec le régulateur contre les faux dégâts de tempête.

## 1. 🔍 Anti-fraude documentaire

- **[Assurances : quand l'IA simule des accidents](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)** — *franceinfo (France 2), 4 juillet 2026*
  Reportage de référence sur la fraude à l'assurance auto à l'IA générative : des photos de dégâts ajoutées en quelques clics sur un véhicule intact. Direct Assurance déclare détecter jusqu'à 16 millions d'euros de demandes frauduleuses par an et avoir **multiplié par 3,5 le nombre de faux documents reçus** (« On a multiplié par 3,5… », Loïc Kueny, directeur marketing). Riposte déployée : applications de déclaration imposant la prise de vue en direct, avec géolocalisation, horodatage et analyse immédiate (WeProov).
  **Pourquoi c'est pertinent ?** Pour un SIU ou un gestionnaire de sinistres, c'est la photographie à jour du couple attaque/détection sur la preuve visuelle : la valeur probante de la photo « importée de la galerie » est morte, et l'assurance auto est la branche la plus exposée (627 M€ en IARD chez ALFA).
  **À surveiller** : la généralisation des prises de vue « in situ » (photo forcée, capteurs, visio-expertise) comme nouveau standard d'entrée en dossier — et les recours contre les faux positifs côté assurés.
  Impact réglementaire : escroquerie à l'assurance = 5 ans d'emprisonnement et 375 000 € d'amende ; déchéance de garantie contractuelle possible.
  🔗 https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html

- **[Assurance auto : l'IA et les fraudeurs font exploser jusqu'à 10 % votre prime — Leocare, 50 % des tentatives de fraude à la souscription](https://www.autoplus.fr/actualite/assurance-auto-lia-et-les-fraudeurs-fait-exploser-jusqua-10-votre-prime-1430056.html)** — *Auto Plus, 11 mars 2026*
  Depuis 2025, l'assureur français Leocare observe que **environ 50 % des tentatives de fraude concernent un maquillage physique ou numérique du véhicule au moment de la souscription** : rayures et impacts effacés par IA sur les photos d'ouverture de contrat, puis déclarés quelques semaines plus tard comme nouveaux sinistres ; jusqu'à photographier un véhicule similaire avec la plaque du souscripteur. Coût moyen d'un sinistre frauduleux : environ 2 500 € en carrosserie hors réseau agréé, 1 000 € en bris de glace.
  **Pourquoi c'est pertinent ?** Le fraude documentaire ne vise plus seulement l'indemnisation : il contamine l'entrée en risque. Pour la souscription et le scoring d'entrée, l'analyse d'image (incohérences de lumière, métadonnées, correspondance plaque/véhicule) devient un contrôle de tarification, pas seulement de sinistre.
  **À surveiller** : la détection des incohérences « niveau de vrai » (vrai véhicule, faux état) plutôt que du faux parfait — typologie transposable aux photos de domicile en MRH et aux factures de santé.
  🔗 https://www.autoplus.fr/actualite/assurance-auto-lia-et-les-fraudeurs-fait-exploser-jusqua-10-votre-prime-1430056.html

## 2. 📈 Efficacité de gestion de la fraude

- **[Rapport annuel d'activité ALFA : 946,3 millions d'euros de fraude identifiée en 2025](https://www.alfa.asso.fr/fraude-a-lassurance/)** — *ALFA (Agence de lutte contre la fraude à l'assurance), rapport publié le 9 juillet 2026*
  La référence annuelle de Place, reprise par Les Échos puis Le Figaro et L'Opinion (une seule entrée ici) : **946,3 M€ de fraudes et tentatives identifiées en 2025 (+ 4,9 %), taux de fraude 1,27 %**. IARD 626,6 M€ (− 0,6 %) ; santé + 11,8 % (optique = 53 % des 112 M€) ; prévoyance + 25,8 % (182 M€) ; vie + 101,7 % (24,8 M€, usurpations d'identité et faux RIB en tête). La fraude réelle est estimée à 2,5 Md€ : le montant détecté mesure autant l'efficacité des mécanismes de détection que le phénomène.
  **Pourquoi c'est pertinent ?** C'est le KPI de référence pour le reporting d'un dispositif antifraude (économies réalisées + montants payés à tort) et la preuve chiffrée du retournement : la hausse des montants détectés est aussi un indicateur de maturité, à présenter en comité.
  **À surveiller** : la bascule de l'effort des adhérents vers l'assurance de personnes (santé + prévoyance + vie = 319 M€) — là où beaucoup de dispositifs restent en sous-investissement IARD.
  🔗 https://www.alfa.asso.fr/fraude-a-lassurance/

- **[La fraude à l'assurance augmentée par l'IA — « chercher le faux est une course perdue ; il faut authentifier le vrai à la source »](https://algopolis.eu/fr/article/19)** — *AlgoPolis (programme de recherche IA & assurance), 23 octobre 2026*
  Note de recherche qui quantifie le changement d'économie du faux : cas de fraude assistée par IA **×4 entre 2022 et 2025 (≈ 20 000 → 80 000)**, + 71 % de fraude constatée par l'assureur Admiral en 2025, **+ 300 % de photos d'accident retouchées en un an** chez un assureur britannique (données primaires : étude UVeye, arXiv 2510.19957, octobre 2025). Thèse centrale : les règles de détection (signaux d'incohérence) sont obsolètes face à un faux sans défaut ; il faut reporter l'effort sur la provenance — signature cryptographique des images, marquage lisible par machine, données de terrain indépendantes (imagerie satellitaire, objets connectés).
  **Pourquoi c'est pertinent ?** Pour le pilote de dispositif, c'est un changement de paradigme de contrôle : du « détection du faux » (coût marginal croissant, faux positifs) vers « l'authentification du vrai » (chaîne de custody de la preuve dès la capture).
  **À surveiller** : les standards de provenance (marquage des contenus, horodatage à la source) — l'AI Act article 50 en fixe déjà le calendrier européen. Impact réglementaire : AI Act (marquage lisible par machine des contenus générés, applicable depuis le 2 août 2026).
  🔗 https://algopolis.eu/fr/article/19

- **[L'ACPR présente son programme de travail 2026 : LCB-FT au plus près des risques, supervision de l'IA, DORA](https://acpr.banque-france.fr/fr/communiques-de-presse/lautorite-de-controle-prudentiel-et-de-resolution-presente-son-programme-de-travail-pour-lannee-2026)** — *ACPR, communiqué du 19 janvier 2026*
  Cinq axes dont trois concernent directement la maturité antifraude et LCB-FT des assureurs : contrôles LCB-FT ciblés sur les organismes les plus exposés au blanchiment (participation à la Recommandation 16 du GAFI sur la transparence des paiements, mise en œuvre opérationnelle de l'AMLA) ; **préparation de la supervision de l'IA — l'ACPR devrait être désignée autorité de surveillance du marché pour la banque et l'assurance** ; montée en puissance des contrôles DORA (gestion des incidents, cadres de risque TIC, conformité des contrats de sous-traitance) et usage interne de l'IA générative dans les outils de contrôle.
  **Pourquoi c'est pertinent ?** Le référentiel d'audit du dispositif (scoring de fraude, refus automatisés) entre dans le champ d'une autorité de contrôle : un SIU qui documente ses modèles d'IA et ses chaînes LCB-FT prépare ses inspections 2026-2027.
  Impact réglementaire : LCB-FT (art. R. 561-1 et suivants CMF), AI Act (gouvernance des systèmes à haut risque : tarification, refus, scoring sinistre), DORA.
  🔗 https://acpr.banque-france.fr/fr/communiques-de-presse/lautorite-de-controle-prudentiel-et-de-resolution-presente-son-programme-de-travail-pour-lannee-2026

## 3. 🗂️ Exploitation de l'opendata

- **[L'ACPR et l'AMF publient leurs listes noires de sites Forex et crypto-actifs : 57 + 36 entrées depuis début 2026](https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0)** — *ACPR / AMF, communiqué du 22 octobre 2026*
  Communiqué conjoint trimestriel : depuis le début de 2026, **57 sites non autorisés ajoutés en catégorie Forex et 36 en produits dérivés sur crypto-actifs (dont 26 et 10 au troisième trimestre)**. Le texte renvoie aux objets exploitables côté assurance/finance : liste noire ABEIS (Prévention arnaques), liste noire AMF, vérification de l'enregistrement d'un interlocuteur via **REGAFI** ( PSI ), **ORIAS** (CIF et intermédiaires d'assurance) et listes blanches AMF.
  **Pourquoi c'est pertinent ?** C'est le croisement « listes noires + registre ORIAS » automatisable qui permet de détecter un faux courtier démarchant au nom d'un assureur — le cœur du contrôle d'entrée en relation, à brancher sur la file réclamations/souscription.
  🔗 https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0

- **[Jeu de données « Listes noires des entités non autorisées à proposer des produits ou services financiers en France » (AMF, publication ouverte)](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *data.gouv.fr (producteur : AMF), mise à jour continue — entrées publiées les 8 et 22 octobre 2026*
  Seule entrée « page de jeu de données » de l'édition (thème opendata), pour ce qu'elle permet de faire : le CSV (licence ouverte 2.0, format Excel) agrège sites, adresses mail et acteurs mis en garde par l'AMF, y compris les **usurpations d'identité d'acteurs régulés** (plusieurs entrées « Usurpation » publiées le 8 octobre 2026 : armen.ltd, wexfordadvisory-ltd.com, paris-majeste.com et des homonymes de sociétés de gestion). Réutilisations déjà en ligne : outil de recherche des sites cryptos sur liste noire, site « AMF Protect Epargne ».
  **Pourquoi c'est pertinent ?** Chargée dans un SI antifraude, cette base alimente un contrôle automatique à trois points — domaine du prospecteur, entité citée, adresse expéditrice — sur la souscription à distance et les demandes de rachat en vie.
  **À surveiller** : la fréquence de mise à jour annoncée non respectée (avertissement qualité data.gouv) : prévoir un raisonnement « liste fraîche de moins de 30 jours » côté règle métier.
  🔗 https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france

## 4. 🕸️ Lutte contre les bandes organisées

- **[Courtage d'assurances : entre abus de biens sociaux et escroqueries, un procès à 2,5 millions d'euros de préjudices à Poitiers](https://www.lanouvellerepublique.fr/poitiers/courtage-d-assurances-entre-abus-de-biens-sociaux-et-escroqueries-un-proces-a-2-5-millions-d-euros-de-prejudices-a-poitiers-1793651487)** — *La Nouvelle République (Centre Presse), 2 novembre 2026 (audience du 17 septembre 2026)*
  Trois anciens associés d'une société de **courtage d'assurances** de la Vienne (ABD Solutions, Savigné) ont comparu pour escroquerie en bande organisée et abus de biens sociaux : sous une façade de courtage, la holding vendait des « prêts participatifs » à 7 % de rendement promis — un schéma de Ponzi où les nouveaux prêts couvraient les anciens, jusqu'à la banqueroute (préjudice estimé 2,5 M€). L'enquête est partie d'un **signalement de Tracfin** au procureur de la République de Poitiers.
  **Pourquoi c'est pertinent ?** Le canal courtage est un angle mort classique : l'escroc a une façade assurantielle agréée, un registre propre et des clients « réels » — la détection vient du signal Tracfin, pas du contrôle interne des assureurs partenaires.
  **À surveiller** : la remontée des signalements Tracfin côté assureur (obligation de déclaration de soupçon, art. L. 561-13 CMF) et la revue périodique des intermédiaires liés aux sinistres comme aux collectes.
  🔗 https://www.lanouvellerepublique.fr/poitiers/courtage-d-assurances-entre-abus-de-biens-sociaux-et-escroqueries-un-proces-a-2-5-millions-d-euros-de-prejudices-a-poitiers-1793651487

- **[Gouverneur Hochul : 16 arrestations dans la répression de la fraude à l'assurance auto — task force police d'État + régulateur financier](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20261020)** — *New York State Department of Financial Services (DFS), communiqué du 20 octobre 2026*
  Communiqué officiel : la **task force conjointe de la New York State Police et du Department of Financial Services** (enquêtes de fraude assurantielle assermentés) a fait tomber 16 personnes — 31 chefs d'accusation dont 29 felonies — pour accidents volontairement mis en scène et blessures fictives (≈ 500 000 $ de sinistres tentés : 70 700 $ de soins fictifs dans le Bronx, 16 000 $ à Brooklyn contredits par la vidéo, 18 000 $ en no-fault pour un faux choc contre un camion Amazon dans le Queens). C'est la première application des réformes Hochul de 2026 : poursuite possible des **organisateurs** de rings (pas seulement des conducteurs) et définition durcie de la « blessure grave » ; l'État chiffre l'impact des accidents organisés jusqu'à 300 $/an de prime par conducteur. (Reprise : Insurance Journal, 21 octobre 2026 ; governor.ny.gov, même date.)
  **Pourquoi c'est pertinent ?** Le pendant institutionnel de l'affaire optique française : un régulateur financier doté d'un bureau d'enquêtes sur la fraude qui travaille en unité mixte avec la police judiciaire — modèle « police/assureurs/régulateur » que la place de France discute à bas bruit. (Source étrangère assumée : pas d'équivalent français en octobre 2026 sur la coopération régulateur-police.)
  🔗 https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20261020

- **[58 millions de fraude à l'Assurance maladie : « une escroquerie exceptionnelle par son ampleur » démantelée (18 centres de santé)](https://www.egora.fr/actus-pro/politiques/58-millions-de-fraude-lassurance-maladie-une-escroquerie-exceptionnelle-par)** — *egora, 27 mars 2026 (communiqué du parquet de Paris du 26 mars 2026)*
  Sept mises en examen, dont détention provisoire, pour avoir facturé massivement des **actes fictifs dans 18 centres de santé** repris fin 2024 : prête-noms, « flotte de téléphones dédiés » pour l'ouverture de comptes, **changements de RIB et manipulation des logiciels de facturation**, actes au nom d'un dentiste décédé en 2021, patients à la complémentaire santé solidaire dont les données étaient usurpées (probablement issues de vols de données revendus). La JIRS de Paris a ouvert l'enquête en septembre 2025, information judiciaire le 23 décembre 2025 ; 16 M€ de remboursements bloqués en amont, 300 000 € saisis ; « task-force nationale » de l'Assurance maladie.
  **Pourquoi c'est pertinent ?** La typologie complète (reprise express de centres, atypie des remboursements, dispersion multi-caisses pour retarder la détection) est le mode d'emploi d'une fraude en réseau industrielle : chaque maillon — RIB, logiciel de facturation, prête-nom — est un point de contrôle détectable.
  **À surveiller** : la corrélation entre date de changement d'exploitant d'un centre et courbe de remboursements — règle transposable aux prestataires de services sur sinistres (carrossiers, experts, transporteurs).
  🔗 https://www.egora.fr/actus-pro/politiques/58-millions-de-fraude-lassurance-maladie-une-escroquerie-exceptionnelle-par

## 5. 🚪 Fraude en entrée en relation

- **[« N'est pas créancier apparent le tiers qui usurpe l'identité du créancier » : Com., 17 juin 2026, n° 24-13.306, publié au Bulletin](https://www.courdecassation.fr/publications/lettre-de-la-chambre-commerciale-financiere-et-economique/ndeg20-octobre-2026/creancier-apparent)** — *Cour de cassation (lettre de la chambre commerciale n° 20), octobre 2026*
  Décision de principe rendue en **formation plénière de la chambre commerciale**, publiée au Bulletin et au Rapport : le paiement effectué de bonne foi sur un **IBAN frauduleusement substitué** (adresse électronique piratée) après une usurpation d'identité n'est **pas libératoire** — le débiteur reste tenu envers le créancier réel. La doctrine de la chambre détaille le raisonnement (question nouvelle, art. 1342-3 du code civil).
  **Pourquoi c'est pertinent ?** Transposé à l'assureur payeur (indemnité de sinistre, rachat vie, prestation prévoyance) : payer un usurpateur n'éteint pas la dette envers l'assuré authentique — la « bonne foi » ne protège plus. C'est l'argument juridique qui justifie les procédures lourdes de vérification des changements de coordonnées bancaires avant tout paiement.
  Impact réglementaire : code civil art. 1342-3 ; chaîne d'effets sur la lutte contre la fraude à l'IBAN (faux RIB, première technique de la fraude vie selon ALFA).
  🔗 https://www.courdecassation.fr/decision/6a323623cdc6046d47934577 (texte de l'arrêt)

- **[Banque de France et ACPR : alerte au deepfake — usurpation de l'identité du gouverneur et de dirigeants](https://acpr.banque-france.fr/fr/communiques-de-presse/la-banque-de-france-et-lacpr-mettent-en-garde-le-public-contre-un-risque-de-fraude-avec-usurpation)** — *Banque de France / ACPR, 27 avril 2026*
  Les deux institutions alertent sur des arnaques utilisant des **deepfakes vidéo imitant le gouverneur François Villeroy de Galhau et la secrétaire générale de l'ACPR Emmanuelle Assouan** sur les réseaux sociaux, pour diriger vers des sites frauduleux (fausses promesses de virement avec « frais » à avancer). Message de doctrine : « jamais un dirigeant de la Banque de France ou de l'ACPR ne recommandera un site ou un produit financier », et surveillance active en lien avec les plateformes.
  **Pourquoi c'est pertinent ?** Si les plus hautes autorités financières sont imitables à façon, tout visage de campagne ou de conseiller « vérifiable » d'un assureur l'est aussi : les kits de prévention client et la vérification des publicités sponsorisées (usurpation de marque) deviennent un chantier d'entrée en relation.
  **À surveiller** : la demande aux plateformes d'alerter/retirer les deepfakes de marque — même mécanique que pour les faux sites d'assureurs des listes noires (axe 3).
  🔗 https://acpr.banque-france.fr/fr/communiques-de-presse/la-banque-de-france-et-lacpr-mettent-en-garde-le-public-contre-un-risque-de-fraude-avec-usurpation

- **[Démarchage téléphonique en assurance : ce que change l'interdiction entrée en vigueur le 11 août 2026](https://www.abe-infoservice.fr/fr/assurance/se-preparer-sassurer/interdiction-du-demarchage-telephonique-en-assurance-depuis-le-11-aout-2026-que-change-cette)** — *ABE Info Service (ACPR / Banque de France / AMF), août 2026*
  Fiche officielle du service public d'information assurance-banque-épargne : depuis le **11 août 2026** (art. 13 de la loi n° 2025-594 du 30 juin 2025), un assureur ou intermédiaire ne peut appeler pour proposer une souscription **sans consentement préalable, clair, univoque et limité à un an** — sauf exécution d'un contrat en cours en lien avec son objet. Les recours du consommateur : SignalConso et saisine de l'ACPR ; fin de Bloctel.
  **Pourquoi c'est pertinent ?** C'est un nouveau marqueur de suspicion gratuit : tout appel de prospection assurance sans consentement horodaté est illicite — un « courtier » qui appelle ainsi, ou un contrat né d'un tel appel, entre dans une zone de souscription frauduleuse. Impact réglementaire : code de la consommation (démarchage), obligations de preuve du consentement conservées 3 ans (DGCCRF).
  🔗 https://www.abe-infoservice.fr/fr/assurance/se-preparer-sassurer/interdiction-du-demarchage-telephonique-en-assurance-depuis-le-11-aout-2026-que-change-cette

## 6. 🩺 Fraude à la santé

- **[Bilan de la lutte contre les fraudes 2025 de l'Assurance maladie : 723 M€ détectés et stoppés, + 15 %](https://www.aefinfo.fr/depeche/749282-lassurance-maladie-detecte-723-m-de-fraudes-en-2025-un-montant-en-hausse-de-15-en-un-an)** — *AEF info (Protection sociale), 16 avril 2026 (dossier de presse de l'Assurance maladie)*
  Conférence de presse du 16 avril 2026 : **723 M€ stoppés en 2025 (+ 15 %, objectif de 550 M€ dépassé, montant triplé depuis 2021, 1 700 agents dédiés)**. Structure révélatrice : les assurés = 53 % des dossiers mais 16 % des montants (arrêts de travail ≈ 49 M€, fraudes aux droits 28 M€ ; 9 700 dossiers de faux arrêts, 25 M€ de pénalités) ; les professionnels de santé et faux « professionnels » concentrent près des **trois quarts des montants** (centres de santé 138 M€, audioprothésistes 86 M€, transporteurs sanitaires 62 M€). L'organisme s'appuie sur le projet de loi contre les fraudes sociales et fiscales.
  **Pourquoi c'est pertinent ?** Pour les complémentaires et les assureurs santé/prévoyance, c'est la cartographie publique du risque : où frappe la fraude de masse (arrêts, droits) versus la fraude en montants (centres, prestations) — et le calibrage attendable de tout dispositif de contrôle de soins.
  🔗 https://www.aefinfo.fr/depeche/749282-lassurance-maladie-detecte-723-m-de-fraudes-en-2025-un-montant-en-hausse-de-15-en-un-an

- **[Cass. 2e civ., 15 octobre 2026, n° 24-15.050 (Bulletin) : la fraude suppose une « volonté de dissimulation »](https://www.courdecassation.fr/decision/6ad099897a102021375f481d)** — *Cour de cassation, 15 octobre 2026*
  Arrêt publié au Bulletin et aux Lettres de chambre : au sens de l'article L. 256-4 du code de la sécurité sociale, l'existence d'une **manœuvre frauduleuse « doit s'entendre d'une volonté de dissimulation en vue d'obtenir les prestations indues »** ; le seul exercice, sans autorisation médicale, d'une activité rémunérée pendant un arrêt de travail ne caractérise pas la manœuvre — et ne ferme donc pas, à lui seul, la porte de la remise gracieuse de l'indu d'indemnités journalières.
  **Pourquoi c'est pertinent ?** C'est la règle d'or de tout contentieux de l'indu et des pénalités : la charge probatoire du caractère intentionnel pèse sur l'organisme. Un SIU qui construit des dossiers « fausse déclaration » (santé, prévoyance, IARD) doit outiller la preuve de l'intention — pas seulement celle du fait.
  Impact réglementaire : code de la sécurité sociale art. L. 256-4 ; effet miroir sur les clauses contractuelles de déchéance pour fausses déclaration/circunstances volontairement fausses.
  🔗 https://www.courdecassation.fr/decision/6ad099897a102021375f481d

- **[Optique : un système d'escroqueries impliquant ophtalmologues et opticiens démantelé à Paris — 22 prévenus jugés en 2027](https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925)** — *Le Figaro, 25 septembre 2026 (communiqué du parquet de Paris)*
  La procureure de Paris Laure Beccuau et la gendarmerie (OCLTI) annoncent le renvoi devant le tribunal de **22 personnes dont deux ophtalmologues et dix opticiens**, pour escroquerie et blanchiment en bande organisée : ordonnances fictives délivrées parfois sans examen du patient, remboursements maximisés par les mutuelles puis restitués en « avoir » produits d'optique (montures de luxe, solaires), produits inutiles dissimulés dans les stocks. Préjudice **≈ 12 M€ par an depuis 2023** — et la piste d'un système « généralisé » chiffrée à **250 M€ sur la plaque parisienne** depuis 2023. L'enquête est née du signalement de mutuelles de santé ; 1,3 M€ de matériel saisis, audiences mai-juin 2027.
  **Pourquoi c'est pertinent ?** L'optique est le premier poste de fraude santé des complémentaires (53 % des 112 M€ du rapport ALFA) : le triptyque « prescripteur complice + opticien + assuré » est la typologie à surveiller dans les flux de remboursement, avec le signalement entre pairs comme point de départ de la détection.
  Impact réglementaire : transmission du dossier aux administrations — redressements fiscaux, **déconventionnement des médecins par l'Assurance maladie**, sanctions ordinales ; 10 ans d'emprisonnement encourus.
  🔗 https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925

## 7. 🧪 Divers — sujet émergent

- **[Villetelle (Hérault) : après les intempéries, la mairie alerte sur les risques d'arnaques aux réparations](https://www.lefigaro.fr/echos-des-territoires/herault/150512-herault-2026-10-21/)** — *Le Figaro — Échos des territoires, 21 octobre 2026*
  Alerte municipale après les intempéries d'octobre dans l'Hérault : des intervenants profitent des dégâts pour proposer des réparations coûteuses, mettre la pression pour un engagement immédiat ou **se prévaloir indûment d'un lien avec les services municipaux**. Consignes officielles aux sinistrés : document écrit détaillé, devis comparés, **photos des dommages avant toute intervention**, appel à l'assureur avant de commander les travaux.
  **Pourquoi c'est pertinent ?** La fraude opportuniste post-aléa climatique est un phénomène émergent à la jonction de l'entrée en relation (faux agents), du documentaire (faux devis) et du sinistre (sur-facturation) : chaque événement cat'nat' ouvre une fenêtre d'arnaques que l'assureur peut préempter par la communication.
  **À surveiller** : les campagnes de démarchage et de faux constats « post-grêle / post-tempête » — un pic d'occurrences est attendu à chaque épisode méditerranéen.
  🔗 https://www.lefigaro.fr/echos-des-territoires/herault/150512-herault-2026-10-21/

- **[Sting operation : un assureur agricole et le régulateur nord-carolinien démantèlent la fraude aux faux dégâts de tempête](https://www.kxan.com/business/press-releases/cision/20261026CL80221/n-c-farm-bureau-and-nciua-partner-with-department-of-insurance-in-undercover-sting-operation-that-leads-to-insurance-fraud-arrest)** — *NCFB / NCIUA via PR Newswire (relayé KXAN), 26 octobre 2026*
  North Carolina Farm Bureau et le pool tempête de l'État (NCIUA) ont participé à une **enquête infiltrée avec la division criminelle du Department of Insurance** : une « bait house » (maison-appât) piégée un couvreur qui a délibérément tordu 20 bardeaux d'un toit en bon état, puis déclaré aux assureurs une tempête inexistante — trois chefs de felony, dont fraude à l'assurance. Les deux assureurs publient la méthode et les conseils aux propriétaires (se défier des inspections gratuites après orage, exiger des photos horodatées, appeler l'agent avant de signer).
  **Pourquoi c'est pertinent ?** Technique de contre-enquête nouvelle pour le climat : les assureurs deviennent parties prenantes d'une opération judiciaire sous couverture — ce que la France ne pratique pas encore ; le réflexe « maison-appât » et le signalement intégré du régulateur sont transposables aux réseaux de carrossiers et de couvreurs. (Source étrangère assumée : pas d'équivalent français en octobre 2026 sur le sting climatique.)
  🔗 https://www.kxan.com/business/press-releases/cision/20261026CL80221/n-c-farm-bureau-and-nciua-partner-with-department-of-insurance-in-undercover-sting-operation-that-leads-to-insurance-fraud-arrest

## Synthèse — 5 signaux faibles à surveiller

1. **Le marquage lisible par machine des contenus générés (AI Act art. 50, applicable depuis le 2 août 2026 ; tolérance jusqu'au 2 décembre 2026 pour les systèmes mis sur le marché avant août) devient le futur standard de la preuve en sinistre** — si l'image « vraie » est signée à la capture et le faux watermarké par défaut, le dossier non signé devient l'anomalie. Sources : https://algopolis.eu/fr/article/19 ; https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html
2. **La fraude documentaire migre du sinistre vers la souscription** : 50 % des tentatives chez Leocare portent sur le maquillage numérique à l'entrée en risque, et la fraude vie (usurpation + faux RIB) a doublé en 2025 (+ 101,7 %) — le contrôle documentaire doit remonter en amont du contrat. Sources : https://www.autoplus.fr/actualite/assurance-auto-lia-et-les-fraudeurs-fait-exploser-jusqua-10-votre-prime-1430056.html ; https://www.alfa.asso.fr/fraude-a-lassurance/
3. **« Acheter, changer les RIB, facturer vite » : la fraude aux centres de santé est passée en mode crime organisé** (prête-noms, flotte de téléphones, logiciels de facturation manipulés, 138 M€ stoppés sur les centres en 2025) — la date de changement d'exploitant est la variable déclenchante. Sources : https://www.egora.fr/actus-pro/politiques/58-millions-de-fraude-lassurance-maladie-une-escroquerie-exceptionnelle-par ; https://www.aefinfo.fr/depeche/749282-lassurance-maladie-detecte-723-m-de-fraudes-en-2025-un-montant-en-hausse-de-15-en-un-an
4. **Payer à l'usurpateur ne libère plus de rien** : l'arrêt de principe Com. 17 juin 2026 (n° 24-13.306) transfère le risque de l'usurpation d'identité sur l'organisme payeur — la vérification du changement de coordonnées bancaires passe du bon réflexe à l'exigence de solvabilité, dans un contexte d'imitation des autorités elles-mêmes (deepfake Banque de France/ACPR). Sources : https://www.courdecassation.fr/publications/lettre-de-la-chambre-commerciale-financiere-et-economique/ndeg20-octobre-2026/creancier-apparent ; https://acpr.banque-france.fr/fr/communiques-de-presse/la-banque-de-france-et-lacpr-mettent-en-garde-le-public-contre-un-risque-de-fraude-avec-usurpation ; https://www.abe-infoservice.fr/fr/assurance/se-preparer-sassurer/interdiction-du-demarchage-telephonique-en-assurance-depuis-le-11-aout-2026-que-change-cette
5. **Le contentieux de la fraude se dote d'un référentiel probatoire** : l'exigence de « volonté de dissimulation » (Cass. 2e civ., 15 octobre 2026) comme la traçabilité des signalements (Tracfin → parquet à Poitiers, mutuelles → OCLTI dans l'optique) imposent d'instruire l'intention et de dater les signaux de départ dans chaque dossier SIU. Sources : https://www.courdecassation.fr/decision/6ad099897a102021375f481d ; https://www.lanouvellerepublique.fr/poitiers/courtage-d-assurances-entre-abus-de-biens-sociaux-et-escroqueries-un-proces-a-2-5-millions-d-euros-de-prejudices-a-poitiers-1793651487 ; https://www.lefigaro.fr/flash-actu/un-systeme-d-escroqueries-impliquant-des-ophtalmologues-et-des-opticiens-demantele-a-paris-20260925

## Méthode et sources

- **Fenêtre** : mois de référence octobre 2026 (édition du 3 novembre 2026). Neuf entrées datées d'octobre-début novembre 2026, deux de septembre-août 2026, sept références indispensables antérieures (rapport ALFA de juillet 2026, reportage franceinfo de juillet 2026, décisions de justice et communiqués d'autorité d'avril à janvier 2026) — toutes postérieures à juillet 2025 et re-datées sur la page source (piège JJ/MM vs MM/JJ vérifié : franceinfo 04/07/2026, egora 27/03/2026, AEF info 16/04/2026, NR 02/11/2026).
- **France d'abord** : 16 sources françaises ou francophones d'autorité, 2 sources étrangères assumées (task force New York ; opération infiltrée en Caroline du Nord) car sans équivalent français en octobre 2026 sur la coopération régulateur-police et le « sting » climatique.
- **Doublons écartés** : reprise de l'histoire franceinfo par autoplus.fr (9 juillet), Auto Journal et planet.fr (même événement, entrée unique) ; le rapport ALFA repris par Les Échos, Le Figaro, L'Opinion, La Tribune et les comparateurs (une entrée, source primaire alfa.asso.fr) ; analyses de cabinets d'avocats sur les faux RIB et faux arrêts maladie (kohenavocats, tigori, cqfd — remplacées par le texte de la décision Cour de cassation et la fiche ABEIS officielle) ; pages éditeurs (Yousign/Ipsos via JDN, Roots Automation via blogs fournisseurs) écartées par principe. L'article Le Progrès du 18 mars sur Leocare (404 au sondage automatisé comme en syndication Groupe NR) a été remplacé à données identiques par l'enquête Auto Plus du 11 mars 2026 (même source Leocare, Christophe Dandois cité).
- **Sites blacklistés non utilisés** : lesnumeriques.com, degrouptest.com. L'Argus de l'Assurance, Les Échos, News Assurances Pro et La Tribune de l'Assurance ont opposé un mur WAF à la vérification automatisée : les faits correspondants sont adossés à la source primaire (alfa.asso.fr) ou à la presse accessible (Le Figaro).


---

# FICHIER : bras-7

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : Onze sources retenues cette édition, toutes françaises, dont sept publiées au fil d'octobre 2026. La tendance dominante est la migration de la fraude documentaire vers la souscription et l'entrée en relation : le faux est devenu gratuit, et l'identité de l'assuré lui-même devient la cible. Côté institutionnel, les autorités accélèrent — listes noires ACPR/AMF actualisées, proposition de loi sur l'usurpation d'identité déposée à l'Assemblée, décrets de la loi fraude en rédaction. Enfin, deux affaires impliquant directement un acteur de la protection sociale (escroquerie optique à 36 M€, soupçons de corruption interne chez Malakoff Humanis) rappellent que le risque ne vient pas que de l'extérieur.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : L'intelligence artificielle générative a fait tomber le coût d'un faux à zéro, et les cas de fraude assistée par IA ont quadruplé en trois ans. Les assureurs répondent en authentifiant la photo à la source, au moment de la capture, plutôt qu'en cherchant le faux après coup.
- **📈 Efficacité de gestion de la fraude** : L'agence de lutte contre la fraude à l'assurance chiffre neuf cent quarante-six millions d'euros de fraude identifiée en deux mille vingt-cinq. Un rapport conjoint des inspections préconise de cibler les contrôles avec la science des données et de payer après vérification.
- **🗂️ Exploitation de l'opendata** : L'ACPR et l'AMF ont publié fin octobre une nouvelle mise en garde commune avec leurs listes noires actualisées. Le jeu de données des entités non autorisées reste disponible en open data et alimente directement les contrôles d'entrée en relation.
- **🕸️ Lutte contre les bandes organisées** : Vingt-deux personnes et quinze structures sont renvoyées devant la justice pour une escroquerie à l'optique de trente-six millions d'euros. Le parquet de Paris y a appliqué pour la première fois des techniques spéciales d'enquête de la criminalité organisée.
- **🚪 Fraude en entrée en relation** : Une proposition de loi déposée début octobre durcirait la répression de l'usurpation d'identité et créerait une alerte consultable à la souscription. Le Médiateur de l'assurance confirme la hausse des fraudes aux versements en assurance vie via de faux relevés bancaires.
- **🩺 Fraude à la santé** : La lutte contre les faux arrêts de travail s'appuie désormais sur des formulaires sécurisés lus automatiquement, pour trente-quatre millions d'euros de fraude empêchée l'an dernier. Sept cents mille assurés ont été contrôlés, et le premier arrêt est plafonné à trente et un jours.
- **🧪 Divers — sujet émergent** : Un grand groupe de protection sociale est éclaboussé par des soupçons de corruption commise en bande organisée visant sa direction générale. Un signalement anonyme interne a déclenché une enquête : le risque de fraude interne mérite d'être traité comme un risque à part entière.

## 1. 🔍 Anti-fraude documentaire

- **[La fraude à l'assurance augmentée par l'IA](https://algopolis.eu/fr/article/19)** — *AlgoPolis, 23 octobre 2026*
  L'observatoire AlgoPolis montre que l'IA générative a réduit à zéro le coût d'une fausse preuve : photos de sinistres, factures et certificats médicaux de synthèse sont désormais à la portée de tous. Les cas de fraude assistée par IA ont été multipliés par quatre entre 2022 et 2025 (20 000 à plus de 80 000), l'assureur britannique Admiral constatant +71 % de fraude en 2025. L'article insiste sur la migration du risque du sinistre vers la souscription et l'identité, et sur l'effondrement de la valeur probante du document.
  **Pourquoi c'est pertinent ?** La conclusion opérationnelle est brutale : chercher le faux est une course perdue, il faut authentifier le vrai à la source (provenance, capture certifiée, données de terrain indépendantes) plutôt que détecter le faux après coup.
  *À surveiller* : les technologies de provenance et de signature cryptographique des images (type C2PA), transposables en preuve de première notification de sinistre.

- **[Assurances : quand l'IA simule des accidents](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)** — *franceinfo (France 2), 4 juillet 2026 — article de référence conservé pour ses chiffres assureurs inédits*
  Le reportage de France 2 documente la fabrication de faux accidents auto par IA générative : Direct Assurance y déclare avoir multiplié par 3,5 le nombre de faux documents reçus et détecter jusqu'à 16 M€ de demandes frauduleuses par an. La parade décrite est l'application de déclaration de sinistre avec photos géolocalisées et analysées en direct, qui crée un faisceau de preuves capté au moment T.
  **Pourquoi c'est pertinent ?** C'est le cas d'usage français le plus concret de la bascule du contrôle documentaire vers la capture certifiée à la FNOL, avec des chiffres d'assureur vérifiables.

## 2. 📈 Efficacité de gestion de la fraude

- **[Rapport d'activité 2025 — chiffres clés de la fraude à l'assurance](https://www.alfa.asso.fr/)** — *ALFA, 17 juillet 2026 — source de référence annuelle*
  Le rapport d'activité de l'agence des assureurs chiffre la fraude identifiée 2025 à 946 M€ (+4,9 %), dont 627 M€ en IARD, avec un taux de fraude de 1,27 % et une fraude réelle estimée à 2,5 Md€. La prévoyance (+25,8 %) et la santé (+11,8 %) progressent vite, l'assurance vie (+101,7 %) reste faible en volume mais double. Les modalités dominantes : fausses déclarations, fraude documentaire (dont photos modifiées par IA) et surévaluation du préjudice.
  **Pourquoi c'est pertinent ?** C'est le référentiel KPI annuel du marché : benchmark obligatoire pour situer l'efficacité de son propre dispositif de détection et calibrer les objectifs SIU.

- **[La lutte contre la fraude aux prescriptions et aux facturations à l'assurance maladie](https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf)** — *IGF-Igas, 29 juillet 2026*
  Le rapport conjoint des deux inspections générales établit que la détection ne couvre qu'une fraction de la fraude estimée (1,4 à 1,9 Md€/an sur le champ évalué) et préconise de cibler les contrôles par la science des données, de couvrir tous les professionnels de santé, de privilégier les dossiers à fort enjeu financier et de renforcer la coordination CPAM-parquets.
  **Pourquoi c'est pertinent ?** Ses recommandations alimentent les décrets de la loi de lutte contre la fraude alors en rédaction — impact réglementaire direct sur les obligations de contrôle et le partage de données entre assureurs et caisses.

## 3. 🗂️ Exploitation de l'opendata

- **[Escroqueries : l'ACPR et l'AMF mettent en garde le public contre les acteurs proposant des investissements Forex et crypto-actifs sans y être autorisés](https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0)** — *ACPR-AMF, 22 octobre 2026*
  Mise en garde conjointe des deux autorités avec actualisation régulière de leurs listes noires de sites proposant Forex et produits dérivés sur crypto-actifs sans autorisation, un grand nombre usurpant l'identité de professionnels régulés.
  **Pourquoi c'est pertinent ?** Chaque communiqué actualise la base de référence à croiser automatiquement en entrée en relation : une entité présente sur une liste noire doit déclencher un refus ou une vigilance renforcée à la souscription.

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers en France](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *data.gouv.fr (AMF), jeu de données mis à jour en continu, consulté le 3 novembre 2026*
  Le jeu de données open data de l'AMF recense les acteurs mis en garde ou usurpant un acteur régulé, en CSV structuré (nom, catégorie, date d'inscription), ce qui permet un contrôle automatique et un croisement avec le fichier clients ou prospects d'un assureur.
  **Pourquoi c'est pertinent ?** C'est la brique d'opendata directement intégrable dans un moteur de contrôle LCB-FT/onboarding : un batch quotidien suffit pour filtrer les entités blacklistées avant toute souscription.

## 4. 🕸️ Lutte contre les bandes organisées

- **[Fraude géante à l'optique : comment Malakoff Humanis a démasqué cette escroquerie à 36 millions d'euros](https://www.argusdelassurance.com/assurance-de-personnes/fraude-geante-a-loptique-comment-malakoff-humanis-a-demasque-cette-escroquerie-a-36-millions-deuros.4WUOHVNDFBB4NOXFVW2WCTFO4M.html)** — *L'Argus de l'assurance, 29 septembre 2026*
  Vingt-deux ophtalmologues, opticiens et responsables de santé, plus 15 structures, sont poursuivis pour escroquerie et blanchiment en bande organisée : fausses prescriptions, consultations fictives et surfacturation au détriment des organismes complémentaires (36 M€ en trois ans, potentiel estimé à 150 M€/an à Paris). Pour la première fois, des « techniques spéciales » de la criminalité organisée (écoutes, géolocalisation, sonorisation) ont été appliquées à un dossier impliquant des professionnels de santé. Le signalement vient d'un assureur : Malakoff Humanis avait repéré dès 2024 des atypies (50 à 150 paires de lunettes facturées par jour, reste à charge systématiquement nul).
  **Pourquoi c'est pertinent ?** La détection d'atypies de consommation par l'assureur, couplée à un signalement précoce au parquet, a déclenché un démantèlement — le modèle de la chaîne détection-signalement-techniques spéciales à répliquer.
  Impact réglementaire : l'affaire intervient pendant la rédaction des décrets de la loi de lutte contre la fraude, qui renforce justement les relations Ocam-Assurance maladie.

## 5. 🚪 Fraude en entrée en relation

- **[Proposition de loi n° 3228 — mieux réprimer l'usurpation d'identité et garantir l'accompagnement et le rétablissement rapide des victimes](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi)** — *Assemblée nationale, 6 octobre 2026*
  Déposée le 6 octobre 2026 et renvoyée en commission des lois, la proposition porte la peine de base de l'usurpation d'identité à cinq ans d'emprisonnement et 50 000 € d'amende, avec un délit aggravé à dix ans et 150 000 € quand les faits servent à souscrire un crédit, ouvrir un compte ou conclure un contrat au nom de la victime. Elle prévoit aussi une « alerte d'identité » consultable par les organismes habilités lors de la souscription d'un contrat d'assurance, et une garantie obligatoire contre les conséquences de l'usurpation dans les contrats couvrant la RC vie privée ou le logement.
  **Pourquoi c'est pertinent ?** Si elle est adoptée, la mesure change directement le KYC assureur : vérification renforcée obligatoire avant toute opération, alerte d'identité à interroger en entrée en relation, et nouvelle garantie à tarif produit.
  Impact réglementaire : texte non adopté à ce stade — à suivre en commission.

- **[Rapport d'activité 2025 de La Médiation de l'Assurance — focus « fraude aux versements » en assurance vie](https://www.mediation-assurance.org/wp-content/uploads/2026/09/Rapport_annuel_2025_LMA_page-simple.pdf)** — *La Médiation de l'Assurance, rapport 2025 publié en 2026 (mis en ligne septembre 2026)*
  Le Médiateur consacre un focus à la recrudescence des fraudes aux versements : un tiers usurpe l'identité de l'assuré ou du bénéficiaire et obtient un rachat ou un versement au décès sur un relevé d'identité bancaire falsifié. Il rappelle que l'assureur doit vérifier que la demande émane bien de l'assuré, sous peine de voir sa responsabilité engagée, et cite la jurisprudence récente sur le paiement non libératoire effectué sur un faux RIB.
  **Pourquoi c'est pertinent ?** Tout changement de coordonnées bancaires suivi d'une demande de rachat est la signature du schéma : ces contrôles en séquence (canal alternatif, corrélation temporelle) sont directement transposables aux procédures back-office vie.

## 6. 🩺 Fraude à la santé

- **[Arrêts maladie abusifs : les mesures anti-fraude sont-elles réellement efficaces ?](https://www.tf1info.fr/sante/reportage-tf1-arrets-maladie-abusifs-les-mesures-anti-fraude-sont-elles-reellement-efficaces-2463521.html)** — *TF1 Info, 11 septembre 2026*
  Le reportage fait le bilan des dispositifs anti-fraude sur les arrêts de travail : formulaire CERFA sécurisé obligatoire (étiquette holographique, encre magnétique) lu automatiquement en 0,3 seconde, 34 M€ de fraude empêchés en 2025 (+15 % sur un an), 700 000 assurés contrôlés dont 240 000 convoqués — l'arrêt n'était plus justifié dans la moitié des cas. Depuis septembre, le premier arrêt est plafonné à 31 jours.
  **Pourquoi c'est pertinent ?** Les prévoyances et complémentaires santé traitent les mêmes faux arrêts que la Sécurité sociale : les éléments de sécurité du CERFA et le plafonnement donnent des points de contrôle concrets pour la gestion IJSS et maintien de salaire.

## 7. 🧪 Divers — sujet émergent

- **[« Signalements anonymes », soupçons de corruption et enquête interne : ce scandale qui empoisonne Malakoff Humanis](https://www.lefigaro.fr/societes/signalements-anonymes-soupcons-de-corruption-et-enquete-interne-ce-scandale-qui-empoisonne-malakoff-humanis-le-geant-de-la-protection-sociale-20261028)** — *Le Figaro, 28 octobre 2026*
  Le deuxième groupe français de protection sociale est éclaboussé par des soupçons « de corruption commise en bande organisée » visant sa direction générale, à la suite de signalements anonymes partis de l'interne ; une enquête interne est en cours et un cabinet de chasse de têtes cherche déjà un remplaçant au DG.
  **Pourquoi c'est pertinent ?** Le risque de fraude interne — corruption en bande organisée au sommet d'un gestionnaire de protection sociale couvrant 10 millions de personnes — appelle les mêmes dispositifs que la fraude externe : lanceurs d'alerte, séparation des pouvoirs, audits ciblés.

## Synthèse — 5 signaux faibles à surveiller

1. **La fraude documentaire migre du sinistre vers la souscription et l'identité** : le faux gratuit rend la preuve injustifiable ; les réponses à structurer sont l'authentification à la source et la provenance cryptographique.
   - https://algopolis.eu/fr/article/19
   - https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html
2. **L'assureur devient à la fois détecteur et partie prenante d'affaires internes** : signalement d'atypies chez Malakoff Humanis d'un côté, soupçons de corruption interne au sommet du même groupe de l'autre.
   - https://www.argusdelassurance.com/assurance-de-personnes/fraude-geante-a-loptique-comment-malakoff-humanis-a-demasque-cette-escroquerie-a-36-millions-deuros.4WUOHVNDFBB4NOXFVW2WCTFO4M.html
   - https://www.lefigaro.fr/societes/signalements-anonymes-soupcons-de-corruption-et-enquete-interne-ce-scandale-qui-empoisonne-malakoff-humanis-le-geant-de-la-protection-sociale-20261028
3. **La réponse pénale se durcit et se professionnalise** : techniques spéciales de la criminalité organisée appliquées à la fraude santé, et proposition de loi portant l'usurpation d'identité aggravée à dix ans.
   - https://www.argusdelassurance.com/assurance-de-personnes/fraude-geante-a-loptique-comment-malakoff-humanis-a-demasque-cette-escroquerie-a-36-millions-deuros.4WUOHVNDFBB4NOXFVW2WCTFO4M.html
   - https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi
4. **Les listes noires deviennent une brique automatisable du contrôle d'entrée en relation** : flux ACPR-AMF régulier et jeu de données open data en CSV directement croisable avec les fichiers clients.
   - https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0
   - https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france
5. **Le chantier réglementaire de la loi fraude arrive en phase opérationnelle** : décrets en rédaction, recommandations IGF-Igas (science des données, contrôle avant paiement, coordination CPAM-parquets) et alerte d'identité proposée en souscription.
   - https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf
   - https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi

---

*Méthode : sources sélectionnées sur fenêtre glissante (priorité octobre 2026, tolérance jusqu'à juillet 2026 pour les références ALFA, IGF-Igas, franceinfo et TF1). Date de publication vérifiée sur chaque page source : piège JJ/MM corrigé sur l'article franceinfo (04/07/2026, et non début août comme suggéré par certains agrégateurs) et sur l'article de l'Argus (29/09/2026, et non 13/10). Aucun site blacklisté (lesnumeriques.com, degrouptest.com) ni blog de cabinet, comparateur ou communiqué d'éditeur retenu ; la fiche du jeu de données data.gouv.fr n'est admise que dans l'axe opendata. Sources écartées : reprises multiples du rapport ALFA (une seule entrée), rapport Tessi (whitepaper d'éditeur), articles identifAI et Reality Defender (journaux de fournisseurs), blogs d'avocats sur la PPL 3228 et l'affaire de Beauvais (texte primaire de l'Assemblée nationale retenu à la place). Aucun accès bloqué n'a dû être contourné pour cette édition.*


---

# FICHIER : bras-8

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : 20 sources retenues pour l'édition couvrant octobre 2026 (18 françaises, 2 internationales), dont huit émanant directement d'autorités — ALFA, Banque de France, Assurance Maladie (Cnam), data.gouv.fr, Sénat, Ministère de l'Économie, MAS. La tendance dominante est la banalisation de la fraude documentaire assistée par l'IA, désormais citée par l'ALFA parmi les trois mécanismes les plus observés en IARD comme en prévoyance. Ce qui monte : l'analyse forensique des pièces et le criblage des identités à l'entrée en relation, portés par les listes noires publiques (AMF/ACPR) et par le registre national des IBAN frauduleux entré en vigueur en mai. Côté santé, l'Assurance Maladie franchit un record — 723 M€ détectés et stoppés en 2025 — et la fraude s'industrialise au point d'être traitée comme une criminalité organisée. Les signaux faibles portent sur la preuve (opposabilité, métadonnées) et sur la responsabilité croissante de l'assureur pour les systèmes d'IA qu'il déploie.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : La fraude documentaire change d'échelle. L'intelligence artificielle permet de fabriquer en quelques clics de faux justificatifs et de fausses photos de sinistres, et les assureurs renforcent l'analyse forensique des pièces.
- **📈 Efficacité de gestion de la fraude** : Les assureurs ont identifié neuf cent quarante-six millions d'euros de fraude en deux mille vingt-cinq, en hausse de près de cinq pour cent. La détection progresse, mais le recouvrement et la qualité de la preuve restent les points faibles.
- **🗂️ Exploitation de l'opendata** : Les données publiques deviennent un outil de contrôle. Listes noires de l'AMF et de l'ACPR, statistiques de la Banque de France sur les paiements : ces bases permettent d'automatiser le criblage des faux courtiers et des bénéficiaires de virements.
- **🕸️ Lutte contre les bandes organisées** : La fraude s'organise. Réseaux de centres de santé, accidents provoqués, corruption interne : la fraude en bande progresse et les parlementaires comme la presse pointent les failles de gouvernance des organismes de protection sociale.
- **🚪 Fraude en entrée en relation** : L'entrée en relation est le nouveau point de rupture. Deepfakes d'identité, usurpation de contrats, faux relevés d'identité bancaire : Interpol et le registre national des IBAN suspects appellent à vérifier l'identité avant tout engagement.
- **🩺 Fraude à la santé** : La fraude à l'assurance maladie atteint un record : sept cent vingt-trois millions d'euros détectés et stoppés en deux mille vingt-cinq. Les centres de santé, les audioprothésistes et les faux arrêts de travail concentrent l'essentiel du préjudice.
- **🧪 Divers — sujet émergent** : L'intelligence artificielle entre dans le champ réglementaire. Le calendrier de l'AI Act se précise et Singapour rend déjà les assureurs responsables des systèmes d'IA de leurs prestataires, y compris les outils de détection.

## 1. 🔍 Anti-fraude documentaire

- **[Assurances : quand l'IA simule des accidents](https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html)** — *franceinfo, 4 juillet 2026*
  L'IA générative permet de fabriquer en quelques clics un accident automobile crédible (photo de véhicule accidenté, déclaration cohérente, témoignages synthétiques). Chez Direct Assurance, les faux documents reçus ont été multipliés par 3,5 en un an. En assurance, la fraude documentaire ne se limite plus à une pièce isolée : elle devient un dossier complet fabriqué pour franchir tous les contrôles.
  **Pourquoi c'est pertinent ?** La preuve photographique — socle historique de la gestion de sinistre — n'est plus fiable en l'état : il faut exiger les originaux, vérifier les métadonnées et industrialiser la détection d'artefacts avant règlement.
  *À surveiller :* analyse des micro-signaux et des métadonnées (création, retouches), confrontation au terrain.
  **Impact réglementaire :** AI Act (traçabilité et marquage des contenus générés), RGPD (analyse des pièces transmises).

- **[C'est quoi le problème avec le système censé lutter contre la fraude à la carte grise ?](https://www.20minutes.fr/societe/4251586-20261006-quoi-probleme-systeme-cense-lutter-contre-fraude-carte-grise)** — *20 Minutes, 6 octobre 2026*
  Depuis le 1ᵉʳ août 2026, l'État a durci les conditions d'accès au système d'immatriculation (SIV) pour les professionnels habilités, après la révélation d'une fraude massive : « voitures fantômes », faux garages et certificats d'immatriculation falsifiés, avec un nombre d'habilitations drastiquement réduit. Le dispositif censé lutter contre la fraude était lui-même le point d'entrée de la fraude.
  **Pourquoi c'est pertinent ?** Un faux certificat d'immatriculation contamine directement la souscription auto : souscripteur non identifiable, véhicule volé, droit à indemnisation fragilisé et recours impossibles contre le tiers responsable.
  *À surveiller :* contrôle des habilitations professionnelles et recoupement SIV / fichiers d'assurance.

- **[Avec l'IA, la fraude documentaire s'industrialise : les assureurs sont-ils prêts ?](https://www.journaldunet.com/fintech/1557315-avec-l-ia-la-fraude-documentaire-s-industrialise-les-assureurs-sont-ils-prets/)** — *Journal du Net, 3 novembre 2026*
  Selon le baromètre Yousign × Ipsos 2026, un professionnel sur cinq déclare avoir déjà été confronté à un document numérique falsifié ou compromis — un chiffre qui traduit une industrialisation, et non une simple hausse des tentatives. L'article pose la question clé : la charge de la preuve repose sur l'assureur, et une preuve numérique n'a de valeur que si elle reste opposable des années après la signature.
  **Pourquoi c'est pertinent ?** La robustesse d'un parcours de souscription numérique ne protège rien si la preuve produite n'est pas défendable en justice : horodatage, scellement et conservation deviennent des exigences de conformité, pas des options.
  **Impact réglementaire :** charge de la preuve en assurance, eIDAS 2 (attestations d'attributs, wallet européen).

## 2. 📈 Efficacité de gestion de la fraude

- **[Fraude à l'assurance — chiffres clés du rapport d'activité 2025](https://www.alfa.asso.fr/fraude-a-lassurance/)** — *ALFA (Agence de lutte contre la fraude à l'assurance), 17 juillet 2026*
  946,3 M€ de fraude identifiée en 2025 (+4,9 %, après +28 % en 2024), dont 626,6 M€ en IARD, 294 M€ en assurance de personnes et 25 M€ en assurance vie ; le taux de fraude ressort à 1,27 % des prestations payées, et la fraude réelle est estimée à 2,5 Md€. La collecte porte sur 19 des 20 plus grands groupes français, sur base volontaire. L'agence souligne à la fois l'ampleur du phénomène et l'efficacité accrue des mécanismes de détection.
  **Pourquoi c'est pertinent ?** C'est la référence chiffrée annuelle pour situer ses propres KPI de détection : la décélération de la hausse (+4,9 % contre +28 %) est un argument de ROI interne à exploiter en comité anti-fraude.
  *À surveiller :* la part de la fraude documentaire (faux justificatifs, photos modifiées par IA), citée parmi les trois mécanismes les plus observés en IARD et en prévoyance.

- **[Rapport d'activité 2025 — focus « la fraude aux versements en assurance vie »](https://www.mediation-assurance.org/rapports-activite/)** — *La Médiation de l'Assurance, septembre 2026*
  La Médiation de l'Assurance a reçu 46 830 saisines en 2025, soit +28 % sur un an, et 60 000 sur les douze derniers mois — un « choc de saisines » qui traduit aussi une dégradation des parcours. Le rapport consacre un focus spécifique à la « fraude » aux versements en assurance vie.
  **Pourquoi c'est pertinent ?** Le litige est le miroir des failles de contrôle en gestion : les dossiers de fraude aux versements (faux RIB, usurpation) remontent par le contentieux, ce qui donne un indicateur de qualité de contrôle exploitable en comité LCB-FT.
  **Impact réglementaire :** conformité des versements/rachats, obligations de vigilance LCB-FT sur les opérations en assurance vie.

- **[Baromètre Fraude 2026 : 52 % des ETI et grandes entreprises constatent une hausse des tentatives](https://www.allianz-trade.fr/actualites/etude-fraude-2026.html)** — *Allianz Trade avec Odoxa, 16 juin 2026*
  Plus d'une ETI ou grande entreprise sur deux constate une hausse des tentatives de fraude sur douze mois ; l'étude (1 005 Français et 315 dirigeants interrogés) mesure la montée des fraudes assistées par l'IA et le taux d'aboutissement des tentatives. La fraude s'installe comme risque opérationnel majeur pour les entreprises françaises.
  **Pourquoi c'est pertinent ?** Ce baromètre documente la maturité réelle des dispositifs côté assurés professionnels — un proxy des risques en souscription pro/RC et un argument de conseil (garanties cyber et fraude) pour les réseaux.

## 3. 🗂️ Exploitation de l'opendata

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers en France](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france)** — *data.gouv.fr (Autorité des marchés financiers), mise à jour du 5 novembre 2026*
  Le jeu de données ouvre et structure les listes noires AMF/ACPR des entités non autorisées (faux assureurs, faux courtiers, sites de crédit ou d'épargne frauduleux). Il permet de construire un contrôle automatisé de criblage — une jointure sur le nom commercial, le domaine ou le SIREN — directement branché sur le parcours de souscription.
  **Pourquoi c'est pertinent ?** Un criblage automatique de ces listes au moment de l'entrée en relation bloque les faux courtiers et les usurpateurs avant tout encaissement de prime ou engagement de garantie.
  **Impact réglementaire :** LCB-FT (vigilance à l'entrée en relation), devoir de conseil sur les intermédiaires.

- **[Observatoire de la sécurité des moyens de paiement — rapport 2025](https://www.banque-france.fr/system/files/2026-09/Communique_de_presse_du_rapport_2025.pdf)** — *Banque de France, 7 septembre 2026*
  Pour son dixième anniversaire, l'Observatoire salue une maîtrise globale de la fraude aux moyens de paiement (la fraude progresse moins vite que les flux) mais appelle à la mobilisation contre la fraude **par manipulation** (faux conseiller, ingénierie sociale, usurpation d'identité). Le rapport est accompagné d'un dossier statistique ouvert au format XLSX.
  **Pourquoi c'est pertinent ?** La fraude par manipulation se prolonge en fraude au faux RIB et à l'ordre de virement côté assureurs et épargnants : disposer des statistiques officielles permet de calibrer les contrôles sur les flux sortants (paiements de sinistres, remboursements).

## 4. 🕸️ Lutte contre les bandes organisées

- **[Structuration de réseaux de fraude à l'assurance maladie](https://www.senat.fr/questions/base/2026/qSEQ260609170.html)** — *Sénat, question écrite publiée le 18 juin 2026*
  Question attirant l'attention du gouvernement sur la structuration de réseaux organisés de fraude à l'assurance maladie, et sur les moyens de détection et de sanction associés. Le sujet est désormais traité comme une criminalité organisée et non comme une série d'abus isolés.
  **Pourquoi c'est pertinent ?** Signal politique : la lutte contre la fraude santé organisée devient un enjeu de sécurité publique, ce qui justifie des moyens d'enquête et une coopération renforcée entre caisses, parquets et assureurs complémentaires.
  **Impact réglementaire :** loi du 25 juin 2026 élargissant le champ des pénalités financières.

- **[« Signalements anonymes », soupçons de corruption et enquête interne : ce scandale qui empoisonne Malakoff Humanis](https://www.lefigaro.fr/societes/signalements-anonymes-soupcons-de-corruption-et-enquete-interne-ce-scandale-qui-empoisonne-malakoff-humanis-le-geant-de-la-protection-sociale-20261028)** — *Le Figaro, 28 octobre 2026*
  Enquête sur une crise de gouvernance au sein d'un des premiers groupes français de protection sociale : signalements anonymes, soupçons de corruption et enquête interne. L'affaire porte sur les conflits d'intérêts et les circuits de décision, pas sur la fraude de l'assuré.
  **Pourquoi c'est pertinent ?** Rappel utile : un dispositif anti-fraude qui ignore la corruption interne et les conflits d'intérêts reste incomplet — la cartographie LCB-FT et le dispositif d'alerte interne font partie du périmètre.

- **[« Crash for cash » : c'est quoi cette arnaque routière qui cible votre assurance ?](https://www.laprovence.com/article/economie/13416947382841/crash-for-cash-cest-quoi-cette-arnaque-routiere-qui-cible-votre-assurance)** — *La Provence, 26 octobre 2026*
  Décryptage de la typologie du « crash for cash » : un conducteur complice provoque volontairement un accident léger (freinage brutal, insertion forcée) pour déclencher des indemnisations corporelles, souvent au sein de réseaux incluant passagers, réparateurs et prestataires médicaux.
  **Pourquoi c'est pertinent ?** Typologie organisée récurrente et rentable : la détection passe par l'analyse de réseau (répétition de véhicules, de tiers, de prestataires) plutôt que par le dossier pris isolément.

## 5. 🚪 Fraude en entrée en relation

- **[INTERPOL lance une campagne de sensibilisation sur les risques d'arnaques par deepfake IA](https://www.interpol.int/fr/Actualites-et-evenements/Actualites/2026/INTERPOL-launches-public-awareness-campaign-highlighting-risk-of-AI-deepfake-scams)** — *INTERPOL, 19 octobre 2026*
  INTERPOL alerte le public sur l'usage des deepfakes — vidéo, voix clonée, faux documents — pour usurper l'identité de proches, de dirigeants ou d'institutions et déclencher des virements. La campagne cible précisément les victimes de manipulation en temps réel.
  **Pourquoi c'est pertinent ?** Ces techniques sont directement transposables aux parcours de vérification d'identité (KYC) et à la fraude au président chez les courtiers et délégataires de gestion : la détection de présence réelle et d'injection vidéo devient un contrôle obligatoire.

- **[« Tout est vrai… sauf mon e-mail » : le cauchemar de Micheline, 82 ans, victime d'une arnaque à l'assurance santé](https://www.leparisien.fr/economie/votre-argent/je-ne-pensais-pas-quil-etait-aussi-facile-dusurper-mon-nom-elle-change-de-complementaire-sante-a-son-insu-10-06-2026-HC7SP7YXKBDHJOEO3P3IWKZHAI.php)** — *Le Parisien, 10 juin 2026*
  Une retraitée découvre que sa complémentaire santé a été changée à son insu, sans démarchage, à partir de données exactes et d'une simple adresse e-mail usurpée. Le journal documente la prolifération de ces usurpations d'identité et faux contrats signés en ligne.
  **Pourquoi c'est pertinent ?** L'usurpation à l'entrée en relation est un angle mort : sans vérification de l'identité et du consentement au changement de contrat, le contrôle des mandats et des avenants ne vaut rien.
  *À surveiller :* vérification d'e-mail/IBAN et double validation aux points de bascule (changement de contrat, ajout de bénéficiaire).

- **[Lancement de la plateforme des IBAN suspects : un nouvel outil-clé de lutte contre la fraude aux paiements](https://presse.economie.gouv.fr/lancement-de-la-plateforme-des-iban-suspects-un-nouvel-outil-cle-de-lutte-contre-la-fraude-aux-paiements/)** — *Ministère de l'Économie et Banque de France, 7 mai 2026*
  Depuis le 7 mai 2026, le fichier national des IBAN frauduleux (FNC-RF) oblige les prestataires de paiement à vérifier les coordonnées bancaires des bénéficiaires avant d'exécuter un virement, et à signaler les IBAN suspects. C'est une brique d'infrastructure publique contre la fraude au faux RIB.
  **Pourquoi c'est pertinent ?** Pour les assureurs, courtiers et délégataires, c'est un contrôle directement mobilisable sur les flux sortants — paiement de sinistres, remboursements, rejets de prime — où la fraude au changement de RIB se concentre.
  **Impact réglementaire :** LCB-FT et sécurité des paiements.

## 6. 🩺 Fraude à la santé

- **[Lutte contre la fraude à l'Assurance maladie : 723 M€ détectés et stoppés en 2025](https://rapport-annuel.assurance-maladie.fr/chiffres-cles)** — *Assurance Maladie (Cnam), bilan 2025 — 16 avril 2026*
  L'Assurance Maladie a détecté et stoppé 723 M€ de fraudes en 2025 (+15 %, au-delà de l'objectif de 550 M€), soit un résultat triplé depuis 2021 ; sa stratégie préventive a en outre évité 286 M€ de paiements indus, avec 1 700 agents dédiés. Les professionnels de santé libéraux concentrent l'essentiel du préjudice : centres de santé (138 M€), audioprothésistes (~86 M€), transporteurs sanitaires (~62 M€) ; les assurés représentent 53 % des dossiers mais 16 % des montants, surtout via les arrêts de travail (49 M€).
  **Pourquoi c'est pertinent ?** C'est la référence absolue du thème : le séquençage prévention/détection et le ciblage par typologie de professionnel sont directement transposables aux organismes complémentaires et aux plateformes de tiers payant.

- **[Soupçonné de fraude à l'assurance maladie, un kiné de Calais placé en garde à vue](https://www.lavoixdunord.fr/1750544/article/2026-10-30/soupconne-de-fraude-l-assurance-maladie-un-kine-de-calais-place-en-garde-a-vue)** — *La Voix du Nord, 30 octobre 2026*
  Un masseur-kinésithérapeute de Calais est soupçonné d'avoir escroqué l'Assurance maladie. La CPAM avait des doutes dès fin 2025 et a signalé le praticien à la police, le témoignage de patients ayant confirmé les soupçons.
  **Pourquoi c'est pertinent ?** Le signalement par les patients/assurés est un canal de détection sous-exploité et peu coûteux : le retour d'expérience est transposable aux complémentaires santé et aux dispositifs de tiers payant.

- **[La lutte contre la fraude aux prescriptions et aux facturations à l'assurance maladie (rapport IGF/IGAS)](https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf)** — *Inspection générale des finances / IGAS, octobre 2025*
  Mission conjointe sur les fraudes aux prescriptions et aux facturations : soins fictifs, surfacturation d'actes, ordonnances détournées ou établies au nom de praticiens décédés. Le rapport documente les montages, les failles du contrôle et les leviers de sécurisation (ordonnance numérique, contrôle à la source).
  **Pourquoi c'est pertinent ?** Cadre de référence pour auditer les réseaux de soins et cibler les contrôles : il distingue les fraudes systémiques (réseaux) des erreurs de facturation et fournit les critères de ciblage.
  **Impact réglementaire :** LFSS, ordonnance numérique, loi du 25 juin 2026.

## 7. 🧪 Divers — sujet émergent

- **[AI Act : obligations en vigueur et reports de l'omnibus 2026/1744](https://www.actuia.com/actualite/calendrier-ai-act-ce-qui-sapplique-ce-que-lomnibus-reporte/)** — *ActuIA, 6 octobre 2026*
  Au 6 octobre 2026, trois blocs du règlement (UE) 2024/1689 s'appliquent déjà, tandis que l'omnibus décale certaines échéances (notamment le régime « haut risque », repoussé au 2 décembre 2027). Or de nombreux systèmes anti-fraude — scoring, biométrie, détection d'anomalies — relèvent du haut risque.
  **Pourquoi c'est pertinent ?** La conformité AI Act conditionne le calendrier de déploiement des outils de détection : documentation, supervision humaine et journalisation doivent être intégrées dès la conception, pas rattrapées après déploiement.
  **Impact réglementaire :** AI Act (règlement UE 2024/1689), RGPD.

- **[Financial institutions must remain accountable for use of third-party AI tools: MAS](https://www.singaporelawwatch.sg/Headlines/userid/3/financial-institutions-must-remain-accountable-for-use-of-third-party-ai-tools-mas)** — *Monetary Authority of Singapore, 7 octobre 2026*
  Singapour a publié ses directives finales de gestion des risques liés à l'IA : banques, assureurs, sociétés de paiement et de gestion d'actifs restent responsables de **tous** les systèmes d'IA qu'ils utilisent, y compris ceux de leurs prestataires, avec une mise en conformité échelonnée à partir d'octobre 2027. Le régulateur refuse explicitement le transfert de responsabilité vers l'éditeur.
  **Pourquoi c'est pertinent ?** Annonce le même principe en Europe (AI Act, eIDAS 2) : l'assureur ne peut pas déléguer sa responsabilité à l'outil anti-fraude acheté — il devra exiger documentation, tests et preuves de son fournisseur.
  **Impact réglementaire :** MAS AI Risk Management Guidelines, AI Act.

- **[Visages volés, deepfakes, arnaques au PDG… L'identité, nouveau front de l'assurance](https://www.ladn.eu/entreprises-innovantes/assurance-deepfakes-usurpation-identite-numerique/)** — *L'ADN, 3 juillet 2026*
  La couverture du risque deepfake et d'usurpation d'identité se structure : avenants « Deepfake Response » (analyse technique, retrait de contenu, soutien réputationnel) et couvertures vol d'identité haut de gamme. L'article souligne la difficulté proprement assurantielle — comment évaluer un préjudice réputationnel ou une voix utilisée sans consentement.
  **Pourquoi c'est pertinent ?** Nouveau terrain d'assurance (RC, cyber) où le risque de « couverture silencieuse » est élevé : il faut décider explicitement ce qui est couvert par l'IA générative avant que le contentieux ne tranche.
  **Impact réglementaire :** AI Act, RGPD (droit à l'image, droit à la voix).

## Synthèse — 5 signaux faibles à surveiller

1. **La preuve photographique et documentaire cesse d'être une preuve.** L'IA générative banalise les faux justificatifs et les photos de dommages truquées ; l'assureur supporte la charge de la preuve et doit la rendre opposable dans le temps.
   - https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html
   - https://www.journaldunet.com/fintech/1557315-avec-l-ia-la-fraude-documentaire-s-industrialise-les-assureurs-sont-ils-prets/

2. **La fraude documentaire migre vers les titres et les professionnels habilités.** Le durcissement du 1ᵉʳ août 2026 sur les habilitations d'immatriculation révèle que les faux paraprofessionnels sont devenus un canal d'entrée de la fraude en assurance auto.
   - https://www.20minutes.fr/societe/4251586-20261006-quoi-probleme-systeme-cense-lutter-contre-fraude-carte-grise

3. **Le recouvrement reste le maillon faible des dispositifs.** Détections records des deux côtés (assureurs comme Assurance Maladie) mais un recouvrement partiel : l'enjeu des deux prochaines années est l'efficacité aval, pas la seule détection.
   - https://www.alfa.asso.fr/fraude-a-lassurance/
   - https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/2025-E-047-Fraude-assurance-maladie.pdf

4. **Le deepfake d'identité devient le vecteur privilégié de l'usurpation à l'entrée en relation.** Alerte internationale d'INTERPOL et usurpations de contrats documentées : la vérification de présence réelle et du consentement redevient un contrôle de premier rang.
   - https://www.interpol.int/fr/Actualites-et-evenements/Actualites/2026/INTERPOL-launches-public-awareness-campaign-highlighting-risk-of-AI-deepfake-scams
   - https://www.leparisien.fr/economie/votre-argent/je-ne-pensais-pas-quil-etait-aussi-facile-dusurper-mon-nom-elle-change-de-complementaire-sante-a-son-insu-10-06-2026-HC7SP7YXKBDHJOEO3P3IWKZHAI.php

5. **La responsabilité pour l'IA déployée se déplace vers l'assureur.** Le calendrier AI Act se précise et Singapour impose déjà l'imputabilité des systèmes d'IA des prestataires : l'outil anti-fraude acheté ne transfère aucune responsabilité.
   - https://www.actuia.com/actualite/calendrier-ai-act-ce-qui-sapplique-ce-que-lomnibus-reporte/
   - https://www.singaporelawwatch.sg/Headlines/userid/3/financial-institutions-must-remain-accountable-for-use-of-third-party-ai-tools-mas


---

# FICHIER : bras-9

# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : Treize sources retenues ce mois-ci, dont onze françaises, avec une actualité dominée par la montée en puissance de l'IA générative dans tous les maillons de la chaîne anti-fraude. La tendance de fond est le glissement du faux document isolé vers le dossier complet et le processus entier, constaté à la fois par l'Observatoire Tessi et par les analystes. Côté sanction, la loi du 25 juin 2026 relative à la lutte contre les fraudes sociales et fiscales durcit fortement le régime des pénalités, notamment en bande organisée. Enfin, les institutions (ALFA, ACPR-AMF, Assurance maladie) investissent simultanément la détection par sources ouvertes, les listes noires et le signalement citoyen.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : Le deuxième rapport de l'Observatoire Tessi constate que la fraude ne se limite plus au faux document isolé, mais s'installe dans des dossiers complets. Trente-deux pour cent des fraudeurs falsificateurs disent avoir utilisé l'IA générative.
- **📈 Efficacité de gestion de la fraude** : L'ALFA publie un bilan à neuf cent quarante-six millions d'euros de fraude détectée en deux mille vingt-cinq. La loi du vingt-cinq juin alourdit les pénalités, jusqu'à quatre cents pour cent en bande organisée.
- **🗂️ Exploitation de l'opendata** : L'ACPR et l'AMF ont ajouté en octobre trente-six nouveaux sites non autorisés à leurs listes noires publiques. Ces données ouvertes alimentent les contrôles d'entrée en relation des assureurs.
- **🕸️ Lutte contre les bandes organisées** : L'arnaque du crash for cash se diffuse en France, avec freinage provoqué, faux témoins et vol de documents. À Toulouse, un réseau de narcotrafic blanchissait via des fraudes aux assurances.
- **🚪 Fraude en entrée en relation** : Les identités synthétiques représentent deux milliards quatre cents millions de dollars d'exposition aux États-Unis. Les données issues de fuites rendent le vrai indiscernable du fraudeur bien informé.
- **🩺 Fraude à la santé** : Douze cents assurés ont acheté un faux arrêt maladie sur Snapchat pour un préjudice de trois millions et demi d'euros. L'Assurance maladie annonce un record historique de sept cent vingt-trois millions d'euros stoppés.
- **🧪 Divers — sujet émergent** : L'ALFA a organisé son troisième Hunter Game, un serious game de renseignement en sources ouvertes. Trois cent quarante-quatre participants ont enquêté sur une fraude d'assurance simulée.

## 1. 🔍 Anti-fraude documentaire

- **Fraude documentaire : le 2e rapport de l'Observatoire Tessi révèle des menaces plus complexes et des réponses en pleine structuration** — *Communiqué Tessi (PDF), 7 juillet 2026*
  https://www.tessi.eu/wp-content/uploads/2026/07/cp-fraude-documentaire-le-2e-rapport-de-lobservatoire-tessi-20260707.pdf
  Le deuxième rapport de l'Observatoire Tessi, fondé sur des entretiens avec des experts indépendants (Cnam, Banque de France, Groupama), établit que 903 M€ de fraudes ont été détectés en assurance (+30 % en un an) et que 32 % des fraudeurs ayant falsifié un document déclarent avoir utilisé l'IA générative. Le constat central : la fraude se déplace du document vers le processus entier — dossiers mêlant pièces authentiques, déclarations trompeuses et identités détournées. Impact réglementaire : le rapport documente la structuration des réponses (eIDAS II, wallet européen, registre européen des IBAN frauduleux opérationnel depuis mai 2026).
  **Pourquoi c'est pertinent ?** Il déplace la cible du contrôle qualité : c'est la cohérence inter-documents du dossier de sinistre qu'il faut scorer, plus la pièce isolée.
  *À surveiller* : l'analyse de cohérence d'ensemble documentaire, transposable aux flux de gestion de sinistres.

- **La fraude à l'assurance augmentée par l'IA** — *AlgoPolis, 23 octobre 2026*
  https://algopolis.eu/fr/article/19
  Cette analyse chiffrée montre que le prix d'un faux est tombé à zéro : cas de fraude assistée par IA multipliés par quatre (de 20 000 en 2022 à plus de 80 000 en 2025), fraude en hausse de 71 % chez l'assureur britannique Admiral en partie imputée aux images générées. L'article plaide pour authentifier le vrai à la source plutôt que de traquer le faux, et couvre la souscription, le sinistre et l'identité. Impact réglementaire : rappelle l'usage des modèles classés « haut risque » au sens de l'AI Act dans la détection.
  **Pourquoi c'est pertinent ?** Il formule le changement de doctrine — authentifier la provenance (photo géolocalisée, horodatage) plutôt que courir après les artefacts du faux.

- **Assurances : quand l'IA simule des accidents** — *franceinfo, 4 juillet 2026*
  https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html
  Le reportage de franceinfo documente des photos de pare-brise endommagé générées par IA envoyées à Direct Assurance : le nombre de faux documents reçus y a été multiplié par 3,5, pour jusqu'à 16 M€ de demandes frauduleuses détectées par an. En parade, des assureurs imposent une application de déclaration où les photos sont prises en direct, géolocalisées et analysées immédiatement. Source de référence, citée par toute la presse d'octobre (Capital, Auto Journal).
  **Pourquoi c'est pertinent ?** Elle donne des chiffres de terrain d'un assureur français et un contre-modèle opérationnel : fermer la porte à l'import de fichiers stockés.

## 2. 📈 Efficacité de gestion de la fraude

- **Fraude à l'assurance : 946 millions détectés en 2025, et l'accident simulé coûte cher** — *JeChange, 24 octobre 2026*
  https://www.jechange.fr/assurance/auto/news/fraude-assurance-946-millions-2025-accident-simule
  Synthèse détaillée du rapport annuel de l'ALFA (publié en juillet 2026) : 946,3 M€ de fraude détectée en 2025 (+4,9 %), dont 626,6 M€ en IARD, contre une fraude réelle estimée à 2,5 milliards. L'article détaille le cas de l'accident simulé (« crash for cash ») et le barème qui condamne le conducteur qui percute l'arrière à 100 % de responsabilité. Comparateur, retenu ici car il porte le chiffrage détaillé par branche daté d'octobre, avec les limites méthodologiques explicitées.
  **Pourquoi c'est pertinent ?** Il fournit le référentiel chiffré annuel à mobiliser dans toute argumentation ROI et la répartition IARD/personnes/vie pour calibrer les dispositifs.

- **Fraudes sociales et fiscales : une loi pour mieux les détecter et lutter** — *economie.gouv.fr, 25 juin 2026*
  https://www.economie.gouv.fr/actualites/fraudes-sociales-et-fiscales-une-loi-pour-mieux-les-detecter-et-lutter
  La loi n° 2026-534 du 25 juin 2026 relative à la lutte contre les fraudes sociales et fiscales est promulguée : CSG à 25 % sur les activités illicites, escroqueries en bande organisée au préjudice des finances publiques passibles de quinze ans de réclusion et 1 M€ d'amende, pouvoirs d'enquête renforcés. Elle porte à 300 % des sommes (400 % en bande organisée) les plafonds de pénalité applicable aux fraudeurs. Impact réglementaire direct : L114-17-1 du Code de la sécurité sociale en vigueur depuis le 27 juin 2026.
  **Pourquoi c'est pertinent ?** Elle change l'échelle des sanctions récupérables en gestion de sinistre santé/prévoyance et justifie d'escalader systématiquement vers le contentieux.

## 3. 🗂️ Exploitation de l'opendata

- **L'ACPR et l'AMF mettent en garde le public contre plusieurs acteurs proposant en France des investissements non autorisés** — *ACPR-Banque de France, 22 octobre 2026*
  https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0
  Mise à jour trimestrielle des listes noires : 57 sites Forex et 36 sites de produits dérivés sur crypto-actifs ajoutés depuis janvier 2026, dont 26 et 10 au seul troisième trimestre. Les listes sont consultables sur ABE IS et amf-france.org, avec renvoi vers Regafi et Orias pour vérifier une autorisation. Page de jeu de données admissible dans cet axe : elle documente ce que le croisement permet — vérifier automatiquement une entité à l'entrée en relation.
  **Pourquoi c'est pertinent ?** Ces listes publiques sont directement consommables dans les contrôles KYC des souscriptions et du démarchage, y compris pour filtrer faux courtiers et faux assureurs.

## 4. 🕸️ Lutte contre les bandes organisées

- **Crash for cash : c'est quoi cette arnaque automobile et comment s'en protéger ?** — *BFM TV, 14 octobre 2026*
  https://www.bfmtv.com/pratique/auto-moto/crash-for-cash-c-est-quoi-cette-arnaque-automobile-et-comment-s-en-proteger_AN-202610140613.html
  La presse nationale relaie en octobre la diffusion en France du « crash for cash » : collision provoquée à faible vitesse, freinage brutal, faux témoins, blessures simulées et — point clé — demande de photographier le permis et l'attestation d'assurance de la victime pour alimenter de faux dossiers de sinistres ou souscrire des contrats à son nom. Typologie déjà alertée par Direct Assurance et reprise par La Provence et franceinfo.
  **Pourquoi c'est pertinent ?** Le vol de documents d'identité sur sinistre relie la fraude auto de rue à la fraude en entrée en relation : il faut traiter le constat amiable comme une collecte de données sensible.

- **Le narcotrafic entre Toulouse et les Pays-Bas rapporte gros, la gendarmerie fait tomber tout un réseau** — *La Dépêche, 26 juin 2026*
  https://www.ladepeche.fr/2026/06/26/grosses-berlines-jet-skis-et-montres-de-luxe-le-narcotrafic-entre-toulouse-et-les-pays-bas-rapporte-gros-la-gendarmerie-fait-tomber-tout-un-reseau-13437539.php
  La section de recherches de Toulouse et le GIR démantèlent un réseau de narcotrafic : dix interpellations, plus de 130 000 € d'avoirs saisis, et surtout un blanchiment d'environ un demi-million d'euros passant par des « fraudes aux assurances » répétées des dizaines de fois entre mai 2025 et avril 2026. Article de référence illustrant l'imbrication entre criminalité organisée classique et fraude à l'assurance comme outil de blanchiment.
  **Pourquoi c'est pertinent ?** Rappelle que la fraude à l'assurance est un vecteur de recyclage pour la criminalité organisée : les signaux doivent remonter vers les cellules LCB-FT, pas seulement vers le SIU.

## 5. 🚪 Fraude en entrée en relation

- **Synthetic identities leave US lenders with $2.4 billion in exposure** — *Help Net Security (rapport TransUnion), 26 octobre 2026*
  https://www.helpnetsecurity.com/2026/10/26/transunion-synthetic-identity-fraud-risks-report/
  Le rapport TransUnion chiffre à 2,4 milliards de dollars l'exposition des prêteurs américains aux identités synthétiques à fin juin 2026, dont 1,5 Md$ en crédit auto, et montre que 81 % de la fraude digitale suspectée a lieu aux connexions et transactions. Les fraudeurs construisent des identités à partir de données réelles issues de fuites, qui passent les contrôles d'onboarding, puis s'en servent sur plusieurs services. Source étrangère assumée : aucune statistique nationale équivalente publiée ce mois.
  **Pourquoi c'est pertinent ?** L'identité synthétique qui « passe » l'onboarding puis circule entre services est exactement le scénario de la souscription montée pour frauder en assurance.
  *À surveiller* : score de fraîcheur des attributs d'identité (ancienneté des coordonnées, présence dans d'autres onboardings) comme signal de détection.

- **Fraude à l'ère de l'IA : l'angle mort des assureurs** — *Paperjam, 30 octobre 2026*
  https://paperjam.lu/article/fraude-a-lere-de-lia-langle-mort-des-assureurs
  Cette analyse luxembourgeoise (en français) décrit le risque structurant pour les assureurs : la fraude ne s'appuie plus sur du faux, mais sur la réutilisation de données d'identité réelles issues d'incidents cyber — souscription sur profils reconstruits, sinistres appuyés par des éléments plausibles mais falsifiés. Elle recommande de corréler les signaux faibles et d'intégrer la donnée cyber dans l'analyse du risque métier.
  **Pourquoi c'est pertinent ?** Il nomme le vrai angle mort du KYC assureur : distinguer le client légitime du fraudeur « bien informé » exige de croiser signaux comportementaux et contexte, pas seulement vérifier des pièces.

## 6. 🩺 Fraude à la santé

- **1 200 assurés ont acheté un faux arrêt maladie sur Snapchat : ce qu'ils doivent rembourser à la Sécu** — *JeChange, 16 octobre 2026*
  https://www.jechange.fr/assurance/mutuelle-sante/news/faux-arret-maladie-snapchat-1200-assures-rembourser-secu
  L'article détaille les conséquences annoncées par l'Assurance maladie aux 1 200 acheteurs du réseau de faux arrêts démantelé en mai 2026 par l'OCLTI (7 interpellations, 3,5 M€ détournés, identités de médecins usurpées) : remboursement de la totalité des indemnités perçues, pénalité pouvant atteindre trois fois le préjudice (quatre fois en bande organisée), poursuites pénales. Le montage : kit arrêt + fausse attestation de salaire contre reversement de 60 % des indemnités.
  **Pourquoi c'est pertinent ?** Il démontre que l'acheteur individuel est désormais systématiquement rattrapé : le message de dissuasion vers les assurés change de nature, et le remboursement total inclut la part reversée au réseau.

- **La fraude à l'Assurance maladie s'élève à 723 millions d'euros, la CPAM renforce ses dispositifs de contrôle** — *France 3 Grand Est, 5 mai 2026*
  https://france3-regions.franceinfo.fr/grand-est/meurthe-et-moselle/nancy/la-fraude-a-l-assurance-maladie-s-eleve-a-723-millions-d-euros-face-a-des-escroqueries-de-plus-en-plus-sophistiquees-la-cpam-renforce-ses-dispositifs-de-controle-3345814.html
  Reprise du bilan officiel de l'Assurance maladie : 723 M€ de fraudes détectées et stoppées en 2025 (+15 %), 286 M€ évités avant paiement, 1 700 agents dédiés. Répartition clé : les assurés concentrent 53 % des dossiers mais 16 % des montants (115 M€), quand les professionnels de santé pèsent 75 % des montants — centres de santé en tête (138 M€, +253 % sur un an), audioprothésistes (85 M€), transporteurs sanitaires (61 M€).
  **Pourquoi c'est pertinent ?** Cette asymétrie dossiers/montants dicte l'allocation des moyens : cibler les prescripteurs et structures plutôt que multiplier les contrôles assurés individuels.

## 7. 🧪 Divers — sujet émergent

- **Hunter Game 3 : 86 équipes et 344 participants pour le serious game anti-fraude de l'ALFA** — *ALFA, 13 octobre 2026*
  https://www.alfa.asso.fr/hunter-game-3/
  Du 5 au 9 octobre 2026, l'ALFA a réuni 86 équipes et 344 participants à son troisième Hunter Game, un serious game en format « Capture The Flag » mobilisant le renseignement d'origine source ouverte (ROSO/OSINT) sur une enquête réaliste de fraude à l'assurance. L'objectif affiché : renforcer les compétences OSINT des équipes, apprendre à distinguer l'information pertinente des pièges, et découvrir de nouveaux outils.
  **Pourquoi c'est pertinent ?** L'OSINT devient une compétence de base formalisée par l'agence sectorielle elle-même : c'est un signal d'institutionnalisation à intégrer dans les plans de formation des SIU.
  *À surveiller* : la transposition du format CTF interne à la montée en compétences d'équipes de gestion plutôt que de seules équipes investigation.

## Synthèse — 5 signaux faibles à surveiller

1. **Le glissement du faux document vers la fraude au processus complet** — des dossiers cohérents mêlant pièces vraies et déclarations trompeuses échappent aux contrôles pièce par pièce.
   https://www.tessi.eu/wp-content/uploads/2026/07/cp-fraude-documentaire-le-2e-rapport-de-lobservatoire-tessi-20260707.pdf
   https://paperjam.lu/article/fraude-a-lere-de-lia-langle-mort-des-assureurs
2. **L'IA générative dans les sinistres auto pousse vers l'authentification à la source** — photo géolocalisée prise en direct, import de fichiers bloqué : le standard de preuve du constat change.
   https://www.franceinfo.fr/economie/assurances-quand-l-ia-simule-des-accidents_8094263.html
   https://algopolis.eu/fr/article/19
3. **Le durcissement massif de l'arsenal sanctionnateur** — loi du 25 juin 2026 : pénalités à 300 % (400 % en bande organisée), quinze ans de réclusion pour les escroqueries en bande ; les assureurs peuvent aggraver leurs réclamations.
   https://www.economie.gouv.fr/actualites/fraudes-sociales-et-fiscales-une-loi-pour-mieux-les-detecter-et-lutter
   https://www.jechange.fr/assurance/mutuelle-sante/news/faux-arret-maladie-snapchat-1200-assures-rembourser-secu
4. **L'institutionnalisation de l'OSINT et du signalement citoyen** — serious game ALFA à 344 participants, listes noires ACPR-AMF mises à jour trimestriellement : les données ouvertes deviennent un outillage de premier niveau.
   https://www.alfa.asso.fr/hunter-game-3/
   https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0
5. **Les identités synthétiques construites sur des données réelles à l'entrée en relation** — 2,4 Md$ d'exposition bancaire aux États-Unis, souscription sur profils reconstruits en Europe : la frontière client légitime/fraudeur informé se brouille.
   https://www.helpnetsecurity.com/2026/10/26/transunion-synthetic-identity-fraud-risks-report/
   https://paperjam.lu/article/fraude-a-lere-de-lia-langle-mort-des-assureurs

---

*Méthode : sélection du 3 novembre 2026 sur fenêtre glissante d'un mois (octobre 2026), avec tolérance jusqu'à juillet 2025 pour les articles de référence (rapport Tessi du 7 juillet 2026, loi du 25 juin 2026, bilan Assurance maladie du 5 mai 2026, démantèlement Toulouse du 26 juin 2026, reportage franceinfo du 4 juillet 2026). Chaque date a été vérifiée sur la page source (format JJ/MM/AAAA). Sources écartées : blog de cabinet d'avocats (kohenavocats) au profit du texte de loi, communiqué d'éditeur (Extend Verify, Businesswire) et article JDN adossé à un baromètre de fournisseur, deuxième reprise du rapport ALFA (Le Figaro, La Tribune — une seule entrée via la synthèse JeChange d'octobre). Deux sources non françaises assumées (TransUnion/Help Net Security, Paperjam) faute d'équivalent national sur l'identité synthétique. Domaines consultés inaccessibles à l'automation (ACPR accessible ici, mais L'Argus de l'Assurance et Les Échos bloqués) : aucune date reconstituée n'a été nécessaire.*
