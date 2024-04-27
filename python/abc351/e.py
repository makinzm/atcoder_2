n = int(input())

xy = []
for i in range(n):
    xy.append(list(map(int,input().split())))

ans = 0
for j in range(1, n):
    x,y = xy[j]
    for i in range(0, j):
        u,v = xy[i]
        u,v = u - x, v - y
        if (u+v) % 2 == 0:
            ans += max(abs(u), abs(v))

print(ans)
