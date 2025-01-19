from collections import deque

def solve():
    n, m, H = map(int, input().split())
    a = list(map(int, input().split()))
    uvs = [list(map(int, input().split())) for _ in range(m)]
    xys = [list(map(int, input().split())) for _ in range(n)]
    
    adj = [[] for _ in range(n)]
    for u, v in uvs:
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * n
    visited = [False] * n

    for start in range(n):
        if not visited[start]:
            queue = deque()
            queue.append((start, 0))
            visited[start] = True
            parent[start] = -1

            while queue:
                cur, depth = queue.popleft()
                if depth == H:
                    continue
                for nxt in adj[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        parent[nxt] = cur
                        queue.append((nxt, depth + 1))

    print(" ".join(map(str, parent)))

if __name__ == "__main__":
    solve()

