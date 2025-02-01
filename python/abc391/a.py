d = input()

if "N" in d:
    d = d.replace("N", "S")
else:
    d = d.replace("S", "N")

if "E" in d:
    d = d.replace("E", "W")
else:
    d = d.replace("W", "E")

print(d)
