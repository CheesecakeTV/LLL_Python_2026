

# 1. Generators (15 Minuten)
Implementiere UND TESTE folgende Generators.
Tipp: Oft kannst du bereits implementierte Generator nutzen, um einen neuen zu erstellen.

1. `blinker()`: Gibt abwechselnd `True` und `False` zurück.
2. `count(initial: int = 0, amount: int = 0)`: Zählt durchgehend hoch. `initial` ist die erste zurückgegebene Zahl, welche nach jedem Aufruf um `amount` erhöht wird.
3. `fib()`: Gibt die Werte der Fibonacci-Folge zurück.
4. `geradeZahlen()`: Äquivalent zu `count(0, 2)`.
5. `zahlenfolge()`: Zählt von 0 bis 1, danach von 0 bis 2, danach 0 bis 3, usw.: `0 1 0 1 2 0 1 2 3 0 1 2 3 4...`.
6. `begrenzen(iterator: Iterable, max_val: int)`: Gibt die Werte des übergebenen Iterables zurück. Übersteigt ein Rückgabewert `max_val`, wird der Generator beendet.
7. `primzahlen()`: Gibt alle Primzahlen zurück.

# 2. Funktionen als Objekte, Generators (20 Minuten)
In dieser Übung programmieren wir einige bereits vorhandene Funktionen nochmal.
Du darfst natürlich die jeweils nachprogrammierte Funktion nicht nutzen, sonst wäre die ganze Geschichte ziemlich witzlos.

1. Implementiere `mapGen(f: Callable, obj: Iterable) -> Generator[Any, None, None]`, die genau das Gleiche macht wie `map`.
2. Implementiere `filterGen(f: Callable, obj: Iterable) -> Generator[Any, None, None]`, die genau das Gleiche macht wie `filter`.
3. Implementiere `enumerateGen`, die genau das Gleiche macht wie rate mal.
4. Implementiere `zipGen`.
5. Implementiere `enumerateZipGen`, was die Funktionalitäten von `enumerateGen` und `zipGen` vereint.

# 3. Decorators (15 Minuten)
Implementiere UND TESTE folgende Decorator.\
Wichtig: Denke dabei daran, dass viele Funktionen sowohl Parameter, als auch Rückgaben haben.
1. Bei jedem Funktionsaufruf wird ausgegeben, dass eine Funktion aufgerufen wird.
2. Bei jedem Funktionsaufruf wird ausgegeben, wie oft die Funktion bisher aufgerufen wurde.
3. Dekorierte Funktionen machen gar nichts mehr. Es wird kein Fehler ausgelöst und auch nichts zurückgegeben.
4. Bei jedem Funktionsaufruf wird die Rückgabe des VORHERIGEN Aufrufs zurückgegeben. Beim ersten Aufruf wird `None` zurückgegeben.
5. Jede Funktion wird in einer gemeinsamen, globalen Liste abgelegt. Der Funktionsaufruf wird nicht beeinflusst.
6. Der Funktionsaufruf wird durch try...except vor einer Art Fehler geschützt. Die Art der Exception und Standard-Rückgabe (default) wird beim Nutzen des Decorators festgelegt:
```py
@handleException(ZeroDivisionError, default=None)
def foo(...):
    ...
```



