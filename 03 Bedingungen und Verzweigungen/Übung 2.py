

x = int(input("Gib eine Ganzzahl ein: ").strip())

# 1.
if x < 0:
    print("Bitte nur positive Zahlen eingeben")
    exit()
if x < 2:
    exit()

# 2. + 3.
i = 2
while x > i:
    print(i, x % i == 0)
    i = i + 1



