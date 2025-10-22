# Zu Datei f_Client_und_Server.ipynb
import requests

name = str(input("Name des Spielers: "))
jahrgang = int(input("Jahrgang des Spielers: "))
staerke = int(input("Stärke des Spielers (1-10): "))
torschuss = int(input("Torschuss des Spielers (1-10): "))
motivation = int(input("Motivation des Spielers (1-10): "))

spieler = {
    "name": name,
    "jahrgang": jahrgang,
    "staerke": staerke,
    "torschuss": torschuss,
    "motivation": motivation
}

response = requests.post('http://localhost:12345/spieler', json=spieler)

print("Antwort vom Server:", response.json())