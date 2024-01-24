"""D Problems."""
s = input()

bit_count_dict = {}
state = 0
ans = 0
bit_count_dict[state] = 1
for c in s:
    state ^= 1 << (int(c))
    if state not in bit_count_dict:
        bit_count_dict[state] = 1
    else:
        ans += bit_count_dict[state]
        bit_count_dict[state] += 1

print(ans)
