
#x = "Hallo\nWelt"
x = "Temp: 200005.1\tFeuchte: 80"
y = "Temp: 5.1\tFeuchte: 80"

#print(x, end="\n")
print(x)
print(y)

z = x + y
print(z)

print(x * 5)

#print(x.replace("Temp", "Heat"))

x = x.replace("Temp", "Heat")

# eingabe = float(input().replace(",", "."))
# print(eingabe)

print("Ericß".upper())
print("Ericß".lower())
print("Ericß".casefold())

print(len(x))

print("Feucht" in x)

wert = 15.5
ausgabe = "Wert: " + str(wert) + " °C"
ausgabe = f"Wert: {wert} °C"
ausgabe = f"{wert=}"
print(ausgabe)

print(f"{10000000000000000:,}")





