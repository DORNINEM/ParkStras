#!/usr/bin/env python3
# Build HTML for veille-RH-IA-2026-08-31
import os

DATE = "2026-08-31"
DATE_DISPLAY = "31 août 2026"

def make_item(title, source, date, url, summary, tags, secteur, badge_type=None, badge_text=None, extra_class=""):
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    badge_html = ""
    if badge_type and badge_text:
        badge_html = f'<span class="meta-badge {badge_type}">{badge_text}</span>'
    
    return f"""<div class="article-card {extra_class}">
    <div class="article-header">
        <div class="article-title">{title}</div>
        {badge_html}
    </div>
    <div class="article-meta">
        <span class="meta-source">{source}</span>
        <span class="meta-date">{date}</span>
    </div>
    <div class="article-summary">{summary}</div>
    <div class="article-footer">
        <div class="article-tags">{tags_html}</div>
        <div class="article-sector">Secteur : {secteur}</div>
    </div>
    <div class="article-link" style="margin-top:8px;"><a href="{url}" target="_blank">🔗 Lire l'article</a></div>
</div>"""

articles_p1 = [
    make_item(
        "SAP People Analytics : l’IA au service de la décision RH",
        "SAP News Center", "août 2026",
        "https://news.sap.com/2026/08/people-analytics-powering-workforce-decision-making/",
        "SAP Business Data Cloud intègre les données workforce avec des insights IA pour anticiper les risques de départ, planifier les talents et supporter des décisions HCM autonomes. L’offre s’appuie sur SuccessFactors et promet une people intelligence en temps réel.",
        ["people analytics", "SAP SuccessFactors", "churn", "planification"], "Transversal", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "IA et SIRH : où en sont vraiment les éditeurs en 2026 ?",
        "ConvictionsRH / Mercer", "2026",
        "https://www.convictionsrh.com/ressources/ia-et-sirh-ou-en-sont-vraiment-les-editeurs-en-2026-notre-etude-exclusive-en-4-volets-pour-passer-de-lintention-a-laction/",
        "Étude exclusive Mercer basée sur plus de 50 éditeurs SIRH, analysant la maturité IA réelle par domaine RH (recrutement, paie, GEPP), les fondations techniques, l’éthique et les recommandations pour passer de l’intention à l’action.",
        ["SIRH", "éditeurs", "étude", "conformité"], "Transversal", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "Workday People Analytics : guide complet pour DRH (2026)",
        "AssistNow", "2026",
        "https://assistnow.com/blog/workday-people-analytics-guide",
        "Workday utilise le machine learning pour prédire l’attrition, analyser les tendances workforce et fournir des insights sur la santé organisationnelle via Prism Analytics. L’outil vise à réduire le turnover involontaire de 15-25 %.",
        ["Workday", "people analytics", "attrition", "Prism"], "Transversal", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "Top 11 des meilleurs logiciels GPEC en 2026",
        "Culture RH", "2026",
        "https://culture-rh.com/logiciel-rh/gpec/",
        "Panorama des solutions GPEC françaises intégrant l’IA pour l’analyse des écarts de compétences, le mapping des fiches de poste et l’intégration avec les SIRH (Cegid Talentsoft, Lucca, Zola).",
        ["GPEC", "SIRH", "compétences", "Talentsoft"], "Transversal", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "SAP SuccessFactors What’s New 2026",
        "SAP Help Portal", "2026",
        "https://help.sap.com/whats-new/8fcf4960eea24f78b1d7613da406a885",
        "Les releases 2026 de SuccessFactors ajoutent des assistants IA (Joule), des agents pour la talent intelligence et la planification workforce, renforçant la prédiction RH et les capacités analytics intégrées.",
        ["SAP SuccessFactors", "IA embarquée", "talent intelligence"], "Transversal", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "Baromètre IA RH 2026 : la grande mutation des métiers est lancée",
        "Parlons RH", "2026",
        "https://www.parlonsrh.com/barometre-ia-et-rh-2026-la-grande-mutation-des-metiers-a-commence/",
        "Le baromètre révèle que 25 % des tâches RH sont déjà remplacées par l’IA, 21 % de nouveaux rôles émergent, et que la fonction RH passe d’un mode administratif à un pilotage stratégique des compétences et de l’accompagnement humain augmenté.",
        ["people analytics", "GEPP", "mutation RH"], "Transversal", "badge-statut-deploiement", "En cours de déploiement"
    ),
]

