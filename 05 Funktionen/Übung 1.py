from typing import Any

def pi() -> float:
    return 3.14159265359

def durchschnitt(a: float, b: float) -> float:
    return (a + b) / 2

def passwortabfrage(passwort: str) -> bool:
    return input("Bitte Passwort eingeben: ") == passwort

def umwandeln(wert: Any, zu_type: type) -> Any:
    return zu_type(wert)


