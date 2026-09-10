from typing import Callable
from functools import wraps

def oberDecorator(ubergabe: str):
    def decorator(fkt: Callable):
        print("Test")

        @wraps(fkt)
        def ruckgabe(*args, **kwargs):
            print(args)
            #print(ubergabe, fkt.__name__)
            return fkt(*args, **kwargs)

        return ruckgabe
    return decorator

#meine_fkt = decorator(meine_fkt)
@oberDecorator("Eingabe")
def meine_fkt(text: str):
    #print("Hallo Welt", text)
    return 5

class Test:

    @oberDecorator("Methode")
    def methode(self, text: str):
        return 7

x = Test()
x.methode("Der Text")

# print(meine_fkt("text"))
# print(meine_fkt("text"))
# print(meine_fkt("text"))
# print(meine_fkt("text"))


