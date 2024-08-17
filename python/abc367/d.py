from collections import defaultdict


n, m = map(int,input().split())
a = list(map(int, input().split()))

current_dict = defaultdict(int)
current_end_mod = 0

for i in range(n):
    current_end_mod += a[i]
    current_end_mod %= m
    current_dict[current_end_mod] += 1

ans = 0
current_start_mod = 0

for i in range(n):
    # Exclude self point from (i) to (i + n)
    current_dict[current_end_mod] -= 1
    ans += current_dict[current_start_mod]
    current_dict[current_end_mod] += 1
    ## Remove point from (i) to (i+1)
    ## Proceed starting point
    current_start_mod += a[i]
    current_start_mod %= m
    current_dict[current_start_mod] -= 1
    # Proceed ending point
    current_end_mod += a[i]
    current_end_mod %= m
    current_dict[current_end_mod] += 1

print(ans)

