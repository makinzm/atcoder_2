import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
edge = [[] for _ in range(n)]
for i in range(m):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append((v, b))
    edge[v].append((u, b))

def dijkstra_with_vertex_weights():
    dist = [float("inf")] * n
    dist[0] = a[0]
    pq = [(dist[0], 0)]

    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, b in edge[v]:
            new_dist = dist[v] + b + a[u]
            if new_dist < dist[u]:
                dist[u] = new_dist
                heapq.heappush(pq, (new_dist, u))

    for i in range(1, n):
        print(dist[i], end=" ")
    print()

dijkstra_with_vertex_weights()
