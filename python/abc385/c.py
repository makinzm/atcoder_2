n = int(input())
h = list(map(int, input().split()))

from collections import defaultdict

h_dict = defaultdict(list)

for i, j in enumerate(h):
    h_dict[j].append(i)

ans = 0
for height, h_list in h_dict.items():
    bit_len_h_list = 2 ** len(h_list)
    for i in range(bit_len_h_list):
        tmp = 0
        last_one = 0
        tmp_sum = 1
        for j in range(len(h_list)):
            if i >> j & 1:
                if tmp == 0:
                    last_one = h_list[j]
                    tmp = -1
                elif tmp == -1:
                    tmp = h_list[j] - last_one
                    last_one = h_list[j]
                    tmp_sum += 1
                else:
                    if h_list[j] - last_one != tmp:
                        continue
                    else:
                        tmp_sum += 1
        ans = max(ans, tmp_sum)
print(ans)

        
