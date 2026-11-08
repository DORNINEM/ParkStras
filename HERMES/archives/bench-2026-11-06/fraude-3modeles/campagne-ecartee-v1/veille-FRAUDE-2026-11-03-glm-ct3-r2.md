# Veille Fraude Assurance — 3 novembre 2026

**Synthèse** : Treize sources retenues, toutes francophones, dont la grande majorité françaises et plusieurs sources d'autorité (Assemblée nationale, ACPR/AMF, parquet de Paris, Médiation de l'assurance). La tendance de fond reste l'industrialisation de la fraude documentaire par IA : photos de sinistres retouchées, faux justificatifs produits à coût nul, et une réponse opérationnelle qui passe désormais par les métadonnées et la capture « à la source ». Deuxième fil : la donnée partagée comme levier (listes noires open data, actualisation du GAFI, proposition de loi contre l'usurpation d'identité). Enfin, les affaires d'octobre montrent la fraude organisée frappant les réseaux de santé et, fait notable, l'intérieur même d'un grand groupe de protection sociale.

## 🎧 Résumé par thématique (version audio)

_Section destinée au résumé vocal : les liens sources sont dans les entrées ci-dessous._

- **🔍 Anti-fraude documentaire** : La photo de sinistre retouchée par IA ne passe plus : les assureurs lisent les métadonnées, analysent l'image et exigent la photo prise dans leur application. Le coût du faux document est désormais tombé à zéro.
- **📈 Efficacité de gestion de la fraude** : Neuf cent quarante-six millions d'euros de fraude détectée par les assureurs en deux mille vingt-cinq, en hausse de près de cinq pour cent. Côté blanchiment, Monaco et la Bulgarie sortent de la liste grise du GAFI.
- **🗂️ Exploitation de l'opendata** : Les listes noires de l'A M F et de l'ACPR sont actualisées et disponibles en données ouvertes. Un rapprochement automatique à la souscription filtre les acteurs non autorisés sans développement lourd.
- **🕸️ Lutte contre les bandes organisées** : Le parquet de Paris renvoie vingt-deux personnes devant le tribunal correctionnel pour une escroquerie en bande organisée à l'optique, au détriment des mutuelles. Chez Malakoff Humanis, une enquête interne vise des soupçons de corruption organisée.
- **🚪 Fraude en entrée en relation** : Une proposition de loi déposée en octobre veut mieux réprimer l'usurpation d'identité et imposer une garantie minimale dans les contrats. Le médiateur de l'assurance alerte sur la hausse des fraudes aux versements en assurance vie.
- **🩺 Fraude à la santé** : L'Assurance maladie a stoppé quarante-neuf millions d'euros de fraudes aux arrêts de travail en deux mille vingt-cinq, en hausse de dix-sept pour cent. Les employeurs sont appelés à devenir un capteur de première ligne.
- **🧪 Divers sujet émergent** : Des pirates revendiquent le vol de quatre cent trente-six mille dossiers de pharmacies : ordonnances, numéros de Sécu et mutuelles. Ces fuites nourrissent directement la fraude aux remboursements.

## 1. 🔍 Anti-fraude documentaire

