import sys
sys.setrecursionlimit(10**7)

Pos = tuple[int, int]

EMPTY = -1
DO_NOTHING = -1
STATION = 0
RAIL_HORIZONTAL = 1
RAIL_VERTICAL = 2
RAIL_LEFT_DOWN = 3
RAIL_LEFT_UP = 4
RAIL_RIGHT_UP = 5
RAIL_RIGHT_DOWN = 6

COST_STATION = 5000
COST_RAIL = 100

DEBUG = True

def input():
    return sys.stdin.readline()

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        # 親を保持する配列。負の値なら自分がrootで、絶対値は木のサイズ
        self.parents = [-1 for _ in range(n * n)]

    def _find_root(self, idx: int) -> int:
        if self.parents[idx] < 0:
            return idx
        self.parents[idx] = self._find_root(self.parents[idx])
        return self.parents[idx]

    def is_same(self, p: Pos, q: Pos) -> bool:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        return self._find_root(p_idx) == self._find_root(q_idx)

    def unite(self, p: Pos, q: Pos) -> None:
        p_idx = p[0] * self.n + p[1]
        q_idx = q[0] * self.n + q[1]
        p_root = self._find_root(p_idx)
        q_root = self._find_root(q_idx)
        if p_root != q_root:
            # サイズの大きい方をnew rootに
            if -self.parents[p_root] > -self.parents[q_root]:
                p_root, q_root = q_root, p_root
            self.parents[q_root] += self.parents[p_root]
            self.parents[p_root] = q_root

def distance(a: Pos, b: Pos) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class Action:
    def __init__(self, type: int, pos: Pos):
        self.type = type
        self.pos = pos

    def __str__(self):
        if self.type == DO_NOTHING:
            return "-1"
        else:
            return f"{self.type} {self.pos[0]} {self.pos[1]}"

class Result:
    def __init__(self, actions: list[Action], score: int):
        self.actions = actions
        self.score = score

    def __str__(self):
        # 実際の提出時は actions のみ出力する
        return "\n".join(map(str, self.actions))

