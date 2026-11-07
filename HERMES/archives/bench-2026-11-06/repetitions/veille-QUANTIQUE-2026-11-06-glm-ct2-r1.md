# Veille informatique quantique — semaine du 31 octobre au 7 novembre 2026

*Générée le 7 novembre 2026 par ORAC (Hermes, profil démo) — bac à sable de comparaison. Fenêtre : 7 jours. Dates de publication vérifiées sur chaque page source. Aucun site blacklisté cité. Une dépêche reprise = une seule entrée.*

## Synthèse — 5 signaux faibles à surveiller

1. **La course à la correction d'erreurs (QEC) devient un sport d'équipe HPC+QPU.** Le lancement de la plateforme de co-design IBM/ORNL/AMD — un processeur Nighthawk co-localisé avec le supercalculateur Umbra (GPU Instinct MI355X) — officialise le paradigme « quantum-centric supercomputing » : le décodage QEC en temps réel exige désormais une puissance classique dédiée. Implication DSI/RSSI : la planification d'un accès quantique à horizon 2028-2029 doit budgéter non pas un QPU isolé, mais un couplage QPU+HPC (latence, énergie, ordonnancement) — et les directions R&D doivent arbitrer tôt entre architectures compatibles avec leur parc HPC existant.
   Sources : https://newsroom.ibm.com/2026-11-05-oak-ridge-national-lab,-ibm,-and-amd-launch-new-co-design-platform-for-quantum-error-correction — https://www.ibm.com/quantum/blog/ornl-amd-error-correction-co-design-platform

2. **L'estimation de rupture de RSA-2048 par Alice & Bob (22 593 qubits physiques, 3,14 jours) raccourcit les horaires de migration PQC.** C'est une *estimation de ressources sur papier*, fondée sur des hypothèses matérielles non démontrées (temps de bit-flip ~10¹¹ ans), mais elle divise par ~40 le décompte de l'estimation de référence de Gidney (2025). Implication DSI/RSSI : les inventaires cryptographiques (CBOM) et les plans de migration vers ML-KEM/ML-DSA ne peuvent plus reposer sur un horizon « 2035 tranquille » ; chaque publication de ce type justifie l'accélération des échéances type NIST (2030/2031 pour les systèmes à forte valeur, cf. NISTIR 8547).
   Sources : https://alice-bob.com/blog/compiling-shors-algorithm-on-cat-qubits-22-593-qubits-to-break-rsa-2048-in-3-14-days/ — https://eprint.iacr.org/2026/2665 — https://www.nist.gov/news-events/news/2026/10/nist-report-provides-guidelines-transition-post-quantum-cryptography

3. **Les QPU entrent dans les budgets des « AI factories » européens.** Le contrat de 33 M€ d'IQM avec le LUMI AI Factory du CSC finlandais — première commande de sa plateforme Halocene à qubits logiques — signale un basculement : les centres de calcul souverains achètent des feuilles de route QEC, pas des machines actuelles. Implication direction R&D/DSI : surveiller les appels d'offres euroHPC à venir ; un fournisseur qui vend une « trajectoire qubits logiques » plutôt qu'un nombre de qubits physiques change la grammaire des cahiers des charges.
   Sources : https://www.sec.gov/Archives/edgar/data/2113060/000119312526448359/iqmx-ex99_1.htm — https://finance.yahoo.com/markets/stocks/articles/iqm-quantum-computers-q3-earnings-211440865.html

4. **La consolidation cyber-quantique s'accélère : IonQ absorbe un éditeur Zero Trust (Elisity, ~1,15 Md$ en actions).** Un pure player quantique rachète de la cybersécurité réseau classique pour empaqueter Zero Trust + PQC + QKD. Implication RSSI : le marché va voir émerger des « suites quantiques-sûres » intégrées ; anticiper les questions de dépendance éditoriale/référencement et vérifier qu'un cabinet Zero Trust acquis par un vendeur de QPU reste neutre sur l'architecture cible.
   Sources : https://thequantuminsider.com/2026/11/04/ionq-completes-acquisition-zero-trust-security-company-elisity/ — https://quantumcomputingreport.com/ionq-completes-1-15b-acquisition-of-elisity-to-integrate-zero-trust-with-quantum-security/

