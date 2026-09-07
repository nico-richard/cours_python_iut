# Validation — séance 2

## Contrat compatible avec Verificator

Les dix énoncés sont dans `data/exercices/seance2.md` et les dix solutions dans
`data/corrections/seance2.md`. Chaque exercice demande un fichier indépendant
contenant une fonction, sans saisie, affichage ou appel au chargement.
Les essais des étudiants se font dans la console Python de leur IDE : ils n'ont pas à
apprendre `assert`, les imports ou le bloc `if __name__ == "__main__"`.

Le cours reste inchangé. La progression couvre fonctions et retour, paramètre
par défaut, tuples et dépaquetage, indexation, listes, slicing, méthodes de
chaînes et de listes, `for`, `range`, compteurs, `while`, `break` et `continue`.
L'utilisation d'objets existants se pratique avec les chaînes et listes ; aucune
classe de capteur fictive ni définition de classe n'est nécessaire.

Prévoir 140 minutes d'exercices et 10 minutes de prise en main et d'échanges.
Cette durée est indicative et comprend les essais et corrections individuelles.

## Vérification locale

Depuis le dossier du cours :

```text
python validation_seance2.py chemin/vers/s2_ex1.py convertir_c_en_k
python validation_seance2.py chemin/vers/s2_ex10.py premiere_mesure_superieure
```

Pour vérifier toutes les fonctions regroupées dans `seance2.py` à côté du
correcteur : `python validation_seance2.py`.
Conserver `data/validation/seance2.py` avec le script : il contient le catalogue
commun de 51 cas. Le processus de validation est interrompu après cinq secondes
pour repérer notamment une boucle qui ne se termine pas.

Les listes et tuples retournés doivent avoir le type et l'ordre demandés.
Les nombres sont comparés avec une tolérance de 1e-9 (relative ou absolue).
Les conversions de distance sont arrondies au dixième et la moyenne au centième,
conformément aux énoncés. Les tests vérifient aussi que les arguments ne sont pas
modifiés. Les cas n'utilisent que les domaines annoncés dans les énoncés.

## Intégration dans Verificator (enseignant)

Le code du dépôt `Verificator` utilise
`Exercise(id, session, title, filename, function_name, test_module)` et
`test_module(module)` ; il ne compare pas des entrées/sorties de console.

Le fichier `data/validation/seance2.py` sert de catalogue de référence au fichier
`verificator/exercises/session2.py`. Ils exposent les dix objets dans
`EXERCICES_SEANCE2`, ainsi que `moyenne_exercise` et `test_moyenne` pour
compatibilité avec l'exercice historique. L'identifiant `s2-moyenne` est conservé.
Dans `verificator/exercises/__init__.py`, remplacer l'enregistrement de la seule
moyenne par :

```python
from .session2 import EXERCICES_SEANCE2

EXERCISES = {exercice.id: exercice for exercice in EXERCICES_SEANCE2}
SESSIONS = {"2": "Séance 2"}
```

Les tests sont du code enseignant et peuvent employer des notions qui ne sont pas
demandées aux étudiants.

## Ce que les tests ne prouvent pas

Les tests contrôlent des résultats sur des cas variés. Ils ne prouvent pas que
l'étudiant utilise réellement la boucle, le dépaquetage ou la méthode imposée,
ni qu'il n'a pas codé les réponses en dur. Vérifier ces contraintes par lecture
du code, ainsi que la clarté des noms et l'absence de variables globales inutiles.
Les corrigés respectent les contraintes pédagogiques annoncées.
