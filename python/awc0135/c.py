n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dp = [ 0 for _ in range(m) ]
dp[0] = a[0][0]
for i in range(1, m):
    dp[i] = dp[i-1] + a[0][i]

for i in range(1, n):
    dp[0] += a[i][0]
    for j in range(1, m):
        dp[j] = max(dp[j-1], dp[j]) + a[i][j]

print(dp[m-1])
