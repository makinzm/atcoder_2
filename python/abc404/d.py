import numpy as np

n, m = map(int, input().split())
c = list(map(int, input().split()))
_k_as = [list(map(int, input().split())) for _ in range(m)]

zoo_animals = [[] for _ in range(n)]
# O(n * m) = 1000
for i in range(m):
    k = _k_as[i][0]
    k_animals = _k_as[i][1:]
    for a in k_animals:
        zoo_animals[a - 1].append(i)

k_as = []
# O(n * m) = 1000
for ka in zoo_animals:
    animals = [0 for _ in range(m)]
    for a in ka:
        animals[a - 1] = 1
    k_as.append(np.array(animals))

k_as = np.array(k_as)

all_patterns_num = 3 ** n
ans = sum(c) * 2

# O(3^n * n) = 3^10 * 1000 = 6 * 10**7
for i in range(all_patterns_num):
    pattern = []
    for j in range(n):
        pattern.append(i % 3)
        i //= 3
    visited_num = np.zeros(m)
    for index, pat in enumerate(pattern):
        visited_num += pat * k_as[index]
    if np.all(visited_num > 1):
        cost = 0
        for index, pat in enumerate(pattern):
            cost += c[index] * pat
        ans = min(ans, cost)

print(ans)

