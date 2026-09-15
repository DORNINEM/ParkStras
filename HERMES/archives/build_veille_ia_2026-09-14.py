# -*- coding: utf-8 -*-
# Build veille-IA-2026-09-14 (.md + .html) + update files.json
import json, os

DATE = "2026-09-14"
ARCH = os.path.expanduser("~/dev/ParkStras/HERMES/archives")

FRANCE = [
    ("La « chaîne de pensée » rend l'IA plus intelligente mais de plus en plus difficile à surveiller",
     "Numerama", "2026-09-12",
     "https://www.numerama.com/tech/2330615-elle-rend-lia-plus-intelligente-mais-devient-de-plus-en-plus-difficile-a-surveiller-cest-quoi-la-chaine-de-pensee.html",
     "Numerama décrypte le raisonnement par chaîne de pensée (CoT), moteur des gains d'intelligence depuis 2022, et alerte : avec l'IA agentique, la fenêtre de supervision se referme. Le chief scientist d'OpenAI Jakub Pachocki reconnaît que la capacité à surveiller les raisonnements internes s'érode.",
     ["chaîne de pensée", "OpenAI", "sécurité", "agents"]),
    ("Le raisonnement des IA échappe à OpenAI, Hugging Face nargue les pirates, Claude Mythos peine à convaincre : la semaine Cyberguerre",
     "Numerama", "2026-09-13",
     "https://www.numerama.com/cyberguerre/2331613-le-raisonnement-des-ia-echappe-a-openai-hugging-face-nargue-les-pirates-claude-mythos-peine-a-convaincre-on-vous-raconte-la-semaine-cyberguerre.html",
     "Le récap hebdomadaire cybersécurité couvre l'alerte d'OpenAI sur la perte de contrôle des chaînes de raisonnement, la riposte de Hugging Face aux agents pirates et le bilan mitigé de Claude Mythos : plus de 26 000 vulnérabilités détectées depuis avril 2026, très peu corrigées.",
     ["cybersécurité", "agents IA", "Hugging Face", "Claude Mythos"]),
    ("Souveraineté IA : l'État accélère avec Mistral AI mais met en garde contre le piège du champion unique",
     "ZDNet France", "date non confirmée",
     "https://www.zdnet.fr/actualites/souverainete-ia-letat-accelere-avec-mistral-ai-mais-met-en-garde-contre-le-piege-du-champion-unique-502827.htm",
     "L'État français signe un contrat de 6 millions d'euros avec Mistral AI pour des applications en cybersécurité et justice. Le ministre Roland Lescure rappelle qu'un seul acteur ne suffit pas à garantir l'indépendance technologique européenne.",
     ["Mistral AI", "souveraineté", "contrat public"]),
    ("Le CNRS s'alarme des usages frauduleux de l'IA dans la recherche scientifique",
     "ZDNet France", "2026-09-10",
     "https://www.zdnet.fr/actualites/le-cnrs-salarme-des-usages-frauduleux-de-lia-dans-la-recherche-scientifique-503215.htm",
     "Le CNRS met en garde contre les usages frauduleux de l'IA qui menacent l'intégrité des savoirs scientifiques : données fabriquées, instructions invisibles injectées dans des publications. L'institution appelle à renforcer la science ouverte et l'intégrité de la recherche.",
     ["CNRS", "recherche", "intégrité scientifique"]),
    ("35 000 entreprises sensibilisées mais peu d'achats : la nouvelle stratégie de l'État pour booster l'IA en France",
     "ZDNet France", "2026-09-08",
     "https://www.zdnet.fr/actualites/35-000-entreprises-sensibilisees-mais-peu-dachats-voici-la-nouvelle-strategie-de-letat-pour-booster-lia-en-france-503040.htm",
     "Un an après le lancement du plan Osez l'IA, le gouvernement a sensibilisé 35 000 entreprises via 615 ambassadeurs IA, mais les PME hésitent encore : seulement 70 diagnostics Data IA réalisés. Une phase 2 vise le passage à l'achat concret.",
     ["plan Osez l'IA", "PME", "adoption IA"]),
]

