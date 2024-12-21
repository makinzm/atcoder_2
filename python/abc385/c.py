n = int(input())
h = list(map(int, input().split()))

dp = [[1] * n for _ in range(n)]
ans = 1

for i in range(n):
    for j in range(i+1,n):
        d = j - i
        if h[j] == h[i]:
            dp[j][d] = max(dp[j][d], dp[i][d] + 1)
            ans = max(ans, dp[j][d])

print(ans)
