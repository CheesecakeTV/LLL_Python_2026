import SwiftGUI as sg

sg.Themes.FourColors.Emerald()

layout = [
    [
        sg.T(
            "Hallo Welt",
            text_color=sg.Color.tomato,
            #background_color=sg.rgb(255, 128, 0),
        )
    ],[
        sg.Button(
            "Klick mich",
            #key="Button",
            key_function= lambda : button2.update(background_color = "green", disabled = True),
            width= 20,
            #expand=True,
        ),
        button2 := sg.Button(
            "Klick mich auch",
            key="Button2",
            width= 20,
            #expand=True,
        ),
    ],[
        sg.Input(
            key="Input",
            default_event=True,
            #width=80,
            expand=True,
        ).bind_event(
            sg.Event.Control_("a"),
            key="Anderer key",
        )
    ]
]

w = sg.Window(layout).bind_event(sg.Event.KeyEscape, key="Escape!")

for e, v in w:
    print(e)

    # if e == "Button":
    #     w["Button"].update(background_color = "green")


