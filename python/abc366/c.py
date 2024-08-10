q = int(input())

queries = [list(map(int, input().split())) for _ in range(q)]

bag = dict()

for query in queries:
    if query[0] == 1:
        x = query[1]
        if x in bag:
            bag[x] += 1
        else:
            bag[x] = 1
    elif query[0] == 2:
        x = query[1]
        if x in bag:
            bag[x] -= 1
            if bag[x] == 0:
                bag.pop(x)
    else:
        print(len(bag))

