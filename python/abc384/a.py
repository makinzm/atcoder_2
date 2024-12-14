n,c,d = input().split()

n = int(n)

s = list(input())

for i in range(n):
    if s[i] != c:
        s[i] = d

print(''.join(s))
