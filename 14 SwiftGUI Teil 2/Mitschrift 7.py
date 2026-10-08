from typing import Hashable

import SwiftGUI as sg
from SwiftGUI import ValueDict

sg.Themes.FourColors.TransgressionTown()

def gib_input():
    return [
        inp := sg.Input(),
        sg.Button("x", key_function=lambda: inp.set_value("")),
    ]

class InputMitX(sg.BaseCombinedElement):

    def __init__(
            self,
            key: Hashable = None,
            default_event: bool = False,
    ):
        layout = [
            [
                sg.Input(key="Input"),
                sg.Button("x", key="Button"),
            ]
        ]

        super().__init__(
            layout,
            key= key,
            default_event= default_event,
        )

    def _event_loop(self, e: Hashable, v: ValueDict):
        if e == "Button":
            v["Input"] = ""
            self.throw_default_event()

layout = [
    [
        InputMitX(key="Combined1", default_event=True),
        InputMitX(key="Combined2"),
        InputMitX(key="Combined3"),
    ],[
        sg.Button("Test", key=10)
    ]
]

w = sg.Window(layout)

for e, v in w:
    print(e)

