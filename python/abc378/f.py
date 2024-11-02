def count_valid_edges(n, uv_list):
    from collections import defaultdict, deque
    import itertools

    # 隣接リストの構築
    adj_list = defaultdict(list)
    for u, v in uv_list:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # 各頂点の次数を計算
    degrees = {i: len(adj_list[i]) for i in range(1, n + 1)}

    # 次数が2の頂点のリストを作成
    degree_2_vertices = [v for v, deg in degrees.items() if deg == 2]

    # 条件を満たす辺の数をカウント
    count = 0
    for u, v in itertools.combinations(degree_2_vertices, 2):
        if not(degrees[u] + 1 == 3 and degrees[v] + 1 == 3):
            continue
        # uとvの間に辺を追加
        if v in adj_list[u]:
            continue  # 既に辺が存在する場合はスキップ

        # BFSでuからvへのパスを探索し、閉路を検出
        queue = deque([(u, None)])  # (現在の頂点, 親頂点)
        visited = {u}
        parent = {u: None}
        found_cycle = False
        cycle_nodes = []

        while queue and not found_cycle:
            current, par = queue.popleft()
            for neighbor in adj_list[current]:
                if neighbor == par:
                    continue
                if neighbor == v:
                    # 閉路を検出
                    found_cycle = True
                    cycle_nodes = [v, current]
                    while current != u:
                        current = parent[current]
                        cycle_nodes.append(current)
                    break
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append((neighbor, current))

        if found_cycle:
            # 閉路内のすべての頂点の次数が3であるか確認
            cycle_nodes_excluded = set(cycle_nodes) - {u, v}
            # print(f"{u=}, {v=}, {cycle_nodes=}, {cycle_nodes_excluded=}")
            all_degree_three = all(degrees[node] == 3 for node in cycle_nodes_excluded)
            if all_degree_three:
                count += 1
        else:
            raise ValueError("No cycle found")

    return count

# 入力の受け取り
n = int(input())
uv_list = [list(map(int, input().split())) for _ in range(n - 1)]

# 結果の出力
print(count_valid_edges(n, uv_list))

