
x = [[1]] * 5
print(x)

y = x.copy()

y[0][0] = 2 # Hier wird y verändert!
print(x)

