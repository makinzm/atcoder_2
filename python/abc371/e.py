from atcoder.segtree import SegTree

n = int(input())
a = list(map(int, input().split()))

seg = SegTree(
    op = lambda x, y: x | y,
    e = set(),
    v = [set([x]) for x in a]
)

ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        ans += len(seg.prod(i, j))

print(ans)

