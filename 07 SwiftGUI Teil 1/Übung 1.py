import SwiftGUI as sg

sg.Themes.FourColors.Jungle()

sg.GlobalOptions.Common_Textual.fontsize = 14
sg.GlobalOptions.Button.fontsize = 12

def clear_elem(e: str, v: sg.ValueDict, elem: sg.Input):
    #v[e] = ""
    elem.value = ""

layout: list[list[sg.BaseElement]] = [
    [
        sg.Input(
            key="In1",
        ).bind_event(
            sg.Event.ClickDoubleLeft,
            key_function=clear_elem,
        )
    ],[
        sg.Input(
            key="In2",
        ).bind_event(
            sg.Event.ClickDoubleLeft,
            key_function=clear_elem,
        )
    ],[
        sg.Button("+", key="+", width=3),
        sg.Button("-", key="-", width=3),
        sg.Button("*", key="*", width=3),
        sg.Button("/", key="/", width=3),
    ], [
        sg.T(
            key="Ausgabe",
        )
    ]
]

w = sg.Window(layout)

for e,v in w:
    print(e)

    # if e == "In1":
    #     v["In1"] = ""

    # if e == "In2":
    #     v["In2"] = ""

    if e == "+":
        v["Ausgabe"] = float(v["In1"]) + float(v["In2"])

    if e == "-":
        v["Ausgabe"] = float(v["In1"]) - float(v["In2"])

    if e == "*":
        v["Ausgabe"] = float(v["In1"]) * float(v["In2"])

    if e == "/":
        v["Ausgabe"] = float(v["In1"]) / float(v["In2"])


