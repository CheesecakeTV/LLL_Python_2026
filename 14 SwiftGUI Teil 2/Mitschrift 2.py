import SwiftGUI as sg

sg.Themes.FourColors.Emerald()
#sg.Examples.preview_all_elements()
sg.Examples.preview_all_themes()
exit()

inner_layout = [
    [
        sg.T(
            "Hallo Welt"
        ),
    ],[
        #sg.HSep()
        sg.Spacer(
            height=30,
            width=500,
        )
    ], [
        sg.Input()
    ]
]

layout = [
    [
        sg.Listbox(

        ),
        sg.VSep(weight=5, padding=10),
        sg.Frame(
            inner_layout
        ),
    ]
]

w = sg.Window(layout)

for e, v in w:
    print(e)




