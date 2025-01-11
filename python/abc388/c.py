n = int(input())
a = list(map(int, input().split()))

last_one = n-2

ans = 0

for i in range(n-1, -1, -1):
    for j in range(last_one, -1, -1):
        if a[j] * 2 <= a[i]:
            ans += j + 1
            last_one = j
            break
        if j == 0:
            last_one = -1

print(ans)