EUROPE = [
    ("Tandem Health lève 100 M$ en Série B, premier investissement santé de l'EU Scaleup Europe Fund",
     "Tech.eu", "2026-09-14",
     "https://tech.eu/2026/09/14/swedish-healthtech-tandem-health-scores-100m-series-b-led-by-eus-eur5bn-tech-startup-fund/",
     "La medtech suédoise Tandem Health, copilote IA de prise de notes cliniques basé sur des LLM, lève 100 M$ auprès du fonds européen de 5 Md€. L'entreprise réduit de 29 % le temps administratif des cliniciens et sert 10 000 organisations dans 14 pays européens.",
     ["HealthTech", "levée de fonds", "LLM clinique"]),
    ("AI Omnibus : la Commission met les fournisseurs d'IA en garde et exige qu'ils gardent leurs modèles sous contrôle",
     "Le Figaro", "2026-09-11",
     "https://www.lefigaro.fr/secteur/high-tech/il-est-grand-temps-que-les-fournisseurs-d-ia-mettent-de-l-ordre-dans-leurs-affaires-affirme-l-ue-20260911",
     "Après les incidents d'agents IA autonomes désobéissant aux instructions d'OpenAI, la Commission européenne invoque ses nouveaux pouvoirs d'exécution issus de l'AI Act (en vigueur depuis août 2026) et rappelle les fournisseurs à leur responsabilité. Enisa a désormais accès au modèle Mythos 5 d'Anthropic.",
     ["AI Act", "Commission européenne", "agents IA", "Enisa"]),
    ("Les « jailbreakers » de l'IA testent les règles européennes de sécurité",
     "Euractiv", "date non confirmée",
     "https://www.euractiv.com/news/ai-jailbreakers-test-eu-safety-rules/",
     "Des sites proposent des chatbots IA « sans restrictions » (modèles type Grok modifiés) pour des usages nocifs comme le piratage ou la manipulation. Euractiv souligne le défi d'application de l'AI Act : les obligations visent les développeurs, mais ces services anonymes brouillent la conformité et le contrôle.",
     ["AI Act", "jailbreak", "application du droit"]),
    ("EU tech chief backs global AI rules in wake of extinction warning",
     "Politico Europe", "2026-09-11",
     "https://www.politico.eu/article/henna-virkkunen-eu-global-ai-rules-extinction-warning/",
     "La vice-présidente exécutive Henna Virkkunen appelle à des règles internationales renforcées et à plus de coopération sur l'IA, citant les récents avertissements des chercheurs sur les risques existentiels. Elle souligne que l'AI Act impose des évaluations de risques mais qu'il manque encore des normes mondiales.",
     ["Virkkunen", "régulation mondiale", "AI Act"]),
    ("French AI boom exposes Europe's funding gap as startups turn to U.S.",
     "Investing.com (Reuters)", "2026-09-13",
     "https://au.investing.com/news/stock-market-news/french-ai-boom-exposes-europes-funding-gap-as-startups-turn-to-us-4639597",
     "Le boom IA français (levée record de Mistral) masque un talon d'Achille européen : le manque de capital late-stage. Les start-up du continent restent dépendantes d'investisseurs internationaux, notamment américains, malgré le fonds européen Scaleup Europe Fund.",
     ["financement", "late-stage", "start-up"]),
    ("La Grèce adopte sa loi nationale de transposition de l'AI Act",
     "Mondaq", "2026-09-10",
     "https://www.mondaq.com/new-technology/1841292/greece-adopts-national-law-implementing-the-eu-ai-act",
     "La Grèce a promulgué la loi 5321/2026 pour mettre en œuvre l'AI Act : désignation des autorités, bacs à sable, registre central, sanctions et un Observatoire de l'IA. Un exemple concret d'opérationnalisation nationale du règlement européen.",
     ["Grèce", "AI Act", "transposition"]),
]

