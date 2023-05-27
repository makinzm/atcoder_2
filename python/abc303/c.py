n,m,h,k = map(int,input().split())
s = input()
xy = set()
for _ in range(m):
    _tmp = list(map(int,input().split()))
    xy.add(str(_tmp))

conversion = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
}

flag = True
x,y = 0,0

# 2 * 10^5
for i, d in enumerate(s):
    # print(i,h,x,y)
    h += -1
    if h <0:
        flag = False
        break
    tup_direction = conversion[d]
    x += tup_direction[0]
    y += tup_direction[1]
    # 2 * 10^5
    # ここを辞書にして最速にする.
    _tmp = str([x,y])
    if _tmp in xy and h < k:
        h = k
        xy.remove(_tmp)

print("Yes" if flag else "No")
