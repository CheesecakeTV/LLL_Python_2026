import random
from pathlib import Path

# Erstellt "Ordner" mit zufällig benannten Dateien

filetypes = [".txt", ".dat", ".jpg", ".cfg", ".jpeg", ".png"]
foldername = "Ordner"

Path(foldername).mkdir(exist_ok=True)

for i in range(10000):
    i = str(i).zfill(6)
    ending = random.choice(filetypes)

    with open(
        f"{foldername}/{random.randint(1, 100000)} Datei {i}{ending}",
        "w",
    ) as f:
        f.write(i)



