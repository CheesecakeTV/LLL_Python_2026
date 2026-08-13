
class Haus:
    # wande: int  # Attribute
    # tueren: int

    def __init__(self, wande: int = 15):
        self.wande = wande
        self.tueren = 7
        self._liste = [1,2,3]

    def print_info(self):
        print(self.wande, self.tueren)

    @staticmethod
    def berechne_wande(tueren: int) -> int:
        return int(tueren / 4)

haus1 = Haus(16)
haus1.print_info()
haus1.wande = 15
haus1.print_info()

print(haus1.berechne_wande(15))

print(dir(haus1))

