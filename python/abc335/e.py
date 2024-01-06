from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

graph = {}
for i in range(m):
    uv = list(map(int, input().split()))
    uv = [uv[0]-1, uv[1]-1]
    if uv[0] not in graph:
        graph[uv[0]] = [uv[1]]
    else:
        graph[uv[0]].append(uv[1])
    if uv[1] not in graph:
        graph[uv[1]] = [uv[0]]
    else:
        graph[uv[1]].append(uv[0])

visited = {}
for i in range(n):
    visited[i] = -1, set()

Q = deque()
Q.append((0, visited))
ans = [0]

while(len(Q) > 0):
    current_place, kinds = Q.popleft()
    kinds[current_place] = 0, kinds[current_place][1].union(set([a[current_place]]))
    if current_place == n-1:
        ans.append(len(kinds[current_place][1]))
    else:
        for i in graph[current_place]:
            if a[i] >= a[current_place] and kinds[i][0] == -1:
                kinds[i] = -1, kinds[current_place][1].union(set([a[current_place]]))
                Q.append((i, deepcopy(kinds)))

print(max(ans))
