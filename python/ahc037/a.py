n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

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

count = 0
while count < 4 * n:
    for previous_point, next_points in next_dict.items():
        if len(next_points) > 1:
            intermediator = (min(list(map(lambda xy: xy[0], next_points))), min(list(map(lambda xy: xy[1], next_points))))
            visited.append(intermediator)
            for point in next_points:
                prev_dict[point] = intermediator
            prev_dict[intermediator] = previous_point
            count += 1
    break

pq = []
heapq.heapify(pq)

for a, b in visited:
    if a == 0 and b == 0:
        continue
    heapq.heappush(pq, (a, b))

visited = {(0, 0)}
answers = []
while pq:
    a, b = heapq.heappop(pq)
    if prev_dict[(a, b)] in visited:
        answers.append((*prev_dict[(a, b)], a, b))
        visited.add((a, b))
    else:
        raise ValueError(f"prev_dict[{(a, b)}] = {prev_dict[(a, b)]} not in visited")

print(len(answers))

[print(*ans) for ans in answers]
