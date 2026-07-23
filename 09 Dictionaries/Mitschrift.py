from typing import Hashable

x: dict[Hashable, str] = {
    "Hallo": "Welt",
    "Python": "Discord",
    "0": "Hallo",
    0: "Null",
}

y = {
    "Python": "Kurs",
    "Noch neuer": "Klappt",
    #**x,
}

print(y)

exit()
#print(x["0"])

#x["Neu"] = "Wert"

x.update(y)

# del x["Hallo"]
# print(x.pop("Python"))

print(x)

for i in x.keys():
    print(i)

for i in x.values():
    print(i)

for key, val in x.items():
    print(key, val)

#print(list(x.keys()))


