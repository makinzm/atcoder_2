n = int(input())
s = []
for i in range(n):
    s.append(input())

ans = 0
for i in range(n):
    if s[i] == "Takahashi":
        ans += 1

print(ans)

