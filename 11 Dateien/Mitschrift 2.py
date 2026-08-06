from pathlib import Path

x = Path("../ordner/test/")
#x = Path("C://ordner/test/")
#x = x / "Test.txt"

#print(Path.home() / "Test")

#x.parent.mkdir(exist_ok=True, parents=True)    # Make directory
# x.write_text("Funktioniert!")

print(x.suffix)
print(x.name)
print(x.stem)
print(x.parent)
print(x)
print(x.with_name("Hallo.py"))
print(x.with_suffix(".png"))
print(x.anchor)

print(x.exists())
print(x.is_dir())   # is directory

# print(x.read_text())
# print(x.read_bytes())

# x.write_text()
# x.write_bytes()

