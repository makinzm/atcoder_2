a = int(input())

n = a * 2 + 1

s = ""
for i in range(n):
    if i % 2 == 0:
        s += "1"
    else:
        s += "0"

print(s)

