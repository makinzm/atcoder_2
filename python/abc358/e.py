factorial_dict = {0: 1}

def factorial(n):
    if n in factorial_dict:
        return factorial_dict[n]
    factorial_dict[n] = n * factorial(n - 1)
    return factorial_dict[n]

k = int(input())
c = list(map(int, input().split()))

MOD = 998244353
ans = 0

# すべての可能な組み合わせを探索する
for i in range(1, 1 << 26):
    lst = []
    n = 0
    for j in range(26):
        if i & ((c[j] > 0) << j):
            lst.append(j)
            n += c[j]  # 選ばれた文字の個数を合計
    if n == 0:
        continue
    if n <= k:
        ans_base = factorial(n)
        if len(lst) > 1:
            for j in lst:
                ans_base //= factorial(c[j])
    else:
        ans_base = 0

    ans = (ans + ans_base) % MOD

    print(ans)
    print(lst, n, bin(i), ans_base)
    if i > 100:
        break

print(ans)

