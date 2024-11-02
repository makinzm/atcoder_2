h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, steps):
    global ans
    if steps == k:
        ans += 1
        return
    
    temp = s[x][y]
    s[x][y] = '#'
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.':
            dfs(nx, ny, steps + 1)
    
    # 戻ってきた時に元に戻す
    s[x][y] = temp

ans = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':  # 障害物でない場所をスタート地点にする
            dfs(i, j, 0)

print(ans)

