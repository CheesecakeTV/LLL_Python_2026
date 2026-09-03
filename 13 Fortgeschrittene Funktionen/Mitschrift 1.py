from typing import Generator, Iterable, Any

def gib_quadrate() -> Generator[int, None, None]:
    i = 0
    while True:
        yield i ** 2
        i += 1

def print_iterable(der_iterable: Iterable[Any]):
    for i in der_iterable:
        print(i)

def range_unendlich(n: int):
    for k in range(n):
        yield from range(n)
        # for i in range(n):
        #     yield i

print_iterable(range_unendlich(5))

# for i in gib_quadrate():
#     if i == 100 ** 2:
#         break
#
#     print(i)



