x = input()

while True:
    if x[-1] == ".":
        x = x[:-1]
        break
    if x[-1] == "0":
        x = x[:-1]
    else:
        break

print(x)
