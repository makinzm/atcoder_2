n = int(input())
a = input()

def f(n, a):
    b = []
    costs = []
    for i in range(0, 3**n, 3):
        sub_group = a[i:i+3]
        cost = sub_group.count("1")
        costs.append(cost)
        if sub_group.count("1") > 1:
            b.append(1)
        else:
            b.append(0)
    return b, costs


