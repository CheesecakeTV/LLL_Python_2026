import SwiftGUI as sg

#sg.Examples.preview_all_themes()
sg.Themes.FourColors.DarkGold()
#sg.Examples.preview_all_elements()

layout = [
    [
        sg.Text("Hallo Welt"),
        sg.Button("Text", key="ButtonOben")
    ],[
        sg.Button(
            "Neue Zeile",
            key="Button",
        )
    ],[
        sg.Input(
            key="Input",
            #default_event=True,
        ).bind_event(
            sg.Event.KeyEnter,
            key_extension="Enter",
        ).bind_event(
            sg.Event.MouseEnter,
            key="MouseEnter",
        )
    ],[
        sg.Checkbox(
            "Check",
            key="Check",
            default_event=True,
        )
    ]
]

w = sg.Window(layout)

for e,v in w:
    print("Event:",e, "Werte:",v)
    print(v["Input"])

    if e == "Button":
        print("Button unten!")
        v["Input"] = "0"
        v["Button"] = "UNTEN"

    if e == "ButtonOben":
        print("Button oben!")
        v["Check"] = True

