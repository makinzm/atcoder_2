n = int(input())
tv_s = [list(map(int, input().split())) for _ in range(n)]

current = 0
current_i = 0
for ind, i in enumerate(range(tv_s[-1][0] + 1)):
    current = max(current -1, 0)
    if i == tv_s[current_i][0]:
        current += tv_s[current_i][1]
        current_i += 1

print(current)

