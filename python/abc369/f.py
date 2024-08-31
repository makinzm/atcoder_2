from collections import defaultdict

def create_graph(points):
    points.sort()  # y座標を昇順、y座標が同じ場合はx座標を昇順にソート
    graph = defaultdict(list)

    prev_point = None
    min_dist = float('inf')
    for point in points:
        if prev_point:
            dist = abs(point[0] - prev_point[0]) + abs(point[1] - prev_point[1])
            if dist == min_dist:
                graph[prev_point].append(point)
                graph[point].append(prev_point)
        min_dist = abs(point[0] - prev_point[0]) + abs(point[1] - prev_point[1])
        prev_point = point

    return graph

points = [(1, 3), (2, 2), (4, 1), (3, 4), (2, 4)]
result = create_graph(points)
print(result)
