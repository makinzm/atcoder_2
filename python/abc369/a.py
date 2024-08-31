a,b = map(int, input().split())

ans = -1

if a == b:
    ans = 1
elif a % 2 == b % 2:
    ans = 3
else:
    ans = 2

print(ans)

