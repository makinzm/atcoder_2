DEBUG = False

n = int(input())

ans = 0

for a in range(1, 10**9):
    b_square = n // (2 ** a)
    b = int(b_square ** 0.5)
    if b == 0:
        break
    if DEBUG:
        print(f"{a=}, {b=}, {2**a * b**2=}, {n=}")
    if b % 2 == 0:
        ans += b // 2
    else:
        ans += 1 + b // 2

print(ans)

