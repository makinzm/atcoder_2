from heapq import heappop, heappush

n = int(input())

g = [[] for _ in range(n)]

for i in range(n-1):
    a, b, x = list(map(int, input().split()))
    x -= 1
    g[i].append((i+1, a))
    g[i].append((x, b))

def dijkstra(s, n, g):
    d = [float('inf')] * n
    d[s] = 0
    q = [(0, s)]
    while q:
        _, u = heappop(q)
        for v, c in g[u]:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                heappush(q, (d[v], v))
    return d

print(dijkstra(0,n,g)[n-1])
