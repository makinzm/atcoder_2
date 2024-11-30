n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_with_index_desc = sorted([(b[i], i) for i in range(m)], reverse=True)
b_who_eat = [-1] * m
first_b_index = 0

last_a_index = 0
for i in range(m):
    value_b, index_b = b_with_index_desc[i]
    for j in range(last_a_index, n):
        if value_b >= a[j]:
            b_who_eat[index_b] = j + 1
            last_a_index = j
            break
        if j == n - 1:
            last_a_index = n - 1

[print(b_who_eat[i]) for i in range(m)]
