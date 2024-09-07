n = int(input())
a = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

current = 0
for i in range(n):
    l, r = current, i
    if l < r:
        r, l = l, r

    try:
        current = a[l][r]
    except IndexError:
        print(a)
        print(i, current)
        print(l, r)
        raise IndexError

print(current + 1)

