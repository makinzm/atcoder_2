import math
from collections import defaultdict

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n, x = map(int, input().split())
p = list(map(int, input().split()))

what_number = defaultdict(int)
for i in range(n):
    what_number[i] = comb(n, i)

