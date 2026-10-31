# Veille Mistral AI — France · Europe & Monde · Usages entreprises

**31 octobre 2026** — Actualité de Mistral AI (entreprise, produits, positionnement, usages, tarifs) · fenêtre du 24 au 31 octobre 2026 · 12 articles + 5 signaux faibles + encadré tarifs

Synthèse : la semaine est dominée par la publication des poids ouverts de **Mistral Large 4 « Le Chonk »** (29 octobre), modèle multimodal Mixture-of-Experts d'environ 1 000 milliards de paramètres (≈52 Md actifs, 1 M de tokens de contexte), désormais téléchargeable sous la licence « Mistral Ecosystem Open-Weight License » (MIT modifiée, avec clause commerciale pour les hébergeurs de modèles). Mistral revendique la première place des modèles ouverts en code (FrontierCode 2.0 de Cognition, 19,7 %) et 41 % sur Terminal-Bench 4.0, à quasi-égalité avec le chinois GLM-5.3 sur le Coding Agent Index d'Artificial Analysis (48 %) tout en consommant 47 % de tokens en moins par tâche. La cybersécurité devient le terrain de différenciation : Orange Cyberdefense officialise le 29 octobre un partenariat (tests d'intrusion, réponse à incident) et Mistral cite CrowdStrike, Cloudflare, Rubrik, Zscaler, Fortinet, ENISA ou Booz Allen parmi les évaluateurs. Côté plateforme, Mistral ouvre une Responses API au format OpenAI (28 octobre, servie depuis l'UE et les États-Unis) et héberge désormais des modèles tiers (DeepSeek V4.1 Flash, GLM 5.3 Flash). Le recalibrage de l'Intelligence Index v5 d'Artificial Analysis (27–30 octobre, 60 % de tests privés) rappelle toutefois que l'écart entre modèles ouverts et fermés reste large : Large 4 final à 26 points, 7e des modèles ouverts, loin des 58 points de Claude Opus 5.5.

## 🇫🇷 Mistral en France

### [Mistral publie les poids de Large 4 « Le Chonk », meilleur modèle ouvert en code selon ses benchmarks](https://mistral.ai/fr/news/mistral-large-4-oss/)
*Mistral AI • 29/10/2026*

Trois semaines après son aperçu public, Mistral rend téléchargeables les poids de Mistral Large 4 (Le Chonk), un modèle multimodal à architecture Mixture-of-Experts d'environ 1 000 milliards de paramètres (≈52 Md actifs, fenêtre de contexte de 1 M de tokens). Sous la « Mistral Ecosystem Open-Weight License », il peut être utilisé, modifié et affiné sans frais, mais un hébergeur commercialisant un modèle en tant que service (MaaS) doit signer une licence séparée. La version finale progresse : 41 % sur Terminal-Bench 4.0 (+13 points sur l'aperçu, avec 30 % de tokens de sortie en moins) et première place des modèles ouverts sur FrontierCode 2.0 de Cognition (19,7 %) ; sur le Coding Agent Index d'Artificial Analysis, 48 %, à égalité avec GLM-5.3 mais avec 47 % de tokens en moins par tâche. Trois modes de raisonnement (low/medium/high) et un entraînement réalisé de bout en bout sur l'infrastructure européenne de Mistral.

### [Orange Cyberdefense et Mistral AI co-développent des services de cybersécurité sur une variante de Large 4](https://www.latribune.fr/article/tech/informatique/13271310428432/orange-cyberdefense-et-mistral-ai-unissent-leurs-forces-pour-creer-des-agents-ia-capable-de-deceler-les-failles-de-cybersecurite)
*La Tribune • 29/10/2026*