- **[Photos de dégâts retouchés par IA : les assureurs les détectent en lisant les métadonnées](https://www.jechange.fr/assurance/habitation/news/photos-degats-retouchees-ia-assureurs-detectent-metadonnees)** — *Jechange, 6 octobre 2026*
  Article méthodologique appuyé sur le bilan 2025 de l'ALFA : les assureurs repèrent une photo de dégât retouchée ou générée par IA par trois moyens — lecture des métadonnées du fichier, analyse de l'image elle-même, et surtout exigence d'une photo prise dans l'application assureur ou en visio-expertise. La fraude documentaire est confirmée comme l'un des trois grands postes de la fraude à l'assurance.
  **Pourquoi c'est pertinent ?** Détaille les trois contrôles réellement déployés au premier appel de sinistre : c'est une grille d'implémentation directement utilisable pour un gestionnaire IARD.
  *À surveiller : la capture de la preuve dans l'app assureur (photo contrainte, horodatage) comme standard de preuve par défaut, plus fiable que la détection a posteriori.*

- **[La fraude à l'assurance augmentée par l'IA](https://algopolis.eu/fr/article/19)** — *AlgoPolis, 23 octobre 2026*
  L'observatoire chiffre la bascule : cas de fraude assistée par IA multipliés par quatre (environ 20 000 en 2022, plus de 80 000 en 2025), hausse de 71 % de la fraude constatée en 2025 par un assureur automobile britannique, en partie imputée aux images générées par IA. Le constat central s'applique au marché français : le coût d'un faux (photo de sinistre, facture, certificat) est tombé à zéro, et la réponse ne peut plus être seulement de « chercher le faux » mais d'authentifier le vrai à la source.
  **Pourquoi c'est pertinent ?** Feuille de route anti-fraude en une page : déplacer l'effort de la détection a posteriori vers la traçabilité des preuves dès la souscription et le premier appel.
  *À surveiller : l'authentification des preuves à la source (horodatage certifié, données EXIF/attestations d'origine) comme contrôleur par défaut.*

## 2. 📈 Efficacité de gestion de la fraude

- **[Les fraudes à l'assurance en hausse de 4,9 % en 2025](https://www.lefigaro.fr/conjoncture/les-fraudes-a-l-assurance-en-hausse-de-4-9-en-2025-20260709)** — *Le Figaro (d'après AFP, rapport ALFA), 9 juillet 2026 (référence indispensable)*
  Chiffres du rapport d'activité 2025 de l'ALFA : 946,3 millions d'euros de fraude détectée par les assureurs (+4,9 % sur un an), l'IARD pesant les deux tiers (626,6 M€). Les procédés dominants restent les fausses déclarations (sinistres fictifs, véhicules maquillés, accidents simulés), la fraude documentaire — photos modifiées à l'aide de l'IA — et la surestimation du préjudice. Le rapport souligne une fraude « de plus en plus structurée ».
  **Pourquoi c'est pertinent ?** Le couple « montant détecté + évolution annuelle » de l'ALFA est l'indicateur de ROI de référence que tout fraude manager ressort en comité de direction.
  *À surveiller : impact réglementaire loi fraude — l'extension des recours et des signalements qui irriguent ces statistiques.*

- **[Monaco et la Bulgarie retirés de la liste GAFI](https://www.lcb-ft.fr/news/gafi-octobre-2026)** — *LCB-FT Fr, 30 octobre 2026*
  À l'issue de sa troisième réunion plénière de l'année, le GAFI retire Monaco et la Bulgarie (ainsi que la Côte d'Ivoire et la République démocratique du Congo) de sa liste grise ; aucun pays n'y est ajouté. Pour les assureurs assujettis LCB-FT, les juridictions de la liste grise conditionnent le niveau de vigilance complémentaire appliqué aux opérations et aux souscripteurs liés à ces pays.
  **Pourquoi c'est pertinent ?** La sortie de Monaco allège concrètement le traitement des dossiers liés à une place financière très présente dans les contrats vie et les patrimoines des clients privés français.
  *Impact réglementaire LCB-FT : mettre à jour les listes pays internes et les scénarios de scoring de risque dès la publication GAFI, pas seulement à la transposition.*

## 3. 🗂️ Exploitation de l'opendata

- **[L'AMF et l'ACPR mettent en garde contre plusieurs acteurs non autorisés (Forex, crypto-actifs)](https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0)** — *ACPR/AMF (communiqué conjoint), 22 octobre 2026*
  Les deux autorités publient une nouvelle mise en garde conjointe contre des plateformes proposant investissements Forex et produits dérivés sur crypto-actifs sans agrément, et actualisent leurs listes noires. Ces entités usurpent régulièrement des noms d'intermédiaires ou d'assureurs agréés pour démarcher les épargnants.
  **Pourquoi c'est pertinent ?** Cette liste est une entrée de contrôle gratuite : croiser les contreparties détectées en souscription ou en sinistre avec les listes noires AMF/ACPR filtre une partie des dossiers à risque dès la collecte.

- **[Listes noires des entités non autorisées à proposer des produits ou services financiers en France](https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france/)** — *data.gouv.fr / AMF (jeu de données), jeu de données actualisé (fichiers mis à jour en octobre 2026)*
  Jeu de données open data centralisant les listes noires AMF/ACPR sous forme de fichiers téléchargeables avec historique. Concrètement, il permet d'industrialiser un rapprochement automatique : importer les listes dans le SI souscription/réclamations et filtrer noms, domaines et identifiants signalés avant toute mise en relation.
  **Pourquoi c'est pertinent ?** Le chaînon entre l'alerte réglementaire et le contrôle automatique : un batch quotidien sur ce dataset élimine les faux courtiers et plateformes usurpées sans intervention manuelle.

## 4. 🕸️ Lutte contre les bandes organisées

- **[Un réseau d'escroquerie en bande organisée visant le financement de voitures démantelé en Ariège](https://www.ladepeche.fr/2026/10/21/500-000-euros-de-prejudice-faux-dossiers-de-credit-bmw-mercedes-ou-opel-vises-un-reseau-descroquerie-en-bande-organisee-touchant-des-voitures-13591111.php)** — *La Dépêche, 21 octobre 2026*
  Sept personnes ont comparu à Foix pour un réseau ayant monté de faux dossiers de crédit afin d'acquérir des véhicules haut de gamme (BMW, Mercedes, Opel) revendus ensuite, pour environ 500 000 euros de préjudice. Le schéma combine usurpation d'identité, faux justificatifs de revenus et complicités internes — un mode opératoire qui déborde directement sur les assureurs : financement, garantie, sinistres sur véhicules mal acquis.
  **Pourquoi c'est pertinent ?** La typologie « dossier complet frauduleux » (identité + revenus + justificatifs) est exactement celle que les fraudeurs réutilisent en souscription auto : le signalement croisé crédit/assurance est l'anticipation à construire.

- **[« Signalements anonymes », soupçons de corruption et enquête interne : ce scandale qui empoisonne Malakoff Humanis](https://www.lefigaro.fr/societes/signalements-anonymes-soupcons-de-corruption-et-enquete-interne-ce-scandale-qui-empoisonne-malakoff-humanis-le-geant-de-la-protection-sociale-20261028)** — *Le Figaro, 28 octobre 2026*
  Le deuxième groupe français de protection sociale est éclaboussé par des soupçons « de corruption commise en bande organisée » en interne : signalements anonymes, enquête interne et remises en cause de la gouvernance de la gestion déléguée. Le dossier illustre le risque de fraude interne et de prestataires, rarement mis en avant au profit de la fraude « client ».
  **Pourquoi c'est pertinent ?** La bande organisée n'est pas toujours externe : les contrôles en quatre yeux, l'audit des flux vers les prestataires et le traitement sérieux des lanceurs d'alerte font partie du dispositif anti-fraude.

## 5. 🚪 Fraude en entrée en relation

- **[Proposition de loi n° 3228 visant à mieux réprimer l'usurpation d'identité](https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi.pdf)** — *Assemblée nationale, 6 octobre 2026*
  Déposée le 6 octobre 2026, la proposition de loi renforce la répression de l'usurpation d'identité et organise le rétablissement rapide des victimes. Elle impose notamment l'inclusion d'une garantie minimale contre l'usurpation d'identité dans les contrats couvrant la responsabilité civile de la vie privée — soit une obligation nouvelle pour l'offre assurance.
  **Pourquoi c'est pertinent ?** Si elle est adoptée, la gestion des victimes (preuve, rétablissement, indemnisation) devient un processus à outiller : c'est un sujet de produit et de gestion, pas seulement de pénal.
  *Impact réglementaire : suivi du dossier législatif — nouvelle garantie obligatoire potentielle en RC vie privée et charges associées en gestion.*

- **[Rapport d'activité 2025 — focus « fraude » aux versements en assurance vie](https://www.mediation-assurance.org/wp-content/uploads/2026/09/Rapport_annuel_2025_LMA_page-simple.pdf)** — *La Médiation de l'assurance, septembre 2026*
  Le rapport annuel de la Médiation de l'assurance documente une hausse des saisines liées à des « fraudes » — souvent des abus de confiance — avec un focus consacré à la fraude aux versements en assurance vie : rachats déclenchés par un tiers, usurpation d'identité du souscripteur, faux RIB substitués aux coordonnées réelles du bénéficiaire.
  **Pourquoi c'est pertinent ?** Le signal du médiateur est un indicateur avancé : ces tentatives passent par la gestion (rachat, changement de coordonnées bancaires) et sont interceptables par des contrôles ciblés à ces deux points.

## 6. 🩺 Fraude à la santé

- **[Escroquerie et blanchiment en optique : une enquête met à jour une fraude à plusieurs millions d'euros](https://opticien-lunetier.media/2026/09/28/escroquerie-et-blanchiment-en-optique-une-enquete-met-a-jour-une-fraude-a-plusieurs-millions-deuros/)** — *Opticien-Lunetier (communiqué du parquet de Paris du 25/09/2026), 28 septembre 2026*
  Une enquête de la section économique et financière du parquet de Paris (avec l'OCLTI) débouche sur la convocation de 22 personnes physiques et 15 personnes morales devant le tribunal correctionnel de Paris : escroquerie et blanchiment en bande organisée dans le secteur de l'optique, aux dépens des organismes d'assurance maladie et des complémentaires santé, pour plusieurs millions d'euros de remboursements indus (montures et actes surfacturés ou fictifs).
  **Pourquoi c'est pertinent ?** Première affaire d'ampleur visant la filière optique côté réseaux de soins : le contrôle de la réalité des actes facturés aux complémentaires devient un chantier de détection à part entière.

- **[Fraude à l'Assurance Maladie : et si vous étiez le maillon décisif ?](https://www.ag2rlamondiale.fr/groupe/magazines/agir-a-vos-cotes/societe/fraude-a-l-assurance-maladie-et-si-vous-etiez-le-maillon-decisif)** — *AG2R La Mondiale, magazine « Agir à vos côtés », octobre 2026*
  Le magazine du groupe consacre son dossier d'octobre à la fraude à l'Assurance Maladie : 49 millions d'euros de fraudes aux arrêts de travail stoppées en 2025 (+17 %), le poste le plus surveillé côté assurés, et le rôle que l'employeur — premier destinataire des arrêts et témoin de la reprise d'activité — peut jouer comme capteur de première ligne.
  **Pourquoi c'est pertinent ?** L'arrêt de travail est le poste de fraude « assuré » n° 1 côté santé : l'employeur est le détecteur que les complémentaires et prévoyance peuvent contractualiser (visite de retour, signalement).

## 7. 🧪 Divers — sujet émergent

- **[Ordonnances, numéros de Sécu, mutuelle : des pirates revendiquent le vol de 436 000 dossiers de pharmacies](https://www.capital.fr/conso/ordonnances-numeros-de-secu-mutuelle-des-pirates-revendiquent-le-vol-de-436-000-dossiers-de-pharmacies-1531512)** — *Capital, 2 novembre 2026 (faits des 31 octobre-1er novembre)*
  En deux jours, trois officines (Paris, Strasbourg, Dijon) ont été victimes d'attaques revendiquées par des pirates : 436 000 dossiers patients exfiltrés, contenant ordonnances, numéros de Sécu et informations de mutuelle. Au-delà du cyber, ces données sont la matière première de la fraude aux remboursements : faux remboursements détournés, usurpation d'identité d'assuré, arbitrages frauduleux de tiers payant.
  **Pourquoi c'est pertinent ?** La fuite de données de soins se transforme en tentatives de fraude aux remboursements quelques semaines plus tard : le lien cyber/fraude doit être intégré aux scénarios de détection des complémentaires.
  *À surveiller : exploitation des fuites de données santé (usurpation d'identité assurantielle, faux dossiers de remboursement) comme typologie émergente.*

## Synthèse — 5 signaux faibles à surveiller

1. **Le coût du faux document tend vers zéro : la détection passe par les métadonnées et la preuve à la source.**
   https://www.jechange.fr/assurance/habitation/news/photos-degats-retouchees-ia-assureurs-detectent-metadonnees
   https://algopolis.eu/fr/article/19

2. **L'information anti-fraude se mutualise : listes grises du GAFI, listes noires AMF/ACPR actualisées et open data de contrôle.**
   https://www.lcb-ft.fr/news/gafi-octobre-2026
   https://acpr.banque-france.fr/fr/communiques-de-presse/lacpr-et-lamf-mettent-en-garde-le-public-contre-plusieurs-acteurs-proposant-en-france-des-0
   https://www.data.gouv.fr/datasets/listes-noires-des-entites-non-autorisees-a-proposer-des-produits-ou-services-financiers-en-france/

3. **Le législateur s'empare de l'usurpation d'identité, et le médiateur confirme la montée de la fraude aux versements en assurance vie.**
   https://www.assemblee-nationale.fr/dyn/17/textes/l17b3228_proposition-loi.pdf
   https://www.mediation-assurance.org/wp-content/uploads/2026/09/Rapport_annuel_2025_LMA_page-simple.pdf

4. **La fraude organisée frappe les réseaux de soins (optique) et désormais l'intérieur même d'un grand groupe de protection sociale.**
   https://opticien-lunetier.media/2026/09/28/escroquerie-et-blanchiment-en-optique-une-enquete-met-a-jour-une-fraude-a-plusieurs-millions-deuros/
   https://www.lefigaro.fr/societes/signalements-anonymes-soupcons-de-corruption-et-enquete-interne-ce-scandale-qui-empoisonne-malakoff-humanis-le-geant-de-la-protection-sociale-20261028

5. **Le cyber devient un vecteur direct de fraude aux remboursements : les fuites de données de pharmacies alimentent usurpations et faux dossiers.**
   https://www.capital.fr/conso/ordonnances-numeros-de-secu-mutuelle-des-pirates-revendiquent-le-vol-de-436-000-dossiers-de-pharmacies-1531512

---
Méthode : dates vérifiées sur la page de publication de chaque source (pièges JJ/MM vs MM/JJ contrôlés). L'entrée ACPR du 22 octobre a été vérifiée par extraction directe du site acpr.banque-france.fr (accessible en extraction, malgré le WAF signalé en navigation). Une seule entrée par événement ; le comparateur Jechange est retenu une seule fois, car il porte la méthode ALFA sans doublon. L'entrée Capital (02/11/2026) est en frontière de fenêtre : faits des 31 octobre-1er novembre, conservée comme sujet émergent. Sites blacklistés (lesnumeriques.com, degrouptest.com) : aucun utilisé. Entrées écartées : chronique JDN (journal d'éditeur), Paperjam (contenu sponsorisé Baloise), presse étrangère New York/Jaén (pas de fait que la presse française n'aurait pas).