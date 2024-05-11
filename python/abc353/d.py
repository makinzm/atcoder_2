n = int(input())
a = list(map(int, input().split()))

current_sum = 0
answer_base = 0
mod = 998244353

for j in range(1, n):
    current_sum += a[j-1]
    base_base = (10 ** len(str(a[j])))
    base = a[j] * j + current_sum * base_base
    answer_base += base % mod

print(answer_base % mod)
