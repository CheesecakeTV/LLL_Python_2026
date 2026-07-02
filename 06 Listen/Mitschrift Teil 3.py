
h = ["Hallo", "Welt"]
x = ["ix"]

grosse_list = [
    *h,
    *x,
]
print(grosse_list)

a, b, c = "Hallo", *("Welt", 15)
a, b, c, *d = "Hallo", "Welt", 15, 16, 17, 18
a, (b, c) = "Hallo", ("Welt", 15)

def mal_durch(a: float, b: float) -> tuple[float, float]:
    return a * b, a / b

def print_neu(*rest):
    print(*rest)

print_neu(156, 7, 3, 6, 3, 1)

mal, durch = mal_durch(15, 3)
