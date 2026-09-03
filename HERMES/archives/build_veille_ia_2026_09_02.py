#!/usr/bin/env python3
import json
import os
from datetime import datetime

DATE = "2026-09-02"
DATE_DISPLAY = "2 septembre 2026"
ARCHIVE_DIR = os.path.expanduser("~/dev/ParkStras/HERMES/archives")
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Data
france_items = [
    {
        "title": "Après la séquence de cyberattaques par des IA en test, OpenAI va bientôt lancer son modèle de pointe, Astra, mais corseté",
        "source": "Le Monde",
        "date": "02/09/2026",
        "url": "https://www.lemonde.fr/pixels/article/2026/09/02/apres-la-sequence-de-cyberattaques-par-des-ia-en-test-openai-va-bientot-lancer-son-modele-de-pointe-astra-mais-corsete_6763596_4408996.html",
        "summary": "OpenAI annonce que son modèle Astra peut découvrir et exploiter des vulnérabilités de façon autonome, atteignant le plus haut niveau de risque dans ses évaluations internes de cybersécurité. Le lancement est prévu prochainement avec un renforcement des safeguards et une surveillance accrue pour interrompre les actions non autorisées."
    },
    {
        "title": "IA au travail : une lente réglementation pour éviter les discriminations dans la gestion des ressources humaines",
        "source": "Le Monde",
        "date": "02/09/2026",
        "url": "https://www.lemonde.fr/emploi/article/2026/09/02/ia-au-travail-une-lente-reglementation-pour-eviter-les-discriminations-dans-la-gestion-des-ressources-humaines_6763873_1698637.html",
        "summary": "De nombreuses applications IA dans les RH (tri de CV, matching, analyse vidéo) sont classées à haut risque par l'AI Act européen, certaines étant strictement interdites. Les obligations générales pour les entreprises ne s'appliqueront pleinement que fin 2027, avec un maintien de la supervision humaine."
    },
    {
        "title": "L’IA obligatoire en classe de seconde, mais l'an prochain !",
        "source": "ZDNet FR",
        "date": "01/09/2026",
        "url": "https://www.zdnet.fr/actualites/lia-obligatoire-en-classe-de-seconde-mais-lan-prochain-500969.htm",
        "summary": "Le gouvernement français rendra l'enseignement de l'intelligence artificielle obligatoire en classe de seconde dès la rentrée 2027, avec un focus sur la maîtrise des IA génératives, l'éthique, la gestion des données et la cybersécurité, intégré progressivement sur tous les niveaux."
    },
    {
        "title": "OpenAI met en garde : des attaques « sophistiquées » menées par des essaims d'IA pourraient survenir d'ici quelques mois",
        "source": "ZDNet FR",
        "date": "01/09/2026",
        "url": "https://www.zdnet.fr/actualites/openai-met-en-garde-des-attaques-sophistiquees-menees-par-des-essaims-dia-pourraient-survenir-dici-quelques-mois-voici-ce-que-les-experts-recommandent-aux-entreprises-sur-ce-point-500996.htm",
        "summary": "OpenAI alerte sur des cyberattaques sophistiquées menées par des essaims d'agents IA dans les prochains mois, s'appuyant sur des incidents récents comme la compromission de Hugging Face. Les experts recommandent de renforcer les défenses cyber de base et de préparer des réponses spécifiques aux menaces agentiques."
    },
    {
        "title": "La finance mondiale menacée par l’IA : le gendarme financier international lance un avertissement",
        "source": "01net",
        "date": "01/09/2026",
        "url": "https://www.01net.com/actualites/la-finance-mondiale-menacee-par-lia-le-gendarme-financier-international-lance-un-avertissement.html",
        "summary": "Le président du Financial Stability Board alerte les ministres des Finances du G20 sur les risques des modèles d'IA de pointe pour la stabilité financière mondiale, notamment via des cyberattaques autonomes sophistiquées. Il souligne les menaces transfrontalières interconnectées et appelle à des réponses coordonnées."
    }
]

