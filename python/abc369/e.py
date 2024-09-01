from more_itertools import distinct_permutations as permutations

debug = False

n,m = map(int, input().split())
bridges = []
for i in range(m):
    u, v, w = map(int, input().split())
    u, v = u-1, v-1
    bridges.append((u, v, w))

# answer the cost for any two islands using Warshall-Floyd algorithm
INF = 10**18
cost = [[INF]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0
for u, v, w in bridges:
    cost[u][v] = min(cost[u][v], w)
    cost[v][u] = min(cost[v][u], w)

if debug:
    for i in range(n):
        print(cost[i])

# O(n^3) = 64 * 10^6
for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# O(k) = 5
def solve(permutation, bridge_bit):
    ans = 0
    current = 0
    for j in range(len(permutation)):
        current_bridge = permutation[j]
        if bridge_bit >> j & 1:
            ans += cost[current][bridges[current_bridge][0]]
            current = bridges[current_bridge][1]
            ans += bridges[current_bridge][2]
        else:
            ans += cost[current][bridges[current_bridge][1]]
            current = bridges[current_bridge][0]
            ans += bridges[current_bridge][2]
        if debug:
            print(permutation, bridge_bit, j, current, ans)
    if current != n-1:
        ans += cost[current][n-1]
    if debug:
        print(f"answer: {ans=}, {permutation=}, {bridge_bit=}")
    return ans

q = int(input())
# O(q * k! * 2^k * k) = 3,000 * 120 * 32 * 5 = 57 * 10^6
for _ in range(q):
    k = int(input())
    must_bridge = list(map(lambda x: int(x)-1, input().split()))
    ans = INF
    for permutation in permutations(must_bridge):
        for bridge_bit in range(1 << k):
            ans = min(ans, solve(permutation, bridge_bit))
    print(ans)

