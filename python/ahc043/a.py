import sys
sys.setrecursionlimit(10**7)

# 定数
DO_NOTHING = -1
STATION    = 0
RAIL_HORIZONTAL = 1
RAIL_VERTICAL   = 2
RAIL_LEFT_DOWN  = 3
RAIL_LEFT_UP    = 4
RAIL_RIGHT_UP   = 5
RAIL_RIGHT_DOWN = 6

COST_STATION = 5000
COST_RAIL    = 100

DEBUG = True

def input():
    return sys.stdin.readline()

# 距離関数（問題文での通りマンハッタン距離）
def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def build_l_shaped_path(r0, c0, r1, c1):
    """
    家 (r0,c0) から職場 (r1,c1) へ、まず上下方向に一直線、
    それから左右方向に一直線で繋ぐL字経路を作る。
    戻り値は「(rail_type, r, c)」のリスト (駅を除くレール部分のみ)。
      - 駅は別途、最初と最後に STATION を置くことを想定
    """
    instructions = []
    # 垂直方向のレール敷設
    if r1 > r0:
        # 下に向かって
        for r in range(r0+1, r1):
            instructions.append((RAIL_VERTICAL, r, c0))
        # コーナー
        if c1 > c0:
            # 下 -> 右
            instructions.append((RAIL_RIGHT_UP, r1, c0))
        elif c1 < c0:
            # 下 -> 左
            instructions.append((RAIL_LEFT_UP, r1, c0))
    elif r1 < r0:
        # 上に向かって
        for r in range(r0-1, r1, -1):
            instructions.append((RAIL_VERTICAL, r, c0))
        # コーナー
        if c1 > c0:
            # 上 -> 右
            instructions.append((RAIL_RIGHT_DOWN, r1, c0))
        elif c1 < c0:
            # 上 -> 左
            instructions.append((RAIL_LEFT_DOWN, r1, c0))

    # 水平方向のレール敷設
    if c1 > c0:
        for c in range(c0+1, c1):
            instructions.append((RAIL_HORIZONTAL, r1, c))
    elif c1 < c0:
        for c in range(c0-1, c1, -1):
            instructions.append((RAIL_HORIZONTAL, r1, c))

    return instructions

def solve():
    N, M, K, T = map(int, input().split())
    homes = []
    works = []
    for _ in range(M):
        rs, cs, rt, ct = map(int, input().split())
        homes.append((rs, cs))
        works.append((rt, ct))

    # 今回は単純化のため、前半を建設 (build_phaseターン) に使い、
    # 後半 (collect_phaseターン) は待機＋全員の通勤という近似で計算する
    build_phase   = T // 2     # 前半
    collect_phase = T - build_phase  # 後半

    # 候補ユーザごとに
    #   dist   = マンハッタン距離
    #   cost   = 駅2 + レール(dist-1) 本ぶん
    #   revenue= collect_phase * dist
    #   profit = revenue - cost
    # を計算して格納
    candidates = []
    for i in range(M):
        dist = manhattan(homes[i], works[i])
        # 駅(2箇所) + レール(dist-1) の想定コスト
        cost = 2*COST_STATION + (dist-1)*COST_RAIL
        revenue = collect_phase * dist
        profit = revenue - cost
        # 一応、dist > 4 という制約は問題文にある通り
        # (既に満たされている想定だがチェックするなら dist>4)
        if profit > 0 and dist > 4:
            candidates.append((profit, i, dist, cost))

    # profitの大きい順にソート
    candidates.sort(key=lambda x: x[0], reverse=True)

    # ルートが被らないように用いるグリッド(駅やレールの占有フラグ)
    used = [[False]*N for _ in range(N)]
    
    actions = []   # (type, r, c) のリスト
    used_instructions = 0
    budget = K

    current_turn = 0

    for profit, idx, dist, cost in candidates:
        # これから建設するルートの全セルを取る
        if DEBUG:
            print(f"profit={profit}, idx={idx}, dist={dist}, cost={cost}", file=sys.stderr)
        (r0, c0) = homes[idx]
        (r1, c1) = works[idx]
        # L字レール
        rail_list = build_l_shaped_path(r0, c0, r1, c1)
        # 駅2つ + レールのセル数
        need_cells = len(rail_list) + 2  # 駅2個ぶん

        # 前半(build_phase)の残りターンに収まるか？
        if used_instructions + need_cells > T - current_turn:
            if DEBUG:
                print(f"Time limit exceeded:{current_turn=}, {used_instructions=}, {need_cells=}, {T=}", file=sys.stderr)
                continue
        # コストが足りるか？
        if budget < cost:
            if DEBUG:
                print(f"Budget limit exceeded:{current_turn=}, {budget=}, {cost=}", file=sys.stderr)
            continue

        # セル被り確認
        overlap = False
        # 駅(家)
        if used[r0][c0]:
            overlap = True
        # 駅(職場)
        if used[r1][c1]:
            overlap = True
        # レール
        for (tp, rr, cc) in rail_list:
            if used[rr][cc]:
                overlap = True
                break
        if overlap:
            continue

        # 使えるので確定
        # 駅とレールを actions に追加
        actions.append((STATION, r0, c0))       # 家の駅
        for (tp, rr, cc) in rail_list:
            actions.append((tp, rr, cc))       # レール
        actions.append((STATION, r1, c1))       # 職場の駅

        used[r0][c0] = True
        used[r1][c1] = True
        for (tp, rr, cc) in rail_list:
            used[rr][cc] = True

        used_instructions += need_cells
        budget -= cost
        current_turn += need_cells

    # 上で決まった分の建設命令を先頭に出力し、残りターンは -1 で埋める。
    # もし used_instructions が T を越える心配は上のロジックで除いているが一応ガード。
    result = []
    idx_action = 0
    while idx_action < len(actions) and idx_action < T:
        # 出力行動
        ttype, rr, cc = actions[idx_action]
        result.append(f"{ttype} {rr} {cc}" if ttype != DO_NOTHING else "-1")
        idx_action += 1

    # 余ったターンはすべて待機(-1)
    while len(result) < T:
        result.append("-1")

    print("\n".join(result))

if __name__ == "__main__":
    solve()


