h,w,n = list(map(int, input().split()))

state = [[0 for _ in range(w)] for _ in range(h)]

current_x = 0
current_y = 0
current_direction = 0
for i in range(n):
    b_or_w = state[current_x][current_y]
    state[current_x][current_y] ^= 1
    if b_or_w == 0:
        current_direction = (current_direction + 1) % 4
    else:
        current_direction = (current_direction + 3) % 4
    current_x = (current_x + [-1, 0, 1, 0][current_direction])%(h)
    current_y = (current_y + [0, 1, 0, -1][current_direction])%(w)

for i in range(h):
    print("".join(["#" if state[i][j] == 1 else "." for j in range(w)]))
