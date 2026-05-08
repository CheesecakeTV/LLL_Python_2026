
# 1. Grundlegendes arbeiten mit Listen (10 Minuten)
Folgendes sei deine Einkaufsliste:
```py
einkaufsliste = ["Apfel", "Brot", "Milch"]
```
Jeder Übungsteil ERWEITERT das Skript nur.
Vorherige Zeilen sollen nicht mehr verändert werden.

1. Füge "Banane" und "Käse" hinzu.
2. Sortiere die Liste alphabetisch
3. Falls "Gurken" noch nicht in der Liste ist (im Code prüfen!), füge es hinzu.
4. Gib aus, wie lang die Liste ist
5. Dein Partner wünscht sich auch noch Dinge, die du in dein Skript kopierst:
```py
wuensche = ["Pfirsich", "Ananas", "Schokolade"]
```
Füge die Wünsche deiner Liste hinzu.
6. Lösche das letzte Element deiner Liste.
7. Gib die komplette Liste aus.


# 2. Mutable (Veränderbare) Objekte (20 Minuten)
Sie dir den jeweiligen Codeausschnitt an und ermittle, was dabei auf der Konsole ausgegeben wird.

**ERST DANACH**, führe den jeweiligen Ausschnitt aus, um deine Antwort zu überprüfen.
Finde eine Begründung, warum diese Ausgabe entsteht.

1. 
```py
x = [1]
y = x
y.append(2)

print(x)
```

2.
```py
x = [1]
y = x
y = [2]

print(x)
print(y)
```

3. 
```py
def foo(dieListe: list):
    dieListe.append(2)
    print(dieListe)

x = [1]
foo(x)
print(x)
```

4. (Ein wirklich sehr, sehr häufiger Anfängerfehler)
```py
def foo(dieListe: list):
    dieListe.append(2)
    print(dieListe)

x = [1]
x = foo(x)
print(x)
```

5. 
```py
def foo(dieListe: list = [1]):
    dieListe.append(2)
    print(dieListe)

foo()
foo()
foo()
```

6.
```py
x = [[1]] * 5
print(x)

x[0][0] = 2 # Verändere das 0. Element der 0. Liste
print(x)
```

7. (Knobelaufgabe)
```py
x = [[1]] * 5
print(x)

y = x.copy()

y[0][0] = 2 # Hier wird y verändert!
print(x)
```



