import datetime

_nutzername = "Eric"
_passwort = "Passwort"
_alter = 25

# Alle Funktionen sind zu Beginn Aktionen

# A
def getEingabe(text: str) -> str:
    return input(text).strip()

# A
def gibAus(text: str) -> None:
    print(text)

# A
def gibNutzernamenAus(nutzername = _nutzername) -> None:
    print(nutzername)

# A
def login(passwort: str = _passwort) -> bool:
    return getEingabe("Bitte Passwort eingeben ") == passwort

# K
def vermuteGeburtsjahr(alter: int = _alter, jahrImMoment: int = datetime.datetime.now().year) -> int:
    return jahrImMoment - alter

# K
def istNutzerGeborenVor(
        jahr: int,
        alter = _alter,
        jahrImMoment: int = datetime.datetime.now().year,
) -> bool:
    return vermuteGeburtsjahr(alter, jahrImMoment) < jahr



