import SwiftGUI as sg

#sg.Themes.FourColors.Emerald()
#sg.GlobalOptions.Button.background_color = "green"
#sg.GlobalOptions.Button.text_color = "pink"
#sg.GlobalOptions.Text.text_color = "pink"
# sg.GlobalOptions.Common_Textual.text_color = "pink"
# sg.GlobalOptions.Text.text_color = "blue"
# sg.GlobalOptions.Common_Textual.fontsize = 14
# sg.GlobalOptions.Button.fontsize = None

#sg.Themes.Thematic.Hacker()

class Blau(sg.Themes.BaseTheme):
    def apply(self) -> None:
        sg.GlobalOptions.Common_Background.background_color = "navy"
        sg.GlobalOptions.Common_Field_Background.background_color = "blue"


sg.Examples.preview_all_themes()

exit()

layout = [
    [
        sg.Button("Hallo", background_color="red"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Text("Text"),
        sg.Text("Text"),
        sg.Text("Text"),
        sg.Text("Text"),
        sg.Text("Text"),
    ],[
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
    ],[
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
    ],[
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
        sg.Button("Hallo"),
    ]
]

w = sg.Window(layout)

for e,v in w:
    ...
