n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

# Priority queue

import heapq

pq = []
heapq.heapify(pq)

for a, b in ab:
    heapq.heappush(pq, (a, b))

prev_dict = {}
# prev_dict[(a,b)] = The max value of u < a and v < b in visited
visited = [(0, 0)]

while pq:
    a, b = heapq.heappop(pq)
    prev_dict[(a, b)] = (0, 0)
    for u, v in visited:
        if u < a and v < b:
            prev_dict[(a, b)] = max(prev_dict[(a, b)], (u, v)) 
    visited.append((a, b))

pq = []
heapq.heapify(pq)

for a, b in ab:
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
