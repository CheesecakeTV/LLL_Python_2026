import dataclasses

def dieFkt(*args, hallo = 0, **kwargs):
    print(args)
    print(kwargs)

dieFkt(15, hallo="Welt", python="Kurs")

print([i ** 2 for i in range(10)])
print({i: i**2 for i in range(10)})

