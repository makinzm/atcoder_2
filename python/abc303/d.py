x,y,z = map(int,input().split())
s = input()

"""
素早く押すためには...?
- 数式で一発で計算できそう: 
  - A を押すには [shift] or [Caps状態 + 押す]
  - a を押すには [Caps状態 + shift] or [押す]
- Capsにするかどうかは初めに決めて仕舞えば良い気がする.. <- false
  - A A A a
    - [Caps] [a] [a] [a] [shift+a]
    - [shift+a] [shift+a] [shift+a] [a]
    - [shift+a] [shift+a] [shift+a] [Caps] [shift+a]
- むり

- 動的計画法?
  - dp[i][x]
    - i番目にCapsをしていてたどり着く最短の時間のこと。
"""

dp = [[-1 for _ in range(2)] for _ in range(len(s)+1)]

dp[0][0]=0
dp[0][1]=z

for i in range(1,len(s)+1):
    if s[i-1] == "a":
        dp[i][0] = min(dp[i-1][0] + x, dp[i-1][1] + z + x, dp[i-1][1] + y + z)
        dp[i][1] = min(dp[i-1][0] + y + z, dp[i-1][0] + z + y, dp[i-1][1] + y)
    elif s[i-1] == "A":
        dp[i][0] = min(dp[i-1][0] + y, dp[i-1][1] + z + y, dp[i-1][1] + x + z)
        dp[i][1] = min(dp[i-1][0] + x + z, dp[i-1][0] + z + x, dp[i-1][1] + x)

print(min(dp[len(s)][0],dp[len(s)][1]))
