import datetime as dt
from pydantic import BaseModel, Field, field_validator, ValidationError

class Spieler(BaseModel):

    # Eingabefelder mit Pydantic-Validierung
    name: str = Field(default="x", min_length=1)
    jahrgang: int = Field(default=16.0)
    #jahrgang: int = Field(default=16.0, ge=2009, le=1990)
    staerke: int = Field(default=0, gt=0, le=10)
    torschuss: int = Field(default=0, gt=0, le=10)
    motivation: int = Field(default=0, gt=0, le=10)

    # alternativ: Individuelle Prüfung nur für 'jahrgang'
    @field_validator("jahrgang")
    def check_jahrgang(cls, jahrgang):
        aktuelles_datum = dt.date.today()
        aktuelles_jahr = aktuelles_datum.strftime("%Y")
        alter = aktuelles_jahr - jahrgang
        if (alter < 16) | (alter > 35):
            raise ValueError("Das Alter muss zwischen 16 und 35 Jahren sein!")
        cls.jahrgang_mit_zusicherung = jahrgang

    # Aktiviert Live-Validierung bei späteren Änderungen
    model_config = {"validate_assignment": True}



# Objekt erzeugen (gültige Werte)
s = Spieler(name="Tom", jahrgang=2000, torschuss=5)
print("1️⃣ Neuer Spieler:", s.model_dump())

# Änderung eines gültigen Wertes
s.torschuss = 6
s.motivation = 5
print("2️⃣ Nach Änderung:", s.model_dump())

# Ungültiger Wert für Torschuss
try:
    s.torschuss = -50
    print(s.model_dump())
except ValueError as e:
    print("Fehler:", e)

# Ungültiger Wert für Name
try:
    s.name = ""
    print(s.model_dump())
except ValueError as e:
    print("Fehler:", e)

# Fehler schon beim Erstellen (beide Werte falsch)
try:
    s = Spieler(name="", jahrgang=-2000, torschuss=15)
except ValidationError as e:
    print("Fehler beim Erstellen des Objekts:")
    print(e)