articles_p2 = [
    make_item(
        "IA banque assurance 2026 : quels métiers disparaissent vraiment ?",
        "Mon Job en Danger", "2026",
        "https://monjobendanger.fr/blog/ia-banque-finance-assurance-france-2026-metiers-transformation",
        "Le secteur banque-assurance affiche 51,4 % d’exposition à l’IA (2e secteur le plus touché) ; 45 000 postes d’exécution pourraient être perdus d’ici 2030. Téléconseillers (70 %), analystes crédit juniors (72 %), comptables (68 %) et flow traders (75 %) sont les plus exposés.",
        ["banque", "assurance", "exposition IA"], "Banque/Assurance", "badge-risk-fort", "Risque : Fort"
    ),
    make_item(
        "IA et emploi : la note du Trésor et les métiers qualifiés exposés",
        "Actu IA", "juin 2026",
        "https://www.actuia.com/actualite/ia-et-emploi-la-note-du-tresor-et-les-metiers-qualifies-exposes/",
        "Note Trésor-Éco n°391 soulignant que l’IA expose désormais les métiers qualifiés en finance, assurance et informatique, là où les vagues précédentes touchaient surtout les manuels. L’insertion des jeunes et la formation sont identifiées comme leviers prioritaires.",
        ["Trésor", "métiers qualifiés", "France Stratégie"], "Transversal", "badge-risk-modere", "Risque : Modéré"
    ),
    make_item(
        "« Ce que les jeunes savent, les LLM savent déjà le faire »",
        "Les Numériques", "août 2026",
        "https://www.lesnumeriques.com/intelligence-artificielle/ce-que-les-jeunes-savent-les-llm-savent-deja-le-faire-comment-l-ia-devore-les-postes-d-entree-de-carriere-n260844.html",
        "Une étude Stanford s’appuyant sur les données ADP montre que l’emploi des développeurs 22-25 ans a baissé de près de 20 % depuis fin 2022 dans les rôles exposés à l’IA, tandis que les seniors progressent de 6 à 12 %. Les copilotes automatisent les tâches de codage routinières.",
        ["informatique", "développeur junior", "LLM"], "Informatique", "badge-risk-fort", "Risque : Fort"
    ),
    make_item(
        "Baromètre IA & Métiers 2026",
        "Inovapolis", "2026",
        "https://inovapolis.fr/barometre-ia-metiers/",
        "Les métiers du développement (92/100) et du test QA (85/100) sont en forte contraction face aux copilotes ; les administrateurs systèmes (68/100) mutent vers le cloud et l’orchestration. 78 % des développeurs utilisent déjà des assistants IA.",
        ["informatique", "testeurs", "administrateurs", "copilotes"], "Informatique", "badge-risk-fort", "Risque : Fort"
    ),
    make_item(
        "Plus de 200 000 emplois dans les banques menacés par l’IA d’ici 2030",
        "Les Échos", "2026",
        "https://www.lesechos.fr/finance-marches/banque-assurances/plus-de-200000-emplois-dans-les-banques-menaces-par-lintelligence-artificielle-dici-a-2030-2207295",
        "Morgan Stanley projette ~200 000 suppressions dans les banques européennes d’ici 2030 (~10 %), concentrées sur le back-office, le middle-office, la fraude et la conformité. Les établissements privilégient attrition et restructuration.",
        ["banque", "suppression", "conformité"], "Banque", "badge-risk-fort", "Risque : Fort"
    ),
    make_item(
        "AI and the Future of Insurance Talent",
        "BCG", "2026",
        "https://www.bcg.com/publications/2026/why-ai-demands-a-new-insurance-talent-model",
        "L’IA déplace l’assurance du traitement routinier de la souscription et des sinistres vers le jugement humain sur cas exceptionnels ; les pipelines de recrutement junior risquent de s’éroder car le volume d’apprentissage par la pratique diminue.",
        ["assurance", "talents", "souscripteurs"], "Assurance", "badge-risk-modere", "Risque : Modéré"
    ),
]