5. **La saison des résultats T3 révèle l'écart entre récits et cash.** IonQ (173,8 M$ de CA, x3,6, guidance relevée) et Quantinuum (9,1 M$ de CA, x2,3) racontent la même trajectoire « fault-tolerant 2029 », mais les revenus restent minuscules face aux valorisations, et Pasqal voit son CA reculer (3,3 M€, zéro vente de QPU) malgré 312,8 M€ de trésorerie. Implication direction R&D/achats : dans les due diligences, exiger le détail « revenus QPU vs services vs subventions » — le suivi de la *qualité* du carnet (IQM : 102,5 M€ de backlog dont un contrat QEC) est plus prédictif que les annonces de records.
   Sources : https://www.ionq.com/news — https://www.quantinuum.com/news/news — https://investors.pasqal.com/static-files/acbd7ab1-99e3-4286-bbfb-ba57e30b60c7

## Actualités

### 🇫🇷 France

- **Alice & Bob (avec Inria) : RSA-2048 « cassé » en théorie avec 22 593 qubits cat en 3,14 jours** — *Alice & Bob, 4 novembre 2026.* Compilation intégrale de l'algorithme de Shor sur l'architecture cat-qubit (codes LDPC-cat) : ~40× moins de qubits physiques que l'estimation de Gidney (Google, 2025) pour le même RSA-2048. **Jalon d'estimation, pas une démonstration** : le résultat suppose un temps de bit-flip de ~10¹¹ ans par qubit, non démontré sur du matériel réel ; avec un temps de bit-flip de l'ordre du siècle par qubit (hypothèse des auteurs, non démontrée), le scénario prudent ramène le calcul à ~3,5 jours — et le décompte de qubits reste théorique. Utile comme borne d'ingénierie pour la migration PQC, pas comme preuve de capacité.
  https://alice-bob.com/blog/compiling-shors-algorithm-on-cat-qubits-22-593-qubits-to-break-rsa-2048-in-3-14-days/

- **Pasqal : T3 2026 en repli, mais 312,8 M€ de cash et un carnet de 69,8 M€** — *Pasqal (investors.pasqal.com), 6 novembre 2026.* CA de 3,3 M€ (contre 5,7 M€ un an plus tôt), pénalisé par l'absence de vente de QPU ; les services QPU progressent de 53 % (3,1 M€), dont les premières heures consommées chez Aramco (QCaaS). Le « booked and awarded business » (69,8 M€) inclut subventions et crédits d'impôt — à lire comme une trajectoire, pas comme un backlog commercial pur.
  https://investors.pasqal.com/static-files/acbd7ab1-99e3-4286-bbfb-ba57e30b60c7

- **Quandela s'allie à l'université Kookmin (Corée) : hybridation HPC/QPU et formation** — *Quantum Zeitgeist, 4 novembre 2026.* Nouveau MoU en Corée du Sud (après les contacts évoqués avec Samsung, SK hynix, LG Innotek pour la fabrication de puces photoniques) : accès à Quandela Cloud pour la recherche et l'enseignement, travaux sur le couplage HPC-QPU. Stratégie claire de Quandela : verrouiller l'accès à une filière de fabrication asiatique pour industrialiser ses QPU photoniques.
  https://quantumzeitgeist.com/quandela-kookmin-university-partnership-quantum-research/

