## I have to create graph Union-find-tree
n,q = list(map(int,input().split()))

ops = []
for _ in range(q):
    ops.append(list(map(int,input().split())))

graphs = {}

for i in range(q):
    op = ops[i]
    a = op[1] - 1
    b = op[2] - 1
    if op[0] == 1:
        if a in graphs.keys():
            graphs[a].add(b)
        else:
            graphs[a] = set([b])
    elif op[0] == 2:
        if a in graphs.keys():
            try:
                graphs[a].remove(b)
            except KeyError:
                pass
        else:
            graphs[a] = set([])
    elif op[0] == 3:
        flag = False
        if a in graphs.keys() and b in graphs.keys():
            if b in graphs[a] and a in graphs[b]:
                print("Yes")
                flag = True
        if not flag:
            print("No")
