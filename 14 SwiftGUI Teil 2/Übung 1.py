import SwiftGUI as sg

sg.Themes.FourColors.SlateBlue()

def mach_knopf(text: str, width: int = 3, fontsize: int = 12, **kwargs) -> sg.Button:
    return sg.Button(
        text,
        width=width,
        fontsize=fontsize,
        **kwargs
    )

layout_links = [
    [
        mach_knopf("7"),
        mach_knopf("8"),
        mach_knopf("9"),
    ],[
        mach_knopf("4"),
        mach_knopf("5"),
        mach_knopf("6"),
    ],[
        mach_knopf("1"),
        mach_knopf("2"),
        mach_knopf("3"),
    ],[
        mach_knopf("0"),
        mach_knopf("."),
        mach_knopf("e"),
    ]
]

layout_rechts = [
    [
        mach_knopf("DEL"),
        mach_knopf("AC"),
    ],[
        mach_knopf("x"),
        mach_knopf("/"),
    ],[
        mach_knopf("+"),
        mach_knopf("-"),
    ],[
        mach_knopf("^"),
        mach_knopf("ANS"),
    ]
]

layout = [
    [
        sg.T(width=2),
        sg.Input("15"),
    ],[
        sg.T("^", width=2),
        sg.Input("2"),
    ], [
        sg.T("=", width=2),
        sg.Input("255.0"),
    ],[
        sg.HSep(),
    ],[
        sg.Frame(layout_links),
        sg.VSep(),
        sg.Frame(layout_rechts),
    ]
]

w = sg.Window(layout)

for e,v in w:
    ...

