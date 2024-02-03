n = int(input())
a = list(map(int, input().split()))

current = 0
min_state = 0
for i in range(n):
    current += a[i]
    min_state = min(min_state, current)

print(-min_state + current)
