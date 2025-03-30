import sys
sys.setrecursionlimit(10**8)

DEBUG = False

n, m = map(int, input().split())
uv = [ list(map(int, input().split())) for _ in range(m) ]

graph = [ [] for _ in range(n) ]

for i, uvi in enumerate(uv):
    graph[uvi[0]-1].append((uvi[1]-1, i))
    graph[uvi[1]-1].append((uvi[0]-1, i))

visited_edge = [ False for _ in range(m) ]
visited_node = [ False for _ in range(n) ]
ans = 0

def dfs(v):
    global ans
    for u, i in graph[v]:
        if visited_edge[i]:
            continue
        visited_edge[i] = True
        if visited_node[u]:
            ans += 1
            if DEBUG:
                print(f"edge {i+1} {uv[i]} should be removed")
            continue
        visited_node[u] = True
        dfs(u)
    visited_node[v] = True

for i in range(n):
    if visited_node[i]:
        continue
    if DEBUG:
        print(f"start from {i+1}")
    visited_node[i] = True
    dfs(i)

print(ans)

