n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

b_index = 0
ans = 0

for i in range(n):
    if a[i] >= b[b_index]:
        ans += a[i]
        b_index += 1
    if b_index == m:
        break

if b_index == m:
    print(ans)
else:
    print(-1)

