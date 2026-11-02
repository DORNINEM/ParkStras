# 🛡️ Veille Télésurveillance & Sécurité électronique

**Date :** 2 novembre 2026
**Fenêtre :** 7 jours (26 octobre – 2 novembre 2026)
**Généré par :** Hermes — cron veille-telesurveillance

---

## Synthèse de la semaine

Semaine dominée par le basculement de la vidéoprotection vers des dispositifs « IA + supervision humaine » portés par les collectivités : après le vote du Sénat qui prolonge la vidéoprotection algorithmique jusqu'à fin 2030, les Alpes-Maritimes valident un centre départemental de supervision mutualisé pour 151 communes et Périgueux engage le doublement de son parc. En face, la cybersécurité des équipements reste le maillon faible : l'ANSSI alerte sur les « impacts secondaires » des failles PHP qui touchent aussi caméras et objets connectés (660 000 adresses IP en France) et le CERT-FR publie une vulnérabilité dans un logiciel de station vidéo Axis. En Europe, la reconnaissance faciale en direct continue de s'étendre au Royaume-Uni sans loi dédiée (406 001 visages scannés par une seule police), tandis que l'Allemagne débat du recoupement a posteriori d'images de manifestation. Sur le plan réglementaire, la France n'a toujours pas transposé NIS2 et un référentiel officiel des échéances de l'AI Act rappelle que le report « haut risque » au 2 décembre 2027 change la trajectoire de conformité du secteur. Côté marché, la supervision vidéo 24/7 s'industrialise (partenariat Totem × Milestone) et les opérateurs de salles de contrôle sont désormais au cœur des réflexions sur la fatigue d'alarme.

---

## Actualités

### 🇫🇷 France

1. **Alpes-Maritimes : un centre départemental de supervision dopé à l'IA pour 151 communes**
   - Source : Smart City Mag — 26/10/2026 — https://www.smartcitymag.fr/breve/20/un-centre-departemental-de-supervision-mis-en-service-fin-2026-a-nice
   - Résumé : Validé à l'unanimité le 26 octobre, le Centre départemental de supervision s'installera au Cadam, à Nice, avec une mise en service prévue fin 2026. Il mutualise la surveillance vidéo pour les communes qui n'ont ni le personnel ni les moyens techniques de tenir un mur d'images, notamment la nuit : 151 des 163 communes du département sont éligibles, 15 ont déjà adhéré, plus de 250 caméras municipales seront connectées au lancement (70 à 80 communes visées à terme). Investissement initial : 1,7 M€, coûts d'exploitation estimés à 500 000 €/an. Un modèle de « télésurveillance publique mutualisée » qui concurrence directement les prestataires privés sur les petits territoires.

2. **Périgueux veut doubler son parc de caméras et moderniser son centre de supervision**
   - Source : Dordogne Libre — 01/11/2026 — https://www.dordognelibre.fr/grand-perigueux/la-ville-de-perigueux-veut-doubler-le-nombre-de-cameras-de-videosurveillance-31308352.php
   - Résumé : À l'issue du conseil municipal du 29 octobre, la majorité a défendu le doublement du dispositif, soit jusqu'à une cinquantaine de caméras supplémentaires pour atteindre environ 100 unités sur le mandat, avec une demande de subvention de plus de 521 000 € à l'État. Le centre de supervision urbain actuel, qui n'est pas armé 24 h/24, doit être modernisé dans le même mouvement ; l'opposition s'est abstenue. Signal classique du cycle d'équipement des villes moyennes : extension du parc, puis mise à niveau de la supervision — un appel d'air pour les intégrateurs locaux.

