
# 1. Bedingungen (10 Minuten)

**Nutze in dieser Übung kein `if`.**

Erstelle 3 Zahlen-Variablen: x,y und z. Die Werte darfst du dir selbst aussuchen.

Schreibe Bedingungen, welche die folgenden Fälle prüfen und gib deren Ergebnis auf der Konsole aus. 

1. x ist größer als y.
2. x ist größer als y und kleiner als z.
3. x ist größer als y, oder x ist kleiner als y
4. x ist durch y teilbar


# Übung 2 (20 Minuten)
Tipp: Du kannst das Programm mit `exit()` vom Skript aus stoppen.\

Implementiere Folgendes:

Der Nutzer gibt eine Ganzzahl ein.

1. Falls es sich um eine negative Zahl handelt, soll `Bitte nur positive Zahlen eingaben` ausgegeben, und das Programm beendet werden.

2. Das Programm gibt alle Zahlen von 2 bis zur eingegebenen Zahl (exklusive) auf der Konsole aus.
Wird eine 0 oder 1 eingegeben, gibt das Programm nichts aus.\
Beispiel:
    ```
    >> 8
    2
    3
    4
    5
    6
    7
    ```

3. Zu jeder ausgegebenen Zahl gibt das Programm aus, ob die Eingabe durch diese Zahl teilbar ist.
Beispiel:
    ```
    >> 8
    2 True
    3 False
    4 True
    5 False
    6 False
    7 False
    ```

4. Falls es sich um eine Primzahl handelt, soll `Die Zahl ist eine Primzahl` ausgegeben werden.\
(Eine Primzahl ist ausschließlich durch 1 und sich selbst teilbar, also hinter jeder Ausgabe von 3. muss “Nein” stehen)

5. Das Skript soll so lange wiederholt werden, bis der Nutzer nichts eingibt, also einfach nur enter drückt.

6. Handelt es sich nicht um eine Primzahl, wird nachher die größte Zahl, durch welche geteilt werden kann ausgegeben.\
Beispiele:
`8 -> 4`
`52 -> 26`
`100 -> 50`
`17 -> Primzahl`







