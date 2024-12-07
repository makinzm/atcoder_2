from collections import deque

DEBUG = False

h,w,d = map(int, input().split())
s = [list(input()) for _ in range(h)]

start = set()
for i in range(h):
    for j in range(w):
        if s[i][j] == "H":
            start.add((i,j))

move = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(list_xyd):
    q = deque(list_xyd)
    dist = [[-1]*w for _ in range(h)]
    for x,y,power in list_xyd:
        dist[x][y] = 0
    while q:
        x,y,power = q.popleft()
        if power == 0:
            continue
        for dx,dy in move:
            nx,ny = x+dx,y+dy
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1 and s[nx][ny] == ".":
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx,ny,power-1))
    return dist

list_xyd = []
for x,y in start:
    list_xyd.append((x,y,d))

dist = bfs(list_xyd)

if DEBUG:
    for i in range(h):
        [print(str(dist[i][j]).ljust(3), end=" ") for j in range(w)]
        print()

ans = 0
for i in range(h):
    for j in range(w):
        if dist[i][j] != -1:
            if dist[i][j] <= d:
                ans += 1
print(ans)
