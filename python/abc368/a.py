n, k = map(int, input().split())
a = list(map(int, input().split()))

back = a[-k:]
front = a[:-k]

ans = back + front

print(*ans)
