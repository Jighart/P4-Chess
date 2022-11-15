# Projet 4: Chess Tournament
## Nécessite Python 3.10+

Ce programme gère les tournois d'échecs hebdomadaires et permet de générer des rapports.
Les différents menus permettent de :

- Créer un nouveau tournoi
- Reprendre un tournoi en cours
- Créer de nouveaux joueurs
- Editer les joueurs existants
- Générer des rapports sur les tournois ou les joueurs

# Installation:
Une fois Python installé, lancez la console, placez-vous dans le dossier de votre choix puis clonez ce repository :
```
git clone https://github.com/Jighart/P4-Chess.git
```
Placez vous dans le dossier P4-Chess, puis créez un nouvel environnement virtuel :
```
python -m venv env
```
Ensuite, activez-le.
Windows :
```
env\scripts\activate.bat
```
Mac/Linux :
```
source env/bin/activate
```
Il ne reste plus qu'à installer les packages requis :
```
pip install -r requirements.txt
```
Vous pouvez enfin lancer le programme et vous laisser guider :
```
python main.py
```

Vous trouverez également le rapport flake8 dans le dossier flake_report. A noter que pour l'instant, flake8-html [n'est
pas compatible avec flake8 5.0 ou plus](https://github.com/lordmauve/flake8-html/issues/30), j'ai donc utilisé
la version 4.0.1 ici.