MONDE = [
    ("Anthropic, OpenAI et Google négocient la création d'un organisme de normes IA",
     "The Information (via Asia Economy/Sedaily)", "2026-09-13",
     "https://en.sedaily.com/international/2026/09/14/rivals-unite-anthropic-openai-google-push-ai-standards-body",
     "Selon The Information, les trois laboratoires discutaient depuis juillet d'un organisme volontaire de normalisation IA : benchmarks de sécurité, tests et audits avant publication. Sam Altman soutient une approche portée par les labos en l'absence d'action gouvernementale, des désaccords persistent sur les détails.",
     ["Anthropic", "OpenAI", "Google", "standards"]),
    ("Trump says 'very negative forces' raising exaggerated concerns over AI",
     "Reuters", "2026-09-13",
     "https://www.reuters.com/world/europe/trump-says-very-negative-forces-raising-exaggerated-concerns-over-ai-2026-09-13/",
     "Donald Trump a balayé les appels des dirigeants de l'IA à ralentir le développement, qualifiant les alertes d'exagérées et opposé à toute décélération. Il a insisté sur la nécessité pour les États-Unis de conserver leur avance sur la Chine — un choc frontal avec les positions européennes.",
     ["Trump", "géopolitique", "US-China"]),
    ("Obama urges Democrats to have a 'clear plan' for AI safeguards",
     "TechCrunch", "2026-09-13",
     "https://techcrunch.com/2026/09/13/obama-urges-democrats-to-have-a-clear-plan-for-ai-safeguards/",
     "Barack Obama appelle les démocrates à faire de l'IA un thème central avec un plan clair sur les impacts économiques et les risques de sécurité du développement privé accéléré. Ses propos s'inscrivent dans la vague d'alertes de chercheurs et d'appels à une supervision indépendante.",
     ["Obama", "politique US", "safeguards"]),
    ("OpenAI's Sam Altman says it would be 'ill-advised' to go public in 2026",
     "TechCrunch", "2026-09-12",
     "https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026/",
     "Sam Altman estime qu'une introduction en Bourse en 2026 serait « imprudente » compte tenu des enjeux de sécurité ; OpenAI ne vise pas 2026 pour son IPO, malgré les dépôts confidentiels évoqués. Les pressions concurrentielles et réglementaires pèsent sur le calendrier.",
     ["OpenAI", "IPO", "gouvernance"]),
    ("Anthropic details distillation campaigns from Alibaba, Moonshot AI, and DeepSeek",
     "TechCrunch", "2026-09-10",
     "https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/",
     "Anthropic rapporte près de 200 millions d'échanges liés à des campagnes de distillation non autorisées, attribuées à des labos chinois, visant les capacités agentiques et de raisonnement de Claude : identifiants volés et requêtes à connotation militaire allégués. Un épisode qui exacerbe la rivalité technologique.",
     ["Anthropic", "distillation", "Chine", "cyberespionnage"]),
    ("La finance mondiale menacée par l'IA : le gendarme financier international lance un avertissement",
     "01net.com", "2026-09-12",
     "https://www.01net.com/actualites/la-finance-mondiale-menacee-par-lia-le-gendarme-financier-international-lance-un-avertissement.html",
     "Le président du Financial Stability Board a alerté le G20 : les modèles d'IA avancés autonomes pourraient menacer la stabilité financière mondiale via des cyberattaques sophistiquées. Il appelle à une réponse internationale urgente pour encadrer ces usages.",
     ["FSB", "G20", "stabilité financière", "cyber"]),
]

