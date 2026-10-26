# Veille Informatique Quantique — 5 octobre 2026

## Synthèse — 5 signaux faibles à surveiller

1. Bascule des métriques d'évaluation quantique. Le DOE abandonne le comptage de qubits au profit de l'utilité scientifique démontrée (chimie, matériaux, fusion) pour 2028. Implication : les DSI doivent exiger des preuves d'utilité applicative dans les roadmaps fournisseurs, et l'UE (EuroHPC/Quantum Flagship) pourrait s'aligner.
2. Industrialisation et financiarisation du quantique français. Pasqal coté au Nasdaq quitte le volet défense LSQUARE/PROQCIMA pour se recentrer sur le civil et le FTQC ; IQM est couvert en bourse ; D-Wave s'associe à une business school sur la supply chain. Implication : le quantique passe des programmes publics aux cas d'usage commerciaux — les industriels doivent identifier leurs premiers ateliers hybrides QPU/HPC.
3. La correction d'erreurs devient le centre de gravité produit. Qiskit 2.6 oriente ses pipelines vers la tolérance aux pannes, D-Wave ouvre un simulateur gate-model error-aware avec Jülich, et les travaux théoriques (injection LDPC, codes pseudo-aléatoires) comblent les trous de la stack. Implication : la fenêtre « harvest now, decrypt later » se précise à l'horizon 2028-2030.
4. Pression régulatrice post-quantique croissante en Europe. Autorités financières UE (migration PQC d'ici fin 2026, actifs critiques vers 2030), Cloudflare CA post-quantique, ANSSI en fil rouge. Implication : RSSI — lancer sans attendre l'inventaire cryptographique, le plan de migration PKI et les tests de protocoles hybrides (ML-KEM/ML-DSA).
5. La simulation bat l'optimisation comme premier moteur de valeur. Katzgraber (55North), le programme NEDO anticancer et l'étude BCG climat convergent : la valeur à court/moyen terme est dans la simulation moléculaire et matériaux, pas dans l'optimisation générique. Implication : directions R&D — prioriser les partenariats orientés simulation (chimie, batteries, pharma) plutôt que les POOC sur-glorifiés.

## Actualités

1. **Actualités quantiques de septembre 2026 (podcast Quantum #84)**
   Rétrospective mensuelle de l'écosystème quantique français et européen de septembre : PEPR Quantique Synergy 2026 (9-11 sept), introduction en bourse de Pasqal au Nasdaq et pivot vers le civil après son retrait du programme de défense LSQUARE/PROQCIMA, vente d'un ordinateur quantique par Quandela au Vietnam, progrès de Quobly sur les qubits au silicium avec STMicroelectronics et CEA-Leti, projet de logiciel souverain Aliquante (Thales, Bull, CEA) et partenariat Alice & Bob-CEA.  Note de la veille : seuls 2 articles de cette section datent des 48 dernières heures ; les 4 suivants complètent avec les plus récents des 7 derniers jours.

2. **On a visité l'usine de Pasqal, le champion français de l'ordinateur quantique**
   Reportage dans l'usine de Pasqal à Palaiseau : processeurs quantiques à atomes neutres (rubidium piégé par lasers, cryostats, ultra-vide). Premier champion quantique français coté au Nasdaq (PSQL, août 2026, ~360 M$ levés, valorisation ~2 Md$), la société affiche un chiffre d'affaires S1 2026 de 4,9 M€ (+14 %) pour une perte nette de 53,2 M€, avec 312,9 M€ de trésorerie et une capacité de production de 13 machines/an ; une double cotation Euronext Paris est envisagée en 2027.

3. **TD Cowen initie la couverture d'IQM Quantum Computers avec un avis Achat**
   TD Cowen lance la couverture boursière d'IQM (IQMX, Finlande) avec un rating Achat, saluant son leadership mondial sur les ordinateurs quantiques on-premise livrés aux clients, sa feuille de route haute fidélité et un TCAC projeté supérieur à 60 % (plus de 150 M$ de revenus visés d'ici 2028). Le groupe multiplie les contrats (Brésil, Japon, LUMI) et annonce un plan d'intéressement actions (~18,2 M€).

4. **Alice & Bob et l'ENS Lyon stabilisent les qubits de chat par polarisation continue (DC)**
   Démonstration expérimentale de stabilisation de qubits de chat par une simple polarisation continue (~1 µV) sur un SQUID, remplaçant les pompes micro-ondes : dissipation multi-photons (1, 2 et 4 photons), taux d'échange jusqu'à 18,5 MHz, moins de chaleur et des puces plus compactes. Confirmé par tomographie de Wigner : une étape vers des qubits cat plus fiables et le calcul tolérant aux fautes.

5. **L'UE alloue 47,5 M€ au Quantum Internet Alliance pour un prototype d'internet quantique full-stack**
   La Commission européenne a accordé 47,5 M€ au consortium Quantum Internet Alliance (plus de 50 institutions) pour sa phase SGA 2 de 42 mois : un prototype complet et programmable d'internet quantique, incluant l'interconnexion de deux réseaux métropolitains via fibre longue distance et répéteurs quantiques. Kick-off à Lisbonne les 30 septembre-1er octobre avec plus de 100 chercheurs. Avancée majeure pour la souveraineté européenne en communication quantique, en lien avec EuroQCI.

6. **Pasqal : évolution de son cadre de collaboration avec les autorités publiques françaises**
   Pasqal (NASDAQ: PSQL) annonce la fin de sa participation au programme de défense LSQUARE (volet du PROQCIMA piloté par la DGA) après avoir atteint tous les objectifs de la première phase. L'entreprise se recentre sur le calcul quantique commercial et la R&D fault-tolerant (FTQC) à atomes neutres. Un rebalancement notable pour la souveraineté quantique française, en cohérence avec l'accélération France 2030 (1 Md€ supplémentaires en mai 2026, cible de 1024 qubits logiques d'ici 2032).

7. **Le DOE publie une feuille de route quantique nationale fixant des jalons de tolérance aux pannes pour 2028**
   Le rapport « Path to an Integrated Quantum Future » vise un calcul quantique corrigé d'erreurs scientifiquement pertinent dès 2028, avec un changement de métrique majeur : abandon du simple comptage de qubits physiques au profit de l'utilité scientifique démontrée (chimie quantique, médicaments, matériaux, fusion). Trois phases pour intégrer les QPU comme coprocesseurs des infrastructures HPC/IA. Transposabilité européenne : modèle directement opposable aux feuilles de route Quantum Flagship/EuroHPC.

8. **D-Wave lance le programme bêta de son simulateur gate-model, orienté correction d'erreurs**
   D-Wave (NASDAQ: QBTS) ouvre l'accès anticipé à son simulateur quantique gate-model, bâti sur sa technologie supraconductrice dual-rail conçue pour détecter les erreurs et réaliser une correction à surcoût matériel réduit. Bêta-testeurs : BBVA (finance), FirstQFM, Florida Atlantic University et le centre de supercalcul de Jülich (Allemagne). Implication directe du JSC dans la co-développement error-aware et pont avec les infrastructures HPC européennes (Jupiter).

9. **Helmut Katzgraber (55North) : la simulation de matériaux battra l'optimisation à court terme**
   Entretien avec l'ex-responsable quantique d'AWS, désormais VC au fonds danois 55North : les applications les plus prometteuses à court/moyen terme sont la simulation de matériaux, de chimie et de pharma, pas l'optimisation. Il aborde la compétitivité européenne et les modèles de déploiement cloud vs on-premise. Lecture stratégique pour orienter la R&D et le financement du quantique dans l'UE vers la simulation.

10. **Trois records mondiaux d'atomes de Rydberg circulaires à température ambiante (Stuttgart)**
   Trois records internationaux pour les atomes de Rydberg circulaires : durée de vie (≈11 ms, ×20 vs état de l'art), plus grande orbite contrôlée (n=103, ~1,1 µm) et temps de stockage en pinces optiques (133 ms), le tout à température ambiante sans cryogénie grâce à une suppression de Purcell du rayonnement de corps noir. Publié dans Nature Communications (preprint arXiv:2510.27471). Percée allemande qui renforce la plateforme atomes neutres concurrente de QuEra/Pasqal.

11. **SQC et Schneider Electric passent la prévision énergétique quantique-hybride en phase 2 (A$3,6 M)**
   SQC et Schneider Electric décrochent A$3,6 M en phase 2 du programme australien Critical Technologies Challenge pour déployer leur système Watermelon™ — générateur de caractéristiques quantiques sur QPU phosphore-dans-silicon — dans des réseaux d'énergie distribuée avec UNSW Sydney. Résultats phase 1 : +20 % de précision moyenne (jusqu'à +41 %) sur 12 mois. L'acteur français Schneider valide un cas d'usage répliquable sur le réseau électrique européen.

12. **Cloudflare annonce une autorité de certification publique pour le web post-quantique [7 derniers jours]**
   Cloudflare devient une autorité de certification publique ouverte, avec certificats traditionnels et certificats post-quantiques Merkle Tree (MTC) — production visée au T1 2027 — et acquisition de matéri de racine GlobalSign pour une reconnaissance immédiate sur le web legacy. Contexte : migration vers les algorithmes PQC du NIST avant l'arrivée d'ordinateurs quantiques capables de casser RSA/ECC. Enjeu majeur pour la souveraineté PKI européenne et la conformité eIDAS/EUCS.

13. **Alice & Bob et l'ENS Lyon : stabilisation des qubits chat par polarisation DC [7 derniers jours]**
   Stabilisation de qubits chat supraconducteurs via une simple polarisation en tension continue (~1,1 µV) appliquée à un SQUID, au lieu d'une pompe micro-ondes paramétrique : échanges à deux photons d'environ 3 MHz (jusqu'à 18,5 MHz), processus multi-photons sélectifs (1-, 2-, 4-photons) et termes Kerr parasites dynamiquement moyennés. Simplifie le hardware et réduit la dissipation thermique.  ⚠️ Preprint arXiv:2608.31154 non évalué par les pairs.

14. **Sortie de Qiskit 2.6.0rc1 : API C, tolérance aux pannes et performances**
   IBM a publié la première release candidate du jalon Qiskit 2.6 (gel des fonctionnalités le 3 septembre, release stable attendue vers le 15 octobre 2026). Priorités : enrichissements de l'API C, pipelines orientés tolérance aux pannes, indépendance vis-à-vis de Python, performances et Backend V3. Pré-release à réserver aux tests ; la branche stable reste la 2.5.x.

15. **Injection à overhead constant dans les codes quantiques : une première théorique de Berkeley**
   Louis Golowich et Venkatesan Guruswami proposent le premier schéma tolérant aux pannes pour injecter et éjecter des états quantiques dans des codes correcteurs d'erreurs à taux constant (overhead constant en espace et en temps), à partir de produits hypergraphes de codes LDPC classiques, sous bruit localement stochastique. Résultat clé pour connecter des qubits physiques « nus » aux codes LDPC sans explosion des ressources.  ⚠️ Preprint arXiv non évalué par les pairs ; travail théorique sans démonstration matérielle.

16. **Codes quantiques pseudo-aléatoires : correction d'erreurs + sécurité cryptographique (Hon Hai / Kyoto)**
   Min-Hsiu Hsieh et Shogo Yamada définissent les « quantum pseudorandom error-correcting codes » (QPRC), analogues quantiques des codes pseudo-aléatoires classiques : sous l'hypothèse de dureté du LPN quantique, des codes isométriques pseudo-aléatoires qui corrigent un bruit local allant jusqu'à o(n·log log n / log n) tout en paraissant aléatoires — utile pour protéger des données quantiques en mémoire ou en communication.  ⚠️ Preprint arXiv non évalué par les pairs ; contribution théorique.

17. **Le DOE publie sa feuille de route : ordinateur quantique corrigé d'erreurs scientifiquement pertinent d'ici 2028**
   Feuille de route en trois phases visant une capacité de calcul quantique corrigée d'erreurs et scientifiquement pertinente dès 2028, avec des cibles indicatives de 50 à plus de 100 qubits logiques et une intégration HPC/IA. Ce cadre guide le Quantum Genesis Q Competition du DOE (jusqu'à 215 M$) et déplace l'évaluation du progrès du simple compte de qubits physiques vers l'utilité scientifique démontrée.

18. **Photons quasi indiscernables à 90 % via cascade biexcitonique contrôlée par cavité (Paderborn / Bâle / Bochum)**
   Génération de photons uniques et de paires de photons quasi indiscernables à partir de boîtes quantiques semi-conductrices en contrôlant la décroissance biexcitonique dans un résonateur optique (effet Purcell) : visibilité d'interférence à deux photons de 90 ± 2 % (photons XX, ~80 % pour X), contre ~60 % sans cavité. Directement pertinent pour les calculateurs et réseaux quantiques photoniques. ✅ Évalué par les pairs (PRL 2026).

19. **D-Wave s'associe à l'Université de l'Arkansas pour une initiative quantique dédiée à la supply chain**
   Annoncée lors du salon CSCMP EDGE 2026, la collaboration entre D-Wave et le Supply Chain Management Research Center de Walton College crée un fonds de recherche dédié à l'optimisation quantique des chaînes d'approvisionnement : routage de transport, conception de réseaux logistiques, allocation d'inventaires, ordonnancement et résilience. D-Wave rejoint le programme partenaires du SCMRC (+25 entreprises) : l'optimisation hybride quantique-classique sort des seuls pilotes.

20. **Katzgraber (55North) : la simulation de matériaux bat l'optimisation à court terme**
   Entretien avec Helmut Katzgraber, ex-responsable quantique d'AWS, désormais associé du fonds 55North : les applications les plus prometteuses à court et moyen terme relèvent de la simulation quantique de matériaux, de chimie et de pharma. Il plaide pour des produits autour de cas d'usage étroits mais à forte valeur (ex. matériaux fortement corrélés pour les batteries) et analyse la compétitivité européenne et les modèles de déploiement cloud/on-premise.

21. **Le quantique pourrait réduire les émissions industrielles sans empreinte énergétique de niveau IA, selon le BCG**
   Une étude BCG estime que les technologies quantiques pourraient éviter 3 à 7 milliards de tonnes d'émissions annuelles via les batteries, la capture de carbone et la chimie industrielle — près d'un dixième des émissions mondiales au point médian. Seuls 10 à 15 % de ce potentiel seraient réalisés d'ici 2040 (cycles de remplacement des équipements industriels longs), pour des solutions commercialement viables vers 2035. L'empreinte énergétique du quantique resterait marginale (~0,09 Gt en 2040), contrairement à l'IA.

22. **NEC, Taiho Pharmaceutical et Waseda sélectionnés par NEDO pour une immunothérapie anticancéreuse assistée du quantique**
   Un consortium NEC / Taiho Pharmaceutical / Japanese Foundation for Cancer Research / AIST / Waseda est retenu dans le programme de démonstration à grande échelle de NEDO pour construire une plateforme de calcul combinant quantique, IA et immunologie afin de concevoir et valider des candidats néoantigènes pour l'immunothérapie du cancer. Le calcul quantique passe de la preuve de concept moléculaire à la démonstration industrielle dans le pipeline de conception de médicaments.

23. **QML pour la sécurité réseau : noyaux quantiques compétitifs mais pas d'avantage uniforme ⚠️ preprint arXiv**
   Évaluation systématique des QSVM à noyaux quantiques sur des tâches réelles de cybersécurité (KDD Cup 1999, CICIDS2017, BoT-IoT) : les noyaux quantiques égalent ou dépassent les baselines classiques dans certains cas, mais restent inférieurs aux kernels RBF dans d'autres. À court terme, le QML doit être traité comme une alternative dépendante du jeu de données, pas comme un remplacement supérieur. Les auteurs proposent à plus long terme un avantage mémoire via le « quantum oracle sketching » (QOS) pour la classification en flux.

24. **L'UE met en garde : le Q-Day pourrait arriver avant toute viabilité commerciale du quantique [hors fenêtre — 24 sept.]**
   Dans son évaluation automnale des risques, le comité conjoint des trois autorités européennes de supervision financière avertit qu'un ordinateur quantique capable de casser la cryptographie pourrait exister avant toute application commerciale rentable du quantique. Le rapport souligne le risque « harvest now, decrypt later » et recommande d'adopter une stratégie de migration post-quantique (ML-KEM, ML-DSA, SLH-DSA) d'ici fin 2026, les actifs à haut risque devant être migrés vers 2030.
