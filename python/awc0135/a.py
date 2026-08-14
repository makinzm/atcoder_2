n, r = map(int, input().split())
a = list(map(int, input().split()))

x = min(a) + r
ans = sum(a) + n * (r - x)

print(ans)