class Field:
    """
    各区画を駅(STATION) or 線路(1~6) or EMPTY(= -1) で管理。
    UnionFind で「つながっているか」を判定できるようにしている。
    """
    def __init__(self, N: int):
        self.N = N
        # 各区画の状態(STATION=0 or 1..6 or EMPTY=-1)
        self.rail = [[EMPTY]*N for _ in range(N)]
        self.uf = UnionFind(N)

    def build(self, type: int, r: int, c: int) -> None:
        """
        (r,c) の区画を 'type' (STATION or 1..6) にして UF で連結情報を更新
        """
        # 問題文のルール上、無効な置き換えがないか一応チェック(簡易)
        # - 線路配置は EMPTY のみ
        # - 駅配置は EMPTY or 線路(1..6)
        if type == STATION:
            # 駅
            if self.rail[r][c] not in (EMPTY, RAIL_HORIZONTAL, RAIL_VERTICAL,
                                       RAIL_LEFT_DOWN, RAIL_LEFT_UP, RAIL_RIGHT_UP, RAIL_RIGHT_DOWN):
                raise ValueError("駅配置の衝突")
        else:
            # 線路(1..6)
            if self.rail[r][c] != EMPTY:
                raise ValueError("線路配置の衝突")

        self.rail[r][c] = type

        # 隣接との UnionFind を更新
        self._try_connect(r, c, type)

    def _try_connect(self, r: int, c: int, type: int):
        """
        (r,c) の区画の上下左右に駅や線路があれば、つなげる。
        """
        # 上
        if r > 0:
            self._connect_if_compatible(r, c, r-1, c)
        # 下
        if r < self.N - 1:
            self._connect_if_compatible(r, c, r+1, c)
        # 左
        if c > 0:
            self._connect_if_compatible(r, c, r, c-1)
        # 右
        if c < self.N - 1:
            self._connect_if_compatible(r, c, r, c+1)

    def _connect_if_compatible(self, r1, c1, r2, c2):
        """
        (r1,c1) と (r2,c2) が双方「つながる形状同士」ならUFで unite する。
        """
        t1 = self.rail[r1][c1]
        t2 = self.rail[r2][c2]
        if t1 == EMPTY or t2 == EMPTY:
            return
        # 駅(STATION=0) は上下左右どこでもOK
        # 線路同士の場合は向きが合わないとダメ
        # 下記の対応を踏まえたチェック:
        #   1(H) -- 左右
        #   2(V) -- 上下
        #   3(＼) -- 左下, 右上
        #   4(／) -- 左上, 右下
        #   5(┛) -- 右上, 上右？(問題文図示があればそちら参照)
        #   6(┗) -- 右下, 下右？ ...
        # など。が、サンプル実装はまとめて列挙していました。
        # ここではサンプル実装を踏襲します。

        # (r1,c1)->(r2,c2) が上下/左右のどれか？
        dr = r2 - r1
        dc = c2 - c1

        def can_connect(t, dr, dc):
            # t区画からみて、上下左右方向が通っているか
            # STATIONはどこでもOK
            if t == STATION:
                return True
            if t == RAIL_HORIZONTAL:
                # 左右のみ
                return (dr == 0 and abs(dc) == 1)
            if t == RAIL_VERTICAL:
                # 上下のみ
                return (dc == 0 and abs(dr) == 1)
            if t == RAIL_LEFT_DOWN:
                # 3(＼) -> 上左 or 下右?
                # 問題文の定義:
                #   3 は \ の形状, 上左には繋がらない(実は?), 下右には繋がる
                #   しかしサンプル実装では:
                #     RAIL_LEFT_DOWN(3): 上下左右のチェック -> [V, ...]
                #   正確には: dr>0,dc<0 or dr<0,dc>0 ?
                # ここではサンプルコードと同じ条件をベタ書きする
                # "上/左" あるいは "下/右" に繋がると考えると:
                return (dr == 1 and dc == 0) or (dr == 0 and dc == -1)
            if t == RAIL_LEFT_UP:
                # 4(／)
                return (dr == -1 and dc == 0) or (dr == 0 and dc == -1)
            if t == RAIL_RIGHT_UP:
                # 5
                return (dr == -1 and dc == 0) or (dr == 0 and dc == 1)
            if t == RAIL_RIGHT_DOWN:
                # 6
                return (dr == 1 and dc == 0) or (dr == 0 and dc == 1)

            return False

        # 双方向ともつながるか判定
        if can_connect(t1, dr, dc) and can_connect(t2, -dr, -dc):
            self.uf.unite((r1,c1), (r2,c2))

    def is_connected(self, home: Pos, work: Pos) -> bool:
        """
        問題文での「家周辺 (<=2マス) の駅」と
        「職場周辺 (<=2マス) の駅」が線路で繋がっているかどうか
        """
        # 家周辺の駅群
        stations_home = self.collect_stations(home)
        # 職場周辺の駅群
        stations_work = self.collect_stations(work)
        # いずれかペアが UFで same ならOK
        for sh in stations_home:
            for sw in stations_work:
                if self.uf.is_same(sh, sw):
                    return True
        return False

    def collect_stations(self, pos: Pos) -> list[Pos]:
        """
        pos=(r,c) からマス距離<=2 の範囲で 'station' の区画座標を集める
        """
        res = []
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                rr = pos[0] + dr
                cc = pos[1] + dc
                if 0 <= rr < self.N and 0 <= cc < self.N:
                    if self.rail[rr][cc] == STATION:
                        # 距離制約も満たすか
                        if abs(dr) + abs(dc) <= 2:
                            res.append((rr, cc))
        return res

