n = int(input())
a = list(map(int, input().split()))

dp = [0, 0]

for i in range(n):
    not_battle_even = dp[0]
    not_battle_odd = dp[1]
    next_even = 0
    if i != 0:
        next_even = a[i] * 2 + dp[1]
    next_odd = a[i] + dp[0]
    dp = [max(not_battle_even, next_even), max(not_battle_odd, next_odd)]

print(max(dp))
