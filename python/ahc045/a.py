def flush_print(*args, **kwargs):
    """flush=True で標準出力に出力するヘルパー関数"""
    print(*args, **kwargs, flush=True)

def create_groups(N, M, G, rectangles):
    """
    - N: 都市数
    - M: グループ数
    - G: グループごとの都市数 G[0], ..., G[M-1]
    - rectangles: 都市 i の (lx_i, rx_i, ly_i, ry_i) タプル
    
    返り値:
        groups: 長さ M のリスト。
                groups[k] はグループ k に属する都市番号リスト。
    """
    # 1) 各都市 i の中心座標を計算
    #    (単純に (lx+rx)/2, (ly+ry)/2 の浮動小数でOK)
    centers = []
    for i in range(N):
        lx, rx, ly, ry = rectangles[i]
        cx = (lx + rx) / 2
        cy = (ly + ry) / 2
        centers.append((cx, cy, i))
    
    # 2) ソート: ここでは (cx+cy) が小さい順で並べてみる
    centers.sort(key=lambda x: (x[0] + x[1]))
    
    # 3) ソート後の順に、G[0], G[1], ... 個ずつ区切ってグループ化
    groups = []
    idx = 0
    for k in range(M):
        gsize = G[k]
        sub = centers[idx: idx + gsize]
        idx += gsize
        # sub の中から都市番号だけを取り出す (i)
        group_cities = [t[2] for t in sub]
        groups.append(group_cities)
    
    return groups

def order_fortune(groups, Q, L, input_func):
    """
    - groups: create_groupsで得られた [ [都市群], [都市群], ... ] のリスト
    - Q: クエリ可能回数の上限
    - L: クエリで占える最大都市数
    - input_func: 占いの応答を受け取るための関数 (実際のジャッジでは input() 相当)
    
    返り値:
        group_mst_edges: 各グループの MST 辺のリスト( (a,b) のタプルの列 )。
                         group_mst_edges[i] は groups[i] 内で構成した辺たち。
    """
    group_mst_edges = [[] for _ in range(len(groups))]
    
    # グループごとに占いする or チェーンにする
    for i, cities in enumerate(groups):
        size = len(cities)
        if size <= L and Q > 0:
            # --- 占いクエリを発行 ---
            flush_print("?", size, *cities)
            
            # --- MST (size-1本) を標準入力から受け取る ---
            edges = []
            for _ in range(size - 1):
                # WARNING: Judge の 入力を受け取る部分
                a, b = map(int, input_func().split())
                edges.append((a, b))
            
            group_mst_edges[i] = edges
            
            Q -= 1  # クエリを1回消費した
        else:
            # --- サイズが大きい or Q切れ → チェーンで繋ぐ ---
            chain_edges = []
            for j in range(size - 1):
                chain_edges.append((cities[j], cities[j+1]))
            group_mst_edges[i] = chain_edges
    
    return group_mst_edges

def solve():
    # 1行目: N, M, Q, L, W
    N, M, Q, L, W = map(int, input().split())
    
    # 2行目: G (グループごとの都市数)
    G = list(map(int, input().split()))
    
    # 続く N 行: 各都市の (lx_i, rx_i, ly_i, ry_i)
    rectangles = []
    for _ in range(N):
        lx, rx, ly, ry = map(int, input().split())
        rectangles.append((lx, rx, ly, ry))
   
    groups = create_groups(N, M, G, rectangles)
    group_mst_edges = order_fortune(groups, Q, L, input)

    # ▼ここで “!” を出力し、クエリパートを終了させる▼
    flush_print("!")

    # ▼各グループの内容を出力する▼
    index_start = 0
    for i, cities in enumerate(groups):
        # グループに属する都市たち
        flush_print(" ".join(map(str, cities)))
        # (size - 1) のエッジ (a, b) を出力
        for (a, b) in group_mst_edges[i]:
            flush_print(a, b)

if __name__ == "__main__":
    solve()

