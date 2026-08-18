
# 1. Was ist "is" (5 Minuten)
Gegeben sei der folgende Codeausschnitt.
Die Ausgabe der Print-Statements steht jeweils als Kommentar dahinter.
```py
x = [1, 2]
y = x

print(x == y)   # True
print(x is y)   # True

x = [1, 2]
y = [1, 2]

print(x == y)   # True
print(x is y)   # False
```
Erkläre anhand des Codeausschnitts, was der Unterschied zwischen `==` und `is` ist.

Überlege dir danach, was in folgendem Codeausschnitt ausgegeben werden sollte.
Führe ihn danach zur Überprüfung aus.
```py
x = 5
y = 5

print(x == y)
print(x is y)

x += 1
print(x == y)
print(x is y)

x -= 1
print(x == y)
print(x is y)
```
Du musst dir das Verhalten nicht erklären können.
Nimm es nur als Beispiel für Python-Magie.

# 2. Dunder-Methoden (25 Minuten)
Erstelle die Klasse "Bruch".
Diese Klasse soll einen mathematischen Bruch darstellen, erhält bei der Übergabe also Zähler und Nenner (beide `int`).
Wird kein Nenner übergeben, soll dieser als `1` angenommen werden.

Alle nötigen Formeln zu den Grundrechenarten: https://www.matheretter.de/wiki/bruche-formeln

Nutze bei Bedarf gerne diese Funktion:
```py
def ggt(a: int, b: int) -> int:
    """Gibt den größten gemeinsamen Teiler der übergebenen Zahlen zurück (Euklidischer Algorithmus)"""
    if not b:
        return a
    
    if b > a:
        return ggt(b, a)

    return ggt(b, a % b)
```

1. Brüche sollen sinnvoll auf die Konsole ausgegeben werden können: `print(mein_bruch)`
2. Beim Erstellen eines Bruchs soll dieser so weit wie möglich gekürzt werden. Das hilft dir bei folgenden Teilaufgaben, also behalte es im Hinterkopf.
3. Es soll möglich sein, Brüche in `int` und `float` umzuwandeln: `float(mein_bruch)`
4. Brüche sollen miteinander addiert, subtrahiert, multipliziert und dividiert werden können.
5. Zähler und Nenner sollen auslesbar, aber nicht beschreibbar sein:\
`print(mein_bruch.zahler)` ist ok, aber `mein_bruch.zahler = 5` wirft einen `AttributeError`.
6. Erstellt man einen Bruch, indem man dem Zähler einen Bruch übergibt, wird dieser Bruch kopiert und zurückgegeben (Nenner muss bei der Übergabe leer sein!):\
`print(Bruch(mein_bruch))` gibt das gleiche aus wie `print(mein_bruch)`.
7. Die in `4.` erstellten Operationen sollen auch mit `int` direkt funktionieren, solange die Zahl hinter dem Bruch steht:
`mein_bruch + 5`, `mein_bruch * 3`.
8. Steht die Zahl vor dem Bruch, wird der Bruch als `float` interpretiert:
`15 + mein_bruch` könnte z.B. `17.6` ergeben.
9. (Knobelaufgabe) Erstelle die Funktion `float_to_bruch(x: float) -> Bruch`.
Diese wandelt eine Zahl in einen Bruch um.
Nutze `x = round(x, 10)`, um die Zahl x auf 10 Nachkommastellen zu runden.
Diese Genauigkeit ist ausreichend.

# X. Praxisbeispiel (45 Minuten)
In dieser Übung erstellst du Klassen, die ich so ähnlich selbst erstellt habe und häufig nutze.
Da es für dich vermutlich noch etwas ungewohnt ist, etwas von diesem Umfang zu programmieren, führen dich die einzelnen Aufgabenpunkte dort durch.

Tipp:\
Denk an die Code-Direktiven (Aktion, Kalkulation, etc.).
Erstelle Funktionen/Methoden so, dass sie abstrakt nutzbar sind.

Ziel ist es, eine Dictionary zu erstellen, was seine Daten automatisch in einer Datei speichert:
```py
my_file = DictFile("werte.json")

my_file["Hallo"] = "Welt"   # In Datei gespeichert
```
```py
my_file = DictFile("werte.json")

print(my_file["Hallo"])   # Aus Datei gelesen
```

## Teil 1. Klassen allgemein (35 Minuten):
Folge diesem Ablauf:
1. Erstelle die Klasse `DictFile`.
Beim Erstellen der Instanz wird ein Dateipfad übergeben, der als Attribut gespeichert wird.
Es soll möglich sein, den Pfad als String, oder als `Path` zu übergeben.
2. Alle Überordner des übergebenen Dateipfads sollen automatisch erstellt werden.
3. Implementiere `__getitem__`, `__setitem__` und `__delitem__`.
In der Datei muss noch nicht gespeichert werden.
4. Implementiere `__str__`.
Diese Methode soll alle Werte als einen großen String zurückgeben, so als ob man ein Dictionary auf der Konsole ausgibt.
Das hilft dir im Folgenden ungemein beim Testen.
5. Implementiere die STATISCHE Methode `_save(save_to: Path, data: dict) -> None`. 
Diese speichert das übergebene Dictionary unter dem angegebenen Pfad.
Nutze um die Daten speichern zu können das `json`-Modul.
6. Implementiere die STATISCHE Methode `_load(load_from: Path) -> dict`.
Die macht genau das Gegenteil von `_save` und gibt das geladene `dict` zurück.
7. Implementiere `save()`.
Die Methode speichert die aktuellen Werte in dem zu Beginn übergebenen Dateipfad.
Was also mit `__setitem__` übergeben wurde soll in der Datei gespeichert werden.
8. Implementiere `load()`.
Die Methode läd die Werte aus dem zu Beginn übergebenen Dateipfad und übernimmt sie, sodass man sie mit `__getitem__` abrufen kann.
Falls die Datei nicht existiert, soll die Methode gar nichts machen.
9. Beim erstellen einer Instanz sollen die Werte aus der Datei geladen werden, falls vorhanden.
10. Implementiere die Methode `backup(backup_to: str | Path)`.
Diese speichert die aktuellen Werte in einer separaten Datei.
11.  Implementiere die Methode `load_backup(backup_from: str | Path)`.
Diese läd im Backup gespeicherte Werte, so wie es `load()` tut.

## Teil 2. Vererbung (10 Minuten)
Anstatt als json abzuspeichern, sollen es Varianten deiner Klasse geben, die als `toml` und `pickle` abspeichern können.

Nutze diese Bibliothek für `toml`: https://pypi.org/project/tomlkit/

Die lässt sich quasi genauso nutzen wie `json`:
`tomlkit.dumps` und `tomlkit.loads`

`pickle` genauso, aber achtung: `pickle.dumps` gibt keinen string, sondern bytes zurück.
Entsprechend erwartet `pickle.loads` auch bytes.

1. Implementiere die Klasse `DictFileToml`.
2. Implementiere die Klasse `DictFilePickle`.



