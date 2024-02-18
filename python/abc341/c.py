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
        i_0, j_0 = i, j
        next_i, next_j = i, j
        if s[i*w+j] == ".":
            for n_step in range(n):
                next_i += directories[n_step][1]
                next_j += directories[n_step][0]
                if next_i < 0 or next_i >= h or next_j < 0 or next_j >= w:
                    break
                if s[next_i*w+next_j] == "#":
                    break
            if n_step == n-1:
                ans += 1

print(ans)
