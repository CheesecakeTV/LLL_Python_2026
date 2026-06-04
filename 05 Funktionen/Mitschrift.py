
def print_fehler(variablenname = "?"):
    print("Fehler! Falsche Zahl eingegeben:", variablenname)

def ist_korrekt(falscher_wert, wert, variable= "?", hans = ":"):
    if wert == falscher_wert:
        print_fehler(variable)

def ist_prim(zahl):
    if zahl % 2 == 0:
        return False

    return True

x = 14
y = 16

#ist_korrekt(wert=x, falscher_wert=14, variable="x")
ist_korrekt(12, x, hans="x")
ist_korrekt(13, x)

ist_korrekt(13, y)

zahl_ist_prim = ist_prim(16)

x = 15
def andere_x():
    global x
    x = 14

def print_x():
    print(x)

def hoch(x, y):
    return x ** y

andere_x()
#print(x)

print_x()



