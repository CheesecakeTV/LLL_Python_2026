
def ggt(a: int, b: int) -> int:
    """Gibt den größten gemeinsamen Teiler der übergebenen Zahlen zurück (Euklidischer Algorithmus)"""
    if not b:
        return a

    if b > a:
        return ggt(b, a)

    return ggt(b, a % b)

class Bruch:

    def __init__(self, zahler: int, nenner: int = 1):
        teiler = ggt(zahler, nenner)

        self.zahler: int = int(zahler / teiler)
        self.nenner: int = nenner // teiler

    def __str__(self) -> str:
        return f"<{self.zahler}/{self.nenner}>"

    def __int__(self) -> int:
        return int(self.zahler / self.nenner)

    def __float__(self) -> float:
        return self.zahler / self.nenner

    @staticmethod
    def ggt_method(a: int, b: int):
        return ggt(a, b)

    def __mul__(self, other: "Bruch") -> "Bruch":
        return Bruch(self.zahler * other.zahler, self.nenner * other.nenner)

x = Bruch(1, 3)
y = Bruch(90, 1)

z = x * y

print(x, y, z)


