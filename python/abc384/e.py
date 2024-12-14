h,w,x = map(int,input().split())
p,q = map(int,input().split())
map_list = [list(map(int,input().split())) for _ in range(h)]
p,q = p-1,q-1

moves = [(0,1),(0,-1),(1,0),(-1,0)]

import heapq

enemies = []

for move in moves:
    nx,ny = p,q
    nx,ny = nx+move[0],ny+move[1]
    if 0 <= nx < h and 0 <= ny < w:
        heapq.heappush(enemies,(map_list[nx][ny],nx,ny))

current = map_list[p][q]
map_list[p][q] = 0

debug = False

if debug:
    print('current:', current)

while enemies:
    enemy,nx,ny = heapq.heappop(enemies)
    enemy = map_list[nx][ny]
    if debug:
        print('enemy:', enemy)
        print("nx,ny:", nx,ny)
    if enemy == 0:
        continue
    if enemy * x < current:
        current += enemy
        map_list[nx][ny] = 0
        for move in moves:
            mx,my = nx,ny
            mx,my = mx+move[0],my+move[1]
            if 0 <= mx < h and 0 <= my < w:
                if map_list[mx][my] != 0:
                    heapq.heappush(enemies,(map_list[mx][my],mx,my))
        if debug:
            print('current:', current)
    else:
        continue

print(current)
