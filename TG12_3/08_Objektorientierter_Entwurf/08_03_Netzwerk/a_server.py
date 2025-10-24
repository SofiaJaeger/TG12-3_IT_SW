# Zu Datei a_Netzwerke_Einfuehrung.ipynb

from flask import Flask, request, jsonify
from pydantic import ValidationError
import json
from e_model import Spieler
import os

app = Flask(__name__)

geladene_spieler = []  # Liste zum Speichern der Spieler

# Route für die Hauptseite
@app.route('/')
def home():
    Anzeige() # Aufgabe
    return "Server ist bereit und wartet auf Anfragen."

# Route für mein Profil
@app.route('/profil')
def impressum():
    return "<html><body><h1>Impressum</h1><p>Name: ....</p><p>Wohnort: ...</p><p>E-Mail: ...</p></body></html>"

# Route zum Empfangen von Nachrichten
@app.route('/message', methods=['POST'])
def handle_message():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")
    response_message = f"Echo: {message}"
    Anzeige() # Aufgabe
    return jsonify({"response": response_message})

@app.route('/spieler', methods=['POST'])
def handle_spieler():
    """Erstellt einen Spieler aus Json Dateien und prüft das mit Pydantic."""


    try:
        data = request.get_json()
        spieler = Spieler(**data)
        geladene_spieler.append(spieler)

        with open("spieler.json", "w", encoding="utf-8") as f:
            json.dump([s.model_dump() for s in geladene_spieler], f, ensure_ascii=False, indent=4)
        print("✅ Spieler wurden in 'spieler.json' gespeichert.")


        with open("spieler.json", "r", encoding="utf-8") as f:
            print(f.read())


        return jsonify({
            "status": "ok",
            "message": "Spieler erfolgreich erstellt",
            "spieler": spieler.model_dump()
        }), 201
    except ValidationError as e:
        return jsonify({
            "status": "error",
            "message": "Validierung fehlgeschlagen",
            "details": e.errors()
        }), 400

dateiname = "spieler.json"

if os.path.exists(dateiname):
    with open(dateiname, "r", encoding="utf-8") as f:
        daten = json.load(f)
    geladene_spieler = [Spieler(**s) for s in daten]
    print("📂 Geladene Spieler:")
    for s in geladene_spieler:
        print(s)
else:
    print(f"⚠️ Datei '{dateiname}' wurde nicht gefunden.")
    print("Es wird eine leere Spielerliste erstellt.")
    geladene_spieler = []

# Aufgabe Start
def Anzeige():
    print(f"Method: {request.method}")
    print(f"Args: {request.args}")
    print(f"Form: {request.form}")
    #print(f"Json: {request.json}")
    print(f"Data: {request.data}")
    print(f"Headers: {request.headers}")
    print(f"Cookies: {request.cookies}")
    print(f"Path: {request.path}")
    print(f"Url: {request.url}")
    print(f"Remote_addr: {request.remote_addr}")
# Aufgabe Ende


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)  # Server starten

# Die Funktion muss for if __name__ stehen, weil es eine Endlosschreife ist, die den Server am Laufen hält.
# Alles daruntersetehende wird nicht ausgeführt.

#----------------------------------
# Aufgabe c_Flask.ipynb
# Erweitere die Methoden `home` und `handle_message` im Modul `server.py
# Gebe alle Attributwerte auf der Konsole aus. Schreibe die Ausgabe nur einmal und nutze dies in beiden Methoden.
# Alle Zeilen zu der Aufgabe sind mit # Aufgabe gekennzeichnet.