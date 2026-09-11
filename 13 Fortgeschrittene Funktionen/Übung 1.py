from typing import Generator, Any, Iterable

def blinker() -> Generator[bool, None, None]:
    while True:
        yield True
        yield False

def count(initial: int = 0, amount: int = 1) -> Generator[int, None, None]:
    counter = initial
    while True:
        yield counter
        counter += amount

def fib() -> Generator[int, None, None]:
    yield 0
    yield 1
    vorletzter, letzter = 0, 1

    while True:
        aktuell = vorletzter + letzter  # Das funktioniert auch mit 2 Variablen, aber hier hab ich mich für die besser lesbare Variante entschieden
        vorletzter = letzter
        letzter = aktuell

        yield aktuell

def geradeZahlen() -> Generator[int, None, None]:
    return count(0, 2)  # Alternativ yield from

def zahlenfolge() -> Generator[int, None, None]:
    for i in count(2):
        yield from range(i)

def begrenzen(mein_iterable: Iterable[Any], max_val: int) -> Generator[Any, None, None]:
    for i in mein_iterable:
        if i > max_val:
            return
        # else
        yield i

def _ist_prim(zahl: int) -> bool:
    """
    Hilfsfunktion. Gibt zurück, ob die übergebene Zahl eine Primzahl ist.
    Lässt sich deutlich effizienter schreiben, aber das überlasse ich euch...
    """
    zahl = abs(zahl)

    if zahl in (0, 1):
        return False

    if zahl == 2:
        return True

    if zahl % 2 == 0:
        return False

    for i in begrenzen(count(3, 2), zahl - 1):
        if zahl % i == 0:
            return False

    return True

def primzahlen() -> Generator[int, None, None]:
    for i in count(2):
        if _ist_prim(i):
            yield i


# Berechne testweise mal alle Primzahlen bis 100
for i in begrenzen(primzahlen(), 100):
    print(i)


