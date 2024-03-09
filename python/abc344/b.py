a = []
while True:
    n = int(input())
    a.append(n)
    if n == 0:
        break

for a_i in a[::-1]:
    print(a_i)
