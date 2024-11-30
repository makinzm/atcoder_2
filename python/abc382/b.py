n,d = map(int,input().split())
s = list(input())

last_at = n - 1
for i in range(d):
    while True:
        if s[last_at] == '@':
            s[last_at] = '.'
            break
        last_at -= 1
        if last_at < 0:
            break

print(''.join(s))

