from typing import Hashable
import SwiftGUI as sg

sg.Themes.FourColors.Jungle()

class ListAuswahl(sg.BasePopupTyped[tuple]):

    def __init__(
            self,
            text: str,
            auswahlmoglichkeiten: tuple[str, ...],
    ):
        self._auswahl = auswahlmoglichkeiten

        langste_lange = max(map(len, auswahlmoglichkeiten))
        #langste_lange = len(sorted(auswahlmoglichkeiten, key=len)[-1])

        layout: list[list[sg.BaseElement]] = [
            [
                sg.T(text),
            ],[
                sg.Spacer(height=5)
            ], *[
                [sg.Checkbox(i, width=langste_lange + 2, key=i)] for i in auswahlmoglichkeiten
            ],[
                sg.Button("Fertig", key="Fertig"),
            ]
        ]

        super().__init__(layout, padx = 30, pady = 30, default= tuple())

    def _event_loop(self, e: Hashable, v: sg.ValueDict):

        if e == "Fertig":
            # ruckgabe = list()
            # for i in self._auswahl:
            #     if v[i]:
            #         ruckgabe.append(i)

            # ruckgabe = [i for i in self._auswahl if v[i]]
            ruckgabe = filter(lambda a: v[a], self._auswahl)

            self.done(tuple(ruckgabe))

print(ListAuswahl(
    text="Hallo Welt",
    auswahlmoglichkeiten= ("Schnulli", "Shadow", "Spiegelfechter", "Zapriski"),
)())
