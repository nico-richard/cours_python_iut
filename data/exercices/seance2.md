# Exercices — Séance 2 : Station Aster

La station scientifique Aster vient d'être déployée sur un site isolé. Votre objectif consiste à programmer les fonctions nécessaires à sa mise en service, du traitement des premières mesures au déclenchement d'une alerte.

## Consignes communes

Chaque fonction sera ensuite intégrée au programme de la station. Créer un fichier indépendant par exercice, nommé `s2_ex1.py`, …, `s2_ex10.py`. Respecter le nom de la fonction, l'ordre des arguments et le résultat demandé.

- Recevoir les données par les paramètres et renvoyer le résultat avec `return`, sans modifier les données reçues.
- Ne pas mettre d'`input()`, de `print()` ni d'appel de fonction dans le fichier remis. Pour les essais, appeler la fonction dans une console Python.
- Utiliser uniquement les notions des séances 1 et 2.

## Ex. 1 — Démarrer le capteur de température

**Nom de la fonction :** `convertir_c_en_k`

Le capteur transmet ses relevés en degrés Celsius, mais le système central utilise les kelvins. Recevoir une température en Celcius physiquement possible et renvoyer la valeur correspondante en kelvins, sans arrondir.

## Ex. 2 — Adapter les unités de distance

**Nom de la fonction :** `convertir_depuis_m`

Les différents appareils de la station n'utilisent pas toujours la même unité de distance. Recevoir une longueur positive ou nulle en mètres, puis une unité cible parmi `"m"`, `"cm"` et `"km"`. Renvoyer la longueur convertie dans cette unité, arrondie au dixième.

Utiliser `"m"` comme unité cible par défaut si elle n'est pas fournie.

## Ex. 3 — Positionner un capteur

**Nom de la fonction :** `deplacer`

Un capteur mobile doit être repositionné sur la zone d'étude. Recevoir sa position sous forme de tuple, ainsi qu'un déplacement horizontal et un déplacement vertical. Renvoyer la position obtenue après ce déplacement.

## Ex. 4 — Produire le premier bilan

**Nom de la fonction :** `moyenne`

Après les premiers relevés, l'équipe souhaite obtenir une valeur représentative. Recevoir une liste non vide de nombres et renvoyer leur moyenne, arrondie au centième.

## Ex. 5 — Lire un message de la station

**Nom de la fonction :** `analyser_phrase`

Le centre de contrôle doit extraire plusieurs informations d'un message transmis par la station. Recevoir une chaîne, éventuellement vide. Renvoyer un tuple contenant, dans cet ordre :

- le premier caractère, ou `""` si la chaîne est vide ;
- les cinq premiers caractères ;
- les cinq derniers caractères ;
- la liste des mots.

Si la chaîne contient moins de cinq caractères, conserver tous les caractères disponibles. Les espaces successifs ne doivent pas produire de mots vides.

## Ex. 6 — Simuler une campagne de mesures

**Nom de la fonction :** `generer_mesures`

Avant une campagne réelle, l'équipe veut produire une série de mesures simulées. Recevoir trois entiers, dans cet ordre : une valeur de départ, un pas et un nombre de valeurs compris entre 0 et 100.

Renvoyer la liste de valeurs obtenue à partir de la valeur de départ et du pas indiqué. Le pas peut être négatif ou nul. Si le nombre demandé vaut zéro, renvoyer une liste vide.

## Ex. 7 — Repérer le pic de mesure

**Nom de la fonction :** `maximum`

Les scientifiques cherchent le relevé le plus élevé de la campagne. Recevoir une liste non vide de nombres et renvoyer son plus grand élément.

## Ex. 8 — Enregistrer les capteurs

**Nom de la fonction :** `nettoyer_noms`

La liste des capteurs a été saisie rapidement avant le déploiement et doit être nettoyée. Recevoir une chaîne contenant des noms séparés par `;`. Renvoyer une liste en retirant les espaces aux extrémités de chaque nom et en supprimant les noms vides.

Conserver l'ordre, les doublons, les majuscules, les minuscules et les espaces à l'intérieur des noms.

## Ex. 9 — Suivre la recharge de la batterie

**Nom de la fonction :** `atteindre_objectif`

La batterie de secours se recharge progressivement et doit atteindre un niveau suffisant avant la prochaine mission. Recevoir, dans cet ordre, la charge initiale, le gain par étape et la charge à atteindre. Ce sont des entiers positifs ou nuls ; le gain est strictement positif.

Renvoyer un tuple contenant le nombre d'étapes nécessaires pour atteindre ou dépasser l'objectif et la charge finale. Si l'objectif est déjà atteint ou dépassé au départ, renvoyer zéro étape.

## Ex. 10 — Déclencher la première alerte

**Nom de la fonction :** `premiere_mesure_superieure`

Le système de surveillance doit signaler le premier relevé valide qui dépasse un seuil critique. Recevoir une liste de nombres, éventuellement vide, puis un seuil. Ignorer les mesures négatives et chercher la première mesure positive ou nulle **strictement supérieure** au seuil.

Renvoyer l'indice de cette mesure dans la liste d'origine, ou `-1` si aucune mesure ne convient.