articles_p3 = [
    make_item(
        "Accord GEPP BPCE 2025 – 2028",
        "Groupe BPCE Newsroom", "2025",
        "https://newsroom.groupebpce.fr/actualites/le-groupe-bpce-signe-un-accord-sur-la-gestion-des-emplois-et-des-parcours-professionnels-integrant-de-maniere-inedite-un-volet-sur-lintelligence-artificielle-3cba1-7b707.html",
        "Accord inédit intégrant un volet IA générative, avec Campus Tech & Digital pour développer les compétences data, des parcours de carrière personnalisés et un accompagnement RH dédié aux collaborateurs du groupe bancaire et assurantiel.",
        ["GEPP", "banque", "accord"], "Banque/Assurance", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "Accord collectif GEPP au sein de l’UES Covéa (2026 – 2028)",
        "CFTC Covéa", "2026",
        "https://cftc-covea-france.fr/wp-content/uploads/2026/03/01.-Accord-collectif-relatif-a-la-GEPP-au-sein-de-lUES-Covea-2026-2028-signatures.pdf",
        "Accord couvrant la transformation IA et digitale, la formation et certification, la mobilisation du CPF, la nouvelle période de reconversion, ainsi que des mesures d’outplacement et de mobilité interne pour les salariés de l’assurance.",
        ["GEPP", "accord", "assurance"], "Assurance", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "La période de reconversion",
        "Ministère du Travail", "2026",
        "https://travail-emploi.gouv.fr/la-periode-de-reconversion",
        "Dispositif officiel remplaçant Pro-A depuis février 2026 : 150 à 450 heures de formation sur jusqu’à 12 mois, financement par l’OPCO et co-financement CPF possible, ouverture sur des certifications RNCP ou CQP, et maintien du contrat de travail en mobilité interne.",
        ["période de reconversion", "CPF", "OPCO"], "Transversal", "badge-statut-existant", "Existant"
    ),
    make_item(
        "OPCO Atlas : programme IA-tlas pour banque et assurance",
        "OPCO Atlas", "2026",
        "https://www.opco-atlas.fr/entreprise/nos-services/comment-tirer-profit-intelligence-artificielle-IA",
        "100 % de prise en charge pédagogique pour 6 modules IA dédiés aux entreprises de banque et assurance de moins de 50 salariés en 2026, avec microlearning et financement campusAtlas jusqu’au 31 décembre 2026.",
        ["OPCO Atlas", "formation IA", "financement"], "Banque/Assurance", "badge-statut-deploiement", "En cours de déploiement"
    ),
    make_item(
        "Formation IA Banque 2026 : Fraude, Crédit, KYC",
        "BGB Formation", "2026",
        "https://bgbformation.fr/formation-ia-banque",
        "Formation de 5 jours éligible CPF et OPCO Atlas sur les applications IA dans la banque et l’assurance : détection de fraude, scoring crédit, optimisation KYC et modélisation des risques. Public : professionnels banque, fintech, assureurs et régulateurs.",
        ["CPF", "OPCO Atlas", "formation", "banque"], "Banque/Assurance", "badge-statut-existant", "Existant"
    ),
    make_item(
        "Formation Mise en œuvre de l’IA générative dans la Banque, l’Assurance et les Mutuelles",
        "Capgemini Institut", "2026",
        "https://www.institut.capgemini.fr/formation/mise-en-oeuvre-de-l-ia-generative-dans-la-banque-l-assurance-et-les-mutuelles-sur-des-cas-d-usage-concrets/",
        "Formation pratique de 2 jours (14h) sur les concepts, cas d’usage concrets et perspectives de l’IA générative dans la banque et l’assurance (personnalisation, optimisation des risques, automatisation des rapports), sessions prévues en 2026 à Paris.",
        ["formation", "banque", "assurance", "IA générative"], "Banque/Assurance", "badge-statut-deploiement", "En cours de déploiement"
    ),
]

