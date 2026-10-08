from typing import Hashable, cast
import SwiftGUI as sg

sg.Themes.FourColors.Emerald()

class MeinFenster(sg.BasePopupNonblocking):

    def __init__(self):

        layout = [
            [
                sg.Button("Hallo Welt", key="Button"),
            ],[
                sg.T("Text", key="Text"),
            ]
        ]

        super().__init__(
            layout,
            grab_anywhere=True,
        )

    def _event_loop(self, e: Hashable, v: sg.ValueDict):

        if e == "Button" and sg.Popups.yes_no("Möchtest du das wirklich machen?"):
            v["Text"] = "Hallo Welt"
            #w.close()
            #sg.main_window().close()
            MeinFenster()

class yes_no(sg.BasePopupTyped[bool]):

    def __init__(self, text: str):

        layout = [
            [
                sg.T(text),
            ],[
                sg.Button("Yes", key="Yes"),
                sg.Button("No", key="No"),
            ]
        ]

        super().__init__(layout, default=False)

    def _event_loop(self, e: Hashable, v: sg.ValueDict):
        if e == "Yes":
            self.done(True)

        if e == "No":
            self.done(False)

#w = sg.Window(main_layout, transparency=1, titlebar=False)
# w = sg.HiddenMainWindow()
#
# MeinFenster()
# MeinFenster()
#MeinFenster().w.loop()
#
# w.loop()

#antwort: bool = cast(bool, yes_no("Hallo Welt?"))
antwort = yes_no("Hallo Welt?")()
print(antwort)

#print(sg.Popups.yes_no("Hallo Welt"))