europe_items = [
    {
        "title": "Cambridge University spinout launches AI model 'competitive' with OpenAI and Anthropic",
        "source": "Tech.eu",
        "date": "01/09/2026",
        "url": "https://tech.eu/2026/09/01/cambridge-university-spinout-launches-ai-model-competitive-with-openai-and-anthropic/",
        "summary": "Flower Labs, spin-out de Cambridge, lance Endeavor 1.0, un modèle généraliste compétitif avec OpenAI et Anthropic, déployable localement comme alternative souveraine européenne aux modèles fermés américains, combinant open source et raisonnement propriétaire."
    },
    {
        "title": "AWS rachète DuckLabs : ce que le deal change pour l’analytique et l’open source",
        "source": "Silicon.fr",
        "date": "01/09/2026",
        "url": "https://www.silicon.fr/data-ia-1372/aws-rachete-ducklabs-ce-que-le-deal-change-pour-lanalytique-et-lopen-source-228834",
        "summary": "AWS acquiert DuckLabs, créateur de DuckDB, pour renforcer ses capacités d'analytique légère open source. L'équipe rejoint AWS tandis que la base de données reste open source sous licence MIT, gérée par la DuckDB Foundation."
    },
    {
        "title": "Meta to put its own AI chip into production in September",
        "source": "The Next Web",
        "date": "01/09/2026",
        "url": "https://thenextweb.com/news/meta-mtia-ai-chip-production-september",
        "summary": "Meta commence la production de sa puce IA interne MTIA en septembre 2026, ciblant un doublement de la capacité de calcul de ses datacenters et une réduction de la dépendance aux GPU Nvidia, grâce à un partenariat avec TSMC et Broadcom."
    },
    {
        "title": "EXCLUSIVE: EU orders leading AI labs to detail security practices",
        "source": "EURACTIV",
        "date": "27/08/2026",
        "url": "https://www.euractiv.com/news/exclusive-eu-orders-leading-ai-labs-to-detail-security-practices/",
        "summary": "La Commission européenne utilise pour la première fois ses nouveaux pouvoirs d'exécution de l'AI Act, demandant aux principaux développeurs IA des détails sur leurs pratiques de cybersécurité, sécurité et conformité pour les modèles les plus avancés."
    },
    {
        "title": "A DeepMind exec finally said what the trillion-dollar AI spend is for: machines that improve themselves",
        "source": "The Next Web",
        "date": "28/08/2026",
        "url": "https://thenextweb.com/news/deepmind-sekhon-ai-capex-recursive-self-improvement-rsi",
        "summary": "Le directeur stratégique de Google DeepMind révèle que les dépenses massives en IA visent principalement à développer des systèmes d'auto-amélioration récursive où l'IA améliore elle-même ses capacités, bien que les revenus actuels ne justifient pas encore ces investissements."
    }
]

world_items = [
    {
        "title": "Your files stay put: Perplexity’s hybrid AI keeps confidential data off the cloud",
        "source": "VentureBeat",
        "date": "01/09/2026",
        "url": "https://venturebeat.com/orchestration/your-files-stay-put-perplexitys-hybrid-ai-keeps-confidential-data-off-the-cloud",
        "summary": "Perplexity lance le calcul hybride pour sa plateforme Computer agent, répartissant les tâches entre modèles frontier cloud et modèles locaux open-weight sur Apple silicon, avec une Privacy Gate pour les données sensibles."
    },
    {
        "title": "OpenClaw 2.0 is here, ushering in the era of 'multiplayer' AI coding",
        "source": "VentureBeat",
        "date": "01/09/2026",
        "url": "https://venturebeat.com/technology/openclaw-2-0-is-here-what-it-means-for-enterprises",
        "summary": "OpenClaw 2.0 ajoute collaboration multi-utilisateurs, sessions cloud partagées, mémoire et sécurité renforcée, évoluant d'outil individuel vers infrastructure partagée pour workflows agentiques en entreprise."
    },
    {
        "title": "Anthropic's Claude Fable 5.1 and Mythos 5.1 arrive with a 75% cost reduction for Fable cache reads",
        "source": "VentureBeat",
        "date": "01/09/2026",
        "url": "https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads",
        "summary": "Anthropic lance Claude Fable 5.1 (général) et Mythos 5.1 (restreint cybersécurité et sciences de la vie) avec une réduction de 75% du prix des lectures en cache, ciblant les tâches agentiques longues et complexes."
    },
    {
        "title": "Frontier models can recover up to 65% of facts they can't directly recall — just by thinking longer",
        "source": "VentureBeat",
        "date": "01/09/2026",
        "url": "https://venturebeat.com/orchestration/frontier-models-can-recover-up-to-65-of-facts-they-cant-directly-recall-just-by-thinking-longer",
        "summary": "Une étude Google Research montre que les modèles frontier peuvent récupérer 40-65% des faits non rappelés directement en augmentant le temps d'inférence, remettant en question l'usage systématique du RAG."
    },
    {
        "title": "John Ternus hypes 'huge launch next week' in first memo as Apple CEO",
        "source": "TechCrunch",
        "date": "01/09/2026",
        "url": "https://techcrunch.com/2026/09/01/john-ternus-hypes-huge-launch-next-week-in-first-memo-as-apple-ceo/",
        "summary": "Le nouveau PDG d'Apple John Ternus annonce un événement majeur le 9 septembre 2026, probablement un iPhone pliable et un déploiement élargi de Siri AI, marquant le passage de témoin après Tim Cook."
    },
    {
        "title": "Anthropic's Claude designed working protein binders, and beat human experts on some",
        "source": "The Next Web",
        "date": "28/08/2026",
        "url": "https://thenextweb.com/news/anthropic-claude-protein-design-chemistry",
        "summary": "Anthropic rapporte que Claude a conçu des protéines fonctionnelles pour 14 cibles sur 15, surpassant parfois les experts humains en force de liaison, ouvrant la voie à une accélération de la découverte de médicaments et de la recherche en chimie."
    }
]

