n,m,x,y = map(int,input().split())
xy = [list(map(int,input().split())) for _ in range(n)]
dc = [list(input().split()) for _ in range(m)]

mapping = {'U':(0,1), 'D':(0,-1), 'L':(-1,0), 'R':(1,0)}

from collections import defaultdict

from bisect import bisect_left, bisect_right

rows = defaultdict(set)
cols = defaultdict(set)

gyakubiki = dict()

for i in range(n):
    rows[xy[i][1]].add(xy[i][0])
    cols[xy[i][0]].add(xy[i][1])
    gyakubiki[tuple(xy[i])] = i

ans = 0

DEBUG = False

if DEBUG:
    print(f"{x=}, {y=}")
    print(f"{xy=}")
    print(f"{dc=}")
    print(f"{gyakubiki=}")

for i in range(m):
    d, c = dc[i]
    mx, my = mapping[d]
    c = int(c)
    if mx == 0:
        candidates = cols[x]
        current = y
        next = y + my * c
        y = next
        if current >= next:
            current, next = next, current
    else:
        candidates = rows[y]
        current = x
        next = x + mx * c
        x = next
        if current >= next:
            current, next = next, current

    # find left and right
    sorted_candidates = sorted(list(candidates))
    left = bisect_left(sorted_candidates, current)
    right = bisect_right(sorted_candidates, next)
    ans += max(0, right - left)
    if right - left > 0:
        for point in sorted_candidates[left:right]:
            if mx == 0:
                dot = gyakubiki[(x, point)]
            else:
                dot = gyakubiki[(point, y)]
            rows[xy[dot][1]].remove(xy[dot][0])
            cols[xy[dot][0]].remove(xy[dot][1])
    if DEBUG:
        print(f"{d=}, {c=}, {x=}, {y=}, {ans=}, {mx=}, {my=}, {current=}, {next=}, {left=}, {right=}, {sorted_candidates=}")
print(x,y,ans)
