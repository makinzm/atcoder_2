DEBUG = False

n, s = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)

if s % sum_a != 0:
    s = s % sum_a
else:
    s = sum_a

a_with_twice = a + a

culmulative_sum = [0] * (2 * n + 1)

from collections import defaultdict

remainders = defaultdict(set)

remainders[0].add(0)

for i in range(2 * n):
    culmulative_sum[i + 1] = culmulative_sum[i] + a_with_twice[i]
    remainders[culmulative_sum[i + 1] % s].add(i + 1)


if DEBUG:
    print("s:", s)
    print('culmulative_sum:', culmulative_sum)
    print('remainders:', remainders)

from more_itertools import distinct_combinations

for i, remainder in remainders.items():
    if len(remainders[i]) < 2:
        continue
    for comb in distinct_combinations(remainder, 2):
        if DEBUG:
            print('comb:', comb)
        left_index, right_index = comb
        left_value = culmulative_sum[left_index]
        right_value = culmulative_sum[right_index]
        if abs(left_value - right_value) == s:
            print('Yes')
            exit()

print('No')
