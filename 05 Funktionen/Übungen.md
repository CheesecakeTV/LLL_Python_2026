
# 1. Grundlegende Funktionen (10 Minuten)
Die Teilaufgaben sind unabhängig voneinander lösbar.\
Implementiere folgende Funktionen.
VERSEHE DABEI JEDE FUNKTION VOLLSTÄNDIG MIT TYPEHINTS!!! 

1. `pi()`: Gibt `3.14159265359` zurück 
2. `durchschnitt(a, b)`: Gibt den durchschnitt der Zahlen a und b zurück.
3. `passwortabfrage(passwort)`: Fordert den Nutzer dazu auf, ein Passwort auf der Konsole einzugeben (ein Versuch). Die Funktion gibt zurück, ob das Passwort korrekt (wie das übergebene Passwort) eingegeben wurde.
4. `umwandeln(wert, zu_type)`: Wandelt `wert` in den übergebenen Typen um. Beispiel: `umwandeln(15, float)` entspricht `float(15)` und gibt `15.0` zurück.

# 2. Funktionale Programmierung (10 Minuten)
Entscheide (und begründe) für den folgenden Code, welche der Funktionen Kalkulationen und welche Aktionen sind.
Überlege für die Aktionen, ob/wie sich die jeweilige Funktion in eine Kalkulation umwandeln lässt.
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


