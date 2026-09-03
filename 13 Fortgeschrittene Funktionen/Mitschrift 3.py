
def ist_gerade(x: int) -> bool:
    return x % 2 == 0

x = [1,2,3,4,5,6,7,8,9]
y = list(map(lambda a: a**2, x))
z = list(filter(lambda a:a % 2 == 0, x))

#y = map(lambda a: -a, x)
x.sort(key= lambda a:-a)
x.sort(key= lambda a: abs(5 - a))
print(x)


