h,w,n = map(int, input().split())
T = input()
s = ""
for i in range(h):
    s += input()

directory_map = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1)
}

directories = []
for i in range(n):
    directories.append(directory_map[T[i]])

ans = 0

for i in range(h):
    for j in range(w):
        next_i, next_j = i, j
        ok = 1
        if s[i*w+j] == ".":
            for n_step in range(n):
                move = directories[n_step]
                next_i += move[1]
                next_j += move[0]
                if not (0 <= next_i < h and 0 <= next_j < w) or s[next_i*w+next_j] == "#":
                    ok = 0
                    break
            ans += ok

print(ans)
