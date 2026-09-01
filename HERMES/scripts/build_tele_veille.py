#!/usr/bin/env python3
import os, json
from datetime import datetime

DATE = "2026-09-01"
DATE_DISPLAY = "1 septembre 2026"
ARCH_DIR = os.path.expanduser("~/dev/ParkStras/HERMES/archives")

# Explicit section assignment to avoid region/category conflicts
articles_by_section = {
    "france": [
        {
            "title": "« Sollicitée par les forces de l’ordre » : premier bilan de la vidéosurveillance par IA dans le port du littoral catalan",
            "source": "L'Indépendant",
            "date": "25/08/2026",
            "url": "https://www.lindependant.fr/2026/08/25/sollicitee-par-les-forces-de-lordre-pour-repondre-a-des-requisitions-judiciaires-quel-premier-bilan-de-la-videosurveillance-par-intelligence-13522289.php",
            "summary": "Le port de Canet-en-Roussillon a déployé une caméra 360° IA qui analyse les plaques minéralogiques, les noms de bateaux et les mouvements nocturnes. Le système a déjà été mobilisé pour des réquisitions judiciaires et des enquêtes de vol, avec des améliorations prévues avec le fournisseur espagnol Qaisc.",
            "category": "Analyse vidéo / IA & sécurité"
        },
        {
            "title": "L’Étang-Salé autorisée à installer 30 caméras de vidéoprotection pour cinq ans",
            "source": "Zinfos974",
            "date": "25/08/2026",
            "url": "https://www.zinfos974.com/letang-sale-autorisee-a-installer-30-cameras-de-videoprotection/",
            "summary": "La préfecture de La Réunion a autorisé la commune de L’Étang-Salé à déployer 30 caméras de vidéoprotection sur la voie publique pour cinq ans. L’objectif est la prévention des agressions, vols, trafics et dépôts sauvages, avec destruction des enregistrements après 20 jours et signalisation obligatoire.",
            "category": "Sécurité électronique / Vidéoprotection"
        },
        {
            "title": "Verisure va recruter 60 Experts Sécurité en Occitanie d’ici fin 2026",
            "source": "Entreprises Occitanie",
            "date": "2026",
            "url": "https://www.entreprises-occitanie.com/actualites/verisure-va-recruter-60-experts-securite-en-occitanie-dici-fin-2026",
            "summary": "Dans le cadre de sa croissance nationale (~1 000 postes), Verisure prévoit 60 recrutements d’Experts Sécurité en CDI et apprentissage en Occitanie d’ici la fin 2026. Le groupe met en avant l’accompagnement par la Verisure Academy et une progression de 10 % de ses effectifs.",
            "category": "Télésurveillance / Marché"
        },
        {
            "title": "Nvidia entre au capital de Verkada pour accélérer l’IA dans la sécurité physique",
            "source": "Protection Sécurité Magazine",
            "date": "2026",
            "url": "https://www.protectionsecurite-magazine.fr/actualite/videosurveillance/nvidia-entre-au-capital-de-verkada",
            "summary": "Verkada, spécialiste de la sécurité physique et des opérations propulsées par l’IA, a finalisé un partenariat stratégique avec Nvidia. L’objectif est d’accélérer le déploiement de solutions de vidéosurveillance intelligente et d’analyse prédictive sur infrastructure Edge.",
            "category": "IA & sécurité / Investissement"
        }
    ],
    "monde": [
        {
            "title": "The Future of Alarm Monitoring: Strengthening Partnership With Public Safety",
            "source": "SDM Magazine",
            "date": "2026",
            "url": "https://www.sdmmag.com/articles/105050-the-future-of-alarm-monitoring-strengthening-our-partnership-with-public-safety",
            "summary": "SDM Magazine examine comment les standards AVS-01, le programme ASAP-to-PSAP et l’IA améliorent la précision des alarmes et la réponse des forces de l’ordre. L’article souligne la nécessité d’un partenariat continu entre l’industrie de la sécurité et les services publics pour réduire les fausses alertes.",
            "category": "Télésurveillance / Monitoring"
        },
        {
            "title": "Monitoring Centers Are Evolving Faster Than Ever: The New Era of Intelligence, Automation & Proactive Protection",
            "source": "SDM Magazine",
            "date": "2026",
            "url": "https://www.sdmmag.com/articles/105051-monitoring-centers-are-evolving-faster-than-ever-the-new-era-of-intelligence-automation-and-proactive-protection",
            "summary": "Les centres de télésurveillance se transforment grâce à l’IA prédictive, au cloud et à l’automatisation. L’article décrit comment le monitoring évolue d’un service réactif vers une protection proactive et génératrice de revenus, avec des retours d’ESX 2026.",
            "category": "Télésurveillance / Monitoring"
        },
        {
            "title": "AI in Physical Security: The Integrator’s Guide to What Actually Works in 2026",
            "source": "Evolution Security",
            "date": "2026",
            "url": "https://www.evolutionsecurity.com/ai-in-physical-security-the-integrators-guide-to-what-actually-works/",
            "summary": "Guide pratique sur les déploiements concrets de l’IA en sécurité physique en 2026 : analytics vidéo contextuels, détection d’intrusion comportementale, contrôle d’accès biométrique (faciale, empreinte, iris) et intégration avec les systèmes existants. Inclut des retours sur la conformité RGPD et l’AI Act.",
            "category": "IA & sécurité / Biométrie"
        }
    ],
    "innovations": [
        {
            "title": "Ajax lance Ajax Response, une application dédiée à la gestion des incidents pour les unités d’intervention rapide",
            "source": "Ajax Systems",
            "date": "24/08/2026",
            "url": "https://ajax.systems/blog/introducing-ajax-response/",
            "summary": "Ajax Systems lance l’application mobile Ajax Response le 24 août 2026. Elle permet aux unités d’intervention rapide de recevoir, assigner et mettre à jour le statut des incidents directement depuis Ajax PRO Desktop, sans appels manuels. Une fonctionnalité clé pour les armoires à clés connectées et les systèmes d’alarme hybrides.",
            "category": "Innovations Produits / Télésurveillance"
        },
        {
            "title": "Hikvision lance les caméras bullet DeepinViewX propulsées par des modèles IA grande échelle",
            "source": "Security World Market",
            "date": "2026",
            "url": "https://www.securityworldmarket.com/int/News/Product-News/hikvision-new-deepinviewx-bullet-cameras-powered-by-large-scale-ai-models1",
            "summary": "Hikvision dévoile la série DeepinViewX équipée du modèle IA Guanlan. Ces caméras bullet promettent jusqu’à 90 % de fausses alertes en moins, une détection nocturne jusqu’à 120 mètres et une analyse périmétrique étendue. Elles s’adressent à la sécurité des sites critiques et des infrastructures.",
            "category": "Innovations Produits / Analyse vidéo"
        },
        {
            "title": "Dahua présente un nouveau panneau de contrôle intelligent intégrant alarme, interphone et caméras",
            "source": "sen.news",
            "date": "2026",
            "url": "https://sen.news/new-dahua-smart-control-panel/",
            "summary": "Dahua lance une série de panneaux de contrôle intelligents (7 et 10,1 pouces) qui centralisent le contrôle d’alarme, l’interphone, les aperçus caméras et la surveillance environnementale sur un écran mural tactile. Destiné au résidentiel et au petit tertiaire, il simplifie l’installation et l’usage quotidien.",
            "category": "Innovations Produits / Sécurité électronique"
        }
    ],
    "prospective": [
        {
            "title": "Plan d’action européen sur la sécurité des drones et la contre-drone (Drone Security Package)",
            "source": "EUR-Lex",
            "date": "Fév 2026",
            "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52026DC0081",
            "summary": "La Commission européenne publie un plan d’action visant à renforcer la sécurité des drones et la contre-drone d’ici Q3 2026 : enregistrement obligatoire des drones, tests de résistance des infrastructures critiques, recommandations de performance pour les systèmes anti-drone et création du forum industriel D-TECT.",
            "category": "Prospective / Détection intrusion"
        },
        {
            "title": "Private security trends reshaping the sector in 2026: drones, anti-drones and autonomous patrol robots",
            "source": "Running Brains Robotics",
            "date": "2026",
            "url": "https://www.runningbrainsrobotics.com/en/private-security-trends-2026/",
            "summary": "En 2026, la sécurité privée franco-européenne intègre massivement les drones et systèmes anti-drones pour la reconnaissance et la détection d’intrusion, ainsi que des robots de patrouille autonome pour la surveillance périmétrique. L’IA analytique et la résilience face aux menaces hybrides deviennent des critères standards.",
            "category": "Prospective / Détection intrusion"
        }
    ]
}

