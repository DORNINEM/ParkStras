(function () {
  document.addEventListener('DOMContentLoaded', function () {
    const groups = [
      { pattern: /^MISTRAL.*\.html$/i, label: 'Actualités Mistral', tabId: 'mistral' },
      { pattern: /^veille-IA.*\.html$/i, label: 'Actualités IA global', tabId: 'veille' },
      { pattern: /^veille-EPS.*\.html$/i, label: 'Veille télésurveillance', tabId: 'veille-eps' },
    ];

    const tabsContainer = document.getElementById('tabs');
    const panelsContainer = document.getElementById('panels');

    fetch('files.json')
      .then(function (response) { return response.json(); })
      .then(function (allFiles) { buildTabs(allFiles); })
      .catch(function () { buildTabs([]); });

    function buildTabs(allFiles) {
    groups.forEach(function (group, index) {
      const files = allFiles
        .filter(function (href) {
          return href && group.pattern.test(href.split('/').pop() || '');
        })
        .sort()
        .reverse();

      const tab = document.createElement('button');
      tab.className = 'tab' + (index === 0 ? ' active' : '') + (files.length === 0 ? ' disabled' : '');
      tab.setAttribute('data-tab', group.tabId);
      tab.textContent = group.label + (files.length === 0 ? ' (aucun)' : '');

      const section = document.createElement('section');
      section.className = 'panel' + (index === 0 ? ' open' : '');
      section.id = group.tabId;

      if (files.length === 0) {
        const empty = document.createElement('div');
        empty.className = 'empty';
        empty.textContent = 'Aucune publication disponible.';
        section.appendChild(empty);
      } else {
        files.forEach(function (href) {
          var name = href.split('/').pop();
          var label = name
            .replace(/.*veille-(IA|EPS)-/i, '')
            .replace(/^MISTRAL-?/i, '')
            .replace(/\.html$/i, '')
            .trim();
          var article = document.createElement('article');
          article.className = 'entry';
          var a = document.createElement('a');
          a.href = href;
          a.textContent = label || href;
          article.appendChild(a);
          section.appendChild(article);
        });
      }

      tabsContainer.appendChild(tab);
      panelsContainer.appendChild(section);
    });

    var tabs = document.querySelectorAll('.tab');
    var panels = document.querySelectorAll('.panel');

    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        if (tab.classList.contains('disabled')) return;
        var target = tab.getAttribute('data-tab');
        tabs.forEach(function (t) {
          t.classList.toggle('active', t === tab);
        });
        panels.forEach(function (p) {
          p.classList.toggle('open', p.id === target);
        });
      });
    });
    }
  });
})();
