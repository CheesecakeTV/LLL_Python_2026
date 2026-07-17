
# 1. Schleifen (10 Minuten)
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
3. Gibt der Nutzer eine negative Zahl ein, wird die Eingabe nicht beachtet und übersprungen.
4. Gibt der Nutzer nichts ein, endet die Schleife. Das Programm gibt "Ende" aus.
5. Nachdem die Schleife endet, werden alle Eingaben des Nutzers der Reihe nach auf der Konsole ausgegeben (jede Eingabe ein `print`).
6. Vor jeder Eingabe soll (bei der Ausgabe nach der Schleife von Teil 5.) stehen, an welcher Stelle diese Zahl eingegeben wurde:
```
1 6
2 3
3 15
4 9
5 12
usw...
```

# 2. Funktionen (20 Minuten)
In dieser Übung schreibst du ein Programm, was beim Wichteln helfen soll.
Ziel ist es, dass jeder Person ein zufälliger Wichtel zugeordnet wird.

Starte mit folgendem Code:
```py
import random

namen = ["Anna", "Ben", "Carla", "Hans", "Martin", "Mira"]
partner = random.sample(namen, len(namen))
```

1. Untersuche, was `partner` enthält und welchen Typen es hat. Tipp: Führe das selbe Skript mehrfach aus.
2. Gib ordentlich aus, welcher Partner wem zugeteilt wurde:
```
Anna - Hans
Ben - Martin
Carla - Mira
Hans - Carla
Martin - Anna
Mira - Ben
```
3. Erstelle die Funktion `getPartnerListe(namenListe: list[str]) -> list[str]`.
Diese erstellt eine partner-Liste, passend zur übergebenen Liste.
Nutze diese Funktion, um die Liste `partner` zu erstellen (also vorhandenen Code verändern).\
Wichtig: `getPartnerListe` ist eine reine Kalkulation.

4. Erstelle die Funktion `printPartner(namenListe: list[str], partnerListe: list[str])`.
Diese gibt beide Listen so aus (print), wie in Teil `2.` beschrieben.
Verändere den Code aus `2.` so, dass diese Funktion stattdessen genutzt wird.

5. Bei dieser Art der Zuteilung fällt dir ein Problem auf:
Es ist möglich, dass eine Person sich selbst zugeteilt wird.
Löse, oder umgehe das Problem.\
Du darfst dabei zusätzliche Funktionen schreiben und bestehenden Code verändern, so viel wie du willst.\
Tipp: Um ein einzelnes, zufälliges Element aus einer Liste zu wählen, nutze `random.choice(dieListe)`.\
Zu diesem Teil fallen mir nach kurzer Überlegung 3 vernünftige Lösungen ein.
Eine davon ist super einfach zu implementieren, aber schwierig zu finden.



