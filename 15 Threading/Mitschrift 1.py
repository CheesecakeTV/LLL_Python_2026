import SwiftGUI as sg
import threading
import time

def zahler():
    i = 0
    while True:
        i += 1
        w.throw_event(key="Zahl", value=i)
        time.sleep(1)

sg.Themes.FourColors.Emerald()

layout = [
    [
        sg.T(key="Zähler", fontsize=20)
    ]
]

w = sg.Window(layout)

threading.Thread(target=zahler, daemon=True).start()

for e,v in w:

    if e == "Zahl":
        v["Zähler"] = v["Zahl"]