Le 29 octobre, Orange Cyberdefense officialise un partenariat stratégique avec Mistral AI, un jour après la publication des poids de Large 4. Deux services d'abord : des tests d'intrusion dopés par une déclinaison du modèle spécialement optimisée pour les usages cyber (déceler les failles avant exploitation), puis l'investigation post-incident et la réponse aux attaques, avec analyse accélérée des traces numériques. Toutes les actions critiques restent, selon les deux partenaires, sous responsabilité directe d'experts humains. Présentée comme une alternative française à Claude Mythos (Anthropic) et GPT-5.6-Cyber (OpenAI), l'alliance fait d'Orange Cyberdefense le premier partenaire européen de Mistral sur ce terrain.

### [Large 4 mis à l'épreuve en conditions réelles : ASML, Cisco, l'Agence spatiale européenne et le Crédit agricole](https://www.latribune.fr/article/tech/intelligence-artificielle/1239517926291914/large-4-comment-mistral-a-rattrape-les-ia-chinoises-en-code)
*La Tribune • 29/10/2026*

Pendant les trois semaines de préversion, Mistral a testé Large 4 chez quelques clients, dont ASML, Cisco, l'Agence spatiale européenne et le Crédit agricole, avant de publier les poids le 29 octobre. Pierre Stock, vice-président science, attribue la progression « significative » du modèle (de 28 % à 41 % sur Terminal-Bench en moins de trois semaines) à la méthode d'apprentissage par renforcement maison, présentée comme l'atout stratégique de la start-up face aux laboratoires chinois. Cette phase semi-ouverte est présentée comme la clé du bond de performance final.

### [Licence « MEOW » : l'ouverture de Large 4 s'accompagne d'une condition commerciale](https://www.informatiquenews.fr/mistral-large-4-poids-ouverts-251154)
*InformatiqueNews • 30/10/2026*

Contrairement à Large 3, publié sous Apache 2.0, Large 4 adopte la « Mistral Ecosystem Open-Weight License » (MEOW), dérivée de MIT mais assortie d'une restriction. Les entreprises peuvent télécharger, modifier, affiner et intégrer le modèle à leurs applications ; en revanche, un acteur qui fournit à des tiers un accès au modèle pour l'inférence ou l'entraînement (activité « Model-as-a-Service ») doit conclure un accord commercial avec Mistral. La licence exclut explicitement de cette définition les produits finaux intégrant le modèle dans des fonctionnalités précises, et protège les usages internes. Le fichier de licence est publié sur Hugging Face.

## 🌍 Mistral en Europe & dans le monde

### [Artificial Analysis recalibre son Intelligence Index : Large 4 7e modèle ouvert, l'écart ouvert/fermé persiste](https://www.actuia.com/actualite/mistral-large-4-passe-de-38-a-25-points-sur-le-nouvel-indice-dartificial-analysis/)
*ActuIA • mis à jour le 30/10/2026*

Artificial Analysis a publié le 27 octobre la version 5 de son Intelligence Index, fondée à 60 % sur des évaluations dont les jeux de test restent privés ou secrets. Conséquence : les modèles à poids ouverts suivis perdent de 12 à 16 points. Mistral Large 4 passe de 38 à 25 points sur l'aperçu, puis à **26 points** pour la version finale publiée le 29 octobre, ce qui le place au 7e rang des modèles à poids ouverts, devant Muse Spark Open (25) — mais loin des 58 points de Claude Opus 5.5, qui reste stable. ActuIA souligne que la version précédente de l'indice donnait des scores bien plus élevés (DeepSeek V4.1 Flash, MiMo-V2.6-Pro, GLM-5.3 dépassaient 44 points) : le recalibrage change la lecture de la rivalité entre modèles ouverts et fermés.

### [Large 4, « meilleur modèle ouvert construit en Occident », mais l'écart avec OpenAI et Anthropic demeure](https://fortune.com/2026/10/29/mistral-releases-new-model-large-4-and-claims-top-open-model-for-agentic-coding-and-cyber-defense/)
*Fortune • 29/10/2026*

