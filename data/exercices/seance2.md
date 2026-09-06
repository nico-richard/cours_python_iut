# Exercices — Séance 2 : Station Aster

Programmer les fonctions de la station Aster, de la conversion des mesures au déclenchement d'une alerte.

## Consignes communes

Créer un fichier indépendant par exercice, nommé `s2_ex1.py`, …, `s2_ex10.py`. Respecter le nom de la fonction, l'ordre des arguments et le résultat demandé. Choisir des noms de paramètres clairs.

- Recevoir les données par les paramètres et renvoyer le résultat avec `return`, sans modifier les données reçues.
- Ne pas mettre d'`input()`, de `print()` ni d'appel de fonction dans le fichier remis. Pour les essais, appeler la fonction dans la console Python d'un IDE.
- Utiliser uniquement les notions des séances 1 et 2. Les données respectent les conditions annoncées : aucune vérification des arguments n'est demandée.

## Ex. 1 — Démarrer le capteur de température

**Nom de la fonction :** `convertir_c_en_k`

Recevoir une température en degrés Celsius, supérieure ou égale à `-273.15`. Renvoyer la température en kelvins en ajoutant `273.15`, sans arrondir.

## Ex. 2 — Adapter les unités de distance

**Nom de la fonction :** `convertir_depuis_m`

Recevoir une longueur positive ou nulle en mètres, puis une unité parmi `"m"`, `"cm"` et `"km"`. Renvoyer, sans arrondir :

- pour `"m"` : la longueur inchangée ;
- pour `"cm"` : la longueur multipliée par 100 ;
- pour `"km"` : la longueur divisée par 1000.

Utiliser `"m"` par défaut si l'unité n'est pas fournie.

## Ex. 3 — Positionner un capteur

**Nom de la fonction :** `deplacer`

Recevoir un tuple de deux coordonnées, puis un déplacement horizontal et un déplacement vertical. Ajouter chaque déplacement à la coordonnée correspondante et renvoyer les deux nouvelles coordonnées dans un tuple.

## Ex. 4 — Produire le premier bilan

**Nom de la fonction :** `moyenne`

Recevoir une liste non vide de nombres. Renvoyer leur moyenne : la somme des valeurs divisée par leur nombre, sans arrondir.

## Ex. 5 — Lire un message de la station

**Nom de la fonction :** `analyser_phrase`

Recevoir une chaîne, éventuellement vide. Renvoyer un tuple contenant, dans cet ordre :

- le premier caractère, ou `""` si la chaîne est vide ;
- les cinq premiers caractères ;
- les cinq derniers caractères ;
- la liste des mots.

Si la chaîne contient moins de cinq caractères, conserver tous les caractères disponibles. Les espaces successifs ne doivent pas produire de mots vides.

## Ex. 6 — Simuler une campagne de mesures

**Nom de la fonction :** `generer_mesures`

Recevoir trois entiers, dans cet ordre : une valeur de départ, un pas et un nombre de valeurs compris entre 0 et 100.

Renvoyer une liste de la longueur demandée : commencer par la valeur de départ, puis ajouter le pas pour obtenir chaque valeur suivante. Le pas peut être négatif ou nul. Si le nombre demandé vaut zéro, renvoyer une liste vide.

## Ex. 7 — Repérer le pic de mesure

**Nom de la fonction :** `maximum`

Recevoir une liste non vide de nombres et renvoyer son plus grand élément.

## Ex. 8 — Enregistrer les capteurs

**Nom de la fonction :** `nettoyer_noms`

Recevoir une chaîne contenant des noms séparés par `;`. Renvoyer une liste en retirant les espaces aux extrémités de chaque nom et en supprimant les noms vides.

Conserver l'ordre, les doublons, les majuscules, les minuscules et les espaces à l'intérieur des noms.

## Ex. 9 — Suivre la recharge de la batterie

**Nom de la fonction :** `atteindre_objectif`

Recevoir, dans cet ordre, la charge initiale, le gain par étape et la charge à atteindre. Ce sont des entiers positifs ou nuls ; le gain est strictement positif.

Ajouter le gain à chaque étape jusqu'à atteindre ou dépasser l'objectif. Renvoyer un tuple contenant le nombre d'étapes et la charge finale. Si l'objectif est déjà atteint ou dépassé au départ, effectuer zéro étape.

## Ex. 10 — Déclencher la première alerte

**Nom de la fonction :** `premiere_mesure_superieure`

Recevoir une liste de nombres, éventuellement vide, puis un seuil. Ignorer les mesures négatives et chercher la première mesure positive ou nulle **strictement supérieure** au seuil.

Renvoyer l'indice de cette mesure dans la liste d'origine, ou `-1` si aucune mesure ne convient. La recherche doit s'arrêter dès que la première alerte est trouvée.
