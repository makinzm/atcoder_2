n,r = map(int,input().split())
da_list = [list(map(int,input().split())) for _ in range(n)]

current = r

for i in range(n):
    d,a = da_list[i]
    left,right = -1, -1
    if d == 1:
        left = 1600
        right = 2799
    elif d == 2:
        left = 1200
        right = 2399
    assert left != -1 and right != -1
    if left <= current <= right:
        current += a

print(current)


