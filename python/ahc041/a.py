import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    # 入力
    n, m, H = map(int, input().split())
    a = list(map(int, input().split()))
    uvs = [list(map(int, input().split())) for _ in range(m)]
    xys = [list(map(int, input().split())) for _ in range(n)]
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for u, v in uvs:
        adj[u].append(v)
        adj[v].append(u)
    # 各頂点の隣接を、美しさが「小さい順」にソートしておく
    # → DFS で「小さいAの頂点」を先に探索し、大きいAの頂点を後回しにする
    for v in range(n):
        adj[v].sort(key=lambda x: a[x])
    parent = [-1]*n
    visited = [False]*n
    # 深さ制限付きDFS
    def dfs(cur, depth):
        if depth == H:
            return
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = cur
                dfs(nxt, depth + 1)
    # 美しさの小さい順に頂点を並べる
    # → この順番で「未訪問なら root として DFS」を始める
    #    ⇒ root はなるべく美しさの小さい頂点に
    order = sorted(range(n), key=lambda x: a[x])
    for v in order:
        if not visited[v]:
            visited[v] = True
            parent[v] = -1
            dfs(v, 0)
    print(" ".join(map(str, parent)))

if __name__ == "__main__":
    solve()

