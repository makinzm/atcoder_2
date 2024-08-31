n = int(input())
a = list(map(int, input().split()))

ans = 0
current_count = 2

if n == 1:
    print(1)
    exit()

current_diff = a[1] - a[0]

if n == 2:
    print(3)
    exit()

for i in range(2, n):
    next_diff = a[i] - a[i-1]
    if current_diff != next_diff:
        ans += current_count * (current_count - 1) // 2
        current_count = 2
        current_diff = next_diff
    else:
        current_count += 1

if current_count > 1:
    ans += current_count * (current_count - 1) // 2

print(ans + n)
