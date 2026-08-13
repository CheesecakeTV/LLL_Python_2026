
class Haus:
    # wande: int  # Attribute
    # tueren: int

    def __init__(self, wande: int = 15):
        self.wande = wande
        self.tueren = 7
        self._liste = [1,2,3]

    def __eq__(self, other: "Haus") -> bool:
        return self.wande == other.wande

    def __str__(self) -> str:
        return f"<Haus-Objekt {self.wande=}, {self.tueren=}>"

    def __bool__(self) -> bool:
        return self.tueren > 0

    def __repr__(self) -> str:
        #return str(self)
        return f"<Haus-Objekt {id(self)} {self.wande=}, {self.tueren=}>"

    def __hash__(self) -> int:
        return hash((self.wande, self.tueren))

    def print_info(self):
        print(self.wande, self.tueren)

    @staticmethod
    def berechne_wande(tueren: int) -> int:
        return int(tueren / 4)

haus1 = Haus(16)
haus2 = Haus(16)

if haus1:
    ...

meine_liste = [haus1, haus2]
#meine_liste = ["1",2,3]
print(meine_liste)

print(haus1 == haus2) # haus1.__eq__(haus2)
print(haus1 is haus2)

# haus1.print_info()
# haus1.wande = 15
# haus1.print_info()

#print(haus1.berechne_wande(15))

#print(dir(haus1))

mein_dict = {haus1: haus2, haus2: haus1}
print(mein_dict)