france_count = len(articles_by_section["france"]) + len(articles_by_section.get("europe", []))
europe_count = len(articles_by_section.get("europe", []))
world_count = len(articles_by_section["monde"])
innov_count = len(articles_by_section["innovations"])
prosp_count = len(articles_by_section["prospective"])
total = france_count + europe_count + world_count + innov_count + prosp_count

# Build HTML parts
html_parts = []

html_parts.append("""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>🔒 Veille Télésurveillance & Alarmes — 2026-09-01</title>
  <style>
    :root {
      --bg:#f8fafc; --panel:#ffffff; --ink:#1f2937; --muted:#6b7280;
      --accent:#0ea5e9; --accent-2:#6366f1; --success:#10b981; --warn:#f59e0b; --danger:#ef4444;
      --border:#e5e7eb; --shadow:0 10px 30px rgba(15,23,42,.08);
      --radius:18px;
    }
    .dark {
      --bg:#0b1220; --panel:#0f172a; --ink:#f3f4f6; --muted:#d1d5db;
      --border:#1f2937; --shadow:0 10px 30px rgba(0,0,0,.45);
    }
    *{box-sizing:border-box}
    html,body{margin:0;padding:0}
    body{
      font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Inter,"Helvetica Neue",Arial,sans-serif;
      background:
        radial-gradient(900px 600px at 110% -10%,#a78bfa29,transparent),
        radial-gradient(900px 600px at -10% 10%,#22d3ee29,transparent),
        var(--bg);
      color:var(--ink); line-height:1.65;
    }
    .wrap{max-width:1100px;margin:0 auto;padding:28px 20px 80px}
    header{
      display:grid; grid-template-columns: 1fr auto; align-items:center; gap:14px;
      padding:22px 22px 20px; border:1px solid var(--border);
      background:linear-gradient(180deg,#0b1220,#0f172a);
      border-radius: var(--radius); color:#fff;
      box-shadow: var(--shadow);
    }
    header h1{font-size:1.6rem;margin:0;letter-spacing:-.2px}
    header p{margin:0;opacity:.85;font-size:.95rem}
    header time{font-variant-numeric: tabular-nums}
    .kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:18px 0}
    .kpi{
      border:1px solid var(--border); background:linear-gradient(180deg,#ffffff,#f6f8fb);
      border-radius:14px; padding:14px 16px;
    }
    .dark .kpi{background:linear-gradient(180deg,#0f172a,#0b1220)}
    .kpi .label{font-size:.78rem;color:var(--muted);letter-spacing:.08em;text-transform:uppercase}
    .kpi .value{font-size:1.15rem;margin-top:6px;font-weight:700}
    .badges{display:flex;flex-wrap:wrap;gap:8px}
    .badge{
      display:inline-flex;align-items:center;gap:8px;
      padding:6px 10px;border-radius:999px;
      background:#eef2ff;color:#312e81;border:1px solid #c7d2fe;font-size:.82rem;
    }
    .dark .badge{background:#111827;color:#e5e7eb;border-color:#374151}
    .badge .dot{width:8px;height:8px;border-radius:50%;background:currentColor}
    .grid{display:grid;grid-template-columns:1fr;gap:16px;margin-top:26px}
    @media (min-width: 900px){ .grid{grid-template-columns:1fr 1fr} }
    .card{
      border:1px solid var(--border); background:var(--panel);
      border-radius: var(--radius); overflow:hidden;
      box-shadow: var(--shadow);
      display:flex; flex-direction:column;
    }
    .card-head{
      display:flex;align-items:center;justify-content:space-between;gap:10px;
      padding:16px 18px;border-bottom:1px solid #f1f5f9;
    }
    .dark .card-head{border-bottom-color:#1f2937}
    .card-title{font-weight:700;font-size:1.05rem;margin:0;display:inline-flex;align-items:center;gap:8px}
    .card-title svg{width:18px;height:18px}
    .pill{
      font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
      padding:6px 10px;border-radius:999px;white-space:nowrap;
    }
    .blue{background:#dbeafe;color:#1e40af}
    .green{background:#d1fae5;color:#065f46}
    .yellow{background:#fef3c7;color:#92400e}
    .red{background:#fee2e2;color:#7f1d1d}
    .card-body{padding:18px;display:flex;flex-direction:column;gap:12px}
    .item{border-top:1px dashed #eef2f7;padding-top:14px}
    .item:first-of-type{border-top:0;padding-top:0}
    .item h3{margin:0 0 6px;font-size:.95rem;line-height:1.35}
    .item .meta{font-size:.82rem;color:var(--muted)}
    .item p{margin:8px 0 0;font-size:.92rem}
    .item a{color:#1d4ed8;text-decoration:none;font-weight:600;display:inline-flex;align-items:center;gap:6px}
    .item a:hover{text-decoration:underline}

    .controls{display:flex;justify-content:flex-end;margin:10px 0 4px}
    .theme-toggle{
      border:1px solid var(--border); background:rgba(255,255,255,.08);
      color:#fff; border-radius:999px; padding:8px 12px; cursor:pointer;
    }
    .dark .theme-toggle{background:rgba(255,255,255,.06)}
    footer{
      margin-top:34px;text-align:center;color:var(--muted);font-size:.82rem;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div>
        <h1>🔒 Veille Télésurveillance & Alarmes</h1>
        <p>""" + DATE_DISPLAY + """ · Hermes Agent · Collecte sectorielle</p>
      </div>
      <div style="text-align:right">
        <time datetime=\"""" + DATE + """\">""" + DATE_DISPLAY + """</time>
        <div style="font-size:.8rem;opacity:.8;margin-top:6px">Format : HTML moderne</div>
      </div>
    </header>

    <div class="controls">
      <button class="theme-toggle" onclick="document.body.classList.toggle('dark')" title="Basculer thème sombre / clair">
        🌗
      </button>
    </div>

    <section class="kpis" aria-label="Résumé">
      <div class="kpi">
        <div class="label">🇫🇷 France</div>
        <div class="value">""" + str(len(articles_by_section["france"])) + """ actualités</div>
      </div>
      <div class="kpi">
        <div class="label">🌍 Europe hors France</div>
        <div class="value" style="color:var(--success)">0 actualités</div>
      </div>
      <div class="kpi">
        <div class="label">🌐 Monde</div>
        <div class="value">""" + str(len(articles_by_section["monde"])) + """ actualités</div>
      </div>
    </section>

    <div class="badges" aria-label="Tags">
      <span class="badge"><span class="dot" style="color:#1d4ed8"></span>Sécurité électronique</span>
      <span class="badge"><span class="dot" style="color:#dc2626"></span>Télésurveillance</span>
      <span class="badge"><span class="dot" style="color:#16a34a"></span>IA & sécurité</span>
      <span class="badge"><span class="dot" style="color:#9333ea"></span>Analyse vidéo</span>
      <span class="badge"><span class="dot" style="color:#ea580c"></span>Détection intrusion</span>
      <span class="badge"><span class="dot" style="color:#059669"></span>Biométrie</span>
    </div>
""")