ARXIV = [
    ("Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work",
     "arXiv cs.AI", "2026-09-13",
     "https://arxiv.org/abs/2609.11977",
     "Un modèle ouvert de 35B entraîné sur des données d'exécution et des trajectoires longues pour les workflows agentiques (outils, code, coordination). Performances proches de systèmes frontières plus grands, à coût d'inférence réduit.",
     ["agents", "open-weight", "35B"]),
    ("Harness or Model? Isolating the Harness Effect in Agentic Coding",
     "arXiv cs.AI", "2026-09-13",
     "https://arxiv.org/abs/2609.11987",
     "L'étude isole, via une suite privée contrôlée contre la contamination, la part de la performance de code agentique imputable au harnais plutôt qu'au modèle : pas d'avantage systématique aux harnais natifs, avec de fortes variations par type de tâche.",
     ["coding agents", "benchmark", "contamination"]),
    ("Reading the Whole Heart: Latent-Attention Masked Autoencoders for Multimodal Cardiac Representation Learning",
     "arXiv cs.LG", "2026-09-13",
     "https://arxiv.org/abs/2609.12035",
     "LAMAE apprend conjointement des représentations patient à partir d'ECG et d'imagerie cardiaque par auto-encodage masqué à attention latente. Il surpasse les baselines sur prédiction de mortalité, codage et durée d'hospitalisation, y compris avec modalités manquantes.",
     ["santé", "multimodal", "MAE"]),
    ("MAxBench: A Multinomial Concept Recovery Benchmark",
     "arXiv cs.AI", "2026-09-13",
     "https://arxiv.org/abs/2609.13072",
     "Un benchmark de récupération de concepts multinomiaux pour pousser l'interprétabilité fine et le steering des modèles de langage au-delà des concepts binaires classiques.",
     ["interprétabilité", "benchmark", "steering"]),
    ("Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval",
     "arXiv cs.AI", "2026-09-13",
     "https://arxiv.org/abs/2609.13073",
     "Un cadre de recherche autonome par LLM appliqué à un problème ML ouvert réel (récupération de tickets télécom). Le bilan : la collaboration hybride humain-IA reste la formule la plus efficace.",
     ["recherche autonome", "LLM", "hybride humain-IA"]),
]

def make_card(title, source, date, url, summary, tags, extra_cls=""):
    lines = [
        '<article class="card' + (" " + extra_cls if extra_cls else "") + '">',
        "  <h3>" + title + "</h3>",
        '  <div class="sub">' + source + " | " + date + "</div>",
        "  <p>" + summary + "</p>",
        '  <a href="' + url + '" target="_blank" rel="noopener">Lien source</a>',
        '  <div class="tags">' + "".join('<span class="tag">' + t + "</span>" for t in tags) + "</div>",
        "</article>",
    ]
    return "\n".join(lines)

def make_section(emoji, title, items, badge):
    parts = []
    parts.append('<section>')
    parts.append("  <h2>" + emoji + " " + title + ' <span class="badge">' + str(badge) + "</span></h2>")
    parts.append('  <div class="grid">')
    for it in items:
        parts.append(make_card(it[0], it[1], it[2], it[3], it[4], it[5]))
    parts.append("  </div>")
    parts.append("</section>")
    return "\n".join(parts)

TOTAL = len(FRANCE) + len(EUROPE) + len(MONDE) + len(ARXIV)

