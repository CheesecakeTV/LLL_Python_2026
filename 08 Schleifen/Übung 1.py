
zahler = 0
eingaben_liste = []

while True:
    eingabe = input("Eingabe: ")

    if not eingabe:
        break

    eingabe = int(eingabe)

    if eingabe < 0:
        continue

    eingaben_liste.append(eingabe)
    print(zahler := zahler + eingabe)

print("Ende")

for n,i in enumerate(eingaben_liste):
    print(n + 1, "-", i)

