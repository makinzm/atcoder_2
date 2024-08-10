n, d = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]

xy_transformed = [(x + y, x - y) for x, y in xy]

max_sum = max(x + y for x, y in xy)
min_sum = min(x + y for x, y in xy)
max_diff = max(x - y for x, y in xy)
min_diff = min(x - y for x, y in xy)

count = 0

for x_plus_y in range(min_sum - d, max_sum + d + 1):
    for x_minus_y in range(min_diff - d, max_diff + d + 1):
        if x_plus_y % 2 != x_minus_y % 2:
            continue
        total_distance = 0
        for xpy, xmy in xy_transformed:
            total_distance += max(abs(x_plus_y - xpy), abs(x_minus_y - xmy))
        if total_distance <= d:
            count += 1
            # print(f"x_plus_y={x_plus_y}, x_minus_y={x_minus_y}")
            # print(f"total_distance={total_distance}")
            # print(f"x,y=({(x_plus_y + x_minus_y) // 2}, {(x_plus_y - x_minus_y) // 2})")
            # print()

print(count)
