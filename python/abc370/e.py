debug = False
n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

mod = 998244353

# Use a dictionary to store non-zero values
dp = {a[0]: 1, 0: 1}

for i in range(1, n):
    new_dp = dp.copy()
    for j in dp:
        # Calculate dp[i + 1][j]
        new_dp[j + a[i]] = dp[j] + dp.get(j + a[i], 0)
        new_dp[j + a[i]] %= mod
    dp = new_dp
    if debug:
        print(f"{i=}, {dp=}")

all_patterns = 2 ** (n - 1) % mod

ans =(all_patterns - dp.get(k,0)) + mod * 2
ans %= mod

print(ans)

