from pathlib import Path
import os

ordner_alt = Path("Ordner")
ordner_neu = Path("OrdnerNeu")
ordner_neu.mkdir(exist_ok=True)

def korrigiere_pfad(derPfad: Path | str | os.PathLike, neuer_ordner: Path) -> Path:
    derPfad = Path(derPfad)

    stem = derPfad.stem
    stem = stem.split(" ")
    stem[0], stem[2] = stem[2], stem[0]
    stem = " ".join(stem)

    name = derPfad.with_stem(stem).name

    return neuer_ordner / name

def kopiere_datei(alter_pfad: Path, neuer_pfad: Path):
    data = alter_pfad.read_bytes()
    neuer_pfad.write_bytes(data)

#ordner_alt.iterdir()
for i in os.listdir(ordner_alt):
    alter_pfad = ordner_alt / i
    neuer_pfad = korrigiere_pfad(alter_pfad, ordner_neu)

    kopiere_datei(alter_pfad, neuer_pfad)


