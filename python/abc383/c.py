import sys

sys.setrecursionlimit(10**7)

h,w,d = map(int, input().split())
s = [list(input()) for _ in range(h)]

start = set()
for i in range(h):
    for j in range(w):
        if s[i][j] == "H":
            start.add((i,j))
s_initial = [i.copy() for i in s]

move = [(1,0),(-1,0),(0,1),(0,-1)]

visited = start.copy()

def dfs(x,y):
    global ans, d
    for dx,dy in move:
        nx,ny = x+dx,y+dy

        if 0<=nx<h and 0<=ny<w:
            if s[nx][ny] == "H":
                continue
            elif s[nx][ny] == ".":
                s[nx][ny] = "#"
                if (nx,ny) not in visited:
                    visited.add((nx,ny))
                d -= 1
                if d > 0:
                    dfs(nx,ny)
                d += 1

for x,y in start:
    s = [i.copy() for i in s_initial]
    dfs(x,y)

print(len(visited))

