n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(1, n+1):
    for j in range(2*n-2):
        if a[j] == i and a[j+2] == i:
            ans += 1

print(ans)

