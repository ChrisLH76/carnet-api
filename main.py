import sqlite3
from flask import Flask, request

app = Flask(__name__)

def ouvrir_base():
	return sqlite3.connect("notes.db")

def creer_table():
	connexion = ouvrir_base()
	connexion.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, texte TEXT NOT NULL)")
	connexion.commit()
	connexion.close()

creer_table()

@app.route("/")
def accueil():
	return "Bienvenue dans l'application carnet-api."

@app.route("/notes", methods=["POST"])
def ajouter_note():
	donnees = request.get_json()
	texte = donnees["texte"]
	connexion = ouvrir_base()
	connexion.execute("INSERT INTO notes (texte) VALUES (?)", (texte,))
	connexion.commit()
	connexion.close()
	return donnees
@app.route("/notes")
def lister_notes():
	connexion=ouvrir_base()
	lignes = connexion.execute("SELECT * FROM notes").fetchall()
	connexion.close()
	return lignes

@app.route("/notes/<int:id_note>", methods=["DELETE"])
def supprimer_note(id_note):
	connexion=ouvrir_base()
	connexion.execute("DELETE FROM notes WHERE id = ?", (id_note,))
	connexion.commit()
	connexion.close()
	return "Ok"