from dataclasses import dataclass, replace, asdict

@dataclass(slots=True, frozen=True)
class Auto:
    typ: str
    gewicht: float  = 1
    anzahl_turen: int   = 2
    reifen: str = "Gummi"

mein_auto = Auto("Hyundai", 0.8, 4)
mein_auto2 = Auto("Audi", 1.2, 5)
mein_auto3 = Auto("BMW", anzahl_turen=5)

#mein_auto.bla = "151"
#mein_auto.typ = "VW"

mein_auto = replace(mein_auto, typ="VW", gewicht=1)
print(asdict(mein_auto))

print(mein_auto.typ)
print(mein_auto)

def printAuto(dasAuto: Auto):
    assert isinstance(dasAuto, Auto)
    print(dasAuto)

# print(mein_auto)
# print(mein_auto2)


