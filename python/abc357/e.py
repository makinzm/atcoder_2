import sys
sys.setrecursionlimit(10**8)

n = int(input())
a = list(map(int, input().split()))

class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children = []
        self.peers = []

    def add_child(self, child):
        self.children.append(child)

    def set_peers(self, peers):
        self.peers = peers

nodes = [Node(i, None) for i in range(n)]
cycles = []

for i in range(n):
    nodes[i].parent = nodes[a[i] - 1]
    nodes[a[i] - 1].add_child(nodes[i])
    # If the parent already appears, this may create a cycle
    if a[i] - 1 <= i:
        parent = nodes[a[i] - 1]
        is_cycle = False
        maybe_cycle = [parent]
        while parent:
            if parent.value == i:
                is_cycle = True
                break
            if len(parent.peers) > 0:
                is_cycle = False
                break
            parent = parent.parent
            maybe_cycle.append(parent)
        if is_cycle:
            for node in maybe_cycle:
                node.peers = maybe_cycle
                cycles.append(node)

visited = [ False for _ in range(n) ]
ans = 0

DEBUG = False

def dfs(node, count):
    if visited[node.value]:
        return
    visited[node.value] = True

    global ans
    if len(node.peers) > 0:
        count = len(node.peers)
        ans += count
    else:
        count += 1
        ans += count

    if DEBUG:
        print(f"node: {node.value}, count: {count}")

    for child in node.children:
        dfs(child, count)

for cycle_node in cycles:
    dfs(cycle_node, 0)

print(ans)


