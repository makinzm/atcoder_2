import sys
sys.setrecursionlimit(10**7)
from collections import deque

def compute_score(n, parent, a):
    """
    親配列 parent[v] によって構築される根付き森のスコア:
       sum_{v=0..n-1} ( (height(v)+1) * A[v] )
    を計算して返す。
    """
    children = [[] for _ in range(n)]
    for v in range(n):
        p = parent[v]
        if p != -1:
            children[p].append(v)
    
    visited = [False]*n
    score = 0
    
    # 各 root から BFS して高さを求め、スコア加算
    for v in range(n):
        if parent[v] == -1:  # root
            queue = deque([(v,0)])  # (頂点, 高さ)
            visited[v] = True
            score += (0 + 1)*a[v]
            while queue:
                cur, h = queue.popleft()
                for nxt in children[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        nh = h+1
                        score += (nh+1)*a[nxt]
                        queue.append((nxt, nh))
    return score


def build_forest_with_ratio(n, m, H, a, adj, r):
    """
    ratio = r のとき、
      - 深さ d < floor(r*H) までは「Aが小さい順」に子を優先。
      - 深さ d >= floor(r*H) からは「Aが大きい順」に子を優先。
    という DFS を、"Aが小さい順" の頂点を root として始める形で構築する。
    
    戻り値: parent[v] (vがrootなら -1)
    """

    parent = [-1]*n
    visited = [False]*n
    
    # まず頂点を "美しさが小さい順" に並べる
    order = sorted(range(n), key=lambda x: a[x])
    
    # 隣接リスト自体は両方の順序を使う可能性があるので、
    # ここではあえてソートせずに、DFS内で動的にソートする。
    
    limit_depth_switch = int(r * H)  # ここで深さの切り替えを行う（小数を含む場合切り捨て）
    
    def dfs(cur, depth):
        if depth == H:
            return
        # 今の深さ < limit_depth_switch => A小さい順
        # 今の深さ >= limit_depth_switch => A大きい順
        if depth < limit_depth_switch:
            neighbors = sorted(adj[cur], key=lambda x: a[x])  # 小さい順
        else:
            neighbors = sorted(adj[cur], key=lambda x: a[x], reverse=True)  # 大きい順
        
        for nxt in neighbors:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = cur
                dfs(nxt, depth+1)
    
    for v in order:
        if not visited[v]:
            visited[v] = True
            parent[v] = -1  # root
            dfs(v, 0)
    
    return parent


def solve():
    input = sys.stdin.readline
    n, m, H = map(int, input().split())
    a = list(map(int, input().split()))
    uvs = [list(map(int, input().split())) for _ in range(m)]
    xys = [list(map(int, input().split())) for _ in range(n)]
    
    # 隣接リスト
    adj = [[] for _ in range(n)]
    for u, v in uvs:
        adj[u].append(v)
        adj[v].append(u)
    
    # 試す ratio のリスト
    ratio_list = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
    
    best_score = -1
    best_parent = None
    
    for r in ratio_list:
        # 親配列を構築
        parent_candidate = build_forest_with_ratio(n, m, H, a, adj, r)
        sc = compute_score(n, parent_candidate, a)
        if sc > best_score:
            best_score = sc
            best_parent = parent_candidate
            print(" ".join(map(str, best_parent)))

if __name__ == "__main__":
    solve()

