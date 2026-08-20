from dataclasses import dataclass, asdict
import json
from pathlib import Path
from pprint import pprint

@dataclass(slots=True, frozen=True)
class Person:
    first_name: str
    last_name: str
    email:str
    phone_number:str
    address:str
    country:str
    city:str
    birth_date:str

def lese_data_json(pfad: Path) -> dict[str, Person]:
    raw: str = pfad.read_text()
    raw: dict[str, dict[str, str]] = json.loads(raw)

    umgewandelt = dict()
    for key, val in raw.items():
        umgewandelt[key] = Person(**val)

    return umgewandelt

def schreibe_data_json(mein_objekt: dict[str, Person], pfad: Path):
    umgewandelt = dict()
    for key, val in mein_objekt.items():
        umgewandelt[key] = asdict(val)

    pfad.write_text(
        json.dumps(umgewandelt, indent=4)
    )

x = lese_data_json(Path("Data.json"))
schreibe_data_json(x, Path("Test.json"))

