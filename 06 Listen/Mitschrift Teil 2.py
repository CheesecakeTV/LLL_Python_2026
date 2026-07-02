
x: list[str | int] = []
a: tuple[str, int, int] = ("H", 5, 23)
c: tuple[str| int, ...] = ("H", 5)

y = ([5], 2, 3, 7, 3)
b = y
y = y + (5, ) # Quasi .append

y[0][0] = 3

s = "Hallo Welt Discord"
print(s)
liste = list(s)
liste[0] = "h"
s = "".join(liste)
print(s)

print(s.split(" "))
print(s)

