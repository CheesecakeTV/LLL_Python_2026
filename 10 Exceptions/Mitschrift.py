
#raise ZeroDivisionError("Hallo Welt")

try:
    1 / 0
except AttributeError:
    ...
except (ZeroDivisionError, TypeError):
    print("Division durch 0")
else:
    print("Hallo")
finally:
    ...

def fkt():
    try:
        return
    finally:
        print("Hallo")

fkt()

# while True:
#     try:
#         eingabe = input("Eingabe: ")
#         eingabe = int(eingabe)
#         break
#     except Exception:
#         ...

