n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n)]
for a, b in edges:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def is_chain(graph):
    start = 0
    count = 0
    visited = [False] * len(graph)
    while True:
        if len(graph[start]) != 2:
            break
        visited[start] = True 
        is_decided_next = False
        for i in graph[start]:
            if not visited[i]:
                is_decided_next = True
                start = i
                break
        if not is_decided_next:
            break
        count += 1
    return count

graph_len = is_chain(graph)

if graph_len == n - 1:
    print("Yes")
else:
    print("No")

