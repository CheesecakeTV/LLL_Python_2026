
# Vor falscher Übergabe schützen (10 Minuten)
Halte dich nicht zu lange mit einzelnen Teilen dieser Übung auf.

Kopiere folgende Funktion:
```py
def istTeilbar(zahl: int, durch: int) -> bool:
    """
    Gibt zurück, ob 'zahl' durch 'durch' teilbar ist.
    """
    return not zahl % durch
```

Implementiere folgendes, indem du die Funktion veränderst.
Teste alles Neue, indem du die Funktion entsprechend nutzt.
1. Ist mindestens ein Argument nicht vom Typ `int`, wird ein Fehler ausgelöst.
2. Ist `durch` gleich `0`, wird `None` zurückgegeben. Tipp: Passe auch die Typehints entsprechend an.
3. Ist mindestens ein Argument kleiner als `0`, wird `None` zurückgegeben.
4. Ist `durch` größer als `zahl`, wird `None` zurückgegeben.
5. Wird `durch` nicht übergeben, wird es als `2` definiert.


