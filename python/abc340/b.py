q = int(input())

a = {}
p = 0
for _ in range(q):
    t,x = list(map(int, input().split()))
    if t == 1:
        a[p] = x
        p += 1
    else:
        print(a[len(a)-x])
