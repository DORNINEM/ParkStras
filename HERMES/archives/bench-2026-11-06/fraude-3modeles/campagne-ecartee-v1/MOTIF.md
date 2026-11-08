# Tirages écartés — campagne fraude v1, 08/11/2026

Campagne `bench_test_fraude_3modeles.sh` (suffixe `-ct3-rN`), lancée à 16h56, terminée à 18h22,
neuf bras produits (3 modèles × 3 répétitions), 18 fichiers.

**Pourquoi tout est écarté.** L'audit des neuf sessions de bras (appel par appel, dans
`~/.hermes/profiles/demo/state.db`) montre qu'**une seule** est contaminée : la session `32f42293`,
un sous-agent du bras DeepSeek de la première répétition, qui a listé `/Users/manud/dev/ParkStras` et
lu `veille-FRAUDE-2026-11-03-hybride.md` pour s'inspirer de la structure de l'édition de production.
Aucune écriture hors du bac à sable, le dépôt de production est intact — le défaut est une **lecture**,
pas une écriture.

**Pourquoi ne pas garder les huit autres.** Le garde-fou qui interdisait cette lecture fait partie de
la consigne envoyée aux bras. Le durcir pour la seule répétition fautive donnerait neuf tirages
produits sous deux textes différents, et un banc dont les bras ne partagent pas la même consigne n'est
plus un banc. Les neuf tirages sont donc conservés ici comme trace, et la campagne repart de zéro en
v2 (`-ct3b-rN`) avec le garde-fou durci pour tout le monde.

**Correction de fond.** Le garde-fou du harnais (`~/.hermes/scripts/veille_model_bench.py`) interdisait
d'écrire hors du bac à sable, jamais de lire les veilles existantes. Il interdit désormais explicitement
de chercher une édition précédente, de lister ParkStras et de s'inspirer d'une veille existante ; seul
le gabarit HTML du skill reste une référence autorisée. La v2 embarque en plus son propre contrôle de
non-contamination en fin de campagne, qui inspecte les sessions des neuf bras et signale tout appel
vers ParkStras ou vers une édition précédente.

**Ce que la v1 montre quand même, sans valeur de mesure.** Les trois modèles remplissent les sept axes
sur les neuf tirages, avec cinq signaux faibles sourcés sur cinq et sept blocs audio : la procédure
tient. Les mesures generiques de `veille_bench_metrics.py` affichent « sections absentes : france,
europe, monde, juridique, metiers, prospective, mistral » et « hors fenêtre 7j » pour des dates
d'octobre : ce sont les contrôles des autres thèmes, inapplicables ici (fenêtre mensuelle, sept axes
propres) — les mesures du thème passent par `bench_fraude_axes.py`.