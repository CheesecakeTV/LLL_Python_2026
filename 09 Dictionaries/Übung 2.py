from dataclasses import dataclass, replace

@dataclass(frozen=True, slots=True)
class Person:
    vorname: str
    nachname: str
    alter: int = 0
    eltern: tuple[None | Person, None | Person] = (None, None)

alle_personen: list[Person] = [
    Person("Taylor", "Charvez", 53),
    Person("Linda", "Shannon", 52),
    Person("Dennis", "Johnson", 22),
    Person("Sarah", "Graves", 13),
    Person("Jasmine", "Turner", 16),
]

def get_alter_ueber(die_personen: list[Person], min_alter: int = 18) -> list[Person]:
    return [i for i in die_personen if i.alter >= min_alter]

def erstelle_kind(kind_informationen: Person, elternteil1: Person, elternteil2: Person) -> Person:
    return replace(
        kind_informationen,
        eltern=(elternteil1, elternteil2),
    )

print(get_alter_ueber(alle_personen))
kind = Person("Christian", "Spannagel")

print(kind)
kind = erstelle_kind(kind, alle_personen[2], alle_personen[1])

print(kind)

