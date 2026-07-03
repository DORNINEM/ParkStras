from pathlib import Path

base = Path('/Users/manud/dev/ParkStras/HERMES/archives')
today = '2026-07-03'

france_items = [
    ('Google suspend les résumés IA Overviews aux US après des intoxications', 'ZDNet FR · 03/07/2026', 'À la suite d\'intoxications produites par AI Overviews, Google suspend temporairement cette fonctionnalité aux États-Unis et annonce des gardes renforcées.', 'https://www.zdnet.fr/actualites/google-suspend-ses-resumes-ia-overview-aux-us-apres-des-intoxications-498288.htm'),
    ('BlaBlaCar passe à 41 pays grâce à l\'IA', 'ZDNet FR · 03/07/2026', 'BlaBlaCar étend sa couverture mondiale avec 20 nouveaux marchés atteints par IA de prédiction, traduction automatisée et ciblage marketing, sans équipes locales dédiées.', 'https://www.zdnet.fr/actualites/comment-blablacar-se-deploie-dans-20-nouveaux-pays-grace-a-lia-498284.htm'),
    ('OpenAI envisagerait de céder jusqu\'à 5 % de son capital à l\'État américain', 'ZDNet FR · 03/07/2026', 'OpenAI étudie une offre de participation publique aux États-Unis pour réduire les pressions réglementaires. L\'équivalent pourrait atteindre plusieurs dizaines de milliards de dollars.', 'https://www.zdnet.fr/actualites/openai-envisagerait-de-ceder-jusqua-5-de-son-capital-a-letat-americain-498242.htm'),
    ('Google annonce l\'ère de l\'IA agentique avec Gemini', '01net · 03/07/2026', 'Google structure sa feuille de route autour d\'agents IA autonomes capables d\'anticiper les besoins utilisateurs et d\'exécuter des séquences complexes sans sollicitation explicite.', 'https://www.01net.com/actualites/google-annonce-lere-de-lia-agentique-quest-ce-que-ca-va-changer.html'),
    ('Les émissions de CO₂ de Google et d\'Amazon bondissent sous l\'effet de l\'IA', 'Le Monde · 03/07/2026', 'Les deux géants voient leur empreinte carbone augmenter fortement à cause de l\'infrastructure IA, compromettant leurs engagements neutralité à court terme.', 'https://www.lemonde.fr/pixels/article/2026/07/03/les-emissions-de-co-de-google-et-amazon-bondissent-propulsees-par-l-essor-de-l-ia_6718303_4408996.html')
]

europe_items = [
    ('Les conseillers IA de l’UE craignent que l’Europe ne soit « cuite » sans action drastique', 'EURACTIV · 03/07/2026', 'Des notes internes peignent un tableau sombre du retard européen en IA et appellent à une accélération budgétaire et réglementaire urgente.', 'https://www.euractiv.com/news/eu-ai-advisers-fear-europe-could-be-cooked-without-drastic-action/'),
    ('Coulisses du plan européen de gigafactories d’IA', 'EURACTIV · 03/07/2026', 'L\'EuroHPC prépare sept hubs d\'IA avec des subventions paneuropéennes ; les appels d\'offres doivent être lancés dès juillet 2026.', 'https://www.euractiv.com/news/an-inside-look-at-the-eus-push-to-build-ai-gigafactories/'),
    ('L’UE détaille un code de transparence pour les contenus générés par IA', 'EURACTIV · 03/07/2026', 'Les règles finales européennes précisent comment marquer et détecter les contenus synthétiques textes, images et vidéos, pour une meilleure traçabilité.', 'https://www.euractiv.com/news/eu-tells-ai-companies-how-they-can-make-their-content-detectable/'),
    ('Brussels claps back at Trump’s tech threats', 'Politico EU · 03/07/2026', 'L\'UE répond aux menaces tarifaires américaines sur le numérique par un dialogue stratégique couvrant IA, cybersécurité, puces et souveraineté technologique.', 'https://www.politico.eu/article/brussels-claps-back-trumps-tech-threats/'),
    ('Microsoft lance Frontier Company : 2,5 Md$ et 6 000 ingénieurs pour l’IA entreprise', 'The Next Web · 03/07/2026', 'Microsoft renforce son offensive entreprises avec une unité dédiée et des ingénieurs déployés chez le client, sur le modèle de Palantir.', 'https://thenextweb.com/news/microsoft-frontier-company-2-5-billion-ai-deployment')
]

