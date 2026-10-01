import SwiftGUI as sg

sg.Themes.FourColors.Emerald()

layout = [
    [
        lb := sg.Listbox(
            ["Hallo", "Welt", "Discord"],
            default_event=True,
            key="Liste",
        )
    ],[
        table := sg.Table(
            headings=["Spalte 1", "Andere Spalte", ""],
            key="Table",
            default_event=True,
            selectmode="extended",
            column_width=(100, 10, 10),
        )
    ]
]

w = sg.Window(layout)
table.overwrite_table_threaded(
    [
        [i, i ** 2, i ** 3] for i in range(30000)
    ],
)

for e,v in w:
    print(e,v, table.all_indexes)

    #table.sort(0, key= lambda a: abs(a - 5))
    if e == "Liste":
        # table.filter(by_column=0, key= lambda a: a % 2 == 0)
        # table.filter(by_column=0, key= lambda a: a % 3 == 0, only_remaining_rows=True)
        # table.persist_filter()
        table.see(499)

    if e == "Table":
        table.reset_filter()

    #table.all_indexes = (0, 1, 2)

    #v["Table"][0] = "Clicked"
    # zeile = v["Table"]
    # zeile[0] = "Clicked"

    #table.value = ["Hallo", "Welt"]
