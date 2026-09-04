
# def ggt(a: int, b: int) -> int:
#     if not b:
#         return a
#
#     if b > a:
#         return ggt(b, a)
#
#     return ggt(b, a % b)

class Bruch:

    def __init__(self, zahler: int | "Bruch", nenner: int = 1):
        if isinstance(zahler, Bruch):
            assert nenner == 1, "Wird ein Bruch übergeben, muss der Nenner leer gelassen werden"
            zahler, nenner = zahler.zahler, zahler.nenner

        teiler = self.ggt_method(zahler, nenner)

        self._zahler: int = int(zahler / teiler)
        self._nenner: int = nenner // teiler

    def __str__(self) -> str:
        return f"<{self.zahler}/{self.nenner}>"

    def __int__(self) -> int:
        return int(self.zahler / self.nenner)

    def __float__(self) -> float:
        return self.zahler / self.nenner

    @staticmethod
    def ggt_method(a: int, b: int):     # Kein Teil der Übung, das hier beantwortet nur eine Frage
        """Gibt den größten gemeinsamen Teiler der übergebenen Zahlen zurück (Euklidischer Algorithmus)"""
        if not b:
            return a

        a, b = abs(a), abs(b)   # Hatte ich noch vergessen, die Zahlen sollen beide nur positiv sein können

        if b > a:
            return Bruch.ggt_method(b, a)   # Bei einer staticmethod darf man den Aufruf über die Klasse selbst machen.
                                            # Wir haben hier kein self zur Verfügung, daher bleibt keine andere Möglichkeit

        return Bruch.ggt_method(b, a % b)

    def __add__(self, other: "Bruch" | int) -> "Bruch":
        if isinstance(other, int):
            other = Bruch(other)

        return Bruch(
            self.zahler * other.nenner + other.zahler * self.nenner,
            self.nenner * other.nenner
        )

    def __sub__(self, other: "Bruch" | int) -> "Bruch":
        if isinstance(other, int):  # Das ist kopierter Code, aber ohne Decorator lässt sich hier wenig vereinfachen
            other = Bruch(other)

        return self + Bruch(- other.zahler, other.nenner)

    def __mul__(self, other: "Bruch" | int) -> "Bruch":
        if isinstance(other, int):
            other = Bruch(other)

        return Bruch(self.zahler * other.zahler, self.nenner * other.nenner)

    def __truediv__(self, other: "Bruch" | int) -> "Bruch":
        if isinstance(other, int):
            other = Bruch(other)

        return Bruch(self.zahler * other.nenner, self.nenner * other.zahler)

    @property
    def zahler(self):   # Dadurch, dass diese Property keinen Setter hat, kann sie nicht verändert werden
        return self._zahler

    @property
    def nenner(self):
        return self._nenner

    def __radd__(self, other: float) -> float:
        return float(self) + other

    def __rsub__(self, other: float) -> float:
        return float(self) - other

    def __rmul__(self, other: float) -> float:
        return float(self) * other

    def __rtruediv__(self, other: float) -> float:
        return float(self) / other

def float_to_bruch(x: float) -> Bruch:
    x = round(x, 10)
    return Bruch(   # Der Bruch wird ja eh automatisch gekürzt, passt also
        int(x * 10_000_000_000),
        10_000_000_000,
    )


