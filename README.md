# CARNET-API

Ce projet est un carnet de notes, modifiable et interrogeable via des requêtes HTTP, développé avec Flask pour le (côté routage) et SQLite pour la gestion de la base de données.

## Installation

création de l'environnement virtuel

```
python3 -m venv .venv
```
activation de l'environnement
```
source .venv/bin/activate
```
installation des dépendances
```
python -m pip install -r requirements.txt
```
Pour information cette API a été testée avec Python 3.15.2
## Lancement

```
python -m flask --debug --app main run
```
- Copiez l'adresse HTTP fournie après Running on...
- Collez-la dans la barre d'URL de votre navigateur.

## Utilisation

Ajoute une note au carnet
```
curl -X POST -H "Content-Type: application/json" -d '{"texte": "acheter du pain"}' http://127.0.0.1:5000/notes
```
Efface une note selon son id dans la base (1 ici dans l'exemple)
```
curl -X DELETE  http://127.0.0.1:5000/notes/1
```
Consulte la liste des notes
```
curl http://127.0.0.1:5000/notes
```