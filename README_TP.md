# TP Introduction à l'IA — assistance au développement

**Binôme :** Côme-Alexis PUECH — <Prénom NOM>
**Dépôt de travail :** scikit-learn-contrib/MAPIE
**Assistant utilisé :** OpenCode + Aristote (Qwen3.6-35B-A3B, Qwen3.8-Flash-Next, gemma-4-31B)

## Tâche

Refaire, avec l'assistance d'une IA, le travail de la pull request **#973** —
*fix: classification quantile is one order statistic too high*.

- Commit de référence (solution des mainteneurs) : `d2002dd`
- Commit de départ (état juste avant le merge) : `712966c0`
- Branche de travail : `tp-ia-puech-fernandez`
- Branche témoin, figée au point de départ : `base`

Le bug : `_compute_classification_quantile` (`mapie/utils.py`) sélectionne une
statistique d'ordre trop haute, produisant des ensembles de prédiction
inutilement conservateurs. La couverture reste valide : le défaut est silencieux.

Point notable : la suite de tests existante **ne détecte pas** le bug. Un des
tests (`test_matches_old_formula`) valide l'implémentation contre elle-même.
Le correctif correct fait donc échouer des tests existants.

## Installation

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -U pip && pip install -e . && pip install pytest pytest-xdist
```

## Tests

```bash
pytest mapie/tests/test_utils.py mapie/tests/test_classification.py -q
```

## Diff du travail

```bash
git diff base..tp-ia-puech-fernandez
```

## Notes

<à compléter>