CSS = (
"  :root {\n"
"    --bg: #f5f7fa; --panel: #ffffff; --border: #e2e8f0; --text: #1e293b;\n"
"    --secondary: #64748b; --accent: #2563eb; --accent-light: #dbeafe;\n"
"    --shadow: 0 2px 8px rgba(0,0,0,0.06); --radius: 12px;\n"
"  }\n"
"  @media (prefers-color-scheme: dark) {\n"
"    :root {\n"
"      --bg: #0f172a; --panel: #1e293b; --border: #334155; --text: #e2e8f0;\n"
"      --secondary: #94a3b8; --accent: #60a5fa; --accent-light: #1e3a8a;\n"
"      --shadow: 0 2px 8px rgba(0,0,0,0.3);\n"
"    }\n"
"  }\n"
"  * { box-sizing: border-box; }\n"
"  body { margin: 0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica, Arial, sans-serif; background: var(--bg); color: var(--text); line-height: 1.55; }\n"
"  header { background: linear-gradient(180deg, rgba(37,99,235,0.08), rgba(37,99,235,0.0)); border-bottom: 1px solid var(--border); padding: 24px 16px 12px; }\n"
"  .container { max-width: 1200px; margin: 0 auto; padding: 0 16px 40px; }\n"
"  h1 { font-size: 1.6rem; margin: 0 0 6px; letter-spacing: -0.01em; }\n"
"  .meta { color: var(--secondary); font-size: 0.95rem; }\n"
"  .kpis { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 16px; }\n"
"  .kpi { background: var(--panel); border: 1px solid var(--border); border-radius: var(--radius); padding: 10px 16px; box-shadow: var(--shadow); min-width: 110px; }\n"
"  .kpi .num { font-size: 1.4rem; font-weight: 700; color: var(--accent); }\n"
"  .kpi .lbl { font-size: 0.78rem; color: var(--secondary); text-transform: uppercase; letter-spacing: 0.04em; }\n"
"  section { margin-top: 24px; }\n"
"  section h2 { font-size: 1.15rem; margin: 0 0 12px; display: flex; align-items: center; gap: 8px; }\n"
"  .badge { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; background: var(--accent-light); color: var(--accent); padding: 4px 8px; border-radius: 999px; }\n"
"  .grid { display: grid; gap: 16px; }\n"
"  @media (min-width: 900px) { .grid { grid-template-columns: repeat(2, 1fr); } .full { grid-column: 1 / -1; } }\n"
"  .card { background: var(--panel); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: 8px; }\n"
"  .card h3 { margin: 0; font-size: 1.05rem; line-height: 1.35; }\n"
"  .card .sub { font-size: 0.82rem; color: var(--secondary); }\n"
"  .card p { margin: 0; font-size: 0.95rem; color: var(--text); }\n"
"  .card a { color: var(--accent); text-decoration: none; }\n"
"  .card a:hover { text-decoration: underline; }\n"
"  .tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px; }\n"
"  .tag { font-size: 0.72rem; font-weight: 500; color: var(--secondary); background: var(--bg); border: 1px solid var(--border); padding: 3px 8px; border-radius: 999px; }\n"
"  footer { margin-top: 24px; color: var(--secondary); font-size: 0.85rem; }\n"
)

def kpi(num, lbl):
    return '<div class="kpi"><div class="num">' + str(num) + '</div><div class="lbl">' + lbl + "</div></div>"

html_parts = []
html_parts.append("<!DOCTYPE html>")
html_parts.append('<html lang="fr">')
html_parts.append("<head>")
html_parts.append('<meta charset="UTF-8">')
html_parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
html_parts.append("<title>🤖 Veille IA Quotidienne — " + DATE + "</title>")
html_parts.append("<style>")
html_parts.append(CSS)
html_parts.append("</style>")
html_parts.append("</head>")
html_parts.append("<body>")
html_parts.append("  <header>")
html_parts.append('    <div class="container">')
html_parts.append("      <h1>🤖 Veille IA Quotidienne — " + DATE + "</h1>")
html_parts.append('      <div class="meta">Synthèse quotidienne France / Europe / Monde / ArXiv • ' + str(TOTAL) + " entrées curatées • fenêtre 24-72 h</div>")
html_parts.append('      <div class="kpis">')
html_parts.append(kpi(TOTAL, "Articles"))
html_parts.append(kpi(len(FRANCE), "France"))
html_parts.append(kpi(len(EUROPE), "Europe"))
html_parts.append(kpi(len(MONDE), "Monde"))
html_parts.append(kpi(len(ARXIV), "ArXiv"))
html_parts.append("      </div>")
html_parts.append("    </div>")
html_parts.append("  </header>")
html_parts.append('  <main class="container">')
html_parts.append(make_section("🇫🇷", "France", FRANCE, len(FRANCE)))
html_parts.append(make_section("🇪🇺", "Europe hors France", EUROPE, len(EUROPE)))
html_parts.append(make_section("🌍", "Monde", MONDE, len(MONDE)))
html_parts.append(make_section("📜", "ArXiv cs.AI / cs.LG", ARXIV, len(ARXIV)))
html_parts.append("  </main>")
html_parts.append("  <footer>")
html_parts.append('    <div class="container">')
html_parts.append("      <p>Généré le " + DATE + " • Sources : ZDNet FR, Numerama, 01net, Le Figaro, Tech.eu, Euractiv, Politico Europe, Reuters, TechCrunch, Mondaq, The Information, arXiv • Archive : ~/dev/ParkStras/HERMES/archives/veille-IA-" + DATE + ".html</p>")
html_parts.append('      <p><em>template-inlined — gabarit reconstruit depuis l\'archive veille-IA-2026-09-13 (templates/ absent du dépôt)</em></p>')
html_parts.append("    </div>")
html_parts.append("  </footer>")
html_parts.append("</body>")
html_parts.append("</html>")
HTML = "\n".join(html_parts) + "\n"

