n = int(input())
s = input()

ans_set = set()
previous_letter = ""
previous_num = 0

alpha_dict = {}

for i in range(n):
    if s[i] != previous_letter:
        previous_letter, previous_num = s[i], 1
    else:
        previous_num += 1
    
    if previous_letter in alpha_dict:
        alpha_dict[previous_letter] = max(alpha_dict[previous_letter], previous_num)
    else:
        alpha_dict[previous_letter] = previous_num

ans = 0
for k,v in alpha_dict.items():
    ans += v
print(ans)
