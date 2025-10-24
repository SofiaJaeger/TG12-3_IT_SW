# Zu Datei f_Client_und_Server.ipynb
import requests
import json

URL = 'http://127.0.0.1:12345/spieler'



spieler = {
    "name": str(input("Name des Spielers: ")),
    "jahrgang": int(input("Jahrgang des Spielers: ")),
    "staerke": int(input("Stärke des Spielers (1-10): ")),
    "torschuss": int(input("Torschuss des Spielers (1-10): ")),
    "motivation": int(input("Motivation des Spielers (1-10): "))
}

response = requests.post(URL, json=spieler)
print("Status Code:", response.status_code)

if response.status_code == 200 or response.status_code == 201:
    print("Spieler erfolgreich erstellt.")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print("Fehler beim Erstellen des Spielers.")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))

#print("Antwort vom Server:", response.json())