articles_p4 = [
    make_item(
        "AI Transformation Requires Redesigning Work, Not Cutting Roles",
        "Harvard Business Review", "août 2026",
        "https://hbr.org/2026/08/ai-transformation-requires-redesigning-work-not-cutting-roles",
        "Les organisations doivent redessiner les processus et les tâches autour des capacités de l’IA et des forces humaines plutôt que de se focaliser sur les réductions d’effectifs lors des restructurations IA. Le redesign des postes devient la priorité stratégique.",
        ["redesign", "job crafting", "augmentation"], "Transversal", "badge-horizon-court", "Court terme <2 ans"
    ),
    make_item(
        "Salesforce and others are hiring for this new $200,000+ AI job",
        "Forbes", "24 août 2026",
        "https://www.forbes.com/sites/rachelwells/2026/08/24/salesforce-and-others-are-hiring-for-this-new-200000-ai-job/",
        "Les entreprises créent des rôles de VP AI Workforce Transformation ou Chief AI Officer RH, hybrides entre RH, IT et stratégie, pour convertir les investissements IA en productivité, reclassement et résultats d’équipes hybrides.",
        ["nouveaux métiers", "Chief AI Officer", "DRH transformation"], "Transversal", "badge-horizon-court", "Court terme <2 ans"
    ),
    make_item(
        "The Future of Jobs Report 2025",
        "World Economic Forum", "janv. 2025",
        "https://www.weforum.org/publications/the-future-of-jobs-report-2025/",
        "170 millions de nouveaux jobs et 92 millions supprimés d’ici 2030 (net +78M) ; l’IA et les données sont les compétences clés. Banque/assurance/IT connaissent un turnover élevé ; les rôles cléricaux et de saisie déclinent, les fintech engineers et spécialistes IA explosent.",
        ["WEF", "prospective 2030", "banque", "assurance", "IT"], "Transversal", "badge-horizon-moyen", "Moyen terme 2-5 ans"
    ),
    make_item(
        "Travailler dans le monde de 2026 : le travail remodelé par l’IA",
        "Cognizant", "2026",
        "https://www.cognizant.com/fr/fr/aem-i/ai-and-the-future-of-work-report",
        "L’IA impacte 93 % des jobs plus vite que prévu, augmentant l’exposition aux tâches et nécessitant un redesign vers l’augmentation et des activités à plus haute valeur. Les modèles hybrides homme-machine deviennent la norme.",
        ["redesign", "hybridation", "impact psychologique"], "Transversal", "badge-horizon-court", "Court terme <2 ans"
    ),
    make_item(
        "Outils RH et intelligence artificielle : l’Europe repousse les obligations haut risque à décembre 2027",
        "Actu IA", "2026",
        "https://www.actuia.com/actualite/outils-rh-et-intelligence-artificielle-leurope-repousse-les-obligations-haut-risque-a-decembre-2027/",
        "L’UE décale les obligations AI Act pour les systèmes RH à haut risque (recrutement, évaluation, promotion) d’août 2026 à décembre 2027, tout en maintenant la classification high-risk. Les entreprises disposent d’un répit pour la mise en conformité.",
        ["EU AI Act", "CNIL", "réglementation"], "Transversal", "badge-horizon-court", "Court terme <2 ans"
    ),
    make_item(
        "Human-AI Collaborative Job Crafting and Employee Performance",
        "Frontiers in Psychology", "2026",
        "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1903517/full",
        "La recherche démontre que le job crafting collaboratif homme-IA améliore l’adéquation humain-machine et la performance au travail, à condition d’être soutenu par des pratiques RH inclusives et une clarté des rôles.",
        ["job crafting", "psychologie", "hybridation"], "Transversal", "badge-horizon-court", "Court terme <2 ans"
    ),
]

