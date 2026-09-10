# Validation — séance 3

## Contrat compatible avec Verificator

Les dix énoncés sont dans `data/exercices/seance3.md` et les dix solutions dans
`data/corrections/seance3.md`. Chaque exercice demande un fichier indépendant
contenant une fonction, sans saisie, affichage ou appel au chargement.

La progression couvre l'import d'un module, la lecture et l'écriture de fichiers
texte, le découpage d'un CSV simple avec `split`, puis la création, l'indexation, la vectorisation et les
calculs suivant un axe avec NumPy. Les fichiers temporaires nécessaires aux tests
sont créés par le correcteur : aucun fichier de données n'est à déposer dans
Verificator avec la solution.

## Vérification locale

Depuis le dossier du cours :

```text
python validation_seance3.py chemin/vers/s3_ex1.py calculer_distance
python validation_seance3.py chemin/vers/s3_ex10.py calculer_moyennes
```

Pour vérifier toutes les fonctions regroupées dans `seance3.py` à côté du
correcteur : `python validation_seance3.py`.

Conserver `data/validation/seance3.py` avec le script : il contient le catalogue
commun des tests. Le processus de validation est interrompu après cinq secondes.
Les nombres et tableaux NumPy sont comparés avec une tolérance de `1e-9`. Les
tests vérifient également le type et la forme des tableaux, le contenu exact du
rapport et l'absence de modification des arguments.

## Intégration dans Verificator

Copier `data/validation/seance3.py` vers
`verificator/exercises/session3.py`, ajouter NumPy aux dépendances, puis réunir
`EXERCICES_SEANCE2` et `EXERCICES_SEANCE3` dans le catalogue global :

```python
from .session2 import EXERCICES_SEANCE2
from .session3 import EXERCICES_SEANCE3

EXERCISES = {
    exercice.id: exercice
    for exercice in EXERCICES_SEANCE2 + EXERCICES_SEANCE3
}
SESSIONS = {"2": "Séance 2", "3": "Séance 3"}
```
