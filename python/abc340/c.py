n = int(input())

ans_dict = {}

def f(x):
    if x in ans_dict:
        return ans_dict[x]
    if x < 2:
        ans_dict[x] = 0
        return 0
    else:
        ans_dict[x] = f(x//2) + f(-(-x//2)) + x
        return ans_dict[x]

print(f(n))

