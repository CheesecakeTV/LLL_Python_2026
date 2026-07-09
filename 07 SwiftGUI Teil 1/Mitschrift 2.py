import SwiftGUI as sg

sg.Themes.FourColors.DarkGold()

def zeile(key: str) -> list[sg.BaseElement]:
    def knopf():      # e, v, elem: sg.BaseElement):
        # elem.value = "Gedrückt"
        meinInput.value = ""

    return [
        #sg.Input(key="Input"),
        meinInput := sg.Input(key=key, default_event=True, width=50),
        sg.Spacer(width=5),
        sg.Button(" x ", key_function=knopf)
    ]

layout = [
    [
        *zeile("Name"),
        *zeile("Alter"),
        *zeile("Nachname"),
    ]
]

w = sg.Window(layout)

for e,v in w:
    print(e, v)

    # if e == "Clear":
    #     #v["Input"] = ""
    #     meinInput.value = ""

