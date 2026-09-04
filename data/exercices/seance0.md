# Exercices — Séance 0 : Installer les outils et exécuter un premier programme

## Objectifs

À la fin de cette séance, vous saurez :

- ouvrir une console sous Windows ;
- vérifier que Python est disponible ;
- tester quelques instructions dans l'interpréteur Python ;
- préparer les dossiers qui serviront pendant le cours ;
- lancer la version portable de Thonny ;
- créer puis exécuter un fichier `.py` depuis la console et depuis Thonny.

Conservez cette arborescence pendant les quatre séances : tous les fichiers du
cours seront rangés au même endroit.

---

## 1. Ouvrir une console

1. Ouvrez le menu **Démarrer** de Windows.
2. Saisissez `PowerShell` dans la zone de recherche.
3. Ouvrez **Windows PowerShell** ou **Terminal**.

Une fenêtre avec une ligne qui ressemble à celle-ci doit apparaître :

```text
PS C:\Users\VotreNom>
```

La partie située avant `>` indique le dossier dans lequel se trouve la
console. Ne recopiez pas cette partie dans les commandes.

### Vérification

Saisissez la commande suivante, puis appuyez sur **Entrée** :

```powershell
py --version
```

Le résultat attendu ressemble à `Python 3.12.4`. Le numéro exact peut être
différent. Si la commande `py` n'est pas reconnue, essayez :

```powershell
python --version
```

Si l'une des deux commandes affiche `Python 3.x`, Python est disponible. Si
aucune ne fonctionne, arrêtez-vous et prévenez l'enseignant avant de poursuivre.

---

## 2. Tester Python dans la console

Lancez l'interpréteur interactif avec la commande qui a fonctionné :

```powershell
py
```

ou :

```powershell
python
```

Le symbole `>>>` indique que Python attend une instruction. Saisissez les
lignes suivantes **une par une** et observez chaque résultat :

```python
print("Bonjour Python !")
2 + 3
10 / 4
2 ** 8
```

Créez ensuite deux variables et utilisez-les dans un calcul :

```python
tension = 5.0
courant = 0.2
puissance = tension * courant
print(puissance)
print(f"Puissance : {puissance} W")
```

Terminez l'interpréteur avec :

```python
exit()
```

Vous devez retrouver une ligne commençant par `PS`. Vous êtes revenu dans la
console Windows.

---

## 3. Préparer le dossier de travail

Dans l'Explorateur de fichiers, ouvrez votre dossier **Documents**, puis créez
un dossier nommé :

```text
Python_IUT
```

Dans `Python_IUT`, créez les dossiers suivants :

```text
Python_IUT
├── logiciels
├── seance0
├── seance1
├── seance2
├── seance3
└── seance4
```

Le dossier `logiciels` contiendra Thonny. Chaque dossier `seanceN` contiendra
les programmes et les données de la séance correspondante.

### Méthode rapide avec PowerShell — facultatif

Si vous êtes à l'aise dans la console, vous pouvez créer la même arborescence
avec les commandes suivantes :

```powershell
cd $HOME\Documents
mkdir Python_IUT
cd Python_IUT
mkdir logiciels, seance0, seance1, seance2, seance3, seance4
```

Vérifiez le résultat dans l'Explorateur de fichiers avant de continuer.

---

## 4. Télécharger et décompresser Thonny portable

1. Ouvrez la page officielle [thonny.org](https://thonny.org/).
2. Dans les téléchargements pour Windows, choisissez l'archive dont le nom se
   termine par **`windows-portable-x64.zip`**. Le numéro de version peut changer.
3. Enregistrez le fichier ZIP dans `Documents\Python_IUT\logiciels`.
4. Dans l'Explorateur, faites un clic droit sur le fichier ZIP, puis choisissez
   **Extraire tout**.
5. Choisissez comme destination un nouveau dossier nommé
   `Documents\Python_IUT\logiciels\thonny`.
6. Ouvrez ce dossier et lancez **`thonny.exe`**.

La version portable ne nécessite pas d'installation classique. Téléchargez-la
uniquement depuis le site officiel. Au premier démarrage, conservez
l'interpréteur Python proposé par défaut. Si Windows demande une autorisation
réseau, elle n'est pas nécessaire pour exécuter les exercices locaux.

### Contrôle rapide dans Thonny

La fenêtre doit contenir :

- une grande zone blanche pour écrire le programme ;
- une zone **Shell** en bas avec une invite `>>>` ;
- un bouton vert **Exécuter** dans la barre d'outils.

Dans le Shell de Thonny, essayez :

```python
print("Thonny fonctionne")
```

---

## 5. Créer le premier fichier Python

1. Dans Thonny, choisissez **Fichier > Nouveau**.
2. Choisissez **Fichier > Enregistrer sous**.
3. Ouvrez `Documents\Python_IUT\seance0`.
4. Enregistrez le fichier sous le nom **`premier_programme.py`**.
5. Recopiez le programme suivant :

```python
nom = input("Quel est votre prénom ? ")

tension = 5.0
courant = 0.2
puissance = tension * courant

print(f"Bonjour {nom} !")
print(f"La puissance calculée est {puissance} W.")
```

Enregistrez avec **Ctrl + S**. Vérifiez que le nom affiché par Thonny se termine
bien par `.py` et non par `.py.txt`.

---

## 6. Exécuter le fichier depuis la console Windows

Dans l'Explorateur, ouvrez le dossier `seance0`. Cliquez dans la barre
d'adresse, saisissez `powershell`, puis appuyez sur **Entrée**. Une console
s'ouvre directement dans le bon dossier.

Vérifiez que le fichier est présent :

```powershell
dir
```

Exécutez ensuite le programme :

```powershell
py premier_programme.py
```

Si vous aviez utilisé la commande `python --version` au début, utilisez plutôt :

```powershell
python premier_programme.py
```

Saisissez votre prénom lorsque le programme le demande. Vous devez obtenir un
message de bienvenue puis une puissance égale à `1.0 W`.

---

## 7. Exécuter le même fichier dans Thonny

1. Revenez dans Thonny et vérifiez que `premier_programme.py` est ouvert.
2. Cliquez sur le bouton vert **Exécuter** ou appuyez sur **F5**.
3. Cliquez dans le Shell en bas de la fenêtre et saisissez votre prénom.
4. Comparez le résultat avec celui obtenu dans la console Windows.

Le même fichier `.py` est exécuté dans les deux cas. Seul l'outil utilisé pour
le lancer change.

---

## 8. Validation de la séance

Avant de terminer, faites vérifier les points suivants :

- `py --version` ou `python --version` affiche une version de Python 3 ;
- Thonny portable démarre depuis `Python_IUT\logiciels\thonny` ;
- les dossiers `seance0` à `seance4` existent ;
- `premier_programme.py` est enregistré dans `seance0` ;
- le programme fonctionne depuis la console Windows ;
- le programme fonctionne avec le bouton **Exécuter** de Thonny.

### Petit défi si vous avez terminé

Modifiez le programme pour demander la tension et le courant à l'utilisateur.
Les valeurs saisies avec `input()` sont du texte : convertissez-les avec
`float()` avant de calculer la puissance.
