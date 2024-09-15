n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

num_divided = 2
# Priority queue

def max_distance(s, t, aim):
    distance_s = abs(s[0] - aim[0]) + abs(s[1] - aim[1])
    distance_t = abs(t[0] - aim[0]) + abs(t[1] - aim[1])
    if distance_s > distance_t:
        return t
    else:
        return s

import heapq
from collections import defaultdict

pq = []
heapq.heapify(pq)

for a, b in ab:
    heapq.heappush(pq, (a, b))

prev_dict = {}
next_dict = defaultdict(list)
# prev_dict[(a,b)] = The max value of u < a and v < b in visited
visited = [(0, 0)]

while pq:
    a, b = heapq.heappop(pq)
    prev_dict[(a, b)] = (0, 0)
    for u, v in visited:
        if u < a and v < b:
            prev_dict[(a, b)] = max_distance(prev_dict[(a,b)], (u,v), (a,b))
    next_dict[prev_dict[(a, b)]].append((a,b))
    visited.append((a, b))

added_points = set()
added_next_points = defaultdict(list)

count = 0
while count < 4 * n:
    for previous_point, next_points in next_dict.items():
        if len(next_points) > 1:
            intermediator = (min(list(map(lambda xy: xy[0], next_points))), min(list(map(lambda xy: xy[1], next_points))))
            visited.append(intermediator)
            added_points.add(intermediator)
            for point in next_points:
                prev_dict[point] = intermediator
                added_next_points[intermediator].append(point)
            prev_dict[intermediator] = previous_point
            count += 1
            if count >= 4 * n:
                break
    break

third_added_next_points = defaultdict(list)

while count <= 4 * n - 2:
    for great_point, next_points in added_next_points.items():
        if len(next_points) > 2:
            num_index = min(1, len(next_points)// num_divided)
            first_group = next_points[:num_index]
            second_group = next_points[num_index:]
            first_intermediator = (min(list(map(lambda xy: xy[0], first_group))), min(list(map(lambda xy: xy[1], first_group))))
            second_intermediator = (min(list(map(lambda xy: xy[0], second_group))), min(list(map(lambda xy: xy[1], second_group))))
            visited.append(first_intermediator)
            visited.append(second_intermediator)
            for point in first_group:
                prev_dict[point] = first_intermediator
                third_added_next_points[first_intermediator].append(point)
            prev_dict[first_intermediator] = great_point
            for point in second_group:
                prev_dict[point] = second_intermediator
                third_added_next_points[second_intermediator].append(point)
            prev_dict[second_intermediator] = great_point
            count += 2
            if count > 4 * n - 1:
                break
    break

def next_generation(added_next_points):
    global count
    while True:
        num_updated = 0
        next_generation_added_next_points = defaultdict(list)
        for great_point, next_points in added_next_points.items():
            if len(next_points) > 2:
                num_index = min(1, len(next_points) // num_divided)
                first_group = next_points[:num_index]
                second_group = next_points[num_index:]
                first_intermediator = (min(list(map(lambda xy: xy[0], first_group))), min(list(map(lambda xy: xy[1], first_group))))
                second_intermediator = (min(list(map(lambda xy: xy[0], second_group))), min(list(map(lambda xy: xy[1], second_group))))
                visited.append(first_intermediator)
                visited.append(second_intermediator)
                for point in first_group:
                    prev_dict[point] = first_intermediator
                    next_generation_added_next_points[first_intermediator].append(point)
                prev_dict[first_intermediator] = great_point
                for point in second_group:
                    prev_dict[point] = second_intermediator
                    next_generation_added_next_points[second_intermediator].append(point)
                prev_dict[second_intermediator] = great_point
                count += 2
                num_updated += 1
            if count >= 4 * n - 1:
                break
        if count >= 4 * n - 1:
            break
        if num_updated == 0:
            break


next_generation(third_added_next_points)

pq = []
heapq.heapify(pq)

for a, b in visited:
    if a == 0 and b == 0:
        continue
    heapq.heappush(pq, (a, b))

visited = {(0, 0)}
answers = []
already_answerd = set()
while pq:
    a, b = heapq.heappop(pq)
    if prev_dict[(a, b)] in visited:
        candidate = (*prev_dict[(a, b)], a, b)
        if candidate in already_answerd:
            continue
        already_answerd.add(candidate)
        answers.append(candidate)
        visited.add((a, b))
    else:
        raise ValueError(f"prev_dict[{(a, b)}] = {prev_dict[(a, b)]} not in visited")

print(len(answers))

[print(*ans) for ans in answers]
