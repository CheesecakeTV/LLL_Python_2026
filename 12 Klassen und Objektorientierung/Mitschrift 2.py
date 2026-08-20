

class Test:

    def __init__(self, wert: int):
        self.wert = wert

    def __str__(self):
        return f"<Test: {self.wert=}>"

    def __getitem__(self, item: int) -> int:
        return self.wert * item

    def __setitem__(self, key: int, value: int):
        print(f"{key=}, {value=}")

    def __delitem__(self, key: int):
        print("Gelöscht:", key)

    def __len__(self) -> int:   # len(...)
        return self.wert

    def __contains__(self, item: int) -> bool:
        return item < self.wert

    def __call__(self, wert: int):
        print(wert, self)
        return self

x = Test(15)
x(100)(125)(135)

print(x[10])
x[100] = 55

del x[123]

if 20 in x:
    print("Ist drin!")
