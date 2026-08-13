
with open("Werte.txt", "r") as f:
    raw = f.readlines()
    #raw = f.read().split("\n")

laenge = len(raw)
print(laenge)

summe = 0
for wert in raw:
    summe += float(wert)

# raw = [float(wert) for wert in raw]
# summe = sum(raw)

print(summe)
print("Durchschnitt:", summe / laenge)
