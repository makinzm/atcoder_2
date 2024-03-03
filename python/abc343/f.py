n, q = map(int, input().split())

a = list(map(int, input().split()))

NEG_VALUE_2 = -2
NEG_VALUE = -1

ST_SIZE = 1 << (n - 1).bit_length()
data = [(NEG_VALUE, 0, NEG_VALUE_2, 0) for _ in range(2 * ST_SIZE - 1)]

# O(n)
for i in range(n):
    # 自分がもつ値の中で 最大のものを二種類 値と個数を持つ
    data[i + ST_SIZE - 1] = (a[i], 1, NEG_VALUE, 0)

def concat(a, b):
    """Return only max 2 items. O(1) because the number of items is always 2."""
    # print(f"a: {a}, b: {b}")
    a_index = 0
    b_index = 0
    first_value = -1
    first_count = 0
    if a[a_index] > b[b_index]:
        first_value = a[a_index]
        first_count += a[a_index + 1]
        a_index += 2
    elif a[a_index] < b[b_index]:
        first_value = b[b_index]
        first_count += b[b_index + 1]
        b_index += 2
    else:
        first_value = a[a_index]
        first_count += a[a_index + 1] + b[b_index + 1]
        a_index += 2
        b_index += 2
    second_value = -2
    second_count = 0
    if a[a_index] > b[b_index]:
        second_value = a[a_index]
        second_count += a[a_index + 1]
    elif a[a_index] < b[b_index]:
        second_value = b[b_index]
        second_count += b[b_index + 1]
    else:
        second_value = a[a_index]
        second_count += a[a_index + 1] + b[b_index + 1]
    return (first_value, first_count, second_value, second_count)

for i in range(ST_SIZE - 2, -1, -1):
    data[i] = concat(data[i * 2 + 1], data[i * 2 + 2])

def change(p, x) -> None:
    """O(log n)"""
    p += ST_SIZE - 1
    data[p] = (x, 1, NEG_VALUE, 0)
    while p > 0:
        p = (p - 1) // 2
        data[p] = concat(data[p * 2 + 1], data[p * 2 + 2])

def output(a, b, k, l, r) -> dict:
    """O(log n)
    [a, b) についての答えを返す
    """
    if r <= a or b <= l:
        return (NEG_VALUE, 0, NEG_VALUE_2, 0)
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
        if len(ans) == 0:
            raise ValueError("No answer")
        elif len(ans) == 1:
            print(0)
        else:
            print(ans[3])
