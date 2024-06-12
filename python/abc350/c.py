n = int(input())
a = list(map(int, input().split()))

index_to_value = {}
for i in range(n):
    index_to_value[i+1] = a[i]

value_to_index = {}
for i in range(n):
    value_to_index[a[i]] = i+1

ans_lst = []
for i in range(1, n+1):
    if index_to_value[i] != i:
        swapped_index = value_to_index[i]
        swapped_value = index_to_value[swapped_index]

        swapping_index = i
        swapping_value = index_to_value[swapping_index]

        index_to_value[swapping_index] = swapped_value
        index_to_value[swapped_index] = swapping_value
        value_to_index[swapping_value] = swapped_index
        value_to_index[swapped_value] = swapping_index

        ans_lst.append([swapping_index, swapped_index])

print(len(ans_lst))
for ans in ans_lst:
    print(*ans)
