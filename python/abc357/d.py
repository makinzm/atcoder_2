import math
N = int(input())
MOD = 998244353

memo = {}

def f(n, i):
    if i == 1:
        return n % MOD

    if (n, i) in memo:
        return memo[(n, i)]

    k = int(math.log10(n)) + 1
    if i % 2 == 0:
        left_side = f(n, i // 2)
        left_base = pow(10, k * (i // 2), MOD)
        right_side = f(n, i // 2)
        result = (left_side * left_base + right_side) % MOD
    else:
        left_side = f(n, i - 1)
        left_base = pow(10, k, MOD)
        result = (left_side * left_base + n) % MOD

    memo[(n, i)] = result
    return result

print(f(N, N))

