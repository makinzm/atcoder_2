from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

positions = defaultdict(list)
for i, v in enumerate(a):
    positions[v].append(i)

total = 0
for value, position_list in positions.items():
    previous_position = -1
    for position in position_list:
        # The times when the position is the first time x The times when the distance from the last one
        # for example, 1 2 1 2 1 2 1 2 1 2
        # value = 1, position_list = [0, 2, 4, 6, 8]
        # value = 2, position_list = [1, 3, 5, 7, 9]
        # value = 1, position = 0, previous_position = -1, added_total = 1 * 10 = 10
        # [1], [1,2], [1,2,1], [1,2,1,2], [1,2,1,2,1], ..., [1,2,1,2,1,2,1,2,1,2]
        # value = 1, position = 2, previous_position = 0, added_total = 2 * 8 = 16
        # [-,2,1], [-,2,1,2], [-,2,1,2,1], [-,2,1,2,1,2], ..., [-,2,1,2,1,2,1,2,1,2]
        # [-,-,1], [-,-,1,2], [-,-,1,2,1], [-,-,1,2,1,2], ..., [-,-,1,2,1,2,1,2,1,2]
        total += (position - previous_position) * (n - position)
        previous_position = position

print(total)

