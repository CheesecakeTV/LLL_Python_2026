
# 2. Themes (Optional)
Erstelle ein gutaussehendes Theme und teste es mit `sg.Examples.preview_all_elements()`.

Gute Themata integriere ich mit deiner Erlaubnis gerne ins SwiftGUI-package.

Für ein vollständiges Thema, denk daran, dass deaktivierte/readonly Elemente standardmäßig anders aussehen.
Um auch das zu berücksichtigen, teste es mit Folgendem:
```py
sg.Examples.preview_all_elements(flip_disabled=True, flip_readonly=True)
```

# X. Praxisbeispiel
Folgende Situation:\
An einen Raspberry Pi mit Touchscreen ist ein QR-Code Scanner angeschlossen.

Der Scanner funktioniert wie eine Tastatur: Nach dem Scannen wird der gescannte Text "geschrieben" und enter gedrückt.

Da weder Maus noch Tastatur angeschlossen sind, muss man bei der Eingabe kreativ sein.

Erstelle das Element `ScanInputButton`.

# X. Verschiedenes
Folgendes Layout enthält zwei `sg.Notebook`.

Sorge dafür, dass wenn der Nutzer den Tab eines Notebooks wechselt, auch der Tab des Anderen wechselt.
Beide Notebooks haben also "immer" den gleichen Tab geöffnet.

Die Layouts beider notebooks sind identisch, könnten aber erweitert werden.
Stelle also sicher, dass deine Lösung auch mit 3, oder mehr Tabs funktioniert.

Bonuspunkte, wenn du es mit sinnvollen key-functions löst.

```py
import SwiftGUI as sg

sg.Themes.FourColors.Jungle()

layout = [
    [
        notebook1 := sg.Notebook(
            sg.TabFrame([
                [sg.T("Tab 1")]
            ], fake_key="Tab1"),
            sg.TabFrame([
                [sg.T("Tab 2")]
            ], fake_key="Tab2"),
        )
    ], [
        sg.Spacer(height=5),
    ], [
        notebook2 := sg.Notebook(
            sg.TabFrame([
                [sg.T("Tab 1")]
            ], fake_key="Tab1"),
            sg.TabFrame([
                [sg.T("Tab 2")]
            ], fake_key="Tab2"),
        )
    ]
]

w = sg.Window(layout, padx=30, pady=30)

for e,v in w:
    print(e, v)
```


