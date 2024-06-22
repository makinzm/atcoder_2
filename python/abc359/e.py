n = int(input())
h = list(map(int, input().split()))

heights = [0] * n
current = 1

for i in range(n):
    should_add = False
    for j in reversed(range(i)):
        if heights[j] > h[i]:
            should_add = True
            break
    if not should_add:
        j = -1
    added = 0
    if j is not None:
        for k in range(j+1, i+1):
            if h[i] > heights[k]:
                added += h[i] - heights[k]
                heights[k] = h[i]
    current += added
    debug = False
    if debug:
        print(i, j)
        print(heights)
        print(added)
        print()
    print(current, end=" ")
print()