3. **Vidéosurveillance : le CERT-FR signale une faille dans les sauvegardes d'Axis Camera Station Pro**
   - Source : CERT-FR (ANSSI) — 28/10/2026 — https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1408/
   - Résumé : L'avis CERTFR-2026-AVI-1408 décrit la vulnérabilité CVE-2026-63286 (gravité élevée, CVSS 7.1) dans Camera Station Pro, le logiciel de station vidéo d'Axis, pour toutes les versions antérieures à 6.20. Elle expose les sauvegardes de la base de données du logiciel à des attaques hors ligne, avec risque de fuite d'identifiants et d'informations. Le correctif est publié en 6.20, mais l'ANSSI précise que les anciennes copies de sauvegarde doivent aussi être supprimées et les identifiants exposés renouvelés. À intégrer dans les procédures de maintenance des parcs vidéo professionnels.

4. **L'ANSSI alerte sur les « impacts secondaires » des failles PHP : caméras, routeurs et objets connectés visés**
   - Source : BFM TV — 28/10/2026 — https://www.bfmtv.com/tech/cybersecurite/il-ne-faut-pas-considerer-que-le-probleme-est-definitivement-resolu-l-anssi-alerte-sur-des-impacts-secondaires-lies-aux-failles-php_AD-202610280917.html
   - Résumé : Après le correctif des serveurs web, l'ANSSI prévient que le risque s'est déplacé vers les produits embarquant une version de PHP dans leur interface d'administration : routeurs, pare-feu, NAS et **objets connectés** — dont caméras IP et enregistreurs. La France compte plus de 660 000 adresses IP utilisant PHP et potentiellement plus de 6 millions d'applications concernées. Seule la mise à jour publiée par chaque fabricant protège réellement l'équipement : pour un installateur, cela se traduit par un inventaire du parc, un suivi des firmwares éditeurs et un cloisonnement réseau systématique.

### 🌍 Europe hors France

5. **Royaume-Uni : la reconnaissance faciale en direct s'étend, toujours sans loi dédiée**
   - Sources : BBC News — 26/10/2026 — https://www.bbc.co.uk/news/articles/ck62y02285r8o • Tech Times — 28/10/2026 — https://www.techtimes.com/articles/329574/20261028/live-facial-recognition-scanned-406001-hampshire-faces-still-no-uk-law.htm • Biometric Update — 30/10/2026 — https://www.biometricupdate.com/202610/uk-facial-recognition-rollout-widens-as-police-oversight-rules-take-shape
   - Résumé : La police du Suffolk redéploie ses fourgons de reconnaissance faciale en direct à Lowestoft (3/11), Bury St Edmunds (4/11) et Ipswich (5/11) ; le Hertfordshire a mis en service deux nouveaux véhicules. Surtout, l'association Big Brother Watch a publié le 27 octobre les chiffres du Hampshire : 406 001 visages convertis en gabarits biométriques en douze mois pour 26 arrestations, sans consentement ni base légale spécifique, en attendant le Police Reform Bill. Pour un intégrateur français : la biométrie en temps réel reste hors du cadre autorisé en France, mais la pression commerciale sur ce type d'offres s'accroît à l'échelle européenne.

6. **Allemagne : recoupement a posteriori contesté au Bade-Wurtemberg et caméras « comportementales » à Berlin**
   - Source : anoni.net (synthèse sourcée, dont netzpolitik.org et Polizei Berlin) — 28/10/2026 — https://anoni.net/news/en/2026/10/germany-police-facial-recognition/
   - Résumé : Selon un témoignage d'audience rapporté par netzpolitik.org, un agent de l'office criminel du Bade-Wurtemberg a passé après coup des images d'une manifestation enregistrée dans un logiciel et identifié quatre participants sans lien avec l'affaire. En parallèle, la police de Berlin a commencé à tester des caméras analysant les comportements dans des lieux à forte criminalité, la loi berlinoise excluant explicitement la reconnaissance faciale automatisée sur ces images. Le rappel utile : l'AI Act interdit en principe l'identification biométrique en temps réel dans l'espace public, mais le recoupement a posteriori ne relève du régime « haut risque » qu'à partir de décembre 2027.