# Build HTML parts safely
header = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veille IA & Mutations RH — Banque · Assurance · Informatique — {DATE}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            line-height: 1.6;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        header {{
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border-bottom: 1px solid #334155;
        }}
        header h1 {{
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}
        header p {{ color: #94a3b8; font-size: 0.95rem; }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        .section-title {{
            font-size: 1.4rem;
            font-weight: 700;
            margin: 32px 0 16px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .section-apports .section-title {{ color: #2dd4bf; }}
        .section-risques .section-title {{ color: #fb923c; }}
        .section-dispositifs .section-title {{ color: #a78bfa; }}
        .section-prospective .section-title {{ color: #60a5fa; }}
        .article-card {{
            background: #1e293b;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            border-left: 4px solid #334155;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .article-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }}
        .section-apports .article-card {{ border-left-color: #14b8a6; }}
        .section-risques .article-card {{ border-left-color: #f97316; }}
        .section-dispositifs .article-card {{ border-left-color: #8b5cf6; }}
        .section-prospective .article-card {{ border-left-color: #3b82f6; }}
        .article-header {{
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 8px;
            margin-bottom: 8px;
        }}
        .article-title {{
            font-size: 1.05rem;
            font-weight: 600;
            color: #f1f5f9;
            flex: 1;
            min-width: 200px;
        }}
        .article-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 10px;
        }}
        .meta-source {{ color: #94a3b8; font-size: 0.85rem; }}
        .meta-date {{ color: #64748b; font-size: 0.85rem; }}
        .meta-badge {{
            font-size: 0.7rem;
            padding: 3px 10px;
            border-radius: 999px;
            font-weight: 600;
        }}
        .badge-risk-fort {{ background: rgba(249,115,22,0.2); color: #fb923c; }}
        .badge-risk-modere {{ background: rgba(234,179,8,0.2); color: #facc15; }}
        .badge-risk-faible {{ background: rgba(34,197,94,0.2); color: #4ade80; }}
        .badge-statut-existant {{ background: rgba(34,197,94,0.2); color: #4ade80; }}
        .badge-statut-deploiement {{ background: rgba(59,130,246,0.2); color: #60a5fa; }}
        .badge-statut-projet {{ background: rgba(168,85,247,0.2); color: #c084fc; }}
        .badge-horizon-court {{ background: rgba(59,130,246,0.2); color: #60a5fa; }}
        .badge-horizon-moyen {{ background: rgba(234,179,8,0.2); color: #facc15; }}
        .badge-horizon-long {{ background: rgba(148,163,184,0.2); color: #cbd5e1; }}
        .article-summary {{
            color: #cbd5e1;
            font-size: 0.95rem;
            margin-bottom: 10px;
        }}
        .article-footer {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            align-items: center;
        }}
        .article-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            flex: 1;
        }}
        .tag {{
            background: #334155;
            color: #e2e8f0;
            padding: 2px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
        }}
        .article-link a {{
            color: #38bdf8;
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
        }}
        .article-link a:hover {{ text-decoration: underline; }}
        .article-sector {{ color: #94a3b8; font-size: 0.85rem; }}
        .extra-sections {{ margin-top: 40px; }}
        .extra-section {{
            background: #1e293b;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            border: 1px solid #334155;
        }}
        .extra-section h2 {{
            font-size: 1.2rem;
            color: #f1f5f9;
            margin-bottom: 16px;
        }}
        .signal-item {{
            background: #0f172a;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            border-left: 3px solid #38bdf8;
        }}
        .signal-item strong {{ color: #f1f5f9; }}
        .dashboard-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 12px;
            font-size: 0.9rem;
        }}
        .dashboard-table th {{
            background: #0f172a;
            color: #38bdf8;
            text-align: left;
            padding: 12px;
            font-weight: 600;
            border-bottom: 2px solid #334155;
        }}
        .dashboard-table td {{
            padding: 12px;
            border-bottom: 1px solid #334155;
            color: #cbd5e1;
        }}
        .dashboard-table tr:hover td {{ background: #0f172a; }}
        .risk-fort {{ color: #fb923c; font-weight: 600; }}
        .risk-modere {{ color: #facc15; font-weight: 600; }}
        .risk-faible {{ color: #4ade80; font-weight: 600; }}
        footer {{
            text-align: center;
            padding: 40px 20px;
            color: #64748b;
            font-size: 0.85rem;
            border-top: 1px solid #334155;
            margin-top: 40px;
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 12px; }}
            header h1 {{ font-size: 1.3rem; }}
            .article-title {{ font-size: 0.95rem; }}
            .dashboard-table {{ font-size: 0.8rem; }}
            .dashboard-table th, .dashboard-table td {{ padding: 8px; }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>🤖 Veille IA & Mutations RH</h1>
            <p>Banque · Assurance · Informatique — """ + DATE_DISPLAY + """</p>
            <p style="margin-top:8px;font-size:0.85rem;">24 articles analysés • Sources primaires et institutionnelles</p>
        </div>
    </header>

    <div class="container">
        <!-- PARTIE 1 -->
        <div class="section-apports">
            <h2 class="section-title">🛠️ IA dans les métiers RH : apports & outils (6 articles)</h2>
""" + "\n".join(articles_p1) + """
        </div>

        <!-- PARTIE 2 -->
        <div class="section-risques">
            <h2 class="section-title">⚠️ Risques & transformations des métiers (6 articles)</h2>
""" + "\n".join(articles_p2) + """
        </div>

        <!-- PARTIE 3 -->
        <div class="section-dispositifs">
            <h2 class="section-title">🔄 Dispositifs d’accompagnement aux mutations (6 articles)</h2>
""" + "\n".join(articles_p3) + """
        </div>

        <!-- PARTIE 4 -->
        <div class="section-prospective">
            <h2 class="section-title">🔭 Prospective : travail, IA et société (6 articles)</h2>
""" + "\n".join(articles_p4) + """
        </div>

        <div class="extra-sections">
            <div class="extra-section">
                <h2>🖼️ Images & schémas analysés</h2>
                <p style="color:#cbd5e1;">Aucun visuel n’a été joint aux articles analysés pour cette édition. Les rapports cités (WEF Future of Jobs 2025, BCG Insurance Talent, OPCO Atlas, SAP Business Data Cloud) contiennent néanmoins des matrices emplois/automatisation, pyramides de compétences et roadmaps de transition accessibles en ligne.</p>
            </div>

            <div class="extra-section">
                <h2>📊 Synthèse — 5 signaux faibles à surveiller</h2>
                <div class="signal-item">
                    <strong>1. Le mur des juniors IT</strong> — l’emploi des développeurs 22-25 ans a chuté de ~20 % depuis fin 2022 (Stanford/ADP). Pour un DRH d’ESN, cela signifie repenser les plans de recrutement junior et miser sur l’alternance augmentée plutôt que sur des CDI classiques.
                </div>
                <div class="signal-item">
                    <strong>2. GEPP IA obligatoire</strong> — BPCE et Covéa intègrent pour la première fois un volet IA générative dans leurs accords GEPP. Ce modèle devrait devenir une norme de branche d’ici 2027 ; anticiper la négociation d’un volet similaire est un signal fort.
                </div>
                <div class="signal-item">
                    <strong>3. Période de reconversion vs Pro-A</strong> — le remplacement de Pro-A par la période de reconversion en février 2026 change les règles du financement ; les entreprises ont intérêt à former leurs managers RH à ce nouveau dispositif sous peine de perdre des jours-formation.
                </div>
                <div class="signal-item">
                    <strong>4. CNIL et AI Act en activation</strong> — la CNIL a fait de l’IA de recrutement un thème prioritaire de contrôle 2026, tandis que les obligations AI Act pour les systèmes à haut risque s’appliquent en deux temps (août 2026 puis décembre 2027). Les DPO et DRH doivent sécuriser leurs inventaires.
                </div>
                <div class="signal-item">
                    <strong>5. Érosion du pipeline junior en assurance</strong> — BCG alerte sur la réduction des volumes d’apprentissage pour les juniors en souscription et gestion de sinistres. Les directions formation doivent créer des parcours hybrides « IA + jugement métier » pour ne pas perdre la relève.
                </div>
            </div>

            <div class="extra-section">
                <h2>🗺️ Tableau de bord des métiers à risque</h2>
                <table class="dashboard-table">
                    <thead>
                        <tr><th>Secteur</th><th>Métier</th><th>Niveau de risque IA</th><th>Horizon</th><th>Piste de reconversion prioritaire</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>Banque</td><td>Conseiller clientèle (téléphone / chat)</td><td class="risk-fort">Fort</td><td>Court terme &lt;2 ans</td><td>Gestion de relation client premium et conseil patrimonial augmenté</td></tr>
                        <tr><td>Banque</td><td>Analyste crédit junior</td><td class="risk-fort">Fort</td><td>Court terme &lt;2 ans</td><td>Analyste risque data-driven, conformité et audit des modèles</td></tr>
                        <tr><td>Banque</td><td>Back-office / middle-office</td><td class="risk-fort">Fort</td><td>Moyen terme 2-5 ans</td><td>Supervision humaine des processus automatisés, contrôle interne</td></tr>
                        <tr><td>Banque</td><td>Agent de conformité / KYC</td><td class="risk-modere">Modéré</td><td>Court terme &lt;2 ans</td><td>Compliance IA et Risk Management augmenté</td></tr>
                        <tr><td>Assurance</td><td>Gestionnaire sinistres (tâches routinières)</td><td class="risk-fort">Fort</td><td>Court terme &lt;2 ans</td><td>Gestion des cas complexes, expertise indemnisation et relation client émotionnelle</td></tr>
                        <tr><td>Assurance</td><td>Souscripteur IARD standard</td><td class="risk-modere">Modéré</td><td>Moyen terme 2-5 ans</td><td>Souscripteur risques complexes, pricing IA et tarification dynamique</td></tr>
                        <tr><td>Informatique</td><td>Développeur junior</td><td class="risk-fort">Fort</td><td>Court terme &lt;2 ans</td><td>Architecte IA, ingénieur prompt, superviseur de code IA</td></tr>
                        <tr><td>Informatique</td><td>Testeur QA manuel</td><td class="risk-fort">Fort</td><td>Court terme &lt;2 ans</td><td>Stratège QA, auditeur de qualité IA, automatisation des tests</td></tr>
                        <tr><td>Informatique</td><td>Administrateur systèmes</td><td class="risk-modere">Modéré</td><td>Moyen terme 2-5 ans</td><td>Ingénieur cloud &amp; automatisation, gouvernance infrastructure IA</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <footer>
        <div class="container">
            Veille IA & Mutations RH — générée le """ + DATE + """ — sources primaires et institutionnelles
        </div>
    </footer>
</body>
</html>"""

output_path = os.path.expanduser("~/dev/ParkStras/HERMES/archives/veille-RH-IA-" + DATE + ".html")
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(header)

print(f"HTML written to {output_path}")
print(f"Size: {os.path.getsize(output_path)} bytes")
