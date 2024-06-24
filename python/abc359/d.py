n, k = map(int, input().split())
s = input()

dp = [[0] * 2 ** k for _ in range(n+1)]
mod = 998244353

if s[0] == "A":
    dp[1][0] = 1
elif s[0] == "B":
    dp[1][1] = 1
elif s[0] == "?":
    dp[1][0] = 1
    dp[1][1] = 1

def is_palindrome(s_bit):
    # たかだか k 桁のビット列 s_bit が回文かどうかを判定する
    ss = ""
    for i in range(k):
        if s_bit & (1 << i):
            ss += "B"
        else:
            ss += "A"
    return ss == ss[::-1]

debug = False
for i in range(2, n+1):
    if debug:
        print("i:", i)
        print("dp", dp[i-1])
    if i < k:
        for j in range(2 ** i):
            if s[i-1] == "A":
                dp[i][j<<1] += dp[i-1][j]
            elif s[i-1] == "B":
                dp[i][(j<<1) + 1] += dp[i-1][j]
            elif s[i-1] == "?":
                dp[i][j<<1] += dp[i-1][j]
                dp[i][(j<<1) + 1] += dp[i-1][j]
    else:
        for j in range(2 ** k):
            if dp[i-1][j] == 0:
                continue
            if s[i-1] == "A":
                next_j = (j << 1) & ((1 << k) - 1)
                if is_palindrome(next_j):
                    dp[i][next_j] = 0
                else:
                    dp[i][next_j] += dp[i-1][j]
                    dp[i][next_j] %= mod
            elif s[i-1] == "B":
                next_j = ((j << 1) + 1) & ((1 << k) - 1)
                if is_palindrome(next_j):
                    dp[i][next_j] = 0
                else:
                    dp[i][next_j] += dp[i-1][j]
                    dp[i][next_j] %= mod
            elif s[i-1] == "?":
                next_j_a = (j << 1) & ((1 << k) - 1)
                next_j_b = ((j << 1) + 1) & ((1 << k) - 1)
                if is_palindrome(next_j_a):
                    dp[i][next_j_a] = 0
                else:
                    dp[i][next_j_a] += dp[i-1][j]
                    dp[i][next_j_a] %= mod
                if is_palindrome(next_j_b):
                    dp[i][next_j_b] = 0
                else:
                    dp[i][next_j_b] += dp[i-1][j]
                    dp[i][next_j_b] %= mod

print(sum(dp[n]) % mod)

