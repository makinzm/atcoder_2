from collections import deque

n = int(input())
s_list = []
visited_matrix = [[[[False for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]

for i in range(n):
    s_list.append(input())

for i in range(n):
    if "P" in s_list[i]:
        s_list[i] = s_list[i].replace("P", "Q", 1)
        break

for i in range(n):
    for j in range(n):
        if s_list[i][j] == "P":
            P_x = i
            P_y = j
        if s_list[i][j] == "Q":
            Q_x = i
            Q_y = j

queue = deque([(P_x, P_y, Q_x, Q_y, 0)])
ans_count = 2 ** 31 - 1

while len(queue) > 0:
    P_x, P_y, Q_x, Q_y, count = queue.popleft()
    count += 1
    if count >= ans_count:
        continue
    if visited_matrix[P_x][P_y][Q_x][Q_y]:
        continue
    visited_matrix[P_x][P_y][Q_x][Q_y] = True
    for i in range(4):
        new_P_x = P_x + [-1, 0, 1, 0][i]
        new_P_y = P_y + [0, 1, 0, -1][i]
        new_Q_x = Q_x + [-1, 0, 1, 0][i]
        new_Q_y = Q_y + [0, 1, 0, -1][i]
        if new_P_x < 0 or new_P_x >= n or new_P_y < 0 or new_P_y >= n:
            new_P_x , new_P_y = P_x, P_y
        elif s_list[new_P_x][new_P_y] == "#":
            new_P_x , new_P_y = P_x, P_y
        if new_Q_x < 0 or new_Q_x >= n or new_Q_y < 0 or new_Q_y >= n:
            new_Q_x , new_Q_y = Q_x, Q_y
        elif s_list[new_Q_x][new_Q_y] == "#":
            new_Q_x , new_Q_y = Q_x, Q_y
        if new_P_x == new_Q_x and new_P_y == new_Q_y:
            ans_count = min(ans_count, count)
        else:
            queue.append((new_P_x, new_P_y, new_Q_x, new_Q_y, count))

print(ans_count if ans_count != 2 ** 31 - 1 else -1)
