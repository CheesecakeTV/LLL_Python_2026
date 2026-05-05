
# 1. While (10 Minuten)
1. Der Nutzer wird endlos dazu aufgefordert, eine Zahl einzugeben. Also nach einer Eingabe wird eine weitere Eingabe verlangt.
2. Nach jeder Eingabe gibt das Programm die Summe aller bisherigen Zahlen aus:
```
>> 5
5
>> 7
12
>> 3
15
```
3. Gibt der Nutzer eine negative Zahl ein, wird die Eingabe nicht beachtet und übersprungen. Es wird nichts ausgegeben.
4. Gibt der Nutzer nichts ein, endet die Schleife. Das Programm gibt "Ende" aus.
5. Nachdem die Schleife endet, sollen alle Eingaben des Nutzers der Reihe nach auf der Konsole ausgegeben werden.
6. Vor jeder Eingabe soll stehen, an welcher Stelle diese Zahl eingegeben wurde:
```
1 6
2 3
3 15
4 9
5 12
usw...
```

# 2. For (10 Minuten)
In dieser Übung schreibst du ein Programm, was beim Wichteln helfen soll.
Ziel ist es, dass jeder Person nachher ein zufälliger Wichtel zugeordnet wird.

Starte mit folgendem Code:
```py
import random

namen = ["Anna", "Ben", "Carla", "Hans", "Martin", "Mira"]
partner = random.sample(namen, len(namen))
```

1. Untersuche, was `partner` enthält und welchen Typen es hat. Tipp: Führe das Skript mehrfach aus.

2. Gib ordentlich aus, welcher Partner wem zugeteilt wurde:
```
Anna - Hans
Ben - Martin
Carla - Mira
```

3. Wandle dein Skript in zwei Funktionen um: `getPartner` und `printPartner`.\
`getPartner` erstellt zu einer übergebenen Liste die partner-Liste.\
`printPartner` erstellt aus zwei übergebenen Listen die ordentliche Ausgabe.\
Überlege dir jeweils gut, welche Parameter/Rückgaben die Funktionen haben.
Denk auch an die Typehints.

4. Bei dieser Art der Zuteilung fällt dir vermutlich ein Problem auf:
Es ist möglich, dass eine Person sich selbst zieht.
Löse, oder umgehe das Problem.



