n = int(input())

grids = [[0 for _ in range(n)] for _ in range(n)]

current = [0,0]
grids[current[0]][current[1]] = 1

current_move = 1
i = 2
while(i <= n**2-1):
    if current_move == 1:
        try:
            if current[0] + 1 < n and grids[current[0]+1][current[1]] == 0:
                current[0] += 1
                grids[current[0]][current[1]] = i
                i += 1
            else:
                current_move = 2
        except IndexError:
            current_move = 2
    elif current_move == 2:
        try:
            if current[1] + 1 < n and grids[current[0]][current[1]+1] == 0:
                current[1] += 1
                grids[current[0]][current[1]] = i
                i += 1
            else:
                current_move = 3
        except IndexError:
            current_move = 3
    elif current_move == 3:
        try:
            if current[0] - 1 >= 0 and grids[current[0]-1][current[1]] == 0:
                current[0] -= 1
                grids[current[0]][current[1]] = i
                i += 1
            else:
                current_move = 4
        except IndexError:
            current_move = 4
    elif current_move == 4:
        try:
            if current[1] - 1 >= 0 and grids[current[0]][current[1]-1] == 0:
                current[1] -= 1
                grids[current[0]][current[1]] = i
                i += 1
            else:
                current_move = 1
        except IndexError:
            current_move = 1

takahashi_place = (n+1)//2
if grids[takahashi_place-1][takahashi_place-1] == 0:
    grids[takahashi_place-1][takahashi_place-1] = "T"
else:
    raise Exception("Takahashi Error")

for i in range(n):
    for j in range(n):
        print(grids[i][j], end=" ")
    print()
