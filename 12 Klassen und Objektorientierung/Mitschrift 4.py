
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

class MeinBruch(Bruch):

    def __init__(self, zahler: int = 1, nenner: int = 1, zahl: int = 5):
        super().__init__(zahler=zahler, nenner=nenner)
        print(self.zahler)
        self.zahl = zahl

    def __str__(self):
        return f"<Bruch: {self.zahler}/{self.nenner}>"

x = MeinBruch()
y = Bruch(15, 3)
print(x)
print(y)

class MeineListe(list):

    def append(self, object, /) -> "MeineListe":
        super().append(object)
        return self

    def sort(self, *, key = None, reverse = False) -> "MeineListe":
        return MeineListe(sorted(self, key=key, reverse=reverse))

x = MeineListe([2,3,6,1,6,33,5])
print(type(x.sort()))
print(type(x))

print(x)
print(x.append(123))
print(x)

print(isinstance(x, list))
print(type(x) == list)



