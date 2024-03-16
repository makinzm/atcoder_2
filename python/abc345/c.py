s = input()

count_dict = {}

for c in s:
    count_dict[c] = count_dict.get(c, 0) + 1

n = len(s)
ans = 0

for c in s:
    ans += n - count_dict[c] 

include_me = 0
for key in count_dict.keys():
    if count_dict[key] > 1:
        include_me = 1
        break

print(ans//2 + include_me)