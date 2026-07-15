
# 1. Grundlegende Nutzung von Dateien Teil 1 (10 Minuten)
Die Datei `Werte.txt` (Im Ordner für Materialien) enthält einige Zahlen.

Bestimme den Durchschnitt aller Zahlen, indem du diese aufaddierst und durch die Anzahl der Zahlen teilst.

Veränderd dabei nicht die Datei.

# 2. Verschiedenes (15 Minuten)
Lade dir aus den Materialien `Ordner.zip` herunter.
Die Zip-Datei enthält einen Ordner mit vielen kleinen Dateien.

Die Dateinamen bestehen aus einer Zufallszahl, dem Wort `Datei` und dem "index" der Datei.
Eigentlich sollte aber der index vorne stehen und die Zufallszahl hinten.

Falsch ist also `105663 Datei 001.txt`, korrekt wäre `001 Datei 105663.txt`.

Korrigiere den Fehler für alle Dateien.

# 3. Sinnvolles Auslesen von Daten (25 Minuten)
Irgendein Programm hat `Data.json` generiert, was du im GibHub unter Materialien findest.

Ich gebe bei dieser Übung keinen wirklichen Ablauf vor, sondern nur das Ergebnis.
Du darfst die Übung lösen wie du willst, was natürlich cool ist, aber auch gefährlich.
Überlege dir auf jeden Fall vorher grob, wie du `2.` und `3.` lösen willst.

1. Erstelle den Datentypen `Person`, welcher zu den Daten passt.
2. Erstelle die Funktion `lese_data_json`, welche diese Art von Datei ausliest.
Zurückgegeben wird ein Dict, welches den jeweiligen Namen als Key hat und `Person`-Objekte als Values.
3. Erstelle die Funktion `schreibe_data_json`, welche genau das Gegenteil macht.
Sie bekommt also ein Objekt, wie es von `lese_data_json` erstellt wurde und schreibt es in eine Datei, die vom Aufbau her `Data.json` entspricht.

# X. Grundlegende Nutzung von Dateien Teil 2 (10 Minuten)
Lade dir die Datei `Namenliste.txt` herunter.

Beantworte folgende Fragen darüber, OHNE DIE DATEI VON HAND AUSZULESEN (Also nur in deinem Python-Skript arbeiten).
"Vorname" bedeutet einfach, das erste Wort des vollen Namens.
Machs nicht zu kompliziert bitte.
1. Wie ist die Datei aufgebaut? Was enthält sie?
2. Welche Vornamen beginnen mit dem Buchstaben `X`?
3. Wie viele Vornamen beginnen mit `A`?

Danach:

4. Sortiere die Liste alphabetisch (nach den Vornamen) und speichere sie als `NamenlisteSortiert.txt` in der gleichen Form ab.