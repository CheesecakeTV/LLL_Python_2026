from typing import Callable

def dieFkt() -> int:
    print("Hallo Welt")
    return 5

def rufe_auf(fkt: Callable) -> None:
    fkt()

def gib_funktion() -> Callable:
    var = 5

    def ruckgabe() -> int:
        nonlocal var
        print("Hallo", var)
        var += 1
        return 15

    return ruckgabe

r = gib_funktion()
r()
r()
r()     # 7
r2 = gib_funktion()
r2()    # 5
r()     # 8


# def hoch2(x: int) -> int:
#     return x ** 2


hoch2 = lambda x: x ** 2
print(hoch2(5))

rufe_auf(lambda : print("Hallo Welt"))


