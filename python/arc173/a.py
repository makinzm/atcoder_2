t = int(input())

cases = []
for _ in range(t):
    case_i = int(input())
    cases.append(case_i)

def whether_neq(n: int):
    """
    return whether n is Neq Number
    """
    n_seq = list(str(n))
    previous = n_seq[0]
    for i in range(1, len(n_seq)):
        if n_seq[i] == previous:
            return False
        previous = n_seq[i]
    return True

"""
This problem is too difficult for me to solve.

So, I will list candidates of the answer which I know.

- DP: I think this problem doesn't have any state, so DP is not suitable.
- DFS, BFS: I think this problem doesn't have any graph structure, so DFS, BFS is not suitable.
- Greedy: This order is 10^12 >> 10^7, so I think greedy is not suitable.
- Math: There may be some mathematical properties of Neq Numbers but I can't find it.
- Segment Tree: I think this problem doesn't have any range query, so Segment Tree is not suitable.
- Binary Search: I need to find the mathematical properties of Neq Numbers to use Binary Search, so I can't use it.
- Bipartite, Flow, Matching: I think this problem doesn't have any graph structure, so these are not suitable.

"""

