import heapq

DEBUG = False

h, w = map(int, input().split())
s_global = [list(input().rstrip()) for _ in range(h)]
a,b,c,d = map(int, input().split())

visited = [[False] * w for _ in range(h)]
ans = 10**9

directions = {
    0: (1, 0),
    1: (-1, 0),
    2: (0, 1),
    3: (0, -1),
}

def print_visited():
    if DEBUG:
        for i in range(h):
            for j in range(w):
                if visited[i][j]:
                    print("O", end="")
                else:
                    print("X", end="")
            print()
        print()


def bfs(num_kic, x, y, s):
    global ans
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (num_kic, x, y, s))
    while queue:
        num_kic, x, y, s = heapq.heappop(queue)
        visited[x][y] = True 
        if num_kic >= ans:
            continue
        if DEBUG:
            print(f"{num_kic=}, {x=}, {y=}")
            print_visited()
        if (x, y) == (c-1, d-1):
            ans = min(ans, num_kic)
            if DEBUG:
                print(f"{ans=}")
                print_visited()
            continue
        for num_dir in range(4):
            dx, dy = directions[num_dir]
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if s[nx][ny] == "#":
                    s[nx][ny] = "."
                    nnx, nny = x + dx * 2, y + dy * 2
                    is_blocked = False
                    if 0 <= nnx < h and 0 <= nny < w:
                        if s[nnx][nny] == "#":
                            s[nnx][nny] = "."
                            is_blocked = True
                    heapq.heappush(queue, (num_kic + 1, nx, ny, s))
                    s[nx][ny] = "#"
                    if is_blocked:
                        s[nnx][nny] = "#"
                else:
                    heapq.heappush(queue, (num_kic, nx, ny, s))

bfs(0, a-1, b-1, s_global)

if ans == 10**9:
    print(-1)
else:
    if ans > 1:
        print(ans-1)
    else:
        print(ans)

