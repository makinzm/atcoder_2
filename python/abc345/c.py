s = input()

count_dict = {}

for c in s:
    count_dict[c] = count_dict.get(c, 0) + 1

n = len(s)
ans = 0

for c in s:
    ans += n - count_dict[c] 

print(ans//2 if len(count_dict) >= 2 else 1)
