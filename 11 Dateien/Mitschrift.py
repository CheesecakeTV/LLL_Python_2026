import os

print(os.listdir())

with open("Ablauf.md", "r", encoding="utf-8") as f: # read = lesen
    raw = f.read()

#print(raw)

test: bytes = b"Hallo Welt"
#print(test)

# with open("Test.txt", "wb") as f: # write = überschreiben
#     f.write(b"Hallo Welt")

with open("Test.txt", "a") as f:    # append = Anhängen
    f.write("\nHallo Welt")