Fortune rapporte que Mistral revendique, avec Large 4, avoir rejoint ses rivaux chinois à la frontière des modèles à poids ouverts : le modèle de 1 000 milliards de paramètres, disponible sur Hugging Face depuis le 29 octobre, serait le meilleur modèle ouvert occidental en code agentique et en cybersécurité. Il serait à égalité avec GLM-5.3 sur Terminal-Bench 4.0 et consommerait 47 % de tokens de moins par tâche. Les modèles propriétaires d'OpenAI et d'Anthropic restent toutefois devant en capacités globales : Anthropic Mythos 5.1 affiche 60,9 % sur le même banc d'essai. La valorisation de Mistral (~21 Md€) demeure très inférieure à celles de ses concurrents américains.

### [Le Responses API de Mistral arrive en préversion publique, au format OpenAI, servi depuis l'UE et les États-Unis](https://www.techtimes.com/articles/329673/20261029/mistral-adds-responses-api-making-european-infrastructure-drop-agent-pipelines.htm)
*TechTimes • 29/10/2026*

Annoncé le 28 octobre sur X et ouvert en préversion publique, le endpoint `/v1/responses` de Mistral adopte le format Responses d'OpenAI : chaque réponse sépare le texte, le raisonnement et les appels d'outils en items distincts. L'intérêt affiché est l'absence de réécriture pour les développeurs déjà sur le format OpenAI — changer l'URL de base et la clé d'API suffit. Le service fonctionne avec tous les modèles de chat hébergés par Mistral, dont Large 4, est accessible depuis l'UE et les États-Unis, et repose sur l'infrastructure européenne du fournisseur (RGPD natif). Il complète une gamme déjà composée des APIs Agents (2025) et Workflows (avril 2026).

