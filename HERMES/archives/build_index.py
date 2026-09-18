import os, re

d = "/Users/manud/dev/ParkStras/HERMES/archives"
files = sorted(os.listdir(d))

groups = [
    ("mistral",   "Actualités Mistral",       re.compile(r'^MISTRAL-.*\.html$')),
    ("ia",        "Actualités IA global",     re.compile(r'^veille-IA-.*\.html$')),
    ("tele",      "Veille télésurveillance",  re.compile(r'^veille-TELE-.*\.html$')),
    ("rh",        "Veille IA RH",             re.compile(r'^veille-RH-IA-.*\.html$')),
    ("quantique", "Veille IA Q",              re.compile(r'^veille-quantique-.*\.html$')),
    ("diabete",   "Veille Diabète",           re.compile(r'^veille-diabete-.*\.html$')),
]
EXCLUDE = re.compile(r' copie\.html$')  # copies de secours, pas des publications

MONTHS = {1:"janvier",2:"février",3:"mars",4:"avril",5:"mai",6:"juin",7:"juillet",
          8:"août",9:"septembre",10:"octobre",11:"novembre",12:"décembre"}

def date_label(fname):
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', fname)
    if not m:
        return None
    y, mo, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return f"{day} {MONTHS[mo]} {y}" if mo in MONTHS else None

total = 0
built = []  # (pid, label, count, nav_html, panel_html)
for pid, label, pat in groups:
    fl = sorted([f for f in files if pat.match(f) and not EXCLUDE.search(f)], reverse=True)
    total += len(fl)
    if fl:
        items = []
        for f in fl:
            dl = date_label(f) or f
            items.append(f'<li><a href="{f}">{dl}<span class="date">{f}</span></a></li>')
        panel = (f'<section class="panel" id="panel-{pid}">'
                 f'<ul class="list">{"".join(items)}</ul></section>')
        nav = f'<button data-panel="{pid}">{label} ({len(fl)})</button>'
    else:
        panel = (f'<section class="panel" id="panel-{pid}">'
                 f'<div class="empty">Aucune publication disponible.</div></section>')
        nav = f'<button data-panel="{pid}" disabled>{label}</button>'
    built.append((pid, nav, panel, bool(fl)))

# First non-empty group is active by default
first_set = False
nav_btns = []
panels_html = []
for pid, nav, panel, has in built:
    if has and not first_set:
        nav = nav.replace('>', ' class="active">', 1) if 'class=' not in nav.split('>')[0] else nav.replace(' data-panel', ' class="active" data-panel', 1)
        panel = panel.replace('class="panel"', 'class="panel active"', 1)
        first_set = True
    nav_btns.append(nav)
    panels_html.append(panel)

html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>HERMES Archives</title>
<style>
:root{{--bg:#0f1420;--panel:#171e2e;--card:#1e2740;--txt:#e7ecf5;--muted:#8b98b3;--accent:#5b8def;--border:#28324d}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--txt);min-height:100vh}}
header{{padding:2.2rem 1.2rem 1.4rem;text-align:center;background:linear-gradient(180deg,#141b2b 0%,var(--bg) 100%)}}
header img{{max-width:340px;width:70%;height:auto;border-radius:14px;display:block;margin:0 auto 1.1rem}}
h1{{font-size:1.55rem;font-weight:600;letter-spacing:.4px}}
header p{{color:var(--muted);font-size:.88rem;margin-top:.35rem}}
nav{{display:flex;flex-wrap:wrap;justify-content:center;gap:.5rem;padding:1rem 1rem .4rem;position:sticky;top:0;background:rgba(15,20,32,.95);backdrop-filter:blur(6px);z-index:5}}
nav button{{background:var(--panel);border:1px solid var(--border);color:var(--muted);padding:.5rem 1rem;border-radius:999px;font-size:.85rem;cursor:pointer;transition:all .18s}}
nav button:hover:not(:disabled){{color:var(--txt);border-color:var(--accent)}}
nav button.active{{background:var(--accent);border-color:var(--accent);color:#fff}}
nav button:disabled{{opacity:.38;cursor:not-allowed}}
main{{max-width:760px;margin:0 auto;padding:1.2rem 1rem 3rem}}
.panel{{display:none}}
.panel.active{{display:block}}
ul.list{{list-style:none}}
ul.list li{{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.55rem;transition:border-color .18s}}
ul.list li:hover{{border-color:var(--accent)}}
ul.list a{{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:.7rem 1rem;color:var(--txt);text-decoration:none;font-size:.92rem}}
ul.list a span.date{{color:var(--muted);font-size:.8rem;white-space:nowrap}}
.empty{{color:var(--muted);text-align:center;padding:2.5rem 1rem;font-size:.92rem;background:var(--card);border:1px dashed var(--border);border-radius:10px}}
footer{{text-align:center;color:var(--muted);font-size:.75rem;padding:1.5rem 1rem 2.5rem}}
</style>
</head>
<body>
<header>
  <img src="innovia2.png" alt="Innovia">
  <h1>HERMES Archives</h1>
  <p>Publications et veilles archivées</p>
</header>
<nav id="tabs">
{chr(10).join(nav_btns)}
</nav>
<main>
{chr(10).join(panels_html)}
</main>
<footer>Généré automatiquement — {total} publications</footer>
<script>
document.querySelectorAll('nav button').forEach(function(b){{b.addEventListener('click',function(){{
  if(b.disabled)return;
  document.querySelectorAll('nav button').forEach(function(x){{x.classList.remove('active')}});
  document.querySelectorAll('.panel').forEach(function(p){{p.classList.remove('active')}});
  b.classList.add('active');
  document.getElementById('panel-'+b.dataset.panel).classList.add('active');
}});}});
</script>
</body>
</html>
"""

with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"OK - index.html ecrit, {total} publications")
for pid, nav, panel, has in built:
    print(f"  {pid}: {'OK' if has else 'VIDE'}")
