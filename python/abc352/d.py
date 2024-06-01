from atcoder.segtree import SegTree

n,k = map(int, input().split())
p = list(map(int, input().split()))

dict_p = {p[i]:i+1 for i in range(n)}
sorted_p = [dict_p[i] for i in range(1,n+1)]

seg_tree_max = SegTree(op = max, e = 0, v = sorted_p)
seg_tree_min = SegTree(op = min, e = n, v = sorted_p)

min_value = n
for i in range(n-k+1):
    i_k = seg_tree_max.prod(i,i+k)
    i_1 = seg_tree_min.prod(i,i+k)
    min_value = min(min_value, i_k-i_1)

print(min_value)