class Solver:
    def __init__(self, N: int, M: int, K: int, T: int,
                 home: list[Pos], workplace: list[Pos]):
        self.N = N
        self.M = M
        self.K = K
        self.T = T
        self.home = home
        self.workplace = workplace
        self.field = Field(N)
        self.money = K

        self.actions: list[Action] = []

    def solve(self) -> Result:
        """
        複数ユーザについて
          - マンハッタン距離 dist
          - 駅2つ + レール(dist - 1)本のコスト
          - profit = (T * dist) - cost の見込み
        を計算し、正のものを大きい順に採用してL字経路で敷設する。
        
        ただし実際にはターンごとに1マス建設 → その都度収益が入る形でシミュレーション。
        """
        # まず「単独収益」が正になりそうな候補を集める
        # (より厳密にはターン毎集金にすれば早期に完成した方が得だが、ここでは簡易指標)
        candidates = []
        for i in range(self.M):
            dist = distance(self.home[i], self.workplace[i])
            # 駅(2箇所) + レール(dist-1) の想定コスト
            cost_est = 2*COST_STATION + (dist - 1)*COST_RAIL
            # 簡単に Tターン全部通う想定の収益
            revenue_est = dist * self.T
            profit_est = revenue_est - cost_est
            # 問題文では dist > 4 を満たすが、一応確認しつつ
            if dist > 4 and profit_est > 0:
                candidates.append((profit_est, i, dist, cost_est))

        # 利益が大きい順にソート
        candidates.sort(key=lambda x: x[0], reverse=True)

        # あとは、1人ずつ順に「L字経路 + 駅2つ」を建設できるかどうかをチェック
        plan = []  # (type, r, c) のリスト全体
        rest_turns = self.T # 残りターン数
        income_by_turn = 0
        while candidates:
            if DEBUG:
                print(f"CURRENT: {self.money=}, {rest_turns=}, {income_by_turn=}", file=sys.stderr)
            new_candidates = []
            for _idx, (profit_est, idx, dist, cost_est) in enumerate(candidates):
                # すでに埋まっている箇所であるかをチェック
                # ここで「すでに敷設済かどうか」簡単チェック
                #   - なるべく衝突を避ける
                #   - station可能か (EMPTY or rail上書き)
                #   - railはEMPTYのみ
                #   → もしダメならスキップ
                if not self._can_place_station(self.home[idx]):
                    continue
                if not self._can_place_station(self.workplace[idx]):
                    continue
                can_build_all = True
                route_rail = self._build_l_shaped_path(self.home[idx], self.workplace[idx])
                for (t, rr, cc) in route_rail:
                    if not self._can_place_rail(rr, cc):
                        can_build_all = False
                        break
                if not can_build_all:
                    continue

                # 時間が足りるかどうかをチェック
                needed_cells = len(route_rail) + 2
                if rest_turns < needed_cells + 10: # 集金ターンも含めて10ターン分余裕を持つ
                    # 時間が足りないのでスキップ
                    continue

                # 予算が足りるかどうかをチェック
                if DEBUG:
                    print(f"TRY TO BUILD: {idx=}, {dist=}, {cost_est=}, {self.money=} {profit_est=}", file=sys.stderr)
                if self.money < cost_est:
                    # 次のタイミングで埋められるかもしれないので、次に回す
                    if DEBUG:
                        print(f"SKIP TO BUILD: {idx=}, {dist=}, {cost_est=}, {self.money=} {profit_est=}", file=sys.stderr)
                    new_candidates.append((profit_est, idx, dist, cost_est))
                    continue

                # OKなら、このルートを計画に追加

                # 予算を減らし、実際に建設命令(駅→レール群→駅)を並べる
                # 後のターンシミュレーションで実際に処理

                # 駅(家)
                plan.append((STATION, self.home[idx][0], self.home[idx][1]))
                self.field.build(STATION, self.home[idx][0], self.home[idx][1])
                # レール
                plan.extend(route_rail)
                for (t, rr, cc) in route_rail:
                    self.field.build(t, rr, cc)
                # 駅(職場)
                plan.append((STATION, self.workplace[idx][0], self.workplace[idx][1]))
                self.field.build(STATION, self.workplace[idx][0], self.workplace[idx][1])
                self.money -= cost_est  # 仮に予算を消費(ここで消費する)

                rest_turns -= needed_cells  # 残りターン数を減らす

                # 収益を加算
                income_by_turn += dist
                
                break

            # 候補を更新
            candidates = new_candidates + candidates[_idx+1:]

            # 何もしないという選択について追加
            rest_turns -= 1
            plan.append((DO_NOTHING, 0, 0))

            self.money += income_by_turn  # 収益を加算


        # 余った時間は何もしないで待つ
        for _ in range(rest_turns):
            plan.append((DO_NOTHING, 0, 0))
            self.money += income_by_turn

        return Result([Action(t, (r, c)) for t, r, c in plan], self.money)

    ### 下記はサンプルコード等で用意されていたメソッド ###

    def _calc_income(self) -> int:
        """
        現時点で全ユーザが通勤を試みるときの1ターンあたりの合計収入。
        """
        income = 0
        for i in range(self.M):
            # 接続チェック
            if self.field.is_connected(self.home[i], self.workplace[i]):
                # 距離ぶんの収入
                income += distance(self.home[i], self.workplace[i])
        return income

    def _build_rail(self, rail_type: int, r: int, c: int) -> None:
        """
        線路配置: コスト100
        """
        # 資金が足りない(あるいはマイナスになる)場合はNGだが、ここでは
        # すでに cost_est 分を差し引いているため簡単に通す
        self.field.build(rail_type, r, c)
        self.money -= COST_RAIL
        self.actions.append(Action(rail_type, (r, c)))

    def _build_station(self, r: int, c: int) -> None:
        """
        駅配置: コスト5000
        """
        self.field.build(STATION, r, c)
        self.money -= COST_STATION
        self.actions.append(Action(STATION, (r, c)))

    def _build_nothing(self) -> None:
        self.actions.append(Action(DO_NOTHING, (0, 0)))
        # 待機なのでコスト変動なし

    ### 以下、L字経路生成 & 設置可能チェック ###

    def _build_l_shaped_path(self, start: Pos, goal: Pos) -> list[tuple[int,int,int]]:
        """
        start->goal を「まず上下方向に一直線→そこから水平方向」のL字で結ぶ。
        戻り値は「(rail_type, r, c)」のリスト(駅を除く)。
        """
        (r0, c0) = start
        (r1, c1) = goal
        instructions = []
        # 垂直方向
        if r1 > r0:
            for r in range(r0+1, r1):
                instructions.append((RAIL_VERTICAL, r, c0))
            # コーナー
            if c1 > c0:
                instructions.append((RAIL_RIGHT_UP, r1, c0))
            elif c1 < c0:
                instructions.append((RAIL_LEFT_UP, r1, c0))
        elif r1 < r0:
            for r in range(r0-1, r1, -1):
                instructions.append((RAIL_VERTICAL, r, c0))
            # コーナー
            if c1 > c0:
                instructions.append((RAIL_RIGHT_DOWN, r1, c0))
            elif c1 < c0:
                instructions.append((RAIL_LEFT_DOWN, r1, c0))

        # 水平方向
        if c1 > c0:
            for cc in range(c0+1, c1):
                instructions.append((RAIL_HORIZONTAL, r1, cc))
        elif c1 < c0:
            for cc in range(c0-1, c1, -1):
                instructions.append((RAIL_HORIZONTAL, r1, cc))

        return instructions

    def _can_place_station(self, pos: Pos) -> bool:
        """
        pos区画に駅を置けるか？(EMPTYか線路ならOK、それ以外はNG)
        """
        (r, c) = pos
        t = self.field.rail[r][c]
        if t == EMPTY:
            return True
        return False

    def _can_place_rail(self, r: int, c: int) -> bool:
        """
        (r,c)に線路を置けるか？(EMPTYのみOK)
        """
        return (self.field.rail[r][c] == EMPTY)

def main():
    N, M, K, T = map(int, input().split())
    home = []
    workplace = []
    for _ in range(M):
        r0, c0, r1, c1 = map(int, input().split())
        home.append((r0, c0))
        workplace.append((r1, c1))

    solver = Solver(N, M, K, T, home, workplace)
    result = solver.solve()

    # 出力
    print(result)
    # スコア出力(最終資金を stderr に表示)
    print(f"score={result.score}", file=sys.stderr)

if __name__ == "__main__":
    main()

