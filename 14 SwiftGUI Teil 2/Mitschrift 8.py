from typing import Hashable, Any, Self
import SwiftGUI as sg
import json

sg.Themes.FourColors.Jungle()

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

    def _event_loop(self, e: Hashable, v: sg.ValueDict):
        if e == "Button":
            self.done(self.value)
            v["Input"] = ""
            self.throw_default_event()
            #self.throw_event()

    def _get_value(self) -> str:
        return self.v["Input"]

    def set_value(self, val: str) -> Self:
        self.v["Input"] = val
        return self

    def init_window_creation_done(self):
        super().init_window_creation_done()

    def popup(self, **window_kwargs) -> str:
        super().popup(**window_kwargs)

#print(InputMitX().popup(padx = 50, pady = 50))

layout = [
    [
        InputMitX(key="Combined1", default_event=True),
        InputMitX(key="Combined2"),
        InputMitX(key="Combined3"),
    ],[
        mein_knopf := sg.Button("Test", key=10)
    ],[
        sg.Button("Speichern", key="Save"),
        sg.Button("Laden", key="Laden"),
        sg.ColorChooserButton(),
    ]
]

w = sg.Window(layout)
gespeichert = dict()

for e, v in w:
    print(v.to_json())
    #print(json.dumps(v.to_json(), indent=4))
    #v.from_json({"Combined1":{"Input": "Hallo Welt"}})
    #v.from_json(v.to_json())
    # mein_knopf.to_json()
    # mein_knopf.from_json("Hallo")

    #v["Combined2"]["Input"] = "Hallo Welt"
    #v["Combined2"] = "Hallo Welt"

    if e == "Save":
        gespeichert = v.to_json()

    if e == "Laden":
        v.from_json(gespeichert)
