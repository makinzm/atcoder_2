from collections import deque

t = input()
n_t = len(t)
n = int(input())
a = []
for _ in range(n):
    _a = input().split()
    a.append(_a[1:])

ans = 200

Q = deque()
# 0: how much, 1: what string is arrived
Q.append((0, 0))

while Q:
    _how_much, _now = Q.popleft()
    for i in range(n):
        for j, a_j in enumerate(a[i]):
            if a_j == t[n_t-_now-len(a_j):n_t-_now]:
                if _now + len(a_j) < n_t:
                    Q.append((_how_much+1, _now+len(a_j)))
                else:
                    ans = min(ans, _how_much+1)

print(ans if ans != 200 else -1)

