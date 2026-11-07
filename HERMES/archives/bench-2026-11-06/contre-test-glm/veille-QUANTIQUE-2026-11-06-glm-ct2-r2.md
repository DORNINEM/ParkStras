# Veille Informatique Quantique — semaine du 31 octobre au 6 novembre 2026

*Générée le 6 novembre 2026 par ORAC (Hermes) · fenêtre 7 jours · dates de publication vérifiées sur chaque page source · 12 articles*

---

## Synthèse — 5 signaux faibles à surveiller

1. **La menace RSA se quantifie, pas seulement s'annonce.** Alice & Bob publie la compilation complète de l'algorithme de Shor sur qubits « chat » : 22 593 qubits physiques pendant 3,14 jours pour casser RSA-2048 — une **estimation théorique** (hypothèse d'erreurs de bit-flip ~1/100 ans/qubit, très en deçà du matériel démontré à ce jour), pas une démonstration. Mais le passage du « un jour peut-être » à un chiffrage précis des ressources transforme la question pour une DSI : ce n'est plus « si » mais « combien de qubits à quelle date ». → **Implication :** lancer (ou accélérer) l'inventaire cryptographique et le plan de migration PQC maintenant ; toute donnée interceptée aujourd'hui reste déchiffrable à l'horizon 2030+. Sources : https://alice-bob.com/blog/compiling-shors-algorithm-on-cat-qubits-22-593-qubits-to-break-rsa-2048-in-3-14-days/ · https://www.techzine.eu/blogs/security/145562/dutch-government-praises-quantum-keys-but-doesnt-use-them/

2. **La correction d'erreur quantique (QEC) devient un chantier industriel orchestré par les États.** IBM, le Quantum Science Center d'Oak Ridge et AMD ouvrent une plateforme de co-conception associant le processeur Nighthawk (120 qubits) au HPC Umbra (GPU AMD), adossée à l'objectif du DOE de 100 qubits logiques exécutant 100 000 opérations « dures » fin 2028 ; Quantinuum avait annoncé fin octobre un record de correction d'erreur ×10. → **Implication R&D :** suivre les jalons QEC vérifiés (fidélité logique, décodage temps réel) plutôt que les compteurs de qubits physiques ; c'est là que se jouera l'avance de 2028-2029. Sources : https://newsroom.ibm.com/2026-11-05-oak-ridge-national-lab,-ibm,-and-amd-launch-new-co-design-platform-for-quantum-error-correction · https://www.quantinuum.com/press-releases/quantinuum-unveils-nexus-roadmap-to-deliver-the-first-developer-platform-designed-for-the-fault-tolerant-quantum-era

3. **La PQC entre dans le silicium et le cloud grand public.** STMicroelectronics lance le STM32G5, premier MCU mixte avec accélérateur matériel couvrant tous les algorithmes PQC du NIST (ML-KEM, ML-DSA, SLH-DSA, LMS) ; AWS KMS ajoute ML-KEM (FIPS 203) avec clés privées en HSM FIPS 140-3 niveau 3. La migration post-quantique n'est plus un chantier de bibliothèques logicielles mais un équipement d'infrastructure standard. → **Implication RSSI :** intégrer les exigences PQC (CNSA 2.0, échéances fédérales US 2030-2031) dans les cahiers des charges dès le prochain renouvellement de flotte IoT/embedded. Sources : https://blog.st.com/stm32g5-security/ · https://aws.amazon.com/blogs/aws/aws-weekly-roundup-gpt-6-1-terra-on-bedrock-step-functions-as-agent-tools-and-more-november-2-2026/

4. **Les gouvernements refroidissent les attentes sur la QKD.** La stratégie quantique néerlandaise présentée début octobre le dit explicitement : la QKD « ne répond pas encore aux exigences de sécurité » de l'État central, qui privilégie la PQC ; les industriels eux-mêmes (SES, Eurofiber, QuTech) reconnaissent nœuds de confiance, portée ~100 km en fibre et dépendance à une authentification classique. Les positions FR/DE/SE (AIVD, 2024) convergent. → **Implication :** ne pas budgéter de la QKD avant d'avoir déployé la PQC ; si la QKD entre dans le scope (défense, infrastructures critiques), l'exiger en complément — défense en profondeur — jamais en remplacement. Sources : https://www.techzine.eu/blogs/security/145562/dutch-government-praises-quantum-keys-but-doesnt-use-them/ · https://hun-ren.hu/research_news/hun-ren-wigner-researchers-exchange-quantum-key-encrypted-radio-messages-in-budapest-110446

5. **Consolidation boursière : la valeur migre vers la sécurité et l'abonnement.** Résultats T3 contrastés dans la même semaine : IonQ bondit (173,8 M$, backlog 1,2 Md$) et rachète Elisity, une société de sécurité réseau Zero Trust ; Quantinuum et IQM lèvent leurs objectifs ; Pasqal voit son chiffre d'affaires reculer (3,3 M€, aucune vente de QPU) malgré 312,8 M€ de trésorerie. La pression sur la consolidation des acteurs européens (alerte de la Cour des comptes en août) se lit dans ces écarts. → **Implication direction :** pour un investisseur ou un acheteur public, le critère devient la récurrence (cloud, sécurité, services) et non la vente de machines ; surveiller le risque de rachat des pépites françaises. Sources : https://www.ionq.com/news/ionq-announces-record-3q26-revenues-and-raises-fy2026-guidance-to-505---515-million-as-backlog-grows-to-1-2-billion · https://www.stocktitan.net/news/USAR/pasqal-reports-third-quarter-business-ev6q2a8arymm.html · https://www.sec.gov/Archives/edgar/data/2113060/000119312526448359/iqmx-ex99_1.htm

---

## Actualités

### 🇫🇷 France

#### [Alice & Bob chiffre RSA-2048 sur qubits « chat » : 22 593 qubits pendant 3,14 jours — une estimation, pas une démonstration](https://alice-bob.com/blog/compiling-shors-algorithm-on-cat-qubits-22-593-qubits-to-break-rsa-2048-in-3-14-days/)
*Blog Alice & Bob · 04/11/2026*

La startup parisienne publie la compilation intégrale de l'algorithme de Shor sur son architecture de qubits chat : 22 593 qubits physiques exécutés 3,14 jours pour factoriser RSA-2048, soit environ 40 fois moins de qubits que les projections à code de surface. Point d'honnêteté technique : l'estimation suppose des bit-flips négligeables (1/100 ans/qubit), très au-delà du matériel démontré (18 qubits chat actuels) — c'est une feuille de route de ressources, pas un démonstrateur. À lire avec le dépôt du dossier PROQCIMA phase 1 de la même équipe (portes logiques non-Clifford, code de répétition distance 3 sur puce 12 qubits, taux d'erreur logique encore au-dessus du seuil de tolérance aux pannes).

#### [Pasqal : T3 en repli (3,3 M€) mais 312,8 M€ de trésorerie et un carnet de 69,8 M€](https://www.stocktitan.net/news/USAR/pasqal-reports-third-quarter-business-ev6q2a8arymm.html)
*StockTitan (communiqué GlobeNewswire) · 06/11/2026*

Le leader des atomes neutres, coté au Nasdaq depuis fin août, rapporte un chiffre d'affaires de 3,3 M€ contre 5,7 M€ un an plus tôt — l'écart s'explique par l'absence de vente de QPU sur le trimestre (3,2 M€ reconnus l'an passé). Les services liés aux QPU progressent de 53 % (3,1 M€), dont les premières heures consommées du contrat QCaaS avec Aramco ; carnet ferme de 69,8 M€ stable. Le modèle bascule clairement de la vente de machines vers les services d'accès.

#### [Quandela s'allie à l'université coréenne Kookmin : recherche et formation en photonique](https://quantumzeitgeist.com/quandela-kookmin-university-partnership-quantum-research/)
*Quantum Zeitgeist · 04/11/2026*

Via son Quantum University Program, Quandela ouvre ses plateformes photoniques et son cloud à l'université Kookmin (Séoul), avec un axe hybride HPC-QPU et la formation de talents quantiques. Après l'accord industriel avec FPT au Vietnam (octobre), le leader photonique européen tisse un réseau académique et commercial en Asie — une stratégie de distribution à faible capital qui compense la sous-capitalisation pointée par la Cour des comptes.

### 🌍 Europe

#### [IQM : 42,2 M€ de commandes au T3, dont 33 M€ pour LUMI-IQ, le premier supercalculateur quantique européen à qubits logiques](https://www.sec.gov/Archives/edgar/data/2113060/000119312526448359/iqmx-ex99_1.htm)
*Communiqué boursier IQM (SEC) · 05/11/2026*

Le finlandais IQM (Nasdaq : IQMX) signe un T3 record : 42,2 M€ de nouvelles commandes, backlog de 102,5 M€ (+52 % depuis janvier), revenus 8,9 M€ (+51 %). La pièce maîtresse est le contrat de 33 M€ avec le CSC (LUMI AI Factory) pour Halocene, sa plateforme de correction d'erreur : livraison 2027 (150 qubits physiques), correction d'erreur temps réel en 2028 — premier ordinateur quantique supraconducteur européen à qubits logiques annoncé. Première vente en Amérique du Sud (Brésil), deuxième au Japon (TOYO).

#### [Les Pays-Bas adoptent la PQC et tiennent la QKD à distance — malgré leur station EAGLE-1](https://www.techzine.eu/blogs/security/145562/dutch-government-praises-quantum-keys-but-doesnt-use-them/)
*Techzine · 04/11/2026*

Enquête de terrain à Rotterdam (Quantum Communication Fieldlab) : le gouvernement néerlandais félicite sa station sol pour le satellite QKD EAGLE-1 mais n'utilise pas la QKD pour sa propre sécurité — « elle ne répond pas encore aux exigences ». Nœuds de confiance obligatoires, portée ~100 km en fibre, authentification classique requise : les industriels eux-mêmes ne présentent plus la QKD comme un remplacement mais comme un semi-produit intégré à une défense en profondeur avec la PQC. Le signal le plus net d'Europe sur la hiérarchie PQC d'abord, QKD ensuite.

#### [QKD par radio mesh à Budapest : les chercheurs du Wigner chiffrent des messages Meshtastic](https://hun-ren.hu/research_news/hun-ren-wigner-researchers-exchange-quantum-key-encrypted-radio-messages-in-budapest-110446)
*HUN-REN · 04/11/2026*

Première mondiale revendiquée : des clés générées par QKD (via le projet QCIHungary, contribution hongroise à EuroQCI financé par Digital Europe) ont protégé des messages échangés sur le réseau radio ouvert Meshtastic (LoRa), entre les deux rives du Danube. Portée radio comparable aux liaisons QKD fibre directes, réseau décentralisé sans infrastructure : une démonstration de vulgarisation qui montre la bonne intégration des clés quantiques dans des systèmes existants — une démo, pas un produit.

### 🌐 Monde

#### [IBM allume son Quantum System Two le plus avancé à Chicago, propulsé par Nighthawk](https://newsroom.ibm.com/2026-11-06-ibm-unveils-its-most-advanced-quantum-computer-in-chicago,-marking-a-milestone-for-illinoiss-quantum-future)
*IBM Newsroom · 06/11/2026*

Premier ordinateur quantique d'IBM dans l'Illinois : un Quantum System Two alimenté par Nighthawk (« la puce quantique la plus puissante jamais construite par IBM ») est opérationnel à Hyde Park Labs, hébergé par l'université de Chicago, avant transfert vers l'Illinois Quantum and Microelectronics Park. Un jalon de déploiement d'infrastructure — pas une nouvelle démonstration de tolérance aux pannes ni d'avantage quantique.

#### [IBM + Oak Ridge + AMD : une plateforme de co-conception pour la correction d'erreur quantique](https://newsroom.ibm.com/2026-11-05-oak-ridge-national-lab,-ibm,-and-amd-launch-new-co-design-platform-for-quantum-error-correction)
*IBM Newsroom · 05/11/2026*

À Poughkeepsie, le Nighthawk 120 qubits est désormais co-localisé avec Umbra, le HPC d'Oak Ridge (GPU AMD Instinct MI355X + EPYC), pour tester le décodage temps réel à basse latence. L'objectif affiché s'aligne sur le DOE : un ordinateur quantique scientifiquement pertinent d'ici 2028, avec 100 qubits logiques exécutant 100 000 opérations « dures » fin 2028 — IBM revendique à ce jour jusqu'à 70 qubits logiques et 438 opérations, soit un facteur ~230 à combler.

#### [IonQ : T3 record à 173,8 M$ (+336 %), backlog 1,2 Md$, et rachat d'Elisity pour la sécurité quantique](https://www.ionq.com/news/ionq-announces-record-3q26-revenues-and-raises-fy2026-guidance-to-505---515-million-as-backlog-grows-to-1-2-billion)
*IonQ · 05/11/2026*

Sixième trimestre record consécutif, guidance annuelle relevée à 505-515 M$ — mais une croissance tirée en partie par la fonderie SkyWater acquise en juillet (83,5 M$ sur deux mois), donc pas organique. Le 4 novembre, IonQ a aussi bouclé le rachat d'Elisity (1,15 Md$ en actions), société de sécurité réseau Zero Trust, et signé un contrat avec l'initiative QuantumCT du Connecticut (150+ heures de cloud). Signal : la sécurité « quantum-ready » devient un moteur de croissance, pas un coût.

#### [Quantinuum dévoile la roadmap Nexus : la première plateforme développeurs de l'ère de la tolérance aux pannes](https://www.quantinuum.com/press-releases/quantinuum-unveils-nexus-roadmap-to-deliver-the-first-developer-platform-designed-for-the-fault-tolerant-quantum-era)
*Quantinuum · 05/11/2026*

Le trapped-ioniste (Nasdaq : QNT) annonce une roadmap multi-années de sa plateforme Nexus : encodage de correction d'erreur automatisé, bibliothèques fault-tolerantes et orchestration hybride, alignés sur chaque génération de matériel jusqu'à Apollo, son ordinateur quantique universel tolérant aux fautes prévu pour 2029. En parallèle, T3 à 9,1 M$ (+233 %) et adoption de Nexus par 215 organisations. La bataille se déplace du nombre de qubits vers l'expérience développeur de l'ère QEC.

#### [AWS KMS adopte ML-KEM : la post-quantique entre dans le service de clés managé](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-gpt-6-1-terra-on-bedrock-step-functions-as-agent-tools-and-more-november-2-2026/)
*AWS News Blog · 02/11/2026*

AWS Key Management Service prend en charge ML-KEM (FIPS 203) sur ses trois jeux de paramètres, via les opérations Encapsulate/Decapsulate, avec clés privées scellées dans des HSM FIPS 140-3 niveau 3. La cible nommée : la menace « harvest now, decrypt later ». Disponible dans toutes les régions (hors Moyen-Orient et Chine). Pour une DSI, c'est la voie la plus rapide pour couvrir les échanges de clés critiques sans réécrire les applications.

#### [STM32G5 : STMicroelectronics embarque un cœur cryptographique post-quantique dans un MCU grand public](https://blog.st.com/stm32g5-security/)
*Blog ST · 03/11/2026*

Le nouveau STM32G5 (Cortex-M33, 280 MHz) devient le premier MCU mixte de ST avec un accélérateur matériel couvrant l'ensemble des algorithmes PQC approuvés par le NIST : ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205) et LMS. Certification visée SESIP/PSA niveau 3. La migration post-quantique descend au niveau de la passe de silicium — les flottes IoT déployées dans les prochaines années seront nativement « quantum-ready ».

---

## 🔮 Prospective

**Court terme (2027) :** la pression réglementaire PQC devient cadence — échéances CNSA 2.0 et exigences fédérales US (migrations prioritaires d'ici fin 2030 pour les échanges de clés), arrivée des standards d'harmonisation du Cyber Resilience Act européen (Q4 2026), et côté recherche, deadline le 17/11/2026 de l'appel Horizon Europe « Next-Generation QKD Systems » (EuroHPC) qui imposera l'hybridation QKD+PQC sur applications réelles. → Les cahiers des charges 2027 doivent déjà exiger des algorithmes PQC validés.

**Moyen terme (2028-2029) :** le duel des jalons QEC vérifiés — DOE : 100 qubits logiques/100 000 opérations fin 2028 ; Quantinuum Apollo et fault tolerance IBM en 2029 ; LUMI-IQ avec correction temps réel en 2028-2029 en Europe. Le premier acteur à publier une fidélité logique s'améliorant durablement sous le seuil avec des centaines de qubits logiques aura gagné le récit, indépendamment des records de qubits physiques.

**Long terme (2030-2032) :** convergence des feuilles de route souveraines — PROQCIMA porte à 1 024 qubits logiques en 2032, Alice & Bob vise 100 qubits logiques utiles en 2030, IQM et l'EU Quantum Act (attendu 2027) cherchent à structurer des fonderies de qubits européennes. Pour les organisations, l'horizon pertinent reste simple : tout secret devant rester confidentiel au-delà de 2035 doit changer de cryptographie avant la fin de cette décennie.

---

*Fenêtre : 31 octobre – 6 novembre 2026. Chaque date de publication a été vérifiée sur la page source elle-même. Aucune source blacklistée (lesnumeriques.com, degrouptest.com) citée. Une dépêche = une entrée (pas de doublon presse/reprise).*
