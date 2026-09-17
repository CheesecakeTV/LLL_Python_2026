from functools import wraps
from typing import Callable, Any


def neutral(fkt):

    @wraps(fkt)
    def inner(*args, **kwargs):
        return fkt(*args, **kwargs)

    return inner

def a1(fkt):

    @wraps(fkt)
    def inner(*args, **kwargs):
        print(f"Funktion {fkt.__name__} aufgerufen")
        return fkt(*args, **kwargs)

    return inner

def a2(fkt):
    counter = 0

    @wraps(fkt)
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1

        print(f"Funktion {fkt.__name__} wurde {counter} mal aufgerufen!")

        return fkt(*args, **kwargs)

    return inner

def a3(fkt):

    @wraps(fkt)
    def inner(*args, **kwargs):
        pass

    return inner

def a4(fkt):
    zwischenspeicher = None

    @wraps(fkt)
    def inner(*args, **kwargs):
        nonlocal zwischenspeicher

        speicher2 = zwischenspeicher
        zwischenspeicher = fkt(*args, **kwargs)
        return speicher2

    return inner

alle_funktionen: list[Callable] = []
def a5(fkt):
    alle_funktionen.append(fkt)
    return fkt

def a6(art_des_fehlers: type, default: Any = None):
    def decorator(fkt):

        @wraps(fkt)
        def inner(*args, **kwargs):
            try:
                return fkt(*args, **kwargs)
            except art_des_fehlers:
                return default

        return inner

    return decorator

@a6(TypeError, default="Typerror")
@a6(ZeroDivisionError, default=1)
def test(hallo):
    return None + "5"

@a5
def test2(hallo):
    print(hallo)

print(alle_funktionen)

print(test("Hallo"))
print(test("Welt"))
print(test("Discord"))
print(test(5))

