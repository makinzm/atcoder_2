n, q = map(int, input().split())
t = list(map(int, input().split()))

start = [ 1 for _ in range(n) ]

for i in t:
    if start[i-1] == 1:
        start[i-1] = 0
    else:
        start[i-1] = 1

print(sum(start))
