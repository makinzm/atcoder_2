n = int(input())
a = list(map(int, input().split()))

visited = [False] * n

ans = 0

i_pair = n-1

for i in range(n-1, -1, -1):
    if visited[i]:
        continue
    for j in range(i_pair, -1, -1):
        if visited[j]:
            continue
        if a[j] * 2 <= a[i]:
            ans += 1
            visited[j] = True
            visited[i] = True
            i_pair = j - 1
            break
        if j == 0:
            i_pair = -1

visited = [False] * n

ans_2 = 0

i_pair = 0

for i in range(n):
    if visited[i]:
        continue
    for j in range(i_pair, n):
        if visited[j]:
            continue
        if a[i] * 2 <= a[j]:
            ans_2 += 1
            visited[j] = True
            visited[i] = True
            i_pair = j + 1
            break
        if j == n-1:
            i_pair = n

ans = max(ans, ans_2)

print(ans)
