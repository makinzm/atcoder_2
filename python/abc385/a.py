a = list(map(int, input().split()))

if a[0] == a[1] == a[2]:
    print('Yes')
    exit()

if a[0] == a[1] + a[2] or a[1] == a[0] + a[2] or a[2] == a[0] + a[1]:
    print('Yes')
    exit()

print('No')