7. **Yale et Ajax renforcent leur alliance : la Linus Smart Lock L2 Lite intégrée nativement à l'écosystème Ajax**
   - Source : Digital Security Magazine — 29/10/2026 — https://www.digitalsecuritymagazine.com/2026/10/29/yale-ajax-alianza-integracion-linus-smart-lock-l2-lite/
   - Résumé : La dernière serrure connectée de la gamme Linus (Yale, groupe ASSA ABLOY) est désormais officiellement intégrée dans le cloud Ajax : elle apparaît comme un dispositif natif dans les applications Ajax et se pilote depuis la même interface que les protections intrusion, incendie et vidéosurveillance. Objectif affiché : centraliser le contrôle d'accès sans passerelle tierce. Pour les installateurs certifiés Ajax, c'est une brique de plus dans une offre unifiée alarme + accès + vidéo, et un premier pas concret de la convergence contrôle d'accès / intrusion côté européen.

### 🌐 Monde

8. **Ukraine : le CERT-UA alerte sur le piratage de caméras Dahua via les services cloud**
   - Sources : The Record (Recorded Future News) — 26/10/2026 — https://therecord.media/ukraine-cert-ua-warning-chinese-dahua-cameras-hacked • eSecurity Planet — 27/10/2026 — https://www.esecurityplanet.com/news/dahua-camera-cloud-access-attacks-emea-ukraine/
   - Résumé : L'autorité ukrainienne CERT-UA signale une campagne active contre les caméras et enregistreurs Dahua connectés à internet, exploitant des vulnérabilités connues (dont CVE-2021-33044) pour accéder aux flux vidéo et créer des comptes non autorisés. Le point le plus préoccupant : le service cloud Easy4IP permet l'accès aux équipements même derrière un pare-feu, ce qui invalide la protection par simple isolation réseau. À lire comme un rappel que la « commodité cloud » des caméras grand public est un vecteur d'attaque direct pour tout parc professionnel mal cloisonné.

9. **ADT rénove son centre de surveillance du Texas pour 2 M$**
   - Source : Security Today — 28/10/2026 — https://securitytoday.com/articles/2026/10/28/adt-unveils-renovated-texas-monitoring-center.aspx
   - Résumé : ADT a achevé la rénovation de son centre de surveillance d'Irving (Texas) avec un investissement de 2 M$ : postes de travail modernisés, espaces de collaboration élargis et équipements destinés à fluidifier la coordination des alarmes et des dispatchs 24/7. Le signal pour la filière : les industriels continuent d'investir dans le **bâtiment** des centres de surveillance, alors que l'essentiel de la valeur perçue migre vers le logiciel et l'analyse — un arbitrage budgétaire à surveiller pour les centres français de taille intermédiaire.

10. **Totem et Milestone s'associent pour industrialiser la supervision vidéo 24/7 externalisée**
    - Sources : SDM Magazine — 27/10/2026 — https://www.sdmmag.com/articles/105949-totem-partners-with-milestone-to-extend-the-power-of-video-management-into-24-7-monitoring-operations • Security.World — 27/10/2026 — https://security.world/totem-partners-with-milestone-to-expand-24-7-video-monitoring-operations/ • SourceSecurity — 28/10/2026 — https://www.sourcesecurity.com/news/totem-milestone-partner-24-7-video-co-1621407195-ga.1793167014.html
    - Résumé : Annoncé le 27 octobre, le partenariat combine le VMS XProtect de Milestone et le service de supervision humaine 24/7 de Totem. Les centrales de télésurveillance peuvent ainsi proposer de la vérification vidéo et du traitement d'alerte sans recruter ni construire d'infrastructure supplémentaire. C'est l'illustration d'un modèle « monitoring as a service » qui déplace la concurrence : la barrière à l'entrée d'un centre de supervision vidéo baisse, mais la dépendance à un tiers opérateur augmente.

---

## ⚖️ Juridique & Réglementaire

