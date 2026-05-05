
# X. Funktionale Programmierung (5 Minuten)
Entscheide (und begründe) für den folgenden Code, welche der Funktionen Kalkulationen und welche Aktionen sind:
```py
import datetime

_nutzername = "Eric"
_passwort = "Passwort"
_alter = 25

def getEingabe(text: str) -> str:
    return input(text).strip()

def gibAus(text: str) -> None:
    print(text)

def login(passwort: str = _passwort) -> bool:
    return getEingabe("Bitte Passwort eingeben ") == passwort

def vermuteGeburtsjahr(alter: int = _alter) -> int:
    return datetime.datetime.now().year - alter

def istNutzerGeborenVor(jahr: int) -> bool:
    return vermuteGeburtsjahr(_alter) < jahr
```

# X. Vor falscher Übergabe schützen (10 Minuten)
Halte dich nicht zu lange mit einzelnen Teilen dieser Übung auf.

Kopiere folgende Funktion:
```py
def istTeilbar(zahl: int, durch: int) -> bool:
    """
    Gibt zurück, ob 'zahl' durch 'durch' teilbar ist.
    """
    return not zahl % durch
```

Implementiere Folgendes, indem du die Funktion veränderst.
Teste alles Neue, indem du die Funktion entsprechend nutzt.
1. Ist mindestens ein Argument nicht vom Typ `int`, wird ein Fehler ausgelöst.
2. Ist `durch` gleich `0`, wird `None` zurückgegeben. Tipp: Passe auch die Typehints entsprechend an.
3. Ist mindestens ein Argument kleiner als `0`, wird `None` zurückgegeben.
4. Ist `durch` größer als `zahl`, wird `None` zurückgegeben.
5. Wird `durch` nicht übergeben, wird es als `2` definiert.


