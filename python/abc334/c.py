n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 2 * 10 ** 5

from_even_to_odd = [0] * ( -(-k // 2) )
from_odd_to_even = [0] * ( k // 2 )

for i in range(k):
    if i % 2 == 0 and i + 1 < k:
        from_even_to_odd[i // 2] = abs(a[i] - a[i + 1])
    elif i % 2 == 1 and i + 1 < k:
        from_odd_to_even[i // 2] = abs(a[i] - a[i + 1])

if k % 2 == 0:
    ans = sum(from_even_to_odd)
else:
    for i in range(k):
        ans = min(
                ans,
                sum(from_even_to_odd[:i // 2]) + sum(from_odd_to_even[i // 2:])
            )

print(ans)
