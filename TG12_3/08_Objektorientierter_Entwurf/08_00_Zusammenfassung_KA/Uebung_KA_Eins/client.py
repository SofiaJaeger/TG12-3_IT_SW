import requests

server_url = 'http://localhost:12345/message'




while True:
    message = input("Gebe hier die Daten ein")                  # Richtig

    response = requests.post(server_url, json={"message" : message})        

    if (response.status_code == 200) | (response.status_code == 201):
        data = response.json()
        print(data['Antwort lautet'])
    else:
        print("Fehler", response.status_code)


data = {
    "Marke": "Audi",
    "Modell": "A4",
    "Farbe": "Schwarz",
    "PS": 300,
    "Verbrauch": 100
    }

response = requests.post(server_url, json=data)

if ((response.status_code == 200) | (response.status_code == 201)):
    print("Statuscode:", response, status_code)
    json.dumps(response.json(response.json, indent = 2))
else:
    json.dumps(response.json())
    print("Statuscode: Fehlgeschlagen")