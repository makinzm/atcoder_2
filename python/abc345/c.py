import itertools

s = input()

count_dict = {}

for c in s:
    count_dict[c] = count_dict.get(c, 0) + 1

ans = 0

for combi in itertools.combinations(count_dict.keys(), 2):
    ans += count_dict[combi[0]] * count_dict[combi[1]]

print(ans if len(count_dict) >= 2 else 1)
