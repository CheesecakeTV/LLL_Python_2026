import json
from typing import Generator

import faker    # Bibliothek heißt Faker

# Generates Data.json

fake = faker.Faker()

def get_fake() -> tuple[str, dict]:
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name + " " + last_name, {
        "first_name": first_name,
        "last_name": last_name,
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.address(),
        "city": fake.city(),
        "country": fake.country(),
        "birth_date": fake.date_of_birth().strftime("%Y-%m-%d"),
    }

def faker_generator(qtt: int = 5000) -> Generator[tuple[str, dict], None, None]:
    for i in range(qtt):
        yield get_fake()

data = dict(faker_generator())

with open("Data.json", "w") as f:
    f.write(json.dumps(data, indent=4))

print("Done")