arxiv_items = [
    {
        "title": "Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation",
        "source": "arXiv",
        "date": "01/09/2026",
        "url": "https://arxiv.org/abs/2609.01604",
        "summary": "Étude sur les mécanismes de jugement des LLMs dans l'évaluation de résumés, analysant comment les modèles évaluent la qualité au-delà des simples scores pour améliorer la fiabilité des benchmarks d'évaluation."
    },
    {
        "title": "Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation",
        "source": "arXiv",
        "date": "01/09/2026",
        "url": "https://arxiv.org/abs/2609.01603",
        "summary": "Propose une méthode d'évaluation efficace pour les agents de génie logiciel en prenant en compte les trajectoires d'exécution, améliorant la comparabilité et la fiabilité des benchmarks sur des tâches de développement réel."
    },
    {
        "title": "Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation",
        "source": "arXiv",
        "date": "01/09/2026",
        "url": "https://arxiv.org/abs/2609.01601",
        "summary": "Présente une approche de récupération adaptive pour la génération de code à l'échelle d'un dépôt, identifiant les tokens critiques pour améliorer la pertinence du contexte et les performances des modèles."
    },
    {
        "title": "CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?",
        "source": "arXiv",
        "date": "01/09/2026",
        "url": "https://arxiv.org/abs/2609.01600",
        "summary": "Introduit CordisBench, un benchmark pour évaluer le raisonnement des modèles de langage sur les cycles de vie de composants dans des harnais d'agents dynamiques, révélant des limites dans la gestion d'états complexes."
    },
    {
        "title": "The Rise of Verbal Reinforcement Learning",
        "source": "arXiv",
        "date": "01/09/2026",
        "url": "https://arxiv.org/abs/2609.01597",
        "summary": "Explore le renforcement verbal comme paradigme d'apprentissage où les retours textuels remplacent les récompenses numériques, ouvrant de nouvelles voies pour l'alignement et l'apprentissage interactif des LLMs."
    }
]

# Helpers
def make_item(item):
    return f"""<div class="item">
<h3><a href="{item['url']}" target="_blank">{item['title']}</a></h3>
<div class="meta">{item['source']} • {item['date']}</div>
<p>{item['summary']}</p>
</div>"""

def make_card(title, items):
    card_items = "\n".join(make_item(i) for i in items)
    return f"""<div class="card">
<div class="card-head"><div class="card-title">{title}</div></div>
<div class="card-body">
{card_items}
</div>
</div>"""

# Markdown
md_lines = [
    f"# Veille IA quotidienne — {DATE_DISPLAY}",
    f"",
    f"**Sources FR/EU + Monde — généré automatiquement par Hermes**",
    f"",
    f"## 🇫🇷 France ({len(france_items)} articles)",
    f"",
]
for item in france_items:
    md_lines.append(f"- [{item['title']}]({item['url']}) — *{item['source']}*, {item['date']}")
    md_lines.append(f"  {item['summary']}")
    md_lines.append(f"")

