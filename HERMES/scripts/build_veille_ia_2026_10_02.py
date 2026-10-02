#!/usr/bin/env python3
"""Construit veille-IA-2026-10-02.html à partir du .md (template moderne identique au 30/09)."""
import re, html, json, datetime

BASE = '/Users/manud/dev/ParkStras/HERMES/archives'
MD = f'{BASE}/veille-IA-2026-10-02.md'
OUT = f'{BASE}/veille-IA-2026-10-02.html'
DATE_ISO = '2026-10-02'
DATE_FR = '2 octobre 2026'

md = open(MD).read()

sections = {}
cur = None
items = []
for line in md.splitlines():
    m = re.match(r'^## (.+)$', line)
    if m:
        if cur:
            sections[cur] = items
        cur = (m.group(1)
               .replace('🇫🇷 ', '').replace('🌍 ', '')
               .replace('🌐 ', '').replace('📚 ', '').strip())
        cur = re.sub(r'\s*\(\d+\)\s*$', '', cur)  # retire le compte "(5)" du titre
        items = []
        continue
    if cur and line.startswith('- **['):
        tm = re.match(r'^- \*\*\[(.+?)\]\((https?://.+?)\)\*\* — (.+?) • (.+?)\s*$', line)
        if tm:
            items.append({'title': tm.group(1), 'url': tm.group(2),
                          'src': tm.group(3), 'date': tm.group(4), 'desc': ''})
        continue
    if cur and items and line.strip() and not line.startswith(('_', '#', '-', '---')):
        items[-1]['desc'] = (items[-1]['desc'] + ' ' + line.strip()).strip()
if cur:
    sections[cur] = items

fr = sections.get('France', [])
eu = sections.get('Europe hors France', [])
mo = sections.get('Monde', [])
ax = [s for s, v in sections.items() if s.startswith('ArXiv')]
ax = sections.get(ax[0], []) if ax else []

def esc(s):
    return html.escape(s, quote=False)

def render_items(items):
    out = []
    for it in items:
        out.append(
            '<div class="item">\n'
            f'<h3><a href="{it["url"]}" target="_blank">{esc(it["title"])}</a></h3>\n'
            f'<div class="meta">{esc(it["src"])} • {esc(it["date"])}</div>\n'
            f'<p>{esc(it["desc"])}</p>\n'
            '</div>'
        )
    return '\n'.join(out)

def card(title, items):
    return ('<div class="card">\n'
            f'<div class="card-head"><div class="card-title">{title}</div></div>\n'
            '<div class="card-body">\n' + render_items(items) + '\n</div>\n</div>')

def card_empty(title, msg):
    return ('<div class="card">\n'
            f'<div class="card-head"><div class="card-title">{title}</div></div>\n'
            '<div class="card-body">\n'
            f'<div class="arxiv-empty">{esc(msg)}</div>\n'
            '</div>\n</div>')

cards = [
    card('🇫🇷 France', fr) if fr else card_empty('🇫🇷 France', 'Aucune actualité France identifiée dans la fenêtre 1–2 octobre 2026.'),
    card('🌍 Europe hors France', eu) if eu else card_empty('🌍 Europe hors France', 'Aucune actualité Europe hors France identifiée dans la fenêtre.'),
    card('🌐 Monde', mo) if mo else card_empty('🌐 Monde', 'Aucune actualité Monde identifiée dans la fenêtre.'),
]

arxiv_block = (
    '  <div class="arxiv-section">\n'
    '    <h2>📚 ArXiv (cs.AI &amp; cs.LG)</h2>\n'
    + ('    <div class="card"><div class="card-body">\n' + render_items(ax) + '\n</div></div>\n' if ax
       else '    <div class="arxiv-empty">Aucun papier ArXiv cs.AI/cs.LG retenu pour la fenêtre.</div>\n')
    + '  </div>'
)

total = len(fr) + len(eu) + len(mo)
prev = open(f'{BASE}/veille-IA-2026-09-30.html').read()
css = prev[prev.index('  <style>'):prev.index('</head>')]  # réutilise exactement le CSS du dernier rapport validé

body = f'''<!doctype html><html lang="fr"><head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Veille IA quotidienne — {DATE_ISO}</title>
{css}</head><body>
<div class="wrap">
  <header>
    <div>
      <h1>🤖 Veille IA quotidienne</h1>
      <p>Sources FR/EU + Monde — généré automatiquement par Hermes</p>
    </div>
    <time datetime="{DATE_ISO}">{DATE_FR}</time>
  </header>
  <div class="kpis">
<div class="kpi"><div class="label">🇫🇷 France</div><div class="value">{len(fr)}</div></div>
<div class="kpi"><div class="label">🌍 Europe hors France</div><div class="value">{len(eu)}</div></div>
<div class="kpi"><div class="label">🌐 Monde</div><div class="value">{len(mo)}</div></div>
  </div>
  <div class="badges">
    <span class="pill blue">📰 {total} articles</span>
    <span class="pill green">📅 {DATE_FR}</span>
    <span class="pill yellow">🔬 ArXiv : {len(ax)}</span>
  </div>
  <div class="grid">
''' + '\n'.join(cards) + '''
  </div>
''' + arxiv_block + '''
  <footer>
    <p>Généré le {DATE_ISO} par Hermes (procédure veille-ia-quotidienne renforcée cron). Template moderne inline (dark theme, KPIs, cartes responsive). Fichiers : veille-IA-{DATE_ISO}.md + .html</p>
    <p>Dernière modification : <span id="lastmod"></span></p>
    <script>document.getElementById("lastmod").innerText = new Date(document.lastModified).toLocaleString("fr-FR");</script>
  </footer>
</div>
</body></html>
'''

open(OUT, 'w').write(body)

# --- mise à jour files.json : supprimer entrée du jour + ajouter la nouvelle ---
FJ = f'{BASE}/files.json'
data = json.load(open(FJ))
today = 'veille-IA-' + DATE_ISO
files = data.get('files', [])
files = [f for f in files if not (f.get('name', '').startswith(today) or f.get('path', '').startswith(today))]
files.append({
    'name': today,
    'path': today + '.html',
    'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'query': 'veille IA quotidienne',
})
data['files'] = files
json.dump(data, open(FJ, 'w'), ensure_ascii=False, indent=2)

print('HTML écrit, items:', total, 'arxiv:', len(ax), '| files.json entries:', len(files))
