n = int(input())

for i in range(n+1):
    si = None
    for j in range(1,10):
        if n % j == 0:
            if i % (n/j) == 0:
                si = j
                break
    if si is None:
        si = "-"
    print(si,end="")
print()
