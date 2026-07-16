
x = []

for i in range(10):
    if i % 2 == 0:
        x.append(i ** 2)
    else:
        x.append("?")

print(x)


#y = [i ** 2 for i in range(10)]
#y = [i ** 2 for i in range(10) if i % 2 == 0]
y = [i ** 2 if i % 2 == 0 else "?" for i in range(10)]
print(y)

