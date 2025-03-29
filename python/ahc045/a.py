def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    # 先頭から順番に読み取るためのイテレータを作る
    it = iter(input_data)

    N = int(next(it))  # 800
    M = int(next(it))  # グループ数
    Q = int(next(it))  # 最大クエリ数(400)
    L = int(next(it))  # クエリに含める都市数の上限(3~15)
    W = int(next(it))  # 長方形の幅・高さの最大値(500~2500)

    G = [int(next(it)) for _ in range(M)]  # 各グループの都市数

    # 各都市の長方形範囲 (lx_i, rx_i, ly_i, ry_i) を読み取り
    # TODO: これを使って都市間の距離を計算する
    rectangles = []
    for _ in range(N):
        lx = int(next(it))
        rx = int(next(it))
        ly = int(next(it))
        ry = int(next(it))
        rectangles.append((lx, rx, ly, ry))

    # ▼クエリを発行しないのでここで “!” を出力し、クエリパートを終了させる▼
    print("!")
    
    # ▼各グループの内容を出力する▼
    index_start = 0
    for size in G:
        # グループに属する都市
        group_cities = list(range(index_start, index_start + size))
        index_start += size
        
        # まずグループ内の都市一覧を出力 (スペース区切り)
        print(" ".join(map(str, group_cities)))
        
        # 次にグループ内を連結にするための辺を (size - 1) 本出力
        # 今は単に (i, i+1) の「鎖状」に繋ぐだけ
        for i in range(size - 1):
            print(group_cities[i], group_cities[i+1])

if __name__ == "__main__":
    solve()

