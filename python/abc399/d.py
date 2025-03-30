import sys
sys.setrecursionlimit(10**8)

t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    case = list(map(int, input().split()))
    cases.append(case)

# Test cases
# 1
# 3
# 1 2 1 3 2 3
# should be zero

# 1
# 2
# 1 2 1 2

def solve_case(case):
    first = -1
    chance_pairs = set()
    ans = 0
    first = case[0]
    before_pair = (-1, -1)

    for i in range(1, len(case)):
        smaller = min(first, case[i])
        larger = max(first, case[i])
        if smaller == larger:
            first = case[i]
            before_pair = (-1, -1)
            continue
        if (smaller, larger) in chance_pairs:
            ans += 1
            chance_pairs.remove((smaller, larger))
            first = case[i]
            before_pair = (-1, -1)
            continue
        chance_pairs.add(before_pair)
        before_pair = (smaller, larger)
        first = case[i]

    return ans

for case in cases:
    print(solve_case(case))

