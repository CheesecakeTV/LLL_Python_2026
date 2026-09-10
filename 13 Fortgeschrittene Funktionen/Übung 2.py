from typing import Iterable, Callable, Generator, Any, TypeVar

def meineFkt(_: str):
    return "Hallo"

inner_obj = TypeVar("inner_obj")
def mapGen(f: Callable[[inner_obj], Any], obj: Iterable[inner_obj]) -> Generator[Any, None, None]:
    for i in obj:
        yield f(i)

def filterGen(f: Callable, obj: Iterable[inner_obj]) -> Generator[inner_obj, None, None]:
    for i in obj:
        if f(i):
            yield i

def enumerateGen(obj: Iterable) -> Generator[tuple[int, Any], None, None]:
    zahler = 0
    for i in obj:
        yield zahler, i
        zahler += 1

def zipGen(obj1: Iterable, obj2: Iterable) -> Generator[tuple[Any, Any], None, None]:
    obj1, obj2 = iter(obj1), iter(obj2)

    while True:
        try:
            yield next(obj1), next(obj2)
        except StopIteration:
            return

def enumerateZipGen(obj1: Iterable, obj2: Iterable) -> Generator[tuple[int, tuple[Any, Any]]]:
    #yield from enumerateGen(zipGen(obj1, obj2))
    return enumerateGen(zipGen(obj1, obj2))

x = [1,2,3,4]
y = [5,6,7,8,9,10]

for index, (n, i) in enumerateZipGen(x, y):
    print(index, n, i)

x = filterGen(lambda a: a % 2 != 0, x)

print(list(x))

