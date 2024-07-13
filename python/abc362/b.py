a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ab = [b[0] - a[0], b[1] - a[1]]
ac = [c[0] - a[0], c[1] - a[1]]

cross_a = ab[0] * ac[0] + ab[1] * ac[1]
cross_b = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
cross_c = (b[0] - c[0]) * (a[0] - c[0]) + (b[1] - c[1]) * (a[1] - c[1])

if cross_a == 0 or cross_b == 0 or cross_c == 0:
    print("Yes")
else:
    print("No")

