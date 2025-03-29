def flush_print(*args, **kwargs):
    """flush=True で標準出力に出力するヘルパー関数"""
    print(*args, **kwargs, flush=True)

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
    
    # ▼クエリを発行しないのでここで “!” を出力し、クエリパートを終了させる▼
    flush_print("!")

    # ▼各グループの内容を出力する▼
    #   単純に都市を 0,1,2,... の順番で切り分け、同じグループ内は
    #   鎖状につなぐだけ。
    index_start = 0
    for size in G:
        # グループに属する都市
        group_cities = list(range(index_start, index_start + size))
        index_start += size
        
        # まずグループ内の都市一覧を1行で出力 (スペース区切り)
        flush_print(" ".join(map(str, group_cities)))
        
        # 次にグループ内を連結にするための辺を (size - 1) 本出力
        # 今は (i, i+1) のチェーン(鎖)構造で接続しているだけ
        for i in range(size - 1):
            flush_print(group_cities[i], group_cities[i+1])

if __name__ == "__main__":
    solve()

