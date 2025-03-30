import sys
import math
import random
import numpy as np
import os

def setup_seed(seed):
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    random.seed(seed)
    
seed = 42
setup_seed(seed)

def constrained_kmeans(points, G, max_iter=20):
    """
    Constrained K-Means (簡易版) 
      - points: shape (N, 2) の numpy配列
      - G: 長さMの配列 [G_0, G_1, ..., G_{M-1}] 
           それぞれのクラスタが収容できる最大サイズ
           合計は N 以上を想定 (合計 == N なら全てぴったり埋める形になる)
      - max_iter: 割り当て反復回数の上限

    返り値:
      assignments: 長さN の配列 (各点が属するクラスタ番号 0..M-1)
      centers: shape (M,2) の配列 (各クラスタ中心)
    """
    N = len(points)
    M = len(G)
    G = np.array(G)

    # --- k-means++ 初期中心選択 ---
    # 1) 1つ目の中心をランダムに
    idx0 = random.randint(0, N-1)
    centers = [points[idx0].copy()]
    # 2) 残り M-1 個を k-means++ 距離²比で選ぶ
    dist_sq = np.sum((points - centers[0])**2, axis=1)
    for _ in range(M-1):
        prob = dist_sq / dist_sq.sum()
        chosen = np.random.choice(N, p=prob)
        centers.append(points[chosen].copy())
        new_dist_sq = np.sum((points - points[chosen])**2, axis=1)
        dist_sq = np.minimum(dist_sq, new_dist_sq)
    centers = np.array(centers, dtype=float)

    # --- 割り当て配列(最初は -1 で未割当とする) ---
    assignments = np.full(N, -1, dtype=int)

    # --- 反復 ---
    for iter_num in range(max_iter):
        changed = False

        # 1) 全クラスタを空にして容量カウンタもリセット
        cluster_sizes = np.zeros(M, dtype=int)
        assignments[:] = -1

        # 2) 各点を割り当て (「近い中心から試し、容量が余っていれば割り当て」)
        #    ※ 点をランダム順序で走査したほうが局所解を逃れやすい場合もある
        order = np.arange(N)
        np.random.shuffle(order)

        # まず距離をまとめて計算しておく: shape (N,M)
        # d2[i,k] = 点 i と centers[k] の距離²
        d2 = np.sum((points[:, None, :] - centers[None, :, :])**2, axis=2)

        for i in order:
            # 近いクラスタ k 順に試す
            idxs = np.argsort(d2[i])  # k のリスト
            assigned = False
            for k in idxs:
                if cluster_sizes[k] < G[k]:
                    # 容量OKなので割り当て
                    assignments[i] = k
                    cluster_sizes[k] += 1
                    assigned = True
                    break
            if not assigned:
                # 全クラスタ満杯の場合 → 仕方なく「最も近いクラスタidxs[0]」に入れる
                # (厳密制限を破るが、実際にはどうするか要検討)
                forced = idxs[0]
                assignments[i] = forced
                cluster_sizes[forced] += 1
                # G[forced] を破る可能性がある

        # 3) centers を再計算
        new_centers = np.zeros_like(centers)
        count = np.zeros(M, dtype=int)
        for i in range(N):
            k = assignments[i]
            new_centers[k] += points[i]
            count[k] += 1
        for k in range(M):
            if count[k] > 0:
                new_centers[k] /= count[k]
            else:
                # もし空クラスタなら、ランダムに割り当て直すなど対策
                new_centers[k] = centers[k]  # 変化なし

        # 4) 収束判定
        dist_shift = np.sqrt(np.sum((centers - new_centers)**2))
        if dist_shift > 1e-7:
            changed = True
        centers = new_centers

        if not changed:
            break

    return assignments, centers

# 動作デモ用（クラスタサイズが厳密 G[k] の場合は最終微調整が要る）

def fix_cluster_sizes(points, assignments, centers, G):
    """
    "最大" G[k] ではなく、"厳密" に G[k] のサイズにしたい場合は、
    過剰クラスタ > 不足クラスタへ点を移動して微調整する。
    (ヒューリスティック実装の一例)
    """
    M = len(G)
    N = len(assignments)
    cluster_sizes = np.zeros(M, dtype=int)
    for k in range(M):
        cluster_sizes[k] = np.sum(assignments == k)

    # 同様に "fix_assignments" 的に調整
    max_iter = 10
    for _ in range(max_iter):
        over = np.where(cluster_sizes > G)[0]
        under = np.where(cluster_sizes < G)[0]
        if len(over)==0 or len(under)==0:
            break
        for i in over:
            surplus = cluster_sizes[i] - G[i]
            if surplus <= 0:
                continue
            i_idx = np.where(assignments == i)[0]
            # iクラスタ内の点を "最も近い不足クラスタ" に移す
            for j in under:
                needed = G[j] - cluster_sizes[j]
                if needed <= 0:
                    continue
                if surplus <= 0:
                    break
                move_count = min(surplus, needed)

                # i_idx のうち、centers[j] に近い順に move_count個だけ j に移す
                d2 = np.sum((points[i_idx] - centers[j])**2, axis=1)
                sort_idx = np.argsort(d2)
                to_move = i_idx[sort_idx[:move_count]]

                # 移動
                assignments[to_move] = j
                cluster_sizes[i] -= move_count
                cluster_sizes[j] += move_count
                surplus -= move_count

                # centers も再計算 (i, j)
                for c in [i, j]:
                    pts_c = points[assignments == c]
                    if len(pts_c) > 0:
                        centers[c] = pts_c.mean(axis=0)
            if surplus <= 0:
                continue

    return assignments, centers


def query(c):
    print("?", len(c), *c, flush=True)
    return [tuple(map(int, input().split())) for _ in range(len(c) - 1)]


def answer(groups, edges):
    print("!")
    for i in range(len(groups)):
        print(*groups[i])
        for e in edges[i]:
            print(*e)


# read input
N, M, Q, L, W = map(int, input().split())
G = list(map(int, input().split()))
lx, rx, ly, ry = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    lx.append(a)
    rx.append(b)
    ly.append(c)
    ry.append(d)

# use center of rectangle
x = [(l + r) // 2 for l, r in zip(lx, rx)]
y = [(l + r) // 2 for l, r in zip(ly, ry)]

# split cities into groups

centers = np.array(list(zip(x, y)))
assignments, centers = constrained_kmeans(centers, G)
assignments, centers = fix_cluster_sizes(centers, assignments, centers, G)
groups = [[] for _ in range(M)]
for i in range(N):
    groups[assignments[i]].append(i)

# cities = list(range(N))
# cities.sort(key=lambda i: (x[i], y[i]))

# groups = []
# start_idx = 0
# for g in G:
#     groups.append(cities[start_idx : start_idx + g])
#     start_idx += g

# get edges from queries
edges = []
for k in range(M):
    gcities = groups[k]
    gsize = len(gcities)
    if gsize <= L and Q > 0 and gsize >= 2:
        ret = query(gcities)
        edges.append(ret)
        Q -= 1
    else:
        chain = []
        for i in range(gsize - 1):
            chain.append((gcities[i], gcities[i + 1]))
        edges.append(chain)

# output answer
answer(groups, edges)