1. **Vidéoprotection algorithmique : le Sénat vote une nouvelle extension, jusqu'à fin 2030** *(France)*
   - Sources : INCYBER NEWS (28/10/2026) https://incyber.org/article/videoprotection-algorithmique-le-senat-vote-une-nouvelle-extension-du-dispositif/ • Armées.com (28/10/2026) https://armees.com/casseurs-payeurs-drones-surveillance-algorithmes-maintien-ordre/
   - Impact concret : adopté dans la nuit du 27 au 28 octobre par 229 voix contre 105, le projet de loi « casseurs-payeurs » prolonge l'expérimentation d'analyse automatisée des images (caméras et drones judiciaires) et élargit son usage aux troubles à l'ordre public ; le texte part à l'Assemblée nationale. Pour un intégrateur : le cadre de la vidéoprotection algorithmique se consolide côté « événementiel et ordre public », mais reste strictement encadré (pas de reconnaissance faciale en temps réel généralisée, autorisations plafonnées). Toute offre d'analyse vidéo IA doit être calibrée sur les finalités autorisées.

2. **NIS2 : la France toujours non transposée, le texte retiré de l'agenda parlementaire** *(France/Europe)*
   - Sources : AOCSI (mis à jour 29/10/2026) https://aocsi.fr/blog/loi-resilience-transposition-nis2 • NIS2 Transposition Tracker (27/10/2026) https://nhimg.org/nis2-transposition-tracker • Silicon.fr (octobre 2026) https://www.silicon.fr/cybersecurite-1371/nis2-ce-quil-faut-attendre-du-projet-de-loi-examine-a-lassemblee-nationale-229520
   - Impact concret : 24 des 27 États membres ont une loi NIS2 en vigueur ; la France, l'Irlande et l'Espagne non. Le projet de loi « Résilience » (transposition NIS2, CER, DORA) a été retiré de l'ordre du jour de l'Assemblée nationale le 6 octobre, sans nouvelle date, alors qu'il élargirait le périmètre à environ 15 000 entités sur 18 secteurs. Pour un centre de télésurveillance ou un intégrateur : les obligations d'hygiène cyber et de notification ne sont pas encore opposables en droit français, mais les donneurs d'ordre (collectivités, santé, énergie) les intègrent déjà dans leurs cahiers des charges. Anticiper reste la seule option.

3. **AI Act : un référentiel officiel des échéances publié le 29 octobre, « haut risque » reporté au 2 décembre 2027** *(Europe)*
   - Sources : data.gouv.fr (29/10/2026) https://www.data.gouv.fr/datasets/referentiel-ia-act-echeances-obligations-et-sanctions-du-reglement-europeen-sur-lia • ActuIA (octobre 2026) https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/
   - Impact concret : le référentiel exploitable publié le 29 octobre rappelle que le règlement omnibus (UE) 2026/1744 a repoussé les obligations « haut risque » de l'annexe III au **2 décembre 2027** (annexe I : 2 août 2028), tout en conservant l'application des interdictions, des règles GPAI et de transparence. Pour un fournisseur de VMS, d'analytique vidéo ou un centre de télésurveillance : la fenêtre de mise en conformité s'allonge de plusieurs trimestres, mais la documentation (cartographie des fonctions IA, supervision humaine, journalisation) reste à produire avant l'audit — le report ne supprime aucune obligation de fond.

---

## 💼 Métiers de la télésurveillance — focus impacts IA

1. **Opérateurs de télésurveillance & levée de doute : l'IA trie, l'humain décide** — Source : Benchmark Magazine — 29/10/2026 — https://benchmarkmagazine.com/reducing-control-room-fatigue-where-ai-can-help/
   - Ce que l'IA change : l'article décrit précisément le partage des rôles en salle de contrôle — l'analytique vidéo détecte l'activité inhabituelle, écarte les alertes redondantes et met en avant les événements qui méritent attention ; l'opérateur conserve la levée de doute, la qualification de l'alerte, la décision d'escalade et la relation avec le client. Tâches automatisées : filtrage des fausses alertes, pré-tri, priorisation de la file. Tâches humaines conservées : vérification contextuelle, arbitrage en cas d'ambiguïté, appel client, transmission aux forces de l'ordre. Il s'appuie sur une enquête Omdia auprès d'utilisateurs finaux en Amérique du Nord et en Europe montrant un retour sur investissement marqué des investissements en analytique vidéo. Compétence qui monte : exploiter et paramétrer les scénarios d'analyse, non plus seulement « lire » des images.

