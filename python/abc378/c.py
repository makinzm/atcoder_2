n = int(input())
a = list(map(int, input().split()))

the_last_value_to_index = dict()
ans_dict_index_to_pre = [-1 for _ in range(n)]

for i in range(n):
    a_value = a[i]
    if a_value in the_last_value_to_index:
        ans_dict_index_to_pre[i] = the_last_value_to_index[a_value] + 1
    the_last_value_to_index[a_value] = i

ans = " ".join(map(str, ans_dict_index_to_pre))
print(ans)