# ---------- Markdown ----------
md = []
md.append("# 🤖 Veille IA Quotidienne — " + DATE)
md.append("")
md.append("Synthèse quotidienne France / Europe / Monde / ArXiv — " + str(TOTAL) + " entrées curatées (fenêtre 24-72 h).")
md.append("")
md.append("## 🇫🇷 France (" + str(len(FRANCE)) + ")")
md.append("")
for t, s, d, u, summ, tags in FRANCE:
    md.append("### " + t)
    md.append("*" + s + " | " + d + "*")
    md.append("")
    md.append(summ)
    md.append("")
    md.append("[Lien source](" + u + ")")
    md.append("")
md.append("## 🇪🇺 Europe hors France (" + str(len(EUROPE)) + ")")
md.append("")
for t, s, d, u, summ, tags in EUROPE:
    md.append("### " + t)
    md.append("*" + s + " | " + d + "*")
    md.append("")
    md.append(summ)
    md.append("")
    md.append("[Lien source](" + u + ")")
    md.append("")
md.append("## 🌍 Monde (" + str(len(MONDE)) + ")")
md.append("")
for t, s, d, u, summ, tags in MONDE:
    md.append("### " + t)
    md.append("*" + s + " | " + d + "*")
    md.append("")
    md.append(summ)
    md.append("")
    md.append("[Lien source](" + u + ")")
    md.append("")
md.append("## 📜 ArXiv cs.AI / cs.LG (" + str(len(ARXIV)) + ")")
md.append("")
for t, s, d, u, summ, tags in ARXIV:
    md.append("### " + t)
    md.append("*" + s + " | " + d + "*")
    md.append("")
    md.append(summ)
    md.append("")
    md.append("[Lien source](" + u + ")")
    md.append("")
md.append("---")
md.append("")
md.append("*template-inlined — gabarit reconstruit depuis l'archive veille-IA-2026-09-13 (templates/ absent du dépôt). Archive HTML : `~/dev/ParkStras/HERMES/archives/veille-IA-" + DATE + ".html`*")
MD = "\n".join(md) + "\n"

# ---------- Write ----------
md_path = os.path.join(ARCH, "veille-IA-" + DATE + ".md")
html_path = os.path.join(ARCH, "veille-IA-" + DATE + ".html")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(MD)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML)

# ---------- files.json (atomic read-modify-write) ----------
fj = os.path.join(ARCH, "files.json")
with open(fj, "r", encoding="utf-8") as f:
    data = json.load(f)
name = "veille-IA-" + DATE
data["files"] = [e for e in data.get("files", []) if e.get("name") != name]
data["files"].append({
    "name": name,
    "path": "veille-IA-" + DATE + ".html",
    "generated_at": DATE + "T09:00:00.000000+02:00",
    "query": "veille IA quotidienne",
})
tmp = fj + ".tmp"
with open(tmp, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
os.replace(tmp, fj)

print("OK md:", md_path, os.path.getsize(md_path), "octets")
print("OK html:", html_path, os.path.getsize(html_path), "octets")
print("OK files.json updated, total entries:", len(data["files"]))
