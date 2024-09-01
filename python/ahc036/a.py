# get input
N, M, T, L_A, L_B = map(int, input().split())

G = [[] for _ in range(N)]

# Warshefloyd
print("# Warshefloyd")
cost = [[10**18] * N for _ in range(N)]
for i in range(N):
    cost[i][i] = 0

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    cost[u][v] = min(cost[u][v], 1)
    cost[v][u] = min(cost[v][u], 1)

print("# Calculate cost")

for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

print("# Calculate cost done")

t = list(map(int, input().split()))

P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

all_pathes = []

pos_from = 0

for pos_to in t:

    # determine the path by DFS
    path = []
    visited = [False] * N

    def dfs(cur, prev):
        if visited[cur]:
            return False

        if cur != pos_from:
            path.append(cur)

        visited[cur] = True
        if cur == pos_to:
            return True

        # visit next city in ascending order of Euclidean distance to the target city
        for v in sorted(G[cur], key=lambda x: cost[x][pos_to]):
            if v == prev:
                continue
            if dfs(v, cur):
                return True
        path.pop()
        return False

    dfs(pos_from, -1)

    all_pathes += path
    pos_from = pos_to

# construct and output the array A
A = [-1 for _ in range(L_A)]
where_u = {}
count = 0
for i, u in enumerate(all_pathes):
    if not u in where_u:
        where_u[u] = count
        A[count] = u
        count += 1
if count < L_A:
    A[count:] = all_pathes[-(L_A - count):]

assert not -1 in A

print("#", all_pathes)
print(*A)

current_b = [-1 for _ in range(L_B)]
for next_u in all_pathes:
    if not next_u in current_b:
        index_u = where_u[next_u]
        remain_a = min(L_B, L_A - index_u)
        print("s", remain_a, index_u, 0)
        index_u = where_u[next_u]
        current_b = A[index_u:index_u + remain_a] + current_b[remain_a:]
    print("#", current_b)
    print("m", next_u)

