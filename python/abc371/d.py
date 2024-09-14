n = int(input())
x = list(map(int, input().split()))
p = list(map(int, input().split()))

xp = [(x[i], p[i]) for i in range(n)]
xp.sort(key=lambda x: x[0])

import bisect

cum_sum = [0 for _ in range(n+2)]
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + xp[i][1]

q = int(input())

import bisect

for _ in range(q):
    l, r = map(int, input().split())
    left = bisect.bisect_left(xp, (l, 0))
    right = bisect.bisect_right(xp, (r, 10 ** 10))

    if left == right:
        print(0)
    else:
        print(cum_sum[right] - cum_sum[left])

