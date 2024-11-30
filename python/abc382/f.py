h,w,n = map(int,input().split())
rcl_list = [list(map(int,input().split())) for _ in range(n)]

rcl_descending_with_index = sorted(enumerate(rcl_list), key=lambda x: x[1][0], reverse=True)

ans = {}
current_height = [h] * w

debug = False

for i, (r, c, l) in rcl_descending_with_index:
    flag = True
    min_diff = 10**9
    for x in range(c - 1, c + l - 1):
        if current_height[x] <= r:
            flag = False
            break
        min_diff = min(min_diff, current_height[x] - r)
    if flag:
        for x in range(c - 1, c + l - 1):
            current_height[x] -= 1
        ans[i] = r + min_diff
    else:
        ans[i] = r

    if debug:
        print(f"{r=}, {c=}, {l=}, {flag=}, {current_height=}")
        print(f"{ans=} {min_diff=}")

for i in range(n):
    print(ans[i])