- **Multiverse Computing s'associe à YellowDog.ai pour du calcul IA européen** — *Quantum Zeitgeist, 3 novembre 2026.* L'éditeur espagnol de logiciels (compression de modèles, optimisation inspirée du quantique) s'appuie sur l'orchestrateur YellowDog pour distribuer des charges de calcul IA au sein de l'UE — signal de l'industrialisation côté logiciel plus que du matériel.
  https://quantumzeitgeist.com/2026/11/page/2/

### 🌍 Europe

- **Quint Computing (Erlangen, Allemagne) : 9,1 M€ en seed — record allemand du segment** — *Quantonation, 3 novembre 2026.* Tour mené par Vsquared avec Quantonation, Nucleus, Faber, Vanagon, ZOHO.VC et Mikko Möttönen (cofondateur d'IQM), plus une subvention EIC Pathfinder de 2,2 M€. Architecture supraconductrice visant à corriger les erreurs au niveau matériel (stabilisation électrique continue) pour réduire d'un facteur ~100 le surcoût de la QEC. **R&D prometteuse, aucun résultat matériel publié** : à suivre comme pari d'architecture, pas comme jalon validé.
  https://www.quantonation.com/news/quantonation-backs-quint-computing-in-e9-1-million-funding-round

- **IQM : T3 solide, 33 M€ du CSC finlandais pour la première plateforme QEC Halocene** — *IQM Quantum Computers (dépôt SEC 6-K), 5 novembre 2026.* 8,9 M€ de CA au T3 (+51 %), 42,2 M€ de nouvelles commandes, backlog porté à 102,5 M€ (+52 % depuis janvier). Le contrat LUMI AI Factory (CSC) doit déboucher sur ce qui est présenté comme le premier ordinateur quantique supraconducteur européen à qubits logiques — objectif de feuille de route, pas encore un livrable. Première vente en Amérique du Sud (Eldorado, Brésil). Pertes opérationnelles lourdes (171 M€ au T3) : le pari reste capitalistique.
  https://www.sec.gov/Archives/edgar/data/2113060/000119312526448359/iqmx-ex99_1.htm

### 🌐 Monde

- **IBM dévoile son System Two le plus avancé à Chicago (puce Nighthawk)** — *IBM Newsroom, 6 novembre 2026.* Premier ordinateur quantique d'IBM dans l'Illinois, hébergé par l'université de Chicago (Hyde Park Labs), futur anchor de l'Illinois Quantum and Microelectronics Park. **Jalon de déploiement, pas de fault-tolerance** : l'annonce porte sur l'infrastructure et l'écosystème (NQAC, Deloitte, AbbVie, EPRI), pas sur une nouvelle démonstration de capacité.
  https://newsroom.ibm.com/2026-11-06-ibm-unveils-its-most-advanced-quantum-computer-in-chicago,-marking-a-milestone-for-illinoiss-quantum-future

- **IBM + Oak Ridge + AMD : plateforme de co-design pour la correction d'erreurs quantiques** — *IBM Newsroom, 5 novembre 2026.* Co-localisation de processeurs Nighthawk (dont le r2, 120 qubits) avec le HPC Umbra (AMD Instinct MI355X + EPYC) à Poughkeepsie, raccordé à l'écosystème d'Oak Ridge ; s'inscrit dans la cible DOE « Quantum Genesis » : 100 qubits logiques / 100 000 opérations « dures » fin 2028. IBM annonce ses propres expériences à ~70 qubits logiques et 438 opérations dures — à suivre au Quantum Developer Conference du 11-13 novembre.
  https://newsroom.ibm.com/2026-11-05-oak-ridge-national-lab,-ibm,-and-amd-launch-new-co-design-platform-for-quantum-error-correction

- **Quantinuum : T3 et feuille de route « Nexus » pour l'ère fault-tolerante** — *Quantinuum, 5 novembre 2026.* CA de 9,1 M$ au T3 (+233 % sur un an, mais 9 mois en retrait de 6,8 %) et relève de la guidance annuelle à 31-34 M$. Lancement de Nexus, plateforme développeurs annoncée comme la première pensée pour l'ère fault-tolerante. Contexte : après le record QEC annoncé le 19 octobre (fidélité logique 99,9995 % sur Helios, code couleur — dix fois mieux que son propre record de septembre), la société cible Sol en 2027 et Apollo (fault-tolerant) en 2029.
  https://www.quantinuum.com/news/news

- **IonQ : record de CA au T3 (173,8 M$, +336 %) et guidance relevée à 505-515 M$** — *IonQ Newsroom, 5 novembre 2026.* Croissance tirée par la consolidation (SkyWater, acquisitions) et un carnet de 1,2 Md$ ; le segment Plateforme pèse 90,3 M$. Trois annonces additionnelles dans la semaine : partenariat QuantumCT (Connecticut, >150 h de temps cloud), fin de l'acquisition d'Elisity (4 nov.), financement de suivi de 7,5 M$ de l'AFRL pour le réseau quantique.
  https://www.ionq.com/news

- **IonQ finalise l'acquisition d'Elisity (Zero Trust) pour ~1,15 Md$ en actions** — *The Quantum Insider, 4 novembre 2026.* L'éditeur de microsegmentation réseau identitaire complète la feuille de route sécurité d'IonQ (PQC + QKD), avec jusqu'à 150 M$ d'earn-out sur jalons de revenus à janvier 2028. Voir signal faible n° 4.
  https://thequantuminsider.com/2026/11/04/ionq-completes-acquisition-zero-trust-security-company-elisity/

- **NIST : feuille de route officielle de transition post-quantique (NISTIR 8547)** — *NIST, publié le 27 octobre 2026, page mise à jour le 2 novembre 2026 (fin de fenêtre).* Le rapport identifie les algorithmes vulnérables à abandonner, les remplacements et le calendrier : 2030 pour l'établissement de clés et 2031 pour les signatures sur les systèmes fédéraux à forte valeur (EO 14412), 2035 en cible générale (NSM-10). Référence directe pour tout plan de migration PQC d'entreprise.
  https://www.nist.gov/news-events/news/2026/10/nist-report-provides-guidelines-transition-post-quantum-cryptography

## 🔮 Prospective

- **Court terme (6-12 mois)** : le Quantum Developer Conference d'IBM (11-13 novembre 2026) et la publication de la feuille de route Kookaburra/Cockatoo diront si l'objectif DOE « 100 qubits logiques / 100 000 opérations dures d'ici fin 2028 » est crédible. À surveiller aussi : l'acceptation client des deux premiers systèmes IQM 150 qubits (condition de la guidance 2026) et la nomination des finalistes PROQCIMA phase 2 en France.
- **Moyen terme (2-4 ans)** : Généralisation du modèle « AI factory + QPU » inauguré par le CSC/LUMI — les supercalculateurs européens coupleront des QPU à qubits logiques sous contrat de feuille de route. En parallèle, la pression réglementaire PQC (échéances NIST 2030/2031, équivalents européens) transformera l'inventaire cryptographique en projet budgété, pas en intention.
- **Long terme (5-10 ans)** : si les hypothèses d'Alice & Bob (suppression du bit-flip au niveau matériel) sont un jour démontrées sur du silicium réel, l'échelle d'une menace opérationnelle sur RSA-2048 passerait de « 2035+ incertain » à « ingénierie, fin des années 2030 » ; dans le cas inverse, les architectures à codes de surface (IBM, Google) restent la voie conservative. Les deux trajectoires convergent vers la même conclusion DSI : migrer maintenant.

---
*Contrôle qualité : 12 articles, dates vérifiées sur les pages sources (pas de date de sidebar) ; la station optique ESA/QKD de Windhof a été écartée faute de date de publication fiable (26/07/2026 et 15/04/2026 selon les pages ESA). Aucun site blacklisté utilisé. Rien d'autre n'a été écrit que les fichiers .md et .html de cette veille.*
