
x = [5, 2, 3, 7, 1, 1, 2, 6, 3, 54, 7, 2]#, [1,2,3]]
strings = ["Hallo", "Welt", "Discord", "hallo", "aaron"]

print(len(x))

print(5 in x)
print("Hal" in "Hallo")

print(sorted(x))
# x.sort()
# strings.sort()

print(x)
print(strings)

del x[2]

print(x.pop(-1))
print(x)

x[0] = 0
print(x)

print(x.index(2))
print(x.count(2))

print(x + [1, 2, 3])
x.append(6)
x.extend([1,2,3])
print(x)

print([1, 2] * 5)

print(x[1])
print(x[-1])

print(x[1:4])
print(x[1:])
print(x[:4])

print(x[1:10:2])
print(x[10:1:-1])
print(x[1:10][::-1])

x = "Hallo Welt"
print(x[0:5])
print(x[::-1])

# y = [[1,2,3], [4,5,6], [7,8,9]]
# y = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# y[1][0]
