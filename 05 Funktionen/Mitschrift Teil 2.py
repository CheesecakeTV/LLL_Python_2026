from typing import Any

def strip(derString: str) -> Any: #str | None:
    """
    Wendet .strip auf derString an

    :param derString: String der gestrippt werden soll
    :return:
    """
    assert isinstance(derString, str)
    if not derString:
        return None

    return derString.strip()

def cast(o: Any, derTyp: type) -> Any:
    assert not isinstance(o, str)

    # if isinstance(o, str):
    #     print("String:", o)

    return derTyp(o)

def fib(n: int) -> int:
    if n < 2:   # Verankerung
        return n

    return fib(n - 1) + fib(n - 2)  # Rekursionsschritt

print(fib(40))

