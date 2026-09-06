# Exercices — Séance 2 : Station Aster

Un atelier universitaire installe **Aster**, une petite station chargée de surveiller son environnement. Pour la mettre en service, il faut progressivement convertir les données de ses capteurs, repérer leur position, analyser leurs mesures et déclencher une alerte.

Chaque exercice ajoute une nouvelle capacité à la station et reprend les notions déjà rencontrées. Les programmes restent indépendants afin de pouvoir être vérifiés séparément. L'objectif final est de disposer des outils nécessaires pour détecter automatiquement une mesure anormale.

## Comment rendre un programme vérifiable

Pour chaque exercice, créer un fichier Python indépendant nommé selon le format `sX_exY.py`, où `X` est le numéro de la séance et `Y` celui de l'exercice. Pour cette séance, les fichiers sont donc nommés `s2_ex1.py`, …, `s2_ex10.py`. Respecter exactement le nom de la fonction, le nombre et l'ordre des arguments attendus ainsi que le type du résultat. Choisir des noms de paramètres clairs. Verificator charge le fichier et appelle la fonction avec plusieurs jeux de données.

- Recevoir les données par les paramètres et renvoyer le résultat avec `return`.
- Ne mettre aucun `input()` ni `print()` dans le fichier remis : l'outil fournit les données et récupère le résultat.
- Ne pas ajouter d'appel de fonction au niveau principal du fichier. Pour essayer son programme, l'exécuter dans un IDE puis appeler la fonction dans sa console Python.
- Les arguments respectent les domaines annoncés : aucune gestion d'exception ni validation de saisie n'est demandée.
- Utiliser seulement les notions des séances 1 et 2. Aucun import, accès aux fichiers, définition de classe, compréhension de liste ou `assert` n'est nécessaire.

## Ex. 1 — Démarrer le capteur de température

**Nom de la fonction :** `convertir_c_en_k`

Le premier capteur d'Aster mesure une température en degrés Celsius, mais sa fiche technique utilise les kelvins. La fonction reçoit une température supérieure ou égale à `-273.15` et renvoie sa valeur en kelvins. Pour effectuer la conversion, ajouter `273.15`. Ne pas arrondir le résultat.

## Ex. 2 — Adapter les unités de distance

**Nom de la fonction :** `convertir_depuis_m`

Les capteurs sont reliés à la station par des câbles dont les longueurs peuvent être affichées dans différentes unités. La fonction reçoit d'abord une longueur positive ou nulle exprimée en mètres, puis une unité parmi `"m"`, `"cm"` et `"km"`. Renvoyer la longueur inchangée pour `"m"`, multipliée par 100 pour `"cm"` ou divisée par 1000 pour `"km"`. Si la seconde donnée n'est pas fournie, utiliser `"m"`. Ne pas arrondir le résultat.

## Ex. 3 — Positionner un capteur

**Nom de la fonction :** `deplacer`

Le plan de l'atelier représente la position d'un capteur par un tuple de deux nombres. La fonction reçoit ce tuple, puis les déplacements horizontal et vertical. Elle renvoie un nouveau tuple contenant les deux coordonnées après le déplacement.

## Ex. 4 — Produire le premier bilan

**Nom de la fonction :** `moyenne`

Aster reçoit maintenant plusieurs mesures d'un même capteur dans une liste non vide. Pour produire son premier bilan, la fonction reçoit cette liste et renvoie la moyenne arithmétique de ses valeurs, sans arrondir le résultat. La liste reçue ne doit pas être modifiée.

## Ex. 5 — Lire un message de la station

**Nom de la fonction :** `analyser_phrase`

La station transmet aussi des messages textuels. Pour préparer leur analyse, la fonction reçoit une chaîne éventuellement vide. Renvoyer un tuple contenant, dans cet ordre : le premier caractère, les cinq premiers caractères, les cinq derniers caractères et la liste des mots. Si la chaîne est vide, le premier caractère doit être la chaîne vide `""`.

## Ex. 6 — Simuler une campagne de mesures

**Nom de la fonction :** `generer_mesures`

Avant de connecter le matériel réel, il faut simuler une campagne de mesures régulières. La fonction reçoit, dans cet ordre, la valeur de départ, le pas entre deux valeurs et le nombre de valeurs à produire. Les deux premières données sont des entiers ; la troisième est un entier compris entre 0 et 100. Renvoyer une nouvelle liste contenant la valeur de départ, puis les valeurs suivantes obtenues en ajoutant successivement le pas. Un pas négatif ou nul est autorisé. Si le nombre demandé vaut zéro, renvoyer une liste vide.

## Ex. 7 — Repérer le pic de mesure

**Nom de la fonction :** `maximum`

Une campagne est terminée : Aster doit maintenant repérer son pic de mesure. La fonction reçoit une liste non vide de nombres et renvoie son plus grand élément. Ne pas modifier la liste reçue.

## Ex. 8 — Enregistrer les capteurs

**Nom de la fonction :** `nettoyer_noms`

Avant le lancement officiel, un technicien transmet les noms des capteurs dans une chaîne séparée par `;`. Cette saisie peut contenir des espaces superflus et des champs vides. La fonction reçoit cette chaîne et renvoie la liste des noms nettoyés. Les espaces placés aux extrémités de chaque nom et les champs vides doivent disparaître. Conserver l'ordre, les doublons, la casse et les espaces à l'intérieur des noms.

## Ex. 9 — Suivre la recharge de la batterie

**Nom de la fonction :** `atteindre_objectif`

Aster doit disposer d'assez d'énergie avant de démarrer sa surveillance. La fonction reçoit, dans cet ordre, la charge de départ, la charge gagnée à chaque étape et la charge à atteindre. Ces valeurs sont des entiers positifs ou nuls, et la charge gagnée à chaque étape est strictement positive. Augmenter la charge jusqu'à atteindre ou dépasser l'objectif, puis renvoyer un tuple contenant le nombre d'étapes et la quantité finale. Si l'objectif est déjà atteint ou dépassé au départ, effectuer zéro étape.

## Ex. 10 — Déclencher la première alerte

**Nom de la fonction :** `premiere_mesure_superieure`

La station est prête pour sa mission finale : parcourir les mesures et signaler la première alerte. La fonction reçoit une liste de nombres éventuellement vide, puis un seuil. Chercher la première mesure **positive ou nulle** strictement supérieure à ce seuil. Les mesures négatives sont invalides et doivent être ignorées, même si elles dépassent le seuil.

Renvoyer l'indice de cette mesure dans la liste d'origine, ou `-1` si aucune mesure ne convient. La recherche doit s'arrêter dès que la première alerte est trouvée.

Une fois cette fonction validée, Aster sait convertir et structurer ses données, préparer une campagne de mesures, en extraire des informations et détecter une situation anormale : la station est opérationnelle.