md_lines.append(f"## 🌍 Europe hors France ({len(europe_items)} articles)")
md_lines.append(f"")
for item in europe_items:
    md_lines.append(f"- [{item['title']}]({item['url']}) — *{item['source']}*, {item['date']}")
    md_lines.append(f"  {item['summary']}")
    md_lines.append(f"")

md_lines.append(f"## 🌐 Monde ({len(world_items)} articles)")
md_lines.append(f"")
for item in world_items:
    md_lines.append(f"- [{item['title']}]({item['url']}) — *{item['source']}*, {item['date']}")
    md_lines.append(f"  {item['summary']}")
    md_lines.append(f"")

md_lines.append(f"## 📚 ArXiv (cs.AI & cs.LG) — {DATE_DISPLAY}")
md_lines.append(f"")
for item in arxiv_items:
    md_lines.append(f"- [{item['title']}]({item['url']}) — *{item['source']}*, {item['date']}")
    md_lines.append(f"  {item['summary']}")
    md_lines.append(f"")

md_lines.append(f"---")
md_lines.append(f"*Généré le {DATE_DISPLAY} par Hermes Agent*")
md_content = "\n".join(md_lines)

# HTML
cards = [
    make_card("🇫🇷 France", france_items),
    make_card("🌍 Europe hors France", europe_items),
    make_card("🌐 Monde", world_items),
]
arxiv_card = make_card("📚 ArXiv", arxiv_items)

