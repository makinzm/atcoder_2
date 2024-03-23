n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = (k * (k+1)) // 2

appear_set = set()

for i in range(n):
    if a[i] <= k:
        appear_set.add(a[i])

ans -= sum(appear_set)

print(ans)