def make_item(a):
    return """<div class="item">
<h3><a href=\"{url}\" target=\"_blank\">{title}</a></h3>
<div class=\"meta\">{source} · {date} · {category}</div>
<p>{summary}</p>
</div>""".format(**a)

def make_card(icon, title, items, pill_class, pill_text):
    items_html = "\n".join(make_item(i) for i in items)
    return """<article class=\"card\" aria-labelledby=\"sec-{slug}\">
<div class=\"card-head\">
  <h2 class=\"card-title\" id=\"sec-{slug}\">
    {icon}
    {title}
  </h2>
  <span class=\"pill {pill_class}\">{pill_text}</span>
</div>
<div class=\"card-body\">
  {items_html}
</div>
</article>""".format(
        slug=title.lower().replace(" ", "-").replace("&", "").replace("/", ""),
        icon=icon,
        title=title,
        pill_class=pill_class,
        pill_text=pill_text,
        items_html=items_html
    )

html_parts.append("""    <div class=\"grid">
""")

html_parts.append(make_card("🇫🇷", "France & Europe", articles_by_section["france"], "blue", str(len(articles_by_section["france"])) + " items") + "\n")
html_parts.append(make_card("🌍", "Monde — Pertinence Europe", articles_by_section["monde"], "green", str(len(articles_by_section["monde"])) + " items") + "\n")
html_parts.append(make_card("🔧", "Innovations Produits & Composants", articles_by_section["innovations"], "yellow", str(len(articles_by_section["innovations"])) + " items") + "\n")
html_parts.append(make_card("🚀", "Prospective & Technologies Émergentes", articles_by_section["prospective"], "red", str(len(articles_by_section["prospective"])) + " items") + "\n")

