n,m = map(int, input().split())

a = []
for _ in range(m):
    a.append(list(map(int, input().split())))

not_good_relationship = [[1 for _ in range(n)] for _ in range(n)]

for time in range(m):
    for human in range(n-1):
        not_good_relationship[a[time][human]-1][a[time][human+1]-1]=0
        not_good_relationship[a[time][human+1]-1][a[time][human]-1]=0

# for i in range(n):
#     print(i,not_good_relationship[i])

ans = 0
for i in range(n):
    for j in range(n):
        ans += not_good_relationship[i][j]

print(int((ans-n)/2))
