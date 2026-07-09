import SwiftGUI as sg

sg.Themes.FourColors.DarkGold()

layout = [
    [
        sg.Input(),
        sg.Button(" x ", key="Clear")
    ]
]

w = sg.Window(layout)

for e,v in w:
    ...

