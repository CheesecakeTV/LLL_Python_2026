
x = False
y = True

if bool(x):
    print("Wahr!")
elif y:
    print("Andere Bedingung")
elif x and y:
    ...
    pass
else:
    print("Falsch!")

x = "Hallo"
if x:
    print(x, "<- Ausgabe")

print("2. Zeile")

while x:
    x = False
    print(x, "<- Ausgabe")
