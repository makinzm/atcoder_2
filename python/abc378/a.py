a = list(map(int, input().split()))

the_same_count = dict()

for i in a:
    if i in the_same_count:
        the_same_count[i] += 1
    else:
        the_same_count[i] = 1

ans = 0
for key, value in the_same_count.items():
    if value > 1:
        ans += 1
    if value == 4:
        ans += 1

print(ans)
