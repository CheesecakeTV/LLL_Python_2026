# Erstelle die Funktion int_input() -> int.
# Diese fordert den Nutzer auf, eine Eingabe zu tätigen (input).
# Bei einer erfolgreichen Eingabe wird diese in int umgewandelt und zurückgegeben.
# Ansonsten wiederholt sich die Aufforderung.
from typing import Any


# Erstelle die Funktion type_input(derTyp: type).
# Sie funktioniert genau wie int_input, erwartet aber eine Eingabe, die zum übergebenen Typen passt.

# Schreibe int_input so um, dass durch den vorherigen Übungsteil kein kopierter Code enthalten ist.

def int_input() -> int:
    return type_input(int)

def type_input(derTyp: type) -> Any:
    while True:
        ganzzahl = input(f"Gib eine {derTyp.__name__} ein: ")
        try:
            return derTyp(ganzzahl)
        except ValueError:
            print(f"Das war keine {derTyp.__name__}!")

print(type_input(float))






