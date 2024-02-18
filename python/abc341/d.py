n,m,k = map(int, input().split())

MAX_ANS = n * m * k + 1
MIN_ANS_LESS = 0

def gcd(x, y):
    """Return the greatest common divisor of x and y."""
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    """Return the least common multiple of x and y."""
    return (x * y) // gcd(x, y)

def solve(a):
    """Return the number which a include this constraint."""
    num_n = a // n
    num_m = a // m
    num_nm = a // lcm(n, m)
    return num_n + num_m - 2 * num_nm

while MAX_ANS - MIN_ANS_LESS > 1:
    mid = (MAX_ANS + MIN_ANS_LESS) // 2
    if solve(mid) >= k:
        MAX_ANS = mid
    else:
        MIN_ANS_LESS = mid

print(MAX_ANS)