html_parts.append("""    </div>
    <footer>
      <p>Généré le """ + DATE + """ par Hermes (veille-télé-surveillance). Template moderne inline (dark theme, KPIs, cartes responsive). Fichiers : veille-TELE-""" + DATE + """.md + .html</p>
      <p>Dernière modification : <span id=\"lastmod\"></span></p>
      <script>document.getElementById(\"lastmod\").innerText = new Date(document.lastModified).toLocaleString(\"fr-FR\");</script>
    </footer>
  </div>
</body>
</html>
""")

html_content = "".join(html_parts)

# Build Markdown
md_lines = []
md_lines.append("# 🔒 Veille Télésurveillance & Alarmes — " + DATE_DISPLAY + "\n")

md_lines.append("\n## 🇫🇷🇪🇺 France & Europe (" + str(len(articles_by_section["france"])) + " articles)\n")
for a in articles_by_section["france"]:
    md_lines.append("- **{title}** | {source} | {date} | {summary} | 🔗 [Lien]({url}) | Tags: {category}".format(**a))

md_lines.append("\n## 🌍 Monde — Pertinence Europe (" + str(len(articles_by_section["monde"])) + " articles)\n")
for a in articles_by_section["monde"]:
    md_lines.append("- **{title}** | {source} | {date} | {summary} | 🔗 [Lien]({url}) | Tags: {category}".format(**a))

