N = int(input())
MOD = 998244353

def f(n, i):
    if i == 1:
        return n % MOD
    k = len(str(n))
    if i % 2 == 0:
        left_side = f(n, i // 2)
        left_base = pow(10, k * (i // 2), MOD)
        return (left_side * left_base + left_side) % MOD
    left_side = f(n, i - 1)
    left_base = pow(10, k, MOD)
    return (left_side * left_base + n) % MOD

print(f(N, N))

