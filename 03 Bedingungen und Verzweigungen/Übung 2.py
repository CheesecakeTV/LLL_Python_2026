

while True:
    x = input("Gib eine Ganzzahl ein: ").strip()

    if not x:
        exit()

    x = int(x)

    if x < 0:
        print("Bitte nur positive Zahlen eingeben")
        exit()
    if x < 2:
        exit()

    i = 2
    #grossterTeile = None
    grossterTeile = 1
    while x > i:
        teilbar = x % i == 0
        print(i, teilbar)

        if teilbar:
            grossterTeile = i

        i = i + 1

    #if grossterTeile is None:
    if grossterTeile == 1:
        print("Die Zahl ist eine Primzahl")
    else:
        print("Teilbar durch:", grossterTeile)


