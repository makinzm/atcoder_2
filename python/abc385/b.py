h,w,x,y = map(int, input().split())

x,y = x-1,y-1

s = [input() for _ in range(h)]
t = input()

current = 0

def can_move(x,y):
    return 0 <= x < h and 0 <= y < w and s[x][y] != "#"

visited = [[False]*w for _ in range(h)]

if s[x][y] == "@":
    current += 1

visited[x][y] = True

mapping = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

DEBUG = False

for i in range(len(t)):
    move = mapping[t[i]]
    tmp_x,tmp_y = x+move[0],y+move[1]
    if DEBUG:
        print(tmp_x,tmp_y,t[i])
        print(s[tmp_x][tmp_y])
    if can_move(tmp_x,tmp_y):
        x,y = tmp_x,tmp_y
        if not visited[x][y]:
            visited[x][y] = True
            if s[x][y] == "@":
                current += 1
    if DEBUG:
        print(x+1,y+1,current)

print(x+1,y+1,current)
