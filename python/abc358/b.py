n, a = map(int, input().split())
t = list(map(int, input().split()))

current_time = 0

for i in range(n):
    if current_time < t[i]:
        current_time = t[i]

    current_time += a

    print(current_time)