### [Mistral héberge désormais des modèles ouverts tiers, dont DeepSeek V4.1 Flash](https://fourweekmba.com/ai-mistral-adds-deepseek-rated-above-large-4-at-under-1-3-price/)
*FourWeekMBA (d'après les annonces de Mistral sur X) • 28/10/2026*

Toujours le 28 octobre, Mistral annonce servir sur son API deux modèles chinois tiers : DeepSeek V4.1 Flash 1017 en préversion publique (1 M de tokens de contexte, servi « sans modification », 0,30 $/M à l'entrée et 1,20 $/M à la sortie) et Z.ai GLM 5.3 Flash, désormais en disponibilité générale (0,15 $/M entrée, 0,03 $/M en cache, 0,50 $/M sortie), tous deux sous licence MIT. Point notable relevé par l'analyste : DeepSeek V4.1 Flash obtient 32 points sur l'Intelligence Index v5, soit **7 points de plus que Large 4**, pour moins d'un tiers du prix catalogue — Mistral se positionne ainsi aussi comme agrégateur de modèles ouverts tiers, y compris concurrents.

## 💼 Usages & cas d'usage entreprises

### [Cyberdéfense : les grands éditeurs de sécurité valident Large 4 en conditions réelles](https://mistral.ai/fr/news/mistral-large-4-oss/)
*Mistral AI / Dealroom • 29/10/2026*

Mistral adosse la sortie de Large 4 aux retours d'une série d'acteurs de la cybersécurité : Booz Allen, Cisco, Cloudflare, CrowdStrike, Elastic, Fortinet, l'agence européenne ENISA, NVIDIA, Orange Cyberdefense, Rubrik et Zscaler figurent parmi les organisations citées comme testant ou soutenant le modèle. Sur l'Artificial Analysis Cyber Index, Large 4 obtient 51 % (détecter, reproduire et corriger des vulnérabilités sans casser le code existant), avec un taux de refus moyen de 96,6 % sur les requêtes cyber malveillantes — le plus élevé mesuré parmi les modèles ouverts selon Mistral. Une variante dédiée au pentest et au red-team est réservée à des partenaires vérifiés (dont Orange Cyberdefense).

### [Banque : Crédit Agricole Artificial Intelligence bâtit sa plateforme IA de groupe avec Mistral](https://presse.credit-agricole.com/le-credit-agricole-sallie-a-des-acteurs-europeens-de-premier-plan-pour-accelerer-le-deploiement-industriel-de-lintelligence-artificielle/?lang=fra)
*Crédit Agricole (communiqué) • 20/10/2026*

Hors fenêtre stricte mais structurant : le 20 octobre, Crédit Agricole Artificial Intelligence — la filiale IA du groupe, opérationnelle depuis septembre avec 150 collaborateurs — a annoncé un partenariat industriel avec Mistral. Au programme : construction de la plateforme IA servant l'ensemble des clients et collaborateurs, agent conversationnel pour les banques de proximité (Caisses régionales, LCL), transformation agentique des processus et cybersécurité. Les équipes mutualisent leurs ressources et le groupe adapte les modèles de langage à ses données pour optimiser performance et consommation de calcul. L'accord s'inscrit dans un plan d'investissement d'environ 500 M€ sur 2026-2028.

### [Cloudera intègre Mistral à son écosystème d'IA hybride pour la souveraineté des données](https://siliconangle.com/2026/10/28/cloudera-expands-its-ai-ecosystem-with-partnerships-and-packaged-blueprints/)
*SiliconANGLE • 28/10/2026*

Le 28 octobre, Cloudera a élargi son Enterprise AI Ecosystem en associant Mistral AI, Neo4j, Cartesia et VAST Data. Le partenariat avec Mistral, déjà existant, s'appuie sur le portefeuille du laboratoire (Large 4 de 1,05 billion de paramètres, Timestral pour la prévision, Robostral pour la navigation incarnée) et sa collaboration d'ingénierie avec NVIDIA. Objectif affiché : permettre aux entreprises de déployer des modèles à poids ouverts au plus près de leurs données, dans une logique de « sovereign AI inference » où le client garde le contrôle sur les données, les modèles et l'infrastructure. Marjorie Janiewicz, chief revenue officer de Mistral, met en avant la combinaison modèles + plateforme de données hybride.

### [Voix : la transcription de Mistral classée 2e, des agents vocaux pour les centres de contact](https://x.com/MistralAI/status/2115443720371814478)
*Mistral AI (X) • 28/10/2026*

Mistral a annoncé le 28 octobre que Voxtral Mini Transcribe 3 se classe n°2 sur le classement « Diarization + ASR » de Voice Arena. La famille Voxtral 3, lancée le 20 octobre, associe reconnaissance vocale, synthèse et un SDK d'agents vocaux bâti sur LiveKit (écoute, raisonnement avec appels d'outils et réponse vocale en un seul flux, plus de 50 langues). Elle vise explicitement les centres de contact, les assistants virtuels et les copilots mains libres, avec un choix entre API hébergée dans l'UE et auto-déploiement sur infrastructure cliente — un argument de souveraineté pour les secteurs régulés. Les modèles Voxtral 3 ne sont pas à poids ouverts.

## 💰 Tarifs du moment

*Sources : docs.mistral.ai/fr/inference/pricing, mistral.ai/fr/pricing et changelog Mistral — consultés le 31/10/2026. Les tarifs de préversion (Voxtral) peuvent évoluer.*

- **Mistral Large 4 (API)** : 0,70 $ /M de tokens en entrée · 0,07 $ /M en entrée mise en cache · 2,10 $ /M en sortie. Plusieurs comparateurs tiers évoquent une offre de lancement à moitié prix (0,68 $ / 2,09 $) face au tarif catalogue (1,36 $ / 4,18 $) — à confirmer sur la page officielle. Batch API : −50 % ; entrée en cache : jusqu'à −90 %.
- **Modèles plus légers** : Ministral 3 3B à partir de 0,10 $ /M ; Mistral Small 4 0,15 $ /M entrée / 0,60 $ /M sortie ; Mistral Medium 3.5 1,50 $ / 7,50 $ ; Mistral Large 3 0,50 $ / 1,50 $ (chiffres tiers, à recouper).
- **Modèles tiers hébergés par Mistral** : DeepSeek V4.1 Flash 0,30 $ / 1,20 $ par M ; GLM 5.3 Flash 0,15 $ /M entrée (0,03 $ en cache) / 0,50 $ /M sortie.
- **Audio (préversion Voxtral 3)** : agent vocal à 0,04 $/min (avec Mistral Small 4) ou 0,08 $/min (modèle plus grand) ; transcription Mini ≈ 0,0035 $/min ; synthèse vocale 13 $/million de caractères (chiffres tiers, tarifs de préversion).
- **Vibe (ex-Le Chat)** : Free ; **Pro 14,99 $/mois** ; **Team 24,99 $/utilisateur/mois** ; **Enterprise sur devis** (déploiements privés, modèles et agents personnalisés, SAML SSO, journaux d'audit, white label). Tarif étudiant vérifié : 5,99 $/mois.
- **Licences** : Large 4 sous licence ouverte (usage interne et intégration libres) ; hébergement en tant que service = licence commerciale. Voxtral 3 : pas de poids ouverts, auto-déploiement sous licence commerciale.

## 📡 Signaux faibles

1. **La licence « MEOW » (MIT modifiée) réserve la revente d'inférence à un accord commercial.** Large 4 abandonne l'Apache 2.0 de Large 3 : usage interne, fine-tuning et intégration applicative restent libres, mais tout service de modèles (MaaS) exige une licence payante — y compris pour des versions dérivées.
   - https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B/raw/main/LICENSE
   - https://www.globalbole.com/fr/post/fr-mistral-large4-open-weights-2026-10-30/
   - https://datanorth.ai/news/mistral-large-4-open-weights

2. **Le recalibrage de l'Intelligence Index v5 creuse l'écart ouvert/fermé.** 60 % de l'indice reposent désormais sur des jeux de tests privés ; les 11 modèles ouverts suivis perdent 12 à 16 points, ce qui rebat la hiérarchie au détriment de la lecture « les modèles ouverts rattrapent ».
   - https://www.actuia.com/actualite/mistral-large-4-passe-de-38-a-25-points-sur-le-nouvel-indice-dartificial-analysis/
   - https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5
   - https://www.actuia.com/actualite/gemini-4-carbon-premier-de-lindice-dartificial-analysis-est-reserve-aux-cyberdefenseurs/

3. **L'écart de puissance de calcul reste structurel.** Large 4 a été entraîné sur ~3 800 à 4 000 GPU Grace Blackwell (~10 MW) dans les centres européens de Mistral, quand OpenAI a entraîné GPT-6 Astra sur plus de 100 000 puces (site Stargate, Texas) et que Colossus (xAI) consomme ~2 GW.
   - https://www.businessinsider.es/tecnologia/mistral-ia-francesa-que-puede-darle-europa-musculo-que-necesita-frente-eeuu-china_7046922_0.html
   - https://www.planetegrandesecoles.com/mistral-ai-vs-openai

4. **Mistral s'ouvre à l'hébergement de modèles tiers, y compris chinois.** DeepSeek V4.1 Flash et GLM 5.3 Flash servis côte à côte avec Large 4, des endpoints régionaux UE/US facturés 1,1× le prix catalogue, et une présence sur OpenRouter : un glissement d'éditeur de modèles vers plateforme d'inférence multi-modèles.
   - https://fourweekmba.com/ai-mistral-adds-deepseek-rated-above-large-4-at-under-1-3-price/
   - https://docs.mistral.ai/resources/changelogs.md

5. **La famille vocale Voxtral 3 n'ouvre pas ses poids.** Contrairement à Voxtral Realtime (Apache 2.0), Voxtral 3 reste en API hébergée UE ou auto-déploiement sous licence commerciale — un choix qui pèse pour les secteurs régulés voulant l'on-prem, et qui limite la réutilisation hors écosystème Mistral.
   - https://tensoria.fr/blog/voxtral-3-agent-vocal-mistral-pme
   - https://docs.mistral.ai/fr/resources/changelogs

---

*Veille générée le 31 octobre 2026 par Hermes (skill veille-mistral-ai + template veille-html). Fenêtre 24–31 octobre 2026. Liens sources cliquables ; dates de publication vérifiées page par page ; aucune source sponsorisée.*
