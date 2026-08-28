# Exercices — Séance 1 : Premiers programmes Python

**Ex. 1 — Premier script**
Créer un fichier `bonjour.py` qui affiche votre nom et votre filière, puis l'exécuter depuis un terminal.

**Ex. 2 — Calculatrice d'opérations**
Demander deux nombres à l'utilisateur (`input`) et afficher le résultat de `+ - * / // % **` entre eux, avec des f-strings lisibles.

**Ex. 3 — Conversions de types**
Demander une chaîne comme `"3.14"`, la convertir en `float`, puis afficher la valeur avec deux chiffres après la virgule à l'aide d'une f-string.

**Ex. 4 — Précision flottante**
Calculer `0.1 + 0.2`, comparer à `0.3` avec `==` puis avec une tolérance (`abs(a-b) < 1e-9`). Expliquer la différence en commentaire.

**Ex. 5 — Classification d'une mesure**
Demander une pression en bar et afficher : "normale" si `1 <= pression <= 2`, "alerte" si `0 <= pression < 1` ou `2 < pression <= 3`, et "danger" si `pression > 3`. Une valeur négative doit être signalée comme invalide.

**Ex. 6 — Autonomie d'une batterie**
Demander la capacité d'une batterie en ampères-heures et le courant consommé en ampères. Calculer l'autonomie théorique `capacite / courant`, l'afficher avec une décimale, puis indiquer "faible" sous 2 h, "moyenne" de 2 h à moins de 5 h, ou "élevée" à partir de 5 h. Signaler le cas d'un courant nul ou négatif.
