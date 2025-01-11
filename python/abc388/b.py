n,d = map(int, input().split())
tls = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,d+1):
    ans = 0
    for tl in tls:
        t,l = tl
        ans = max(ans, t*(l+i))
    print(ans)

