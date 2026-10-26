# Veille Informatique Quantique — 26 octobre 2026

## Synthèse — 5 signaux faibles à surveiller

1. La migration post-quantique bascule de la doctrine au déploiement produit. Cloudflare (GeoKey ML-KEM), l'appel du G7, la pression ONCD/CISA et la position des quatre agences européennes (QKD non mature, PQC prioritaire) convergent. Implication RSSI : l'inventaire cryptographique devient une échéance réglementaire 2030/2035, à lancer maintenant — et la QKD ne doit pas être traitée comme une alternative de production.
2. La fidélité logique devient le terrain de records qui compte, plus le nombre de qubits. Quantinuum (99,9995 %), SEEQC (décodage QEC −50 %), Alice & Bob (première porte non-Clifford sur cat-qubits) : la pile fault-tolerante se verticalise (hardware + décodeur + orchestration). Implication DSI/R&D : évaluer les fournisseurs sur leur feuille de route QEC et leurs jalons vérifiés, pas sur leur décompte de qubits.
3. Le couplage HPC-quantique souverain se construit en Europe cette semaine. Quobly/SiPearl, record de simulation NVIDIA sur JUPITER (Jülich), plateforme métrologique MetriQs-France, démonstrateur NVQLink de Quandela : l'Europe investit dans l'hybride souverain. Implication directions R&D : les architectures hybrides GPU-QPU seront le point d'entrée industriel du quantique bien avant la fault-tolerance complète.
4. Le financement du quantique entre dans l'ère de la reddition de comptes. Enquête d'actionnaires sur Pasqal après sa sortie de PROQCIMA, valorisations indexées sur des multiples de revenus 2030-2035 (Evercore) : les démos ne suffisent plus, la consolidation est anticipée. Implication directions stratégiques : sécuriser les partenaires quantiques par des engagements contractuels multi-années, pas par la seule promesse technologique.
5. La géographie du quantique s'élargit par les déploiements nationaux et l'export. Madrid (Telefónica/IQM), Vietnam (Quandela/Quanova), structuration Benelux-QCI d'EuroQCI : les écosystèmes émergents se dotalent de QPU via des partenariats croisés. Implication DSI : cartographier les offres d'accès cloud souveraines (Espagne, Italie, Asie) comme alternatives ou compléments aux plateformes US.

## Actualités

1. **Telefónica et IQM installent le premier ordinateur quantique de Madrid à l'Université polytechnique**
   Telefónica et l'européen IQM déploieront avant fin 2026 un ordinateur quantique IQM Spark (5 qubits supraconducteurs) sur site à l'Universidad Politécnica de Madrid : premier système quantique de la Communauté de Madrid et troisième en Espagne via leur partenariat. Ouvert aux universités, hôpitaux, centres de recherche et startups pour tester des algorithmes et des cas d'usage industriels, il renforce l'écosystème quantique ibérique et européen.

