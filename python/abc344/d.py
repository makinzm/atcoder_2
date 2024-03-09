t = input()
n_t = len(t)
n = int(input())
a = []
for _ in range(n):
    _a = input().split()
    a.append(_a[1:])

ans = 200

dp = [200 for _ in range(n_t + 1)]
dp[0] = 0

for i in range(n_t):
    for j in range(n):
        for ij in range(len(a[j])):
            if i + len(a[j][ij]) <= n_t and t[n_t - i - len(a[j][ij]):n_t - i] == a[j][ij]:
                dp[i + len(a[j][ij])] = min(dp[i + len(a[j][ij])], dp[i] + 1)

print(dp[n_t] if dp[n_t] < 200 else -1)
