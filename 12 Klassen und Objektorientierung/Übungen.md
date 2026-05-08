

# X. Komplettes Kapitel (45 Minuten)
In dieser Übung erstellst du Klassen, die ich so, oder so ähnlich selbst erstellt habe und häufig nutze.
Da es für dich vermutlich noch etwas ungewohnt ist, etwas von diesem Umfang zu programmieren, führen dich die einzelnen Aufgabenpunkte dort durch.

Tipp:\
Denk an den Teil mit der Funktionalen Programmierung.
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
Beim erstellen der Instanz wird ein Dateipfad übergeben, der als Attribut gespeichert wird.
Es soll möglich sein, den Pfad als String, oder als `Path` zu übergeben.
2. Alle Überordner des übergebenen Dateipfads sollen automatisch erstellt werden.
3. Implementiere `__getitem__`, `__setitem__` und `__delitem__`.
In der Datei muss noch nicht gespeichert werden.
4. Implementiere `__str__`.
Diese Methode soll alle Werte als ein großer String zurückgeben, so als ob man ein Dictionary auf der Konsole ausgibt.
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
Anstatt json zum speichern zu nutzen, sollen es Varianten deiner Klasse geben, die als `toml` und `pickle` abspeichern können.

Nutze diese Bibliothek für `toml`: https://pypi.org/project/tomlkit/

Die lässt sich quasi genauso nutzen wie `json`:
`tomlkit.dumps` und `tomlkit.loads`

`pickle` genauso, aber achtung: `pickle.dumps` gibt keinen string, sondern bytes zurück.
Entsprechend erwartet `pickle.loads` auch bytes.

1. Implementiere `DictFileToml`.
2. Implementiere `DictFilePickle`.



