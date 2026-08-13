import json
#from pprint import pprint

x = [list(range(i)) for i in range(10)]

print(x)
mein_str = json.dumps(x, indent=4)

print(mein_str)

y = json.loads(mein_str)
print(y)

#pprint(x)

