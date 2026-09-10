# Exercices — Séance 3 : Mission Bathys

Le bathyscaphe Bathys vient de remonter une série de mesures. Votre objectif consiste à lire ces données, à les conserver puis à les analyser avec NumPy.

## Consignes communes

Créer un fichier indépendant par exercice, nommé `s3_ex1.py`, …, `s3_ex10.py`. Respecter le nom de la fonction, l'ordre des arguments et le résultat demandé.

- Recevoir les données par les paramètres et renvoyer le résultat avec `return`, sans modifier les données reçues.
- Ne pas mettre d'`input()`, de `print()` ni d'appel de fonction dans le fichier remis. Pour les essais, appeler la fonction dans une console Python.
- Utiliser uniquement les notions des séances 1 à 3.
- Pour les exercices utilisant un fichier, le chemin est fourni à la fonction : ne pas imposer de nom de fichier dans le programme.

## Ex. 1 — Calculer une distance

**Nom de la fonction :** `calculer_distance`

Le déplacement horizontal et le déplacement vertical de Bathys forment les deux côtés d'un triangle rectangle. Recevoir ces deux longueurs positives ou nulles et renvoyer la distance parcourue, calculée avec `math.sqrt`, sans arrondir.

## Ex. 2 — Relire les profondeurs

**Nom de la fonction :** `lire_valeurs`

Un fichier texte contient une valeur numérique par ligne. Recevoir son chemin, lire le fichier avec `with open(...)` et renvoyer la liste des nombres convertis en `float`, dans leur ordre d'origine.

Le fichier est encodé en UTF-8 et ne contient pas de ligne vide.

## Ex. 3 — Décoder le journal CSV

**Nom de la fonction :** `lire_mesures_csv`

Le journal de plongée est un fichier CSV encodé en UTF-8. Sa première ligne contient l'en-tête `temps;temperature` ; les lignes suivantes contiennent deux nombres séparés par `;`.

Recevoir le chemin du fichier et renvoyer un tuple contenant la liste des temps puis la liste des températures. Toutes les valeurs doivent être converties en `float`. Utiliser le module `csv` et ignorer l'en-tête.

## Ex. 4 — Rédiger le bilan de plongée

**Nom de la fonction :** `ecrire_rapport`

Recevoir le chemin du rapport à créer et une liste non vide de températures. Écrire, en UTF-8, exactement trois lignes donnant la moyenne, le minimum et le maximum, arrondis à deux décimales :

```text
Moyenne : 20.50 °C
Minimum : 19.25 °C
Maximum : 21.75 °C
```

Les valeurs ci-dessus illustrent uniquement le format attendu. Terminer chaque ligne, y compris la dernière, par `\n`. La fonction ne renvoie rien.

## Ex. 5 — Convertir la série en kelvins

**Nom de la fonction :** `convertir_en_kelvins`

Recevoir une liste de températures en degrés Celsius. Créer un `ndarray` NumPy puis renvoyer un nouveau tableau contenant les températures en kelvins. Effectuer la conversion sur le tableau entier, sans boucle et sans arrondir.

## Ex. 6 — Construire l'axe du temps

**Nom de la fonction :** `creer_instants`

Recevoir une durée positive ou nulle et un nombre de mesures supérieur ou égal à 2. Renvoyer avec `np.linspace` un `ndarray` contenant ce nombre d'instants régulièrement espacés entre `0` et la durée, bornes incluses.

## Ex. 7 — Charger les colonnes avec NumPy

**Nom de la fonction :** `charger_mesures_numpy`

Recevoir le chemin d'un fichier ayant la même structure que dans l'exercice 3. Le charger avec `np.loadtxt`, puis renvoyer un tuple contenant la colonne des temps et la colonne des températures sous forme de deux `ndarray` à une dimension.

## Ex. 8 — Corriger l'étalonnage

**Nom de la fonction :** `corriger_mesures`

Le capteur applique une relation affine à toutes ses mesures. Recevoir une séquence de nombres, un coefficient et un décalage. Renvoyer un nouveau `ndarray` contenant, pour chaque mesure, `mesure * coefficient + decalage`.

Effectuer le calcul sur le tableau entier, sans boucle et sans modifier la séquence reçue.

## Ex. 9 — Résumer la campagne

**Nom de la fonction :** `calculer_statistiques`

Recevoir une séquence non vide de nombres, la convertir en `ndarray` et renvoyer un tuple contenant, dans cet ordre, la moyenne, l'écart-type, le minimum et le maximum calculés avec NumPy. Ne pas arrondir les résultats.

L'écart-type attendu est celui calculé par défaut par NumPy avec `std()`.

## Ex. 10 — Comparer les capteurs

**Nom de la fonction :** `calculer_moyennes`

Recevoir un tableau NumPy à deux dimensions dont chaque ligne correspond à un capteur et chaque colonne à un instant. Renvoyer un tuple contenant :

- la moyenne de chaque capteur (`axis=1`) ;
- la moyenne de chaque instant (`axis=0`).

Les deux résultats doivent être des `ndarray`. Ne pas modifier le tableau reçu.