world_items = [
    ('Zuckerberg avoue que les agents IA n’avancent pas aussi vite qu’espéré', 'TechCrunch · 03/07/2026', 'Meta admet un décalage sur ses ambitions agents ; les retours tangibles sont attendus dans les 3 à 6 mois.', 'https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/'),
    ('Anthropic discute avec Samsung d’une puce IA dédiée', 'TechCrunch · 03/07/2026', 'Anthropic négocie avec Samsung un accélérateur mémoire personnalisé pour réduire sa dépendance historique.', 'https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/'),
    ('Z.ai : GLM-5.2, un modèle chinois low-cost qui talonne les leaders', 'The Next Web · 03/07/2026', 'Le modèle chinois atteint la 4e place mondiale sur un benchmark majeur tout en s\'exécutant sur puces domestiques à faible coût.', 'https://thenextweb.com/news/a-cheap-chinese-ai-model-is-closing-in-on-anthropic-and-openai'),
    ('Together AI lève 800 M$ en Series C, dépassant les 8 Md$', 'The Next Web · 03/07/2026', 'La plateforme cloud open-source profite de l\'explosion des usages en entreprise, soutenue par Aramco Ventures.', 'https://thenextweb.com/news/together-ai-800m-series-c-aramco-ventures'),
    ('Mirage de l’automatisation : Ford réembauche ses seniors pour sauver son IA', 'ZDNet FR · 03/07/2026', 'Ford rappelle 350 ingénieurs seniors après avoir constaté que l\'IA ne résolvait pas ses problèmes de qualité.', 'https://www.zdnet.fr/actualites/mirage-de-lautomatisation-quand-ford-reembauche-ses-seniors-pour-sauver-son-ia-498290.htm'),
    ('Surveillance en ligne pour LLMs : un moniteur temps réel simple mais efficace', 'arXiv cs.AI · 03/07/2026', 'Des chercheurs proposent un moniteur calibré par contrôle de risque pour détecter des sorties dangereuses.', 'http://arxiv.org/abs/2607.02510v1')
]

def item_html(item):
    title, source, summary, url = item
    return '''          <div class="item">
            <h3>''' + title + '''</h3>
            <div class="meta">''' + source + '''</div>
            <p>''' + summary + '''</p>
            <a href="''' + url + '''" target="_blank" rel="noopener">Lire l'article →</a>
          </div>'''

def card(title, icon_path, items, section_id, fullwidth=False):
    items_html = ''.join(item_html(i) for i in items)
    width_attr = ' style="grid-column: 1 / -1"' if fullwidth else ''
    return '''
      <article class="card" aria-labelledby="''' + section_id + '''"''' + width_attr + '''>
        <div class="card-head">
          <h2 class="card-title" id="''' + section_id + '''">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">''' + icon_path + '''</svg>
            ''' + title + '''
          </h2>
          <span class="pill ''' + ('blue' if title == 'France' else 'green') + '''">''' + str(len(items)) + ''' items</span>
        </div>
        <div class="card-body">
''' + items_html + '''
        </div>
      </article>'''

europe_icon = '<path d="M3 3h18v18H3z"/><path d="M8 7h8M9 12h6M10 17h4"/>'
france_icon = '<path d="M3 3h18v18H3z"/><path d="M7 7h10v10H7z"/>'
monde_icon = '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>'

body = '''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Veille IA quotidienne — ''' + today + '''</title>
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
        <h1>🤖 Veille IA quotidienne</h1>
        <p>Vendredi 3 juillet 2026 · Hermes Agent</p>
      </div>
      <div style="text-align:right">
        <time datetime="2026-07-03T07:00:00.000000+00:00">Vendredi 3 juillet 2026</time>
        <div style="font-size:.8rem;opacity:.8;margin-top:6px">Format : HTML moderne</div>
      </div>
    </header>

    <div class="controls">
      <button class="theme-toggle" onclick="document.body.classList.toggle('dark')" title="Basculer thème sombre / clair">🌗</button>
    </div>

    <section class="kpis" aria-label="Résumé">
      <div class="kpi">
        <div class="label">🇫🇷 France</div>
        <div class="value">''' + str(len(france_items)) + ''' actualités</div>
      </div>
      <div class="kpi">
        <div class="label">🌍 Europe hors France</div>
        <div class="value" style="color:var(--success)">''' + str(len(europe_items)) + ''' actualités</div>
      </div>
      <div class="kpi">
        <div class="label">🌐 Monde</div>
        <div class="value">''' + str(len(world_items)) + ''' actualités</div>
      </div>
    </section>

    <div class="badges" aria-label="Tags">
      <span class="badge"><span class="dot" style="color:#1d4ed8"></span>Agents & automation</span>
      <span class="badge"><span class="dot" style="color:#dc2626"></span>Géopolitique & régulation</span>
      <span class="badge"><span class="dot" style="color:#16a34a"></span>Infrastructure & hardware</span>
      <span class="badge"><span class="dot" style="color:#9333ea"></span>Recherche</span>
      <span class="badge"><span class="dot" style="color:#ea580c"></span>Emploi & transition</span>
      <span class="badge"><span class="dot" style="color:#059669"></span>Énergie & climat</span>
    </div>

    <div class="grid">
      ''' + card('France', france_icon, france_items, 'france') + '''
      ''' + card('Monde', monde_icon, world_items, 'monde') + '''
      ''' + card('Europe hors France', europe_icon, europe_items, 'europe', fullwidth=True) + '''
    </div>

    <footer>
      Rapport généré par Hermes Agent · veille IA quotidienne · ''' + today + '''
    </footer>
  </div>
</body>
</html>'''

out = base / ('veille-IA-' + today + '.html')
out.write_text(body, encoding='utf-8')
print('wrote', out, 'size', out.stat().st_size)