2. **Formation et carte professionnelle : le CNAPS précise les règles du tronc commun obligatoire** — Source : 83-629.fr (Sécurité Privée, CNAPS & Réglementation) — 27/10/2026 — https://www.83-629.fr/tag/telesurveillance/
   - Ce que l'IA change : dans un secteur où les fiches de poste s'élargissent aux outils numériques et d'analyse, la question du socle de compétences devient un enjeu RH direct — l'article revient sur les cas où un agent ayant déjà suivi le tronc commun doit (ou non) le refaire, réponse du CNAPS à l'appui. Pour un centre de télésurveillance : c'est le cadre à maîtriser pour valider la conformité des agents (carte professionnelle, formations obligatoires) au moment où l'on ajoute des modules d'exploitation vidéo et d'outils IA aux parcours internes. Métiers concernés : opérateurs vidéoprotection/télésurveillance, formateurs et responsables RH des entreprises de sécurité privée.

---

## 🔮 Prospective — tendances de fond

- **Salles de supervision mutualisées « IA + opérateur » portées par le public** — *Horizon : Court terme (<2 ans)*. Le centre départemental des Alpes-Maritimes (151 communes éligibles, 250+ caméras) et le doublement du parc de Périgueux montrent que les collectivités investissent désormais directement dans la supervision assistée par IA. Pour les centres privés : positionnement à revoir sur les petits territoires, qui basculent vers l'intercommunal ou le départemental. (https://www.smartcitymag.fr/breve/20/un-centre-departemental-de-supervision-mis-en-service-fin-2026-a-nice • https://www.dordognelibre.fr/grand-perigueux/la-ville-de-perigueux-veut-doubler-le-nombre-de-cameras-de-videosurveillance-31308352.php)
- **Hygiène cyber des équipements de sécurité comme prérequis contractuel** — *Horizon : Court terme (<2 ans)*. Failles PHP dans les objets connectés (660 000 IP en France), vulnérabilité Axis Camera Station Pro, caméras Dahua détournées via le cloud : trois signaux convergents la même semaine. Les installateurs devront prouver un inventaire firmware, des accès durcis et un cloisonnement réseau, et le contractualiser. (https://www.bfmtv.com/tech/cybersecurite/il-ne-faut-pas-considerer-que-le-probleme-est-definitivement-resolu-l-anssi-alerte-sur-des-impacts-secondaires-lies-aux-failles-php_AD-202610280917.html • https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1408/ • https://therecord.media/ukraine-cert-ua-warning-chinese-dahua-cameras-hacked)
- **Biométrie : extension des usages, retard du cadre** — *Horizon : Moyen terme (2-5 ans)*. Le Royaume-Uni déploie la reconnaissance faciale en direct sans loi dédiée (406 001 visages scannés par une seule police) et l'Allemagne teste l'analyse comportementale, alors que le régime « haut risque » de l'AI Act ne s'applique qu'en décembre 2027. Un décalage qui continuera d'alimenter contentieux et revirements réglementaires. (https://www.biometricupdate.com/202610/uk-facial-recognition-rollout-widens-as-police-oversight-rules-take-shape • https://anoni.net/news/en/2026/10/germany-police-facial-recognition/)
- **Industrialisation de la supervision vidéo externalisée (monitoring as a service)** — *Horizon : Moyen terme (2-5 ans)*. Le partenariat Totem × Milestone permet à une centrale d'ajouter de la vérification vidéo 24/7 sans recruter ni bâtir d'infrastructure : la barrière à l'entrée baisse, mais la valeur migre vers le logiciel et le réseau d'opérateurs. Modèle à surveiller pour les centres français de taille intermédiaire. (https://www.sdmmag.com/articles/105949-totem-partners-with-milestone-to-extend-the-power-of-video-management-into-24-7-monitoring-operations)
- **Convergence accès / intrusion / vidéo dans une même application** — *Horizon : Moyen terme (2-5 ans)*. L'intégration native de la serrure Yale Linus L2 Lite dans l'écosystème Ajax acte la fin des silos « contrôle d'accès » et « alarme » côté offre installateur ; la valeur se déplace vers la plateforme unifiée et les scénarios automatisés. (https://www.digitalsecuritymagazine.com/2026/10/29/yale-ajax-alianza-integracion-linus-smart-lock-l2-lite/)

---

## 🧭 Synthèse — 5 signaux faibles à surveiller

1. **Les collectivités deviennent des exploitants de vidéoprotection IA (centre départemental, mutualisation intercommunale)** — implication : repositionner l'offre des centres privés vers l'infogérance et l'expertise, pas la revente de caméras.
   - https://www.smartcitymag.fr/breve/20/un-centre-departemental-de-supervision-mis-en-service-fin-2026-a-nice
   - https://www.rivieraradio.mc/article/new-ai-powered-cctv-centre-to-monitor-towns-across-the-alpes-maritimes-5HjdkXw_2/
   - https://www.dordognelibre.fr/grand-perigueux/la-ville-de-perigueux-veut-doubler-le-nombre-de-cameras-de-videosurveillance-31308352.php

2. **La faille vient du firmware, pas de la caméra : le parc installé est le vrai risque** — implication : inventaire des firmwares, veille CERT-FR, cloisonnement réseau et engagement de maintenance à contractualiser.
   - https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1408/
   - https://www.bfmtv.com/tech/cybersecurite/il-ne-faut-pas-considerer-que-le-probleme-est-definitivement-resolu-l-anssi-alerte-sur-des-impacts-secondaires-lies-aux-failles-php_AD-202610280917.html
   - https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/

3. **La supervision vidéo s'achète désormais comme un service opéré par un tiers** — implication : décider vite entre internaliser (opérateurs, process) et s'appuyer sur un partenaire, avant que la marge ne se déplace définitivement.
   - https://www.sdmmag.com/articles/105949-totem-partners-with-milestone-to-extend-the-power-of-video-management-into-24-7-monitoring-operations
   - https://www.sourcesecurity.com/news/totem-milestone-partner-24-7-video-co-1621407195-ga.1793167014.html

4. **La biométrie en direct progresse dans les usages policiers européens avant tout cadre légal national** — implication : refuser ou encadrer strictement toute demande client de reconnaissance faciale en temps réel ; documenter le refus, c'est de la maîtrise du risque.
   - https://www.techtimes.com/articles/329574/20261028/live-facial-recognition-scanned-406001-hampshire-faces-still-no-uk-law.htm
   - https://anoni.net/news/en/2026/10/germany-police-facial-recognition/
   - https://www.biometricupdate.com/202610/uk-facial-recognition-rollout-widens-as-police-oversight-rules-take-shape

5. **Le report « haut risque » de l'AI Act (2 décembre 2027) décale la conformité mais ne l'annule pas** — implication : constituer dès maintenant les preuves documentaires (cartographie IA, supervision humaine, journalisation) et les valoriser commercialement face aux donneurs d'ordre publics.
   - https://www.data.gouv.fr/datasets/referentiel-ia-act-echeances-obligations-et-sanctions-du-reglement-europeen-sur-lia
   - https://aocsi.fr/blog/loi-resilience-transposition-nis2

---

*Généré le 2 novembre 2026 par Hermes (veille-telesurveillance). Fichiers : veille-TELE-2026-11-02.md + .html*
