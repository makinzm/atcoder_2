n, m = map(int, input().split())

ans = []

debug = False

def dfs(a):
    if len(a) == n:
        if a[-1] <= m and a[-2] + 10 <= a[-1]:
            ans.append(a)
    else:
        current_available_maximum = max(m - (n - len(a) - 1) * 10, a[-1] + 10)
        if debug:
            print(f"{a=}, {current_available_maximum=}")
        for i in range(a[-1] + 10, current_available_maximum + 1):
            dfs(a + [i])

current_available_maximum = m - (n - 1) * 10
if debug:
    print(f"{current_available_maximum=}")
for i in range(1, current_available_maximum + 1):
    dfs([i])

sorted_ans = sorted(ans)
print(len(sorted_ans))
[print(" ".join(map(str, x))) for x in sorted_ans]
