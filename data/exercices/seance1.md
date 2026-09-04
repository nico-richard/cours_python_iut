# Exercices — Séance 1 : Premiers programmes Python

**Ex. 1 — Premier script**
Créer un fichier `bonjour.py` qui affiche votre nom et votre filière, puis l'exécuter depuis un terminal.

**Ex. 2 — Calculatrice d'opérations**
Demander deux nombres à l'utilisateur (`input`) et afficher le résultat de `+ - * / // % **` entre eux, avec des f-strings lisibles. Pour ce premier exercice, choisir un second nombre non nul.

**Ex. 3 — Conversions de types**
Demander une chaîne comme `"3.14"`, la convertir en `float`, puis afficher la valeur avec deux chiffres après la virgule à l'aide d'une f-string.

**Ex. 4 — Classification d'une mesure**
Demander une pression en bar et afficher : "normale" si `1 <= pression <= 2`, "alerte" si `0 <= pression < 1` ou `2 < pression <= 3`, et "danger" si `pression > 3`. Une valeur négative doit être signalée comme invalide.

**Ex. 5 — Autonomie d'une batterie**
Demander la capacité d'une batterie en ampères-heures et le courant consommé en ampères. Calculer l'autonomie théorique `capacite / courant`, l'afficher avec une décimale, puis indiquer "faible" sous 2 h, "moyenne" de 2 h à moins de 5 h, ou "élevée" à partir de 5 h. Signaler le cas d'un courant nul ou négatif.

**Ex. 6 — Devis pour une impression 3D**
Un fablab souhaite vérifier qu'une impression 3D respecte le budget d'un client. Écrire un programme qui demande :

- la masse de filament nécessaire en grammes ;
- le prix d'un kilogramme de filament ;
- la durée d'impression en heures ;
- la puissance électrique moyenne de l'imprimante en kilowatts ;
- le budget maximal du client.

Le prix de l'électricité est fixé à **0,25 € par kWh**.

Calculer séparément le coût du filament, le coût de l'électricité et le coût total, puis les afficher avec deux chiffres après la virgule. Si une valeur saisie est négative, afficher un message d'erreur. Sinon, afficher `Devis accepté` lorsque le coût total ne dépasse pas le budget, ou `Budget dépassé` avec le montant du dépassement dans le cas contraire. Si le devis est accepté, afficher aussi le budget restant.

Exemple de calcul : pour 250 g de filament à 24 €/kg, 5 h d'impression avec une puissance de 0,12 kW et une électricité à 0,25 €/kWh, le filament coûte 6 € et l'électricité 0,15 €.
