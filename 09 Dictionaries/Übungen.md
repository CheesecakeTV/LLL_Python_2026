
# 1. Dictionary (10 Minuten)
1. Erstelle die Funktion `printDict(dasDict: dict)`.
Diese gibt den Inhalt von `dasDict` zeilenweise auf der Konsole aus.\
Beispiel:
```py
printDict({"Hallo": "Zusammen", "Python": "Kurs"})

# Erstellt folgende Ausgabe:
# Hallo - Zusammen
# Python - Kurs
```
2. Erstelle die Funktion `replace`.
Die Funktion erhält ein Dict und gibt ein neues Dict zurück.
Außerdem ist es möglich, optionale Argumente zu übergeben, die ins neue Dict geschrieben werden.\
Wichtig: Das übergebene Dict wird nicht verändert.\
Beispiel:
```py
dasDict = {"Hallo": "Zusammen", "Python": "Kurs"}
dasNeueDict = replace(
    dasDict,
    Hallo="Welt",
    NeuerKey="Mir fällt nichts ein",
)

print(dasDict)  # {"Hallo": "Zusammen", "Python": "Kurs"}
print(dasNeueDict)  # {"Hallo": "Welt", "Python": "Kurs", "NeuerKey": "Mir fällt nichts ein"}
```

# 2. Dataclasses (15 Minuten)
Beginne mit folgendem Codeausschnitt:
```py
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Person:
    vorname: str
    nachname: str
    alter: int = 0
```

1. Erstelle die Liste `alle_personen`.
Füge der Liste folgende fiktive Personen hinzu:
```
Taylor Chavez, 53
Linda Shannon, 25
Dennis Johnson, 22
Sarah Graves, 13
Jasmine Turner, 16
```

2. Erstelle die Funktion `get_erwachsen(personen_liste)` (Kalkulation!).
Diese erhält eine Liste von Personen und gibt eine Liste aus allen davon volljährigen Personen zurück.
Füge auch möglichst konkrete Typehints hinzu.

3. Füge der Klasse `Person` das Attribut `eltern` hinzu.
Sind die Eltern bekannt, erhält es ein Tupel mit beiden Eltern-Personen.
Normalerweise enthält es `(None, None)`.
Vergiss die Typehints nicht.

4. Erstelle die Funktion `erstelle_kind(kind_informationen: Person, elternteil1, elternteil2)` (Kalkulation!).
Diese gibt eine Person zurück, dessen Eltern die übergebenen Elternteile sind.
Das Alter des Kindes ist `0`, Vor- und Nachname können `kind_informationen` entnommen werden.
Wie immer, füge fehlende Typehints hinzu.



