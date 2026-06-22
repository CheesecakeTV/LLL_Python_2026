
def aufdecken(feld):
    # Rekursionsverankerung
    if istAufgedeckt(feld):
        return

    if getWert(feld) != 0:
        wirklichAufdecken(feld) # Wert enthüllen
        return

    # Rekursionsschritt
    für alle Nachbarfelder:
        aufdecken(nachbarfeld)