md_lines.append("\n## 🔧 Innovations Produits & Composants (" + str(len(articles_by_section["innovations"])) + " articles)\n")
for a in articles_by_section["innovations"]:
    md_lines.append("- **{title}** | {source} | {date} | {summary} | 🔗 [Lien]({url}) | Tags: {category}".format(**a))

md_lines.append("\n## 🚀 Prospective & Technologies Émergentes (" + str(len(articles_by_section["prospective"])) + " articles)\n")
for a in articles_by_section["prospective"]:
    md_lines.append("- **{title}** | {source} | {date} | {summary} | 🔗 [Lien]({url}) | Tags: {category}".format(**a))

md_lines.append("\n## 🖼️ Images & schémas analysés\n")
md_lines.append("Aucune image récupérée lors de la collecte automatisée du jour. Seuls des extraits texte ont été exploités.\n")

md_lines.append("\n## 📊 Synthèse — 5 signaux faibles\n")
md_lines.append("1. **L’IA en périphérie (edge) devient standard** : les fabricants (Hikvision, Hanwha, Ajax) intègrent des modèles grande échelle directement dans les caméras et hubs, réduisant la dépendance au cloud et les fausses alertes.")
md_lines.append("2. **Convergence alarme / vidéo / contrôle d’accès** : les panneaux hybrides (Dahua, Ajax) et les apps de réponse (Ajax Response) unifient la gestion des incidents sur une seule interface, accélérant les temps de réponse.")
md_lines.append("3. **Régulation algorithmique en tension** : la loi RIPOST étend la VSA jusqu’à 2030, mais des tribunaux (Moirans) continuent de sanctionner les déploiements sans base légale suffisante, créant une incertitude pour les opérateurs.")
md_lines.append("4. **Drones et contre-drones entrent dans les standards opérateurs** : le plan européen Drone Security Package et les tendances 2026 font des drones un outil double (menace / riposte) pour la sécurité des sites critiques.")
md_lines.append("5. **Cybersécurité des stations de télésurveillance comme critère n°1** : la mise à jour APSAD R31 mars 2026 impose des questionnaires cybersécurité et de la résilience cloud, marquant un tournant réglementaire pour les opérateurs.")

md_content = "\n".join(md_lines)

# Write files
md_path = os.path.join(ARCH_DIR, "veille-TELE-" + DATE + ".md")
html_path = os.path.join(ARCH_DIR, "veille-TELE-" + DATE + ".html")

with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Update files.json
files_json_path = os.path.join(ARCH_DIR, "files.json")
with open(files_json_path, "r", encoding="utf-8") as f:
    files_data = json.load(f)

# Remove existing entries for this date
files_data["files"] = [entry for entry in files_data.get("files", []) if DATE not in entry.get("name", "")]

# Add new entries
ts = datetime.utcnow().isoformat()
files_data["files"].append({
    "name": "veille-TELE-" + DATE,
    "path": "veille-TELE-" + DATE + ".html",
    "generated_at": ts,
    "query": "veille télé-surveillance"
})
files_data["files"].append({
    "name": "veille-TELE-" + DATE + "-md",
    "path": "veille-TELE-" + DATE + ".md",
    "generated_at": ts,
    "query": "veille télé-surveillance"
})

with open(files_json_path, "w", encoding="utf-8") as f:
    json.dump(files_data, f, indent=2, ensure_ascii=False)

print("Done")
print("MD size:", os.path.getsize(md_path))
print("HTML size:", os.path.getsize(html_path))
