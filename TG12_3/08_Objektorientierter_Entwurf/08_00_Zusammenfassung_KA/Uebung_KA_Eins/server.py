from flask import Flask, request, jsonify, send_from_directory
from pydantic import ValidationError
import json
from model import Auto
import os
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
URL = 'http://localhost:12345/message'


# CORS(app, origins = [
#    "http://127.0.0.1:5500",
#    "http://localhost:5500"
#])

CORS(app)

eingabe_liste = []

@app.route('/message', methods=['POST'])
def methode():
    data = request.json
    message = data.get('message', '')
    print(f"Empfangen: {message}")
    response_message = f"Echo: {message}"
    return jsonify({"Antwort lautet" : response_message})


data = {
    "Marke": "Audi",
    "Modell": "A4",
    "Farbe": "Schwarz",
    "PS": 300,
    "Verbrauch": 100
    }

response = requests.post(URL, json=data)

if ((response.status_code == 200) | (response.status_code == 201)):
    print("Statuscode: ", response.status_code)
    json.dumps(response.json())
else:
    json.dumps(response.json())
    print("Statuscode: Fehlgeschlagen")

server = "server.json"

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=12345)