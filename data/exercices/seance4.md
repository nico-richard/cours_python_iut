# Exercices — Séance 4 : Banc de mesure

Une campagne de mesures doit être représentée puis reliée à un instrument. Les exercices construisent progressivement les fonctions de visualisation et de communication nécessaires.

## Consignes communes

Créer un fichier indépendant par exercice, nommé `s4_ex1.py`, …, `s4_ex10.py`. Respecter le nom de la fonction, l'ordre des arguments et le résultat demandé.

- Recevoir les données par les paramètres, sans les modifier. Lorsqu'un résultat est demandé, le renvoyer avec `return`.
- Ne pas mettre d'`input()`, de `print()`, de `plt.show()` ni d'appel de fonction dans le fichier remis. Pour les essais, appeler la fonction dans une console Python.
- Utiliser uniquement les notions des séances 1 à 4.
- Utiliser uniquement les fonctions de `matplotlib.pyplot` sous la forme `plt.plot()`, `plt.xlabel()`, etc. Ne pas manipuler d'objets `Figure` ou `Axes`.
- Lorsqu'une fonction produit un graphique, elle ne renvoie rien. Le graphique sera vérifié après l'appel de la fonction.

## Ex. 1 — Tracer l'évolution d'une mesure

**Nom de la fonction :** `tracer_evolution`

Recevoir une séquence d'instants puis une séquence de mesures de même longueur. Tracer la courbe des mesures en fonction du temps avec `plt.plot()`. La fonction ne renvoie rien.

## Ex. 2 — Produire un graphique scientifique

**Nom de la fonction :** `annoter_courbe`

Recevoir une séquence d'instants puis une séquence de températures de même longueur. Créer une courbe bleue avec le marqueur `"o"` et le label `"Température"`.

Ajouter les éléments suivants :

- abscisse : `"Temps (s)"` ;
- ordonnée : `"Température (°C)"` ;
- titre : `"Évolution de la température"` ;
- grille avec une transparence `alpha=0.3` ;
- légende.

La fonction ne renvoie rien.

## Ex. 3 — Étudier la relation entre deux grandeurs

**Nom de la fonction :** `tracer_nuage`

Recevoir deux séquences de même longueur : les tensions puis les courants correspondants. Créer un nuage de points avec `plt.scatter()`. La fonction ne renvoie rien.

## Ex. 4 — Observer une distribution

**Nom de la fonction :** `tracer_histogramme`

Recevoir une séquence de mesures et un nombre de classes. Utiliser `5` comme nombre de classes par défaut. Créer l'histogramme avec `plt.hist()`. La fonction ne renvoie rien.

## Ex. 5 — Comparer deux représentations

**Nom de la fonction :** `creer_comparaison`

Recevoir une séquence d'instants puis une séquence de températures de même longueur. Créer deux sous-graphiques côte à côte avec `plt.subplot()` :

- à gauche, la température en fonction du temps ;
- à droite, l'histogramme des températures avec `5` classes.

Ajuster les espacements avec `plt.tight_layout()`. La fonction ne renvoie rien.

## Ex. 6 — Exporter une courbe

**Nom de la fonction :** `exporter_courbe`

Recevoir le chemin du fichier PNG à créer, une séquence d'instants puis une séquence de températures. Créer une courbe dont les axes sont nommés `"Temps (s)"` et `"Température (°C)"`.

Enregistrer le graphique avec `plt.savefig()` en utilisant `dpi=300` et `bbox_inches="tight"`. La fonction ne renvoie rien.

## Ex. 7 — Décoder une mesure reçue

**Nom de la fonction :** `decoder_mesure`

Recevoir une suite d'octets contenant un nombre encodé en UTF-8 et éventuellement terminé par des caractères de fin de ligne. Décoder les octets, retirer les caractères aux extrémités avec `strip()` puis renvoyer la mesure convertie en `float`.

Exemple : `b"20.5\r\n"` doit produire `20.5`.

## Ex. 8 — Préparer une commande

**Nom de la fonction :** `encoder_commande`

Recevoir une commande sous forme de chaîne sans caractère de fin de ligne. Ajouter `"\n"`, encoder le texte en UTF-8 et renvoyer les octets obtenus.

Exemple : `"*IDN?"` doit produire `b"*IDN?\n"`.

## Ex. 9 — Lire une série de mesures

**Nom de la fonction :** `lire_mesures`

Recevoir un objet `port` déjà ouvert et un nombre de mesures positif ou nul. À chaque itération, appeler `port.readline()`, décoder la réponse comme dans l'exercice 7 et ajouter le nombre obtenu à une liste. Renvoyer la liste des mesures dans leur ordre de réception.

Le port fourni possède une méthode `readline()` et chaque lecture contient une mesure valide.

## Ex. 10 — Interroger un instrument

**Nom de la fonction :** `interroger_instrument`

Recevoir un objet `port` déjà ouvert et une commande sous forme de chaîne sans fin de ligne. Encoder la commande comme dans l'exercice 8, l'envoyer avec `port.write()`, puis lire une réponse avec `port.readline()`.

Décoder la réponse en UTF-8, retirer ses caractères aux extrémités et renvoyer le texte obtenu. Le port fourni possède les méthodes `write()` et `readline()`.

## Activité facultative avec le matériel

Si un port série est disponible, ouvrir la liaison avec `serial.Serial(...)`, appeler `lire_mesures()` pour acquérir dix valeurs, puis tracer le résultat. Les paramètres du port et la terminaison des messages doivent être vérifiés dans la documentation du matériel.
