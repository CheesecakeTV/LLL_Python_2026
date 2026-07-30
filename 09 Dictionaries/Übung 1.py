
def printDict(dasDict: dict) -> None:
    for key, val in dasDict.items():
        print(key, "-", val)

printDict({"Hallo": "Zusammen", "Python": "Kurs"})

def replace(dasDict: dict, **kwargs) -> dict:
    dasDict = dasDict.copy()

    dasDict.update(kwargs)
    return dasDict

# Erstellt folgende Ausgabe:
# Hallo - Zusammen
# Python - Kurs

dasDict = {"Hallo": "Zusammen", "Python": "Kurs"}
dasNeueDict = replace(
    dasDict,
    Hallo="Welt",
    NeuerKey="Mir fällt nichts ein",
)

print(dasNeueDict)
