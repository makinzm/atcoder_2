count_managemnt = {}
value_managemnt = {}

n, t = map(int, input().split())

count_managemnt[0] = n
# O(n)
for i in range(n):
    value_managemnt[i] = 0

# O(t)
for i in range(t):
    a, b = map(int, input().split())
    a, b = a - 1, b
    # O(1)
    a_value = value_managemnt[a]
    # O(1)
    count_managemnt[a_value] -= 1
    # O(1)
    if count_managemnt[a_value] == 0:
        # O(1)
        count_managemnt.pop(a_value)
    if a_value + b in count_managemnt:
        # O(1)
        count_managemnt[a_value + b] += 1
    else:
        # O(1)
        count_managemnt[a_value + b] = 1
    # O(1)
    value_managemnt[a] += b

    print(len(count_managemnt))
    # print(f"\tcount_managemnt: {count_managemnt}")
    # print(f"\tvalue_managemnt: {value_managemnt}")
