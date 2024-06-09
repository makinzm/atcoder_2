N = int(input())

MOD = 998244353

def f(n, i):
    if i <= 0:
        raise ValueError("i must be positive")
    if i == 1:
        return n % MOD
    else:
        k = len(str(n))
        if i % 2 == 0:
            left_side = f(n, i // 2) % MOD
            left_base = (10 ** (k * (i // 2))) % MOD
            right_side = f(n, i // 2) % MOD
            return ((left_side * left_base) % MOD + right_side) % MOD
        else:
            left_side = f(n, i-1) % MOD
            left_base = (10 ** k) % MOD
            return ((left_side * left_base) % MOD + n) % MOD

print(f(N, N))


