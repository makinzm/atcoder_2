from copy import deepcopy

h, w = list(map(int,input().split()))
s = []
for i in range(h):
    s.append(input())

visited = [[False for _ in range(w)] for _ in range(h)]
stuck = [[False for _ in range(w)] for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            visited[i][j] = True

init_visited = deepcopy(visited)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def is_over(x, y):
    return x < 0 or x >= h or y < 0 or y >= w

def dfs(x, y):
    """
    Solve the degree of freedom of (x, y) in the grid.
    if answer is 1, it means this point is stuck.
    """
    if visited[x][y]:
        return -1
    visited[x][y] = True
    if stuck[x][y]:
        return 1
    is_stuck = False
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_over(nx, ny):
            continue
        if s[nx][ny] == "#":
            is_stuck = True
            break
    if is_stuck:
        stuck[x][y] = True
        return 1
    else:
        next_all = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_over(nx, ny):
                continue
            next_ans = dfs(nx, ny)
            if next_ans != -1:
                next_all += next_ans
        return next_all + 1 # contain itself
                

ans = 0
for i in range(h):
    for j in range(w):
        if init_visited[i][j]:
            continue
        visited = deepcopy(init_visited)
        ans_candidate = dfs(i, j)
        if ans_candidate != -1:
            ans = max(ans, ans_candidate)
print(ans)
