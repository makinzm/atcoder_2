n = int(input())
a = list(map(int, input().split()))

count = 0
while True:
    a = sorted(a, reverse=True)
    if a[1] <= 0:
        break
    a[0] -= 1
    a[1] -= 1
    count += 1

print(count)
