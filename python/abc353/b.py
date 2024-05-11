n,k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
next_group = 0
current_empty = k

while next_group < n:
    while True:
        if a[next_group] <= current_empty:
            current_empty -= a[next_group]
            next_group += 1
            if next_group == n:
                break
        else:
            break
    count += 1
    current_empty = k

print(count)
