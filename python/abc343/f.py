n, q = map(int, input().split())

a = list(map(int, input().split()))

ST_SIZE = 1 << (n - 1).bit_length()
data = [{} for _ in range(2 * ST_SIZE - 1)]

# O(n)
for i in range(n):
    # 自分がもつ値の中で 最大のものを二種類 値と個数を持つ
    data[i + ST_SIZE - 1] = {a[i] : 1}

def concat(a, b):
    """Return only max 2 items. O(1) because the number of items is always 2."""
    c = {}
    for k, v in a.items():
        c[k] = v
    for k, v in b.items():
        if k in c:
            c[k] += v
        else:
            c[k] = v
    if len(c) > 2:
        c = dict(sorted(c.items(), key=lambda x: x[0], reverse=True)[:2])
    return c

for i in range(ST_SIZE - 2, -1, -1):
    data[i] = concat(data[i * 2 + 1], data[i * 2 + 2])

def change(p, x) -> None:
    """O(log n)"""
    p += ST_SIZE - 1
    data[p] = {x : 1}
    while p > 0:
        p = (p - 1) // 2
        data[p] = concat(data[p * 2 + 1], data[p * 2 + 2])

def output(a, b, k, l, r) -> dict:
    """O(log n)
    [a, b) についての答えを返す
    """
    if r <= a or b <= l:
        return {}
    if a <= l and r <= b:
        return data[k]
    else:
        vl = output(a, b, k * 2 + 1, l, (l + r) // 2)
        vr = output(a, b, k * 2 + 2, (l + r) // 2, r)
        return concat(vl, vr)
    

# print(f"Inital: {data}")

for _ in range(q):
    status, p, x = map(int, input().split())
    if status == 1:
        p -= 1
        # O(log n)
        change(p, x)
        # print(f"Changed: {data}")
    else:
        p, x = p - 1 , x
        # O(log n)
        ans = output(p, x, 0, 0, ST_SIZE)
        # print(f"Length: {len(ans)}")
        # print(f"Answer: {ans}")
        if len(ans) == 0:
            print(0)
        elif len(ans) == 1:
            print(0)
        else:
            print(sorted(ans.items(), key=lambda x: x[0], reverse=True)[:2][1][1])
