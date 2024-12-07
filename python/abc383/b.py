h,w,d = map(int, input().split())
s = [input() for _ in range(h)]

current_max = -1
floors = []

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            floors.append((i,j))

from more_itertools import distinct_combinations

for comb in distinct_combinations(floors, 2):
    x1, y1 = comb[0]
    x2, y2 = comb[1]
    current = 0
    for i in range(h):
        for j in range(w):
            if (i,j) not in floors:
                continue
            if (i,j) not in [comb[0], comb[1]]:
                if abs(x1 - i) + abs(y1 - j) <= d:
                    current += 1
                elif abs(x2 - i) + abs(y2 - j) <= d:
                    current += 1
            else:
                current += 1
    current_max = max(current_max, current)

print(current_max)