2. **QKD vs PQC : quatre agences européennes (dont l'ANSSI) priorisent le post-quantique**
   Analyse des positions convergentes de quatre agences européennes de cybersécurité (ANSSI en France, BSI en Allemagne, Pays-Bas, Suède) qui jugent la distribution de clés quantiques (QKD) pas assez mature pour un déploiement de production et privilégient la migration vers la cryptographie post-quantique, avec des échéances 2030 pour les systèmes à haut risque et 2035 pour le reste. Les projets EuroQCI sont repositionnés comme démonstrateurs plutôt qu'infrastructure opérationnelle. Directement utile pour les feuilles de route conformité/PQC des acteurs français.

3. **Pasqal sous le coup d'une enquête d'actionnaires après sa sortie du programme PROQCIMA**
   Le cabinet Pomerantz annonce une enquête sur d'éventuelles fraudes aux valeurs mobilières visant Pasqal (cotée à New York), après son communiqué du 28 septembre 2026 mettant fin à sa participation au programme français LSQUARE/PROQCIMA — annonce qui avait fait chuter le titre de 8,36 %. Un épisode qui illustre la tension entre cotation internationale et programmes souverains français pour la pépite d'atomes neutres.

4. **EuroQCI : QDNL rassemble les partenaires Benelux-QCI pour structurer les priorités QKD**
   Le 22 octobre à Utrecht, QDNL a réuni les partenaires Benelux-QCI (Pays-Bas, Belgique, Luxembourg, Grèce) autour des priorités QKD d'EuroQCI : montée en compétences, engagement des utilisateurs finaux, démonstrateurs et standards européens, avec un focus sur les fibres transfrontalières et la gestion de clés open source. L'infrastructure européenne de communication quantique passe des pilotes à une structuration par blocs régionaux — un modèle suivi de près par la France.

5. **Marché du quantique : les valorisations dépendront des multiples de revenus 2030 et de la consolidation (Evercore)**
   Entretien avec Mehmet Sanliol (Evercore) sur la valorisation des sociétés quantiques cotées, désormais indexée sur des multiples de revenus projetés 2030-2035, le rôle de la consolidation dans un secteur où les démos seules ne suffisent plus, et les parcours d'introduction en Bourse (IPO/SPAC). Éclairage utile pour situer la valorisation des acteurs européens (Pasqal cotée à New York, IQM…) et le risque de concentration du marché.

6. **Quobly et SiPearl s'allient sur le calcul quantique-HPC souverain européen**
   Les Français Quobly (qubits de spin silicium) et SiPearl (processeur HPC souverain Rhea1) ont signé un protocole d'accord le 23 octobre pour intégrer les serveurs SiPearl aux systèmes quantiques de Quobly et bâtir des architectures hybrides HPC-quantique européennes souveraines. Un couplage concret entre la feuille de route processeur européen et l'industrie quantique tricolore.

7. **La plateforme de mesure dédiée au quantique MetriQs-France est opérationnelle (complément fenêtre 7 jours)**
   La plateforme MetriQs-France, dotée de 13 M€ via France 2030, a été inaugurée à Trappes : elle donne à la France des instruments de mesure de référence pour la qualité des qubits et des technologies quantiques, en collaboration avec le CEA, le CNRS, les startups Alice & Bob et C12 ainsi que Thales. Maillon clé de la souveraineté métrologique de l'écosystème quantique français.

8. **Alice & Bob livre les premiers résultats de la Phase 1 du programme PROQCIMA (complément fenêtre 7 jours)**
   Alice & Bob publie les résultats de la Phase 1 de PROQCIMA (cadre d'achat de la stratégie quantique française liée à France 2030, qui réunit aussi Pasqal, Quandela, Quobly et C12, objectif : prototypes à 1 000 qubits logiques d'ici 2032) : trois démonstrateurs cat-qubit opérationnels (deux puces 6 qubits, une 12 qubits), portes CNOT à bruit biaisé, cycles de code de répétition et première porte non-Clifford sur qubits chat. Taux d'erreur logique encore au-dessus du seuil, avec un jumeau numérique identifiant les pistes d'amélioration.

9. **ONCD, CISA : les agences fédérales appelées à prioriser la transition post-quantique**
   Les responsables de l'ONCD et de la CISA exhortent les agences fédérales américaines à prioriser la transition vers les algorithmes post-quantiques du NIST, face au risque d'ordinateurs quantiques capables de casser la cryptographie actuelle. Pertinent pour les organisations européennes exposées aux échanges avec les administrations américaines : la dynamique de migration s'accélère à l'approche des échéances 2030-2035.

10. **G7 : les agences cyber appellent à une planification immédiate de la migration post-quantique**
   Le groupe de travail cyber du G7 (incluant France, Allemagne, Italie et l'UE) appelle à une planification immédiate de la migration depuis la cryptographie à clé publique vulnérable au quantique, en s'appuyant sur la RFC 10024 de l'IETF pour le TLS hybride et les standards NIST. Message direct pour la souveraineté numérique européenne et les opérateurs d'importance vitale.

11. **Arqit investit dans Sirius pour le réseau quantum-safe tactique après sa sélection OTAN**
   Arqit (Royaume-Uni), sélectionné sur un contrat de l'OTAN, investit dans Sirius Computer pour fournir du chiffrement quantum-safe aux communications militaires tactiques sans refonte matérielle. Première application défense d'envergure de la cryptographie post-quantique en Europe, au moment où les inquiétudes autour du « harvest now, decrypt later » montent dans les appareils de sécurité occidentaux.

12. **Quandela et Quanova s'associent pour déployer le premier ordinateur quantique du Vietnam**
   Quanova a retenu le système photonique MosaiQ de la française Quandela pour un programme de recherche et d'enseignement à l'université Quang Trung (soutenu par Nam A Bank) : premier ordinateur quantique du Vietnam. Première exportation d'un QPU français en Asie du Sud-Est — la filière photonique française se positionne sur les marchés émergents, utile à la lecture de la stratégie internationale des acteurs tricolores.

13. **Google Quantum AI lance une compétition Kaggle à 150 000 $ pour compresser des circuits quantiques tolérants aux fautes avec des agents IA**
   Compétition Kaggle (du 22 octobre 2026 au 20 janvier 2027) : utiliser des agents d'IA pour compresser des circuits quantiques tolérants aux fautes, « kickmix » et vérifiables classiquement, au service d'applications en énergie de fusion, optimisation et chimie quantique. Illustration de la convergence IA/quantique au cœur de la feuille de route de correction d'erreurs de Google.

14. **Quantinuum : fidélité logique record de 99,9995 % sur Helios (complément fenêtre 7 jours)**
   Quantinuum annonce un record mondial de fidélité logique de 99,9995 % sur son système à ions piégés Helios (code couleur, distance 7, erreur logique de 5×10⁻⁶), soit 10× mieux que son propre record de septembre et ~100× au-delà des meilleures plateformes d'autres modalités, avec suppression d'erreur 12× par incrément de distance. Trajectoire revendiquée vers son ordinateur tolérant aux fautes Apollo en 2029 ; la communauté y lit aussi une accélération potentielle de l'échéance Q-Day (résultat fabricant, non encore publié en revue).

15. **Certification device-independent de fermions de Majorana**
   Papier théorique : de nouvelles inégalités de Bell généralisées permettent une certification device-independent de fermions de Majorana (comme générateurs d'algèbre de Clifford multi-qubits), avec une nouvelle équivalence pour le self-testing. Pertinent pour valider les plateformes topologiques type Majorana sans faire confiance au device. Peer-reviewed (npj QI).

16. **Comment les réfrigérateurs à dilution maintiennent les ordinateurs quantiques en fonctionnement**
   Article de fond sur la chaîne cryogénique des ordinateurs quantiques : systèmes modulaires IBM descendant sous 15 mK, et verrou principal du scaling — la chaleur injectée par le câblage de contrôle à mesure que le nombre de qubits augmente. Bonne synthèse du goulot d'étranglement hardware cryogénique actuel.

17. **NVIDIA franchit un record de simulation quantique tolérante aux fautes à 104 qubits sur le supercalculateur européen JUPITER**
   NVIDIA a simulé un calcul quantique tolérant aux fautes à l'échelle de 104 qubits sur JUPITER (centre de supercalcul de Jülich, Allemagne) avec CUDA-Q et cuQuantum, sous bruit réaliste, validant des techniques de magic state cultivation qui pourraient réduire de ~90 % le nombre de qubits physiques requis. Premier record de ce type établi sur un supercalculateur européen — coopération UE/industrie à suivre.

18. **SEEQC et NVIDIA : −50 % de latence de décodage QEC via un pré-décodeur numérique sur puce**
   SEEQC annonce l'intégration de son pré-décodeur chip-based avec les modèles Ising de NVIDIA via NVQLink : réduction d'environ 50 % de la latence de décodage QEC et des taux d'erreurs logiques, en simulation.  ⚠️ Annonce fabricant, résultats simulés, non vérifiés par les pairs ; à suivre sur données réelles.

19. **Quandela démontre une architecture hybride photonique GPU-QPU en direct via NVQLink (GTC Berlin)**
   Quandela a présenté à NVIDIA GTC Berlin un démonstrateur hybride IA-quantique en conditions réelles, intégrant son QPU photonique à des systèmes NVIDIA DGX via NVQLink et la plateforme CUDA-Q, pour des workflows hybrides et du reservoir computing. Le logiciel de couplage GPU-QPU devient un champ d'innovation où l'acteur français est en première ligne.

20. **Qiskit SDK v2.6 : extension du C API (pass-manager, QPY natif, opérations custom)**
   Qiskit 2.6.0/2.6.1 (PyPI : 16 et 22/10) étend le C API : framework de pass-manager, sérialisation QPY v18 native et opérations hardware customs sans Python, vers une pile quantique « Python-optional » pour l'intégration HPC (C, C++, Julia). Suite directe de la 2.6.0 couverte la semaine dernière ; la pile logicielle se prépare aux architectures hybrides HPC.

21. **The Compendium of Super-Quadratic Computational Quantum Advantages**
   Compilation structurée des problèmes présentant des perspectives crédibles d'avantage quantique super-quadratique. Au-delà d'un catalogue, elle identifie les caractéristiques structurelles requises (chargeabilité efficace des données classiques, profondeurs de circuit tolérables, structure algébrique du problème) pour qu'un speedup théorique se traduise en avantage pratique — et réfute implicitement les annonces d'avantage prématurées. Les cas d'usage industriels super-quadratiques restent un horizon au-delà de 5 ans.  ⚠️ Preprint arXiv non validé par les pairs.

22. **Constant-Depth Quantum Barrier Option Pricing via a Static Bivariate Oracle Framework**
   Méthode quantique à profondeur constante pour le pricing d'options à barrière, évitant la discrétisation séquentielle des trajectoires du Monte-Carlo classique. L'oracle bivarié statique réduit fortement le nombre de qubits et de portes tout en maintenant la précision sur matériel bruité — un progrès face au verrou principal de l'estimation d'amplitude (QAE) en finance, qui exigeait des circuits trop profonds pour le NISQ.  ⚠️ Preprint arXiv non validé par les pairs.

23. **Distributed Quantum-Centric Supercomputing with Multi-Layered Generative Learning for Intermolecular Interactions**
   Cadre distribué combinant apprentissage génératif multi-couches et supercalcul quantique-centrique pour simuler les interactions intermoléculaires (dimères et hexamères d'eau) avec une réduction significative des exigences en qubits. Dans la lignée des travaux IBM/Cleveland Clinic/RIKEN sur les protéines (~12 600 atomes), une étape vers la chimie computationnelle pertinente pour la découverte de médicaments — systèmes traités encore loin des cibles biologiques réelles.  ⚠️ Preprint arXiv non validé par les pairs.

24. **Quantum computing for logistics à IEEE Quantum Week 2026 : résultats mitigés face aux solveurs classiques**
   Retour sur les articles consacrés à l'optimisation logistique quantique à QCE26 : QAOA et recuit quantique testés sur du scheduling ferroviaire, du routage de véhicules et de la livraison camion-drone. Verdict sans concession : résultats mixtes, les solveurs classiques restant compétitifs ou supérieurs sur les cas réels. En miroir, D-Wave (initiative supply chain avec l'université de l'Arkansas) et SuperQ (logistique militaire en conditions dégradées) misent sur le déploiement opérationnel. La logistique reste un banc d'essai, pas encore un marché.

25. **Cloudflare lance PQ GeoKey Manager : post-quantique et clés géo-fencées (ML-KEM + X25519)**
   Cloudflare lance en bêta fermée son PQ GeoKey Manager : les clés de déchiffrement sont enveloppées avec un schéma hybride ML-KEM-768 + X25519 (HPKE) pour n'être décapulables que par les serveurs de la géographie choisie par le client, jalonnant la migration PKI souveraine. Disponibilité générale prévue au T1 2027 ; s'ajoutent le support opt-in de ML-KEM et ML-DSA dans Workers et le ML-KEM hybride dans IPsec — en phase avec les échéances fédérales US (key establishment fin 2030, signatures 2031, dépréciation visée 2035, NIST IR 8547).

26. **Supervised Learning with Quantum Hamiltonian Embeddings**
   Cadre QML encodant les données d'entraînement classiques dans un hamiltonien paramétré dont l'état fondamental approximé définit le classifieur. Apports : garanties prouvables (bornes de généralisation) — rare en QML, souvent dominé par les arguments d'expressivité — et démonstration expérimentale scalable sur IBM Heron. À mettre en regard des études négatives récentes (aucune supériorité systématique du QML sur données réelles) : le champ progresse surtout sur le front théorique.  ⚠️ Preprint arXiv non validé par les pairs.