html_parts = [
    f"""<!doctype html><html lang="fr"><head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Veille IA quotidienne — {DATE}</title>
  <style>
    :root {{
      --bg:#f8fafc; --panel:#ffffff; --ink:#1f2937; --muted:#6b7280;
      --accent:#0ea5e9; --accent-2:#6366f1; --success:#10b981; --warn:#f59e0b; --danger:#ef4444;
      --border:#e5e7eb; --shadow:0 10px 30px rgba(15,23,42,.08);
      --radius:18px;
    }}
    .dark {{
      --bg:#0b1220; --panel:#0f172a; --ink:#f3f4f6; --muted:#d1d5db;
      --border:#1f2937; --shadow:0 10px 30px rgba(0,0,0,.45);
    }}
    *{{box-sizing:border-box}}
    html,body{{margin:0;padding:0}}
    body{{
      font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Inter,"Helvetica Neue",Arial,sans-serif;
      background:
        radial-gradient(900px 600px at 110% -10%,#a78bfa29,transparent),
        radial-gradient(900px 600px at -10% 10%,#22d3ee29,transparent),
        var(--bg);
      color:var(--ink); line-height:1.65;
    }}
    .wrap{{max-width:1100px;margin:0 auto;padding:28px 20px 80px}}
    header{{
      display:grid; grid-template-columns: 1fr auto; align-items:center; gap:14px;
      padding:22px 22px 20px; border:1px solid var(--border);
      background:linear-gradient(180deg,#0b1220,#0f172a);
      border-radius: var(--radius); color:#fff;
      box-shadow: var(--shadow);
    }}
    header h1{{font-size:1.6rem;margin:0;letter-spacing:-.2px}}
    header p{{margin:0;opacity:.85;font-size:.95rem}}
    header time{{font-variant-numeric: tabular-nums}}
    .kpis{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}}
    .kpi{{
      border:1px solid var(--border); background:linear-gradient(180deg,#ffffff,#f6f8fb);
      border-radius:14px; padding:14px 16px;
    }}
    .dark .kpi{{background:linear-gradient(180deg,#0f172a,#0b1220)}}
    .kpi .label{{font-size:.78rem;color:var(--muted);letter-spacing:.08em;text-transform:uppercase}}
    .kpi .value{{font-size:1.15rem;margin-top:6px;font-weight:700}}
    .badges{{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}}
    .pill{{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;font-size:.75rem;font-weight:600;border:1px solid var(--border);background:var(--panel);color:var(--ink)}}
    .pill.blue{{background:#0ea5e9;color:#fff;border-color:#0ea5e9}}
    .pill.green{{background:#10b981;color:#fff;border-color:#10b981}}
    .pill.yellow{{background:#f59e0b;color:#fff;border-color:#f59e0b}}
    .grid{{display:grid;grid-template-columns:1fr;gap:16px}}
    .card{{border:1px solid var(--border);background:linear-gradient(180deg,#ffffff,#f6f8fb);border-radius:18px;box-shadow:var(--shadow)}}
    .dark .card{{background:linear-gradient(180deg,#0f172a,#0b1220)}}
    .card-head{{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 18px 0}}
    .card-title{{font-size:1.05rem;font-weight:700}}
    .card-body{{padding:12px 18px 18px}}
    .item{{border-top:1px solid var(--border);padding:14px 0}}
    .item:first-child{{border-top:0;padding-top:0}}
    .item h3{{margin:0 0 6px;font-size:.98rem;line-height:1.4}}
    .item h3 a{{color:var(--accent-2);text-decoration:none}}
    .item h3 a:hover{{text-decoration:underline}}
    .meta{{color:var(--muted);font-size:.82rem;margin-bottom:6px}}
    .item p{{margin:0;font-size:.92rem;color:var(--ink)}}
    .dark .item p{{color:#e5e7eb}}
    .arxiv-section{{margin-top:22px}}
    .arxiv-section h2{{font-size:1.1rem;margin:0 0 10px}}
    footer{{padding:18px 2px 0;color:var(--muted);font-size:.85rem}}
    footer p{{margin:4px 0}}
    @media (min-width: 860px){{
      .grid{{grid-template-columns:1fr 1fr}}
    }}
    @media (min-width: 1080px){{
      .grid{{grid-template-columns:1fr 1fr 1fr}}
    }}
  </style>
</head><body>
<div class="wrap">
  <header>
    <div>
      <h1>🤖 Veille IA quotidienne</h1>
      <p>Sources FR/EU + Monde — généré automatiquement par Hermes</p>
    </div>
    <time datetime="{DATE}">{DATE_DISPLAY}</time>
  </header>
  <div class="kpis">
    <div class="kpi"><div class="label">🇫🇷 France</div><div class="value">5</div></div>
    <div class="kpi"><div class="label">🌍 Europe hors France</div><div class="value">5</div></div>
    <div class="kpi"><div class="label">🌐 Monde</div><div class="value">6</div></div>
  </div>
  <div class="badges">
    <span class="pill blue">📰 16 articles</span>
    <span class="pill green">📅 {DATE_DISPLAY}</span>
    <span class="pill yellow">🔬 ArXiv 5 articles</span>
  </div>
  <div class="grid">
""",
    "\n".join(cards),
    """  </div>
  <div class="arxiv-section">
    <h2>📚 ArXiv (cs.AI &amp; cs.LG) — """ + DATE_DISPLAY + """</h2>
    <p>Soumissions du 1er septembre 2026. Filtrage sur date de publication respecté.</p>
    <div class="grid">
""",
    arxiv_card,
    """    </div>
  </div>
  <footer>
    <p>Généré le """ + DATE_DISPLAY + """ par Hermes Agent</p>
    <p>Sources : ZDNet FR, Le Monde, 01net, Numerama, Silicon.fr, Tech.eu, The Next Web, EURACTIV, VentureBeat, TechCrunch, arXiv</p>
    <p>template-inlined</p>
  </footer>
</div>
</body></html>"""
]

html_content = "".join(html_parts)

# Write files
md_path = os.path.join(ARCHIVE_DIR, f"veille-IA-{DATE}.md")
html_path = os.path.join(ARCHIVE_DIR, f"veille-IA-{DATE}.html")

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Update files.json
files_json_path = os.path.join(ARCHIVE_DIR, "files.json")
if os.path.exists(files_json_path):
    with open(files_json_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception:
            data = {"files": []}
else:
    data = {"files": []}

data["files"] = [entry for entry in data.get("files", []) if entry.get("name") != f"veille-IA-{DATE}"]
data.setdefault("files", []).append({
    "name": f"veille-IA-{DATE}",
    "path": f"veille-IA-{DATE}.html",
    "generated_at": datetime.now().isoformat(),
    "query": "veille IA quotidienne"
})

with open(files_json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Wrote:", md_path)
print("Wrote:", html_path)
print("Updated:", files_json_path)
print("MD size:", os.path.getsize(md_path))
print("HTML size:", os.path.getsize(html_path))
print("HTML items:", html_content.count('class="item"'))
