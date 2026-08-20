
x = [1,2,3,4]

for i in x:
    print(i)

class MeinRange:

    def __init__(self, ende: int):
        self.ende = ende
        self._wert = -1

    def __iter__(self):
        self._wert = -1
        return self

    def __next__(self):
        self._wert += 1

        if self._wert >= self.ende:
            raise StopIteration

        return self._wert

    @property
    def wert(self):
        return self._wert

    @wert.setter
    def wert(self, val):
        self._wert = val

x = MeinRange(15)

#print(type(x).__name__)

iterator = iter(x)  # Erstelle Iterator
while True:
    try:
        i = next(iterator)  # Schritt: Nächstes Objekt holen
    except StopIteration: # Ende: Exception ausgelöst
        break

    print(i)    # Innerhalb der Schleife

x.wert = 15
for i in x:
    print(x.wert)
