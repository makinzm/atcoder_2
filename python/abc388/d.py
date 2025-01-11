from atcoder import lazysegtree

n = int(input())
a = list(map(int, input().split()))

budgets = [0] * n

def op(x, y):
    return x + y

def mapping(func, ele):
    return func + ele

def composition(func1, func2):
    return func1 + func2

e = 0
id_ = 0

seg = lazysegtree.LazySegTree(op, e, mapping, composition, id_, budgets)

DEBUG = False

for i in range(n):
    num_given = seg.get(i)
    a[i] += num_given
    if i == n-1:
        break
    num_range = 0
    if a[i] >= n-i-1:
        if DEBUG:
            print(f"AA {a=}, {num_given=}, {num_range=}")
        num_range = n - 1 - i
    else:
        if DEBUG:
            print(f"BB {a=}, {num_given=}, {num_range=}")
        num_range = a[i]
    a[i] -= num_range
    seg.apply(i, num_range + i + 1, 1)
    if DEBUG:
        print(f"{a=}, {num_given=}, {num_range=}, {seg._d=}")

print(" ".join(map(str, a)))
