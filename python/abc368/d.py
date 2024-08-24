import sys

sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
targets = set(map(lambda x: int(x)-1, input().split()))

def minimize_subtree(v, p=-1):
    subtree_size = 1
    target_count = int(v in targets)

    for u in graph[v]:
        if u == p:
            continue
        child_size, child_count = minimize_subtree(u, v)
        if child_count > 0:
            subtree_size += child_size
            target_count += child_count

    if target_count == 0:
        return 0, 0

    return subtree_size, target_count

start_node = next(iter(targets))
result, _ = minimize_subtree(start_node)
print(result)

